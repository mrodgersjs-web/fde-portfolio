"""Loader for the YAML playbook files in src/fde_portfolio/playbooks/.

A playbook is a structured FDE phase checklist. Items are validated
against two JSON schemas:

* `file.schema.json` for the bundle shape;
* `playbook.schema.json` for each item.

The loader's only public surface is `load_playbook`, `load_playbooks`,
`list_playbooks`, `validate_playbook`, and the `Playbook` / `PlaybookItem`
data classes.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from importlib import resources
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

PHASES: tuple[str, ...] = ("discovery", "evaluation", "architecture", "go-live", "handoff")
ITEM_TYPES: tuple[str, ...] = ("question", "task", "decision", "evidence", "owners")
PLAYBOOKS_DIR = Path("playbooks")


class PlaybookError(ValueError):
    """Raised for any validation failure: schema, type, or phase mismatch."""


@dataclass(frozen=True)
class PlaybookItem:
    """One question / task / decision / evidence / owners entry in a playbook file."""

    id: str
    title: str
    description: str
    type: str
    default_owner: str | None = None
    example_response: str | None = None
    see_also: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, d: dict) -> PlaybookItem:
        if "id" not in d or not isinstance(d["id"], str):
            raise PlaybookError("item missing string 'id'")
        if d["type"] not in ITEM_TYPES:
            raise PlaybookError(
                f"item {d.get('id')!r}: type must be one of {ITEM_TYPES!r}, got {d.get('type')!r}"
            )
        see = d.get("see_also") or ()
        return cls(
            id=d["id"],
            title=d["title"],
            description=d["description"],
            type=d["type"],
            default_owner=d.get("default_owner"),
            example_response=d.get("example_response"),
            see_also=tuple(see),
        )


@dataclass(frozen=True)
class Playbook:
    """A single FDE phase playbook: discovery, evaluation, architecture, go-live, or handoff."""

    schema_version: int
    id: str
    title: str
    purpose: str
    phase: str
    items: tuple[PlaybookItem, ...]
    see_also: tuple[str, ...] = ()

    @property
    def item_ids(self) -> tuple[str, ...]:
        return tuple(i.id for i in self.items)

    def item(self, item_id: str) -> PlaybookItem | None:
        for i in self.items:
            if i.id == item_id:
                return i
        return None


def _bundled_path(name: str) -> Path:
    """Resolve a resource path inside the installed package."""
    return Path(resources.files("fde_portfolio").joinpath(name))


def _schema(name: str) -> dict:
    return json.loads(_bundled_path(f"schemas/{name}").read_text("utf-8"))


def validate_playbook(data: dict) -> list[str]:
    """Validate parsed YAML against the file schema and per-item rules.

    Returns a list of human-readable error messages; empty list means valid.
    """
    problems: list[str] = []

    file_schema = _schema("file.schema.json")
    item_schema = _schema("playbook.schema.json")
    # Inline the per-item ref so jsonschema can resolve it without a separate
    # Store. The two schemas are co-shipped in src/fde_portfolio/schemas/.
    file_schema = json.loads(json.dumps(file_schema).replace(
        '"$ref": "playbook.schema.json"', '"$ref": "#/$defs/playbook_item"'
    ))
    bundle = {"$defs": {"playbook_item": item_schema}, **file_schema}

    try:
        validator = Draft202012Validator(bundle)
    except Exception as e:  # pragma: no cover - schema load error
        problems.append(f"schema load: {e}")
        return problems

    for err in validator.iter_errors(data):
        problems.append(
            f"file schema: {err.message} at "
            f"{'/'.join(str(p) for p in err.absolute_path)}"
        )

    item_validator = Draft202012Validator(item_schema)
    for i, item in enumerate(data.get("items", []) or ()):
        for err in item_validator.iter_errors(item):
            problems.append(
                f"item[{i}] {item.get('id', '?')}: {err.message} at "
                f"{'/'.join(str(p) for p in err.absolute_path)}"
            )

    if "phase" in data and data["phase"] not in PHASES:
        problems.append(f"file schema: phase {data['phase']!r} must be one of {PHASES!r}")

    if "id" in data and "phase" in data and data["id"] != data["phase"]:
        problems.append(
            f"file schema: id {data['id']!r} does not match the phase {data['phase']!r}"
        )

    items = data.get("items") or []
    seen: set[str] = set()
    for item in items:
        if item.get("id") in seen:
            problems.append(f"duplicate item id: {item.get('id')!r}")
        seen.add(item.get("id"))

    return problems


def load_playbook(name: str, root: Path | None = None) -> Playbook:
    """Load one playbook by id or by file path.

    `name` may be a phase id (`discovery`, `evaluation`, `architecture`,
    `go-live`, `handoff`), a file stem, or a YAML file path. Returns the
    parsed `Playbook`; raises `PlaybookError` on any validation failure.
    """
    path = Path(name)
    if path.is_file():
        candidates = [path]
    elif path.suffix == ".yaml" and not path.exists():
        candidates = [path]  # surface 'no such file' below
    elif root is not None:
        candidates = [Path(root) / f"{name}.yaml"]
    else:
        # Bundled playbook from the installed package data
        candidates = [
            Path(__file__).parent / "playbooks" / f"{name}.yaml",
            _bundled_path(f"{PLAYBOOKS_DIR}/{name}.yaml"),
        ]

    for candidate in candidates:
        if candidate.is_file():
            raw = yaml.safe_load(candidate.read_text("utf-8"))
            if not isinstance(raw, dict):
                raise PlaybookError(f"playbook {candidate} must be a YAML mapping at the top")
            problems = validate_playbook(raw)
            if problems:
                raise PlaybookError(
                    f"playbook {candidate} has {len(problems)} validation problem(s): "
                    + "; ".join(problems[:3])
                    + ("..." if len(problems) > 3 else "")
                )
            items = tuple(PlaybookItem.from_dict(i) for i in raw["items"])
            return Playbook(
                schema_version=raw["schema_version"],
                id=raw["id"],
                title=raw["title"],
                purpose=raw["purpose"],
                phase=raw["phase"],
                items=items,
                see_also=tuple(raw.get("see_also") or ()),
            )

    raise PlaybookError(f"unknown playbook {name!r}: no file at {candidates}")


def load_playbooks(root: Path | None = None) -> dict[str, Playbook]:
    """Load every bundled playbook, keyed by phase id."""
    out: dict[str, Playbook] = {}
    for phase in PHASES:
        out[phase] = load_playbook(phase, root=root)
    return out


def list_playbooks(root: Path | None = None) -> list[Playbook]:
    """Return every playbook as a list in canonical phase order."""
    return [load_playbook(phase, root=root) for phase in PHASES]
