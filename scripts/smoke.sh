#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
for f in README.md docs/implementation-playbook.md docs/architecture.md docs/evaluation-strategy.md docs/public-boundary.md; do test -s "$f"; done
echo "fde-portfolio smoke PASS"
