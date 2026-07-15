#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: structural_properties.json ===
cat > "$OUTDIR/structural_properties.json" <<'FFEOF'
{
  "AlNiAs": {
    "a": 5.72113,
    "B0": 111.4,
    "B0_prime": 4.72,
    "delta_H": -1.23
  },
  "AlNiSb": {
    "a": 5.99904,
    "B0": 98.0,
    "B0_prime": 4.81,
    "delta_H": -1.08
  }
}
FFEOF

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'FFEOF'
{
  "AlNiAs": {
    "C11": 146.026,
    "C12": 91.270,
    "C44": 47.716,
    "Cp": 43.554,
    "A": 2.191
  },
  "AlNiSb": {
    "C11": 149.272,
    "C12": 73.435,
    "C44": 37.369,
    "Cp": 36.066,
    "A": 2.072
  }
}
FFEOF

# === solve block: mechanical_properties.json ===
cat > "$OUTDIR/mechanical_properties.json" <<'FFEOF'
{
  "AlNiAs": {
    "B_V": 109.522,
    "B_R": 109.522,
    "B_H": 109.522,
    "G_V": 39.580,
    "G_R": 36.785,
    "G_H": 38.183,
    "E_V": 105.976,
    "E_R": 99.244,
    "E_H": 102.610,
    "nu_V": 0.338,
    "nu_R": 0.348,
    "nu_H": 0.343,
    "BH_GH": 2.868
  },
  "AlNiSb": {
    "B_V": 98.714,
    "B_R": 98.714,
    "B_H": 98.714,
    "G_V": 37.589,
    "G_R": 37.587,
    "G_H": 37.588,
    "E_V": 100.066,
    "E_R": 100.061,
    "E_H": 100.064,
    "nu_V": 0.331,
    "nu_R": 0.331,
    "nu_H": 0.331,
    "BH_GH": 2.626
  }
}
FFEOF

# === solve block: dos_at_fermi.json ===
cat > "$OUTDIR/dos_at_fermi.json" <<'FFEOF'
{
  "AlNiAs": 0.75,
  "AlNiSb": 1.01
}
FFEOF

# === solve block: phonon_frequencies.json ===
cat > "$OUTDIR/phonon_frequencies.json" <<'FFEOF'
{
  "AlNiAs": {
    "T1_freq": 255.0,
    "T2_freq": 192.45
  },
  "AlNiSb": {
    "T1_freq": 227.32,
    "T2_freq": 193.68
  }
}
FFEOF

# === solve finalize ===
echo "All scored outputs written."
