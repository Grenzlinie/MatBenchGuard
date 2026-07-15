#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: allotropes_properties.json ===
python3 << 'PYEOF'
import json

properties = [
    {
        "allotrope_id": "diamond",
        "space_group": "Fd-3m",
        "delta_E_PBE": 0.00,
        "bulk_modulus": 441,
        "hardness": 93.2,
        "band_gap_PBE": 4.2,
        "band_gap_HSE": 5.4,
        "refractive_index_xx": 2.40,
        "refractive_index_yy": 2.40,
        "refractive_index_zz": 2.40
    },
    {
        "allotrope_id": "oP24-I (#8170628)",
        "space_group": "Pbam",
        "delta_E_PBE": 0.08,
        "bulk_modulus": 418,
        "hardness": 91.1,
        "band_gap_PBE": 4.7,
        "band_gap_HSE": 5.9,
        "refractive_index_xx": 2.34,
        "refractive_index_yy": 2.38,
        "refractive_index_zz": 2.42
    },
    {
        "allotrope_id": "oP24-II (#8129388)",
        "space_group": "Pnma",
        "delta_E_PBE": 0.11,
        "bulk_modulus": 412,
        "hardness": 90.8,
        "band_gap_PBE": 4.9,
        "band_gap_HSE": 6.3,
        "refractive_index_xx": 2.36,
        "refractive_index_yy": 2.37,
        "refractive_index_zz": 2.38
    },
    {
        "allotrope_id": "oP28 (#8255250)",
        "space_group": "Pnma",
        "delta_E_PBE": 0.12,
        "bulk_modulus": 412,
        "hardness": 90.9,
        "band_gap_PBE": 4.7,
        "band_gap_HSE": 6.0,
        "refractive_index_xx": 2.36,
        "refractive_index_yy": 2.38,
        "refractive_index_zz": 2.42
    },
    {
        "allotrope_id": "oP20 (#8155755)",
        "space_group": "Pmma",
        "delta_E_PBE": 0.11,
        "bulk_modulus": 420,
        "hardness": 91.4,
        "band_gap_PBE": 4.0,
        "band_gap_HSE": 5.1,
        "refractive_index_xx": 2.31,
        "refractive_index_yy": 2.36,
        "refractive_index_zz": 2.36
    },
    {
        "allotrope_id": "mS32 (#8036927)",
        "space_group": "C2/m",
        "delta_E_PBE": 0.12,
        "bulk_modulus": 415,
        "hardness": 90.8,
        "band_gap_PBE": 4.5,
        "band_gap_HSE": 5.7,
        "refractive_index_xx": 2.35,
        "refractive_index_yy": 2.36,
        "refractive_index_zz": 2.40
    },
    {
        "allotrope_id": "mP16 (#8036926)",
        "space_group": "P2/m",
        "delta_E_PBE": 0.11,
        "bulk_modulus": 423,
        "hardness": 91.0,
        "band_gap_PBE": 4.3,
        "band_gap_HSE": 5.5,
        "refractive_index_xx": 2.35,
        "refractive_index_yy": 2.36,
        "refractive_index_zz": 2.40
    }
]

with open('/app/outputs/allotropes_properties.json', 'w') as f:
    json.dump(properties, f, indent=2)
PYEOF
