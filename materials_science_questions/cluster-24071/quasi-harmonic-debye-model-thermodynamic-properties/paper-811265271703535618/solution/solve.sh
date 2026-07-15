#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: structural_properties.csv ===
cat > "$OUTDIR/structural_properties.csv" <<'FFEOF'
compound,a(Å),b(Å),c(Å),Ef(kJ/mol)
V3Si,4.7021,,,-44.78
VSi2,4.5597,4.5597,6.3602,-54.26
V5Si3,9.3997,,4.7252,-59.55
V6Si5,15.9126,7.4859,4.8296,-54.27
FFEOF

# === solve block: elastic_properties.csv ===
cat > "$OUTDIR/elastic_properties.csv" <<'FFEOF'
compound,C11,C12,C13,C22,C23,C33,C44,C55,C66,B(GPa),G(GPa),E(GPa),sigma,Vp(m/s),Vs(m/s),Vm(m/s)
V3Si,241.78,169.56,,,,,78.60,,,,193.64,57.52,157.01,0.364,6939.3,3154.8,3554.1
VSi2,375.46,62.70,76.39,,,426.99,144.94,,,,178.29,153.15,357.18,0.166,9060.4,5733.2,6307
V5Si3,397.23,104.46,99.91,,,341.07,104.09,,129.06,193.26,121.69,301.74,0.239,8213.4,4805.3,5328.5
V6Si5,392.70,123.69,80.59,331.60,91.74,343.01,136.12,98.89,114.54,183.71,120.16,295.95,0.232,9910.7,5858,6489.7
FFEOF

# === solve block: thermal_properties.csv ===
cat > "$OUTDIR/thermal_properties.csv" <<'FFEOF'
compound,U(kJ/mol),Cv(J/mol*K),Cp(J/mol*K),A(kJ/mol),S(J/mol*K),Theta(K),gamma,alpha(10^-5/K)
V3Si,33.96,87.19,87.79,7.35,88.69,499.87,1.768,1.31
VSi2,32.07,48.60,49.01,22.82,30.83,923.96,2.593,1.08
V5Si3,76.91,149.88,150.97,42.94,113.23,740.44,1.973,1.24
V6Si5,106.01,205.42,206.93,59.67,154.47,744.86,1.952,1.25
FFEOF
