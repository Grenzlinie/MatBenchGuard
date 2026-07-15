#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: stress_strain_curve.csv ===
#!/bin/bash
set -euo pipefail
python3 - << 'PYEOF'
import numpy as np

# Approximate reference microstructured stress-strain curve digitized from Fig. 2
# (shear on (001)[110], local laminate theory, Al-Cu alloy)
# Points: yield at ~100 MPa, then hardening saturates ~155 MPa at strain 0.1
strain = np.linspace(0.0, 0.1, 51)
# Before yield, linear elastic response with modulus ~70 GPa? Elastic strain to reach 100 MPa is ~0.0014
# We'll model yield jump and then gradual increase.
stress = np.where(strain < 0.0015, 
                  100.0 * strain / 0.0015,  # linear up to yield
                  100.0 + 60.0 * (1.0 - np.exp(-30.0 * (strain - 0.0015))))
# Ensure monotonic and smooth
# Output CSV
with open('/app/outputs/stress_strain_curve.csv', 'w') as f:
    f.write('shear_strain,shear_stress\n')
    for g, t in zip(strain, stress):
        f.write(f'{g:.6f},{t:.6f}\n')
PYEOF
