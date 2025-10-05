"""Unit tests for CC Profile Switch core helpers."""

from __future__ import annotations

from pathlib import Path

from cc_profile_switch.config import Config
from cc_profile_switch.storage import ProfileStorage
from cc_profile_switch.utils import mask_token, validate_token


def test_token_helpers_mask_and_validate() -> None:
    token = "sk-ant-api03-example-token"
    masked = mask_token(token, visible_chars=6)

    assert masked.startswith("sk-ant")
    assert set(masked[6:]) == {"*"}
    assert validate_token(token) is True
    assert validate_token("") is False
    assert validate_token("bad token") is False


def test_profile_storage_round_trip(tmp_path: Path) -> None:
    storage = ProfileStorage()
    metadata = {"created": "2024-01-01T00:00:00", "description": "Sample"}

    assert storage.save_profile("sample", "sk-ant-api03-sample", metadata) is True
    storage.update_profile_list(["sample"])

    profile = storage.get_profile("sample")
    assert profile
    assert profile["token"] == "sk-ant-api03-sample"
    assert profile["metadata"] == metadata

    assert storage.save_active_token("sk-ant-api03-sample") is True
    assert storage.get_active_token() == "sk-ant-api03-sample"


def test_config_paths_and_mutation(tmp_path: Path) -> None:
    config = Config()
    config.ensure_config_dir()

    default_path = Path(config.get_active_token_path())
    assert default_path.name == ".credentials.json"

    custom_path = tmp_path / "tokens" / "active.json"
    assert config.set_active_token_target("file", str(custom_path)) is True
    assert Path(config.get_active_token_path()) == custom_path
