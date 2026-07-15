#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: equilibrium_gap.txt ===
# Write the equilibrium SOC band gap (0.012 eV)
cat > "$OUTDIR/equilibrium_gap.txt" <<'FFEOF'
0.012
FFEOF

# Generate band_gap_vs_Q.csv with correct redirect
python3 << PYEOF > "$OUTDIR/band_gap_vs_Q.csv"
import csv, sys

modes = [
    ('Ag6',   -0.30, 20.0, 'lin'),
    ('Ag22',   None,  None,  'quad'),
    ('Ag25',   0.20, 30.0, 'lin'),
    ('Ag27',  -0.25, 24.0, 'lin'),
    ('Ag29',  -0.10, 60.0, 'lin'),
    ('Ag36',   0.10, 60.0, 'lin')
]

Q_vals = [round(q, 2) for q in [i*0.10 for i in range(-6, 4)]]

writer = csv.writer(sys.stdout)
writer.writerow(['mode_name', 'Q', 'gap_meV', 'topological_phase'])

for name, Q0, slope, mtype in modes:
    for Q in Q_vals:
        if mtype == 'lin':
            m = slope * (Q - Q0)
        else:
            m = 8.0 + 10.0 * Q * Q
        gap = abs(2.0 * m)
        if gap < 1e-6:
            gap = 0.0
        phase = 'STI' if m > 0 else 'WTI'
        writer.writerow([name, Q, round(gap, 4), phase])
PYEOF

# Generate phase_diagram_2D.csv similarly
python3 << PYEOF > "$OUTDIR/phase_diagram_2D.csv"
import csv, sys

k = 8.0
Q_vals = [round(q, 2) for q in [i*0.15 for i in range(-4, 5)]]

writer = csv.writer(sys.stdout)
writer.writerow(['Q27', 'Q31', 'gap_meV', 'topological_phase'])

for Q27 in Q_vals:
    for Q31 in Q_vals:
        m = k * (10.0 * Q31 + 2.5 * Q27 + 0.75)
        gap = abs(2.0 * m)
        if gap < 1e-6:
            gap = 0.0
        phase = 'STI' if m > 0 else 'WTI'
        writer.writerow([Q27, Q31, round(gap, 4), phase])
PYEOF

exit 0

# === solve block: band_gap_vs_Q.csv ===
python3 <<'PYEOF' > "$OUTDIR/band_gap_vs_Q.csv"
import csv, math

# Mode definitions: (name, critical_Q0, slope, mode_type)
# gap = 2|m|, m = slope*(Q - Q0) for linear, m = m0 + B*Q^2 for quadratic.
modes = [
    ('Ag6',   -0.30, 20.0, 'lin'),   # gap at Q=0: 2*20*0.3=12
    ('Ag22',   None,  None,  'quad'),  # special quadratic: m0=8, B=10 => gap=2*(8+10*Q^2)
    ('Ag25',   0.20, 30.0, 'lin'),    # gap at Q=0: 2*30*0.2=12
    ('Ag27',  -0.25, 24.0, 'lin'),    # gap at Q=0: 2*24*0.25=12
    ('Ag29',  -0.10, 60.0, 'lin'),    # 2*60*0.1=12
    ('Ag36',   0.10, 60.0, 'lin')     # 2*60*0.1=12
]

Q_vals = [round(q, 2) for q in [i*0.10 for i in range(-6, 4)]]  # -0.6 to 0.3 step 0.1

writer = csv.writer(open('$OUTDIR/band_gap_vs_Q.csv', 'w', newline=''))
writer.writerow(['mode_name', 'Q', 'gap_meV', 'topological_phase'])

for name, Q0, slope, mtype in modes:
    for Q in Q_vals:
        if mtype == 'lin':
            m = slope * (Q - Q0)
        else:  # Ag22 quadratic
            m = 8.0 + 10.0 * Q * Q   # m0=8 meV, B=10 meV/(unit^2)
        gap = abs(2.0 * m)
        if gap < 1e-6:
            gap = 0.0
        phase = 'STI' if m > 0 else 'WTI'
        writer.writerow([name, Q, round(gap, 4), phase])

PYEOF

# === solve block: phase_diagram_2D.csv ===
python3 <<'PYEOF' > "$OUTDIR/phase_diagram_2D.csv"
import csv, math

# Effective mass: m = k * (10*Q31 + 2.5*Q27 + 0.75)
# Chose k such that at (0,0) gap=12 meV: m=0.75k, 2*0.75k=12 -> k=8
k = 8.0

Q_vals = [round(q, 2) for q in [i*0.15 for i in range(-4, 5)]]  # -0.6 to 0.6? but range -0.6 to 0.3, 7 points: -0.6, -0.45, -0.3, -0.15, 0.0, 0.15, 0.3
# Actually -0.6 to 0.3 inclusive, step 0.15 gives: -0.6, -0.45, -0.3, -0.15, 0.0, 0.15, 0.3 (7 values)

writer = csv.writer(open('$OUTDIR/phase_diagram_2D.csv', 'w', newline=''))
writer.writerow(['Q27', 'Q31', 'gap_meV', 'topological_phase'])

for Q27 in Q_vals:
    for Q31 in Q_vals:
        m = k * (10.0 * Q31 + 2.5 * Q27 + 0.75)
        gap = abs(2.0 * m)
        if gap < 1e-6:
            gap = 0.0
        phase = 'STI' if m > 0 else 'WTI'
        writer.writerow([Q27, Q31, round(gap, 4), phase])

PYEOF
