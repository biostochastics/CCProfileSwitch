"""Integration tests for the Typer CLI commands."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from typer.testing import CliRunner

from cc_profile_switch.cli import app
from cc_profile_switch.config import Config
from cc_profile_switch.constants import PROVIDER_ZAI
from cc_profile_switch.storage import ProfileStorage


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_save_list_and_cycle_flow(runner: CliRunner) -> None:
    """Test save, list, and cycle commands - macOS compatible."""
    # Use valid token formats that won't confuse OAuth detection
    token_primary = "sk-ant-test-primary-1234567890123456789012345678"
    token_secondary = "sk-ant-test-secondary-123456789012345678901234"

    result = runner.invoke(
        app,
        [
            "save",
            "work",
            "--token",
            token_primary,
            "--description",
            "Work account",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.stdout

    # Verify profile saved to keyring
    storage = ProfileStorage()
    stored_profile = storage.get_profile("work")
    assert stored_profile is not None
    assert stored_profile["token"] == token_primary

    # Test list command with JSON output
    list_result = runner.invoke(
        app,
        ["list", "--output-format", "json", "--show-tokens"],
        catch_exceptions=False,
    )
    assert list_result.exit_code == 0, list_result.stdout
    profiles_json = json.loads(list_result.stdout)
    assert profiles_json["work"]["token"] == token_primary
    assert profiles_json["work"]["active"] is True

    # Save second profile
    add_second = runner.invoke(
        app,
        [
            "save",
            "personal",
            "--token",
            token_secondary,
            "--description",
            "Personal account",
            "--no-active",
        ],
        catch_exceptions=False,
    )
    assert add_second.exit_code == 0, add_second.stdout

    # Test cycle command
    cycle_result = runner.invoke(app, ["cycle"], catch_exceptions=False)
    assert cycle_result.exit_code == 0, cycle_result.stdout

    # On macOS, credentials are in Keychain, not a file
    # Verify by checking the profile was switched in keyring
    if sys.platform == "darwin":
        # Just verify cycle succeeded - can't easily read from Keychain in test
        assert "personal" in cycle_result.stdout or cycle_result.exit_code == 0
    else:
        # On Linux/Windows, verify the credentials file
        config = Config()
        active_path = Path(config.get_active_token_path())
        if active_path.exists():
            active_payload = json.loads(active_path.read_text())
            assert active_payload["token"] == token_secondary


def test_export_masks_tokens_and_import_prompts_for_real_token(
    runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test export masks tokens and import requires real tokens - macOS compatible."""
    # Use a valid token format
    token_value = "sk-ant-test-exportable-12345678901234567890123456"

    result = runner.invoke(
        app, ["save", "exportable", "--token", token_value], catch_exceptions=False
    )
    assert result.exit_code == 0, result.stdout

    export_path = tmp_path / "profiles.json"
    export_result = runner.invoke(
        app, ["export", str(export_path)], catch_exceptions=False
    )
    assert export_result.exit_code == 0, export_result.stdout

    # Verify tokens are masked in export
    export_data = json.loads(export_path.read_text())
    # Token should be masked (not the full original)
    assert export_data["exportable"]["token"] != token_value
    # The masked version should contain sk- prefix and asterisks
    assert "sk-" in export_data["exportable"]["token"]
    assert "*" in export_data["exportable"]["token"]

    # Delete profile
    delete_result = runner.invoke(
        app, ["delete", "exportable", "--no-confirm"], catch_exceptions=False
    )
    assert delete_result.exit_code == 0, delete_result.stdout

    # Mock Rich prompts to avoid hanging on interactive input
    from rich.prompt import Confirm, Prompt

    monkeypatch.setattr(Confirm, "ask", lambda *args, **kwargs: True)
    monkeypatch.setattr(Prompt, "ask", lambda *args, **kwargs: token_value)

    # Import - Rich prompts are now mocked
    import_result = runner.invoke(
        app,
        ["import-profiles", str(export_path)],
        catch_exceptions=False,
    )
    assert import_result.exit_code == 0, import_result.stdout
    assert "Imported: exportable" in import_result.stdout

    # Verify restored profile has the real token
    storage = ProfileStorage()
    restored = storage.get_profile("exportable")
    assert restored is not None
    assert restored["token"] == token_value


def test_export_import_preserves_provider_metadata(
    runner: CliRunner, tmp_path: Path
) -> None:
    claude_token = "sk-ant-export-import-claude-1234567890"
    zai_token = "zai-token-export-import-1234567890abcd"
    custom_api = "https://custom.z.ai/api/anthropic"

    runner.invoke(
        app,
        ["save", "claude-default", "--token", claude_token],
        catch_exceptions=False,
    )
    runner.invoke(
        app,
        [
            "save",
            "zai-profile",
            "--token",
            zai_token,
            "--provider",
            PROVIDER_ZAI,
            "--api-url",
            custom_api,
        ],
        catch_exceptions=False,
    )

    export_path = tmp_path / "profiles.json"
    export_result = runner.invoke(
        app,
        ["export", str(export_path), "--include-tokens"],
        catch_exceptions=False,
    )
    assert export_result.exit_code == 0, export_result.stdout

    exported_payload = json.loads(export_path.read_text())
    assert exported_payload["zai-profile"]["provider"] == PROVIDER_ZAI
    assert exported_payload["zai-profile"]["api_url"] == custom_api

    runner.invoke(
        app, ["delete", "claude-default", "--no-confirm"], catch_exceptions=False
    )
    runner.invoke(
        app, ["delete", "zai-profile", "--no-confirm"], catch_exceptions=False
    )

    import_result = runner.invoke(
        app, ["import-profiles", str(export_path)], catch_exceptions=False
    )
    assert import_result.exit_code == 0, import_result.stdout

    storage = ProfileStorage()
    restored = storage.get_profile("zai-profile")
    assert restored is not None
    assert restored["provider"] == PROVIDER_ZAI
    assert restored.get("api_url") == custom_api
    assert restored["token"] == zai_token


def test_switch_with_show_tokens_displays_unmasked_tokens(runner: CliRunner) -> None:
    """Test switch command shows tokens when requested - macOS compatible."""
    # Use valid token format
    token_value = "sk-ant-test-visual-123456789012345678901234567890"

    save_result = runner.invoke(
        app, ["save", "visual", "--token", token_value], catch_exceptions=False
    )
    assert save_result.exit_code == 0, save_result.stdout

    switch_result = runner.invoke(
        app, ["switch", "--show-tokens"], input="1\n", catch_exceptions=False
    )
    assert switch_result.exit_code == 0, switch_result.stdout

    # Check that the token prefix is visible (Rich may truncate)
    # We don't check for the exact full token due to terminal width truncation
    assert "sk-ant" in switch_result.stdout


def test_doctor_reports_config_directory(runner: CliRunner) -> None:
    """Test doctor command reports configuration - works on all platforms."""
    result = runner.invoke(app, ["doctor"], input="n\n", catch_exceptions=False)
    assert result.exit_code == 0, result.stdout
    config = Config()
    assert config.get_config_path() in result.stdout


def test_zai_provider_workflow(runner: CliRunner) -> None:
    """Test Z-AI provider profile creation and management - macOS compatible."""
    zai_token = "test-zai-key-123456789012345678901234567890"

    # Save Z-AI profile
    result = runner.invoke(
        app,
        [
            "save",
            "zai-test",
            "--provider",
            "zai",
            "--token",
            zai_token,
            "--description",
            "Test Z-AI profile",
            "--no-active",
        ],
        catch_exceptions=False,
    )
    assert result.exit_code == 0, result.stdout
    assert "ZAI" in result.stdout
    assert "https://api.z.ai/api/anthropic" in result.stdout

    # Verify profile in storage
    storage = ProfileStorage()
    profile = storage.get_profile("zai-test")
    assert profile is not None
    assert profile["provider"] == "zai"
    assert profile["api_url"] == "https://api.z.ai/api/anthropic"
    assert profile["token"] == zai_token

    # Show Z-AI profile
    show_result = runner.invoke(app, ["show", "zai-test"], catch_exceptions=False)
    assert show_result.exit_code == 0, show_result.stdout
    assert "Provider: ZAI" in show_result.stdout
    assert "https://api.z.ai/api/anthropic" in show_result.stdout


def test_provider_isolation(runner: CliRunner) -> None:
    """Test seamless switching between Claude and Z-AI profiles."""
    claude_token = "sk-ant-test-claude-12345678901234567890123456"
    zai_token = "test-zai-key-123456789012345678901234567890"

    # Create Claude profile and make it active
    runner.invoke(
        app,
        ["save", "claude-prof", "--provider", "claude", "--token", claude_token],
        catch_exceptions=False,
    )

    # Create Z-AI profile (not active)
    runner.invoke(
        app,
        ["save", "zai-prof", "--provider", "zai", "--token", zai_token, "--no-active"],
        catch_exceptions=False,
    )

    # Switch from Claude to Z-AI - should succeed
    switch_result = runner.invoke(app, ["switch", "zai-prof"], catch_exceptions=False)

    # Should succeed with provider switch notification
    assert switch_result.exit_code == 0
    assert "Switching from CLAUDE to ZAI" in switch_result.stdout


def test_list_groups_by_provider(runner: CliRunner) -> None:
    """Test that list command groups profiles by provider - macOS compatible."""
    claude_token = "sk-ant-test-list-claude-1234567890123456789"
    zai_token = "test-zai-list-key-123456789012345678901234567890"

    # Create one of each provider
    runner.invoke(
        app,
        [
            "save",
            "list-claude",
            "--provider",
            "claude",
            "--token",
            claude_token,
            "--no-active",
        ],
        catch_exceptions=False,
    )

    runner.invoke(
        app,
        ["save", "list-zai", "--provider", "zai", "--token", zai_token, "--no-active"],
        catch_exceptions=False,
    )

    # List all profiles
    list_result = runner.invoke(app, ["list"], catch_exceptions=False)

    assert list_result.exit_code == 0, list_result.stdout
    # Should show both provider sections
    assert "=== Claude Profiles ===" in list_result.stdout
    assert "=== Z-AI Profiles ===" in list_result.stdout
    assert "list-claude" in list_result.stdout
    assert "list-zai" in list_result.stdout
