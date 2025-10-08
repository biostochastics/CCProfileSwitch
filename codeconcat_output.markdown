# CodeConCat Analysis Report

**Generated**: 2025-10-05 16:47:05

**Total Files**: 11


## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [File Index](#file-index)
- [File Details](#file-details)
  - [1. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/fzf_integration.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-fzf-integration-py)
  - [2. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/config.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-config-py)
  - [3. /Users/biostochastics/CCProfileSwitch/tests/test_basic.py](#users-biostochastics-ccprofileswitch-tests-test-basic-py)
  - [4. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/storage.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-storage-py)
  - [5. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/theme.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-theme-py)
  - [6. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/utils.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-utils-py)
  - [7. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/__init__.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-init-py)
  - [8. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/cli.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-cli-py)
  - [9. /Users/biostochastics/CCProfileSwitch/conftest.py](#users-biostochastics-ccprofileswitch-conftest-py)
  - [10. /Users/biostochastics/CCProfileSwitch/claude_profile_manager_typer_rich.py](#users-biostochastics-ccprofileswitch-claude-profile-manager-typer-rich-py)
  - [11. /Users/biostochastics/CCProfileSwitch/tests/test_cli.py](#users-biostochastics-ccprofileswitch-tests-test-cli-py)

---

## Project Overview {#project-overview}

### Summary Statistics

| Metric | Value |
|--------|-------|
| Total Files | 11 |
| Source Files | 11 |
| Documentation Files | 0 |
| Total Lines | 2909 |

### Directory Structure {#directory-structure}

<details>
<summary>Click to expand directory tree</summary>

```
CCProfileSwitch/
    .gitignore
    claude_profile_manager_typer_rich.py
    conftest.py
    pyproject.toml
    cc_profile_switch/
        __init__.py
        cli.py
        config.py
        fzf_integration.py
        storage.py
        theme.py
        utils.py
    tests/
        test_basic.py
        test_cli.py
```
</details>

## File Index {#file-index}

### Source Code

| # | File | Type | Size |
|---|------|------|------|
| 1 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/fzf_integration.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-fzf-integration-py) | PY | 5.6 KB |
| 2 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/config.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-config-py) | PY | 4.5 KB |
| 3 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/storage.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-storage-py) | PY | 6.7 KB |
| 4 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/theme.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-theme-py) | PY | 4.3 KB |
| 5 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/utils.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-utils-py) | PY | 10.1 KB |
| 6 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/__init__.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-init-py) | PY | 208 B |
| 7 | [/Users/biostochastics/CCProfileSwitch/cc_profile_switch/cli.py](#users-biostochastics-ccprofileswitch-cc-profile-switch-cli-py) | PY | 26.8 KB |
| 8 | [/Users/biostochastics/CCProfileSwitch/claude_profile_manager_typer_rich.py](#users-biostochastics-ccprofileswitch-claude-profile-manager-typer-rich-py) | PY | 27.9 KB |

### Tests

| # | File | Type | Size |
|---|------|------|------|
| 1 | [/Users/biostochastics/CCProfileSwitch/tests/test_basic.py](#users-biostochastics-ccprofileswitch-tests-test-basic-py) | PY | 1.6 KB |
| 2 | [/Users/biostochastics/CCProfileSwitch/conftest.py](#users-biostochastics-ccprofileswitch-conftest-py) | PY | 2.1 KB |
| 3 | [/Users/biostochastics/CCProfileSwitch/tests/test_cli.py](#users-biostochastics-ccprofileswitch-tests-test-cli-py) | PY | 4.0 KB |

---

## File Details {#file-details}

### 1. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/fzf_integration.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-fzf-integration-py}

[↑ Back to TOC](#table-of-contents) | 
[Next →](#users-biostochastics-ccprofileswitch-cc-profile-switch-config-py)


#### Summary

> Contains 6 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 204 |
| Functions/Classes | 64 |
| Security Issues | 3 |

<details>
<summary>📦 Declarations</summary>

- **variable** `console` (lines 8-8)
- **constant** `console` (lines 8-8)
- **function** `check_fzf_available` (lines 11-17)
- **function** `fzf_select_profile` (lines 20-97)
- **variable** `fzf_input` (lines 34-34)
- **constant** `fzf_input` (lines 34-34)
- **variable** `token` (lines 36-36)
- **constant** `token` (lines 36-36)
- **variable** `token_display` (lines 38-38)
- **constant** `token_display` (lines 38-38)
- **variable** `token_display` (lines 42-42)
- **constant** `token_display` (lines 42-42)
- **variable** `metadata` (lines 44-44)
- **constant** `metadata` (lines 44-44)
- **variable** `description` (lines 45-45)
- **constant** `description` (lines 45-45)
- **variable** `created` (lines 46-46)
- **constant** `created` (lines 46-46)
- **variable** `fzf_cmd` (lines 52-74)
- **constant** `fzf_cmd` (lines 52-74)
- **variable** `header` (lines 77-77)
- **constant** `header` (lines 77-77)
- **variable** `input_data` (lines 78-78)
- **constant** `input_data` (lines 78-78)
- **variable** `result` (lines 81-83)
- **constant** `result` (lines 81-83)
- **variable** `selected_line` (lines 85-85)
- **constant** `selected_line` (lines 85-85)
- **variable** `selected_name` (lines 87-87)
- **constant** `selected_name` (lines 87-87)
- **function** `fzf_select_multiple` (lines 100-172)
- **variable** `fzf_input` (lines 111-111)
- **constant** `fzf_input` (lines 111-111)
- **variable** `token` (lines 113-113)
- **constant** `token` (lines 113-113)
- **variable** `token_display` (lines 115-115)
- **constant** `token_display` (lines 115-115)
- **variable** `token_display` (lines 119-119)
- **constant** `token_display` (lines 119-119)
- **variable** `metadata` (lines 121-121)
- **constant** `metadata` (lines 121-121)
- **variable** `description` (lines 122-122)
- **constant** `description` (lines 122-122)
- **variable** `fzf_cmd` (lines 127-146)
- **constant** `fzf_cmd` (lines 127-146)
- **variable** `header` (lines 149-149)
- **constant** `header` (lines 149-149)
- **variable** `input_data` (lines 150-150)
- **constant** `input_data` (lines 150-150)
- **variable** `result` (lines 153-155)
- **constant** `result` (lines 153-155)
- **variable** `selected_lines` (lines 157-157)
- **constant** `selected_lines` (lines 157-157)
- **variable** `selected_names` (lines 158-158)
- **constant** `selected_names` (lines 158-158)
- **variable** `selected_name` (lines 162-162)
- **constant** `selected_name` (lines 162-162)
- **function** `install_fzf_instructions` (lines 175-204)
- **function** `check_fzf_available` (lines 11-19)
- **variable** `fzf_cmd` (lines 52-52)
- **variable** `result` (lines 81-81)
- **variable** `fzf_cmd` (lines 127-127)
- **variable** `result` (lines 153-153)
- **function** `install_fzf_instructions` (lines 175-205)
</details>

<details>
<summary>⚠️ Security Issues</summary>

- ❓ **Line 14**: Potential command injection
- ❓ **Line 81**: Potential command injection
- ❓ **Line 153**: Potential command injection

</details>

#### Source Code

```python
"""FZF integration for fuzzy profile selection."""

import subprocess
from typing import Any, Dict, List, Optional

from rich.console import Console

console = Console()


def check_fzf_available() -> bool:
    """Check if fzf is available in the system."""
    try:
        subprocess.run(["fzf", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def fzf_select_profile(
    profiles: Dict[str, Dict[str, Any]], show_tokens: bool = False
) -> Optional[str]:
    """Use fzf to select a profile interactively."""
    if not check_fzf_available():
        console.print(
            "[yellow]fzf not found. Install fzf for fuzzy selection.[/yellow]"
        )
        console.print(
            "Install with: brew install fzf (macOS) or apt-get install fzf (Ubuntu)"
        )
        return None

    # Prepare fzf input
    fzf_input = []
    for name, data in profiles.items():
        token = data.get("token", "")
        if show_tokens:
            token_display = token
        else:
            from .utils import mask_token

            token_display = mask_token(token)

        metadata = data.get("metadata", {})
        description = metadata.get("description", "")
        created = metadata.get("created", "Unknown")

        # Format: name|token|description|created
        fzf_input.append(f"{name}|{token_display}|{description}|{created}")

    # Prepare fzf command
    fzf_cmd = [
        "fzf",
        "--delimiter",
        "|",
        "--header",
        "Select a profile (Tab to select, Enter to confirm)",
        "--header-lines",
        "1",
        "--layout",
        "reverse",
        "--height",
        "40%",
        "--prompt",
        "Profile> ",
        "--preview",
        "echo 'Token: {2}\\nDescription: {3}\\nCreated: {4}'",
        "--preview-window",
        "down:3:wrap",
        "--bind",
        "ctrl-r:reload(echo 'Name|Token|Description|Created')",
        "--bind",
        "ctrl-c:abort",
    ]

    # Add header
    header = "Name|Token|Description|Created"
    input_data = header + "\n" + "\n".join(fzf_input)

    try:
        result = subprocess.run(
            fzf_cmd, input=input_data, text=True, capture_output=True, check=True
        )

        selected_line = result.stdout.strip()
        if selected_line and selected_line != header:
            selected_name = selected_line.split("|")[0]
            return selected_name

        return None

    except subprocess.CalledProcessError:
        # User cancelled
        return None
    except Exception as e:
        console.print(f"[red]Error running fzf: {e}[/red]")
        return None


def fzf_select_multiple(
    profiles: Dict[str, Dict[str, Any]], show_tokens: bool = False
) -> List[str]:
    """Use fzf to select multiple profiles."""
    if not check_fzf_available():
        console.print(
            "[yellow]fzf not found. Install fzf for fuzzy selection.[/yellow]"
        )
        return []

    # Prepare fzf input
    fzf_input = []
    for name, data in profiles.items():
        token = data.get("token", "")
        if show_tokens:
            token_display = token
        else:
            from .utils import mask_token

            token_display = mask_token(token)

        metadata = data.get("metadata", {})
        description = metadata.get("description", "")

        fzf_input.append(f"{name}|{token_display}|{description}")

    # Prepare fzf command for multiple selection
    fzf_cmd = [
        "fzf",
        "--delimiter",
        "|",
        "--multi",
        "--header",
        "Select profiles (Tab to select, Enter to confirm)",
        "--header-lines",
        "1",
        "--layout",
        "reverse",
        "--height",
        "40%",
        "--prompt",
        "Profiles> ",
        "--preview",
        "echo 'Token: {2}\\nDescription: {3}'",
        "--preview-window",
        "down:2:wrap",
    ]

    # Add header
    header = "Name|Token|Description"
    input_data = header + "\n" + "\n".join(fzf_input)

    try:
        result = subprocess.run(
            fzf_cmd, input=input_data, text=True, capture_output=True, check=True
        )

        selected_lines = result.stdout.strip().split("\n")
        selected_names = []

        for line in selected_lines:
            if line and line != header:
                selected_name = line.split("|")[0]
                selected_names.append(selected_name)

        return selected_names

    except subprocess.CalledProcessError:
        # User cancelled
        return []
    except Exception as e:
        console.print(f"[red]Error running fzf: {e}[/red]")
        return []


def install_fzf_instructions() -> None:
    """Show fzf installation instructions."""
    console.print("[bold blue]fzf Installation Instructions[/bold blue]")
    console.print()

    console.print("[bold]macOS:[/bold]")
    console.print("  brew install fzf")
    console.print()

    console.print("[bold]Ubuntu/Debian:[/bold]")
    console.print("  sudo apt-get install fzf")
    console.print()

    console.print("[bold]Fedora:[/bold]")
    console.print("  sudo dnf install fzf")
    console.print()

    console.print("[bold]Windows:[/bold]")
    console.print("  scoop install fzf")
    console.print("  # or")
    console.print("  choco install fzf")
    console.print()

    console.print("[bold]From source:[/bold]")
    console.print("  git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    console.print("  ~/.fzf/install")
    console.print()

    console.print("[dim]After installation, restart your shell or run:[/dim]")
    console.print("[dim]  source ~/.bashrc  # or ~/.zshrc[/dim]")

```

---

### 2. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/config.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-config-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-fzf-integration-py) | 
[Next →](#users-biostochastics-ccprofileswitch-tests-test-basic-py)


#### Summary

> Contains 18 functions, 2 classes

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 126 |
| Functions/Classes | 35 |

<details>
<summary>📦 Declarations</summary>

- **variable** `platform_user_config_dir` (lines 10-10)
- **constant** `platform_user_config_dir` (lines 10-10)
- **variable** `console` (lines 13-13)
- **constant** `console` (lines 13-13)
- **function** `_user_config_dir` (lines 16-19)
- **class** `Config` (lines 22-126)
- **function** `__init__` (lines 25-38)
- **function** `ensure_config_dir` (lines 40-42)
- **function** `load_config` (lines 44-56)
- **variable** `config` (lines 49-49)
- **constant** `config` (lines 49-49)
- **function** `save_config` (lines 58-67)
- **function** `get` (lines 69-72)
- **variable** `config` (lines 71-71)
- **constant** `config` (lines 71-71)
- **function** `set` (lines 74-78)
- **variable** `config` (lines 76-76)
- **constant** `config` (lines 76-76)
- **function** `get_active_token_path` (lines 80-86)
- **variable** `config` (lines 82-82)
- **constant** `config` (lines 82-82)
- **variable** `target` (lines 83-85)
- **constant** `target` (lines 83-85)
- **function** `set_active_token_target` (lines 88-90)
- **function** `get_default_profile` (lines 92-94)
- **function** `set_default_profile` (lines 96-98)
- **function** `is_auto_switch_enabled` (lines 100-102)
- **function** `set_auto_switch` (lines 104-106)
- **function** `should_show_token_warning` (lines 108-110)
- **function** `set_token_warning` (lines 112-114)
- **function** `should_mask_tokens` (lines 116-118)
- **function** `set_token_masking` (lines 120-122)
- **function** `get_config_path` (lines 124-126)
- **variable** `platform_user_config_dir` (lines 10-18)
- **class** `Config` (lines 22-127)
</details>

#### Source Code

```python
"""Configuration management for CC Profile Switch."""

import json
from pathlib import Path
from typing import Any, Dict, Optional

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

```

---

### 3. /Users/biostochastics/CCProfileSwitch/tests/test_basic.py {#users-biostochastics-ccprofileswitch-tests-test-basic-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-config-py) | 
[Next →](#users-biostochastics-ccprofileswitch-cc-profile-switch-storage-py)


#### Summary

> Contains 5 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 48 |
| Functions/Classes | 21 |

<details>
<summary>📦 Declarations</summary>

- **function** `test_token_helpers_mask_and_validate` (lines 12-20)
- **variable** `token` (lines 13-13)
- **constant** `token` (lines 13-13)
- **variable** `masked` (lines 14-14)
- **constant** `masked` (lines 14-14)
- **function** `test_profile_storage_round_trip` (lines 23-36)
- **variable** `storage` (lines 24-24)
- **constant** `storage` (lines 24-24)
- **variable** `metadata` (lines 25-25)
- **constant** `metadata` (lines 25-25)
- **variable** `profile` (lines 30-30)
- **constant** `profile` (lines 30-30)
- **function** `test_config_paths_and_mutation` (lines 39-48)
- **variable** `config` (lines 40-40)
- **constant** `config` (lines 40-40)
- **variable** `default_path` (lines 43-43)
- **constant** `default_path` (lines 43-43)
- **variable** `custom_path` (lines 46-46)
- **constant** `custom_path` (lines 46-46)
- **function** `test_token_helpers_mask_and_validate` (lines 12-22)
- **function** `test_config_paths_and_mutation` (lines 39-49)
</details>

#### Source Code

```python
"""Unit tests for CC Profile Switch core helpers."""

from __future__ import annotations

from pathlib import Path

from cc_profile_switch.config import Config
from cc_profile_switch.storage import ProfileStorage
from cc_profile_switch.utils import mask_token, validate_token


def test_token_helpers_mask_and_validate() -> None:
    token = "sk-ant-api03-example-token"
    masked = mask_token(token, visible_chars=6)

    assert masked.startswith("sk-ant")
    assert set(masked[6:]) == {"*"}
    assert validate_token(token) is True
    assert validate_token("") is False
    assert validate_token("bad token") is False


def test_profile_storage_round_trip(tmp_path: Path) -> None:
    storage = ProfileStorage()
    metadata = {"created": "2024-01-01T00:00:00", "description": "Sample"}

    assert storage.save_profile("sample", "sk-ant-api03-sample", metadata) is True
    storage.update_profile_list(["sample"])

    profile = storage.get_profile("sample")
    assert profile
    assert profile["token"] == "sk-ant-api03-sample"
    assert profile["metadata"] == metadata

    assert storage.save_active_token("sk-ant-api03-sample") is True
    assert storage.get_active_token() == "sk-ant-api03-sample"


def test_config_paths_and_mutation(tmp_path: Path) -> None:
    config = Config()
    config.ensure_config_dir()

    default_path = Path(config.get_active_token_path())
    assert default_path.name == ".credentials.json"

    custom_path = tmp_path / "tokens" / "active.json"
    assert config.set_active_token_target("file", str(custom_path)) is True
    assert Path(config.get_active_token_path()) == custom_path

```

---

### 4. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/storage.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-storage-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-tests-test-basic-py) | 
[Next →](#users-biostochastics-ccprofileswitch-cc-profile-switch-theme-py)


#### Summary

> Contains 13 functions, 2 classes

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 181 |
| Functions/Classes | 54 |

<details>
<summary>📦 Declarations</summary>

- **variable** `platform_user_config_dir` (lines 13-13)
- **constant** `platform_user_config_dir` (lines 13-13)
- **variable** `console` (lines 19-19)
- **constant** `console` (lines 19-19)
- **function** `_user_config_dir` (lines 22-26)
- **class** `ProfileStorage` (lines 29-181)
- **function** `__init__` (lines 32-36)
- **function** `ensure_config_dir` (lines 38-40)
- **function** `save_profile` (lines 42-54)
- **variable** `profile_data` (lines 47-47)
- **constant** `profile_data` (lines 47-47)
- **function** `get_profile` (lines 56-65)
- **variable** `data` (lines 59-59)
- **constant** `data` (lines 59-59)
- **function** `delete_profile` (lines 67-77)
- **function** `list_profiles` (lines 79-94)
- **variable** `profiles` (lines 81-81)
- **constant** `profiles` (lines 81-81)
- **variable** `profile_list_data` (lines 85-85)
- **constant** `profile_list_data` (lines 85-85)
- **variable** `profile_names` (lines 87-87)
- **constant** `profile_names` (lines 87-87)
- **variable** `profile` (lines 89-89)
- **constant** `profile` (lines 89-89)
- **function** `update_profile_list` (lines 96-111)
- **variable** `lock_path` (lines 98-98)
- **constant** `lock_path` (lines 98-98)
- **function** `save_active_token` (lines 113-138)
- **variable** `target` (lines 118-118)
- **constant** `target` (lines 118-118)
- **variable** `target` (lines 123-123)
- **constant** `target` (lines 123-123)
- **variable** `temp_path` (lines 130-130)
- **constant** `temp_path` (lines 130-130)
- **function** `get_active_token` (lines 140-156)
- **variable** `target` (lines 144-144)
- **constant** `target` (lines 144-144)
- **variable** `target` (lines 146-146)
- **constant** `target` (lines 146-146)
- **variable** `data` (lines 152-152)
- **constant** `data` (lines 152-152)
- **function** `get_config_path` (lines 158-160)
- **function** `check_keyring_backend` (lines 162-168)
- **variable** `backend` (lines 165-165)
- **constant** `backend` (lines 165-165)
- **function** `test_keyring_access` (lines 170-181)
- **variable** `test_key` (lines 173-173)
- **constant** `test_key` (lines 173-173)
- **variable** `test_value` (lines 174-174)
- **constant** `test_value` (lines 174-174)
- **variable** `retrieved` (lines 176-176)
- **constant** `retrieved` (lines 176-176)
- **variable** `platform_user_config_dir` (lines 13-25)
- **class** `ProfileStorage` (lines 29-182)
</details>

#### Source Code

```python
"""Secure storage module for Claude profiles using keyring."""

import json
import os
import stat
import tempfile
from pathlib import Path
from typing import Any, Dict, Optional

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

    def save_profile(
        self, name: str, token: str, metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Save a profile to the keyring."""
        try:
            profile_data = {"token": token, "metadata": metadata or {}}
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
                return json.loads(data)
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
                        profiles[name] = profile
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

    def save_active_token(self, token: str, target_path: Optional[str] = None) -> bool:
        """Save the active token to the specified location."""
        try:
            if target_path:
                # Use custom target path
                target = Path(target_path).expanduser()
                target.parent.mkdir(parents=True, exist_ok=True)
            else:
                # Use default location
                self.ensure_config_dir()
                target = self.credentials_file

            # Write atomically
            with tempfile.NamedTemporaryFile(
                "w", dir=str(target.parent), delete=False
            ) as tmp_file:
                json.dump({"token": token}, tmp_file)
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

```

---

### 5. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/theme.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-theme-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-storage-py) | 
[Next →](#users-biostochastics-ccprofileswitch-cc-profile-switch-utils-py)


#### Summary

> Contains 18 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 170 |
| Functions/Classes | 51 |

<details>
<summary>📦 Declarations</summary>

- **variable** `APP_THEME` (lines 15-26)
- **constant** `APP_THEME` (lines 15-26)
- **variable** `ICONS` (lines 29-36)
- **constant** `ICONS` (lines 29-36)
- **variable** `ASCII_ICONS` (lines 38-45)
- **constant** `ASCII_ICONS` (lines 38-45)
- **function** `should_use_rich` (lines 48-58)
- **function** `should_use_unicode` (lines 61-65)
- **function** `get_icon` (lines 68-71)
- **variable** `icons` (lines 70-70)
- **constant** `icons` (lines 70-70)
- **function** `get_console` (lines 74-80)
- **variable** `console` (lines 84-84)
- **constant** `console` (lines 84-84)
- **function** `show_header` (lines 87-94)
- **function** `show_success` (lines 97-103)
- **variable** `icon` (lines 99-99)
- **constant** `icon` (lines 99-99)
- **function** `show_error` (lines 106-112)
- **variable** `icon` (lines 108-108)
- **constant** `icon` (lines 108-108)
- **function** `show_warning` (lines 115-121)
- **variable** `icon` (lines 117-117)
- **constant** `icon` (lines 117-117)
- **function** `show_info` (lines 124-130)
- **variable** `icon` (lines 126-126)
- **constant** `icon` (lines 126-126)
- **function** `show_spinner` (lines 133-141)
- **variable** `spinner` (lines 136-136)
- **constant** `spinner` (lines 136-136)
- **function** `create_panel` (lines 144-157)
- **function** `show_transition` (lines 160-170)
- **variable** `arrow` (lines 162-162)
- **constant** `arrow` (lines 162-162)
- **constant** `APP_THEME` (lines 15-15)
- **constant** `ICONS` (lines 29-29)
- **constant** `ASCII_ICONS` (lines 38-38)
- **function** `should_use_rich` (lines 48-60)
- **function** `get_icon` (lines 68-73)
- **variable** `theme` (lines 77-77)
- **variable** `no_color` (lines 79-79)
- **function** `show_header` (lines 87-96)
- **function** `show_error` (lines 106-114)
- **function** `show_info` (lines 124-132)
- **variable** `title` (lines 146-156)
- **function** `show_transition` (lines 160-171)
- **variable** `box_style` (lines 148-148)
- **variable** `title` (lines 153-153)
- **variable** `border_style` (lines 154-154)
- **variable** `box` (lines 155-155)
- **variable** `padding` (lines 156-156)
</details>

#### Source Code

```python
"""Theme and presentation module for CCProfileSwitch CLI."""

import os
import sys
from typing import Optional

from rich import box
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.spinner import Spinner
from rich.theme import Theme

# Custom theme with accessible, colorblind-friendly colors
APP_THEME = Theme(
    {
        "title": "bold cyan",
        "accent": "bright_cyan",
        "success": "bold green",
        "warning": "bold yellow",
        "error": "bold red",
        "info": "bold blue",
        "muted": "dim",
        "highlight": "bold bright_cyan",
    }
)

# Icons with ASCII fallbacks
ICONS = {
    "success": "✔",
    "warning": "⚠",
    "error": "✖",
    "info": "ℹ",
    "arrow": "→",
    "active": "●",
}

ASCII_ICONS = {
    "success": "[OK]",
    "warning": "[!]",
    "error": "[ERR]",
    "info": "[i]",
    "arrow": "->",
    "active": "*",
}


def should_use_rich() -> bool:
    """Determine if rich formatting should be used."""
    # Check NO_COLOR environment variable
    if os.getenv("NO_COLOR"):
        return False
    if os.getenv("CCPS_NO_COLOR"):
        return False
    # Check if output is a TTY
    if not sys.stdout.isatty():
        return False
    return True


def should_use_unicode() -> bool:
    """Determine if Unicode icons should be used."""
    if os.getenv("CCPS_ASCII"):
        return False
    return sys.stdout.encoding.lower() in ("utf-8", "utf8")


def get_icon(name: str) -> str:
    """Get an icon by name, with ASCII fallback."""
    icons = ICONS if should_use_unicode() else ASCII_ICONS
    return icons.get(name, "")


def get_console() -> Console:
    """Get a configured console instance."""
    return Console(
        theme=APP_THEME,
        force_terminal=should_use_rich(),
        no_color=not should_use_rich(),
    )


# Global console instance
console = get_console()


def show_header(title: str, subtitle: Optional[str] = None) -> None:
    """Show a styled command header."""
    if should_use_rich():
        if subtitle:
            console.rule(f"[title]{title}[/title] [muted]{subtitle}[/muted]")
        else:
            console.rule(f"[title]{title}[/title]")
        console.print()


def show_success(message: str, **kwargs) -> None:
    """Show a success message."""
    icon = get_icon("success")
    if should_use_rich():
        console.print(f"[success]{icon} {message}[/success]", **kwargs)
    else:
        print(f"{icon} {message}")


def show_error(message: str, **kwargs) -> None:
    """Show an error message."""
    icon = get_icon("error")
    if should_use_rich():
        console.print(f"[error]{icon} {message}[/error]", **kwargs)
    else:
        print(f"{icon} {message}")


def show_warning(message: str, **kwargs) -> None:
    """Show a warning message."""
    icon = get_icon("warning")
    if should_use_rich():
        console.print(f"[warning]{icon} {message}[/warning]", **kwargs)
    else:
        print(f"{icon} {message}")


def show_info(message: str, **kwargs) -> None:
    """Show an info message."""
    icon = get_icon("info")
    if should_use_rich():
        console.print(f"[info]{icon} {message}[/info]", **kwargs)
    else:
        print(f"{icon} {message}")


def show_spinner(message: str, spinner_type: str = "dots") -> Live:
    """Create a spinner context for operations."""
    if should_use_rich():
        spinner = Spinner(spinner_type, text=message, style="accent")
        return Live(spinner, console=console, transient=True)
    else:
        # For non-TTY, just print the message
        print(message)
        return None


def create_panel(
    content: str,
    title: Optional[str] = None,
    border_style: str = "accent",
    box_style=box.ROUNDED,
) -> Panel:
    """Create a styled panel."""
    return Panel(
        content,
        title=title,
        border_style=border_style,
        box=box_style,
        padding=(1, 2),
    )


def show_transition(from_profile: str, to_profile: str) -> None:
    """Show a profile transition with visual feedback."""
    arrow = get_icon("arrow")
    if should_use_rich():
        console.print()
        console.print(
            f"[muted]Previous:[/muted] {from_profile} {arrow} "
            f"[success]Active:[/success] [bold]{to_profile}[/bold]"
        )
    else:
        print(f"Previous: {from_profile} {arrow} Active: {to_profile}")

```

---

### 6. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/utils.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-utils-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-theme-py) | 
[Next →](#users-biostochastics-ccprofileswitch-cc-profile-switch-init-py)


#### Summary

> Contains 20 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 325 |
| Functions/Classes | 79 |

<details>
<summary>📦 Declarations</summary>

- **function** `mask_token` (lines 15-19)
- **function** `validate_token` (lines 22-31)
- **function** `find_claude_config_paths` (lines 34-67)
- **variable** `home` (lines 36-36)
- **constant** `home` (lines 36-36)
- **variable** `possible_paths` (lines 37-42)
- **constant** `possible_paths` (lines 37-42)
- **function** `create_profile_table` (lines 70-122)
- **variable** `table` (lines 74-80)
- **constant** `table` (lines 74-80)
- **variable** `active_icon` (lines 82-82)
- **constant** `active_icon` (lines 82-82)
- **variable** `token` (lines 91-91)
- **constant** `token` (lines 91-91)
- **variable** `token_display` (lines 93-93)
- **constant** `token_display` (lines 93-93)
- **variable** `token_display` (lines 95-95)
- **constant** `token_display` (lines 95-95)
- **variable** `created` (lines 97-97)
- **constant** `created` (lines 97-97)
- **variable** `metadata` (lines 98-98)
- **constant** `metadata` (lines 98-98)
- **variable** `created_display` (lines 101-101)
- **constant** `created_display` (lines 101-101)
- **variable** `is_active` (lines 104-104)
- **constant** `is_active` (lines 104-104)
- **variable** `indicator` (lines 105-105)
- **constant** `indicator` (lines 105-105)
- **function** `prompt_for_profile_selection` (lines 125-153)
- **variable** `table` (lines 133-133)
- **constant** `table` (lines 133-133)
- **variable** `choice` (lines 138-140)
- **constant** `choice` (lines 138-140)
- **variable** `profile_names` (lines 145-145)
- **constant** `profile_names` (lines 145-145)
- **variable** `index` (lines 146-146)
- **constant** `index` (lines 146-146)
- **function** `confirm_action` (lines 156-158)
- **function** `show_success` (lines 161-165)
- **function** `show_error` (lines 168-172)
- **function** `show_warning` (lines 175-179)
- **function** `show_info` (lines 182-186)
- **function** `format_timestamp` (lines 189-201)
- **variable** `dt` (lines 198-198)
- **constant** `dt` (lines 198-198)
- **function** `detect_current_token` (lines 204-304)
- **variable** `result` (lines 213-226)
- **constant** `result` (lines 213-226)
- **variable** `keychain_data` (lines 227-227)
- **constant** `keychain_data` (lines 227-227)
- **variable** `data` (lines 231-231)
- **constant** `data` (lines 231-231)
- **variable** `credential_paths` (lines 245-245)
- **constant** `credential_paths` (lines 245-245)
- **variable** `content` (lines 268-268)
- **constant** `content` (lines 268-268)
- **variable** `data` (lines 272-272)
- **constant** `data` (lines 272-272)
- **variable** `data` (lines 297-297)
- **constant** `data` (lines 297-297)
- **function** `check_file_permissions` (lines 307-314)
- **variable** `stat_info` (lines 310-310)
- **constant** `stat_info` (lines 310-310)
- **function** `secure_file_permissions` (lines 317-325)
- **function** `mask_token` (lines 15-21)
- **function** `find_claude_config_paths` (lines 34-69)
- **variable** `table` (lines 74-74)
- **variable** `box` (lines 76-76)
- **variable** `show_header` (lines 78-78)
- **variable** `style` (lines 115-115)
- **variable** `choice` (lines 138-138)
- **function** `confirm_action` (lines 156-160)
- **function** `show_error` (lines 168-174)
- **function** `show_info` (lines 182-188)
- **variable** `dt` (lines 198-240)
- **function** `check_file_permissions` (lines 307-316)
- **variable** `title` (lines 75-75)
- **variable** `row_styles` (lines 77-77)
- **variable** `header_style` (lines 79-79)
</details>

#### Source Code

```python
"""Utility functions for CC Profile Switch."""

import re
import sys
from pathlib import Path
from typing import List, Optional

from rich import box
from rich.prompt import Confirm, Prompt
from rich.table import Table

from .theme import console, get_icon, should_use_rich


def mask_token(token: str, visible_chars: int = 4) -> str:
    """Mask a token, showing only the first few characters."""
    if not token or len(token) <= visible_chars:
        return "*" * len(token) if token else ""
    return token[:visible_chars] + "*" * (len(token) - visible_chars)


def validate_token(token: str) -> bool:
    """Validate Claude API token format (sk-ant-* pattern)."""
    if not token:
        return False
    # Claude tokens follow the pattern: sk-ant-{identifier}-{key}
    # Example: sk-ant-api03-xxxxx...
    if len(token) < 20:
        return False
    # Enforce Claude-specific token format (minimum 7 chars after second hyphen)
    return bool(re.match(r"^sk-ant-[a-zA-Z0-9]{4,}-[a-zA-Z0-9\-_]{7,}$", token))


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
    """Try to detect the current Claude token from OS-specific locations."""
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
                # Try to parse as JSON (OAuth format)
                try:
                    data = json.loads(keychain_data)
                    # Extract accessToken from claudeAiOauth
                    if (
                        "claudeAiOauth" in data
                        and "accessToken" in data["claudeAiOauth"]
                    ):
                        return data["claudeAiOauth"]["accessToken"]
                except json.JSONDecodeError:
                    # Not JSON, return as-is (plain token)
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
                        if (
                            "claudeAiOauth" in data
                            and "accessToken" in data["claudeAiOauth"]
                        ):
                            return data["claudeAiOauth"]["accessToken"]

                        # Look for token in various possible keys
                        for key in ["token", "accessToken", "auth_token", "api_key"]:
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
                    data = json.load(f)
                    for key in ["token", "accessToken", "auth_token", "api_key"]:
                        if key in data:
                            return data[key]
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

```

---

### 7. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/__init__.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-init-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-utils-py) | 
[Next →](#users-biostochastics-ccprofileswitch-cc-profile-switch-cli-py)


#### Summary

> No declarations found

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 5 |
| Functions/Classes | 6 |

<details>
<summary>📦 Declarations</summary>

- **variable** `__version__` (lines 3-3)
- **constant** `__version__` (lines 3-3)
- **variable** `__author__` (lines 4-4)
- **constant** `__author__` (lines 4-4)
- **variable** `__description__` (lines 5-5)
- **constant** `__description__` (lines 5-5)
</details>

#### Source Code

```python
"""CC Profile Switch - A cross-platform Claude profile manager."""

__version__ = "0.1.0"
__author__ = "Claude Profile Manager"
__description__ = "A cross-platform Claude profile manager with Typer and Rich"

```

---

### 8. /Users/biostochastics/CCProfileSwitch/cc_profile_switch/cli.py {#users-biostochastics-ccprofileswitch-cc-profile-switch-cli-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-init-py) | 
[Next →](#users-biostochastics-ccprofileswitch-conftest-py)


#### Summary

> Contains 29 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 822 |
| Functions/Classes | 285 |

<details>
<summary>📦 Declarations</summary>

- **variable** `app` (lines 45-50)
- **constant** `app` (lines 45-50)
- **function** `get_storage` (lines 53-55)
- **function** `get_config` (lines 58-60)
- **function** `init` (lines 63-142)
- **function** `init` (lines 64-142)
- **variable** `storage` (lines 78-78)
- **constant** `storage` (lines 78-78)
- **variable** `config` (lines 79-79)
- **constant** `config` (lines 79-79)
- **variable** `found_paths` (lines 92-92)
- **constant** `found_paths` (lines 92-92)
- **variable** `token_target` (lines 94-94)
- **constant** `token_target` (lines 94-94)
- **variable** `token_target` (lines 97-97)
- **constant** `token_target` (lines 97-97)
- **variable** `profiles` (lines 105-105)
- **constant** `profiles` (lines 105-105)
- **variable** `default_profile` (lines 109-109)
- **constant** `default_profile` (lines 109-109)
- **variable** `current_token` (lines 116-116)
- **constant** `current_token` (lines 116-116)
- **variable** `metadata` (lines 119-122)
- **constant** `metadata` (lines 119-122)
- **variable** `existing_profiles` (lines 124-124)
- **constant** `existing_profiles` (lines 124-124)
- **variable** `all_profile_names` (lines 126-126)
- **constant** `all_profile_names` (lines 126-126)
- **variable** `all_profile_names` (lines 128-128)
- **constant** `all_profile_names` (lines 128-128)
- **function** `save` (lines 145-218)
- **function** `save` (lines 146-218)
- **variable** `storage` (lines 164-164)
- **constant** `storage` (lines 164-164)
- **variable** `config` (lines 165-165)
- **constant** `config` (lines 165-165)
- **variable** `existing_profile` (lines 168-168)
- **constant** `existing_profile` (lines 168-168)
- **variable** `token` (lines 178-178)
- **constant** `token` (lines 178-178)
- **variable** `token` (lines 183-183)
- **constant** `token` (lines 183-183)
- **variable** `metadata` (lines 190-194)
- **constant** `metadata` (lines 190-194)
- **variable** `existing_profiles` (lines 198-198)
- **constant** `existing_profiles` (lines 198-198)
- **variable** `all_profile_names` (lines 200-200)
- **constant** `all_profile_names` (lines 200-200)
- **variable** `all_profile_names` (lines 202-202)
- **constant** `all_profile_names` (lines 202-202)
- **function** `switch` (lines 221-301)
- **function** `switch` (lines 222-301)
- **variable** `storage` (lines 234-234)
- **constant** `storage` (lines 234-234)
- **variable** `config` (lines 235-235)
- **constant** `config` (lines 235-235)
- **variable** `profiles` (lines 237-237)
- **constant** `profiles` (lines 237-237)
- **variable** `active_token` (lines 243-243)
- **constant** `active_token` (lines 243-243)
- **variable** `current_profile` (lines 244-244)
- **constant** `current_profile` (lines 244-244)
- **variable** `current_profile` (lines 248-248)
- **constant** `current_profile` (lines 248-248)
- **variable** `name` (lines 254-254)
- **constant** `name` (lines 254-254)
- **variable** `name` (lines 259-259)
- **constant** `name` (lines 259-259)
- **variable** `profile` (lines 270-270)
- **constant** `profile` (lines 270-270)
- **variable** `token` (lines 271-271)
- **constant** `token` (lines 271-271)
- **variable** `spinner` (lines 273-273)
- **constant** `spinner` (lines 273-273)
- **variable** `success` (lines 277-277)
- **constant** `success` (lines 277-277)
- **variable** `success` (lines 279-279)
- **constant** `success` (lines 279-279)
- **variable** `metadata` (lines 287-287)
- **constant** `metadata` (lines 287-287)
- **variable** `token_display` (lines 288-288)
- **constant** `token_display` (lines 288-288)
- **variable** `info` (lines 289-293)
- **constant** `info` (lines 289-293)
- **variable** `panel` (lines 295-295)
- **constant** `panel` (lines 295-295)
- **function** `list` (lines 304-361)
- **function** `list` (lines 305-361)
- **variable** `storage` (lines 319-319)
- **constant** `storage` (lines 319-319)
- **variable** `config` (lines 320-320)
- **constant** `config` (lines 320-320)
- **variable** `profiles` (lines 322-322)
- **constant** `profiles` (lines 322-322)
- **variable** `active_token` (lines 328-328)
- **constant** `active_token` (lines 328-328)
- **variable** `active_profile` (lines 329-329)
- **constant** `active_profile` (lines 329-329)
- **variable** `active_profile` (lines 334-334)
- **constant** `active_profile` (lines 334-334)
- **variable** `profiles` (lines 338-338)
- **constant** `profiles` (lines 338-338)
- **variable** `output` (lines 344-344)
- **constant** `output` (lines 344-344)
- **variable** `table` (lines 353-353)
- **constant** `table` (lines 353-353)
- **variable** `active_icon` (lines 355-355)
- **constant** `active_icon` (lines 355-355)
- **function** `current` (lines 364-408)
- **function** `current` (lines 365-408)
- **variable** `storage` (lines 369-369)
- **constant** `storage` (lines 369-369)
- **variable** `config` (lines 370-370)
- **constant** `config` (lines 370-370)
- **variable** `active_token` (lines 372-372)
- **constant** `active_token` (lines 372-372)
- **variable** `profiles` (lines 377-377)
- **constant** `profiles` (lines 377-377)
- **variable** `active_profile` (lines 378-378)
- **constant** `active_profile` (lines 378-378)
- **variable** `active_profile` (lines 382-382)
- **constant** `active_profile` (lines 382-382)
- **variable** `profile` (lines 386-386)
- **constant** `profile` (lines 386-386)
- **variable** `metadata` (lines 387-387)
- **constant** `metadata` (lines 387-387)
- **function** `cycle` (lines 411-491)
- **function** `cycle` (lines 412-491)
- **variable** `storage` (lines 416-416)
- **constant** `storage` (lines 416-416)
- **variable** `config` (lines 417-417)
- **constant** `config` (lines 417-417)
- **variable** `all_profiles` (lines 419-419)
- **constant** `all_profiles` (lines 419-419)
- **variable** `profiles` (lines 420-420)
- **constant** `profiles` (lines 420-420)
- **variable** `active_token` (lines 426-426)
- **constant** `active_token` (lines 426-426)
- **variable** `current_index` (lines 427-427)
- **constant** `current_index` (lines 427-427)
- **variable** `current_profile` (lines 428-428)
- **constant** `current_profile` (lines 428-428)
- **variable** `profile` (lines 432-432)
- **constant** `profile` (lines 432-432)
- **variable** `current_index` (lines 434-434)
- **constant** `current_index` (lines 434-434)
- **variable** `current_profile` (lines 435-435)
- **constant** `current_profile` (lines 435-435)
- **variable** `next_index` (lines 439-439)
- **constant** `next_index` (lines 439-439)
- **variable** `next_profile` (lines 440-440)
- **constant** `next_profile` (lines 440-440)
- **variable** `arrow` (lines 444-444)
- **constant** `arrow` (lines 444-444)
- **variable** `prev_idx` (lines 450-454)
- **constant** `prev_idx` (lines 450-454)
- **variable** `prev_profile` (lines 455-455)
- **constant** `prev_profile` (lines 455-455)
- **variable** `carousel` (lines 457-463)
- **constant** `carousel` (lines 457-463)
- **variable** `profile_data` (lines 468-468)
- **constant** `profile_data` (lines 468-468)
- **variable** `spinner` (lines 470-470)
- **constant** `spinner` (lines 470-470)
- **variable** `success` (lines 474-476)
- **constant** `success` (lines 474-476)
- **variable** `success` (lines 478-480)
- **constant** `success` (lines 478-480)
- **function** `delete` (lines 494-521)
- **function** `delete` (lines 495-521)
- **variable** `storage` (lines 504-504)
- **constant** `storage` (lines 504-504)
- **variable** `profiles` (lines 516-516)
- **constant** `profiles` (lines 516-516)
- **function** `rename` (lines 524-564)
- **function** `rename` (lines 525-564)
- **variable** `storage` (lines 530-530)
- **constant** `storage` (lines 530-530)
- **variable** `profiles` (lines 532-532)
- **constant** `profiles` (lines 532-532)
- **variable** `old_profile` (lines 542-542)
- **constant** `old_profile` (lines 542-542)
- **variable** `profiles` (lines 554-554)
- **constant** `profiles` (lines 554-554)
- **function** `export` (lines 567-629)
- **function** `export` (lines 568-629)
- **variable** `storage` (lines 580-580)
- **constant** `storage` (lines 580-580)
- **variable** `profiles` (lines 582-582)
- **constant** `profiles` (lines 582-582)
- **variable** `export_data` (lines 587-587)
- **constant** `export_data` (lines 587-587)
- **variable** `output` (lines 598-598)
- **constant** `output` (lines 598-598)
- **variable** `output` (lines 603-603)
- **constant** `output` (lines 603-603)
- **variable** `output_path` (lines 607-607)
- **constant** `output_path` (lines 607-607)
- **function** `import_profiles` (lines 632-719)
- **function** `import_profiles` (lines 633-719)
- **variable** `storage` (lines 643-643)
- **constant** `storage` (lines 643-643)
- **variable** `input_path` (lines 646-646)
- **constant** `input_path` (lines 646-646)
- **variable** `content` (lines 651-651)
- **constant** `content` (lines 651-651)
- **variable** `import_data` (lines 655-655)
- **constant** `import_data` (lines 655-655)
- **variable** `import_data` (lines 660-660)
- **constant** `import_data` (lines 660-660)
- **variable** `imported_count` (lines 673-673)
- **constant** `imported_count` (lines 673-673)
- **variable** `profile_name` (lines 675-675)
- **constant** `profile_name` (lines 675-675)
- **variable** `token` (lines 683-683)
- **constant** `token` (lines 683-683)
- **variable** `token` (lines 689-691)
- **constant** `token` (lines 689-691)
- **variable** `metadata` (lines 702-702)
- **constant** `metadata` (lines 702-702)
- **variable** `profiles` (lines 712-712)
- **constant** `profiles` (lines 712-712)
- **function** `show` (lines 722-750)
- **function** `show` (lines 723-750)
- **variable** `storage` (lines 730-730)
- **constant** `storage` (lines 730-730)
- **variable** `profile` (lines 732-732)
- **constant** `profile` (lines 732-732)
- **variable** `metadata` (lines 737-737)
- **constant** `metadata` (lines 737-737)
- **variable** `token_display` (lines 738-738)
- **constant** `token_display` (lines 738-738)
- **function** `doctor` (lines 753-818)
- **function** `doctor` (lines 754-818)
- **variable** `storage` (lines 758-758)
- **constant** `storage` (lines 758-758)
- **variable** `config` (lines 759-759)
- **constant** `config` (lines 759-759)
- **variable** `config_path` (lines 774-774)
- **constant** `config_path` (lines 774-774)
- **variable** `token_path` (lines 782-782)
- **constant** `token_path` (lines 782-782)
- **variable** `found_paths` (lines 801-801)
- **constant** `found_paths` (lines 801-801)
- **variable** `profiles` (lines 810-810)
- **constant** `profiles` (lines 810-810)
- **variable** `app` (lines 45-45)
- **variable** `help` (lines 47-47)
- **variable** `rich_markup_mode` (lines 49-49)
- **function** `get_storage` (lines 53-57)
- **variable** `interactive` (lines 65-66)
- **variable** `token_target` (lines 68-69)
- **variable** `default_profile` (lines 71-72)
- **variable** `metadata` (lines 119-119)
- **variable** `name` (lines 147-149)
- **variable** `description` (lines 151-152)
- **variable** `set_active` (lines 154-155)
- **variable** `overwrite` (lines 157-158)
- **variable** `metadata` (lines 190-190)
- **variable** `name` (lines 223-225)
- **variable** `fzf` (lines 227-228)
- **variable** `info` (lines 289-289)
- **variable** `panel` (lines 295-336)
- **variable** `profiles` (lines 338-350)
- **function** `current` (lines 365-410)
- **function** `cycle` (lines 412-493)
- **variable** `name` (lines 496-498)
- **variable** `old_name` (lines 526-536)
- **variable** `output_file` (lines 569-570)
- **variable** `include_tokens` (lines 572-573)
- **variable** `format` (lines 575-576)
- **variable** `input_file` (lines 634-636)
- **variable** `prefix` (lines 638-639)
- **variable** `token` (lines 689-689)
- **variable** `name` (lines 724-726)
- **variable** `title` (lines 747-789)
- **variable** `name` (lines 46-46)
- **variable** `no_args_is_help` (lines 48-48)
- **variable** `output` (lines 346-346)
- **variable** `export_data` (lines 589-589)
- **variable** `output_path` (lines 608-608)
- **variable** `metadata` (lines 703-703)
- **variable** `imported_count` (lines 706-706)
- **variable** `title` (lines 747-747)
- **variable** `border_style` (lines 748-748)
</details>

#### Source Code

```python
"""Main CLI interface for CC Profile Switch."""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import typer
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from .config import Config
from .fzf_integration import (
    check_fzf_available,
    fzf_select_profile,
    install_fzf_instructions,
)
from .storage import ProfileStorage
from .theme import (
    console,
    create_panel,
    get_icon,
    should_use_rich,
    show_error,
    show_header,
    show_info,
    show_spinner,
    show_success,
    show_transition,
    show_warning,
)
from .utils import (
    check_file_permissions,
    create_profile_table,
    detect_current_token,
    find_claude_config_paths,
    format_timestamp,
    mask_token,
    prompt_for_profile_selection,
    secure_file_permissions,
    validate_token,
)

app = typer.Typer(
    name="claude-profile",
    help="A cross-platform Claude profile manager with secure storage",
    no_args_is_help=True,
    rich_markup_mode="rich",
)


def get_storage() -> ProfileStorage:
    """Get the profile storage instance."""
    return ProfileStorage()


def get_config() -> Config:
    """Get the config instance."""
    return Config()


@app.command()
def init(
    interactive: bool = typer.Option(
        True, "--interactive/--no-interactive", help="Run interactive setup"
    ),
    token_target: Optional[str] = typer.Option(
        None, "--token-target", help="Path to store active token"
    ),
    default_profile: Optional[str] = typer.Option(
        None, "--default-profile", help="Default profile name"
    ),
):
    """Initialize the profile manager with guided setup."""
    show_header("Profile Manager Setup", "Initialize CCProfileSwitch")

    storage = get_storage()
    config = get_config()

    # Test keyring access
    if not storage.test_keyring_access():
        show_error("Keyring access failed. Please check your system keyring setup.")
        raise typer.Exit(1)

    console.print(
        f"[green]✓ Keyring backend: {storage.check_keyring_backend()}[/green]"
    )

    # Setup token target - auto-use default or first found path
    if not token_target:
        found_paths = find_claude_config_paths()
        if found_paths:
            token_target = str(found_paths[0])
            show_info(f"Using existing Claude config: {token_target}")
        else:
            token_target = str(config.get_active_token_path())
            show_info(f"Using default token path: {token_target}")

    config.set_active_token_target("file", token_target)
    show_success(f"Active token storage: {token_target}")

    # Setup default profile
    if interactive and not default_profile:
        profiles = storage.list_profiles()
        if profiles:
            console.print("\n[bold]Default Profile Configuration[/bold]")
            if Confirm.ask("Set a default profile?", default=False):
                default_profile = prompt_for_profile_selection(profiles)

    if default_profile:
        config.set_default_profile(default_profile)
        show_success(f"Default profile set to: {default_profile}")

    # Import existing token if found - auto-import without asking
    current_token = detect_current_token()
    if current_token and validate_token(current_token):
        show_info(f"Detected current token: {mask_token(current_token)}")
        metadata = {
            "created": datetime.now().isoformat(),
            "description": "Auto-imported from existing configuration",
        }
        if storage.save_profile("default", current_token, metadata):
            existing_profiles = storage.list_profiles()
            if existing_profiles:
                all_profile_names = [k for k in existing_profiles.keys()]
            else:
                all_profile_names = []

            if "default" not in all_profile_names:
                all_profile_names.insert(0, "default")
            storage.update_profile_list(all_profile_names)
            show_success("Auto-imported current token as 'default' profile")
    else:
        show_warning(
            "No current token detected - use 'claude-profile save <name>' "
            "to create your first profile"
        )

    show_success(
        "Setup complete! You can now use 'claude-profile save', 'switch', 'list' etc."
    )


@app.command()
def save(
    name: str = typer.Argument(..., help="Profile name to save"),
    token: Optional[str] = typer.Option(
        None, "--token", help="Claude token (will prompt if not provided)"
    ),
    description: Optional[str] = typer.Option(
        None, "--description", help="Profile description"
    ),
    set_active: bool = typer.Option(
        True, "--active/--no-active", help="Set as active profile after saving"
    ),
    overwrite: bool = typer.Option(
        False, "--overwrite/--no-overwrite", help="Overwrite existing profile"
    ),
):
    """Save the current or provided token as a named profile."""
    show_header("Save Profile", f"Save profile '{name}'")

    storage = get_storage()
    config = get_config()

    # Check if profile exists
    existing_profile = storage.get_profile(name)
    if existing_profile and not overwrite:
        if not Confirm.ask(
            f"Profile '{name}' already exists. Overwrite?", default=False
        ):
            console.print("Operation cancelled.")
            raise typer.Exit()

    # Get token
    if not token:
        token = detect_current_token()
        if token:
            show_info(f"Auto-detected current token: {mask_token(token)}")
        else:
            show_warning("No current token detected - please enter manually")
            token = Prompt.ask("Enter your Claude token", password=True)

    if not validate_token(token):
        show_error("Invalid token format")
        raise typer.Exit(1)

    # Save profile
    metadata = {
        "created": datetime.now().isoformat(),
        "description": description
        or f"Profile saved on {datetime.now().strftime('%Y-%m-%d')}",
    }

    if storage.save_profile(name, token, metadata):
        # Update profile list - get existing profiles and add the new one
        existing_profiles = storage.list_profiles()
        if existing_profiles and hasattr(existing_profiles, "keys"):
            all_profile_names = [k for k in existing_profiles.keys()]
        else:
            all_profile_names = []

        if name not in all_profile_names:
            all_profile_names.append(name)
        storage.update_profile_list(all_profile_names)

        show_success(f"Profile '{name}' saved successfully")

        # Set as active if requested
        if set_active:
            if storage.save_active_token(token, config.get_active_token_path()):
                show_success(f"Profile '{name}' is now active")
            else:
                show_warning("Profile saved but could not set as active")
    else:
        show_error(f"Failed to save profile '{name}'")
        raise typer.Exit(1)


@app.command()
def switch(
    name: Optional[str] = typer.Argument(None, help="Profile name to switch to"),
    show_tokens: bool = typer.Option(
        False, "--show-tokens", help="Show tokens in selection list"
    ),
    fzf: bool = typer.Option(
        False, "--fzf/--no-fzf", help="Use fzf for interactive selection"
    ),
):
    """Switch to a different profile (interactive if no name provided)."""
    show_header("Profile Switch", "Switch between Claude profiles")

    storage = get_storage()
    config = get_config()

    profiles = storage.list_profiles()
    if not profiles:
        show_error("No profiles found. Use 'claude-profile save' to create one.")
        raise typer.Exit(1)

    # Get current profile for transition display
    active_token = storage.get_active_token(config.get_active_token_path())
    current_profile = None
    if active_token:
        for pname, pdata in profiles.items():
            if pdata["token"] == active_token:
                current_profile = pname
                break

    # Get profile name
    if not name:
        if fzf and check_fzf_available():
            name = fzf_select_profile(profiles, show_tokens)
        else:
            if fzf and not check_fzf_available():
                show_warning("fzf not available, falling back to regular selection")
                install_fzf_instructions()
            name = prompt_for_profile_selection(profiles, show_tokens)

        if not name:
            console.print("No profile selected.")
            raise typer.Exit()

    if name not in profiles:
        show_error(f"Profile '{name}' not found")
        raise typer.Exit(1)

    # Switch profile with spinner
    profile = profiles[name]
    token = profile["token"]

    spinner = show_spinner(f"Switching to profile '{name}'...")
    if spinner:
        with spinner:
            time.sleep(0.5)  # Brief delay for visual feedback
            success = storage.save_active_token(token, config.get_active_token_path())
    else:
        success = storage.save_active_token(token, config.get_active_token_path())

    if success:
        if current_profile:
            show_transition(current_profile, name)
        show_success(f"Switched to profile '{name}'")

        # Show profile info in a panel
        metadata = profile.get("metadata", {})
        token_display = token if show_tokens else mask_token(token)
        info = (
            f"[dim]Description:[/dim] {metadata.get('description', 'No description')}\n"
            f"[dim]Created:[/dim] {format_timestamp(metadata.get('created'))}\n"
            f"[dim]Token:[/dim] {token_display}"
        )
        if should_use_rich():
            panel = create_panel(info, title=f"Profile: {name}", border_style="success")
            console.print(panel)
        else:
            console.print(info)
    else:
        show_error(f"Failed to switch to profile '{name}'")
        raise typer.Exit(1)


@app.command()
def list(
    show_tokens: bool = typer.Option(
        False, "--show-tokens", help="Show actual tokens instead of masked"
    ),
    output_format: str = typer.Option(
        "table", "--output-format", help="Output format (table, json)"
    ),
    active_only: bool = typer.Option(
        False, "--active-only", help="Show only the active profile"
    ),
):
    """List all saved profiles."""
    show_header("Profile List", "View all saved Claude profiles")

    storage = get_storage()
    config = get_config()

    profiles = storage.list_profiles()
    if not profiles:
        show_info("No profiles found")
        return

    # Get active token
    active_token = storage.get_active_token(config.get_active_token_path())
    active_profile = None

    if active_token:
        for name, data in profiles.items():
            if data["token"] == active_token:
                active_profile = name
                break

    if active_only and active_profile:
        profiles = {active_profile: profiles[active_profile]}
    elif active_only and not active_profile:
        show_info("No active profile found")
        return

    if output_format == "json":
        output = {}
        for name, data in profiles.items():
            output[name] = {
                "token": data["token"] if show_tokens else mask_token(data["token"]),
                "metadata": data.get("metadata", {}),
                "active": name == active_profile,
            }
        console.print(json.dumps(output, indent=2))
    else:
        table = create_profile_table(profiles, show_tokens, active_profile)
        if active_profile:
            active_icon = get_icon("active")
            console.print(
                f"[success]{active_icon} Active profile: "
                f"[bold]{active_profile}[/bold][/success]"
            )
            console.print()
        console.print(table)


@app.command()
def current():
    """Show the currently active profile."""
    show_header("Current Profile", "View active profile details")

    storage = get_storage()
    config = get_config()

    active_token = storage.get_active_token(config.get_active_token_path())
    if not active_token:
        show_info("No active profile found")
        return

    profiles = storage.list_profiles()
    active_profile = None

    for name, data in profiles.items():
        if data["token"] == active_token:
            active_profile = name
            break

    if active_profile:
        profile = profiles[active_profile]
        metadata = profile.get("metadata", {})

        console.print(
            Panel(
                f"[bold green]Active Profile: {active_profile}[/bold green]\n\n"
                f"[dim]Description: "
                f"{metadata.get('description', 'No description')}[/dim]\n"
                f"[dim]Created: {format_timestamp(metadata.get('created'))}[/dim]\n"
                f"[dim]Token: {mask_token(active_token)}[/dim]",
                title="Current Profile",
                border_style="green",
            )
        )
    else:
        console.print(
            Panel(
                f"[dim]Token: {mask_token(active_token)}[/dim]\n"
                f"[yellow]This token is not associated with any saved profile[/yellow]",
                title="Current Token",
                border_style="yellow",
            )
        )


@app.command()
def cycle():
    """Cycle through available profiles."""
    show_header("Profile Cycle", "Cycle to next profile")

    storage = get_storage()
    config = get_config()

    all_profiles = storage.list_profiles()
    profiles = [k for k in all_profiles.keys()] if all_profiles else []
    if len(profiles) < 2:
        show_error("Need at least 2 profiles to cycle")
        raise typer.Exit(1)

    # Get current active profile
    active_token = storage.get_active_token(config.get_active_token_path())
    current_index = -1
    current_profile = None

    if active_token:
        for i, name in enumerate(profiles):
            profile = storage.get_profile(name)
            if profile and profile["token"] == active_token:
                current_index = i
                current_profile = name
                break

    # Calculate next profile
    next_index = (current_index + 1) % len(profiles)
    next_profile = profiles[next_index]

    # Show carousel animation
    if should_use_rich():
        arrow = get_icon("arrow")
        console.print()
        console.print("[muted]Cycling profiles...[/muted]")
        console.print()

        # Show profile carousel
        prev_idx = (
            (current_index - 1) % len(profiles)
            if current_index >= 0
            else len(profiles) - 1
        )
        prev_profile = profiles[prev_idx]

        carousel = (
            f"  [dim]{prev_profile}[/dim] "
            f"{arrow} "
            f"[bold]{profiles[current_index] if current_index >= 0 else '?'}[/bold] "
            f"{arrow} "
            f"[highlight bold]{next_profile}[/highlight bold]"
        )
        console.print(carousel)
        console.print()

    # Perform the switch
    profile_data = storage.get_profile(next_profile)
    if profile_data:
        spinner = show_spinner(f"Switching to '{next_profile}'...")
        if spinner:
            with spinner:
                time.sleep(0.4)  # Brief animation
                success = storage.save_active_token(
                    profile_data["token"], config.get_active_token_path()
                )
        else:
            success = storage.save_active_token(
                profile_data["token"], config.get_active_token_path()
            )

        if success:
            if current_profile:
                show_transition(current_profile, next_profile)
            show_success(f"Cycled to profile '{next_profile}'")
        else:
            show_error(f"Failed to cycle to profile '{next_profile}'")
            raise typer.Exit(1)
    else:
        show_error(f"Failed to retrieve profile '{next_profile}'")
        raise typer.Exit(1)


@app.command()
def delete(
    name: str = typer.Argument(..., help="Profile name to delete"),
    confirm: bool = typer.Option(
        True, "--confirm/--no-confirm", help="Confirm before deletion"
    ),
):
    """Delete a saved profile."""
    show_header("Delete Profile", f"Delete profile '{name}'")

    storage = get_storage()

    if name not in storage.list_profiles():
        show_error(f"Profile '{name}' not found")
        raise typer.Exit(1)

    if confirm and not Confirm.ask(f"Delete profile '{name}'?", default=False):
        console.print("Operation cancelled.")
        raise typer.Exit()

    if storage.delete_profile(name):
        # Update profile list
        profiles = storage.list_profiles()
        storage.update_profile_list([k for k in profiles.keys()] if profiles else [])
        show_success(f"Profile '{name}' deleted")
    else:
        show_error(f"Failed to delete profile '{name}'")
        raise typer.Exit(1)


@app.command()
def rename(
    old_name: str = typer.Argument(..., help="Current profile name"),
    new_name: str = typer.Argument(..., help="New profile name"),
):
    """Rename a saved profile."""
    storage = get_storage()

    profiles = storage.list_profiles()
    if old_name not in profiles:
        show_error(f"Profile '{old_name}' not found")
        raise typer.Exit(1)

    if new_name in profiles:
        show_error(f"Profile '{new_name}' already exists")
        raise typer.Exit(1)

    # Get old profile data
    old_profile = storage.get_profile(old_name)
    if not old_profile:
        show_error(f"Could not retrieve profile '{old_name}'")
        raise typer.Exit(1)

    # Save with new name
    if storage.save_profile(
        new_name, old_profile["token"], old_profile.get("metadata", {})
    ):
        # Delete old profile
        if storage.delete_profile(old_name):
            # Update profile list
            profiles = storage.list_profiles()
            storage.update_profile_list(
                [k for k in profiles.keys()] if profiles else []
            )
            show_success(f"Profile renamed from '{old_name}' to '{new_name}'")
        else:
            show_error(f"Renamed but failed to delete old profile '{old_name}'")
            raise typer.Exit(1)
    else:
        show_error(f"Failed to rename profile '{old_name}'")
        raise typer.Exit(1)


@app.command()
def export(
    output_file: Optional[str] = typer.Argument(
        None, help="Output file path (prints to stdout if not provided)"
    ),
    include_tokens: bool = typer.Option(
        False, "--include-tokens", help="Include actual tokens in export"
    ),
    format: str = typer.Option(
        "json", "--export-format", help="Export format (json, yaml)"
    ),
):
    """Export profiles to a file."""
    storage = get_storage()

    profiles = storage.list_profiles()
    if not profiles:
        show_info("No profiles to export")
        return

    export_data = {}
    for name, data in profiles.items():
        export_data[name] = {
            "metadata": data.get("metadata", {}),
            "token": data["token"] if include_tokens else mask_token(data["token"]),
        }

    if format.lower() == "yaml":
        try:
            import yaml  # type: ignore[import-untyped]

            output = yaml.dump(export_data, default_flow_style=False)
        except ImportError:
            show_error("PyYAML is required for YAML export")
            raise typer.Exit(1)
    else:
        output = json.dumps(export_data, indent=2)

    if output_file:
        try:
            output_path = Path(output_file).expanduser()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(output)
            show_success(f"Profiles exported to {output_path}")
        except Exception as e:
            show_error(f"Failed to write export file: {e}")
            raise typer.Exit(1)
    else:
        console.print(output)

    if not include_tokens:
        show_info(
            "Tokens are masked in the export. "
            "Use --include-tokens to export real tokens."
        )
    else:
        show_warning(
            "⚠️  SECURITY WARNING: Exported file contains plaintext API tokens!\n\n"
            "Recommended: Encrypt the export file immediately:\n"
            "  Using GPG: cat export.json | gpg -c > export.json.gpg\n"
            "  Using age: cat export.json | age -p > export.json.age\n\n"
            "Delete the plaintext file after encryption."
        )


@app.command()
def import_profiles(
    input_file: str = typer.Argument(..., help="Input file path"),
    merge: bool = typer.Option(
        True, "--merge/--replace", help="Merge with existing profiles"
    ),
    prefix: Optional[str] = typer.Option(
        None, "--prefix", help="Prefix for imported profile names"
    ),
):
    """Import profiles from a file."""
    storage = get_storage()

    try:
        input_path = Path(input_file).expanduser()
        if not input_path.exists():
            show_error(f"File not found: {input_file}")
            raise typer.Exit(1)

        content = input_path.read_text()

        # Try JSON first, then YAML
        try:
            import_data = json.loads(content)
        except json.JSONDecodeError:
            try:
                import yaml

                import_data = yaml.safe_load(content)
            except ImportError:
                show_error("PyYAML is required for YAML import")
                raise typer.Exit(1)
            except yaml.YAMLError:
                show_error("Invalid file format")
                raise typer.Exit(1)

        if not isinstance(import_data, dict):
            show_error("Invalid import file format")
            raise typer.Exit(1)

        # Import profiles
        imported_count = 0
        for name, data in import_data.items():
            profile_name = f"{prefix}{name}" if prefix else name

            if not merge and profile_name in storage.list_profiles():
                console.print(
                    f"[yellow]Skipping existing profile: {profile_name}[/yellow]"
                )
                continue

            token = data.get("token")
            if not token or not validate_token(token):
                show_warning(
                    f"Profile '{profile_name}' has no usable token in the import file"
                )
                if Confirm.ask("Provide the token now?", default=True):
                    token = Prompt.ask(
                        f"Enter token for '{profile_name}'", password=True
                    ).strip()
                    if not token or not validate_token(token):
                        show_warning(
                            f"Skipping profile '{profile_name}' - "
                            f"provided token invalid"
                        )
                        continue
                else:
                    show_warning(f"Skipping profile '{profile_name}' - token missing")
                    continue

            metadata = data.get("metadata", {})
            metadata["imported"] = datetime.now().isoformat()

            if storage.save_profile(profile_name, token, metadata):
                imported_count += 1
                console.print(f"[green]Imported: {profile_name}[/green]")
            else:
                show_error(f"Failed to import: {profile_name}")

        # Update profile list
        profiles = storage.list_profiles()
        storage.update_profile_list([k for k in profiles.keys()] if profiles else [])

        show_success(f"Imported {imported_count} profiles")

    except Exception as e:
        show_error(f"Import failed: {e}")
        raise typer.Exit(1)


@app.command()
def show(
    name: str = typer.Argument(..., help="Profile name to show"),
    show_token: bool = typer.Option(
        False, "--show-token", help="Show the actual token"
    ),
):
    """Show details of a specific profile."""
    storage = get_storage()

    profile = storage.get_profile(name)
    if not profile:
        show_error(f"Profile '{name}' not found")
        raise typer.Exit(1)

    metadata = profile.get("metadata", {})
    token_display = profile["token"] if show_token else mask_token(profile["token"])

    console.print(
        Panel(
            f"[bold]Profile: {name}[/bold]\n\n"
            f"[dim]Token: {token_display}[/dim]\n"
            f"[dim]Created: {format_timestamp(metadata.get('created'))}[/dim]\n"
            f"[dim]Description: {metadata.get('description', 'No description')}[/dim]\n"
            f"[dim]Imported: {format_timestamp(metadata.get('imported'))}[/dim]",
            title=f"Profile Details: {name}",
            border_style="blue",
        )
    )


@app.command()
def doctor():
    """Check system configuration and diagnose issues."""
    show_header("System Check", "Diagnose configuration issues")

    storage = get_storage()
    config = get_config()

    # Check keyring
    console.print("[bold]Keyring Check:[/bold]")
    if storage.test_keyring_access():
        console.print(
            f"[green]✓ Keyring accessible: {storage.check_keyring_backend()}[/green]"
        )
    else:
        console.print("[red]✗ Keyring access failed[/red]")

    # Check config directory
    console.print("\n[bold]Configuration Check:[/bold]")
    try:
        config.ensure_config_dir()
        config_path = config.get_config_path()
        # Use print to avoid Rich text wrapping
        print(f"\033[32m✓ Config directory: {config_path}\033[0m")
    except Exception as e:
        console.print(f"[red]✗ Config directory error: {e}[/red]")

    # Check active token file
    console.print("\n[bold]Active Token Check:[/bold]")
    token_path = Path(config.get_active_token_path())
    if token_path.exists():
        console.print(f"[green]✓ Token file exists: {token_path}[/green]")
        if check_file_permissions(token_path):
            console.print("[green]✓ File permissions are secure (0600)[/green]")
        else:
            console.print(
                "[yellow]⚠ File permissions are not secure (should be 0600)[/yellow]"
            )
            if Confirm.ask("Fix file permissions?", default=True):
                if secure_file_permissions(token_path):
                    console.print("[green]✓ File permissions fixed[/green]")
                else:
                    console.print("[red]✗ Failed to fix file permissions[/red]")
    else:
        console.print(f"[yellow]⚠ Token file does not exist: {token_path}[/yellow]")

    # Check for existing Claude configurations
    console.print("\n[bold]Existing Claude Configurations:[/bold]")
    found_paths = find_claude_config_paths()
    if found_paths:
        for path in found_paths:
            console.print(f"[green]✓ Found: {path}[/green]")
    else:
        console.print("[yellow]⚠ No existing Claude configurations found[/yellow]")

    # Check profiles
    console.print("\n[bold]Profiles Check:[/bold]")
    profiles = storage.list_profiles()
    if profiles:
        console.print(f"[green]✓ Found {len(profiles)} profiles[/green]")
        for name in profiles:
            console.print(f"  - {name}")
    else:
        console.print("[yellow]⚠ No profiles found[/yellow]")

    console.print("\n[bold green]System check complete![/bold green]")


if __name__ == "__main__":
    app()

```

---

### 9. /Users/biostochastics/CCProfileSwitch/conftest.py {#users-biostochastics-ccprofileswitch-conftest-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-cc-profile-switch-cli-py) | 
[Next →](#users-biostochastics-ccprofileswitch-claude-profile-manager-typer-rich-py)


#### Summary

> Contains 7 functions, 1 classes

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 57 |
| Functions/Classes | 18 |

<details>
<summary>📦 Declarations</summary>

- **function** `isolated_cc_profile_env` (lines 15-57)
- **function** `isolated_cc_profile_env` (lines 16-57)
- **variable** `keyring_store` (lines 19-19)
- **constant** `keyring_store` (lines 19-19)
- **function** `fake_set_password` (lines 21-22)
- **function** `fake_get_password` (lines 24-25)
- **function** `fake_delete_password` (lines 27-32)
- **class** `FakeKeyringBackend` (lines 34-38)
- **variable** `__module__` (lines 37-37)
- **constant** `__module__` (lines 37-37)
- **variable** `__name__` (lines 38-38)
- **constant** `__name__` (lines 38-38)
- **variable** `config_root` (lines 47-47)
- **constant** `config_root` (lines 47-47)
- **function** `fake_user_config_dir` (lines 49-52)
- **variable** `path` (lines 50-50)
- **constant** `path` (lines 50-50)
- **function** `isolated_cc_profile_env` (lines 16-58)
</details>

#### Source Code

```python
"""Pytest fixtures for CC Profile Switch tests."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import pytest

from cc_profile_switch import config as config_module
from cc_profile_switch import storage as storage_module
from cc_profile_switch import utils as utils_module


@pytest.fixture(autouse=True)
def isolated_cc_profile_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Provide an isolated config directory and in-memory keyring for every test."""

    keyring_store: Dict[Tuple[str, str], str] = {}

    def fake_set_password(service: str, key: str, value: str) -> None:
        keyring_store[(service, key)] = value

    def fake_get_password(service: str, key: str):  # type: ignore[override]
        return keyring_store.get((service, key))

    def fake_delete_password(service: str, key: str) -> None:
        if (service, key) not in keyring_store:
            raise storage_module.keyring.errors.PasswordDeleteError(
                "Password not found"
            )
        del keyring_store[(service, key)]

    class FakeKeyringBackend:
        """Simple stand-in object so the doctor command can report a backend name."""

        __module__ = "cc_profile_switch.tests"
        __name__ = "InMemoryKeyring"

    monkeypatch.setattr(storage_module.keyring, "set_password", fake_set_password)
    monkeypatch.setattr(storage_module.keyring, "get_password", fake_get_password)
    monkeypatch.setattr(storage_module.keyring, "delete_password", fake_delete_password)
    monkeypatch.setattr(
        storage_module.keyring, "get_keyring", lambda: FakeKeyringBackend()
    )

    config_root = tmp_path / "config"

    def fake_user_config_dir(app_name: str) -> str:
        path = config_root / app_name
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    monkeypatch.setattr(storage_module, "_user_config_dir", fake_user_config_dir)
    monkeypatch.setattr(config_module, "_user_config_dir", fake_user_config_dir)

    monkeypatch.setattr(utils_module, "find_claude_config_paths", lambda: [])

```

---

### 10. /Users/biostochastics/CCProfileSwitch/claude_profile_manager_typer_rich.py {#users-biostochastics-ccprofileswitch-claude-profile-manager-typer-rich-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-conftest-py) | 
[Next →](#users-biostochastics-ccprofileswitch-tests-test-cli-py)


#### Summary

> Contains 31 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 837 |
| Functions/Classes | 271 |

<details>
<summary>📦 Declarations</summary>

- **variable** `app` (lines 53-58)
- **constant** `app` (lines 53-58)
- **variable** `console` (lines 60-60)
- **constant** `console` (lines 60-60)
- **function** `get_storage` (lines 63-65)
- **function** `get_config` (lines 68-70)
- **function** `init` (lines 73-163)
- **function** `init` (lines 74-163)
- **variable** `storage` (lines 89-89)
- **constant** `storage` (lines 89-89)
- **variable** `config` (lines 90-90)
- **constant** `config` (lines 90-90)
- **variable** `found_paths` (lines 108-108)
- **constant** `found_paths` (lines 108-108)
- **variable** `choice` (lines 115-118)
- **constant** `choice` (lines 115-118)
- **variable** `token_target` (lines 119-119)
- **constant** `token_target` (lines 119-119)
- **variable** `default_path` (lines 122-122)
- **constant** `default_path` (lines 122-122)
- **variable** `token_target` (lines 123-125)
- **constant** `token_target` (lines 123-125)
- **variable** `profiles` (lines 133-133)
- **constant** `profiles` (lines 133-133)
- **variable** `default_profile` (lines 137-137)
- **constant** `default_profile` (lines 137-137)
- **variable** `current_token` (lines 145-145)
- **constant** `current_token` (lines 145-145)
- **variable** `metadata` (lines 151-154)
- **constant** `metadata` (lines 151-154)
- **function** `save` (lines 166-228)
- **function** `save` (lines 167-228)
- **variable** `storage` (lines 183-183)
- **constant** `storage` (lines 183-183)
- **variable** `config` (lines 184-184)
- **constant** `config` (lines 184-184)
- **variable** `existing_profile` (lines 187-187)
- **constant** `existing_profile` (lines 187-187)
- **variable** `token` (lines 197-197)
- **constant** `token` (lines 197-197)
- **variable** `token` (lines 199-199)
- **constant** `token` (lines 199-199)
- **variable** `metadata` (lines 206-210)
- **constant** `metadata` (lines 206-210)
- **variable** `profiles` (lines 214-214)
- **constant** `profiles` (lines 214-214)
- **function** `switch` (lines 231-273)
- **function** `switch` (lines 232-273)
- **variable** `storage` (lines 239-239)
- **constant** `storage` (lines 239-239)
- **variable** `config` (lines 240-240)
- **constant** `config` (lines 240-240)
- **variable** `profiles` (lines 242-242)
- **constant** `profiles` (lines 242-242)
- **variable** `name` (lines 249-249)
- **constant** `name` (lines 249-249)
- **variable** `profile` (lines 259-259)
- **constant** `profile` (lines 259-259)
- **variable** `token` (lines 260-260)
- **constant** `token` (lines 260-260)
- **variable** `metadata` (lines 266-266)
- **constant** `metadata` (lines 266-266)
- **function** `list` (lines 276-326)
- **function** `list` (lines 277-326)
- **variable** `storage` (lines 289-289)
- **constant** `storage` (lines 289-289)
- **variable** `config` (lines 290-290)
- **constant** `config` (lines 290-290)
- **variable** `profiles` (lines 292-292)
- **constant** `profiles` (lines 292-292)
- **variable** `active_token` (lines 298-298)
- **constant** `active_token` (lines 298-298)
- **variable** `active_profile` (lines 299-299)
- **constant** `active_profile` (lines 299-299)
- **variable** `active_profile` (lines 304-304)
- **constant** `active_profile` (lines 304-304)
- **variable** `profiles` (lines 308-308)
- **constant** `profiles` (lines 308-308)
- **variable** `output` (lines 314-314)
- **constant** `output` (lines 314-314)
- **variable** `table` (lines 323-323)
- **constant** `table` (lines 323-323)
- **function** `current` (lines 329-370)
- **function** `current` (lines 330-370)
- **variable** `storage` (lines 332-332)
- **constant** `storage` (lines 332-332)
- **variable** `config` (lines 333-333)
- **constant** `config` (lines 333-333)
- **variable** `active_token` (lines 335-335)
- **constant** `active_token` (lines 335-335)
- **variable** `profiles` (lines 340-340)
- **constant** `profiles` (lines 340-340)
- **variable** `active_profile` (lines 341-341)
- **constant** `active_profile` (lines 341-341)
- **variable** `active_profile` (lines 345-345)
- **constant** `active_profile` (lines 345-345)
- **variable** `profile` (lines 349-349)
- **constant** `profile` (lines 349-349)
- **variable** `metadata` (lines 350-350)
- **constant** `metadata` (lines 350-350)
- **function** `cycle` (lines 373-407)
- **function** `cycle` (lines 374-407)
- **variable** `storage` (lines 376-376)
- **constant** `storage` (lines 376-376)
- **variable** `config` (lines 377-377)
- **constant** `config` (lines 377-377)
- **variable** `profiles` (lines 379-379)
- **constant** `profiles` (lines 379-379)
- **variable** `active_token` (lines 385-385)
- **constant** `active_token` (lines 385-385)
- **variable** `current_index` (lines 386-386)
- **constant** `current_index` (lines 386-386)
- **variable** `profile` (lines 390-390)
- **constant** `profile` (lines 390-390)
- **variable** `current_index` (lines 392-392)
- **constant** `current_index` (lines 392-392)
- **variable** `next_index` (lines 396-396)
- **constant** `next_index` (lines 396-396)
- **variable** `next_profile` (lines 397-397)
- **constant** `next_profile` (lines 397-397)
- **variable** `profile_data` (lines 400-400)
- **constant** `profile_data` (lines 400-400)
- **function** `delete` (lines 410-435)
- **function** `delete` (lines 411-435)
- **variable** `storage` (lines 418-418)
- **constant** `storage` (lines 418-418)
- **variable** `profiles` (lines 430-430)
- **constant** `profiles` (lines 430-430)
- **function** `rename` (lines 438-476)
- **function** `rename` (lines 439-476)
- **variable** `storage` (lines 444-444)
- **constant** `storage` (lines 444-444)
- **variable** `profiles` (lines 446-446)
- **constant** `profiles` (lines 446-446)
- **variable** `old_profile` (lines 456-456)
- **constant** `old_profile` (lines 456-456)
- **variable** `profiles` (lines 468-468)
- **constant** `profiles` (lines 468-468)
- **function** `export` (lines 479-532)
- **function** `export` (lines 480-532)
- **variable** `storage` (lines 492-492)
- **constant** `storage` (lines 492-492)
- **variable** `profiles` (lines 494-494)
- **constant** `profiles` (lines 494-494)
- **variable** `export_data` (lines 499-499)
- **constant** `export_data` (lines 499-499)
- **variable** `output` (lines 510-510)
- **constant** `output` (lines 510-510)
- **variable** `output` (lines 515-515)
- **constant** `output` (lines 515-515)
- **variable** `output_path` (lines 519-519)
- **constant** `output_path` (lines 519-519)
- **function** `import_profiles` (lines 535-621)
- **function** `import_profiles` (lines 536-621)
- **variable** `storage` (lines 546-546)
- **constant** `storage` (lines 546-546)
- **variable** `input_path` (lines 549-549)
- **constant** `input_path` (lines 549-549)
- **variable** `content` (lines 554-554)
- **constant** `content` (lines 554-554)
- **variable** `import_data` (lines 558-558)
- **constant** `import_data` (lines 558-558)
- **variable** `import_data` (lines 563-563)
- **constant** `import_data` (lines 563-563)
- **variable** `imported_count` (lines 576-576)
- **constant** `imported_count` (lines 576-576)
- **variable** `profile_name` (lines 578-578)
- **constant** `profile_name` (lines 578-578)
- **variable** `token` (lines 586-586)
- **constant** `token` (lines 586-586)
- **variable** `token` (lines 592-594)
- **constant** `token` (lines 592-594)
- **variable** `metadata` (lines 604-604)
- **constant** `metadata` (lines 604-604)
- **variable** `profiles` (lines 614-614)
- **constant** `profiles` (lines 614-614)
- **function** `show` (lines 624-652)
- **function** `show` (lines 625-652)
- **variable** `storage` (lines 632-632)
- **constant** `storage` (lines 632-632)
- **variable** `profile` (lines 634-634)
- **constant** `profile` (lines 634-634)
- **variable** `metadata` (lines 639-639)
- **constant** `metadata` (lines 639-639)
- **variable** `token_display` (lines 640-640)
- **constant** `token_display` (lines 640-640)
- **function** `doctor` (lines 655-719)
- **function** `doctor` (lines 656-719)
- **variable** `storage` (lines 661-661)
- **constant** `storage` (lines 661-661)
- **variable** `config` (lines 662-662)
- **constant** `config` (lines 662-662)
- **variable** `token_path` (lines 683-683)
- **constant** `token_path` (lines 683-683)
- **variable** `found_paths` (lines 702-702)
- **constant** `found_paths` (lines 702-702)
- **variable** `profiles` (lines 711-711)
- **constant** `profiles` (lines 711-711)
- **function** `completions` (lines 722-833)
- **function** `completions` (lines 723-833)
- **variable** `script_path` (lines 728-728)
- **constant** `script_path` (lines 728-728)
- **variable** `completion_script` (lines 731-746)
- **constant** `completion_script` (lines 731-746)
- **variable** `completion_script` (lines 748-770)
- **constant** `completion_script` (lines 748-770)
- **variable** `completion_script` (lines 772-788)
- **constant** `completion_script` (lines 772-788)
- **variable** `completion_script` (lines 790-797)
- **constant** `completion_script` (lines 790-797)
- **variable** `comp_file` (lines 811-811)
- **constant** `comp_file` (lines 811-811)
- **variable** `comp_file` (lines 819-825)
- **constant** `comp_file` (lines 819-825)
- **variable** `app` (lines 53-53)
- **variable** `help` (lines 55-55)
- **variable** `rich_markup_mode` (lines 57-57)
- **function** `get_storage` (lines 63-67)
- **variable** `interactive` (lines 75-76)
- **variable** `token_target` (lines 78-79)
- **variable** `default_profile` (lines 81-82)
- **variable** `choice` (lines 115-115)
- **variable** `choices` (lines 117-117)
- **variable** `metadata` (lines 151-151)
- **variable** `name` (lines 168-170)
- **variable** `description` (lines 172-173)
- **variable** `set_active` (lines 175-176)
- **variable** `overwrite` (lines 178-179)
- **variable** `metadata` (lines 206-206)
- **variable** `name` (lines 233-235)
- **variable** `show_tokens` (lines 278-279)
- **variable** `output_format` (lines 281-282)
- **variable** `active_only` (lines 284-285)
- **variable** `profiles` (lines 308-320)
- **function** `current` (lines 330-372)
- **function** `cycle` (lines 374-409)
- **variable** `name` (lines 412-414)
- **variable** `old_name` (lines 440-450)
- **variable** `output_file` (lines 481-482)
- **variable** `include_tokens` (lines 484-485)
- **variable** `format` (lines 487-488)
- **variable** `input_file` (lines 537-539)
- **variable** `prefix` (lines 541-542)
- **variable** `token` (lines 592-592)
- **variable** `name` (lines 626-628)
- **variable** `title` (lines 649-690)
- **variable** `shell` (lines 724-732)
- **constant** `COMPREPLY` (lines 735-735)
- **variable** `prev` (lines 737-737)
- **constant** `COMPREPLY` (lines 741-741)
- **variable** `completion_script` (lines 748-748)
- **variable** `commands` (lines 752-752)
- **variable** `completion_script` (lines 772-772)
- **variable** `completion_script` (lines 790-790)
- **variable** `comp_file` (lines 819-819)
- **variable** `name` (lines 54-54)
- **variable** `no_args_is_help` (lines 56-56)
- **variable** `token_target` (lines 123-123)
- **variable** `output` (lines 316-316)
- **variable** `export_data` (lines 501-501)
- **variable** `output_path` (lines 520-520)
- **variable** `metadata` (lines 605-605)
- **variable** `imported_count` (lines 608-608)
- **variable** `title` (lines 649-649)
- **variable** `border_style` (lines 650-650)
- **variable** `completion_script` (lines 731-731)
- **variable** `cur` (lines 736-736)
- **variable** `opts` (lines 738-738)
- **variable** `comp_file` (lines 812-812)
- **variable** `console` (lines 816-816)
- **variable** `comp_file` (lines 826-826)
</details>

#### Source Code

```python
#!/usr/bin/env python3
"""
Standalone Claude Profile Manager with Typer + Rich
A cross-platform Claude profile manager with interactive guided setup.

Install dependencies:
pip install typer[all] rich keyring platformdirs

Usage:
python claude_profile_manager_typer_rich.py --help
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Add the package to Python path for standalone execution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import typer
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm, Prompt
except ImportError as e:
    print(f"Missing required dependency: {e}")
    print("Install with: pip install typer[all] rich keyring platformdirs")
    sys.exit(1)

from cc_profile_switch.config import Config

# Import our modules
from cc_profile_switch.storage import ProfileStorage
from cc_profile_switch.utils import (
    check_file_permissions,
    create_profile_table,
    detect_current_token,
    find_claude_config_paths,
    format_timestamp,
    mask_token,
    prompt_for_profile_selection,
    secure_file_permissions,
    show_error,
    show_info,
    show_success,
    show_warning,
    validate_token,
)

app = typer.Typer(
    name="claude-profile",
    help="A cross-platform Claude profile manager with secure storage",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

console = Console()


def get_storage() -> ProfileStorage:
    """Get the profile storage instance."""
    return ProfileStorage()


def get_config() -> Config:
    """Get the config instance."""
    return Config()


@app.command()
def init(
    interactive: bool = typer.Option(
        True, "--interactive/--no-interactive", help="Run interactive setup"
    ),
    token_target: Optional[str] = typer.Option(
        None, "--token-target", help="Path to store active token"
    ),
    default_profile: Optional[str] = typer.Option(
        None, "--default-profile", help="Default profile name"
    ),
):
    """Initialize the profile manager with guided setup."""
    console.print("[bold blue]🚀 Welcome to Claude Profile Manager Setup[/bold blue]")
    console.print()

    storage = get_storage()
    config = get_config()

    # Test keyring access
    if not storage.test_keyring_access():
        show_error("Keyring access failed. Please check your system keyring setup.")
        raise typer.Exit(1)

    console.print(
        f"[green]✓ Keyring backend: {storage.check_keyring_backend()}[/green]"
    )

    # Setup token target
    if interactive and not token_target:
        console.print("\n[bold]Active Token Storage Configuration[/bold]")
        console.print(
            "This determines where your currently active Claude token will be stored."
        )

        found_paths = find_claude_config_paths()
        if found_paths:
            console.print("\n[yellow]Found existing Claude configurations:[/yellow]")
            for i, path in enumerate(found_paths, 1):
                console.print(f"  {i}. {path}")

            if Confirm.ask("Use one of these paths?", default=True):
                choice = Prompt.ask(
                    "Select path number",
                    choices=[str(i) for i in range(1, len(found_paths) + 1)],
                )
                token_target = str(found_paths[int(choice) - 1])

        if not token_target:
            default_path = config.get_active_token_path()
            token_target = Prompt.ask(
                "Enter path for active token storage", default=default_path
            )

    if token_target:
        config.set_active_token_target("file", token_target)
        show_success(f"Active token will be stored in: {token_target}")

    # Setup default profile
    if interactive and not default_profile:
        profiles = storage.list_profiles()
        if profiles:
            console.print("\n[bold]Default Profile Configuration[/bold]")
            if Confirm.ask("Set a default profile?", default=False):
                default_profile = prompt_for_profile_selection(profiles)

    if default_profile:
        config.set_default_profile(default_profile)
        show_success(f"Default profile set to: {default_profile}")

    # Import existing token if found
    if interactive:
        current_token = detect_current_token()
        if current_token and validate_token(current_token):
            console.print(
                f"\n[yellow]Found existing Claude token: {mask_token(current_token)}[/yellow]"
            )
            if Confirm.ask("Import this token as 'default' profile?", default=True):
                metadata = {
                    "created": datetime.now().isoformat(),
                    "description": "Imported from existing configuration",
                }
                if storage.save_profile("default", current_token, metadata):
                    storage.update_profile_list(
                        ["default"] + list(storage.list_profiles().keys())
                    )
                    show_success("Imported existing token as 'default' profile")

    show_success(
        "Setup complete! You can now use 'claude-profile save', 'switch', 'list' etc."
    )


@app.command()
def save(
    name: str = typer.Argument(..., help="Profile name to save"),
    token: Optional[str] = typer.Option(
        None, "--token", "-t", help="Claude token (will prompt if not provided)"
    ),
    description: Optional[str] = typer.Option(
        None, "--description", "-d", help="Profile description"
    ),
    set_active: bool = typer.Option(
        True, "--active/--no-active", help="Set as active profile after saving"
    ),
    overwrite: bool = typer.Option(
        False, "--overwrite/--no-overwrite", help="Overwrite existing profile"
    ),
):
    """Save the current or provided token as a named profile."""
    storage = get_storage()
    config = get_config()

    # Check if profile exists
    existing_profile = storage.get_profile(name)
    if existing_profile and not overwrite:
        if not Confirm.ask(
            f"Profile '{name}' already exists. Overwrite?", default=False
        ):
            console.print("Operation cancelled.")
            raise typer.Exit()

    # Get token
    if not token:
        token = detect_current_token()
        if not token:
            token = Prompt.ask("Enter your Claude token", password=True)

    if not validate_token(token):
        show_error("Invalid token format")
        raise typer.Exit(1)

    # Save profile
    metadata = {
        "created": datetime.now().isoformat(),
        "description": description
        or f"Profile saved on {datetime.now().strftime('%Y-%m-%d')}",
    }

    if storage.save_profile(name, token, metadata):
        # Update profile list
        profiles = storage.list_profiles()
        if name not in profiles:
            storage.update_profile_list(list(profiles.keys()) + [name])

        show_success(f"Profile '{name}' saved successfully")

        # Set as active if requested
        if set_active:
            if storage.save_active_token(token, config.get_active_token_path()):
                show_success(f"Profile '{name}' is now active")
            else:
                show_warning("Profile saved but could not set as active")
    else:
        show_error(f"Failed to save profile '{name}'")
        raise typer.Exit(1)


@app.command()
def switch(
    name: Optional[str] = typer.Argument(None, help="Profile name to switch to"),
    show_tokens: bool = typer.Option(
        False, "--show-tokens", help="Show tokens in selection list"
    ),
):
    """Switch to a different profile (interactive if no name provided)."""
    storage = get_storage()
    config = get_config()

    profiles = storage.list_profiles()
    if not profiles:
        show_error("No profiles found. Use 'claude-profile save' to create one.")
        raise typer.Exit(1)

    # Get profile name
    if not name:
        name = prompt_for_profile_selection(profiles, show_tokens)
        if not name:
            console.print("No profile selected.")
            raise typer.Exit()

    if name not in profiles:
        show_error(f"Profile '{name}' not found")
        raise typer.Exit(1)

    # Switch profile
    profile = profiles[name]
    token = profile["token"]

    if storage.save_active_token(token, config.get_active_token_path()):
        show_success(f"Switched to profile '{name}'")

        # Show profile info
        metadata = profile.get("metadata", {})
        console.print(
            f"[dim]Description: {metadata.get('description', 'No description')}[/dim]"
        )
        console.print(f"[dim]Token: {mask_token(token)}[/dim]")
    else:
        show_error(f"Failed to switch to profile '{name}'")
        raise typer.Exit(1)


@app.command()
def list(
    show_tokens: bool = typer.Option(
        False, "--show-tokens", help="Show actual tokens instead of masked"
    ),
    output_format: str = typer.Option(
        "table", "--output-format", help="Output format (table, json)"
    ),
    active_only: bool = typer.Option(
        False, "--active-only", help="Show only the active profile"
    ),
):
    """List all saved profiles."""
    storage = get_storage()
    config = get_config()

    profiles = storage.list_profiles()
    if not profiles:
        show_info("No profiles found")
        return

    # Get active token
    active_token = storage.get_active_token(config.get_active_token_path())
    active_profile = None

    if active_token:
        for name, data in profiles.items():
            if data["token"] == active_token:
                active_profile = name
                break

    if active_only and active_profile:
        profiles = {active_profile: profiles[active_profile]}
    elif active_only and not active_profile:
        show_info("No active profile found")
        return

    if output_format == "json":
        output = {}
        for name, data in profiles.items():
            output[name] = {
                "token": data["token"] if show_tokens else mask_token(data["token"]),
                "metadata": data.get("metadata", {}),
                "active": name == active_profile,
            }
        console.print(json.dumps(output, indent=2))
    else:
        table = create_profile_table(profiles, show_tokens)
        if active_profile:
            console.print(f"[green]Active profile: {active_profile}[/green]")
        console.print(table)


@app.command()
def current():
    """Show the currently active profile."""
    storage = get_storage()
    config = get_config()

    active_token = storage.get_active_token(config.get_active_token_path())
    if not active_token:
        show_info("No active profile found")
        return

    profiles = storage.list_profiles()
    active_profile = None

    for name, data in profiles.items():
        if data["token"] == active_token:
            active_profile = name
            break

    if active_profile:
        profile = profiles[active_profile]
        metadata = profile.get("metadata", {})

        console.print(
            Panel(
                f"[bold green]Active Profile: {active_profile}[/bold green]\n\n"
                f"[dim]Description: {metadata.get('description', 'No description')}[/dim]\n"
                f"[dim]Created: {format_timestamp(metadata.get('created'))}[/dim]\n"
                f"[dim]Token: {mask_token(active_token)}[/dim]",
                title="Current Profile",
                border_style="green",
            )
        )
    else:
        console.print(
            Panel(
                f"[dim]Token: {mask_token(active_token)}[/dim]\n"
                f"[yellow]This token is not associated with any saved profile[/yellow]",
                title="Current Token",
                border_style="yellow",
            )
        )


@app.command()
def cycle():
    """Cycle through available profiles."""
    storage = get_storage()
    config = get_config()

    profiles = list(storage.list_profiles().keys())
    if len(profiles) < 2:
        show_error("Need at least 2 profiles to cycle")
        raise typer.Exit(1)

    # Get current active profile
    active_token = storage.get_active_token(config.get_active_token_path())
    current_index = -1

    if active_token:
        for i, name in enumerate(profiles):
            profile = storage.get_profile(name)
            if profile and profile["token"] == active_token:
                current_index = i
                break

    # Switch to next profile
    next_index = (current_index + 1) % len(profiles)
    next_profile = profiles[next_index]

    # Use the switch command logic
    profile_data = storage.get_profile(next_profile)
    if profile_data and storage.save_active_token(
        profile_data["token"], config.get_active_token_path()
    ):
        show_success(f"Cycled to profile '{next_profile}'")
    else:
        show_error(f"Failed to cycle to profile '{next_profile}'")
        raise typer.Exit(1)


@app.command()
def delete(
    name: str = typer.Argument(..., help="Profile name to delete"),
    confirm: bool = typer.Option(
        True, "--confirm/--no-confirm", help="Confirm before deletion"
    ),
):
    """Delete a saved profile."""
    storage = get_storage()

    if name not in storage.list_profiles():
        show_error(f"Profile '{name}' not found")
        raise typer.Exit(1)

    if confirm and not Confirm.ask(f"Delete profile '{name}'?", default=False):
        console.print("Operation cancelled.")
        raise typer.Exit()

    if storage.delete_profile(name):
        # Update profile list
        profiles = storage.list_profiles()
        storage.update_profile_list(list(profiles.keys()))
        show_success(f"Profile '{name}' deleted")
    else:
        show_error(f"Failed to delete profile '{name}'")
        raise typer.Exit(1)


@app.command()
def rename(
    old_name: str = typer.Argument(..., help="Current profile name"),
    new_name: str = typer.Argument(..., help="New profile name"),
):
    """Rename a saved profile."""
    storage = get_storage()

    profiles = storage.list_profiles()
    if old_name not in profiles:
        show_error(f"Profile '{old_name}' not found")
        raise typer.Exit(1)

    if new_name in profiles:
        show_error(f"Profile '{new_name}' already exists")
        raise typer.Exit(1)

    # Get old profile data
    old_profile = storage.get_profile(old_name)
    if not old_profile:
        show_error(f"Could not retrieve profile '{old_name}'")
        raise typer.Exit(1)

    # Save with new name
    if storage.save_profile(
        new_name, old_profile["token"], old_profile.get("metadata", {})
    ):
        # Delete old profile
        if storage.delete_profile(old_name):
            # Update profile list
            profiles = storage.list_profiles()
            storage.update_profile_list(list(profiles.keys()))
            show_success(f"Profile renamed from '{old_name}' to '{new_name}'")
        else:
            show_error(f"Renamed but failed to delete old profile '{old_name}'")
            raise typer.Exit(1)
    else:
        show_error(f"Failed to rename profile '{old_name}'")
        raise typer.Exit(1)


@app.command()
def export(
    output_file: Optional[str] = typer.Argument(
        None, help="Output file path (prints to stdout if not provided)"
    ),
    include_tokens: bool = typer.Option(
        False, "--include-tokens", help="Include actual tokens in export"
    ),
    format: str = typer.Option(
        "json", "--export-format", help="Export format (json, yaml)"
    ),
):
    """Export profiles to a file."""
    storage = get_storage()

    profiles = storage.list_profiles()
    if not profiles:
        show_info("No profiles to export")
        return

    export_data = {}
    for name, data in profiles.items():
        export_data[name] = {
            "metadata": data.get("metadata", {}),
            "token": data["token"] if include_tokens else mask_token(data["token"]),
        }

    if format.lower() == "yaml":
        try:
            import yaml

            output = yaml.dump(export_data, default_flow_style=False)
        except ImportError:
            show_error("PyYAML is required for YAML export")
            raise typer.Exit(1)
    else:
        output = json.dumps(export_data, indent=2)

    if output_file:
        try:
            output_path = Path(output_file).expanduser()
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(output)
            show_success(f"Profiles exported to {output_path}")
        except Exception as e:
            show_error(f"Failed to write export file: {e}")
            raise typer.Exit(1)
    else:
        console.print(output)

    if not include_tokens:
        show_info(
            "Tokens are masked in the export. Use --include-tokens to export real tokens."
        )


@app.command()
def import_profiles(
    input_file: str = typer.Argument(..., help="Input file path"),
    merge: bool = typer.Option(
        True, "--merge/--replace", help="Merge with existing profiles"
    ),
    prefix: Optional[str] = typer.Option(
        None, "--prefix", help="Prefix for imported profile names"
    ),
):
    """Import profiles from a file."""
    storage = get_storage()

    try:
        input_path = Path(input_file).expanduser()
        if not input_path.exists():
            show_error(f"File not found: {input_file}")
            raise typer.Exit(1)

        content = input_path.read_text()

        # Try JSON first, then YAML
        try:
            import_data = json.loads(content)
        except json.JSONDecodeError:
            try:
                import yaml

                import_data = yaml.safe_load(content)
            except ImportError:
                show_error("PyYAML is required for YAML import")
                raise typer.Exit(1)
            except yaml.YAMLError:
                show_error("Invalid file format")
                raise typer.Exit(1)

        if not isinstance(import_data, dict):
            show_error("Invalid import file format")
            raise typer.Exit(1)

        # Import profiles
        imported_count = 0
        for name, data in import_data.items():
            profile_name = f"{prefix}{name}" if prefix else name

            if not merge and profile_name in storage.list_profiles():
                console.print(
                    f"[yellow]Skipping existing profile: {profile_name}[/yellow]"
                )
                continue

            token = data.get("token")
            if not token or not validate_token(token):
                show_warning(
                    f"Profile '{profile_name}' has no usable token in the import file"
                )
                if Confirm.ask("Provide the token now?", default=True):
                    token = Prompt.ask(
                        f"Enter token for '{profile_name}'", password=True
                    ).strip()
                    if not token or not validate_token(token):
                        show_warning(
                            f"Skipping profile '{profile_name}' - provided token invalid"
                        )
                        continue
                else:
                    show_warning(f"Skipping profile '{profile_name}' - token missing")
                    continue

            metadata = data.get("metadata", {})
            metadata["imported"] = datetime.now().isoformat()

            if storage.save_profile(profile_name, token, metadata):
                imported_count += 1
                console.print(f"[green]Imported: {profile_name}[/green]")
            else:
                show_error(f"Failed to import: {profile_name}")

        # Update profile list
        profiles = storage.list_profiles()
        storage.update_profile_list(list(profiles.keys()))

        show_success(f"Imported {imported_count} profiles")

    except Exception as e:
        show_error(f"Import failed: {e}")
        raise typer.Exit(1)


@app.command()
def show(
    name: str = typer.Argument(..., help="Profile name to show"),
    show_token: bool = typer.Option(
        False, "--show-token", help="Show the actual token"
    ),
):
    """Show details of a specific profile."""
    storage = get_storage()

    profile = storage.get_profile(name)
    if not profile:
        show_error(f"Profile '{name}' not found")
        raise typer.Exit(1)

    metadata = profile.get("metadata", {})
    token_display = profile["token"] if show_token else mask_token(profile["token"])

    console.print(
        Panel(
            f"[bold]Profile: {name}[/bold]\n\n"
            f"[dim]Token: {token_display}[/dim]\n"
            f"[dim]Created: {format_timestamp(metadata.get('created'))}[/dim]\n"
            f"[dim]Description: {metadata.get('description', 'No description')}[/dim]\n"
            f"[dim]Imported: {format_timestamp(metadata.get('imported'))}[/dim]",
            title=f"Profile Details: {name}",
            border_style="blue",
        )
    )


@app.command()
def doctor():
    """Check system configuration and diagnose issues."""
    console.print("[bold blue]🔍 Claude Profile Manager - System Check[/bold blue]")
    console.print()

    storage = get_storage()
    config = get_config()

    # Check keyring
    console.print("[bold]Keyring Check:[/bold]")
    if storage.test_keyring_access():
        console.print(
            f"[green]✓ Keyring accessible: {storage.check_keyring_backend()}[/green]"
        )
    else:
        console.print("[red]✗ Keyring access failed[/red]")

    # Check config directory
    console.print("\n[bold]Configuration Check:[/bold]")
    try:
        config.ensure_config_dir()
        console.print(f"[green]✓ Config directory: {config.get_config_path()}[/green]")
    except Exception as e:
        console.print(f"[red]✗ Config directory error: {e}[/red]")

    # Check active token file
    console.print("\n[bold]Active Token Check:[/bold]")
    token_path = Path(config.get_active_token_path())
    if token_path.exists():
        console.print(f"[green]✓ Token file exists: {token_path}[/green]")
        if check_file_permissions(token_path):
            console.print("[green]✓ File permissions are secure (0600)[/green]")
        else:
            console.print(
                "[yellow]⚠ File permissions are not secure (should be 0600)[/yellow]"
            )
            if Confirm.ask("Fix file permissions?", default=True):
                if secure_file_permissions(token_path):
                    console.print("[green]✓ File permissions fixed[/green]")
                else:
                    console.print("[red]✗ Failed to fix file permissions[/red]")
    else:
        console.print(f"[yellow]⚠ Token file does not exist: {token_path}[/yellow]")

    # Check for existing Claude configurations
    console.print("\n[bold]Existing Claude Configurations:[/bold]")
    found_paths = find_claude_config_paths()
    if found_paths:
        for path in found_paths:
            console.print(f"[green]✓ Found: {path}[/green]")
    else:
        console.print("[yellow]⚠ No existing Claude configurations found[/yellow]")

    # Check profiles
    console.print("\n[bold]Profiles Check:[/bold]")
    profiles = storage.list_profiles()
    if profiles:
        console.print(f"[green]✓ Found {len(profiles)} profiles[/green]")
        for name in profiles:
            console.print(f"  - {name}")
    else:
        console.print("[yellow]⚠ No profiles found[/yellow]")

    console.print("\n[bold green]System check complete![/bold green]")


@app.command()
def completions(
    shell: str = typer.Argument(..., help="Shell type (bash, zsh, fish, powershell)"),
    install: bool = typer.Option(False, "--install", help="Install completions"),
):
    """Generate shell completions."""
    script_path = Path(__file__).absolute()

    if shell == "bash":
        completion_script = f"""
# Claude Profile Manager bash completion
_claude_profile_completion() {{
    local cur prev opts
    COMPREPLY=()
    cur="${{COMP_WORDS[COMP_CWORD]}}"
    prev="${{COMP_WORDS[COMP_CWORD-1]}}"
    opts="init save switch list current cycle delete rename export import show doctor completions"

    if [[ ${{cur}} == * ]] ; then
        COMPREPLY=( $(compgen -W "${{opts}}" -- ${{cur}}) )
        return 0
    fi
}}
complete -F _claude_profile_completion {script_path.name}
"""
    elif shell == "zsh":
        completion_script = f"""
#compdef {script_path.name}
_claude_profile() {{
    local -a commands
    commands=(
        'init:Initialize the profile manager'
        'save:Save a profile'
        'switch:Switch to a profile'
        'list:List profiles'
        'current:Show current profile'
        'cycle:Cycle through profiles'
        'delete:Delete a profile'
        'rename:Rename a profile'
        'export:Export profiles'
        'import:Import profiles'
        'show:Show profile details'
        'doctor:System check'
        'completions:Generate completions'
    )
    _describe 'command' commands
}}
_claude_profile
"""
    elif shell == "fish":
        completion_script = f"""
# Claude Profile Manager fish completion
complete -c {script_path.name} -f
complete -c {script_path.name} -n __fish_use_subcommand -a init -d 'Initialize the profile manager'
complete -c {script_path.name} -n __fish_use_subcommand -a save -d 'Save a profile'
complete -c {script_path.name} -n __fish_use_subcommand -a switch -d 'Switch to a profile'
complete -c {script_path.name} -n __fish_use_subcommand -a list -d 'List profiles'
complete -c {script_path.name} -n __fish_use_subcommand -a current -d 'Show current profile'
complete -c {script_path.name} -n __fish_use_subcommand -a cycle -d 'Cycle through profiles'
complete -c {script_path.name} -n __fish_use_subcommand -a delete -d 'Delete a profile'
complete -c {script_path.name} -n __fish_use_subcommand -a rename -d 'Rename a profile'
complete -c {script_path.name} -n __fish_use_subcommand -a export -d 'Export profiles'
complete -c {script_path.name} -n __fish_use_subcommand -a import -d 'Import profiles'
complete -c {script_path.name} -n __fish_use_subcommand -a show -d 'Show profile details'
complete -c {script_path.name} -n __fish_use_subcommand -a doctor -d 'System check'
complete -c {script_path.name} -n __fish_use_subcommand -a completions -d 'Generate completions'
"""
    elif shell == "powershell":
        completion_script = f"""
# Claude Profile Manager PowerShell completion
Register-ArgumentCompleter -Native -CommandName {script_path.name} -ScriptBlock {{
    param($wordToComplete, $commandAst, $cursorPosition)
    $commands = @('init', 'save', 'switch', 'list', 'current', 'cycle', 'delete', 'rename', 'export', 'import', 'show', 'doctor', 'completions')
    $commands | Where-Object {{ $_ -like "$wordToComplete*" }} | ForEach-Object {{ [System.Management.Automation.CompletionResult]::new($_, $_, 'ParameterValue', $_) }}
}}
"""
    else:
        show_error(f"Unsupported shell: {shell}")
        raise typer.Exit(1)

    if install:
        # Installation instructions
        console.print(f"[bold]Shell Completion Installation for {shell}[/bold]")
        console.print()

        if shell == "bash":
            console.print("Add this to your ~/.bashrc:")
            console.print(completion_script)
        elif shell == "zsh":
            comp_file = Path.home() / ".zsh" / "_claude_profile"
            comp_file.parent.mkdir(exist_ok=True)
            comp_file.write_text(completion_script)
            console.print(f"Completion file written to: {comp_file}")
            console.print("Add this to your ~/.zshrc:")
            console.print(f"fpath=({comp_file.parent} $fpath)")
            console.print("autoload -U compinit && compinit")
        elif shell == "fish":
            comp_file = (
                Path.home()
                / ".config"
                / "fish"
                / "completions"
                / f"{script_path.name}.fish"
            )
            comp_file.parent.mkdir(parents=True, exist_ok=True)
            comp_file.write_text(completion_script)
            console.print(f"Completion file written to: {comp_file}")
        elif shell == "powershell":
            console.print("Add this to your PowerShell profile:")
            console.print(completion_script)
    else:
        console.print(completion_script)


if __name__ == "__main__":
    app()

```

---

### 11. /Users/biostochastics/CCProfileSwitch/tests/test_cli.py {#users-biostochastics-ccprofileswitch-tests-test-cli-py}

[↑ Back to TOC](#table-of-contents) | 
[← Previous](#users-biostochastics-ccprofileswitch-claude-profile-manager-typer-rich-py) | 


#### Summary

> Contains 8 functions

#### File Information

| Property | Value |
|----------|-------|
| Language | python |
| Lines | 134 |
| Functions/Classes | 69 |

<details>
<summary>📦 Declarations</summary>

- **function** `runner` (lines 16-18)
- **function** `runner` (lines 17-18)
- **function** `test_save_list_and_cycle_flow` (lines 21-75)
- **variable** `token_primary` (lines 22-22)
- **constant** `token_primary` (lines 22-22)
- **variable** `token_secondary` (lines 23-23)
- **constant** `token_secondary` (lines 23-23)
- **variable** `result` (lines 25-36)
- **constant** `result` (lines 25-36)
- **variable** `storage` (lines 39-39)
- **constant** `storage` (lines 39-39)
- **variable** `stored_profile` (lines 40-40)
- **constant** `stored_profile` (lines 40-40)
- **variable** `list_result` (lines 44-48)
- **constant** `list_result` (lines 44-48)
- **variable** `profiles_json` (lines 50-50)
- **constant** `profiles_json` (lines 50-50)
- **variable** `add_second` (lines 54-66)
- **constant** `add_second` (lines 54-66)
- **variable** `cycle_result` (lines 69-69)
- **constant** `cycle_result` (lines 69-69)
- **variable** `config` (lines 72-72)
- **constant** `config` (lines 72-72)
- **variable** `active_path` (lines 73-73)
- **constant** `active_path` (lines 73-73)
- **variable** `active_payload` (lines 74-74)
- **constant** `active_payload` (lines 74-74)
- **function** `test_export_masks_tokens_and_import_prompts_for_real_token` (lines 78-114)
- **variable** `token_value` (lines 81-81)
- **constant** `token_value` (lines 81-81)
- **variable** `export_path` (lines 86-86)
- **constant** `export_path` (lines 86-86)
- **variable** `export_result` (lines 87-89)
- **constant** `export_result` (lines 87-89)
- **variable** `export_data` (lines 92-92)
- **constant** `export_data` (lines 92-92)
- **variable** `delete_result` (lines 96-98)
- **constant** `delete_result` (lines 96-98)
- **variable** `import_input` (lines 101-101)
- **constant** `import_input` (lines 101-101)
- **variable** `import_result` (lines 102-107)
- **constant** `import_result` (lines 102-107)
- **variable** `storage` (lines 111-111)
- **constant** `storage` (lines 111-111)
- **variable** `restored` (lines 112-112)
- **constant** `restored` (lines 112-112)
- **function** `test_switch_with_show_tokens_displays_unmasked_tokens` (lines 117-127)
- **variable** `token_value` (lines 118-118)
- **constant** `token_value` (lines 118-118)
- **variable** `switch_result` (lines 123-125)
- **constant** `switch_result` (lines 123-125)
- **function** `test_doctor_reports_config_directory` (lines 130-134)
- **variable** `result` (lines 131-131)
- **constant** `result` (lines 131-131)
- **variable** `config` (lines 133-133)
- **constant** `config` (lines 133-133)
- **function** `runner` (lines 17-20)
- **variable** `result` (lines 25-25)
- **variable** `catch_exceptions` (lines 35-35)
- **variable** `list_result` (lines 44-44)
- **variable** `catch_exceptions` (lines 47-47)
- **variable** `add_second` (lines 54-54)
- **variable** `catch_exceptions` (lines 65-65)
- **variable** `delete_result` (lines 96-96)
- **variable** `input` (lines 105-105)
- **function** `test_switch_with_show_tokens_displays_unmasked_tokens` (lines 117-129)
- **variable** `export_result` (lines 87-87)
- **variable** `import_result` (lines 102-102)
- **variable** `catch_exceptions` (lines 106-106)
</details>

#### Source Code

```python
"""Integration tests for the Typer CLI commands."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from cc_profile_switch.cli import app
from cc_profile_switch.config import Config
from cc_profile_switch.storage import ProfileStorage


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_save_list_and_cycle_flow(runner: CliRunner) -> None:
    token_primary = "sk-ant-api03-primary"
    token_secondary = "sk-ant-api03-secondary"

    result = runner.invoke(
        app,
        [
            "save",
            "work",
            "--token",
            token_primary,
            "--description",
            "Work account",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.stdout

    storage = ProfileStorage()
    stored_profile = storage.get_profile("work")
    assert stored_profile is not None
    assert stored_profile["token"] == token_primary

    list_result = runner.invoke(
        app,
        ["list", "--output-format", "json", "--show-tokens"],
        catch_exceptions=False,
    )
    assert list_result.exit_code == 0, list_result.stdout
    profiles_json = json.loads(list_result.stdout)
    assert profiles_json["work"]["token"] == token_primary
    assert profiles_json["work"]["active"] is True

    add_second = runner.invoke(
        app,
        [
            "save",
            "personal",
            "--token",
            token_secondary,
            "--description",
            "Personal account",
            "--no-active",
        ],
        catch_exceptions=False,
    )
    assert add_second.exit_code == 0, add_second.stdout

    cycle_result = runner.invoke(app, ["cycle"], catch_exceptions=False)
    assert cycle_result.exit_code == 0, cycle_result.stdout

    config = Config()
    active_path = Path(config.get_active_token_path())
    active_payload = json.loads(active_path.read_text())
    assert active_payload["token"] == token_secondary


def test_export_masks_tokens_and_import_prompts_for_real_token(
    runner: CliRunner, tmp_path: Path
) -> None:
    token_value = "sk-ant-api03-exporttest"
    runner.invoke(
        app, ["save", "exportable", "--token", token_value], catch_exceptions=False
    )

    export_path = tmp_path / "profiles.json"
    export_result = runner.invoke(
        app, ["export", str(export_path)], catch_exceptions=False
    )
    assert export_result.exit_code == 0, export_result.stdout

    export_data = json.loads(export_path.read_text())
    assert export_data["exportable"]["token"] != token_value
    assert token_value not in export_path.read_text()

    delete_result = runner.invoke(
        app, ["delete", "exportable", "--no-confirm"], catch_exceptions=False
    )
    assert delete_result.exit_code == 0, delete_result.stdout

    import_input = "y\n" + token_value + "\n"
    import_result = runner.invoke(
        app,
        ["import-profiles", str(export_path)],
        input=import_input,
        catch_exceptions=False,
    )
    assert import_result.exit_code == 0, import_result.stdout
    assert "Imported: exportable" in import_result.stdout

    storage = ProfileStorage()
    restored = storage.get_profile("exportable")
    assert restored is not None
    assert restored["token"] == token_value


def test_switch_with_show_tokens_displays_unmasked_tokens(runner: CliRunner) -> None:
    token_value = "sk-ant-api03-visualtest"
    runner.invoke(
        app, ["save", "visual", "--token", token_value], catch_exceptions=False
    )

    switch_result = runner.invoke(
        app, ["switch", "--show-tokens"], input="1\n", catch_exceptions=False
    )
    assert switch_result.exit_code == 0, switch_result.stdout
    assert token_value in switch_result.stdout


def test_doctor_reports_config_directory(runner: CliRunner) -> None:
    result = runner.invoke(app, ["doctor"], input="n\n", catch_exceptions=False)
    assert result.exit_code == 0, result.stdout
    config = Config()
    assert config.get_config_path() in result.stdout

```

---


---

*Generated by CodeConCat - Optimized for human review*
