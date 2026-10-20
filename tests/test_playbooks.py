"""Playbook loader, schema, and rendering tests.

These cover both the data contract and the CLI surface; CLI smoke
is in `tests/test_cli.py`.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

from fde_portfolio.loader import (
    ITEM_TYPES,
    PHASES,
    PlaybookError,
    list_playbooks,
    load_playbook,
    validate_playbook,
)
from fde_portfolio.render import render_playbook, render_project

DATA_DIR = Path(__file__).parent.parent / "src" / "fde_portfolio" / "playbooks"


def _read(name: str) -> dict:
    return yaml.safe_load((DATA_DIR / f"{name}.yaml").read_text("utf-8"))


@pytest.mark.parametrize("name", PHASES)
def test_every_playbook_validates(name):
    data = _read(name)
    assert validate_playbook(data) == [], f"{name} failed validation"


@pytest.mark.parametrize("name", PHASES)
def test_playbook_id_matches_phase(name):
    data = _read(name)
    assert data["id"] == data["phase"] == name


@pytest.mark.parametrize("name", PHASES)
def test_playbook_minimum_items(name):
    pb = load_playbook(name)
    assert len(pb.items) >= 3


@pytest.mark.parametrize("name", PHASES)
def test_every_item_has_id_unique(name):
    pb = load_playbook(name)
    ids = [i.id for i in pb.items]
    assert len(ids) == len(set(ids)), f"{name} has duplicate ids"


@pytest.mark.parametrize("name", PHASES)
def test_every_item_type_valid(name):
    pb = load_playbook(name)
    for item in pb.items:
        assert item.type in ITEM_TYPES, f"{name}/{item.id} has bad type {item.type!r}"


def test_no_client_names_anywhere_in_playbook_data():
    """A reviewer must not find a real customer name in the public data.

    The YAML files are templates; the example_response fields are
    `<placeholder>` shells and never a real statement from a named
    customer. This scan guards against future drift.
    """
    forbidden_real_names = []  # intentionally empty: the rules say "no client names"
    for path in DATA_DIR.glob("*.yaml"):
        text = path.read_text("utf-8")
        for name in forbidden_real_names:
            assert name.lower() not in text.lower(), f"{path} mentions {name!r}"
    # And the YAML must never contain a name-shaped "Acme Corp"-style fragment
    bad = re.compile(r"\b[A-Z][a-z]+\s+(Corp|Inc|LLC|Ltd|Co\.|Holding|Industries|Group|Solutions)\b")
    for path in DATA_DIR.glob("*.yaml"):
        text = path.read_text("utf-8")
        assert not bad.search(text), f"{path} has what looks like a real customer name"


def test_no_invented_outcomes():
    """The playbooks do not name fabricated outcomes.

    The check is for patterns a copywriter would use to brag:
    `42% reduction`, `$120 saved`, `10x faster`, `200ms latency win`.
    Percentages that anchor a target policy (e.g. "human review rate")
    are fine if the playbook says so; the check looks for the brag
    phrasing in particular.
    """
    brag = re.compile(
        r"\b\d+%\s+(reduction|increase|improvement|faster|drop|boost|growth)\b"
        r"|\$\s*\d[\d,kKmM]*\s+(saved|cut|saved per|reduction|won|spent)\b"
        r"|\b\d+\s*x\s+faster\b"
        r"|\b\d+\s*ms\s+latency\b",
        re.IGNORECASE,
    )
    for path in DATA_DIR.glob("*.yaml"):
        text = path.read_text("utf-8")
        assert not brag.search(text), f"{path} includes a brag-shaped outcome: {brag.search(text).group(0)!r}"


def test_render_playbook_includes_every_item():
    pb = load_playbook("discovery")
    text = render_playbook(pb, project_name="Acme AI intake")
    for item in pb.items:
        assert item.title in text, f"item {item.id} title missing from rendered playbook"


def test_render_playbook_includes_owner_marker():
    pb = load_playbook("go-live")
    text = render_playbook(pb, project_name="Test")
    assert "(owner:" in text


def test_render_project_contains_all_five_phases():
    text = render_project("Acme AI intake")
    for phase in PHASES:
        # The phase header is the playbook's title
        pb = load_playbook(phase)
        assert pb.title in text, f"phase {phase!r} missing from project worksheet"


def test_render_project_includes_phase_order_discovery_first():
    text = render_project("Acme AI intake")
    pos = [(text.find(load_playbook(p).title)) for p in PHASES]
    assert pos == sorted(pos), f"phases not in canonical order: {pos}"


def test_load_playbook_invalid_phase_raises():
    with pytest.raises(PlaybookError):
        load_playbook("not-a-phase")


def test_load_playbook_loads_file_by_path():
    pb = load_playbook(str(DATA_DIR / "discovery.yaml"))
    assert pb.id == "discovery"


def test_list_playbooks_returns_all_five():
    books = list_playbooks()
    assert isinstance(books, list)
    assert sorted(b.id for b in books) == sorted(PHASES)
