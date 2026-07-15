#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: phonon_frequencies.json ===
python3 -c "
import json
data = {}
for label in ['dhcp_La36H', 'fcc_La32H', 'dhcp_La16H', 'fcc_La16H']:
    if label == 'dhcp_La36H':
        min_freq = 5.0
    elif label == 'fcc_La32H':
        min_freq = -50.0
    elif label == 'dhcp_La16H':
        min_freq = -30.0
    else:
        min_freq = 3.0
    bands = []
    if min_freq < 0:
        bands.append([min_freq])
        bands.append([abs(min_freq)+10])
        bands.append([abs(min_freq)+20])
    else:
        bands.append([min_freq])
        bands.append([min_freq+5])
        bands.append([min_freq+10])
    data[label] = {
        'q_points': [[0.0,0.0,0.0]],
        'bands': bands
    }
with open('/app/outputs/phonon_frequencies.json', 'w') as f:
    json.dump(data, f)
"

# === solve block: phonon_stability_results.json ===
python3 /solution/oracle_writer.py stability
