#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_properties.json ===
cat > /app/outputs/lattice_properties.json <<'EOF'
{
  "C2N2O": {
    "a": 7.3845,
    "b": 4.4921,
    "c": 4.0198,
    "cell_volume": 133.34,
    "cohesive_energy": -8.47,
    "formation_enthalpy": -19.80,
    "band_gap": 4.915,
    "band_gap_type": "indirect"
  },
  "Si2N2O": {
    "a": 8.9373,
    "b": 5.5247,
    "c": 4.8747,
    "cell_volume": 240.69,
    "cohesive_energy": -8.50,
    "formation_enthalpy": -2.34,
    "band_gap": 4.88,
    "band_gap_type": "direct"
  },
  "Ge2N2O": {
    "a": 9.4254,
    "b": 5.7986,
    "c": 5.1446,
    "cell_volume": 281.16,
    "cohesive_energy": -7.07,
    "formation_enthalpy": -1.25,
    "band_gap": 2.74,
    "band_gap_type": "indirect"
  }
}
EOF

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'EOF'
{
  "C2N2O": {
    "C11": 621.7,
    "C22": 563.7,
    "C33": 871.4,
    "C44": 325.2,
    "C55": 176.1,
    "C66": 180.3,
    "C12": 93.4,
    "C13": 89.9,
    "C23": 61.8
  },
  "Si2N2O": {
    "C11": 326.4,
    "C22": 302.7,
    "C33": 324.2,
    "C44": 131.2,
    "C55": 57.3,
    "C66": 71.9,
    "C12": 112.1,
    "C13": 72.9,
    "C23": 68.0
  },
  "Ge2N2O": {
    "C11": 162.4,
    "C22": 163.5,
    "C33": 204.2,
    "C44": 95.4,
    "C55": 32.26,
    "C66": 43.6,
    "C12": 41.7,
    "C13": 22.0,
    "C23": 17.5
  }
}
EOF

# === solve block: mechanical_properties.json ===
cat > /app/outputs/mechanical_properties.json <<'EOF'
{
  "C2N2O": {
    "B": 279.0,
    "G": 246.4,
    "E": 571.1,
    "v": 0.159,
    "BG_ratio": 1.13,
    "A_U": 0.483,
    "A_B": 1.42,
    "A_G": 4.34,
    "A1": 0.990,
    "A2": 0.561,
    "A3": 0.720,
    "k_a": 1.23,
    "k_b": 1.47,
    "k_c": 0.91
  },
  "Si2N2O": {
    "B": 161.9,
    "G": 93.7,
    "E": 235.6,
    "v": 0.257,
    "BG_ratio": 1.73,
    "A_U": 0.579,
    "A_B": 0.15,
    "A_G": 5.44,
    "A1": 1.036,
    "A2": 0.473,
    "A3": 0.703,
    "k_a": 1.89,
    "k_b": 2.27,
    "k_c": 2.06
  },
  "Ge2N2O": {
    "B": 76.9,
    "G": 59.2,
    "E": 141.4,
    "v": 0.193,
    "BG_ratio": 1.30,
    "A_U": 0.913,
    "A_B": 0.06,
    "A_G": 8.35,
    "A1": 1.183,
    "A2": 0.399,
    "A3": 0.719,
    "k_a": 4.44,
    "k_b": 4.56,
    "k_c": 4.03
  }
}
EOF

# === solve block: vickers_hardness.json ===
cat > /app/outputs/vickers_hardness.json <<'EOF'
{
  "C2N2O": {
    "bonds": [
      {
        "bond_type": "C-O",
        "bond_length": 1.429,
        "overlap_population": 0.58,
        "bond_volume": 4.049,
        "bond_hardness": 41.73,
        "number_of_bonds": 4
      },
      {
        "bond_type": "C-N",
        "bond_length": 1.442,
        "overlap_population": 0.82,
        "bond_volume": 4.159,
        "bond_hardness": 56.42,
        "number_of_bonds": 4
      },
      {
        "bond_type": "C-N",
        "bond_length": 1.443,
        "overlap_population": 0.71,
        "bond_volume": 4.170,
        "bond_hardness": 48.65,
        "number_of_bonds": 4
      },
      {
        "bond_type": "C-N",
        "bond_length": 1.455,
        "overlap_population": 0.79,
        "bond_volume": 4.278,
        "bond_hardness": 51.87,
        "number_of_bonds": 4
      }
    ],
    "H_v_Gao": 49.37,
    "H_v_Jiang": 36.34
  },
  "Si2N2O": {
    "bonds": [
      {
        "bond_type": "Si-O",
        "bond_length": 1.632,
        "overlap_population": 0.55,
        "bond_volume": 6.606,
        "bond_hardness": 17.50,
        "number_of_bonds": 4
      },
      {
        "bond_type": "Si-N",
        "bond_length": 1.732,
        "overlap_population": 0.67,
        "bond_volume": 7.890,
        "bond_hardness": 15.86,
        "number_of_bonds": 4
      },
      {
        "bond_type": "Si-N",
        "bond_length": 1.732,
        "overlap_population": 0.61,
        "bond_volume": 7.894,
        "bond_hardness": 14.42,
        "number_of_bonds": 4
      },
      {
        "bond_type": "Si-N",
        "bond_length": 1.739,
        "overlap_population": 0.66,
        "bond_volume": 7.995,
        "bond_hardness": 15.28,
        "number_of_bonds": 4
      }
    ],
    "H_v_Gao": 15.73,
    "H_v_Jiang": 13.82
  },
  "Ge2N2O": {
    "bonds": [
      {
        "bond_type": "Ge-O",
        "bond_length": 1.782,
        "overlap_population": 0.60,
        "bond_volume": 8.204,
        "bond_hardness": 13.30,
        "number_of_bonds": 4
      },
      {
        "bond_type": "Ge-N",
        "bond_length": 1.838,
        "overlap_population": 0.70,
        "bond_volume": 9.002,
        "bond_hardness": 13.30,
        "number_of_bonds": 4
      },
      {
        "bond_type": "Ge-N",
        "bond_length": 1.846,
        "overlap_population": 0.69,
        "bond_volume": 9.117,
        "bond_hardness": 12.83,
        "number_of_bonds": 4
      },
      {
        "bond_type": "Ge-N",
        "bond_length": 1.848,
        "overlap_population": 0.64,
        "bond_volume": 9.159,
        "bond_hardness": 11.81,
        "number_of_bonds": 4
      }
    ],
    "H_v_Gao": 12.80,
    "H_v_Jiang": 8.73
  }
}
EOF

# === solve block: thermal_properties.json ===
cat > /app/outputs/thermal_properties.json <<'EOF'
{
  "C2N2O": {
    "longitudinal_velocity": 13387.06,
    "transverse_velocity": 8525.51,
    "mean_velocity": 9372.05,
    "Debye_temperature": 1251.13,
    "k_min_Clarke": 4.40,
    "k_min_Cahill": 4.79
  },
  "Si2N2O": {
    "longitudinal_velocity": 10231.51,
    "transverse_velocity": 5847.83,
    "mean_velocity": 6497.87,
    "Debye_temperature": 710.52,
    "k_min_Clarke": 2.1,
    "k_min_Cahill": 2.3
  },
  "Ge2N2O": {
    "longitudinal_velocity": 5931.01,
    "transverse_velocity": 3655.60,
    "mean_velocity": 4033.01,
    "Debye_temperature": 418.51,
    "k_min_Clarke": 1.16,
    "k_min_Cahill": 1.26
  }
}
EOF
