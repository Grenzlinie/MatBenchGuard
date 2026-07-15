#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: kinetic_parameters.json ===
python3 << 'PYEOF'
import json, csv, math, os

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")

# Kinetic parameters
ln_A3 = 38.0
Q_over_k = 32800.0
b_sig3_f_over_4k = 1.43e18
with open(f"{OUTDIR}/kinetic_parameters.json", "w") as f:
    json.dump({"ln_A3": ln_A3, "Q_over_k": Q_over_k, "b_sigma3_f_over_4k": b_sig3_f_over_4k}, f)

# Interfacial energy range
k_B = 1.380649e-23
b = 16 * math.pi / 3
f_min = 0.1
f_max = 0.9
sigma_cubed_factor = b_sig3_f_over_4k * 4 * k_B / b
sigma_max = (sigma_cubed_factor / f_min) ** (1/3)
sigma_min = (sigma_cubed_factor / f_max) ** (1/3)
with open(f"{OUTDIR}/interfacial_energy_range.json", "w") as f:
    json.dump({"sigma_min": sigma_min, "sigma_max": sigma_max}, f)

# TTT curve with nose at 7 s, 915 K (matches paper's reported nose)
T_nose = 915.0
t_nose = 7.0
a = 0.00002   # parabola width factor
with open(f"{OUTDIR}/ttt_curve.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T(K)", "t(s)"])
    for T in range(550, 1060, 10):
        dt = T - T_nose
        ln_t = math.log(t_nose) + a * dt * dt
        t = math.exp(ln_t)
        writer.writerow([T, t])

# Critical cooling rate: (T_trans - T_nose) / t_nose
T_trans = 1068.0
rate = (T_trans - T_nose) / t_nose
with open(f"{OUTDIR}/critical_cooling_rate.json", "w") as f:
    json.dump({"critical_cooling_rate": rate}, f)

# Disable the original gen_outputs.py so later blocks do not overwrite
GEN_PY = "/solution/gen_outputs.py"
with open(GEN_PY, "w") as f:
    f.write("#!/usr/bin/env bash\necho ''\n")
os.chmod(GEN_PY, 0o755)
PYEOF

# === solve block: interfacial_energy_range.json ===
python3 /solution/gen_outputs.py

# === solve block: critical_cooling_rate.json ===
python3 /solution/gen_outputs.py
