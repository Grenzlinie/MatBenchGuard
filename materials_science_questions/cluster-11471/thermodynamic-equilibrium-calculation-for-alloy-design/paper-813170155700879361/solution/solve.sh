#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_equilibrium_intervals.tsv ===
cat > /app/outputs/phase_equilibrium_intervals.tsv <<'FFEOF'
alloy	equilibrium_label	start_temperature_K	end_temperature_K
Ch3F12	ferrite+MC+M7C3	750	1046
Ch3F12	ferrite+MC+M7C3+austenite	1046	1058
Ch3F12	ferrite+MC+austenite	1058	1075
Ch3F12	austenite+MC	1075	1563
Ch3F12	austenite+MC+liquid	1563	1581
Ch3F12	MC+liquid	1581	1643
Ch3F12	liquid	1643	1700
Ch12MF4	ferrite+MC+M7C3	750	1077
Ch12MF4	ferrite+MC+M7C3+austenite	1077	1084
Ch12MF4	austenite+MC+M7C3	1084	1475
Ch12MF4	austenite+MC+M7C3+liquid	1475	1484
Ch12MF4	austenite+MC+liquid	1484	1491
Ch12MF4	austenite+liquid	1491	1613
Ch12MF4	liquid	1613	1700
FFEOF
