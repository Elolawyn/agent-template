"""Centralized package metadata from pyproject.toml."""

from __future__ import annotations

import tomllib  # Python 3.11+ required by project
from pathlib import Path
from typing import Any

PACKAGE_NAME = "agent-template"


def _read_from_pyproject() -> dict[str, Any]:
    """Read metadata directly from pyproject.toml."""
    pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"

    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    return data.get("project", {})


def get_version() -> str:
    """Get package version from pyproject.toml."""
    return _read_from_pyproject().get("version", "0.0.0")


def get_name() -> str:
    """Get package name from pyproject.toml."""
    return _read_from_pyproject().get("name", "agent-template")


def get_description() -> str:
    """Get package description from pyproject.toml."""
    return _read_from_pyproject().get(
        "description",
        "Plantilla para crear agentes de inteligencia artificial con FastAPI",
    )


def get_api_metadata() -> dict[str, str]:
    """Get API-specific metadata with appropriate formatting."""
    project_data = _read_from_pyproject()
    name = project_data.get("name", get_name())
    description = project_data.get("description", get_description())
    version = project_data.get("version", get_version())

    return {
        "api_title": name + " API",
        "api_description": "API "
        + description.lower().replace("plantilla para crear ", "template for "),
        "api_version": version,
    }


# Export convenient constants for backward compatibility
__version__ = get_version()
__name__ = get_name()
__description__ = get_description()
