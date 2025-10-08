"""Utility functions for CC Profile Switch."""

import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from rich import box
from rich.prompt import Confirm, Prompt
from rich.table import Table

from .constants import (
    ENV_ANTHROPIC_BASE_URL,
    ENV_ZAI_API_KEY,
    ENV_ZHIPUAI_API_KEY,
    PROVIDER_CLAUDE,
    PROVIDER_ZAI,
)
from .theme import console, get_icon, should_use_rich


def mask_token(token: str, visible_chars: int = 4) -> str:
    """Mask a token, showing only the first few characters.

    Handles both plain tokens and OAuth JSON structures.
    """
    import json

    if not token:
        return ""

    # Check if it's OAuth JSON
    try:
        data = json.loads(token)
        if "claudeAiOauth" in data:
            # Mask the accessToken in OAuth JSON
            access_token = data["claudeAiOauth"].get("accessToken", "")
            if access_token:
                masked = access_token[:visible_chars] + "*" * (
                    len(access_token) - visible_chars
                )
                return f"OAuth: {masked} (with refreshToken)"
            return "OAuth structure (no accessToken)"
        elif "token" in data:
            # Wrapped token format
            inner_token = data["token"]
            return mask_token(inner_token, visible_chars)
    except (json.JSONDecodeError, TypeError):
        pass

    # Plain token
    if len(token) <= visible_chars:
        return "*" * len(token)
    return token[:visible_chars] + "*" * (len(token) - visible_chars)


def validate_token(token: str, provider: str = PROVIDER_CLAUDE) -> Tuple[bool, str]:
    """Validate API token format for a specific provider.

    Args:
        token: The API key or token to validate
        provider: Provider name ("claude" or "zai")

    Returns:
        Tuple of (is_valid, error_message)
    """
    import json

    if not token:
        return False, "Token is empty"

    if provider == PROVIDER_CLAUDE:
        # Check if it's OAuth JSON first (may contain legitimate whitespace)
        try:
            data = json.loads(token)
            if "claudeAiOauth" in data:
                # Validate OAuth structure has required fields
                oauth = data["claudeAiOauth"]
                has_access = "accessToken" in oauth and oauth["accessToken"]
                has_refresh = "refreshToken" in oauth
                if has_access and has_refresh:
                    return True, ""
                return False, "OAuth structure missing required fields"
            elif "token" in data:
                # Wrapped token - validate inner token
                return validate_token(data["token"], provider)
        except (json.JSONDecodeError, TypeError):
            pass

        # Plain token validation for Claude
        # Claude tokens: sk-ant-{type}-{key} or plain sk-* tokens
        # Check for whitespace (OAuth JSON was already handled above)
        if " " in token or "\n" in token or "\t" in token:
            return False, "Token contains whitespace"

        if len(token) < 20:
            return False, "Token too short (minimum 20 characters)"

        if token.startswith("sk-"):
            return True, ""

        return False, "Claude token must start with 'sk-' prefix"

    elif provider == PROVIDER_ZAI:
        # Z-AI tokens: be permissive but safe
        # Check for whitespace
        if " " in token or "\n" in token or "\t" in token:
            return False, "Token contains whitespace"

        if len(token) < 20:
            return False, "Token too short (minimum 20 characters)"
        return True, ""

    return False, f"Unknown provider: {provider}"


def detect_zai_token() -> Optional[str]:
    """Detect Z-AI API key from environment variables."""
    return os.getenv(ENV_ZAI_API_KEY) or os.getenv(ENV_ZHIPUAI_API_KEY)


def detect_current_provider() -> Dict[str, Any]:
    """Detect current provider from Claude settings.json.

    Returns:
        Dictionary with keys:
        - provider: "claude" or "zai"
        - token_present: bool
        - base_url: Optional[str]
        - source: str
    """
    from .config import Config

    config = Config()
    env_vars = config.get_claude_settings_env()

    base_url = env_vars.get(ENV_ANTHROPIC_BASE_URL)
    has_token = "ANTHROPIC_AUTH_TOKEN" in env_vars

    # Infer provider from base URL
    if base_url and ("z.ai" in base_url or "bigmodel.cn" in base_url):
        provider = PROVIDER_ZAI
    else:
        provider = PROVIDER_CLAUDE

    return {
        "provider": provider,
        "token_present": has_token,
        "base_url": base_url,
        "source": "claude_settings_env",
    }


def find_claude_config_paths() -> List[Path]:
    """Find possible Claude configuration paths."""
    home = Path.home()
    possible_paths = [
        home / ".claude" / "credentials.json",
        home / ".config" / "claude" / "credentials.json",
        home / "AppData" / "Roaming" / "Claude" / "credentials.json",
        home / "Library" / "Application Support" / "Claude" / "credentials.json",
    ]

    # Add platform-specific paths
    if sys.platform == "darwin":  # macOS
        possible_paths.extend(
            [
                home / "Library" / "Application Support" / "Claude" / "config.json",
                home / ".claude" / "config.json",
            ]
        )
    elif sys.platform == "win32":  # Windows
        possible_paths.extend(
            [
                home / "AppData" / "Local" / "Claude" / "credentials.json",
                home / "AppData" / "Local" / "Claude" / "config.json",
            ]
        )
    else:  # Linux and others
        possible_paths.extend(
            [
                home / ".config" / "claude" / "config.json",
                home / ".claude" / "config.json",
            ]
        )

    return [path for path in possible_paths if path.exists()]


def create_profile_table(
    profiles: dict, show_tokens: bool = False, active_profile: Optional[str] = None
) -> Table:
    """Create a Rich table for displaying profiles."""
    table = Table(
        title="[title]Claude Profiles[/title]",
        box=box.MINIMAL_HEAVY_HEAD,
        row_styles=["", "dim"] if should_use_rich() else None,
        show_header=True,
        header_style="bold cyan",
    )

    active_icon = get_icon("active")
    table.add_column("", style="accent", width=3)  # Active indicator
    table.add_column("No.", style="cyan", width=4)
    table.add_column("Name", style="magenta")
    table.add_column("Token", style="green")
    table.add_column("Created", style="yellow")
    table.add_column("Description", style="blue")

    for i, (name, data) in enumerate(profiles.items(), 1):
        token = data.get("token", "")
        if show_tokens:
            token_display = token
        else:
            token_display = mask_token(token)

        created = data.get("metadata", {}).get("created", "Unknown")
        metadata = data.get("metadata", {}).get("description", "")

        # Format created timestamp
        created_display = format_timestamp(created)

        # Mark active profile
        is_active = name == active_profile
        indicator = active_icon if is_active else ""

        if is_active and should_use_rich():
            table.add_row(
                indicator,
                f"[bold]{i}[/bold]",
                f"[bold highlight]{name}[/bold highlight]",
                token_display,
                created_display,
                metadata,
                style="highlight",
            )
        else:
            table.add_row(
                indicator, str(i), name, token_display, created_display, metadata
            )

    return table


def prompt_for_profile_selection(
    profiles: dict, show_tokens: bool = False
) -> Optional[str]:
    """Prompt user to select a profile from a list."""
    if not profiles:
        console.print("[red]No profiles available[/red]")
        return None

    table = create_profile_table(profiles, show_tokens)
    console.print(table)

    while True:
        try:
            choice = Prompt.ask(
                "Select a profile by number (or 'q' to quit)", default="q"
            )

            if choice.lower() == "q":
                return None

            profile_names = list(profiles.keys())
            index = int(choice) - 1

            if 0 <= index < len(profile_names):
                return profile_names[index]
            else:
                console.print("[red]Invalid selection. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")


def confirm_action(message: str, default: bool = False) -> bool:
    """Ask for user confirmation."""
    return Confirm.ask(message, default=default)


def show_success(message: str) -> None:
    """Show a success message."""
    from .theme import show_success as theme_show_success

    theme_show_success(message)


def show_error(message: str) -> None:
    """Show an error message."""
    from .theme import show_error as theme_show_error

    theme_show_error(message)


def show_warning(message: str) -> None:
    """Show a warning message."""
    from .theme import show_warning as theme_show_warning

    theme_show_warning(message)


def show_info(message: str) -> None:
    """Show an info message."""
    from .theme import show_info as theme_show_info

    theme_show_info(message)


def format_timestamp(timestamp: Optional[str]) -> str:
    """Format a timestamp for display."""
    if not timestamp:
        return "Unknown"

    try:
        from datetime import datetime

        # Try to parse ISO format first
        dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, AttributeError):
        return str(timestamp)


def detect_current_token() -> Optional[str]:
    """Try to detect the current Claude token from OS-specific locations.

    Returns the complete OAuth JSON structure for OAuth tokens, or plain token string.
    For OAuth: returns the full JSON string with accessToken, refreshToken, etc.
    For plain API keys: returns just the token string.
    """
    import json
    import os
    import subprocess

    # Try macOS Keychain first
    if sys.platform == "darwin":
        try:
            result = subprocess.run(
                [
                    "security",
                    "find-generic-password",
                    "-a",
                    os.environ.get("USER", ""),
                    "-s",
                    "Claude Code-credentials",
                    "-w",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            keychain_data = result.stdout.strip()
            if keychain_data:
                # Return the complete keychain data (OAuth JSON or plain token)
                # This preserves refreshToken, expiresAt, scopes, mcpOAuth, etc.
                return keychain_data
        except (subprocess.CalledProcessError, KeyError):
            pass

    # Try platform-specific file locations
    credential_paths = []

    if sys.platform == "win32":
        # Windows credential locations
        credential_paths.extend(
            [
                Path.home() / "AppData" / "Roaming" / "Claude" / ".credentials.json",
                Path.home() / "AppData" / "Local" / "Claude" / ".credentials.json",
            ]
        )

    # Linux/Unix and fallback paths
    credential_paths.extend(
        [
            Path.home() / ".claude" / ".credentials.json",
            Path.home() / ".config" / "claude" / "credentials.json",
        ]
    )

    for credential_file in credential_paths:
        if credential_file.exists():
            try:
                with open(credential_file, "r") as f:
                    content = f.read().strip()

                    # Try to parse as JSON first
                    try:
                        data = json.loads(content)

                        # Check for OAuth format (like macOS Keychain)
                        # Return COMPLETE JSON to preserve refreshToken, mcpOAuth, etc.
                        if (
                            "claudeAiOauth" in data
                            and "accessToken" in data["claudeAiOauth"]
                        ):
                            return content  # Return full JSON string!

                        # Look for wrapped token format {"token": "..."}
                        if "token" in data:
                            # Check if the token itself is OAuth JSON
                            token_value = data["token"]
                            try:
                                token_data = json.loads(token_value)
                                if "claudeAiOauth" in token_data:
                                    return token_value  # Return OAuth JSON
                            except (json.JSONDecodeError, TypeError):
                                pass
                            return token_value  # Return plain token

                        # Check other possible keys (legacy formats)
                        for key in ["accessToken", "auth_token", "api_key"]:
                            if key in data:
                                return data[key]
                    except json.JSONDecodeError:
                        # Not JSON - might be plain token
                        if content and validate_token(content):
                            return content
            except Exception:
                continue

    # Fallback to searching other config paths
    for path in find_claude_config_paths():
        try:
            if path.exists():
                with open(path, "r") as f:
                    content = f.read().strip()
                    data = json.loads(content)

                    # Check for OAuth structure
                    if (
                        "claudeAiOauth" in data
                        and "accessToken" in data["claudeAiOauth"]
                    ):
                        return content  # Return full JSON

                    # Check standard token keys
                    for key in ["token", "accessToken", "auth_token", "api_key"]:
                        if key in data:
                            token_value = data[key]
                            # Check if it's OAuth JSON
                            try:
                                token_data = json.loads(token_value)
                                if "claudeAiOauth" in token_data:
                                    return token_value
                            except (json.JSONDecodeError, TypeError):
                                pass
                            return token_value
        except Exception:
            continue

    return None


def check_file_permissions(path: Path) -> bool:
    """Check if a file has secure permissions (0600)."""
    try:
        stat_info = path.stat()
        # Check if file is readable/writable only by owner
        return (stat_info.st_mode & 0o777) == 0o600
    except Exception:
        return False


def secure_file_permissions(path: Path) -> bool:
    """Set secure permissions on a file (0600)."""
    try:
        import os

        os.chmod(path, 0o600)
        return True
    except Exception:
        return False
