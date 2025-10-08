"""Main CLI interface for CC Profile Switch."""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import typer
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

from .config import Config
from .constants import (
    ENV_ANTHROPIC_AUTH_TOKEN,
    ENV_ANTHROPIC_BASE_URL,
    PROVIDER_CLAUDE,
    PROVIDER_ZAI,
    ZAI_DEFAULT_API_URL,
)
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
        None, "--token", "-t", help="API token (will prompt if not provided)"
    ),
    description: Optional[str] = typer.Option(
        None, "--description", "-d", help="Profile description"
    ),
    provider: str = typer.Option(
        PROVIDER_CLAUDE,
        "--provider",
        "-p",
        help="Provider: claude or zai",
    ),
    api_url: Optional[str] = typer.Option(
        None, "--api-url", help="Custom API URL (defaults to Z-AI for zai provider)"
    ),
    set_active: bool = typer.Option(
        True, "--active/--no-active", help="Set as active profile after saving"
    ),
    overwrite: bool = typer.Option(
        False, "--overwrite/--no-overwrite", help="Overwrite existing profile"
    ),
):
    """Save an API token as a named profile."""
    from .utils import detect_zai_token, validate_token

    show_header("Save Profile", f"Save profile '{name}'")

    storage = get_storage()
    config = get_config()

    # Validate provider
    provider = provider.lower()
    if provider not in [PROVIDER_CLAUDE, PROVIDER_ZAI]:
        show_error(f"Invalid provider: {provider}. Use 'claude' or 'zai'")
        raise typer.Exit(1)

    # Check if profile exists
    existing_profile = storage.get_profile(name)
    if existing_profile and not overwrite:
        if not Confirm.ask(
            f"Profile '{name}' already exists. Overwrite?", default=False
        ):
            console.print("Operation cancelled.")
            raise typer.Exit()

    # Get token based on provider
    if not token:
        if provider == PROVIDER_ZAI:
            # Try to detect Z-AI token from environment
            token = detect_zai_token()
            if token:
                show_info(f"Auto-detected Z-AI token from environment")
            else:
                show_info("No Z-AI token in environment (ZAI_API_KEY)")
                token = Prompt.ask("Enter your Z-AI API key", password=True)
        else:
            # Claude: try existing detection
            token = detect_current_token()
            if token:
                show_info(f"Auto-detected current token: {mask_token(token)}")
            else:
                show_warning("No current token detected - please enter manually")
                token = Prompt.ask("Enter your Claude token", password=True)

    # Validate token
    is_valid, error_msg = validate_token(token, provider)
    if not is_valid:
        show_error(f"Invalid token: {error_msg}")
        if provider == PROVIDER_ZAI:
            show_info("Z-AI tokens should be at least 20 characters with no whitespace")
        else:
            show_info("Claude tokens should start with 'sk-' and be at least 20 characters")
        raise typer.Exit(1)

    # Set API URL
    if provider == PROVIDER_ZAI and not api_url:
        api_url = ZAI_DEFAULT_API_URL

    # Save profile
    metadata = {
        "created": datetime.now().isoformat(),
        "description": description
        or f"{provider.upper()} profile saved on {datetime.now().strftime('%Y-%m-%d')}",
    }

    if storage.save_profile(name, token, metadata, provider=provider, api_url=api_url):
        # Update profile list - get existing profiles and add the new one
        existing_profiles = storage.list_profiles()
        if existing_profiles and hasattr(existing_profiles, "keys"):
            all_profile_names = [k for k in existing_profiles.keys()]
        else:
            all_profile_names = []

        if name not in all_profile_names:
            all_profile_names.append(name)
        storage.update_profile_list(all_profile_names)

        console.print(f"[green]✓ Profile '{name}' saved successfully[/green]")
        console.print(f"  Provider: [cyan]{provider.upper()}[/cyan]")
        if api_url:
            console.print(f"  API URL: [dim]{api_url}[/dim]")

        # Set as active if requested
        if set_active:
            # Update Claude settings.json with appropriate environment variables
            if provider == PROVIDER_ZAI:
                env_update = {
                    ENV_ANTHROPIC_BASE_URL: api_url or ZAI_DEFAULT_API_URL,
                    ENV_ANTHROPIC_AUTH_TOKEN: token,
                }
                if config.update_claude_settings(env_update):
                    show_success(f"Profile '{name}' is now active (Z-AI configured)")
                else:
                    show_warning("Profile saved but could not update settings.json")
            else:
                # Claude: set token, remove base URL
                env_update = {ENV_ANTHROPIC_AUTH_TOKEN: token}
                if config.update_claude_settings(env_update, remove_keys=[ENV_ANTHROPIC_BASE_URL]):
                    show_success(f"Profile '{name}' is now active (Claude configured)")
                else:
                    show_warning("Profile saved but could not update settings.json")
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
    from .utils import detect_current_provider

    show_header("Profile Switch", "Switch between provider profiles")

    storage = get_storage()
    config = get_config()

    profiles = storage.list_profiles()
    if not profiles:
        show_error("No profiles found. Use 'claude-profile save' to create one.")
        raise typer.Exit(1)

    # Detect current provider
    current_info = detect_current_provider()
    current_provider_name = current_info.get("provider", PROVIDER_CLAUDE)

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

    # Get target profile
    profile = profiles[name]
    target_provider = profile.get("provider", PROVIDER_CLAUDE)

    # CRITICAL: Check provider compatibility
    if current_info.get("token_present") and current_provider_name != target_provider:
        show_error(
            f"Cannot switch between {current_provider_name.upper()} and "
            f"{target_provider.upper()} profiles!"
        )
        console.print()
        console.print("[yellow]Provider switching requires reconfiguration:[/yellow]")
        console.print(f"  Current provider: {current_provider_name.upper()}")
        console.print(f"  Target provider:  {target_provider.upper()}")
        console.print()
        console.print("[dim]Different providers use different API endpoints.[/dim]")
        console.print("[dim]Create a new profile for the target provider instead:[/dim]")
        console.print()
        console.print(f"  claude-profile save {name}_new --provider {target_provider}")
        raise typer.Exit(1)

    # Perform the switch
    token = profile["token"]
    api_url = profile.get("api_url")

    spinner = show_spinner(f"Switching to profile '{name}'...")
    if spinner:
        with spinner:
            time.sleep(0.5)  # Brief delay for visual feedback
            # Update settings.json based on provider
            if target_provider == PROVIDER_ZAI:
                env_update = {
                    ENV_ANTHROPIC_BASE_URL: api_url or ZAI_DEFAULT_API_URL,
                    ENV_ANTHROPIC_AUTH_TOKEN: token,
                }
                success = config.update_claude_settings(env_update)
            else:
                # Claude: set token, remove base URL
                env_update = {ENV_ANTHROPIC_AUTH_TOKEN: token}
                success = config.update_claude_settings(
                    env_update, remove_keys=[ENV_ANTHROPIC_BASE_URL]
                )
    else:
        if target_provider == PROVIDER_ZAI:
            env_update = {
                ENV_ANTHROPIC_BASE_URL: api_url or ZAI_DEFAULT_API_URL,
                ENV_ANTHROPIC_AUTH_TOKEN: token,
            }
            success = config.update_claude_settings(env_update)
        else:
            env_update = {ENV_ANTHROPIC_AUTH_TOKEN: token}
            success = config.update_claude_settings(
                env_update, remove_keys=[ENV_ANTHROPIC_BASE_URL]
            )

    if success:
        show_success(f"Switched to profile '{name}'")
        console.print(f"  Provider: [cyan]{target_provider.upper()}[/cyan]")
        if api_url:
            console.print(f"  API URL: [dim]{api_url}[/dim]")
        console.print()
        console.print("[dim]Environment updated in ~/.claude/settings.json[/dim]")
        console.print()
        console.print(
            "[yellow]Note:[/yellow] Restart Claude Code to use the new configuration"
        )
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
    """List all saved profiles grouped by provider."""
    from .utils import detect_current_provider

    show_header("Profile List", "View all saved profiles")

    storage = get_storage()
    config = get_config()

    profiles = storage.list_profiles()
    if not profiles:
        show_info("No profiles found")
        show_info("Create your first profile:")
        console.print("  • Claude: [cyan]claude-profile save <name> --provider claude[/cyan]")
        console.print("  • Z-AI:   [cyan]claude-profile save <name> --provider zai[/cyan]")
        return

    # Detect active from settings.json
    current_info = detect_current_provider()
    env_vars = config.get_claude_settings_env()
    active_token = env_vars.get(ENV_ANTHROPIC_AUTH_TOKEN)
    active_profile_name = None

    if active_token:
        for name, data in profiles.items():
            if data.get("token") == active_token:
                active_profile_name = name
                break

    if active_only and active_profile_name:
        profiles = {active_profile_name: profiles[active_profile_name]}
    elif active_only and not active_profile_name:
        show_info("No active profile found")
        return

    if output_format == "json":
        output = {}
        for name, data in profiles.items():
            output[name] = {
                "provider": data.get("provider", PROVIDER_CLAUDE),
                "api_url": data.get("api_url"),
                "token": data["token"] if show_tokens else mask_token(data["token"]),
                "metadata": data.get("metadata", {}),
                "active": name == active_profile_name,
            }
        console.print(json.dumps(output, indent=2))
    else:
        # Group profiles by provider
        claude_profiles = {}
        zai_profiles = {}

        for name, data in profiles.items():
            provider = data.get("provider", PROVIDER_CLAUDE)
            if provider == PROVIDER_ZAI:
                zai_profiles[name] = data
            else:
                claude_profiles[name] = data

        # Display Claude profiles
        if claude_profiles:
            console.print("[bold cyan]=== Claude Profiles ===[/bold cyan]\n")
            table = create_profile_table(claude_profiles, show_tokens, active_profile_name)
            console.print(table)
            console.print()

        # Display Z-AI profiles
        if zai_profiles:
            console.print("[bold magenta]=== Z-AI Profiles ===[/bold magenta]\n")
            # Create Z-AI specific table with API URL column
            from rich.table import Table
            from rich import box

            table = Table(
                box=box.MINIMAL_HEAVY_HEAD,
                row_styles=["", "dim"] if should_use_rich() else None,
                show_header=True,
                header_style="bold cyan",
            )

            active_icon = get_icon("active")
            table.add_column("", style="accent", width=3)
            table.add_column("Name", style="magenta")
            table.add_column("Description", style="blue")
            table.add_column("API URL", style="green")
            table.add_column("Created", style="yellow")

            for name, data in zai_profiles.items():
                is_active = name == active_profile_name
                indicator = active_icon if is_active else ""
                api_url = data.get("api_url", ZAI_DEFAULT_API_URL)
                metadata = data.get("metadata", {})
                created = format_timestamp(metadata.get("created", "Unknown"))
                desc = metadata.get("description", "")

                if is_active and should_use_rich():
                    table.add_row(
                        indicator,
                        f"[bold highlight]{name}[/bold highlight]",
                        desc,
                        api_url,
                        created,
                        style="highlight",
                    )
                else:
                    table.add_row(indicator, name, desc, api_url, created)

            console.print(table)
            console.print()

        # Show active profile indicator
        if active_profile_name:
            active_profile = profiles[active_profile_name]
            provider = active_profile.get("provider", PROVIDER_CLAUDE)
            console.print(
                f"[success]{get_icon('active')} Active: [bold]{active_profile_name}[/bold] "
                f"({provider.upper()})[/success]"
            )


@app.command()
def current():
    """Show the currently active provider configuration."""
    from .utils import detect_current_provider

    show_header("Current Configuration", "View active provider and profile")

    storage = get_storage()
    config = get_config()

    # Detect current provider from settings.json
    current_info = detect_current_provider()
    provider = current_info.get("provider", PROVIDER_CLAUDE)
    base_url = current_info.get("base_url")
    has_token = current_info.get("token_present", False)

    if not has_token:
        console.print(
            Panel(
                "[yellow]No active environment configured[/yellow]\n\n"
                "To get started, create a profile:\n"
                "  • Claude: [cyan]claude-profile save <name> --provider claude[/cyan]\n"
                "  • Z-AI:   [cyan]claude-profile save <name> --provider zai[/cyan]",
                title="No Configuration",
                border_style="yellow",
            )
        )
        return

    # Try to match to a saved profile
    env_vars = config.get_claude_settings_env()
    active_token = env_vars.get(ENV_ANTHROPIC_AUTH_TOKEN)
    profiles = storage.list_profiles()
    active_profile_name = None

    if active_token:
        for name, data in profiles.items():
            if data.get("token") == active_token:
                active_profile_name = name
                break

    # Build info display
    info_lines = [
        f"[bold green]Provider:[/bold green] {provider.upper()}",
    ]

    if active_profile_name:
        profile = profiles[active_profile_name]
        metadata = profile.get("metadata", {})
        info_lines.append(f"[bold green]Profile:[/bold green] {active_profile_name}")
        info_lines.append(
            f"[dim]Description:[/dim] {metadata.get('description', 'No description')}"
        )
        info_lines.append(
            f"[dim]Created:[/dim] {format_timestamp(metadata.get('created'))}"
        )
    else:
        info_lines.append("[yellow]Profile: Not matched to saved profile[/yellow]")

    if base_url:
        info_lines.append(f"[dim]API URL:[/dim] {base_url}")

    info_lines.append(f"[dim]Token:[/dim] Token configured ✓")

    info_lines.append("")
    info_lines.append(
        "[dim italic]Note: To switch providers, create and switch to a profile\n"
        "of the desired provider type.[/dim italic]"
    )

    console.print(
        Panel(
            "\n".join(info_lines),
            title="Current Configuration",
            border_style="green",
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
        # On macOS, don't pass target_path to ensure keychain write
        target_path = (
            None if sys.platform == "darwin" else config.get_active_token_path()
        )

        spinner = show_spinner(f"Switching to '{next_profile}'...")
        if spinner:
            with spinner:
                time.sleep(0.4)  # Brief animation
                success = storage.save_active_token(profile_data["token"], target_path)
        else:
            success = storage.save_active_token(profile_data["token"], target_path)

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
        imported_names = []
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
                imported_names.append(profile_name)
                console.print(f"[green]Imported: {profile_name}[/green]")
            else:
                show_error(f"Failed to import: {profile_name}")

        # Update profile list - include both existing and newly imported profiles
        profiles = storage.list_profiles()
        # Use list comprehension instead of list() to avoid shadowing by list command
        all_profile_names = [k for k in profiles.keys()] if profiles else []
        # Add newly imported profiles that aren't already in the list
        for name in imported_names:
            if name and name not in all_profile_names:
                all_profile_names.append(name)
        storage.update_profile_list(all_profile_names)

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
    provider = profile.get("provider", PROVIDER_CLAUDE)
    api_url = profile.get("api_url")
    token_display = profile["token"] if show_token else mask_token(profile["token"])

    info_lines = [
        f"[bold]Profile: {name}[/bold]",
        "",
        f"[bold cyan]Provider:[/bold cyan] {provider.upper()}",
    ]

    if api_url:
        info_lines.append(f"[dim]API URL:[/dim] {api_url}")

    info_lines.extend([
        f"[dim]Token:[/dim] {token_display}",
        f"[dim]Created:[/dim] {format_timestamp(metadata.get('created'))}",
        f"[dim]Description:[/dim] {metadata.get('description', 'No description')}",
    ])

    if metadata.get('imported'):
        info_lines.append(f"[dim]Imported:[/dim] {format_timestamp(metadata.get('imported'))}")

    console.print(
        Panel(
            "\n".join(info_lines),
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

    # Check active token file and detection
    console.print("\n[bold]Active Token Check:[/bold]")
    token_path = Path(config.get_active_token_path())

    # Try to detect token from any source (keychain, file, env)
    detected_token = detect_current_token()

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

        # Check if token is available from other sources
        if detected_token:
            # Determine the actual source based on token format and platform
            env_token = os.environ.get("ANTHROPIC_API_KEY")

            # Check if detected token is OAuth (starts with sk-ant-oat or sk-ant-ort)
            is_oauth = detected_token.startswith(
                "sk-ant-oat"
            ) or detected_token.startswith("sk-ant-ort")

            if is_oauth and sys.platform == "darwin":
                console.print(
                    "[green]✓ Token found in macOS Keychain "
                    "(OAuth authentication)[/green]"
                )
            elif env_token and detected_token == env_token:
                console.print(
                    "[green]✓ Token found in ANTHROPIC_API_KEY "
                    "environment variable[/green]"
                )
            elif sys.platform == "darwin":
                console.print("[green]✓ Token found in macOS Keychain[/green]")
            else:
                console.print("[green]✓ Token found from alternative source[/green]")
        else:
            console.print("[red]✗ No token detected from any source[/red]")

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
