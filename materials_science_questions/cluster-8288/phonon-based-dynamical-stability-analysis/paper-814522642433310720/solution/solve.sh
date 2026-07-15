#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_energy.csv ===
cat > "$OUTDIR/step_01_formation_energy.csv" <<'EOF'
x,Delta_E_I,Delta_E_K_ion_layers,Delta_E_e_doping,Delta_E_FeSe_deformation,Delta_E_C
0.25,-0.43,0.22,1.80,0.15,-2.60
0.50,-0.75,0.45,3.10,0.20,-4.50
0.60,-0.96,0.54,3.60,0.20,-5.30
EOF

# === solve block: step_02_lattice_constants.csv ===
cat > "$OUTDIR/step_02_lattice_constants.csv" <<'EOF'
x,a_Angstrom,c_Angstrom
0.25,3.65,14.42
0.5,3.69,13.92
EOF

# === solve block: step_03_phonon_DOS_x020.json ===
cat > /tmp/gen_phonon_x020.py <<'PYEOF'
import json, math
freqs = []
dos = []
for f in range(-100, 401, 5):
    freqs.append(float(f))
    d = 0.0
    if f < 0:
        d = 0.1 * math.exp(-(f+30)**2 / 200)
    else:
        d = 0.05 * math.exp(-(f-50)**2 / 800) + 0.1 * math.exp(-(f-200)**2 / 2000)
    dos.append(round(d, 5))
data = {'frequencies_cm-1': freqs, 'dos': dos}
with open('/app/outputs/step_03_phonon_DOS_x020.json', 'w') as f:
    json.dump(data, f)
PYEOF
python3 /tmp/gen_phonon_x020.py

# === solve block: step_04_phonon_DOS_x025.json ===
cat > /tmp/gen_phonon_x025.py <<'PYEOF'
import json, math
freqs = []
dos = []
for f in range(0, 401, 5):
    freqs.append(float(f))
    d = 0.1 * math.exp(-(f-55)**2 / 600) + 0.12 * math.exp(-(f-210)**2 / 1800)
    dos.append(round(d, 5))
data = {'frequencies_cm-1': freqs, 'dos': dos}
with open('/app/outputs/step_04_phonon_DOS_x025.json', 'w') as f:
    json.dump(data, f)
PYEOF
python3 /tmp/gen_phonon_x025.py

# === solve block: step_05_Fe_vacancy_energy.csv ===
cat > "$OUTDIR/step_05_Fe_vacancy_energy.csv" <<'EOF'
x,Delta_E_Fe_vacancy
0.8,-1.5
EOF

# === solve finalize ===
echo "All reference artifacts written."
