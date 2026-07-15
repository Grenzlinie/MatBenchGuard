#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 <<'PYEOF'
import json

data = {
    "ISW_NT": {
        "lattice_constants": {"a": 30.0, "b": 30.0, "c": 3.073},
        "tubular_diameter": 11.840,
        "radial_buckling": 0.0,
        "symmetry_number": 2,
        "bulk_modulus": {"a": None, "b": None, "c": 824},
        "band_gap": {"value": 2.312, "transition": "0.65 π/c → 0.95 π/c, Γ → Z"},
        "effective_mass": {"CB": 0.0044, "VB": 0.0040},
        "velocity_z": {"CB": 154320.0, "VB": 35610.0},
        "charge_density": {"s_C": 1.13106, "s_Si": 0.82861, "p_C": 3.93299, "p_Si": 1.99940, "total": 7.89206},
        "total_magnetization": 0.0
    },
    "BSW_NT": {
        "lattice_constants": {"a": 14.738, "b": 14.738, "c": 3.0737},
        "tubular_diameter": 11.887,
        "radial_buckling": 0.0322,
        "symmetry_number": 2,
        "bulk_modulus": {"a": 872, "b": 872, "c": 3398},
        "band_gap": {"value": 1.503, "transition": "0.68 π/c → 0.92 π/c, Γ → Z"},
        "effective_mass": {"CB": 0.0103, "VB": 0.0026},
        "velocity_z": {"CB": 48240.0, "VB": 51950.0},
        "charge_density": {"s_C": 1.13084, "s_Si": 0.82321, "p_C": 3.94195, "p_Si": 1.99932, "total": 7.89533},
        "total_magnetization": 0.0
    },
    "ISW_NTC": {
        "lattice_constants": {"a": 30.0, "b": 30.0, "c": 3.063},
        "tubular_diameter": 11.516,
        "radial_buckling": 0.0395,
        "symmetry_number": 2,
        "bulk_modulus": {"a": None, "b": None, "c": 768},
        "band_gap": {"value": 0.979, "transition": "0.45 π/c → 0.60 π/c, Γ → Z"},
        "effective_mass": {"CB": 0.0128, "VB": 0.0038},
        "velocity_z": {"CB": 167000.0, "VB": 170710.0},
        "charge_density": {"s_C": 1.135685, "s_Si": 0.88920, "p_C": 3.915462, "p_Si": 2.03075, "total": 7.97110},
        "total_magnetization": 0.0
    },
    "ISW_NTSi": {
        "lattice_constants": {"a": 30.0, "b": 30.0, "c": 3.052},
        "tubular_diameter": 11.166,
        "radial_buckling": 0.0458,
        "symmetry_number": 2,
        "bulk_modulus": {"a": None, "b": None, "c": 781},
        "band_gap": {"value": None, "transition": None},
        "effective_mass": {"CB": 0.1272, "VB": None},
        "velocity_z": {"CB": 174420.0, "VB": None},
        "charge_density": {"s_C": 1.125979, "s_Si": 0.87654, "p_C": 3.82680, "p_Si": 1.98760, "total": 7.81691},
        "total_magnetization": 0.0
    }
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
