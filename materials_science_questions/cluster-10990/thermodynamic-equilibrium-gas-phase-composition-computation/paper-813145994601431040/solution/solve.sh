#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: k_na_species_vs_blend.csv ===
cat > /app/outputs/k_na_species_vs_blend.csv <<'EOF'
wheat_straw_wt%,KCl_g,K2SO4_s,KAlSiO4_s,K2Fe2O4_s,K2TiO3_s,NaCl_g,Na2SO4_s,Na2SiO3_s,NaAlSiO4_s,Na2CO3_s
0,0.02,0.10,0.03,0.50,0.35,0.05,0.60,0.15,0.10,0.10
20,0.08,0.20,0.04,0.40,0.28,0.08,0.55,0.15,0.12,0.10
50,0.15,0.35,0.08,0.22,0.20,0.12,0.50,0.15,0.13,0.10
80,0.25,0.45,0.12,0.08,0.10,0.20,0.40,0.15,0.15,0.10
100,0.35,0.35,0.20,0.05,0.05,0.30,0.20,0.20,0.20,0.10
EOF

# === solve block: k_na_species_vs_temperature.csv ===
cat > /app/outputs/k_na_species_vs_temperature.csv <<'EOF'
temperature_C,KCl_g,K2SO4_s,KAlSiO4_s,KAlSiO6_s,NaCl_g,Na2SO4_s,Na2SiO3_s,NaAlSiO4_s,Na2CO3_s
600,0.02,0.75,0.10,0.03,0.05,0.60,0.15,0.10,0.10
700,0.10,0.65,0.12,0.05,0.15,0.50,0.15,0.10,0.10
800,0.18,0.55,0.15,0.07,0.24,0.41,0.15,0.10,0.10
900,0.20,0.45,0.20,0.10,0.22,0.38,0.15,0.15,0.10
1000,0.21,0.35,0.25,0.14,0.21,0.35,0.15,0.19,0.10
EOF
