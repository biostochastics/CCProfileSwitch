"""Configuration management for CC Profile Switch."""

import json
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from platformdirs import user_config_dir as platform_user_config_dir
except ImportError:  # pragma: no cover - fallback for minimal environments
    platform_user_config_dir = None  # type: ignore[assignment]
from rich.console import Console

console = Console()


def _user_config_dir(app_name: str) -> str:
    if platform_user_config_dir is not None:
        return platform_user_config_dir(app_name)
    return str(Path.home() / f".{app_name}")


class Config:
    """Manages application configuration."""

    def __init__(self):
        self.app_name = "claude"
        self.config_dir = Path(_user_config_dir(self.app_name))
        self.config_file = self.config_dir / "config.json"
        self.default_config = {
            "active_token_target": {
                "type": "file",
                "path": str(self.config_dir / ".credentials.json"),
            },
            "default_profile": None,
            "auto_switch": False,
            "show_token_warning": True,
            "mask_tokens": True,
        }

    def ensure_config_dir(self) -> None:
        """Ensure the configuration directory exists."""
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file."""
        try:
            if self.config_file.exists():
                with open(self.config_file, "r") as f:
                    config = json.load(f)
                # Merge with defaults to ensure all keys exist
                return {**self.default_config, **config}
            else:
                return self.default_config.copy()
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load config: {e}[/yellow]")
            return self.default_config.copy()

    def save_config(self, config: Dict[str, Any]) -> bool:
        """Save configuration to file."""
        try:
            self.ensure_config_dir()
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=2)
            return True
        except Exception as e:
            console.print(f"[red]Error saving config: {e}[/red]")
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        config = self.load_config()
        return config.get(key, default)

    def set(self, key: str, value: Any) -> bool:
        """Set a configuration value."""
        config = self.load_config()
        config[key] = value
        return self.save_config(config)

    def get_active_token_path(self) -> str:
        """Get the path where the active token should be stored."""
        config = self.load_config()
        target = config.get(
            "active_token_target", self.default_config["active_token_target"]
        )
        return target.get("path", str(self.config_dir / ".credentials.json"))

    def set_active_token_target(self, target_type: str, path: str) -> bool:
        """Set the active token target."""
        return self.set("active_token_target", {"type": target_type, "path": path})

    def get_default_profile(self) -> Optional[str]:
        """Get the default profile name."""
        return self.get("default_profile")

    def set_default_profile(self, profile_name: Optional[str]) -> bool:
        """Set the default profile name."""
        return self.set("default_profile", profile_name)

    def is_auto_switch_enabled(self) -> bool:
        """Check if auto-switch is enabled."""
        return self.get("auto_switch", False)

    def set_auto_switch(self, enabled: bool) -> bool:
        """Enable or disable auto-switch."""
        return self.set("auto_switch", enabled)

    def should_show_token_warning(self) -> bool:
        """Check if token warnings should be shown."""
        return self.get("show_token_warning", True)

    def set_token_warning(self, enabled: bool) -> bool:
        """Enable or disable token warnings."""
        return self.set("show_token_warning", enabled)

    def should_mask_tokens(self) -> bool:
        """Check if tokens should be masked in output."""
        return self.get("mask_tokens", True)

    def set_token_masking(self, enabled: bool) -> bool:
        """Enable or disable token masking."""
        return self.set("mask_tokens", enabled)

    def get_config_path(self) -> str:
        """Return the configuration directory path."""
        return str(self.config_dir)

    def get_claude_settings_path(self) -> Path:
        """Get path to Claude Code settings.json file."""
        return Path.home() / ".claude" / "settings.json"

    def _read_json(self, path: Path) -> dict:
        """Read JSON file safely, returning {} if not found."""
        if not path.exists():
            return {}
        try:
            with open(path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            console.print(f"[yellow]Warning: Could not read {path}: {e}[/yellow]")
            return {}

    def _write_json_atomic(self, path: Path, data: dict) -> bool:
        """Write JSON atomically using temp file."""
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(
                "w", dir=str(path.parent), delete=False, suffix=".json"
            ) as tmp_file:
                json.dump(data, tmp_file, indent=2)
                temp_path = Path(tmp_file.name)
            temp_path.replace(path)
            return True
        except Exception as e:
            console.print(f"[red]Error writing {path}: {e}[/red]")
            return False

    def get_claude_settings_env(self) -> dict:
        """Read environment variables from Claude settings.json."""
        settings_path = self.get_claude_settings_path()
        settings = self._read_json(settings_path)
        return settings.get("env", {})

    def update_claude_settings(
        self, env_vars: dict, remove_keys: Optional[List[str]] = None
    ) -> bool:
        """Update Claude Code settings.json with environment variables.

        Args:
            env_vars: Dictionary of environment variables to set
            remove_keys: List of keys to remove from environment

        Returns:
            True if successful, False otherwise
        """
        settings_path = self.get_claude_settings_path()

        # Backup settings if they're malformed
        settings = self._read_json(settings_path)
        if settings_path.exists() and not settings:
            backup_path = settings_path.with_suffix(".json.bak")
            try:
                import shutil

                shutil.copy2(settings_path, backup_path)
                console.print(
                    f"[yellow]Backed up malformed settings to {backup_path}[/yellow]"
                )
            except Exception:
                pass

        # Ensure env dict exists
        if "env" not in settings or not isinstance(settings["env"], dict):
            settings["env"] = {}

        # Update environment variables, converting OAuth JSON strings to objects
        for key, value in env_vars.items():
            if key == "ANTHROPIC_AUTH_TOKEN" and isinstance(value, str):
                # Check if value is a JSON-serialized OAuth token
                if value.strip().startswith("{"):
                    try:
                        # Parse the JSON string to an object so Claude Code can use it
                        parsed = json.loads(value)
                        if "claudeAiOauth" in parsed:
                            settings["env"][key] = parsed
                        else:
                            settings["env"][key] = value
                    except json.JSONDecodeError:
                        # Not valid JSON, store as-is (probably a plain API key starting with {)
                        settings["env"][key] = value
                else:
                    # Plain API key
                    settings["env"][key] = value
            else:
                settings["env"][key] = value

        # Remove specified keys
        if remove_keys:
            for key in remove_keys:
                settings["env"].pop(key, None)

        return self._write_json_atomic(settings_path, settings)
