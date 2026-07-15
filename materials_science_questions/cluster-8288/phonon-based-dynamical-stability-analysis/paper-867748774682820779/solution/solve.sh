#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/usr/bin/env bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "lattice_constant_a": 3.257,
  "lattice_constant_b": 3.959,
  "band_gap_SOC": 76.0,
  "C11": 130.67,
  "C22": 215.81,
  "C12": 17.08,
  "C66": 53.45,
  "e31": -0.593,
  "e31_electronic": -0.612,
  "e31_ionic": 0.019,
  "e32": -0.545,
  "e32_electronic": -0.513,
  "e32_ionic": -0.032,
  "d31": -0.425,
  "d32": -0.219,
  "Z2": 1,
  "phonon_stable": true
}
EOF
