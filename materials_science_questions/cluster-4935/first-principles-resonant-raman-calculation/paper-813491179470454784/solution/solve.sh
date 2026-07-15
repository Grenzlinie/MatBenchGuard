#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: blm_frequencies.json ===
cat > "$OUTDIR/blm_frequencies.json" << 'FFEOF'
[
  {"mode": "BM4", "frequency_cm1": 102},
  {"mode": "BM3", "frequency_cm1": 118},
  {"mode": "BM2", "frequency_cm1": 125},
  {"mode": "BM1", "frequency_cm1": 128}
]
FFEOF

# === solve block: band_gap.json ===
cat > "$OUTDIR/band_gap.json" << 'FFEOF'
{"dimer": "(8,6)-(9,7)", "band_gap_eV": 0.72}
FFEOF

# === solve finalize ===
# All artifacts written. Verify existence.
for f in blm_frequencies.json band_gap.json optimized_geometry.json dynamical_matrix_assembled.json raman_spectrum_blm.csv band_structure_edos.csv; do
  if [ ! -f "/app/outputs/$f" ]; then echo "MISSING: $f"; exit 1; fi
done
echo "Oracle solve complete."
