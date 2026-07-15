#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: effective_lengths.csv ===
cat > $OUTDIR/effective_lengths.csv <<'FFEOF'
configuration,length_Angstrom,effective_length_Angstrom
DWCNT_vdW,160,12.0
DWCNT_vdW,324,25.0
DWCNT_vdW,590,45.0
DWCNT_covalent,160,35.0
DWCNT_covalent,590,140.0
SWCNT,0,250.0
FFEOF
