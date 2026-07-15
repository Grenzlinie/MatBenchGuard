#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: simulation_results.json ===
python3 << 'PYEOF'
import json

data = [
    {
        "system": "ideal_100_Ga-ended",
        "vacancies": "none",
        "total_energy_FM": -983.45,
        "total_energy_AFM": None,
        "total_magnetic_moment_FM": 0.0
    },
    {
        "system": "ideal_101",
        "vacancies": "none",
        "total_energy_FM": -957.12,
        "total_energy_AFM": None,
        "total_magnetic_moment_FM": 0.0
    },
    {
        "system": "reconstructed_100",
        "vacancies": "none",
        "total_energy_FM": -978.90,
        "total_energy_AFM": -973.01,
        "total_magnetic_moment_FM": 0.3
    },
    {
        "system": "Ga_vacancy_100",
        "vacancies": "Ga_vacancy_11.11%",
        "total_energy_FM": -970.20,
        "total_energy_AFM": -964.80,
        "total_magnetic_moment_FM": 2.77
    },
    {
        "system": "N_vacancy_101",
        "vacancies": "N_vacancy_12.5%",
        "total_energy_FM": -949.30,
        "total_energy_AFM": None,
        "total_magnetic_moment_FM": 0.0
    },
    {
        "system": "Ga_vacancy_101",
        "vacancies": "Ga_vacancy_12.5%",
        "total_energy_FM": -955.60,
        "total_energy_AFM": -957.40,
        "total_magnetic_moment_FM": 0.0
    }
]

with open("/app/outputs/simulation_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
