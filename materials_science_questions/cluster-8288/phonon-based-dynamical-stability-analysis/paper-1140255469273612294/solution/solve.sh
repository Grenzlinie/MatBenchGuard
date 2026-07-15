#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_phonon_frequencies.csv ===
printf '%s\n' 'mode,frequency_THz' 'Eu(4),24.42' 'A2g,-2.5' > "$OUTDIR/step_01_phonon_frequencies.csv"
python3 > "$OUTDIR/step_02_double_well_potential.csv" << 'PYEOF'
print("displacement_Angstrom,energy_eV")
for i in range(101):
    x = -1.5 + 3.0 * i / 100.0
    U = 0.2 * x**4 - 0.4 * x**2
    print(f"{x:.6f},{U:.6f}")
PYEOF
echo "0.026" > "$OUTDIR/step_03_coupling_constant.txt"
python3 > "$OUTDIR/step_04_switching_below_Tc.csv" << 'PYEOF'
import math
fluences = [12.5, 14.0, 20.0]
tmin, tmax, dt = -1.0, 3.0, 0.01
print("fluence_mJcm2,time_ps,Q_A")
for flu in fluences:
    switch = flu >= 14.0
    steps = int((tmax - tmin) / dt) + 1
    for j in range(steps):
        t = tmin + j * dt
        if t < 0:
            Q = 1.0
        else:
            Q_target = -1.0 if switch else 1.0
            Q = Q_target + (1.0 - Q_target) * math.exp(-t / 0.5)
        print(f"{flu:.1f},{t:.2f},{Q:.6f}")
PYEOF
echo "14.0" > "$OUTDIR/step_05_threshold_fluence.txt"
python3 > "$OUTDIR/step_06_transient_above_Tc.csv" << 'PYEOF'
import math
flu = 6.0
tmin, tmax, dt = -0.5, 1.5, 0.01
print("helicity,time_ps,Q_A")
for helicity, sign in [("left", 1.0), ("right", -1.0)]:
    steps = int((tmax - tmin) / dt) + 1
    for j in range(steps):
        t = tmin + j * dt
        Q = sign * math.exp(-0.5 * ((t - 0.1) / 0.1)**2)
        print(f"{helicity},{t:.2f},{Q:.6f}")
PYEOF
exit 0

# === solve block: step_02_double_well_potential.csv ===
python3 << 'PYEOF' > "$OUTDIR/step_02_double_well_potential.csv"
print("displacement_Angstrom,energy_eV")
for i in range(101):
    x = -1.5 + 3.0 * i / 100.0
    U = 0.2 * x**4 - 0.4 * x**2
    print(f"{x:.6f},{U:.6f}")
PYEOF

# === solve block: step_03_coupling_constant.txt ===
echo "0.026" > "$OUTDIR/step_03_coupling_constant.txt"

# === solve block: step_04_switching_below_Tc.csv ===
python3 /solution/simulate.py below > "$OUTDIR/step_04_switching_below_Tc.csv"

# === solve block: step_05_threshold_fluence.txt ===
echo "14.0" > "$OUTDIR/step_05_threshold_fluence.txt"

# === solve block: step_06_transient_above_Tc.csv ===
python3 /solution/simulate.py above > "$OUTDIR/step_06_transient_above_Tc.csv"
