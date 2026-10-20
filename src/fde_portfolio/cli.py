"""Command-line interface for the FDE playbook data."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .loader import PHASES, PlaybookError, list_playbooks, load_playbook
from .render import render_playbook, render_project

OK, USAGE, BAD = 0, 2, 1


def _load_or_die(name: str):
    try:
        return load_playbook(name)
    except PlaybookError as e:
        print(str(e), file=sys.stderr)
        sys.exit(BAD)


def _bundle_path(name: str) -> Path:
    return Path(__file__).parent / "playbooks" / f"{name}.yaml"


def cmd_list(_args) -> int:
    rows = [(p.id, p.title, len(p.items)) for p in list_playbooks()]
    print(f"{'id':<14} {'items':>5}  title")
    print(f"{'-' * 14} {'-' * 5}  {'-' * 50}")
    for pid, title, n in rows:
        print(f"{pid:<14} {n:>5}  {title}")
    return OK


def _check_one(name: str, args) -> list[str]:
    """Re-validate one playbook against its file. Returns list of problems."""
    import yaml

    from .loader import validate_playbook as validate_dict
    candidates: list[Path] = []
    if args.root:
        candidates.append(Path(args.root) / f"{name}.yaml")
    else:
        candidates.append(_bundle_path(name))
    for path in candidates:
        if path.is_file():
            data = yaml.safe_load(path.read_text("utf-8"))
            return validate_dict(data)
    return [f"playbook {name!r}: not found at {candidates}"]


def cmd_check(args) -> int:
    problems_total = 0
    if args.playbook:
        names = list(args.playbook)
    elif args.root:
        names = [Path(p).stem for p in sorted(Path(args.root).glob("*.yaml"))]
    else:
        names = list(PHASES)
    for name in names:
        try:
            data = load_playbook(name)
            problems = _check_one(name, args)
            if problems:
                for p in problems:
                    print(f"{name}: {p}", file=sys.stderr)
                problems_total += len(problems)
            else:
                print(f"{name}: valid ({len(data.items)} items)")
        except PlaybookError as e:
            print(str(e), file=sys.stderr)
            problems_total += 1
    if problems_total:
        print(f"{problems_total} validation problem(s)", file=sys.stderr)
        return BAD
    return OK


def cmd_checklist(args) -> int:
    pb = _load_or_die(args.playbook)
    out = render_playbook(pb, project_name=args.project)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    return OK


def cmd_build(args) -> int:
    text = render_project(args.project, root=None)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out} for {args.project}")
    else:
        sys.stdout.write(text)
    return OK


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="fde-portfolio")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("list", help="list bundled playbooks and item counts")
    s.set_defaults(fn=cmd_list)

    s = sub.add_parser("check", help="validate every playbook against the JSON Schema")
    s.add_argument("--root", help="directory of YAML files (defaults to bundled)")
    s.add_argument("playbook", nargs="*", help="playbook ids or file stems; default = all bundled")
    s.set_defaults(fn=cmd_check)

    s = sub.add_parser("checklist", help="render one playbook as a Markdown checklist")
    s.add_argument("playbook", help="playbook id or YAML file stem")
    s.add_argument("--project", default="<engagement>", help="name of the engagement rendered into the title")
    s.add_argument("--out", help="write to this path; default = stdout")
    s.set_defaults(fn=cmd_checklist)

    s = sub.add_parser("build", help="render the full project worksheet (all five phases)")
    s.add_argument("--project", required=True, help="name of the engagement rendered into the title")
    s.add_argument("--out", help="write to this path; default = stdout")
    s.set_defaults(fn=cmd_build)

    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
