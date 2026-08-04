#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
for f in README.md docs/implementation-playbook.md docs/architecture.md docs/evaluation-strategy.md docs/public-boundary.md; do
  test -s "$f"
done
echo "fde-portfolio smoke PASS"
