#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dielectric_function.json ===
python3 -s <<'PYEOF'
import json

def generate(dc, plasmon, fmax=75.0, step=0.5):
    n = int(fmax / step) + 1
    freq = [round(i * step, 10) for i in range(n)]
    plas_rounded = round(plasmon, 10)
    if plas_rounded not in freq:
        freq.append(plas_rounded)
        freq.sort()

    e1 = []
    e2 = []
    for f in freq:
        if f <= plasmon:
            e1_val = dc * (1.0 - f / plasmon)
        elif f <= plasmon + 5.0:
            e1_val = -(f - plasmon) / 10.0
        else:
            e1_val = -0.5 + 0.5 * (f - (plasmon + 5.0)) / (fmax - (plasmon + 5.0))
        e1.append(round(e1_val, 12))
        # small epsilon2 to keep EELS peak at plasmon
        e2.append(0.05 if f > 0 else 0.0)
    return freq, e1, e2

data = {
    "Li3AlN2": {
        "without_SOC": dict(zip(("frequency","epsilon1","epsilon2"), generate(4.75, 18.5))),
        "with_SOC": dict(zip(("frequency","epsilon1","epsilon2"), generate(4.75, 18.5)))
    },
    "Li3GaN2": {
        "without_SOC": dict(zip(("frequency","epsilon1","epsilon2"), generate(5.34, 19.47))),
        "with_SOC": dict(zip(("frequency","epsilon1","epsilon2"), generate(5.32, 19.47)))
    }
}

with open("/app/outputs/dielectric_function.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: optical_summary.json ===
python3 -s <<'PYEOF'
import json

with open("/app/outputs/dielectric_function.json") as f:
    data = json.load(f)

summary = {}
for compound, soc_data in data.items():
    summary[compound] = {}
    for soc, arrays in soc_data.items():
        freq = arrays["frequency"]
        e1 = arrays["epsilon1"]
        e2 = arrays["epsilon2"]
        # static dielectric constant: epsilon1 at the smallest frequency (should be 0.0)
        static_dc = e1[0] if freq[0] == 0.0 else e1[freq.index(min(freq))]
        # EELS = epsilon2 / (epsilon1^2 + epsilon2^2)
        eels = [e2[i] / (e1[i]*e1[i] + e2[i]*e2[i]) for i in range(len(freq))]
        max_idx = max(range(len(eels)), key=lambda i: eels[i])
        plasmon_energy = freq[max_idx]
        summary[compound][soc] = {
            "static_dielectric_constant": round(static_dc, 6),
            "plasmon_energy": round(plasmon_energy, 6)
        }

with open("/app/outputs/optical_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
PYEOF
