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
