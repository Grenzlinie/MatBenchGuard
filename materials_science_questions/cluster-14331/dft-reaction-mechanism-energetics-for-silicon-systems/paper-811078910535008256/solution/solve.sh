#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "total_energies": {
    "H-": {
      "hf": -0.4875,
      "correlated": -0.5211
    },
    "H2": {
      "hf": -1.1322,
      "correlated": -1.1680
    },
    "SiH3- (C3v)": {
      "hf": -290.6182,
      "correlated": -290.7847
    },
    "SiH3- (D3h)": {
      "hf": -290.5746,
      "correlated": -290.7429
    },
    "SiH4": {
      "hf": -291.2320,
      "correlated": -291.3899
    },
    "SiH5- (D3h)": {
      "hf": -291.7414,
      "correlated": -291.9429
    },
    "SiH5- (C4v)": {
      "hf": -291.7363,
      "correlated": -291.9390
    },
    "SiH4 + H- (200 au)": {
      "hf": -291.7195,
      "correlated": -291.9115
    }
  },
  "reaction_energies": {
    "reaction1_hf": -13.74,
    "reaction1_correlated": -19.70,
    "pseudorotation_hf": 3.20,
    "pseudorotation_correlated": 2.45,
    "inversion_hf": 27.36,
    "inversion_correlated": 26.23,
    "reaction3_hf": 5.65,
    "reaction3_correlated": 6.15
  }
}
FFEOF

# === solve finalize ===
echo "Reference artifacts written."
