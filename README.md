# CCProfileSwitch

<p align="center">
  <img src="assets/logo.png" alt="CCProfileSwitch Logo" width="300"/>
</p>

<p align="center">
  <strong>Seamless Claude Code profile management with secure credential storage and cross-platform support</strong>
</p>

[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/biostochastics/CCProfileSwitch) [![Python Version](https://img.shields.io/badge/python-3.8.1%2B-blue)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Typer](https://img.shields.io/badge/CLI-typer-green)](https://typer.tiangolo.com/) [![Rich](https://img.shields.io/badge/UI-rich-orange)](https://rich.readthedocs.io/) [![Keyring](https://img.shields.io/badge/security-keyring-red)](https://github.com/jaraco/keyring)

## Table of Contents

- [What is CCProfileSwitch?](#what-is-ccprofileswitch)
- [Quick Start](#quick-start)
- [Core Features](#core-features)
- [Usage Guide](#usage-guide)
- [CLI Reference](#cli-reference)
- [Configuration](#configuration)
- [Security](#security)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)
- [License](#license)
- [Contact](#contact)

## What is CCProfileSwitch?

CCProfileSwitch is a command-line tool that simplifies managing multiple Claude profiles for **Claude Code** and **Anthropic API** usage. If you work across personal and professional projects, switching between Claude API accounts becomes effortless with secure credential storage and one-command profile switching.

**Why CCProfileSwitch?**
- **Secure Storage**: OS-native keyring integration (macOS Keychain, Windows Credential Manager, Linux Secret Service)
- **Zero Configuration Files**: No plaintext API keys in config files or environment variables
- **One-Command Switching**: Switch profiles instantly without manual credential updates
- **Cross-Platform**: Works seamlessly on macOS, Linux, and Windows

**Primary Use Cases:**
- Managing separate Claude Code profiles for work and personal projects
- Switching between multiple Anthropic API keys in team environments
- Development workflows requiring frequent Claude account switching
- Secure credential management for CI/CD pipelines and automation

### Claude Code Integration

CCProfileSwitch seamlessly integrates with **Claude Code** by managing the credential file that Claude Code reads for authentication:

- **Credential Location**: Updates `~/.claude/.credentials.json` (Claude Code's default credential file)
- **Token Format**: Validates Anthropic API tokens (`sk-ant-*` format)
- **Zero Configuration**: Claude Code automatically detects credential changes
- **Instant Switching**: No need to restart Claude Code after switching profiles

When you switch profiles with `claude-profile switch <profile>`, Claude Code immediately uses the new credentials for subsequent API requests.

## Quick Start

### Installation


<details>
<summary>Using Poetry</summary>

```bash
# Clone repository
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch

# Install with Poetry
poetry install

# Run CCProfileSwitch
poetry run claude-profile --help
```
</details>

### Your First Profile

```bash
# Initialize the profile manager
claude-profile init

# Save your first profile
claude-profile save personal

# Switch to a profile
claude-profile switch personal
```

**Expected behavior:** CCProfileSwitch updates `~/.claude/.credentials.json` with the selected profile's API key. Claude Code automatically uses this credential file for authentication.

### Common Examples

```bash
# Save a work profile
claude-profile save work

# Switch between profiles
claude-profile switch personal
claude-profile switch work

# List all profiles
claude-profile list

# Show current active profile
claude-profile current
```

> **⚠️ Security Note**
> CCProfileSwitch stores API keys in your operating system's secure credential manager. Keys are never stored in plaintext files. See the [Security](#security) section for detailed information.

**Next Steps:**
- See [Usage Guide](#usage-guide) for detailed workflows
- Check [CLI Reference](#cli-reference) for all available commands
- Review [Security](#security) for credential storage details

## Core Features

- **Secure Keyring Storage** - API keys stored in OS-native credential managers (macOS Keychain, Windows Credential Manager, Linux Secret Service)
- **Claude-Specific Token Validation** - Validates `sk-ant-*` format tokens to ensure compatibility with Claude Code and Anthropic API
- **Concurrent Access Protection** - File locking prevents race conditions when multiple processes access profiles
- **Interactive Profile Setup** - Guided `init` command gets you started in seconds
- **Fast Profile Switching** - One-command switching updates active credentials instantly
- **Enhanced CLI Experience** - Beautiful, tasteful terminal interface with:
  - Animated spinners for operations
  - Visual profile carousel during cycling
  - Styled tables with active profile highlighting
  - Smooth transitions with before/after feedback
  - Command headers for clear visual hierarchy
  - Accessible color schemes (colorblind-friendly)
  - TTY detection with NO_COLOR support
- **Fuzzy Finding** *(Optional)* - Integrate with `fzf` for quick interactive profile selection
- **Profile Management** - Save, delete, rename, and list profiles with intuitive commands
- **Import/Export** - Backup and restore profiles across systems with enhanced security warnings
- **System Diagnostics** - Built-in `doctor` command checks configuration and diagnoses issues
- **Rich CLI Interface** - Beautiful terminal output powered by Rich with tasteful animations and effects
- **Cross-Platform** - Unified experience on macOS, Linux, and Windows
- **Zero Plaintext Storage** - No API keys in configuration files or environment variables

## Usage Guide

### Basic Usage

**Initialize Profile Manager**

```bash
# Run interactive initialization
claude-profile init

# The init command will:
# 1. Set up credential storage location (~/.claude/.credentials.json)
# 2. Import any existing Claude tokens
# 3. Configure your first profile
```

**Save Profiles**

```bash
# Save a new profile (prompts for API key)
claude-profile save personal

# Save another profile
claude-profile save work
```

**Switch Between Profiles**

```bash
# Switch to a specific profile
claude-profile switch personal

# Interactive switch (shows menu if no profile specified)
claude-profile switch

# Cycle through available profiles
claude-profile cycle
```

**List and Show Profiles**

```bash
# List all saved profiles
claude-profile list

# Show currently active profile
claude-profile current

# Show details of a specific profile
claude-profile show work
```

### Advanced Workflows

**Profile Management**

```bash
# Rename a profile
claude-profile rename old-name new-name

# Delete a profile
claude-profile delete old-profile

# Delete with confirmation prompt
claude-profile delete work  # Will ask for confirmation
```

**Backup and Restore**

```bash
# Export profiles to backup file
claude-profile export profiles-backup.json

# Export to specific location
claude-profile export ~/backups/claude-profiles.json

# Import profiles from backup
claude-profile import-profiles profiles-backup.json

# Import merges with existing profiles
claude-profile import-profiles ~/backups/claude-profiles.json
```

**System Diagnostics**

```bash
# Run system health check
claude-profile doctor

# The doctor command checks:
# - Keyring availability and configuration
# - Credential file location and permissions
# - Profile integrity
# - Common configuration issues
```

### Common Recipes

**Setting Up Multiple Work Environments**

```bash
# Initialize
claude-profile init

# Save profiles for different projects
claude-profile save client-a
claude-profile save client-b
claude-profile save internal

# Switch as needed
claude-profile switch client-a
```

**Migrating to New System**

```bash
# On old system: export profiles
claude-profile export ~/claude-profiles-backup.json

# Transfer file to new system

# On new system: install and import
pip install cc-profile-switch
claude-profile init
claude-profile import-profiles ~/claude-profiles-backup.json
```

**Daily Workflow**

```bash
# Morning: switch to work profile
claude-profile switch work

# Evening: switch to personal projects
claude-profile switch personal

# Or use cycle to rotate through profiles
claude-profile cycle
```

## CLI Reference

### Global Options

| Option | Description |
|--------|-------------|
| `--help` | Show help message |
| `--install-completion` | Install shell completion |
| `--show-completion` | Show shell completion code |

### Commands

#### `claude-profile init`

Initialize the profile manager with guided setup.

**Usage:** `claude-profile init`

**What it does:**
- Sets up credential storage location
- Imports existing Claude tokens if found
- Creates your first profile interactively
- Validates keyring availability

#### `claude-profile save`

Save a new profile with API key.

**Usage:** `claude-profile save <profile-name>`

**Arguments:**
- `profile-name` - Name for the profile (e.g., "personal", "work")

**Example:**
```bash
claude-profile save work
# Prompts: Enter API key for profile 'work':
```

#### `claude-profile switch`

Switch to a different profile.

**Usage:** `claude-profile switch [profile-name]`

**Arguments:**
- `profile-name` - (Optional) Profile to activate. If omitted, shows interactive menu.

**Example:**
```bash
# Switch to specific profile
claude-profile switch personal

# Interactive selection
claude-profile switch
```

#### `claude-profile list`

List all saved profiles.

**Usage:** `claude-profile list`

**Output:** Displays table with profile names and active status.

#### `claude-profile current`

Show the currently active profile.

**Usage:** `claude-profile current`

**Output:** Displays active profile name and last updated timestamp.

#### `claude-profile cycle`

Cycle through available profiles.

**Usage:** `claude-profile cycle`

**What it does:** Activates the next profile in alphabetical order. Useful for quick switching.

#### `claude-profile delete`

Delete a profile from storage.

**Usage:** `claude-profile delete <profile-name>`

**Arguments:**
- `profile-name` - Name of profile to delete

**Options:**
- `--no-confirm` - Skip confirmation prompt

**Example:**
```bash
# With confirmation
claude-profile delete old-profile

# Skip confirmation
claude-profile delete old-profile --no-confirm
```

#### `claude-profile rename`

Rename an existing profile.

**Usage:** `claude-profile rename <old-name> <new-name>`

**Arguments:**
- `old-name` - Current profile name
- `new-name` - New profile name

**Example:**
```bash
claude-profile rename personal personal-projects
```

#### `claude-profile export`

Export profiles to backup file.

**Usage:** `claude-profile export [output-file]`

**Arguments:**
- `output-file` - (Optional) Path for export file (prints to stdout if not provided)

**Options:**
- `--include-tokens` - Include API tokens in export (use with caution)
- `--export-format` - Export format: `json` or `yaml` (default: `json`)

**Example:**
```bash
# Export without tokens (metadata only)
claude-profile export backup.json

# Export with tokens (for migration)
claude-profile export backup.json --include-tokens

# Export to YAML format
claude-profile export backup.yaml --export-format yaml
```

> **Security Warning:** Exported files with `--include-tokens` contain plaintext API tokens. Encrypt and store securely.

#### `claude-profile import-profiles`

Import profiles from backup file.

**Usage:** `claude-profile import-profiles <input-file>`

**Arguments:**
- `input-file` - Path to import file

**Options:**
- `--merge` - Merge with existing profiles (default)
- `--replace` - Replace all existing profiles
- `--prefix` - Add prefix to imported profile names

**Example:**
```bash
# Merge import
claude-profile import-profiles backup.json

# Replace all profiles
claude-profile import-profiles backup.json --replace

# Import with prefix
claude-profile import-profiles backup.json --prefix work-
```

#### `claude-profile show`

Show details of a specific profile.

**Usage:** `claude-profile show <profile-name>`

**Arguments:**
- `profile-name` - Profile to display

**Options:**
- `--show-token` - Show full API token (masked by default)

**Example:**
```bash
# Show with masked token
claude-profile show work

# Reveal full token
claude-profile show work --show-token
```

#### `claude-profile doctor`

Check system configuration and diagnose issues.

**Usage:** `claude-profile doctor`

**What it checks:**
- Keyring backend availability
- Credential file location and permissions
- Profile integrity and validation
- Common configuration issues

**Output:** Detailed diagnostic report with recommendations.

### Shell Completion

Enable tab completion for your shell:

```bash
# Bash
claude-profile --install-completion bash

# Zsh
claude-profile --install-completion zsh

# Fish
claude-profile --install-completion fish
```

## Configuration

CCProfileSwitch uses minimal configuration by design. All settings are managed automatically.

### Storage Locations

| Item | Location | Description |
|------|----------|-------------|
| **Active Credentials** | `~/.claude/.credentials.json` | Claude SDK credential file (updated on switch) |
| **Profile Metadata** | OS Keyring | Profile names and metadata |
| **API Keys** | OS Keyring | Encrypted API keys (never plaintext) |

### Keyring Backends

CCProfileSwitch automatically selects the appropriate keyring backend:

| Platform | Backend | Storage Location |
|----------|---------|------------------|
| **macOS** | Keychain | macOS Keychain (encrypted) |
| **Windows** | Windows Credential Manager | Windows Credential Vault (encrypted) |
| **Linux** | Secret Service | GNOME Keyring / KWallet (encrypted) |

**Fallback:** If no secure backend is available, CCProfileSwitch warns and uses encrypted file storage.

### Environment Variables

```bash
# Override credential file location
export CLAUDE_CREDENTIALS_PATH=~/.config/claude/credentials.json

# Keyring service name (advanced)
export CC_KEYRING_SERVICE=claude-profile

# Disable colors and animations (accessibility)
export NO_COLOR=1
export CCPS_NO_COLOR=1

# Force ASCII icons (no Unicode)
export CCPS_ASCII=1
```

## Security

### Security Architecture

CCProfileSwitch implements security best practices for credential management:

**OS-Native Encryption**
- All API keys stored in operating system credential managers
- macOS Keychain uses AES-128 encryption
- Windows Credential Manager uses DPAPI encryption
- Linux Secret Service uses libsecret with encrypted backends

**Zero Plaintext Storage**
- No API keys in configuration files
- No API keys in environment variables
- No API keys in version control

**Credential File Protection**
- `~/.claude/.credentials.json` contains only the active API key
- File permissions automatically set to `0600` (owner read/write only)
- Temporary exposure minimized (only active profile)

**Secure Backup/Export**
- Exports without `--include-tokens` contain only metadata
- Exports with `--include-tokens` are plaintext (user responsibility to encrypt)
- Enhanced export warnings provide encryption examples (GPG, age)
- Import validates file integrity before applying

**Concurrent Access Protection**
- File locking with 5-second timeout prevents race conditions
- Safe for multiple processes accessing profiles simultaneously
- Atomic writes ensure data integrity

### Security Features

- **Automatic Permission Setting**: Credential files created with restrictive permissions
- **Keyring Validation**: Verifies secure backend availability on init
- **Token Format Validation**: Enforces Claude-specific `sk-ant-*` token format
- **Profile Integrity Checks**: Validates profile data on load
- **Concurrent Access Protection**: File locking prevents race conditions
- **Audit Trail**: `doctor` command reviews security configuration

### ⚠️ Important Security Warnings

#### Backup Security

When exporting profiles with `--include-tokens`, the exported file contains **plaintext API keys**. Always:
1. Encrypt backup files using `gpg`, `age`, or similar tools
2. Store backups in secure locations (password managers, encrypted drives)
3. Never commit backup files to version control
4. Delete unencrypted exports after secure storage

#### Shared Systems

On shared or multi-user systems:
- Each user has isolated keyring storage
- Verify no other users have file system access to `~/.claude/`
- Use `claude-profile doctor` to check permissions
- Consider using dedicated service accounts

#### Recommended Security Practices

1. **Regular Rotation** - Rotate API keys periodically and update profiles
2. **Minimal Exposure** - Only export with `--include-tokens` when necessary
3. **Audit Configuration** - Run `claude-profile doctor` regularly
4. **Secure Transport** - When migrating systems, use encrypted transfer (ssh, encrypted email)
5. **Delete Old Profiles** - Remove unused profiles to minimize exposure

### Security Disclosure

To report security vulnerabilities, please open a GitHub issue with the `security` label or contact maintainers directly. We follow responsible disclosure practices and credit reporters.

### Liability Disclaimer

**NO WARRANTY**: This software is provided "as is" without warranty of any kind, express or implied.

**NO LIABILITY**: In no event shall the authors be liable for any claim, damages, or other liability arising from the use of this software.

**USE AT YOUR OWN RISK**: Users assume all responsibility for API key security, backup encryption, and compliance with applicable regulations.

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch

# Install Poetry if needed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies (including dev)
poetry install

# Activate virtual environment
poetry shell
```

### Code Quality & Testing

```bash
# Run all tests with coverage
poetry run pytest --cov=cc_profile_switch --cov-report=term-missing

# Run specific test file
poetry run pytest tests/test_cli.py -xvs

# Format code
poetry run black cc_profile_switch tests
poetry run isort cc_profile_switch tests

# Lint code
poetry run flake8 cc_profile_switch
poetry run mypy cc_profile_switch

# Run pre-commit hooks
poetry run pre-commit run --all-files
```

### Building & Publishing

```bash
# Build package
poetry build

# Check package
poetry check

# Publish to PyPI (requires credentials)
poetry publish

# Build and publish together
poetry publish --build
```

### Contributing

We welcome contributions! Please ensure:
- All tests pass (`pytest`)
- Code is formatted (`black`, `isort`)
- Type hints are complete (`mypy`)
- Documentation is updated
- Commit messages are descriptive

## Troubleshooting

### Keyring Issues

**No secure keyring backend available**

```bash
# Linux: Install keyring backend
sudo apt-get install gnome-keyring  # GNOME
sudo apt-get install kwalletmanager # KDE

# Verify keyring
claude-profile doctor
```

**KeyringLocked error**

```bash
# macOS: Unlock Keychain
# System Preferences → Passwords → Unlock

# Linux: Unlock keyring
# Usually happens automatically on login
```

### Permission Issues

```bash
# Check credential file permissions
ls -la ~/.claude/.credentials.json

# Fix permissions if needed
chmod 600 ~/.claude/.credentials.json

# Run diagnostic
claude-profile doctor
```

### Profile Not Switching

```bash
# Verify profile exists
claude-profile list

# Check current profile
claude-profile current

# Force switch
claude-profile switch profile-name

# Check credential file
cat ~/.claude/.credentials.json
```

### Import/Export Issues

```bash
# Check file format
cat backup.json | python -m json.tool

# Import profiles
claude-profile import-profiles backup.json
```

## Acknowledgments

CCProfileSwitch is built with these open-source tools:

- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [Keyring](https://github.com/jaraco/keyring) - Secure credential storage
- [FileLock](https://github.com/tox-dev/filelock) - Concurrent access protection
- [PlatformDirs](https://github.com/platformdirs/platformdirs) - Cross-platform config paths
- [Poetry](https://python-poetry.org/) - Dependency management

Special thanks to the Claude team for creating an amazing AI assistant platform.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**GitHub Issues**: [https://github.com/biostochastics/CCProfileSwitch/issues](https://github.com/biostochastics/CCProfileSwitch/issues)

**GitHub Repository**: [https://github.com/biostochastics/CCProfileSwitch](https://github.com/biostochastics/CCProfileSwitch)

---

*Part of the Biostochastics collection of developer tools for enhanced productivity*
