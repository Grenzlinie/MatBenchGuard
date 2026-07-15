#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
# Oracle: write reference adhesion energy artifacts
mkdir -p /app/outputs

# === solve block: beta_in_vacuo.csv ===
cat > /app/outputs/beta_in_vacuo.csv <<'FFEOF'
surface,density_nm2,beta_J_m2
A(100),2.2,-1.56
A(100),3.3,-1.48
A(100),4.4,-1.40
R(110),2.2,-1.27
R(110),3.3,-1.18
R(110),4.4,-1.10
A(011),2.2,-1.20
A(011),3.3,-1.10
A(011),4.4,-1.00
R(100),2.2,-1.15
R(100),3.3,-1.05
R(100),4.4,-0.98
R(011),2.2,-1.12
R(011),3.3,-1.02
R(011),4.4,-0.95
A(110),2.2,-1.10
A(110),3.3,-1.00
A(110),4.4,-0.95
R(001),2.2,-1.05
R(001),3.3,-0.95
R(001),4.4,-0.90
A(001),2.2,-0.90
A(001),3.3,-0.85
A(001),4.4,-0.80
FFEOF

# === solve block: beta_water_modified.csv ===
cat > /app/outputs/beta_water_modified.csv <<'FFEOF'
surface,density_nm2,beta_prime_J_m2
A(100),2.2,-0.50
A(100),3.3,-0.45
A(100),4.4,-0.40
R(110),2.2,-0.30
R(110),3.3,-0.28
R(110),4.4,-0.25
A(011),2.2,-0.28
A(011),3.3,-0.22
A(011),4.4,-0.20
R(100),2.2,-0.27
R(100),3.3,-0.22
R(100),4.4,-0.20
R(011),2.2,-0.26
R(011),3.3,-0.21
R(011),4.4,-0.19
A(110),2.2,-0.25
A(110),3.3,-0.20
A(110),4.4,-0.18
R(001),2.2,-0.20
R(001),3.3,-0.18
R(001),4.4,-0.15
A(001),2.2,-0.05
A(001),3.3,-0.03
A(001),4.4,-0.01
FFEOF
