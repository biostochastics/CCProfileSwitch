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
