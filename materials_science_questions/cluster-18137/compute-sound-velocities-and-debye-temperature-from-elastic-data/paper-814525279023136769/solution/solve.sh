#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'JSONEOF'
{
  "LDA": {
    "C11": 106.34,
    "C12": 66.08,
    "C13": 52.20,
    "C33": 106.53,
    "C44": 25.64,
    "C66": 20.13
  },
  "GGA-WC": {
    "C11": 110.58,
    "C12": 65.76,
    "C13": 47.18,
    "C33": 90.89,
    "C44": 23.11,
    "C66": 22.41
  }
}
JSONEOF

# === solve block: polycrystalline_properties.json ===
cat > "$OUTDIR/polycrystalline_properties.json" <<'JSONEOF'
{
  "LDA": {
    "B": 73.23,
    "G": 23.92,
    "E": 64.71,
    "sigma": 0.353,
    "A": 1.27,
    "B_over_G": 3.06,
    "H": 2.34
  },
  "GGA-WC": {
    "B": 69.29,
    "G": 23.71,
    "E": 63.85,
    "sigma": 0.346,
    "A": 1.03,
    "B_over_G": 2.92,
    "H": 2.44
  }
}
JSONEOF

# === solve block: thermodynamic_properties.json ===
cat > "$OUTDIR/thermodynamic_properties.json" <<'JSONEOF'
{
  "LDA": {
    "rho": 4.12,
    "v_l": 5051.27,
    "v_t": 2409.53,
    "v_m": 2710.06,
    "Theta_D": 310.16
  },
  "GGA-WC": {
    "rho": 3.91,
    "v_l": 5080.01,
    "v_t": 2462.51,
    "v_m": 2767.30,
    "Theta_D": 311.24
  }
}
JSONEOF
