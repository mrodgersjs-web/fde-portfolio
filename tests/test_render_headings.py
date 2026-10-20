"""The rendered headings must match the README examples (colon separator, no em dash)."""
from pathlib import Path

from fde_portfolio import render


def test_render_module_uses_colon_headings():
    src = Path(render.__file__).read_text(encoding="utf-8")
    assert "— Forward Deployed Engineering worksheet" not in src
    assert ": Forward Deployed Engineering worksheet" in src
