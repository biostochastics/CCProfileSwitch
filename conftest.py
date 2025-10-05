"""Pytest fixtures for CC Profile Switch tests."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import pytest

from cc_profile_switch import config as config_module
from cc_profile_switch import storage as storage_module
from cc_profile_switch import utils as utils_module


@pytest.fixture(autouse=True)
def isolated_cc_profile_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Provide an isolated config directory and in-memory keyring for every test."""

    keyring_store: Dict[Tuple[str, str], str] = {}

    def fake_set_password(service: str, key: str, value: str) -> None:
        keyring_store[(service, key)] = value

    def fake_get_password(service: str, key: str):  # type: ignore[override]
        return keyring_store.get((service, key))

    def fake_delete_password(service: str, key: str) -> None:
        if (service, key) not in keyring_store:
            raise storage_module.keyring.errors.PasswordDeleteError(
                "Password not found"
            )
        del keyring_store[(service, key)]

    class FakeKeyringBackend:
        """Simple stand-in object so the doctor command can report a backend name."""

        __module__ = "cc_profile_switch.tests"
        __name__ = "InMemoryKeyring"

    monkeypatch.setattr(storage_module.keyring, "set_password", fake_set_password)
    monkeypatch.setattr(storage_module.keyring, "get_password", fake_get_password)
    monkeypatch.setattr(storage_module.keyring, "delete_password", fake_delete_password)
    monkeypatch.setattr(
        storage_module.keyring, "get_keyring", lambda: FakeKeyringBackend()
    )

    config_root = tmp_path / "config"

    def fake_user_config_dir(app_name: str) -> str:
        path = config_root / app_name
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    monkeypatch.setattr(storage_module, "_user_config_dir", fake_user_config_dir)
    monkeypatch.setattr(config_module, "_user_config_dir", fake_user_config_dir)

    monkeypatch.setattr(utils_module, "find_claude_config_paths", lambda: [])
