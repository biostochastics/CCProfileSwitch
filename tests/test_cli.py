"""Integration tests for the Typer CLI commands."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from cc_profile_switch.cli import app
from cc_profile_switch.config import Config
from cc_profile_switch.storage import ProfileStorage


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_save_list_and_cycle_flow(runner: CliRunner) -> None:
    token_primary = "sk-ant-api03-primary"
    token_secondary = "sk-ant-api03-secondary"

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

    storage = ProfileStorage()
    stored_profile = storage.get_profile("work")
    assert stored_profile is not None
    assert stored_profile["token"] == token_primary

    list_result = runner.invoke(
        app,
        ["list", "--output-format", "json", "--show-tokens"],
        catch_exceptions=False,
    )
    assert list_result.exit_code == 0, list_result.stdout
    profiles_json = json.loads(list_result.stdout)
    assert profiles_json["work"]["token"] == token_primary
    assert profiles_json["work"]["active"] is True

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

    cycle_result = runner.invoke(app, ["cycle"], catch_exceptions=False)
    assert cycle_result.exit_code == 0, cycle_result.stdout

    config = Config()
    active_path = Path(config.get_active_token_path())
    active_payload = json.loads(active_path.read_text())
    assert active_payload["token"] == token_secondary


def test_export_masks_tokens_and_import_prompts_for_real_token(
    runner: CliRunner, tmp_path: Path
) -> None:
    token_value = "sk-ant-api03-exporttest"
    runner.invoke(
        app, ["save", "exportable", "--token", token_value], catch_exceptions=False
    )

    export_path = tmp_path / "profiles.json"
    export_result = runner.invoke(
        app, ["export", str(export_path)], catch_exceptions=False
    )
    assert export_result.exit_code == 0, export_result.stdout

    export_data = json.loads(export_path.read_text())
    assert export_data["exportable"]["token"] != token_value
    assert token_value not in export_path.read_text()

    delete_result = runner.invoke(
        app, ["delete", "exportable", "--no-confirm"], catch_exceptions=False
    )
    assert delete_result.exit_code == 0, delete_result.stdout

    import_input = "y\n" + token_value + "\n"
    import_result = runner.invoke(
        app,
        ["import-profiles", str(export_path)],
        input=import_input,
        catch_exceptions=False,
    )
    assert import_result.exit_code == 0, import_result.stdout
    assert "Imported: exportable" in import_result.stdout

    storage = ProfileStorage()
    restored = storage.get_profile("exportable")
    assert restored is not None
    assert restored["token"] == token_value


def test_switch_with_show_tokens_displays_unmasked_tokens(runner: CliRunner) -> None:
    token_value = "sk-ant-api03-visualtest"
    runner.invoke(
        app, ["save", "visual", "--token", token_value], catch_exceptions=False
    )

    switch_result = runner.invoke(
        app, ["switch", "--show-tokens"], input="1\n", catch_exceptions=False
    )
    assert switch_result.exit_code == 0, switch_result.stdout
    assert token_value in switch_result.stdout


def test_doctor_reports_config_directory(runner: CliRunner) -> None:
    result = runner.invoke(app, ["doctor"], input="n\n", catch_exceptions=False)
    assert result.exit_code == 0, result.stdout
    config = Config()
    assert config.get_config_path() in result.stdout
