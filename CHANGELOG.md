# Changelog

All notable changes to CCProfileSwitch will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-01-10

### Added
- **Z-AI GLM-4.6 Coder Integration**: Full support for Z-AI as an alternative provider
  - New `--provider` flag for `save` command (claude|zai)
  - Auto-detection of Z-AI tokens from `ZAI_API_KEY` environment variable
  - Z-AI API URL configuration (`https://api.z.ai/api/anthropic`)
- **Provider Isolation**: Prevents accidental switching between Claude and Z-AI profiles
  - Clear error messages when attempting cross-provider switches
  - Helpful guidance for managing multiple providers
- **Settings File Management**: Direct `~/.claude/settings.json` integration
  - Atomic updates to Claude Code settings
  - Automatic environment variable management (ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN)
  - Malformed settings backup and recovery
- **Enhanced CLI Commands**:
  - `list`: Groups profiles by provider with separate sections
  - `current`: Shows active provider, API URL, and configuration status
  - `show`: Displays provider and API URL information
  - Provider-aware validation with specific error messages
- **Provider Constants**: Centralized provider definitions in `constants.py`
- **Utility Functions**:
  - `detect_zai_token()`: Auto-detect Z-AI API keys from environment
  - `detect_current_provider()`: Infer provider from settings.json
  - `validate_token()`: Provider-specific token validation

### Changed
- **Profile Data Model**: Added `provider` and `api_url` fields (backward compatible)
  - Legacy profiles automatically normalized to provider="claude"
  - No migration required for existing users
- **Token Validation**: Now returns tuple `(bool, str)` for detailed error messages
- **CLI Messages**: Consistent provider and API URL display across commands
- **README**: Complete rewrite with Z-AI integration guide and provider isolation explanation

### Security
- API keys stored in system keyring (unchanged)
- Settings.json written atomically to prevent corruption
- Token validation prevents obvious invalid formats
- Automatic backup of malformed settings.json

### Deprecated
- None

### Removed
- None

### Fixed
- Settings.json handling now more robust with error recovery

## [0.1.0] - 2024-12-XX

### Added
- Initial release
- Claude profile management with system keyring storage
- Cross-platform support (macOS, Windows, Linux)
- OAuth token preservation
- Profile save/switch/list/delete operations
- Secure credential storage
- Rich terminal UI

[0.2.0]: https://github.com/biostochastics/CCProfileSwitch/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/biostochastics/CCProfileSwitch/releases/tag/v0.1.0
