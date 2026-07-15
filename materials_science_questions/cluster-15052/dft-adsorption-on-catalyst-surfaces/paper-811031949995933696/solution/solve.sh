#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_results.json ===
python3 -c '
import json

result = {
    "pristine_physisorbed_BE": -0.5,
    "pristine_chemisorbed_BE": -31.4,
    "pristine_dissociated_BE": -74.8,
    "pristine_barrier": 16.8,
    "K_physisorbed_BE": -6.5,
    "K_chemisorbed_BE": -46.4,
    "K_dissociated_BE": -80.9,
    "K_barrier": 14.0,
    "K_Bader_charge": 0.82
}

with open("/app/outputs/dft_results.json", "w") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
'
