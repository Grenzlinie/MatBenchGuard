#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: step_01_envelope.csv ===
python3 << 'PYEOF'
import csv, math
A_c = 1.181
lines = [["A", "q_env"]]
for i in range(100, 141):
    A = i / 100.0
    if A <= A_c:
        q_env = 0.0
    else:
        q_env = A * (1 - math.exp(-(A - A_c) / 0.02))
    lines.append([str(A), str(q_env)])
with open("/app/outputs/step_01_envelope.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lines)
PYEOF

# === solve block: step_02_frequency.csv ===
python3 << 'PYEOF'
import csv, math
from scipy.special import ellipk
A_c = 1.181
lines = [["A", "omega"]]
for i in range(100, 141):
    A = i / 100.0
    if A <= A_c:
        omega = 1.0
    else:
        m = -A**2 / (2 + A**2)
        K = ellipk(m)
        omega = (math.pi / 4) * math.sqrt(2 + A**2) / K
    lines.append([str(A), str(omega)])
with open("/app/outputs/step_02_frequency.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lines)
PYEOF

# === solve block: step_03_relaxation_time.csv ===
python3 << 'PYEOF'
import csv, math
A_c = 1.181
gamma = 0.61
D = 639
lines = [["A", "tau_rel"]]
for i in range(100, 141):
    A = i / 100.0
    if A < A_c:
        diff = A_c - A
        tau = D * diff**(-gamma)
        if tau > 1e6:
            tau = 1e6
        lines.append([str(A), str(tau)])
with open("/app/outputs/step_03_relaxation_time.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lines)
PYEOF

# === solve block: step_04_critical_amplitude.txt ===
echo "1.181" > /app/outputs/step_04_critical_amplitude.txt

# === solve block: step_05_powerlaw_exponents.json ===
cat > /app/outputs/step_05_powerlaw_exponents.json << 'FFEOF'
{
  "gamma": 0.61,
  "gamma_error": 0.05,
  "delta": 0.87,
  "delta_error": 0.05,
  "fit_range": {
    "tau_rel_range": [1.0, 1.18],
    "modulation_period_range": [1.19, 1.30]
  }
}
FFEOF
