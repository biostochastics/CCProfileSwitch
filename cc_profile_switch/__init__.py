"""CC Profile Switch - A cross-platform Claude profile manager."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as pkg_version
from pathlib import Path


def _read_pyproject_version() -> str | None:
    """Attempt to read the version from pyproject.toml when running from source."""
    pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    if not pyproject_path.exists():
        return None

    try:  # Python 3.11+ ships tomllib in the stdlib
        import tomllib  # type: ignore[attr-defined]
    except ModuleNotFoundError:  # pragma: no cover - fallback for older interpreters
        try:
            import tomli as tomllib  # type: ignore[import-not-found]
        except ModuleNotFoundError:
            return None

    try:
        text = pyproject_path.read_text(encoding="utf-8")
        data = tomllib.loads(text)
        return data["tool"]["poetry"]["version"]
    except (OSError, KeyError):  # pragma: no cover - IO/key errors
        return None
    except Exception:  # pragma: no cover - TOML decode errors (varies by library)
        return None


_source_version = _read_pyproject_version()

if _source_version:
    __version__ = _source_version
else:
    try:
        __version__ = pkg_version("cc-profile-switch")
    except PackageNotFoundError:  # pragma: no cover - development fallback
        __version__ = "0.0.0"

__author__ = "Claude Profile Manager"
__description__ = "A cross-platform Claude profile manager with Typer and Rich"
