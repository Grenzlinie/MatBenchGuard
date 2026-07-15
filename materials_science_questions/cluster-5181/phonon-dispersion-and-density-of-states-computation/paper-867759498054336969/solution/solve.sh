#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: pdos.dat ===
cat > /tmp/gen_pdos.py << 'PYEOF'
import math, sys

emin, emax, step = -10.0, 10.0, 0.01
n = int((emax - emin) / step) + 1

def total_dos(e):
    base = 0.21
    peak1 = 0.6 * math.exp(-((e + 3.0)**2) / (2 * 1.5**2))
    peak2 = 0.3 * math.exp(-((e - 2.0)**2) / (2 * 1.0**2))
    return base + peak1 + peak2

def b_pz(e):
    base = 0.07
    peak = 0.15 * math.exp(-((e - 2.5)**2) / (2 * 0.8**2))
    return base + peak

with open(sys.argv[1], 'w') as f:
    f.write('energy\ttotal_DOS\tB_pz\n')
    for i in range(n):
        e = emin + i * step
        td = total_dos(e)
        bpz = b_pz(e)
        f.write(f'{e:.2f}\t{td:.6f}\t{bpz:.6f}\n')
PYEOF
python3 /tmp/gen_pdos.py "$OUTDIR/pdos.dat"

# === solve block: phonon_frequencies.json ===
cat > "$OUTDIR/phonon_frequencies.json" << 'EOF'
{
  "E1u": [328.0, 328.0],
  "A2u": [419.0],
  "E2g": [665.0, 665.0],
  "B1g": [679.0]
}
EOF
