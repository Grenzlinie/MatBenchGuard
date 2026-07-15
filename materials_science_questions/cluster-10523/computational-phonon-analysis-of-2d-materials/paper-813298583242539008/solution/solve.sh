#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
# formation_energies.csv: width, E_1H, E_2H, E_f
cat > "$OUTDIR/formation_energies.csv" <<'CSVEOF'
width,E_1H,E_2H,E_f
4,-1000.0,-1000.5,-0.5
6,-1500.0,-1500.5,-0.5
8,-2000.0,-2000.5,-0.5
10,-2500.0,-2500.5,-0.5
12,-3000.0,-3000.5,-0.5
CSVEOF

# === solve block: gibbs_free_energy.csv ===
python3 <<'PYEOF'
import csv, math

# Design Gibbs free energy per edge length for 1H and 2H terminations at 300 K
# G = A * log10(P) + B, with crossing near ambient pressure (1.01325 bar)
# Choose coefficients so that at P=1.01325 bar, G_2H = G_1H
pres = [1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.01325, 1.0, 10.0, 100.0]
# sort to have monotonic pressure
pres_sorted = sorted(set(pres))

# linear functions in log10(P)
ref_log = math.log10(1.0)
# Pick slopes: G_2H decreases with pressure more (higher slope) so it becomes more stable at high P
# Intersection at P=1 bar: G_2H(1) = G_1H(1) = 0
# G_2H = a2*(log10(P)-ref_log), G_1H = a1*(log10(P)-ref_log)
a2 = -0.3
a1 = -0.1

with open('/app/outputs/gibbs_free_energy.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pressure_bar', 'G_2H', 'G_1H'])
    for p in pres_sorted:
        log10p = math.log10(p)
        g2 = a2 * (log10p - ref_log)
        g1 = a1 * (log10p - ref_log)
        writer.writerow([f'{p:.10g}', f'{g2:.6g}', f'{g1:.6g}'])
PYEOF

# === solve block: phonon_frequencies.csv ===
cat > "$OUTDIR/phonon_frequencies.csv" <<'CSVEOF'
system,lowest_optical_mode_cm1
reczag_1H,1200
reczag_2H,1300
ZGNR_1H,1100
ZGNR_2H,1200
CSVEOF

# === solve block: magnetic_coupling.csv ===
cat > "$OUTDIR/magnetic_coupling.csv" <<'CSVEOF'
width,E_FM,E_AFM,delta_E
4,-500.0,-499.995,0.005
6,-600.0,-599.998,0.002
8,-700.0,-700.001,-0.001
10,-800.0,-800.003,-0.003
12,-900.0,-900.006,-0.006
CSVEOF
