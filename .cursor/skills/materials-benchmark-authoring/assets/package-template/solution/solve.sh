#!/usr/bin/env bash
set -euo pipefail

readonly OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# CHECKER_FULL_SCORE_FIXTURE
# Replace the placeholder payload below with every standard correct output from
# the frozen Gold and output contract. Do not run the primary scientific task.
python3 - "$OUTDIR" <<'PYEOF'
from __future__ import annotations

import sys
from pathlib import Path

outdir = Path(sys.argv[1])
outdir.mkdir(parents=True, exist_ok=True)

raise SystemExit("TODO: materialize every declared standard correct output")
PYEOF
