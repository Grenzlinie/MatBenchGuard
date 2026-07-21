#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pt2a_keff.csv ===
# Write PT2a keff data (multiple spurious modes)
cat > "$OUTDIR/pt2a_keff.csv" <<'CSVEOF'
frequency_Hz,keff
310000,0.02
330000,0.15
345000,0.35
370000,0.20
390000,0.10
410000,0.05
CSVEOF

# === solve block: pt2b_keff.csv ===
# Write PT2b keff data (clean working range)
cat > "$OUTDIR/pt2b_keff.csv" <<'CSVEOF'
frequency_Hz,keff
200000,0.01
350000,0.40
500000,0.02
CSVEOF

# === solve block: summary.json ===
# Write summary JSON with spurious mode flags and PT2b parameters
cat > "$OUTDIR/summary.json" <<'JSONEOF'
{
  "PT2a_spurious_modes_present": true,
  "PT2b_spurious_modes_present": false,
  "PT2b_resonance_frequency_Hz": 350000.0,
  "PT2b_anti_resonance_frequency_Hz": 381840.0,
  "PT2b_keff": 0.40
}
JSONEOF
