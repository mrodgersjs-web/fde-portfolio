"""fde-portfolio: structured playbook data plus a CLI that renders project checklists.

The package exposes five playbooks (`discovery`, `evaluation`,
`architecture`, `go-live`, `handoff`), each backed by a YAML file
under `src/fde_portfolio/playbooks/` and validated against the
JSON Schema in `src/fde_portfolio/schemas/`. The CLI renders any
playbook as a Markdown checklist, validates the bundle, or builds
a full project worksheet for a single engagement.
"""

from . import cli
from .loader import (
    PHASES,
    Playbook,
    PlaybookItem,
    list_playbooks,
    load_playbook,
    load_playbooks,
    validate_playbook,
)

__all__ = [
    "PHASES",
    "Playbook",
    "PlaybookItem",
    "load_playbook",
    "load_playbooks",
    "list_playbooks",
    "validate_playbook",
    "cli",
]

__version__ = "0.2.0"
