#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_scaling_data.csv ===
cat > "$OUTDIR/step_01_scaling_data.csv" <<'FFEOF'
network_config,N_p,total_energy,var_local_energy
"(4,64,2,16)",257474,-232.2321,0.3665
"(4,96,2,24)",549026,-232.23994,0.1972
"(4,128,4,32)",949122,-232.24422,0.1304
"(4,256,4,32)",2879618,-232.24689,0.07033
"(4,408,4,48)",7115954,-232.24877,0.04618
"(4,512,8,64)",11329794,-232.24947,0.03262
"(8,512,8,128)",22633986,-232.25025,0.02318
FFEOF

# === solve block: step_02_fit_results.json ===
python3 <<'PYEOF'
import csv, json, math
import numpy as np

rows = []
with open('/app/outputs/step_01_scaling_data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

N_p = np.array([int(r['N_p']) for r in rows])
energies = np.array([float(r['total_energy']) for r in rows])
variances = np.array([float(r['var_local_energy']) for r in rows])

# variance-energy linear fit E = k * V + E_SE
slope_v, intercept_v = np.polyfit(variances, energies, 1)
E_SE = intercept_v

# power-law fit: E - E_SE = alpha * N_p^{-beta}  =>  log10(residual) = log10(alpha) - beta * log10(N_p)
residuals = energies - E_SE
log_res = np.log10(residuals)
log_Np = np.log10(N_p)
coeffs = np.polyfit(log_Np, log_res, 1)   # coeffs[0] = -beta, coeffs[1] = log10(alpha)
beta = -coeffs[0]
alpha = 10**coeffs[1]

output = {
    "power_law": {
        "alpha": alpha,
        "beta": beta,
        "E_SE": E_SE
    },
    "variance_energy": {
        "slope": slope_v,
        "intercept": intercept_v
    }
}

with open('/app/outputs/step_02_fit_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Fits computed and written.")
PYEOF
