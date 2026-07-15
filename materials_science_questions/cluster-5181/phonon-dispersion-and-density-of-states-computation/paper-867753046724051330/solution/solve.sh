#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: step_01_optimized_structure.txt ===
cat > "$OUTDIR/step_01_optimized_structure.txt" <<'FFEOF'
a = 5.8164 Angstrom
b = 5.8167 Angstrom
c = 8.2271 Angstrom
beta = 90.0 degrees
FFEOF

# === solve block: step_02_phonon_frequencies.json ===
python3 -c "
import json

theo = [103.7, 107.7, 128.7, 226.2, 228.5, 294.3, 333.7, 346.3, 381.8, 617.5, 621.5, 659.8, 667.0, 756.4, 788.6]
exp  = [95.6, 99.1, 127.2, 221.8, 223.9, 285.0, 326.6, 337.8, 371.0, 554.6, 561.7, 568.5, 588.8, 685.2, 732.1]
ref = [102.5, 106.5, 130, 216.8, 227.6, 289.5, 324.2, 349.7, 397.6, 561.7, 580.4, 711, 734.7, 773.5, 785.5]

def aard(vals, ref):
    s = sum(abs(v - r) / r for v, r in zip(vals, ref))
    return (100.0 / len(ref)) * s

data = {
    'theoretical_lattice_constants_frequencies': theo,
    'experimental_lattice_constants_frequencies': exp,
    'aard_theoretical': aard(theo, ref),
    'aard_experimental': aard(exp, ref),
}

with open('$OUTDIR/step_02_phonon_frequencies.json', 'w') as f:
    json.dump(data, f, indent=2)
"
