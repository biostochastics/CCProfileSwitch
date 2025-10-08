#!/bin/bash
# CCProfileSwitch Shell Integration
# Add this to your ~/.zshrc or ~/.bashrc

# Function to reset to Claude subscription (unset all ANTHROPIC env vars)
cpreset() {
    unset ANTHROPIC_API_KEY
    unset ANTHROPIC_AUTH_TOKEN
    unset ANTHROPIC_BASE_URL
    unset ANTHROPIC_DEFAULT_SONNET_MODEL
    unset ANTHROPIC_DEFAULT_OPUS_MODEL
    unset ANTHROPIC_DEFAULT_HAIKU_MODEL

    echo "✓ Reset to Claude subscription"
    echo "  All ANTHROPIC environment variables cleared"
    echo ""
    echo "Launch Claude Code to use your subscription (via /login OAuth)"
}

# Function to switch Claude profiles and set environment variables
cpswitch() {
    if [ -z "$1" ]; then
        echo "Usage: cpswitch <profile-name>"
        claude-profile list
        return 1
    fi

    # Run claude-profile switch in eval mode and capture output
    local switch_output=$(claude-profile switch "$1" --eval 2>&1)
    local exit_code=$?

    if [ $exit_code -eq 0 ]; then
        # Source the environment variables
        eval "$switch_output"

        # Unset ANTHROPIC_API_KEY to prevent conflicts with Z-AI profiles
        # Claude Code prioritizes ANTHROPIC_API_KEY over settings.json config
        unset ANTHROPIC_API_KEY

        # If Z-AI profile (base URL contains z.ai), set model mappings
        if [[ "$ANTHROPIC_BASE_URL" == *"z.ai"* ]]; then
            export ANTHROPIC_DEFAULT_SONNET_MODEL="glm-4.6"
            export ANTHROPIC_DEFAULT_OPUS_MODEL="glm-4.6"
            export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-4.5-air"
            echo "✓ Switched to Z-AI profile '$1'"
            echo "  ANTHROPIC_BASE_URL: ${ANTHROPIC_BASE_URL}"
            echo "  ANTHROPIC_AUTH_TOKEN: ${ANTHROPIC_AUTH_TOKEN:0:30}..."
            echo "  Models: Sonnet→glm-4.6, Opus→glm-4.6, Haiku→glm-4.5-air"
        else
            echo "✓ Switched to profile '$1'"
            echo "  ANTHROPIC_BASE_URL: ${ANTHROPIC_BASE_URL:-[not set]}"
            echo "  ANTHROPIC_AUTH_TOKEN: ${ANTHROPIC_AUTH_TOKEN:0:30}..."
        fi
        echo ""
        echo "Restart Claude Code to apply changes"
    else
        echo "✗ Failed to switch profile"
        echo "$switch_output"
        return 1
    fi
}

# Autocomplete for cpswitch (optional - only works if completion system is loaded)
if [ -n "$BASH_VERSION" ]; then
    # Bash completion
    _cpswitch_complete() {
        local profiles=$(claude-profile list 2>/dev/null | grep -E '^\s+│\s+[0-9]+\s+│' | awk -F'│' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')
        COMPREPLY=($(compgen -W "${profiles}" -- "${COMP_WORDS[1]}"))
    }
    complete -F _cpswitch_complete cpswitch 2>/dev/null
elif [ -n "$ZSH_VERSION" ]; then
    # Zsh completion (requires compinit to be loaded)
    autoload -Uz compinit 2>/dev/null && compinit -C 2>/dev/null
    _cpswitch_complete() {
        local profiles=(${(f)"$(claude-profile list 2>/dev/null | grep -E '^\s+│\s+[0-9]+\s+│' | awk -F'│' '{gsub(/^[ \t]+|[ \t]+$/, "", $3); print $3}')"})
        _describe 'profile' profiles
    }
    compdef _cpswitch_complete cpswitch 2>/dev/null || true
fi
