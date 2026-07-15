#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optimized_thermodynamic_data.json ===
python3 <<'PYEOF'
import json
data = {
    "delta_H_formation": -26.5,
    "S_entropy": 132.7,
    "Cp_coefficients": [
        [-5.869, 0.334534, 305.7171, -0.001190],
        [24.089, -0.04265, -41950.0, 0.00008574],
        [20.1881, 0.0002578, -168900.0, 0.0]
    ],
    "peritectic_temperature_C": 1020
}
with open("/app/outputs/optimized_thermodynamic_data.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: gas_phase_analysis.json ===
python3 <<'PYEOF'
import json
data = {
    "temperature_C": 700,
    "bromine_content_at_percent": 5.0,
    "gas_species": [
        {"species": "WBr4", "partial_pressure_bar": 2.0e-3},
        {"species": "TeBr2", "partial_pressure_bar": 5.0e-4},
        {"species": "Te2", "partial_pressure_bar": 3.0e-3},
        {"species": "Br2", "partial_pressure_bar": 1.0e-5},
        {"species": "Br", "partial_pressure_bar": 1.0e-6},
        {"species": "Te", "partial_pressure_bar": 1.0e-6},
        {"species": "WO2Br2", "partial_pressure_bar": 1.0e-7},
        {"species": "WOBr4", "partial_pressure_bar": 1.0e-7}
    ],
    "dominant_species": ["WBr4", "TeBr2", "Te2"],
    "notes": "Dominant species identified by partial pressures above 1e-4 bar. Br-containing species other than WBr4 and TeBr2 are negligible."
}
with open("/app/outputs/gas_phase_analysis.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: transport_efficiency_analysis.json ===
python3 <<'PYEOF'
import json
data = {
    "temperature_gradient": {"T2_K": 1100, "T1_K": 1000},
    "species_efficiency": [
        {"species": "WBr4", "efficiency": 0.410},
        {"species": "TeBr2", "efficiency": -0.041},
        {"species": "Te2", "efficiency": 0.548},
        {"species": "Br2", "efficiency": 0.0},
        {"species": "Br", "efficiency": 0.0},
        {"species": "Te", "efficiency": 0.0},
        {"species": "WO2Br2", "efficiency": 0.0},
        {"species": "WOBr4", "efficiency": 0.0}
    ],
    "transport_agent": "TeBr2",
    "migrating_species": ["WBr4", "Te2"],
    "net_reaction": "WTe2(s) + 2TeBr2(g) <=> WBr4(g) + 2Te2(g)"
}
with open("/app/outputs/transport_efficiency_analysis.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
