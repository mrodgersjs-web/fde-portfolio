"""CLI smoke + golden output tests."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from fde_portfolio import cli

REPO = Path(__file__).parent.parent


def _args(*args: str) -> int:
    return cli.main(list(args))


def test_cli_list_succeeds():
    assert _args("list") == 0


def test_cli_check_pass():
    assert _args("check") == 0


def test_cli_checklist_to_stdout():
    code = _args("checklist", "discovery", "--project", "Acme AI intake")
    assert code == 0


def test_cli_build_writes_file(tmp_path):
    out = tmp_path / "worksheet.md"
    assert _args("build", "--project", "Acme AI intake", "--out", str(out)) == 0
    text = out.read_text(encoding="utf-8")
    assert "Forward Deployed Engineering worksheet" in text
    assert "Acme AI intake" in text


def test_cli_unknown_playbook_exits_bad():
    # sys.exit raises SystemExit; the function's return code is via _args.
    # We catch it here so the test reports exit code 1, not a traceback.
    with pytest.raises(SystemExit) as exc:
        _args("checklist", "not-a-phase")
    assert exc.value.code == 1


def test_cli_build_via_subprocess(tmp_path):
    """End-to-end subprocess invocation, the same shape CI runs."""
    out = tmp_path / "worksheet.md"
    r = subprocess.run(
        [sys.executable, "-m", "fde_portfolio.cli", "build",
         "--project", "Acme AI intake", "--out", str(out)],
        capture_output=True, text=True, cwd=str(REPO),
    )
    assert r.returncode == 0, r.stderr
    assert out.exists()
    assert out.read_text(encoding="utf-8").startswith("# Acme AI intake")
