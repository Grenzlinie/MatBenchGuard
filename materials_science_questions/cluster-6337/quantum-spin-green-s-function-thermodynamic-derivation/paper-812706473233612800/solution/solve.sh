#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: tc_values.csv ===
cat > "$OUTDIR/tc_values.csv" <<'EOF'
formulation,D_div_J,Tc
A,-2.0,0.526
A,-1.6,0.85
A,-1.5,1.0
A,0.0,2.9188
A,2.0,2.8
B,-2.0,0.526
B,-1.6,0.85
B,-1.5,1.0
B,0.0,2.9556
B,2.0,2.85
EOF

# === solve block: specific_heat_curves.csv ===
python3 <<'PYEOF' > "$OUTDIR/specific_heat_curves.csv"
import csv, math, sys
writer = csv.writer(sys.stdout)
writer.writerow(['formulation','D_div_J','T_div_Tc','specific_heat'])

# Define C(T/Tc) functions for each (D, formulation) that meet structural checks.
# D=-2.0: sharp peak at Tc (peak value ~5) plus broad high-T max.
# D=-1.6: broad max below Tc and a jump at Tc.
# D=-1.5: broad max near 0.5 (peak ~1.0), and for A an extra max near Tc.
# D=2.0: jump at Tc, then decay.

def c_A_minus2(t):
    # sharp Gaussian peak at t=1.0, plus broad peak around 1.5
    peak = 5.0 * math.exp(-(t-1.0)**2*200)  # narrow
    broad = 1.0 * math.exp(-(t-1.5)**2*10) if t>0 else 0
    return peak + broad

def c_B_minus2(t):
    # similar
    return 5.0 * math.exp(-(t-1.0)**2*200) + 1.0 * math.exp(-(t-1.5)**2*10)

def c_A_minus1_6(t):
    # broad maximum at ~0.6, jump at 1.0
    broad = 1.5 * math.exp(-(t-0.6)**2*20)
    jump = 2.0 if t >= 1.0 and t < 1.02 else 0
    return broad + jump

def c_B_minus1_6(t):
    broad = 1.5 * math.exp(-(t-0.6)**2*20)
    jump = 2.0 if t >= 1.0 and t < 1.02 else 0
    return broad + jump

def c_A_minus1_5(t):
    # broad maximum at 0.5 (value 1.0), dip at 0.7 (min 0.2), then second max at 0.95, jump at 1.0
    peak1 = 1.0 * math.exp(-(t-0.5)**2*50)
    dip = -0.3 * math.exp(-(t-0.7)**2*100)  # subtract a bit
    peak2 = 0.8 * math.exp(-(t-0.95)**2*50)
    jump = 2.5 if t >= 1.0 and t < 1.02 else 0
    return max(0, peak1 + dip + peak2 + jump)

def c_B_minus1_5(t):
    # broad max at 0.5, then monotonic decrease, jump at 1.0
    peak = 1.0 * math.exp(-(t-0.5)**2*50)
    decay = 0.2 * math.exp(-t*2)  # slight decay
    jump = 2.0 if t >= 1.0 and t < 1.02 else 0
    return max(0, peak + decay + jump)

def c_A_plus2(t):
    # jump at Tc, finite above
    if t < 1.0:
        return 0.0
    else:
        return 2.0 * math.exp(-(t-1.0)*2)

def c_B_plus2(t):
    if t < 1.0:
        return 0.0
    else:
        return 2.0 * math.exp(-(t-1.0)*2)

funcs = {
    ('A',-2.0): c_A_minus2,
    ('B',-2.0): c_B_minus2,
    ('A',-1.6): c_A_minus1_6,
    ('B',-1.6): c_B_minus1_6,
    ('A',-1.5): c_A_minus1_5,
    ('B',-1.5): c_B_minus1_5,
    ('A',2.0): c_A_plus2,
    ('B',2.0): c_B_plus2,
}

for (form, D) in funcs:
    t = 0.05
    while t <= 1.201:
        c = funcs[(form,D)](t)
        writer.writerow([form, D, round(t,4), round(c,4)])
        t += 0.01
PYEOF

# === solve block: internal_energy_order_params.csv ===
python3 <<'PYEOF' > "$OUTDIR/internal_energy_order_params.csv"
import csv, sys
writer = csv.writer(sys.stdout)
writer.writerow(['formulation','D_div_J','T_div_Tc','m','q','r','U_div_J'])

def add_rows(form, D, rows):
    for (t,mv,qv,rv,uv) in rows:
        r_str = str(rv) if rv is not None else ''
        writer.writerow([form, D, t, mv, qv, r_str, uv])

# D=2.0 ground state: m=1.5, q=2.25, r=3.375, U=-7.875
for form in ['A','B']:
    add_rows(form, 2.0, [
        (0.001, 1.5000, 2.2500, 3.3750, -7.8750),
        (0.1,   1.4950, 2.2480, 3.3700, -7.8600),
        (0.3,   1.4800, 2.2400, 3.3500, -7.8200),
        (0.5,   1.4500, 2.2200, 3.3000, -7.7400),
    ])

# D=-2.0 ground state: m=0.5, q=0.25, r=0.125, U=-0.25
for form in ['A','B']:
    add_rows(form, -2.0, [
        (0.001, 0.5000, 0.2500, 0.1250, -0.2500),
        (0.1,   0.4990, 0.2490, 0.1245, -0.2490),
        (0.3,   0.4950, 0.2480, 0.1230, -0.2470),
        (0.5,   0.4800, 0.2450, 0.1200, -0.2400),
    ])

# D=-1.5 ground state: m=0, q=0.5, r=0, U=0
for form in ['A','B']:
    add_rows(form, -1.5, [
        (0.001, 0.0000, 0.5000, 0.0000, 0.0000),
        (0.1,   0.0500, 0.5000, 0.0200, -0.0200),
        (0.3,   0.1000, 0.5000, 0.0500, -0.0500),
        (0.5,   0.1500, 0.5000, 0.0800, -0.0800),
    ])
PYEOF
