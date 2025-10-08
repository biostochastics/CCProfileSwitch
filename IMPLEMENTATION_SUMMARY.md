# Z-AI GLM-4.6 Coder Integration - Implementation Summary

## Completed ✅

### Core Infrastructure
1. **Constants Module** (`cc_profile_switch/constants.py`)
   - Provider constants: `PROVIDER_CLAUDE`, `PROVIDER_ZAI`
   - API URLs: `ZAI_DEFAULT_API_URL`
   - Environment variable keys

2. **Storage Layer** (`cc_profile_switch/storage.py`)
   - Added `provider` and `api_url` fields to profiles
   - Implemented `_normalize_profile()` for backward compatibility
   - Updated `save_profile()` signature with provider support
   - All legacy profiles automatically normalized to `provider="claude"`

3. **Configuration Management** (`cc_profile_switch/config.py`)
   - Implemented `get_claude_settings_path()` 
   - Added `get_claude_settings_env()` to read settings.json
   - Created `update_claude_settings()` with atomic writes
   - Handles malformed settings.json with automatic backup

4. **Utility Functions** (`cc_profile_switch/utils.py`)
   - Provider-aware `validate_token()` returning `(bool, str)` tuple
   - `detect_zai_token()` reads from `ZAI_API_KEY` env var
   - `detect_current_provider()` infers provider from settings.json
   - Validation rules:
     - Claude: must start with `sk-`, length ≥ 20, no whitespace
     - Z-AI: length ≥ 20, no whitespace (permissive)

### CLI Commands

5. **save Command** (`cc_profile_switch/cli.py`)
   - Added `--provider` flag (claude|zai, default: claude)
   - Added `--api-url` flag for custom URLs
   - Auto-detects Z-AI tokens from `ZAI_API_KEY` environment variable
   - Validates tokens using provider-specific rules
   - Updates `~/.claude/settings.json` when `--active` flag is used
   - Shows provider and API URL after saving

6. **switch Command** (`cc_profile_switch/cli.py`)
   - **CRITICAL**: Enforces provider isolation
   - Blocks switching between Claude ↔ Z-AI profiles
   - Detects current provider from settings.json
   - Updates settings.json appropriately:
     - Z-AI: Sets `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`
     - Claude: Sets `ANTHROPIC_AUTH_TOKEN`, removes `ANTHROPIC_BASE_URL`
   - Clear error messages when attempting cross-provider switch

### Documentation

7. **README.md**
   - Added "What CCProfileSwitch Does" section (2 core tasks)
   - Comprehensive Z-AI GLM-4.6 Coder Integration section
   - Quick setup guide with examples
   - Provider isolation explanation
   - Behind-the-scenes technical details
   - Updated version to 0.2.0

## Remaining Tasks 📋

### High Priority
- [ ] **list command**: Group profiles by provider with sections
- [ ] **current command**: Show active provider with helpful guidance
- [ ] **show command**: Include provider details
- [ ] **doctor command**: Validate Z-AI/Claude setups, network checks

### Medium Priority  
- [ ] **init command**: Update to handle provider detection
- [ ] **Tests**: Unit tests for new functionality
- [ ] **Manual QA**: Test on macOS with real Z-AI subscription

### Low Priority
- [ ] **cycle command**: Update for provider awareness
- [ ] **Version bump**: Update pyproject.toml to 0.2.0
- [ ] **CHANGELOG**: Document all changes

## Key Design Decisions

### 1. Provider Isolation
**Decision**: Profiles cannot switch between Claude and Z-AI.

**Rationale**:
- Different API endpoints require different configurations
- Prevents authentication errors from mixed credentials
- Clear mental model: one provider at a time
- Tool positioning: simple credential + settings management

### 2. Settings File Approach
**Decision**: Use `~/.claude/settings.json` instead of shell rc files.

**Rationale**:
- Claude Code reads settings.json natively
- No shell-specific logic needed
- Works across zsh, bash, fish without modification
- Atomic updates prevent corruption
- Clean, predictable behavior

### 3. Backward Compatibility
**Decision**: Legacy profiles without provider field default to "claude".

**Rationale**:
- Existing users see no breaking changes
- Automatic normalization in getters
- No migration script required
- Gradual adoption of provider field

## Testing Strategy

### Unit Tests Needed
- Storage: `_normalize_profile()`, save/get with provider
- Utils: `validate_token()` with various inputs
- Config: `update_claude_settings()` atomic writes
- CLI: Provider detection and validation

### Integration Tests
- Save Z-AI profile with env var auto-detect
- Switch within same provider (success)
- Switch across providers (blocked with clear error)
- Settings.json correctly updated for each provider

### Manual QA Checklist
- [ ] Create Z-AI profile with `ZAI_API_KEY` env var
- [ ] Switch to Z-AI profile
- [ ] Verify `~/.claude/settings.json` has correct keys
- [ ] Launch Claude Code and confirm Z-AI routing
- [ ] Switch back to Claude profile
- [ ] Verify `ANTHROPIC_BASE_URL` removed from settings.json

## Security Considerations

✅ **Implemented**:
- API keys stored in system keyring (not plaintext)
- Settings.json written atomically (no partial writes)
- Token validation prevents obvious invalid formats
- Backup of malformed settings.json before overwrite

⚠️ **Not Protected**:
- settings.json contains plaintext tokens (by design for Claude Code)
- User must secure `~/.claude/` directory with appropriate permissions

## Next Steps

1. **Implement list/current/show commands** with provider display
2. **Add doctor command** with network checks for Z-AI
3. **Write comprehensive tests**
4. **Manual QA** with real Z-AI subscription
5. **Update CHANGELOG** and bump version

## Usage Examples

```bash
# Z-AI Profile Creation
export ZAI_API_KEY="your-zai-key-here"
claude-profile save zai-glm46 --provider zai --description "Z-AI GLM-4.6 Coder"

# Switch to Z-AI
claude-profile switch zai-glm46
# ✓ Switched to profile 'zai-glm46'
#   Provider: ZAI
#   API URL: https://api.z.ai/api/anthropic
#
# Environment updated in ~/.claude/settings.json
#
# Note: Restart Claude Code to use the new configuration

# Attempt cross-provider switch (blocked)
claude-profile switch work  # (work is a Claude profile)
# ✗ Cannot switch between ZAI and CLAUDE profiles!
#
# Provider switching requires reconfiguration:
#   Current provider: ZAI
#   Target provider:  CLAUDE
#
# Different providers use different API endpoints.
# Create a new profile for the target provider instead:
#
#   claude-profile save work_new --provider claude
```

## Files Changed

- `cc_profile_switch/constants.py` (NEW)
- `cc_profile_switch/storage.py` (MODIFIED)
- `cc_profile_switch/config.py` (MODIFIED)
- `cc_profile_switch/utils.py` (MODIFIED)
- `cc_profile_switch/cli.py` (MODIFIED)
- `README.md` (MODIFIED)
- `pyproject.toml` (httpx dependency added)

