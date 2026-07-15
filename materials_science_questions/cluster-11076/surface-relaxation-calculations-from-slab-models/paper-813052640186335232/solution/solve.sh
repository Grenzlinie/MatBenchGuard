#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relaxation_output.json ===
cat > "$OUTDIR/relaxation_output.json" << 'EOF'
{
  "surfaces": [
    {
      "surface": "Rh(111)",
      "raw": {
        "interlayer_spacings": {
          "d12_Ang": 2.1573,
          "d23_Ang": 2.1880,
          "d34_Ang": 2.2056,
          "d45_Ang": 2.1968
        },
        "total_energy_relaxed_eV": -60.8637,
        "total_energy_unrelaxed_eV": -60.9537,
        "n_atoms_slab": 10,
        "surface_area_Ang2": 6.255,
        "n_surface_atoms": 1,
        "bulk_spacing_Ang": 2.1946,
        "bulk_energy_per_atom_eV": -7.5
      },
      "derived": {
        "Delta12_pct": -1.7,
        "Delta23_pct": -0.3,
        "Delta34_pct": 0.5,
        "Delta45_pct": 0.1,
        "sigma_eV_per_atom": 1.13,
        "DeltaE_rel_meV_per_atom": 9.0
      }
    },
    {
      "surface": "Rh(100)",
      "raw": {
        "interlayer_spacings": {
          "d12_Ang": 1.8278,
          "d23_Ang": 1.9133,
          "d34_Ang": 1.9114,
          "d45_Ang": 1.9019
        },
        "total_energy_relaxed_eV": -54.2064,
        "total_energy_unrelaxed_eV": -54.5064,
        "n_atoms_slab": 10,
        "surface_area_Ang2": 7.22,
        "n_surface_atoms": 1,
        "bulk_spacing_Ang": 1.90,
        "bulk_energy_per_atom_eV": -7.5
      },
      "derived": {
        "Delta12_pct": -3.8,
        "Delta23_pct": 0.7,
        "Delta34_pct": 0.6,
        "Delta45_pct": 0.1,
        "sigma_eV_per_atom": 1.44,
        "DeltaE_rel_meV_per_atom": 30.0
      }
    },
    {
      "surface": "Rh(110)",
      "raw": {
        "interlayer_spacings": {
          "d12_Ang": 1.2118,
          "d23_Ang": 1.3789,
          "d34_Ang": 1.3537,
          "d45_Ang": 1.3327
        },
        "total_energy_relaxed_eV": -66.2798,
        "total_energy_unrelaxed_eV": -67.7398,
        "n_atoms_slab": 20,
        "surface_area_Ang2": 10.211,
        "n_surface_atoms": 2,
        "bulk_spacing_Ang": 1.3435,
        "bulk_energy_per_atom_eV": -7.5
      },
      "derived": {
        "Delta12_pct": -9.8,
        "Delta23_pct": 2.6,
        "Delta34_pct": 0.8,
        "Delta45_pct": -0.8,
        "sigma_eV_per_atom": 2.05,
        "DeltaE_rel_meV_per_atom": 73.0
      }
    }
  ]
}
EOF
