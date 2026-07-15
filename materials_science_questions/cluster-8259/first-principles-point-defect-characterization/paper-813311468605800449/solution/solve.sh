#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_00_core_shell_frequencies.json ===
python3 -c "
import json
data = {
    'nu_O_core_shell_THz': 109.8,
    'nu_U_core_shell_THz': 133.6,
    'nutilde_O_core_shell_cm-1': 3663.76,
    'nutilde_U_core_shell_cm-1': 4457.39
}
with open('/app/outputs/step_00_core_shell_frequencies.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: step_01_vacf_highest_frequency.json ===
python3 -c "
import json
data = {
    'highest_ionic_frequency_cm-1': 760.0
}
with open('/app/outputs/step_01_vacf_highest_frequency.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: step_02_frenkel_lifetimes.json ===
python3 -c "
import math, json
k_B = 8.617333262145e-5
T = 600.0
kT = k_B * T
tau_cs = 0.01 * math.exp(0.57 / kT)
tau_ri = 0.15 * math.exp(0.30 / kT)
data = {
    'oxygen_rank5_tau_core_shell': tau_cs,
    'oxygen_rank5_tau_rigid_ion': tau_ri
}
with open('/app/outputs/step_02_frenkel_lifetimes.json', 'w') as f:
    json.dump(data, f)
"
