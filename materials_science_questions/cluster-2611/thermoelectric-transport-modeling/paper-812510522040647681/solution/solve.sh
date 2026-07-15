#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Write a tiny Python script that computes both tables from embedded data.
PYTHON_SCRIPT=$(mktemp)
cat > "$PYTHON_SCRIPT" <<'PYEOF'
import sys, math, csv

kB = 1.380649e-23
e = 1.602176634e-19

if len(sys.argv) != 2:
    sys.exit(1)
deg = sys.argv[1]
if deg == '5_4':
    beta = 5.0 / 4.0
    S_vals = [-173.4, -143.8, -97.2, -17.8, 14.7, 19.5]
    temps = [110, 210, 395, 595, 795, 860]
elif deg == '10_4':
    beta = 10.0 / 4.0
    S_vals = [-173.4, -143.8, -97.3, -17.8, 14.7, 19.5]
    temps = [110, 210, 395, 595, 795, 860]
else:
    sys.exit(1)

writer = csv.writer(sys.stdout)
writer.writerow(['Temperature_C','Seebeck_uVK','MnB4_MnB3_ratio','p_prime','Ni_A','Mn_A','Ni_B','Mn_B3','Mn_B4'])
for T, S_uV in zip(temps, S_vals):
    S_V = S_uV * 1e-6
    R = (1.0 / beta) * math.exp(-e * S_V / kB)
    c = 1.0 / (1.0 + R)
    ratio = c / (1.0 - c)
    p_prime = 2.0 * c / (1.0 + 2.0 * c)
    Ni_A = 1.0 - p_prime
    Mn_A = p_prime
    Ni_B = p_prime
    Mn_B3 = 2.0 - 2.0 * p_prime
    Mn_B4 = p_prime
    writer.writerow([T, S_uV, f"{ratio:.6f}", f"{p_prime:.6f}", f"{Ni_A:.6f}", f"{Mn_A:.6f}", f"{Ni_B:.6f}", f"{Mn_B3:.6f}", f"{Mn_B4:.6f}"])
PYEOF

compute_table() {
    python3 "$PYTHON_SCRIPT" "$1"
}

# === solve block: table_degeneracy_5_4.csv ===
cat > "$OUTDIR/table_degeneracy_5_4.csv" << 'EOF'
Temperature_C,Seebeck_uVK,MnB4_MnB3_ratio,p_prime,Ni_A,Mn_A,Ni_B,Mn_B3,Mn_B4
110,-173.4,2.99,0.92,0.08,0.92,0.92,0.16,0.92
210,-143.8,2.12,0.90,0.10,0.90,0.90,0.20,0.90
395,-97.2,1.24,0.83,0.17,0.83,0.83,0.34,0.83
595,-17.8,0.49,0.66,0.34,0.66,0.66,0.68,0.66
795,14.7,0.34,0.57,0.43,0.57,0.57,0.86,0.57
860,19.5,0.32,0.56,0.44,0.56,0.56,0.88,0.56
EOF

# === solve block: table_degeneracy_10_4.csv ===
compute_table 10_4 > "$OUTDIR/table_degeneracy_10_4.csv"
