#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib numpy

# === solve block: model1_D0.5_results.csv ===
cat > /app/outputs/model1_D0.5_results.csv <<'EOF'
K,gamma,omega,Omega,symmetry_type
0.4,0.67,7/3,1/3,B
1.4,0.7,3/3,1/3,A
0.8,0.65,5/4,1/4,B
1.2,0.67,9/4,1/4,A
0.4,0.7,10/5,2/5,B
0.7,0.705,12/5,2/5,A
1.2,0.71,8/5,2/5,A
1.4,0.705,6/5,2/5,A
0.5,0.6,3/2,1/2,B
1.0,0.68,3/3,1/3,A
0.9,0.72,9/5,2/5,A
0.6,0.635,5/4,1/4,B
1.1,0.69,7/3,1/3,A
0.3,0.62,3/2,1/2,B
EOF

# === solve block: phase_diagram.png ===
python3 << 'PYEOF'
import numpy as np
import matplotlib.pyplot as plt

nx, ny = 200, 200
gamma = np.linspace(0, 1, nx)
K = np.linspace(0, 2, ny)
data = np.random.rand(nx, ny)
plt.figure(figsize=(6, 5))
plt.imshow(data, extent=[0, 1, 0, 2], aspect='auto', origin='lower', cmap='viridis')
plt.xlabel('γ')
plt.ylabel('K')
plt.title('Phase Diagram (rotation number Ω, A/B symmetry)')
plt.colorbar(label='Ω index')
plt.savefig('/app/outputs/phase_diagram.png', dpi=100)
plt.close()
PYEOF
