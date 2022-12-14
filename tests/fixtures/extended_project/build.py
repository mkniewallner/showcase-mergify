from __future__ import annotations

from pathlib import Path
from typing import Any


def build(setup_kwargs: dict[str, Any]):
    assert setup_kwargs["name"] == "extended-project"
    assert setup_kwargs["version"] == "1.2.3"

    dynamic_module = Path(__file__).parent / "extended_project" / "built.py"
    dynamic_module.write_text("# Generated by build.py")
