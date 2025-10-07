"""Secure storage module for Claude profiles using keyring."""

import json
import os
import stat
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

from .constants import PROVIDER_CLAUDE, PROVIDER_ZAI, ZAI_DEFAULT_API_URL

try:
    from platformdirs import user_config_dir as platform_user_config_dir
except ImportError:  # pragma: no cover - fallback for minimal environments
    platform_user_config_dir = None  # type: ignore[assignment]

import keyring
from filelock import FileLock
from rich.console import Console

console = Console()


def _user_config_dir(app_name: str) -> str:
    """Return the platform-specific config directory, with a simple fallback."""
    if platform_user_config_dir is not None:
        return platform_user_config_dir(app_name)
    return str(Path.home() / f".{app_name}")


class ProfileStorage:
    """Manages secure storage of Claude profiles using system keyring."""

    def __init__(self):
        self.service_name = "claude-profile-manager"
        self.app_name = "claude"
        self.config_dir = Path(_user_config_dir(self.app_name))
        self.credentials_file = self.config_dir / ".credentials.json"

    def ensure_config_dir(self) -> None:
        """Ensure the configuration directory exists."""
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def _normalize_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize profile data with defaults for backward compatibility."""
        # Set default provider if missing
        profile.setdefault("provider", PROVIDER_CLAUDE)

        # Set default API URL for Z-AI profiles
        if profile["provider"] == PROVIDER_ZAI:
            profile.setdefault("api_url", ZAI_DEFAULT_API_URL)

        return profile

    def save_profile(
        self,
        name: str,
        token: str,
        metadata: Optional[Dict[str, Any]] = None,
        provider: str = PROVIDER_CLAUDE,
        api_url: Optional[str] = None,
    ) -> bool:
        """Save a profile to the keyring.

        Args:
            name: Profile name
            token: API key or auth token
            metadata: Optional metadata dictionary
            provider: Provider name ("claude" or "zai")
            api_url: Optional API URL (defaults to Z-AI URL for zai provider)
        """
        try:
            profile_data = {
                "token": token,
                "provider": provider,
                "metadata": metadata or {},
            }

            # Add API URL for Z-AI or custom
            if provider == PROVIDER_ZAI:
                profile_data["api_url"] = api_url or ZAI_DEFAULT_API_URL
            elif api_url:
                profile_data["api_url"] = api_url

            keyring.set_password(
                self.service_name, f"profile_{name}", json.dumps(profile_data)
            )
            return True
        except Exception as e:
            console.print(f"[red]Error saving profile '{name}': {e}[/red]")
            return False

    def get_profile(self, name: str) -> Optional[Dict[str, Any]]:
        """Retrieve a profile from the keyring."""
        try:
            data = keyring.get_password(self.service_name, f"profile_{name}")
            if data:
                profile = json.loads(data)
                return self._normalize_profile(profile)
            return None
        except Exception as e:
            console.print(f"[red]Error retrieving profile '{name}': {e}[/red]")
            return None

    def delete_profile(self, name: str) -> bool:
        """Delete a profile from the keyring."""
        try:
            keyring.delete_password(self.service_name, f"profile_{name}")
            return True
        except keyring.errors.PasswordDeleteError:
            console.print(f"[yellow]Profile '{name}' not found[/yellow]")
            return False
        except Exception as e:
            console.print(f"[red]Error deleting profile '{name}': {e}[/red]")
            return False

    def list_profiles(self) -> Dict[str, Dict[str, Any]]:
        """List all profiles from the keyring."""
        profiles = {}
        try:
            # Keyring doesn't provide a direct way to list all keys
            # We'll use a metadata approach by storing a list of profile names
            profile_list_data = keyring.get_password(self.service_name, "profile_list")
            if profile_list_data:
                profile_names = json.loads(profile_list_data)
                for name in profile_names:
                    profile = self.get_profile(name)
                    if profile:
                        # Normalize for backward compatibility
                        profiles[name] = self._normalize_profile(profile)
        except Exception as e:
            console.print(f"[red]Error listing profiles: {e}[/red]")
        return profiles

    def update_profile_list(self, profile_names: list) -> bool:
        """Update profile names in keyring with file locking protection."""
        lock_path = self.config_dir / ".profile_list.lock"
        try:
            # Ensure config directory exists for lock file
            self.ensure_config_dir()

            # Use file lock to prevent race conditions in concurrent access
            with FileLock(str(lock_path), timeout=5):
                keyring.set_password(
                    self.service_name, "profile_list", json.dumps(profile_names)
                )
            return True
        except Exception as e:
            console.print(f"[red]Error updating profile list: {e}[/red]")
            return False

    def save_active_token(
        self, token: str, target_path: Optional[str] = None
    ) -> bool:
        """Save the active token to the specified location.

        For macOS: Writes OAuth JSON to keychain using security command
        (Claude Code compatible)
        For Linux/Windows: Writes to file

        Args:
            token: Either OAuth JSON string or plain token string
            target_path: Optional file path (used only for non-macOS or when
                explicitly specified)
        """
        import subprocess
        import sys

        try:
            # On macOS, write to keychain to be compatible with Claude Code OAuth
            if sys.platform == "darwin" and not target_path:
                # Delete existing keychain entry
                subprocess.run(
                    [
                        "security",
                        "delete-generic-password",
                        "-a",
                        os.environ.get("USER", ""),
                        "-s",
                        "Claude Code-credentials",
                    ],
                    capture_output=True,
                )

                # Add new keychain entry with OAuth data
                result = subprocess.run(
                    [
                        "security",
                        "add-generic-password",
                        "-a",
                        os.environ.get("USER", ""),
                        "-s",
                        "Claude Code-credentials",
                        "-w",
                        token,
                    ],
                    capture_output=True,
                    check=True,
                )
                return result.returncode == 0
            else:
                # File-based storage for Linux/Windows or explicit path
                if target_path:
                    target = Path(target_path).expanduser()
                    target.parent.mkdir(parents=True, exist_ok=True)
                else:
                    self.ensure_config_dir()
                    target = self.credentials_file

                # Write atomically
                with tempfile.NamedTemporaryFile(
                    "w", dir=str(target.parent), delete=False
                ) as tmp_file:
                    # Store as-is (could be OAuth JSON or plain token)
                    tmp_file.write(token)
                    temp_path = Path(tmp_file.name)
                temp_path.replace(target)

                # Set secure permissions (0600)
                os.chmod(target, stat.S_IRUSR | stat.S_IWUSR)
                return True
        except Exception as e:
            console.print(f"[red]Error saving active token: {e}[/red]")
            return False

    def get_active_token(self, target_path: Optional[str] = None) -> Optional[str]:
        """Get the active token from the specified location."""
        try:
            if target_path:
                target = Path(target_path)
            else:
                target = self.credentials_file

            if not target.exists():
                return None

            with open(target, "r") as f:
                data = json.load(f)
                return data.get("token")
        except Exception as e:
            console.print(f"[red]Error reading active token: {e}[/red]")
            return None

    def get_config_path(self) -> str:
        """Get the configuration directory path."""
        return str(self.config_dir)

    def check_keyring_backend(self) -> str:
        """Check which keyring backend is being used."""
        try:
            backend = keyring.get_keyring()
            return f"{backend.__class__.__module__}.{backend.__class__.__name__}"
        except Exception:
            return "Unknown"

    def test_keyring_access(self) -> bool:
        """Test if keyring is accessible."""
        try:
            test_key = "test_access"
            test_value = "test_value"
            keyring.set_password(self.service_name, test_key, test_value)
            retrieved = keyring.get_password(self.service_name, test_key)
            keyring.delete_password(self.service_name, test_key)
            return retrieved == test_value
        except Exception as e:
            console.print(f"[red]Keyring access test failed: {e}[/red]")
            return False
