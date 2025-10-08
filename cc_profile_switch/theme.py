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
    # Safe encoding check - handles None when output is piped/redirected
    encoding = (getattr(sys.stdout, "encoding", "") or "").lower()
    return "utf" in encoding


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


def show_spinner(message: str, spinner_type: str = "dots") -> Optional[Live]:
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
