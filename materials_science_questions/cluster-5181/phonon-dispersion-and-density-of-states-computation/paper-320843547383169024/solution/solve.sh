#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: melting_points.json ===
python3 -c "
import json
data = {
    '27.5': {'melting_temperature_K': 900, 'error_K': 50},
    '64.5': {'melting_temperature_K': 850, 'error_K': 50},
    '99.5': {'melting_temperature_K': 350, 'error_K': 50}
}
with open('$OUTDIR/melting_points.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: phonon_frequencies.json ===
python3 -c "
import json
entries = []
# BCC at 64.5 GPa, q along [100] (Γ-H), q in units of reciprocal lattice vectors
qpts_bcc = [(0.25,0,0), (0.5,0,0), (0.75,0,0), (1.0,0,0)]
for q in qpts_bcc:
    entries.append({
        'pressure_GPa': 64.5,
        'phase': 'bcc',
        'q_point': list(q),
        'mode': 'longitudinal',
        'frequency_cm1': {0.25:145,0.5:195,0.75:175,1.0:172}[q[0]]
    })
    entries.append({
        'pressure_GPa': 64.5,
        'phase': 'bcc',
        'q_point': list(q),
        'mode': 'transverse',
        'frequency_cm1': {0.25:110,0.5:150,0.75:168,1.0:172}[q[0]]
    })
# FCC at 67 GPa, q along [110] (Γ-K) in units of reciprocal lattice vectors
qpts_fcc = [(0.25,0.25,0), (0.5,0.5,0), (0.75,0.75,0), (1.0,1.0,0)]
freqs_67 = {
    'longitudinal': [130,180,175,165],
    'transverse': [90,145,170,140]
}
for i,q in enumerate(qpts_fcc):
    entries.append({
        'pressure_GPa': 67.0,
        'phase': 'fcc',
        'q_point': list(q),
        'mode': 'longitudinal',
        'frequency_cm1': freqs_67['longitudinal'][i]
    })
    entries.append({
        'pressure_GPa': 67.0,
        'phase': 'fcc',
        'q_point': list(q),
        'mode': 'transverse',
        'frequency_cm1': freqs_67['transverse'][i]
    })
# FCC at 99.5 GPa, same q points
freqs_995 = {
    'longitudinal': [110,145,140,125],
    'transverse': [50,80,100,65]
}
for i,q in enumerate(qpts_fcc):
    entries.append({
        'pressure_GPa': 99.5,
        'phase': 'fcc',
        'q_point': list(q),
        'mode': 'longitudinal',
        'frequency_cm1': freqs_995['longitudinal'][i]
    })
    entries.append({
        'pressure_GPa': 99.5,
        'phase': 'fcc',
        'q_point': list(q),
        'mode': 'transverse',
        'frequency_cm1': freqs_995['transverse'][i]
    })
with open('$OUTDIR/phonon_frequencies.json', 'w') as f:
    json.dump(entries, f, indent=2)
"
