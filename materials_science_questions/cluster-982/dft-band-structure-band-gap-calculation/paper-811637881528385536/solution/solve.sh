#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optical_peaks.json ===
cat > "$OUTDIR/optical_peaks.json" <<'EOF'
{
  "Au20": {
    "E1": 1.79,
    "E2": 2.51,
    "E3": 3.87,
    "absorption_peak_nm": 707
  },
  "Au19Zn1": {
    "E1": 1.64,
    "E2": 2.52,
    "E3": 3.90
  },
  "Au18Zn2": {
    "E1": 1.69,
    "E2": 2.35,
    "E3": 3.92
  },
  "Au17Zn3": {
    "E1": 1.47,
    "E2": 2.20,
    "E3": 3.94,
    "absorption_peak_nm": 813
  },
  "Au16Zn4": {
    "E1": 0.85,
    "E2": 2.15,
    "E3": 3.96
  }
}
EOF
