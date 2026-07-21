#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: catalyst_relative_activity_vs_dispersion.tsv ===
cat > "$OUTDIR/catalyst_relative_activity_vs_dispersion.tsv" <<'FFEOF'
Dx	catalyst_relative_activity
0.0	1.0
0.3	0.85
0.6	0.65
0.9	0.40
FFEOF

# === solve block: selectivity_vs_dispersion.tsv ===
cat > "$OUTDIR/selectivity_vs_dispersion.tsv" <<'FFEOF'
Dx	selectivity_HANT	selectivity_4A2NT	selectivity_2A4NT
0.0	0.76	0.14	0.10
0.3	0.60	0.28	0.12
0.6	0.44	0.42	0.14
0.9	0.28	0.56	0.16
FFEOF

# === solve block: arrhenius_data.tsv ===
cat > "$OUTDIR/arrhenius_data.tsv" <<'FFEOF'
temperature_K	TOF_2_4DNT
313.15	0.00588
323.15	0.01200
333.15	0.02348
FFEOF
