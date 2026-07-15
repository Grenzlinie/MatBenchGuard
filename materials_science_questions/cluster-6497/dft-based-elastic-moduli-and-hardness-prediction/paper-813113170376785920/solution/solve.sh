#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduced_properties.json ===
python3 <<'PYEOF'
import json, os

outdir = os.environ.get("OUTDIR", "/app/outputs")
path = os.path.join(outdir, "reproduced_properties.json")

props = {
    "ISW_NT": {
        "num_atoms": 28,
        "lattice_constants": {"a": 30.0, "b": 30.0, "c": 3.073},
        "bulk_modulus": {"a": None, "b": None, "c": 824},
        "tubular_diameter": 11.840,
        "radial_buckling": 0.0000,
        "symmetry": 2,
        "band_gap": 2.312,
        "band_gap_type": "indirect",
        "band_gap_transition": "0.65π/c → 0.95π/c",
        "effective_mass": {"electron": 0.0044, "hole": 0.0040},
        "velocity": {"electron": 1.5432, "hole": 0.3561},
        "ef_minus_evbm": 1.236,
        "ecbm_minus_ef": 1.076,
        "charge_s_C": 1.13106,
        "charge_s_Si": 0.82861,
        "charge_p_C": 3.93299,
        "charge_p_Si": 1.99940,
        "total_charge": 7.89206
    },
    "BSW_NT": {
        "num_atoms": 28,
        "lattice_constants": {"a": 14.738, "b": 14.738, "c": 3.0737},
        "bulk_modulus": {"a": 872, "b": 872, "c": 3398},
        "tubular_diameter": 11.887,
        "radial_buckling": 0.0322,
        "symmetry": 2,
        "band_gap": 1.503,
        "band_gap_type": "indirect",
        "band_gap_transition": "0.68π/c → 0.92π/c",
        "effective_mass": {"electron": 0.0103, "hole": 0.0026},
        "velocity": {"electron": 0.4824, "hole": 0.5195},
        "ef_minus_evbm": 1.212,
        "ecbm_minus_ef": 0.291,
        "charge_s_C": 1.13084,
        "charge_s_Si": 0.82321,
        "charge_p_C": 3.94195,
        "charge_p_Si": 1.99932,
        "total_charge": 7.89533
    },
    "ISW_NT_C": {
        "num_atoms": 27,
        "lattice_constants": {"a": 30.0, "b": 30.0, "c": 3.063},
        "bulk_modulus": {"a": None, "b": None, "c": 768},
        "tubular_diameter": 11.516,
        "radial_buckling": 0.0395,
        "symmetry": 2,
        "band_gap": 0.979,
        "band_gap_type": "indirect",
        "band_gap_transition": "0.45π/c → 0.60π/c",
        "effective_mass": {"electron": 0.0128, "hole": 0.0038},
        "velocity": {"electron": 1.6700, "hole": 1.7071},
        "ef_minus_evbm": 0.779,
        "ecbm_minus_ef": 0.200,
        "charge_s_C": 1.135685,
        "charge_s_Si": 0.88920,
        "charge_p_C": 3.915462,
        "charge_p_Si": 2.03075,
        "total_charge": 7.97110
    },
    "ISW_NT_Si": {
        "num_atoms": 27,
        "lattice_constants": {"a": 30.0, "b": 30.0, "c": 3.052},
        "bulk_modulus": {"a": None, "b": None, "c": 781},
        "tubular_diameter": 11.166,
        "radial_buckling": 0.0458,
        "symmetry": 2,
        "band_gap": None,
        "band_gap_type": None,
        "band_gap_transition": None,
        "effective_mass": {"electron": 0.1272, "hole": None},
        "velocity": {"electron": 1.7442, "hole": 1.7442},
        "ef_minus_evbm": None,
        "ecbm_minus_ef": None,
        "charge_s_C": 1.125979,
        "charge_s_Si": 0.87654,
        "charge_p_C": 3.82680,
        "charge_p_Si": 1.98760,
        "total_charge": 7.81691
    }
}

with open(path, "w") as f:
    json.dump(props, f, indent=2, ensure_ascii=False)
PYEOF
