#!/usr/bin/env bash
# Playbook demo: render the bundled data end-to-end without secrets or network.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../.."

. .venv/bin/activate 2>/dev/null || true
if ! command -v fde-portfolio >/dev/null; then
  pip install -e '.[dev]'
fi

echo "== step 1: list =="
fde-portfolio list

echo ""
echo "== step 2: validate =="
fde-portfolio check

echo ""
echo "== step 3: single-phase checklist =="
fde-portfolio checklist discovery --project "Acme AI intake"

echo ""
echo "== step 4: full project worksheet =="
tmp="$(mktemp)"
fde-portfolio build --project "Acme AI intake" --out "$tmp"
head -25 "$tmp"
rm "$tmp"

echo ""
echo "== all green =="
