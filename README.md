# CCProfileSwitch

**Switch between Claude Code profiles in seconds—without context mistakes or credential exposure.**

[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/biostochastics/CCProfileSwitch) [![Python Version](https://img.shields.io/badge/python-3.8.1%2B-blue)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Typer](https://img.shields.io/badge/CLI-typer-green)](https://typer.tiangolo.com/) [![Rich](https://img.shields.io/badge/UI-rich-orange)](https://rich.readthedocs.io/) [![Keyring](https://img.shields.io/badge/security-keyring-red)](https://github.com/jaraco/keyring) [![DeepWiki](https://img.shields.io/badge/DeepWiki-docs-purple)](https://deepwiki.com/biostochastics/CCProfileSwitch)

## Why CCProfileSwitch?

If you juggle multiple Claude API accounts across personal and professional projects, you know the friction: manually editing credential files, risking context slips where you accidentally use the wrong account, and storing API keys in plaintext configuration. CCProfileSwitch eliminates this workflow tax by managing profiles in your operating system's secure keyring and switching contexts with a single command.

The tool integrates directly with Claude Code by updating `~/.claude/.credentials.json`, the credential file Claude Code monitors for authentication. When you switch profiles, Claude Code immediately uses the new credentials for subsequent requests—no restart required, no manual file edits, no plaintext keys scattered across config files.

Whether you're switching between client accounts, separating personal and work usage, or managing team credentials, CCProfileSwitch handles the mechanics so you can focus on your actual work.

## How It Works

CCProfileSwitch stores your API tokens in your system's native credential manager (macOS Keychain, Windows Credential Manager, or Linux Secret Service) and maintains profile metadata separately. When you need to switch contexts, you run `claude-profile switch <name>`, and the tool writes that profile's token to Claude Code's credential file. The workflow looks like this:

```bash
# Morning: Start with client-a work
$ claude-profile switch client-a
✔ Switched to profile 'client-a'

# Run Claude Code tasks for client-a...

# Afternoon: Switch to personal projects
$ claude-profile switch personal
✔ Switched to profile 'personal'

# Confirm active context
$ claude-profile current
● Active profile: personal
  Description: Personal projects
  Token: sk-a***
```

Profile switching is instant, secure, and deterministic. You always know which context is active, and your credentials never touch version control or plaintext files beyond Claude Code's monitored credential file.

## Quick Start

Install CCProfileSwitch and create your first profile:

```bash
# Clone and install
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
poetry install

# Initialize with guided setup
poetry run claude-profile init

# Save your first profile (prompts for API token)
poetry run claude-profile save personal

# Switch to the profile
poetry run claude-profile switch personal
```

After setup, Claude Code will use the active profile's credentials for all API requests.

## Common Workflows

### Starting Your Day

Confirm or set your default context before beginning work:

```bash
$ claude-profile current
● Active profile: work
```

If you need to switch, use `claude-profile switch <name>` or `claude-profile cycle` to rotate through profiles. The `list` command shows all available profiles with the active one highlighted.

### Mid-Task Context Switch

When you need to temporarily switch contexts for a specific task:

```bash
# Check current context
$ claude-profile current

# Switch to temporary context
$ claude-profile switch client-b

# Perform task with Claude Code...

# Return to default
$ claude-profile switch work
```

Each switch updates `~/.claude/.credentials.json` atomically. Claude Code detects the change immediately, so your next request uses the correct credentials.

### Managing Multiple Clients

Save profiles for each client or project, then switch as needed:

```bash
# Save client profiles
$ claude-profile save client-a
$ claude-profile save client-b
$ claude-profile save internal

# View all profiles
$ claude-profile list
● Active profile: client-a

   No.  Name       Token      Created              Description
   ●   1    client-a   sk-a***    2025-01-15 10:23    Client A projects
       2    client-b   sk-b***    2025-01-15 10:24    Client B projects
       3    internal   sk-i***    2025-01-15 10:25    Internal tools

# Switch between them
$ claude-profile switch client-b
```

Profiles persist in your system keyring, so they survive reboots and are isolated from other users.

## Installation

### Using Poetry (Recommended for Development)

```bash
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
poetry install
poetry run claude-profile --help
```

### Future: PyPI Installation

Once published to PyPI:

```bash
pip install cc-profile-switch
claude-profile --help
```

## Security

CCProfileSwitch stores API tokens in your operating system's credential manager, never in plaintext files except for the single active credential file that Claude Code monitors (`~/.claude/.credentials.json`). This file contains only the currently active token and has file permissions set to 0600 (owner read/write only).

**Credential Storage:**
- macOS: Keychain with AES-128 encryption
- Windows: Credential Manager with DPAPI encryption
- Linux: Secret Service (GNOME Keyring / KWallet) with libsecret

**What's Protected:**
- Profile metadata and tokens stored in encrypted system keyring
- Concurrent access protected by file locking (5-second timeout)
- Token format validation enforces `sk-ant-*` pattern
- Atomic writes prevent partial credential updates

**What's Not Protected:**
- Active credential file (`~/.claude/.credentials.json`) contains plaintext token for Claude Code compatibility
- Exported backups with `--include-tokens` flag contain plaintext tokens (user must encrypt)

For shared or multi-user systems, verify file permissions with `claude-profile doctor`. Each user's keyring is isolated, but ensure no other users have filesystem access to your `~/.claude/` directory.

When exporting profiles with `--include-tokens` for backup or migration, immediately encrypt the export file:

```bash
# Export with tokens
$ claude-profile export backup.json --include-tokens

# Encrypt immediately
$ gpg -c backup.json
$ rm backup.json  # Delete plaintext

# Later: decrypt and import
$ gpg -d backup.json.gpg | claude-profile import-profiles /dev/stdin
```

## Configuration

CCProfileSwitch requires minimal configuration. The tool automatically detects your system's keyring and creates necessary directories.

**Storage Locations:**

| Item | Location | Description |
|------|----------|-------------|
| Active credential | `~/.claude/.credentials.json` | Claude Code credential file (updated on switch) |
| Profile metadata | OS Keyring | Profile names and metadata |
| API tokens | OS Keyring | Encrypted tokens (never plaintext) |

**Environment Variables:**

```bash
# Disable colors and animations (accessibility)
export NO_COLOR=1
export CCPS_NO_COLOR=1

# Force ASCII icons (no Unicode)
export CCPS_ASCII=1

# Override credential file location (advanced)
export CLAUDE_CREDENTIALS_PATH=~/.config/claude/credentials.json
```

**Keyring Backends:**

CCProfileSwitch uses the `keyring` library, which automatically selects the appropriate backend. Check your backend with:

```bash
$ claude-profile doctor
Keyring Check:
✓ Keyring accessible: keyring.backends.macOS.Keychain
```

If no secure backend is available (rare), the tool will warn and suggest installing a keyring provider for your system.

## CLI Reference (Appendix)

### Global Options

| Option | Description |
|--------|-------------|
| `--help` | Show help message |
| `--install-completion` | Install shell completion |

### Commands

**`claude-profile init`** - Initialize profile manager with guided setup

```bash
claude-profile init
```

Sets up credential storage location, imports existing tokens if found, and creates your first profile interactively.

---

**`claude-profile save <name>`** - Save a new profile

```bash
claude-profile save work
claude-profile save personal --description "Personal projects"
```

Options:
- `--token, -t` - Provide token directly (will prompt if not provided)
- `--description, -d` - Profile description
- `--active/--no-active` - Set as active after saving (default: true)
- `--overwrite/--no-overwrite` - Overwrite existing profile

---

**`claude-profile switch [name]`** - Switch to a different profile

```bash
claude-profile switch work          # Switch to specific profile
claude-profile switch               # Interactive selection menu
claude-profile switch --fzf         # Use fzf for selection (if installed)
```

Options:
- `--show-tokens` - Show tokens in selection list
- `--fzf/--no-fzf` - Use fzf for interactive selection

---

**`claude-profile list`** - List all saved profiles

```bash
claude-profile list
claude-profile list --show-tokens
claude-profile list --output-format json
```

Options:
- `--show-tokens` - Show actual tokens (masked by default)
- `--output-format` - Output format: `table` or `json`
- `--active-only` - Show only the active profile

---

**`claude-profile current`** - Show currently active profile

```bash
claude-profile current
```

Displays active profile name, description, creation date, and masked token.

---

**`claude-profile cycle`** - Cycle through available profiles

```bash
claude-profile cycle
```

Activates the next profile in alphabetical order. Useful for quick switching between known profiles.

---

**`claude-profile delete <name>`** - Delete a profile

```bash
claude-profile delete old-profile
claude-profile delete old-profile --no-confirm
```

Options:
- `--confirm/--no-confirm` - Skip confirmation prompt

---

**`claude-profile rename <old> <new>`** - Rename a profile

```bash
claude-profile rename personal personal-projects
```

---

**`claude-profile export [file]`** - Export profiles to backup file

```bash
claude-profile export backup.json
claude-profile export backup.json --include-tokens    # Include plaintext tokens
claude-profile export backup.yaml --export-format yaml
```

Options:
- `--include-tokens` - Include actual tokens (use with caution)
- `--export-format` - Format: `json` or `yaml`

**Security Warning:** Exported files with `--include-tokens` contain plaintext tokens. Encrypt immediately.

---

**`claude-profile import-profiles <file>`** - Import profiles from backup

```bash
claude-profile import-profiles backup.json
claude-profile import-profiles backup.json --prefix work-
claude-profile import-profiles backup.json --replace
```

Options:
- `--merge` - Merge with existing profiles (default)
- `--replace` - Replace all existing profiles
- `--prefix` - Add prefix to imported profile names

---

**`claude-profile show <name>`** - Show profile details

```bash
claude-profile show work
claude-profile show work --show-token
```

Options:
- `--show-token` - Show full token (masked by default)

---

**`claude-profile doctor`** - System diagnostics

```bash
claude-profile doctor
```

Checks keyring availability, credential file permissions, profile integrity, and common configuration issues.

## Troubleshooting

**No secure keyring backend available**

```bash
# Linux: Install keyring backend
sudo apt-get install gnome-keyring  # GNOME
sudo apt-get install kwalletmanager # KDE

# Verify
claude-profile doctor
```

**KeyringLocked error**

macOS: Unlock Keychain in System Preferences → Passwords
Linux: Keyring usually unlocks automatically on login

**Permission issues**

```bash
# Check permissions
ls -la ~/.claude/.credentials.json

# Fix if needed
chmod 600 ~/.claude/.credentials.json

# Run diagnostic
claude-profile doctor
```

**Profile not switching**

```bash
# Verify profile exists
claude-profile list

# Check current profile
claude-profile current

# Force switch
claude-profile switch <name>

# Verify credential file
cat ~/.claude/.credentials.json
```

## Development

### Setup

```bash
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
poetry install
poetry shell
```

### Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=cc_profile_switch --cov-report=term-missing

# Run specific test
poetry run pytest tests/test_cli.py -xvs
```

### Code Quality

```bash
# Format code
poetry run black cc_profile_switch tests
poetry run isort cc_profile_switch tests

# Lint
poetry run flake8 cc_profile_switch

# Type check
poetry run mypy cc_profile_switch
```

### Contributing

Contributions welcome! Please ensure:
- All tests pass
- Code formatted with black and isort
- Type hints complete
- Documentation updated

## Acknowledgments

Built with:
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting with beautiful visual effects
- [Keyring](https://github.com/jaraco/keyring) - Secure credential storage
- [FileLock](https://github.com/tox-dev/filelock) - Concurrent access protection
- [PlatformDirs](https://github.com/platformdirs/platformdirs) - Cross-platform config paths
- [Poetry](https://python-poetry.org/) - Dependency management

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contact

- **GitHub Issues**: [https://github.com/biostochastics/CCProfileSwitch/issues](https://github.com/biostochastics/CCProfileSwitch/issues)
- **Repository**: [https://github.com/biostochastics/CCProfileSwitch](https://github.com/biostochastics/CCProfileSwitch)
- **Documentation**: [https://deepwiki.com/biostochastics/CCProfileSwitch](https://deepwiki.com/biostochastics/CCProfileSwitch)

---

*Part of the Biostochastics collection of developer tools*
