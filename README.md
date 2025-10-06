# CCProfileSwitch

**Switch between Claude Code profiles in seconds—without context mistakes or credential exposure.**

[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/biostochastics/CCProfileSwitch) [![Python Version](https://img.shields.io/badge/python-3.8.1%2B-blue)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![pipx](https://img.shields.io/badge/install-pipx-brightgreen)](https://pipx.pypa.io/) [![Typer](https://img.shields.io/badge/CLI-typer-green)](https://typer.tiangolo.com/) [![Rich](https://img.shields.io/badge/UI-rich-orange)](https://rich.readthedocs.io/) [![Keyring](https://img.shields.io/badge/security-keyring-red)](https://github.com/jaraco/keyring) [![DeepWiki](https://img.shields.io/badge/DeepWiki-docs-purple)](https://deepwiki.com/biostochastics/CCProfileSwitch)

## Why CCProfileSwitch?

If you juggle multiple Claude accounts across personal and professional projects, you know the friction: manually re-authenticating, risking context slips where you accidentally use the wrong account, and managing OAuth sessions. CCProfileSwitch eliminates this workflow tax by managing complete authentication profiles in your operating system's secure storage and switching contexts with a single command.

The tool integrates directly with Claude Code's authentication system:
- **macOS**: Writes complete OAuth credentials (including refresh tokens) to macOS Keychain, preserving MCP server authentication
- **Linux/Windows**: Updates credential files that Claude Code monitors

**Important:** Profile switching requires closing and restarting Claude Code to load the new credentials. This is not a mid-session operation—you must exit Claude Code, run `claude-profile switch <name>`, then start Claude Code again.

Whether you're switching between client accounts, separating personal and work usage, or managing team credentials, CCProfileSwitch handles the mechanics so you can focus on your actual work.

## How It Works

CCProfileSwitch stores complete authentication credentials in your system's native secure storage:

**macOS Architecture:**
- **Profile Storage**: System Keyring (`claude-profile-manager` service)
  - Stores complete OAuth JSON including `accessToken`, `refreshToken`, `expiresAt`, `scopes`, `subscriptionType`
  - Preserves MCP server OAuth tokens (`mcpOAuth`)
  - Profile metadata (description, creation date)

- **Active Session**: macOS Keychain (`Claude Code-credentials` service)
  - Full OAuth structure written via `security` command
  - Claude Code reads directly from Keychain
  - No credential file created on disk (Keychain-only)

**Linux/Windows Architecture:**
- **Profile Storage**: System credential manager (GNOME Keyring, KWallet, Windows Credential Manager)
- **Active Session**: `~/.claude/.credentials.json` (file-based)

On first run, it automatically detects your existing Claude Code credentials and imports them as a profile—no manual token entry needed. When you need to switch contexts, you run `claude-profile switch <name>`, and the tool writes that profile's complete authentication to Claude Code's storage. The workflow looks like this:

```bash
# Morning: Start with client-a work
$ claude-profile switch client-a
✔ Switched to profile 'client-a'
# Now close and restart Claude Code to use client-a credentials

# Run Claude Code tasks for client-a...

# Afternoon: Switch to personal projects (while Claude Code is closed)
$ claude-profile switch personal
✔ Switched to profile 'personal'
# Now start Claude Code to use personal credentials

# Confirm active context
$ claude-profile current
● Active profile: personal
  Description: Personal projects
  Token: sk-a***
```

Profile switching is instant, secure, and deterministic. You always know which context is active, and your credentials are stored securely:
- **macOS**: All credentials in Keychain (OAuth tokens never written to disk)
- **Linux/Windows**: Active credentials in monitored file, profiles in system credential manager

## Quick Start

Install CCProfileSwitch and let it auto-detect your current Claude token:

```bash
# Clone and install with pipx (recommended)
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
pipx install .

# Initialize - auto-detects and imports your current token as 'default' profile
claude-profile init

# Save additional profiles with different tokens
# Method 1: Let it auto-detect current token (if you've switched in Claude Code)
claude-profile save work

# Method 2: Provide token explicitly
claude-profile save personal --token sk-ant-...

# Method 3: Will prompt for token interactively
claude-profile save client-a

# Switch between profiles
claude-profile switch work
```

**Note:** If using Poetry for development, prefix commands with `poetry run` or use `poetry shell` first. See [Installation](#installation) for details.

The `init` command automatically detects your existing Claude Code credentials from:
- **macOS**: Keychain service `Claude Code-credentials` (complete OAuth structure including refreshToken)
- **Linux**: `~/.claude/.credentials.json` or platform-specific paths
- **Windows**: `AppData/Roaming/Claude/.credentials.json` or `AppData/Local/Claude/.credentials.json`

**OAuth Support (All Platforms):**
- ✅ Preserves complete OAuth session including `refreshToken` for seamless authentication
- ✅ Maintains MCP server OAuth tokens (`mcpOAuth`) for persistent MCP connections
- ✅ Supports both OAuth tokens (`sk-ant-oat*`, `sk-ant-ort*`) and API keys (`sk-ant-api*`)
- ✅ Works on macOS (Keychain - tested), Linux (.credentials.json), and Windows (credential files)

> **Note**: OAuth preservation has been verified on macOS. Linux/Windows OAuth support is implemented and should work correctly, but has not been tested on those platforms yet. Please report any issues!

After setup, you must close and restart Claude Code to use the active profile's credentials.

## Common Workflows

### Starting Your Day

Confirm or set your default context before beginning work:

```bash
$ claude-profile current
● Active profile: work
```

If you need to switch, use `claude-profile switch <name>` or `claude-profile cycle` to rotate through profiles. The `list` command shows all available profiles with the active one highlighted.

### Context Switching Between Tasks

When you need to switch contexts for a different task:

```bash
# Check current context (while Claude Code is closed)
$ claude-profile current

# Switch to different context
$ claude-profile switch client-b
# Now start Claude Code to use client-b credentials

# Perform task with Claude Code...
# Close Claude Code when done

# Return to default context
$ claude-profile switch work
# Start Claude Code again to use work credentials
```

Each switch updates Claude Code's authentication storage atomically:
- **macOS**: Updates Keychain entry (no file modification)
- **Linux/Windows**: Updates `~/.claude/.credentials.json`

**You must close and restart Claude Code after switching** for the new credentials to take effect.

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

### Using pipx (Recommended for Daily Use)

Install globally without affecting your system Python:

```bash
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch

# Install pipx if needed
brew install pipx  # macOS
# or: pip install --user pipx  # Linux/Windows

# Install CCProfileSwitch globally
pipx install .

# Now works from anywhere without poetry run
claude-profile --help
claude-profile init
```

### Using Poetry (Recommended for Development)

```bash
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
poetry install

# Option 1: Use poetry run before each command
poetry run claude-profile --help

# Option 2: Activate virtual environment once
poetry shell
claude-profile --help  # Now works without poetry run
```

### Shell Alias (Quick Setup)

Add to `~/.zshrc` or `~/.bashrc`:

```bash
alias claude-profile='poetry -C /Users/YOUR_USERNAME/CCProfileSwitch run claude-profile'
```

Then reload: `source ~/.zshrc`

### Future: PyPI Installation

Once published to PyPI:

```bash
pip install cc-profile-switch
claude-profile --help
```

## Security

CCProfileSwitch stores authentication credentials in your operating system's secure credential storage with platform-specific optimizations.

**Credential Storage by Platform:**

**macOS (Keychain-Only):**
- **Profile Storage**: System Keyring service `claude-profile-manager`
  - AES-128 encryption via macOS Keychain
  - Stores complete OAuth JSON (accessToken, refreshToken, expiresAt, scopes, mcpOAuth)
- **Active Session**: Keychain service `Claude Code-credentials`
  - Written via `security` command for Claude Code compatibility
  - **No credential file created** - fully Keychain-based
  - Preserves refresh tokens for persistent authentication
  - Maintains MCP server OAuth tokens

**Windows:**
- Profile Storage: Credential Manager with DPAPI encryption
- Active Session: File at `AppData/Roaming/Claude/.credentials.json` (0600 permissions)

**Linux:**
- Profile Storage: Secret Service (GNOME Keyring / KWallet) with libsecret
- Active Session: File at `~/.claude/.credentials.json` (0600 permissions)

**Auto-Detection & OAuth Support:**
- Automatically detects existing Claude Code credentials on first run
- **All Platforms**: Reads complete OAuth structure, including:
  - `accessToken` (sk-ant-oat*) - Active authentication token
  - `refreshToken` (sk-ant-ort*) - Token refresh capability
  - `expiresAt`, `scopes`, `subscriptionType` - Session metadata
  - `mcpOAuth` - MCP server authentication tokens
- **macOS**: Reads from Keychain service `Claude Code-credentials`
- **Linux/Windows**: Reads from credential files (`~/.claude/.credentials.json`, etc.)
- Supports both OAuth tokens and API keys (sk-ant-api*)

**What's Protected:**
- **All credentials encrypted** in system-native credential storage
- Concurrent access protected by file locking (5-second timeout)
- Token format validation enforces `sk-ant-*` pattern
- Atomic writes prevent partial credential updates
- **All Platforms**: Complete OAuth structure preserved (never loses refresh tokens or MCP auth)

**What's Not Protected:**
- **macOS**: All credentials stay in Keychain (maximum security - no plaintext files)
- **Linux/Windows**: Active credential file contains plaintext OAuth JSON for Claude Code compatibility (0600 permissions)
- Exported backups with `--include-tokens` flag contain plaintext tokens (user must encrypt)

For shared or multi-user systems, verify security with `claude-profile doctor`. Each user's credential storage is isolated.

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

| Platform | Profile Storage | Active Session | OAuth Support |
|----------|----------------|----------------|---------------|
| **macOS** | System Keyring (`claude-profile-manager`) | Keychain (`Claude Code-credentials`) | ✅ Full OAuth (tested) |
| **Windows** | Credential Manager (DPAPI) | `AppData/Roaming/Claude/.credentials.json` | ✅ Full OAuth (untested) |
| **Linux** | Secret Service (libsecret) | `~/.claude/.credentials.json` | ✅ Full OAuth (untested) |

> **Testing Status**: macOS OAuth support has been verified. Windows/Linux implementations are complete but await real-world testing.

**macOS Architecture Details:**
- Profiles: System Keyring stores `{"token": "{OAuth JSON}", "metadata": {...}}`
- Active: Keychain stores raw OAuth JSON via `security add-generic-password`
- Result: No credential files on disk, complete OAuth preservation

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

Checks keyring availability, authentication storage, profile integrity, and common configuration issues.

**Example Output (macOS):**
```
Keyring Check:
✓ Keyring accessible: keyring.backends.macOS.Keyring

Active Token Check:
⚠ Token file does not exist: ~/.claude/.credentials.json
✓ Token found in macOS Keychain (OAuth authentication)

Profiles Check:
✓ Found 3 profiles
```

The warning about missing file is **normal on macOS** - authentication is stored in Keychain, not files.

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

# Run diagnostics
claude-profile doctor

# Force switch
claude-profile switch <name>

# Verify authentication (macOS)
security find-generic-password -s "Claude Code-credentials" -w | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('claudeAiOauth',{}).get('accessToken','')[:50])"

# Verify authentication (Linux/Windows)
cat ~/.claude/.credentials.json
```

**macOS Note:** If `doctor` shows "Token found in macOS Keychain" but Claude Code doesn't authenticate, close and restart Claude Code to reload the Keychain credentials.

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
