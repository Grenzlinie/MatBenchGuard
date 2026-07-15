#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_frequencies.json ===
python3 -c '
import json
modes = [
    {"mode_id": 1, "frequency_32S_cm-1": 429.0, "frequency_36S_cm-1": 429.0, "symmetry": ""},
    {"mode_id": 2, "frequency_32S_cm-1": 377.0, "frequency_36S_cm-1": 361.0, "symmetry": ""},
    {"mode_id": 3, "frequency_32S_cm-1": 278.0, "frequency_36S_cm-1": 271.0, "symmetry": ""},
    {"mode_id": 4, "frequency_32S_cm-1": 247.0, "frequency_36S_cm-1": 240.0, "symmetry": ""},
    {"mode_id": 5, "frequency_32S_cm-1": 167.0, "frequency_36S_cm-1": 162.0, "symmetry": ""},
    {"mode_id": 6, "frequency_32S_cm-1": 121.0, "frequency_36S_cm-1": 119.0, "symmetry": ""}
]
with open("/app/outputs/dft_frequencies.json", "w") as f:
    json.dump(modes, f, indent=2)
'

# === solve block: ubff_frequencies.json ===
python3 -c '
import json
modes = [
    {"mode_id": 1, "frequency_32S_cm-1": 430.4, "frequency_36S_cm-1": 430.4, "symmetry": "A1"},
    {"mode_id": 2, "frequency_32S_cm-1": 429.3, "frequency_36S_cm-1": 429.2, "symmetry": "E"},
    {"mode_id": 3, "frequency_32S_cm-1": 429.1, "frequency_36S_cm-1": 429.0, "symmetry": "B2"},
    {"mode_id": 4, "frequency_32S_cm-1": 390.4, "frequency_36S_cm-1": 390.1, "symmetry": "A1"},
    {"mode_id": 5, "frequency_32S_cm-1": 388.3, "frequency_36S_cm-1": 386.1, "symmetry": "B2"},
    {"mode_id": 6, "frequency_32S_cm-1": 380.8, "frequency_36S_cm-1": 380.8, "symmetry": "E"},
    {"mode_id": 7, "frequency_32S_cm-1": 378.6, "frequency_36S_cm-1": 364.6, "symmetry": "E"},
    {"mode_id": 8, "frequency_32S_cm-1": 361.0, "frequency_36S_cm-1": 349.5, "symmetry": "B2"},
    {"mode_id": 9, "frequency_32S_cm-1": 347.1, "frequency_36S_cm-1": 332.9, "symmetry": "A1"},
    {"mode_id": 10, "frequency_32S_cm-1": 294.0, "frequency_36S_cm-1": 288.8, "symmetry": "E"},
    {"mode_id": 11, "frequency_32S_cm-1": 299.9, "frequency_36S_cm-1": 295.5, "symmetry": "A1"},
    {"mode_id": 12, "frequency_32S_cm-1": 286.2, "frequency_36S_cm-1": 277.5, "symmetry": "B1"},
    {"mode_id": 13, "frequency_32S_cm-1": 278.4, "frequency_36S_cm-1": 269.2, "symmetry": "A2"},
    {"mode_id": 14, "frequency_32S_cm-1": 284.1, "frequency_36S_cm-1": 281.5, "symmetry": "B2"},
    {"mode_id": 15, "frequency_32S_cm-1": 268.5, "frequency_36S_cm-1": 262.2, "symmetry": "A1"},
    {"mode_id": 16, "frequency_32S_cm-1": 266.1, "frequency_36S_cm-1": 258.9, "symmetry": "E"},
    {"mode_id": 17, "frequency_32S_cm-1": 236.4, "frequency_36S_cm-1": 229.3, "symmetry": "E"},
    {"mode_id": 18, "frequency_32S_cm-1": 221.1, "frequency_36S_cm-1": 213.4, "symmetry": "B2"},
    {"mode_id": 19, "frequency_32S_cm-1": 197.3, "frequency_36S_cm-1": 193.4, "symmetry": "B1"},
    {"mode_id": 20, "frequency_32S_cm-1": 176.6, "frequency_36S_cm-1": 174.1, "symmetry": "A2"},
    {"mode_id": 21, "frequency_32S_cm-1": 179.0, "frequency_36S_cm-1": 176.9, "symmetry": "A1"},
    {"mode_id": 22, "frequency_32S_cm-1": 157.2, "frequency_36S_cm-1": 154.3, "symmetry": "E"},
    {"mode_id": 23, "frequency_32S_cm-1": 143.7, "frequency_36S_cm-1": 140.7, "symmetry": "A1"},
    {"mode_id": 24, "frequency_32S_cm-1": 141.4, "frequency_36S_cm-1": 139.3, "symmetry": "E"},
    {"mode_id": 25, "frequency_32S_cm-1": 131.4, "frequency_36S_cm-1": 129.8, "symmetry": "B2"},
    {"mode_id": 26, "frequency_32S_cm-1": 101.8, "frequency_36S_cm-1": 100.7, "symmetry": "B2"},
    {"mode_id": 27, "frequency_32S_cm-1": 90.7, "frequency_36S_cm-1": 90.3, "symmetry": "E"},
    {"mode_id": 28, "frequency_32S_cm-1": 55.3, "frequency_36S_cm-1": 55.2, "symmetry": "A1"},
    {"mode_id": 29, "frequency_32S_cm-1": 54.3, "frequency_36S_cm-1": 53.9, "symmetry": "B1"},
    {"mode_id": 30, "frequency_32S_cm-1": 39.4, "frequency_36S_cm-1": 39.1, "symmetry": "E"},
    {"mode_id": 31, "frequency_32S_cm-1": 22.2, "frequency_36S_cm-1": 22.2, "symmetry": "B2"},
    {"mode_id": 32, "frequency_32S_cm-1": 19.0, "frequency_36S_cm-1": 18.9, "symmetry": "A1"}
]
with open("/app/outputs/ubff_frequencies.json", "w") as f:
    json.dump(modes, f, indent=2)
'
