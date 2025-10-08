# CCProfileSwitch

```
    ┌─────────────────────┐
    │   Profile A         │
    ├─────────────────────┤
    │        ◄══►         │  Switch
    ├─────────────────────┤
    │   Profile B         │
    └─────────────────────┘
```

**Switch between Claude Code and Z-AI profiles securely—manage multiple AI providers with isolated configurations.**

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/biostochastics/CCProfileSwitch) [![Python Version](https://img.shields.io/badge/python-3.8.1%2B-blue)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![pipx](https://img.shields.io/badge/install-pipx-brightgreen)](https://pipx.pypa.io/) [![Typer](https://img.shields.io/badge/CLI-typer-green)](https://typer.tiangolo.com/) [![Rich](https://img.shields.io/badge/UI-rich-orange)](https://rich.readthedocs.io/) [![Keyring](https://img.shields.io/badge/security-keyring-red)](https://github.com/jaraco/keyring) [![DeepWiki](https://img.shields.io/badge/DeepWiki-docs-purple)](https://deepwiki.com/biostochastics/CCProfileSwitch)

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
  - [What CCProfileSwitch Does](#what-ccprofileswitch-does)
  - [System Architecture](#system-architecture)
  - [OAuth Token Management](#oauth-token-management)
  - [Seamless Provider Switching](#seamless-provider-switching)
  - [Z-AI GLM-4.6 Coder Integration](#z-ai-glm-46-coder-integration)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
  - [Starting Your Day](#starting-your-day)
  - [Context Switching Between Tasks](#context-switching-between-tasks)
  - [Managing Multiple Clients](#managing-multiple-clients)
- [Complete CLI Reference](#complete-cli-reference)
- [Advanced Topics](#advanced-topics)
  - [Security](#security)
  - [Configuration](#configuration)
  - [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

If you juggle multiple Claude accounts across personal and professional projects, you know the friction: manually re-authenticating, risking context slips where you accidentally use the wrong account, and managing OAuth sessions. CCProfileSwitch eliminates this workflow tax by managing complete authentication profiles in your operating system's secure storage and switching contexts with a single command.

### Key Features

- **Secure Credential Storage**: Stores API keys and OAuth tokens in your system's native keyring (Keychain on macOS, Credential Manager on Windows, Secret Service on Linux)
- **Shell Environment Management**: Sets environment variables for Claude Code via the `cpswitch` command
- **Multi-Provider Support**: Seamlessly manage both Claude and Z-AI profiles with isolated configurations
- **OAuth Preservation**: Maintains complete OAuth sessions including refresh tokens and MCP server authentication
- **Cross-Platform**: Works on macOS, Linux, and Windows with platform-specific optimizations

### What's Different?

**No shell modifications, no environment variable exports, no complex configuration.** Just secure storage and settings file management.

The tool integrates directly with Claude Code's authentication system:
- **macOS**: Writes complete OAuth credentials (including refresh tokens) to macOS Keychain, preserving MCP server authentication
- **Linux/Windows**: Updates credential files that Claude Code monitors

**Important:** Profile switching requires closing and restarting Claude Code to load the new credentials. This is not a mid-session operation—you must exit Claude Code, run `claude-profile switch <name>`, then start Claude Code again.

Whether you're switching between client accounts, separating personal and work usage, or managing team credentials, CCProfileSwitch handles the mechanics so you can focus on your actual work.

## Quick Start

Install CCProfileSwitch and let it auto-detect your current Claude token:

```bash
# Clone and install with pipx (recommended)
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
pipx install .

# Initialize - auto-detects and imports your current token as 'default' profile
# Also offers to set up shell integration automatically
claude-profile init

# The init command will:
# 1. Import your existing Claude credentials as 'default' profile
# 2. Detect your shell (bash/zsh/fish)
# 3. Offer to add shell integration to ~/.zshrc or ~/.bashrc
# 4. Enable the 'cpswitch' command for automatic environment setup

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
- Preserves complete OAuth session including `refreshToken` for seamless authentication
- Maintains MCP server OAuth tokens (`mcpOAuth`) for persistent MCP connections
- Supports both OAuth tokens (`sk-ant-oat*`, `sk-ant-ort*`) and API keys (`sk-ant-api*`)
- Works on macOS (Keychain - tested), Linux (.credentials.json), and Windows (credential files)

> **Note**: OAuth preservation has been verified on macOS. Linux/Windows OAuth support is implemented and should work correctly, but has not been tested on those platforms yet. Please report any issues!

After setup, you must close and restart Claude Code to use the active profile's credentials.

## Core Concepts

### What CCProfileSwitch Does

CCProfileSwitch performs **two simple but essential tasks**:

1. **Secure Credential Storage**: Stores API keys and tokens in your system's native keyring (Keychain on macOS, Credential Manager on Windows, Secret Service on Linux)
2. **Shell Environment Management**: The `cpswitch` command sets environment variables that Claude Code reads at startup

**That's it.** Credentials stay in secure storage, environment variables are set when you switch profiles, and Claude Code reads them automatically.

### System Architecture

CCProfileSwitch stores complete authentication credentials in your system's native secure storage with platform-specific optimizations.

#### macOS Architecture

- **Profile Storage**: System Keyring (`claude-profile-manager` service)
  - Stores complete OAuth JSON including `accessToken`, `refreshToken`, `expiresAt`, `scopes`, `subscriptionType`
  - Preserves MCP server OAuth tokens (`mcpOAuth`)
  - Profile metadata (description, creation date)

- **Active Session**: macOS Keychain (`Claude Code-credentials` service)
  - Full OAuth structure written via `security` command
  - Claude Code reads directly from Keychain
  - No credential file created on disk (Keychain-only)

#### Linux/Windows Architecture

- **Profile Storage**: System credential manager (GNOME Keyring, KWallet, Windows Credential Manager)
- **Active Session**: `~/.claude/.credentials.json` (file-based)

#### Workflow

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

### OAuth Token Management

**OAuth tokens expire after approximately 1 hour** and require periodic refresh. CCProfileSwitch handles OAuth tokens differently depending on your platform:

#### macOS

- OAuth tokens stored in **macOS Keychain** by CCProfileSwitch
- CCProfileSwitch saves complete OAuth sessions (access token, refresh token, expiration) in keyring
- When switching between Claude accounts, CCProfileSwitch restores the OAuth for that profile
- Claude Code reads OAuth from Keychain - CCProfileSwitch manages which OAuth is active

#### Windows/Linux

- OAuth tokens stored in CCProfileSwitch's secure storage
- CCProfileSwitch writes OAuth to settings.json when switching profiles
- Expiration warnings shown if token is stale
- **After switching OAuth profiles**: Run `/login` in Claude Code if you see 401 errors

#### Z-AI API Keys (All Platforms)

- Z-AI tokens stored in CCProfileSwitch's secure keyring storage
- Z-AI uses API keys, not OAuth
- When you run `cpswitch`, the token is exported as `ANTHROPIC_AUTH_TOKEN` environment variable
- Claude Code reads the token from the environment
- No `/login` needed - authentication is via API key

#### Recommended Workflow

```bash
# Switch to OAuth profile
$ claude-profile switch work
⚠ OAuth token expired 120 minutes ago
After switching, run /login in Claude Code to refresh
✔ Switched to profile 'work'

# Restart Claude Code
$ # Close and restart Claude Code

# In Claude Code, run /login to refresh OAuth token
# Then continue working
```

#### Why This Design?

- OAuth tokens contain `accessToken`, `refreshToken`, and `expiresAt`
- Stored tokens in profiles can become stale (especially if profile unused for hours/days)
- Platform-specific storage (Keychain vs settings.json) requires different handling
- `/login` command updates platform storage with fresh tokens automatically

### Seamless Provider Switching

**CCProfileSwitch allows you to switch freely between Claude and Z-AI profiles with a single command.**

When you switch providers, CCProfileSwitch automatically:
- Updates `ANTHROPIC_BASE_URL` for Z-AI profiles
- Removes `ANTHROPIC_BASE_URL` for Claude profiles
- Sets the appropriate `ANTHROPIC_AUTH_TOKEN` for each provider
- Shows a notification when switching between providers

#### Workflow

```bash
# Create profiles for each provider
claude-profile save work --provider claude         # Claude profile
claude-profile save zai-work --provider zai        # Z-AI profile

# Switch freely between any profiles
claude-profile switch work          # Switch to Claude
claude-profile switch zai-work      # Switch to Z-AI
claude-profile switch personal      # Switch to another Claude profile

# Provider switches are seamless
# Switching from ZAI to CLAUDE
# ✔ Switched to profile 'work'
```

CCProfileSwitch handles all API endpoint configuration automatically. Just restart Claude Code after switching to load the new configuration.

### Z-AI GLM-4.6 Coder Integration

CCProfileSwitch now supports [Z-AI's GLM-4.6 Coder](https://z.ai/subscribe?utm_campaign=Platform_Ops&_channel_track_key=DaprgHIc) subscription, offering **3× the usage at 1/7 the cost** compared to Claude's standard pricing.

#### Quick Setup for Z-AI

```bash
# 1. Get your Z-AI API key
# Visit: https://z.ai/manage-apikey/apikey-list

# 2. Initialize CCProfileSwitch (sets up shell integration automatically)
claude-profile init
# When prompted "Set up shell integration now?", choose Yes

# 3. Reload your shell
source ~/.zshrc  # or source ~/.bashrc

# 4. Create Z-AI profile
claude-profile save zai-glm46 --provider zai --token your-zai-api-key

# 5. Switch to Z-AI (automatically sets environment variables)
cpswitch zai-glm46

# 6. Start Claude Code
claude

# 7. Verify you're using Z-AI (should show GLM-4.6 Coder)
```

**Important:** Z-AI requires shell environment variables. The `claude-profile init` command automatically sets up the `cpswitch` function. If you skipped this step, run `claude-profile doctor` to set it up later.

#### What Happens Behind the Scenes

When you switch to a Z-AI profile using `cpswitch`, CCProfileSwitch:
1. Retrieves your Z-AI API key from system keyring
2. Exports shell environment variables:
   ```bash
   export ANTHROPIC_BASE_URL="https://api.z.ai/api/anthropic"
   export ANTHROPIC_AUTH_TOKEN="your-zai-api-key"
   export ANTHROPIC_DEFAULT_SONNET_MODEL="glm-4.6"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="glm-4.6"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-4.5-air"
   unset ANTHROPIC_API_KEY  # Prevents OAuth conflicts
   ```
3. Claude Code reads these environment variables at startup and routes requests to Z-AI's API
4. Z-AI automatically maps Claude model names to GLM models

**Why `cpswitch` for Z-AI?** The `cpswitch` function provides Z-AI integration by:
- Setting `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` environment variables
- Setting model mappings so Claude Code uses GLM-4.6 instead of Sonnet
- **Unsetting `ANTHROPIC_API_KEY`** to prevent OAuth conflicts
- Claude Code launched from the same shell inherits these variables

**Note:** CCProfileSwitch does NOT write to `~/.claude/settings.json`. Z-AI works entirely through shell environment variables.

#### Switching Back to Claude from Z-AI

To switch from Z-AI back to your Claude subscription (or another Claude profile):

```bash
# Method 1: Use the cpreset helper (recommended)
cpreset  # Unsets all Z-AI environment variables
claude   # Uses your active Claude OAuth (from /login or last profile switch)

# Method 2: Switch to a specific Claude profile
cpreset  # Clear Z-AI config first
claude-profile switch work  # Switch to 'work' Claude profile
claude

# Method 3: Manual unset
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN ANTHROPIC_BASE_URL
unset ANTHROPIC_DEFAULT_SONNET_MODEL ANTHROPIC_DEFAULT_OPUS_MODEL ANTHROPIC_DEFAULT_HAIKU_MODEL
claude
```

The `cpreset` command clears Z-AI configuration. After that, Claude Code uses whichever Claude OAuth profile is active (managed by CCProfileSwitch or via `/login`).

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

### Shell Integration (Required for Z-AI)

**For Claude subscription:** Use `/login` in Claude Code - no profile switching needed.

**For Z-AI profiles:** Shell integration is **required** - the `cpswitch` command sets environment variables that Claude Code reads at startup.

#### Automated Setup (Recommended)

During `claude-profile init`, CCProfileSwitch will offer to set up shell integration automatically:

```bash
claude-profile init

# Will prompt:
# Set up shell integration now? [Y/n]: y
# ✓ Shell integration added to /Users/you/.zshrc
# Run 'source ~/.zshrc' or restart your terminal to activate
```

This adds two commands:

**`cpswitch <profile>`** - Switch to a Z-AI profile:
- Runs `claude-profile switch <name> --eval` internally
- Automatically sets `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` in your current shell
- For Z-AI profiles: Sets model mappings (`ANTHROPIC_DEFAULT_*_MODEL` → `glm-4.6`)
- **Unsets `ANTHROPIC_API_KEY`** to prevent conflicts
- Shows confirmation of what was set

**`cpreset`** - Clear Z-AI configuration:
- Unsets all `ANTHROPIC_*` environment variables
- Claude Code will use active Claude OAuth profile (managed by CCProfileSwitch or `/login`)

#### Manual Setup (If needed)

```bash
# Add to ~/.zshrc or ~/.bashrc
source /path/to/CCProfileSwitch/shell-integration.sh

# Or check setup status anytime
claude-profile doctor
```

#### Option 2: Run export commands manually

```bash
# Switch profile first
claude-profile switch zai-real

# Then run the export commands shown in the output:
export ANTHROPIC_BASE_URL="https://api.z.ai/api/anthropic"
export ANTHROPIC_AUTH_TOKEN="your-zai-api-key"

# Finally, start Claude Code
claude
```

**Why shell environment variables?** Claude Code reads `ANTHROPIC_BASE_URL` from the process environment at startup. Setting it in `settings.json` is not sufficient - it must be an environment variable in the shell where you launch Claude Code.

## Usage Guide

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

## Complete CLI Reference

### Global Options

| Option | Description |
|--------|-------------|
| `--help` | Show help message |
| `--install-completion` | Install shell completion |

### Profile Management Commands

#### `claude-profile init`
Initialize profile manager with guided setup

```bash
claude-profile init
```

Sets up credential storage location, imports existing tokens if found, and creates your first profile interactively.

---

#### `claude-profile save <name>`
Save a new profile

```bash
claude-profile save work
claude-profile save personal --description "Personal projects"
claude-profile save zai-work --provider zai
```

Options:
- `--token, -t` - Provide token directly (will prompt if not provided)
- `--description, -d` - Profile description
- `--provider, -p` - Provider: `claude` or `zai` (default: claude)
- `--api-url` - Custom API URL (defaults to Z-AI for zai provider)
- `--active/--no-active` - Set as active after saving (default: true)
- `--overwrite/--no-overwrite` - Overwrite existing profile

---

#### `claude-profile switch [name]`
Switch to a different profile

```bash
claude-profile switch work          # Switch to specific profile
claude-profile switch               # Interactive selection menu
claude-profile switch --fzf         # Use fzf for selection (if installed)
```

Options:
- `--show-tokens` - Show tokens in selection list
- `--fzf/--no-fzf` - Use fzf for interactive selection
- `--eval` - Output pure shell export commands (used by cpswitch function)

**For Z-AI profiles:** Use the `cpswitch` function instead of running `claude-profile switch` directly. The `cpswitch` function uses the `--eval` flag internally to set environment variables automatically.

---

#### `claude-profile list`
List all saved profiles grouped by provider

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

#### `claude-profile current`
Show currently active provider configuration

```bash
claude-profile current
```

Displays active profile name, provider, description, creation date, and masked token.

---

#### `claude-profile cycle`
Cycle through available profiles

```bash
claude-profile cycle
```

Activates the next profile in alphabetical order. Useful for quick switching between known profiles.

---

#### `claude-profile delete <name>`
Delete a profile

```bash
claude-profile delete old-profile
claude-profile delete old-profile --no-confirm
```

Options:
- `--confirm/--no-confirm` - Skip confirmation prompt

---

#### `claude-profile rename <old> <new>`
Rename a profile

```bash
claude-profile rename personal personal-projects
```

---

#### `claude-profile show <name>`
Show profile details

```bash
claude-profile show work
claude-profile show work --show-token
```

Options:
- `--show-token` - Show full token (masked by default)

### Backup and Import Commands

#### `claude-profile export [file]`
Export profiles to backup file

```bash
claude-profile export backup.json
claude-profile export backup.json --include-tokens    # Include plaintext tokens
claude-profile export backup.yaml --export-format yaml
```

Options:
- `--include-tokens` - Include actual tokens (use with caution)
- `--export-format` - Format: `json` or `yaml`

**Security Warning:** Exported files with `--include-tokens` contain plaintext tokens. Encrypt immediately:

```bash
# Export with tokens
$ claude-profile export backup.json --include-tokens

# Encrypt immediately
$ gpg -c backup.json
$ rm backup.json  # Delete plaintext

# Later: decrypt and import
$ gpg -d backup.json.gpg | claude-profile import-profiles /dev/stdin
```

---

#### `claude-profile import-profiles <file>`
Import profiles from backup

```bash
claude-profile import-profiles backup.json
claude-profile import-profiles backup.json --prefix work-
claude-profile import-profiles backup.json --replace
```

Options:
- `--merge` - Merge with existing profiles (default)
- `--replace` - Replace all existing profiles
- `--prefix` - Add prefix to imported profile names

### Diagnostics

#### `claude-profile doctor`
System diagnostics

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

## Advanced Topics

### Security

CCProfileSwitch stores authentication credentials in your operating system's secure credential storage with platform-specific optimizations.

#### Credential Storage by Platform

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

#### Auto-Detection and OAuth Support

- Automatically detects existing Claude Code credentials on first run
- **All Platforms**: Reads complete OAuth structure, including:
  - `accessToken` (sk-ant-oat*) - Active authentication token
  - `refreshToken` (sk-ant-ort*) - Token refresh capability
  - `expiresAt`, `scopes`, `subscriptionType` - Session metadata
  - `mcpOAuth` - MCP server authentication tokens
- **macOS**: Reads from Keychain service `Claude Code-credentials`
- **Linux/Windows**: Reads from credential files (`~/.claude/.credentials.json`, etc.)
- Supports both OAuth tokens and API keys (sk-ant-api*)

#### What's Protected

- **All credentials encrypted** in system-native credential storage
- Concurrent access protected by file locking (5-second timeout)
- Token format validation enforces `sk-ant-*` pattern
- Atomic writes prevent partial credential updates
- **All Platforms**: Complete OAuth structure preserved (never loses refresh tokens or MCP auth)

#### What's Not Protected

- **macOS**: All credentials stay in Keychain (maximum security - no plaintext files)
- **Linux/Windows**: Active credential file contains plaintext OAuth JSON for Claude Code compatibility (0600 permissions)
- Exported backups with `--include-tokens` flag contain plaintext tokens (user must encrypt)

For shared or multi-user systems, verify security with `claude-profile doctor`. Each user's credential storage is isolated.

### Configuration

CCProfileSwitch requires minimal configuration. The tool automatically detects your system's keyring and creates necessary directories.

#### Storage Locations

| Platform | Profile Storage | Active Session | OAuth Support |
|----------|----------------|----------------|---------------|
| **macOS** | System Keyring (`claude-profile-manager`) | Keychain (`Claude Code-credentials`) | Full OAuth (tested) |
| **Windows** | Credential Manager (DPAPI) | `AppData/Roaming/Claude/.credentials.json` | Full OAuth (untested) |
| **Linux** | Secret Service (libsecret) | `~/.claude/.credentials.json` | Full OAuth (untested) |

> **Testing Status**: macOS OAuth support has been verified. Windows/Linux implementations are complete but await real-world testing.

#### macOS Architecture Details

- Profiles: System Keyring stores `{"token": "{OAuth JSON}", "metadata": {...}}`
- Active: Keychain stores raw OAuth JSON via `security add-generic-password`
- Result: No credential files on disk, complete OAuth preservation

#### Environment Variables

```bash
# Disable colors and animations (accessibility)
export NO_COLOR=1
export CCPS_NO_COLOR=1

# Force ASCII icons (no Unicode)
export CCPS_ASCII=1

# Override credential file location (advanced)
export CLAUDE_CREDENTIALS_PATH=~/.config/claude/credentials.json

# Force file-based storage instead of Keychain (testing only)
export CCPS_FORCE_FILE_STORAGE=1
```

#### Keyring Backends

CCProfileSwitch uses the `keyring` library, which automatically selects the appropriate backend. Check your backend with:

```bash
$ claude-profile doctor
Keyring Check:
✓ Keyring accessible: keyring.backends.macOS.Keychain
```

If no secure backend is available (rare), the tool will warn and suggest installing a keyring provider for your system.

### Troubleshooting

#### Keychain authorization prompts (macOS)

If you're repeatedly prompted to authorize keychain access, you can grant permanent access:

```bash
# Run doctor to see instructions
claude-profile doctor

# Manual steps:
# 1. Open 'Keychain Access' app
# 2. Search for 'Claude Code-credentials' and 'claude-profile-manager'
# 3. Double-click each entry → Access Control tab
# 4. Select 'Allow all applications to access this item'
# 5. Or add your terminal app to allowed apps
```

**Note:** After first authorization, the keyring library minimizes prompts automatically. Permanent access setup is optional but recommended for smoother experience.

#### No secure keyring backend available

```bash
# Linux: Install keyring backend
sudo apt-get install gnome-keyring  # GNOME
sudo apt-get install kwalletmanager # KDE

# Verify
claude-profile doctor
```

#### KeyringLocked error

- **macOS**: Unlock Keychain in System Preferences → Passwords
- **Linux**: Keyring usually unlocks automatically on login

#### Permission issues

```bash
# Check permissions
ls -la ~/.claude/.credentials.json

# Fix if needed
chmod 600 ~/.claude/.credentials.json

# Run diagnostic
claude-profile doctor
```

#### Profile not switching

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

#### OAuth token expired

```bash
# Switch to profile
claude-profile switch work

# If you see expiration warning, restart Claude Code and run /login
# This refreshes the OAuth token in Keychain/settings.json
```

#### 401 error after switching from API Usage to Claude subscription

If you switch from an API key profile (API Usage Billing) to a Claude subscription profile (OAuth) and get a 401 authentication error after running `/login`, you may need to explicitly sign out first:

```bash
# In Claude Code, sign out completely
> /logout
Successfully logged out from your Anthropic account.

# Then login again with your subscription account
> /login
Login successful

# Now switching between subscription profiles should work
claude-profile switch your-subscription-profile
```

**Why this happens**: Claude Code may cache authentication state from your API key session. Explicitly logging out clears this state before authenticating with OAuth.

#### Switching between providers

CCProfileSwitch handles both Claude OAuth profiles and Z-AI API key profiles:

```bash
# Switching between Claude profiles (OAuth)
claude-profile switch personal  # Switch to personal Claude account
claude-profile switch work      # Switch to work Claude account

# Switching to Z-AI (use cpswitch for environment variables)
source ~/CCProfileSwitch/shell-integration.sh
cpswitch zai-profile
claude  # Launch from same shell

# Switching back from Z-AI to Claude
cpreset  # Clears Z-AI env vars
claude-profile switch work  # Optional: switch to specific Claude profile
claude   # Uses Claude OAuth (from profile switch or /login)
```

**Claude profiles:** Managed via OAuth tokens stored in CCProfileSwitch's secure keyring. Use `claude-profile switch`.
**Z-AI profiles:** Managed via API keys exported as environment variables. Use `cpswitch`.
**Switching from Z-AI to Claude:** Use `cpreset` to clear Z-AI environment variables.

#### Z-AI Integration Not Working

If Claude Code still identifies as "Claude" instead of connecting to Z-AI after switching profiles:

**1. Verify environment configuration:**
```bash
# Run comprehensive diagnostics
claude-profile doctor

# Check environment variables in your shell
echo $ANTHROPIC_BASE_URL    # Should show Z-AI URL
echo $ANTHROPIC_AUTH_TOKEN  # Should show your token
echo $ANTHROPIC_DEFAULT_SONNET_MODEL  # Should show glm-4.6
```

**2. Common causes and solutions:**

| Issue | Cause | Solution |
|-------|-------|----------|
| **`ANTHROPIC_API_KEY` conflict** | **OAuth token from `/login` overrides Z-AI config** | **Use `cpswitch` (automatically unsets it) before launching Claude Code** |
| **Model still shows Sonnet** | **Model mappings not set** | **Use `cpswitch` (sets `ANTHROPIC_DEFAULT_*_MODEL` env vars)** |
| Claude Code launched from desktop | Desktop launchers don't inherit shell env vars | Launch Claude Code from terminal: `claude` |
| Didn't use `cpswitch` | Environment variables not set | Use `cpswitch <profile>` instead of `claude-profile switch` |
| Wrong provider flag | Profile saved as Claude instead of Z-AI | Check with `claude-profile show <name>`, re-save with `--provider zai` |

**3. Manual verification:**
```bash
# Check environment variables (NOT settings.json)
echo $ANTHROPIC_BASE_URL    # Should show: https://api.z.ai/api/anthropic
echo $ANTHROPIC_AUTH_TOKEN  # Should show your Z-AI key
echo $ANTHROPIC_API_KEY     # Should be EMPTY
echo $ANTHROPIC_DEFAULT_SONNET_MODEL  # Should show: glm-4.6

# Verify in Claude Code with /status
# Auth token: ANTHROPIC_AUTH_TOKEN
# Anthropic base URL: https://api.z.ai/api/anthropic
# Model: Default (glm-4.6)
```

**4. Verify the profile was saved correctly:**
```bash
# Show profile details
claude-profile show <your-zai-profile-name>

# Should display:
# Provider: ZAI
# API URL: https://api.z.ai/api/anthropic
```

**Recent bug fixes (if you installed before 2025-01-07):**
- **Bug #1**: validate_token tuple unpacking - prevented Z-AI tokens from being saved
- **Bug #2**: rename lost provider metadata - Z-AI profiles became Claude profiles after renaming
- **Bug #3**: cycle didn't update settings.json - **CRITICAL** for Z-AI, ANTHROPIC_BASE_URL never got set
- **Solution**: Update to latest version: `cd CCProfileSwitch && git pull && pipx reinstall .`

If issues persist after verification, the `claude-profile doctor` command now includes detailed Z-AI diagnostics to help pinpoint the exact problem.

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
