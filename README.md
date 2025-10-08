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

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/biostochastics/CCProfileSwitch) [![Python](https://img.shields.io/badge/python-3.8.1%2B-blue)](https://www.python.org/downloads/) [![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![pipx](https://img.shields.io/badge/install-pipx-brightgreen)](https://pipx.pypa.io/)

---

## ⚠️ **Critical Caveats**

```
┌────────────────────────────────────────────────────────────────────┐
│ 🚨 YOU MUST RESTART CLAUDE CODE after every profile switch        │
│ 🚨 Z-AI requires shell integration (cpswitch command)             │
│ 🚨 macOS uses Keychain (no files), Linux/Windows use files       │
│ 🚨 OAuth tokens expire ~1hr, API keys don't expire               │
│ 🚨 Claude Code reads: Keychain > settings.json > shell env vars  │
└────────────────────────────────────────────────────────────────────┘
```

---

## Overview

CCProfileSwitch manages complete authentication profiles in your OS's secure storage and switches contexts with a single command. Eliminates manual re-authentication and prevents context slips across personal/professional projects.

**Core functionality:**
- **Secure Storage**: System keyring (Keychain/Credential Manager/Secret Service)
- **Profile Switching**: One command to switch, restart Claude Code to apply
- **Multi-Provider**: Claude (OAuth) and Z-AI (API keys) with isolated configs
- **OAuth Preservation**: Maintains refresh tokens and MCP server auth
- **Cross-Platform**: macOS (tested), Linux/Windows (implemented)

---

## Quick Start

```bash
# Install globally
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
pipx install .

# Initialize (auto-detects current token, sets up shell integration)
claude-profile init

# Save profiles
claude-profile save work --token sk-ant-...
claude-profile save zai --provider zai --token your-zai-key

# Switch profiles (then restart Claude Code)
claude-profile switch work
```

For Z-AI: Use `cpswitch zai` (sets environment variables automatically).

---

## Platform Architecture

| Platform | Profile Storage | Active Session | Auth Method | Status |
|----------|----------------|----------------|-------------|--------|
| **macOS** | Keychain (`claude-profile-manager`) | Keychain (`Claude Code-credentials`) | OAuth + API keys | ✅ Tested |
| **Linux** | Secret Service (GNOME Keyring) | `~/.claude/.credentials.json` | OAuth + API keys | ⚠️ Untested |
| **Windows** | Credential Manager (DPAPI) | `AppData/Roaming/Claude/.credentials.json` | OAuth + API keys | ⚠️ Untested |

**macOS Advantage**: No credential files on disk—everything in Keychain with AES-128 encryption.

**OAuth Structure Preserved** (all platforms):
- `accessToken` (sk-ant-oat*), `refreshToken` (sk-ant-ort*)
- `expiresAt`, `scopes`, `subscriptionType`
- `mcpOAuth` (MCP server authentication)

---

## Authentication: OAuth vs API Keys

| Type | Format | Expiration | Refresh | Provider | Setup |
|------|--------|------------|---------|----------|-------|
| **OAuth** | `sk-ant-oat*` | ~1 hour | Auto via `/login` | Claude subscription | Use `/login` in Claude Code |
| **API Keys** | `sk-ant-api*` | Never | N/A | Claude API Usage | Save with `--token` |
| **Z-AI Keys** | Custom format | Never | N/A | Z-AI subscription | Save with `--provider zai` |

**OAuth Workflow:**
1. Switch to OAuth profile: `claude-profile switch work`
2. Restart Claude Code
3. If expired (401 error), run `/login` in Claude Code
4. CCProfileSwitch preserves the refreshed OAuth automatically

**Z-AI Workflow:**
1. Setup once: `claude-profile init` (enables `cpswitch` command)
2. Switch: `cpswitch zai-profile`
3. Start Claude Code from same terminal
4. No `/login` needed—API key never expires

---

## Z-AI GLM-4.6 Integration

**Value Proposition**: 3× usage at 1/7 cost vs Claude standard pricing.

### Setup (One-Time)

```bash
# 1. Get Z-AI API key from: https://z.ai/manage-apikey/apikey-list

# 2. Initialize shell integration
claude-profile init
# Choose "Yes" for shell integration setup
source ~/.zshrc  # or ~/.bashrc

# 3. Save Z-AI profile
claude-profile save zai-glm46 --provider zai --token <your-z-ai-key>

# 4. Switch and start
cpswitch zai-glm46
claude
```

### What `cpswitch` Does

```bash
export ANTHROPIC_BASE_URL="https://api.z.ai/api/anthropic"
export ANTHROPIC_AUTH_TOKEN="<your-z-ai-key>"
export ANTHROPIC_DEFAULT_SONNET_MODEL="glm-4.6"
export ANTHROPIC_DEFAULT_OPUS_MODEL="glm-4.6"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-4.5-air"
unset ANTHROPIC_API_KEY  # Prevents OAuth conflicts
```

Claude Code inherits these variables when launched from the same terminal.

### Switching Back to Claude

```bash
cpreset  # Clears Z-AI env vars
claude   # Uses active Claude OAuth profile
```

**Manual Setup** (if you skipped `init`):
```bash
# Add to ~/.zshrc or ~/.bashrc:
source /path/to/CCProfileSwitch/shell-integration.sh
```

---

## CLI Reference

### Essential Commands

| Command | Usage | Description |
|---------|-------|-------------|
| **init** | `claude-profile init` | Setup wizard (auto-imports current token, configures shell) |
| **save** | `claude-profile save <name> [--token TOKEN] [--provider claude\|zai]` | Save new profile |
| **switch** | `claude-profile switch <name>` | Switch profile (restart Claude Code after) |
| **cpswitch** | `cpswitch <name>` | Switch Z-AI profile (sets env vars) |
| **list** | `claude-profile list [--show-tokens]` | List all profiles by provider |
| **current** | `claude-profile current` | Show active profile |
| **cycle** | `claude-profile cycle` | Rotate to next profile |
| **show** | `claude-profile show <name> [--show-token]` | Profile details |
| **delete** | `claude-profile delete <name> [--no-confirm]` | Delete profile |
| **rename** | `claude-profile rename <old> <new>` | Rename profile |
| **export** | `claude-profile export <file> [--include-tokens]` | Backup profiles |
| **import** | `claude-profile import-profiles <file> [--prefix PREFIX]` | Restore profiles |
| **doctor** | `claude-profile doctor` | System diagnostics |
| **cpreset** | `cpreset` | Clear Z-AI env vars |

### Save Command Options

```bash
# Auto-detect token from active session
claude-profile save myprofile

# Explicit token
claude-profile save work --token sk-ant-...

# Z-AI profile
claude-profile save zai-work --provider zai --token <z-ai-key>

# With description
claude-profile save client-a --description "Client A projects"

# Don't auto-activate
claude-profile save personal --no-active
```

### Export/Import (Backup)

```bash
# Export without tokens (safe to share)
claude-profile export backup.json

# Export with tokens (ENCRYPT IMMEDIATELY)
claude-profile export backup.json --include-tokens
gpg -c backup.json && rm backup.json

# Import
claude-profile import-profiles backup.json --prefix imported-
```

---

## Common Workflows

### Daily Context Switching

```bash
# Morning: Work context
claude-profile switch work
# Restart Claude Code → work credentials active

# Afternoon: Personal projects
claude-profile switch personal
# Restart Claude Code → personal credentials active
```

### Managing Multiple Clients

```bash
# Save client profiles
claude-profile save client-a --token sk-ant-...
claude-profile save client-b --token sk-ant-...
claude-profile save internal --token sk-ant-...

# Quick switch with fzf (if installed)
claude-profile switch --fzf

# Or numbered selection
claude-profile switch
# Shows interactive menu with numbers
```

### Claude ↔ Z-AI Switching

```bash
# Start with Claude
claude-profile switch work
# Restart Claude Code

# Switch to Z-AI for cost savings
cpswitch zai-glm46
# Restart Claude Code

# Back to Claude
cpreset
claude-profile switch work  # optional: specific profile
# Restart Claude Code
```

---

## Troubleshooting

### Z-AI Not Working (Still Shows "Claude")

**Checklist:**
```bash
# 1. Verify environment
echo $ANTHROPIC_BASE_URL     # Should show https://api.z.ai/api/anthropic
echo $ANTHROPIC_AUTH_TOKEN   # Should show your Z-AI key
echo $ANTHROPIC_API_KEY      # Should be EMPTY

# 2. Verify profile is Z-AI
claude-profile show zai-profile
# Provider: ZAI ✓

# 3. Use cpswitch (not claude-profile switch)
cpswitch zai-profile  # Sets env vars automatically

# 4. Start Claude Code from SAME terminal
claude

# 5. Check in Claude Code
/status
# Should show: Auth token: ANTHROPIC_AUTH_TOKEN
#              Anthropic base URL: https://api.z.ai/api/anthropic
```

**Common Mistakes:**
- Started Claude Code from desktop (doesn't inherit shell env vars)
- Used `claude-profile switch` instead of `cpswitch` for Z-AI
- Didn't run `claude-profile init` to set up shell integration
- `ANTHROPIC_API_KEY` is set (conflicts with Z-AI)

### OAuth Token Expired (401 Error)

```bash
# Switch shows expiration warning
claude-profile switch work
# ⚠ OAuth token expired 120 minutes ago

# Restart Claude Code, then run /login
claude
> /login
# OAuth refreshes automatically
```

### Profile Not Switching

```bash
# Verify profile exists
claude-profile list

# Verify current profile
claude-profile current

# Force switch
claude-profile switch <name>

# Restart Claude Code (required!)

# Diagnostics
claude-profile doctor
```

### macOS Keychain Authorization Prompts

**One-time setup** to avoid repeated prompts:
1. Open Keychain Access app
2. Search "Claude Code-credentials" and "claude-profile-manager"
3. Double-click each → Access Control tab
4. Select "Allow all applications"

Or add your terminal app (Terminal.app/iTerm2) to allowed apps.

### Permission Issues (Linux/Windows)

```bash
# Check file permissions
ls -la ~/.claude/.credentials.json
# Should show: -rw------- (0600)

# Fix if needed
chmod 600 ~/.claude/.credentials.json

# Verify
claude-profile doctor
```

### No Keyring Backend Available (Linux)

```bash
# Install backend
sudo apt-get install gnome-keyring  # GNOME
sudo apt-get install kwalletmanager # KDE

# Verify
claude-profile doctor
```

---

## Security

**Credential Protection:**
- ✅ All credentials encrypted in OS-native storage
- ✅ File locks prevent concurrent access corruption
- ✅ Atomic writes prevent partial updates
- ✅ macOS: No credential files on disk (Keychain only)
- ✅ Linux/Windows: Credential files with 0600 permissions
- ⚠️ Exports with `--include-tokens` contain plaintext (user must encrypt)

**OAuth Preservation:**
- All platforms preserve complete OAuth structure
- Never loses refresh tokens or MCP auth
- Platform-specific optimizations (Keychain vs files)

**Verification:**
```bash
claude-profile doctor  # System-wide security check
```

---

## Installation

### Production (pipx - Recommended)

```bash
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
pipx install .
claude-profile --help
```

### Development (Poetry)

```bash
git clone https://github.com/biostochastics/CCProfileSwitch.git
cd CCProfileSwitch
poetry install
poetry shell
claude-profile --help
```

### Shell Alias (Alternative)

```bash
# Add to ~/.zshrc or ~/.bashrc:
alias claude-profile='poetry -C /path/to/CCProfileSwitch run claude-profile'
```

---

## Development

```bash
# Setup
poetry install
poetry shell

# Testing
pytest                                           # All tests
pytest --cov=cc_profile_switch --cov-report=term-missing  # With coverage
pytest tests/test_cli.py -xvs                   # Specific test

# Code Quality
black cc_profile_switch tests        # Format
isort cc_profile_switch tests        # Sort imports
flake8 cc_profile_switch             # Lint
mypy cc_profile_switch               # Type check
```

**Contributing**: PRs welcome! Ensure tests pass, code formatted (black/isort), type hints complete, docs updated.

---

## Configuration

### Environment Variables

```bash
# Accessibility
export NO_COLOR=1                    # Disable colors/animations
export CCPS_NO_COLOR=1
export CCPS_ASCII=1                  # Force ASCII icons

# Advanced
export CLAUDE_CREDENTIALS_PATH=~/.config/claude/credentials.json  # Override path
export CCPS_FORCE_FILE_STORAGE=1    # Force file storage (testing only)
```

### Keyring Backend Check

```bash
claude-profile doctor
# Keyring Check:
# ✓ Keyring accessible: keyring.backends.macOS.Keychain
```

---

## Built With

- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [Keyring](https://github.com/jaraco/keyring) - Secure credential storage
- [FileLock](https://github.com/tox-dev/filelock) - Concurrent access protection
- [PlatformDirs](https://github.com/platformdirs/platformdirs) - Cross-platform paths
- [Poetry](https://python-poetry.org/) - Dependency management

---

## License & Contact

**License**: MIT - see [LICENSE](LICENSE)

**Links**:
- **Issues**: https://github.com/biostochastics/CCProfileSwitch/issues
- **Repository**: https://github.com/biostochastics/CCProfileSwitch
- **Documentation**: https://deepwiki.com/biostochastics/CCProfileSwitch

---

*Part of the Biostochastics collection of developer tools*
