"""Unit tests for CC Profile Switch core helpers."""

from __future__ import annotations

import json
from pathlib import Path

from cc_profile_switch import __version__ as package_version
from cc_profile_switch.config import Config
from cc_profile_switch.storage import ProfileStorage
from cc_profile_switch.utils import mask_token, validate_token


def test_token_helpers_mask_and_validate() -> None:
    token = "sk-ant-test-token-12345678901234567890"
    masked = mask_token(token, visible_chars=6)

    assert masked.startswith("sk-ant")
    assert "*" in masked
    # validate_token returns (is_valid, error_message) tuple
    is_valid, error_msg = validate_token(token)
    assert is_valid is True
    assert error_msg == ""

    is_valid, _ = validate_token("")
    assert is_valid is False

    is_valid, _ = validate_token("bad token")
    assert is_valid is False


def test_profile_storage_round_trip(tmp_path: Path) -> None:
    storage = ProfileStorage()
    metadata = {"created": "2024-01-01T00:00:00", "description": "Sample"}
    test_token = "sk-ant-test-token-12345678901234567890"

    # Test saving a profile
    assert storage.save_profile("sample", test_token, metadata) is True
    storage.update_profile_list(["sample"])

    # Test retrieving a profile
    profile = storage.get_profile("sample")
    assert profile
    assert profile["token"] == test_token
    assert profile["metadata"] == metadata
    assert profile["provider"] == "claude"  # Default provider

    # Active token should round-trip via file storage
    assert storage.save_active_token(test_token) is True
    assert storage.get_active_token() == test_token


def test_active_token_preserves_oauth_payload() -> None:
    storage = ProfileStorage()
    oauth_payload = json.dumps(
        {
            "claudeAiOauth": {
                "accessToken": "sk-ant-oat-example-token",
                "refreshToken": "refresh-token-value",
            }
        }
    )

    assert storage.save_active_token(oauth_payload) is True
    retrieved = storage.get_active_token()
    assert retrieved == oauth_payload


def test_config_paths_and_mutation(tmp_path: Path) -> None:
    config = Config()
    config.ensure_config_dir()

    default_path = Path(config.get_active_token_path())
    assert default_path.name == ".credentials.json"

    custom_path = tmp_path / "tokens" / "active.json"
    assert config.set_active_token_target("file", str(custom_path)) is True
    assert Path(config.get_active_token_path()) == custom_path


def test_package_version_matches_pyproject() -> None:
    # tomllib is available in Python 3.11+
    import tomllib

    pyproject = tomllib.loads(Path("pyproject.toml").read_text())
    expected = pyproject["tool"]["poetry"]["version"]
    assert package_version == expected
