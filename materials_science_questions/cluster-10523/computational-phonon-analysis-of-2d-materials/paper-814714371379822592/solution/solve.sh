#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_04_computed_properties.json ===
cat > "$OUTDIR/step_04_computed_properties.json" << 'EOF'
{
  "dielectric_constants": {
    "BMT": {
      "average": 26.2,
      "epsilon_11": 28.21,
      "epsilon_33": 22.05
    },
    "BMN": {
      "average": 36.3,
      "epsilon_11": 41.73,
      "epsilon_33": 25.55
    },
    "BZN": {
      "average": 45.4,
      "epsilon_11": 51.67,
      "epsilon_33": 32.87
    }
  },
  "phonon_frequencies": {
    "BMT": {
      "IR_active": {
        "E_u": [634.2, 518.6, 400.8, 325.7, 259.9, 218.4, 174.4, 136.9, 113.2],
        "A_2u": [807.9, 579.5, 425.8, 323.2, 270.9, 136.6, 102.1]
      },
      "Raman_active": [786.0, 583.8, 420.1, 374.8, 255.5, 210.5, 157.8, 105.0, 102.4]
    },
    "BMN": {
      "IR_active": {
        "E_u": [616.4, 483.8, 396.9, 326.3, 257.0, 200.9, 169.3, 144.7, 113.9],
        "A_2u": [779.2, 562.3, 422.8, 332.3, 280.6, 145.3, 102.1]
      },
      "Raman_active": [775.6, 565.6, 425.1, 377.2, 290.9, 266.7, 173.1, 104.9, 103.5]
    },
    "BZN": {
      "IR_active": {
        "E_u": [604.2, 489.3, 393.3, 250.2, 214.9, 173.4, 147.2, 139.2, 111.3],
        "A_2u": [781.8, 552.4, 414.1, 291.5, 171.6, 138.6, 98.4]
      },
      "Raman_active": [768.8, 534.3, 408.4, 363.9, 280.5, 259.3, 167.5, 103.9, 101.0]
    }
  },
  "mode_effective_charges": {
    "BMT": {
      "E_u_6": [0.04, -0.06],
      "E_u_7": [-0.02, 0.06],
      "E_u_8": [1.39, 0.73],
      "A_2u_4": [-1.84],
      "A_2u_5": [7.96],
      "A_2u_6": [5.30]
    },
    "BMN": {
      "E_u_6": [0.18, -0.11],
      "E_u_7": [0.04, -0.03],
      "E_u_8": [0.55, 0.49],
      "A_2u_4": [0.15],
      "A_2u_5": [-8.83],
      "A_2u_6": [-5.06]
    },
    "BZN": {
      "E_u_6": [-0.04, 0.03],
      "E_u_7": [0.12, -0.10],
      "E_u_8": [0.75, 0.43],
      "A_2u_4": [-7.75],
      "A_2u_5": [-7.92],
      "A_2u_6": [4.31]
    }
  },
  "per_atom_dielectric_contributions": {
    "BMT": {
      "Ba1": { "epsilon_i_11": 1.01, "epsilon_i_33": -0.13 },
      "Ba2": { "epsilon_i_11": 0.62, "epsilon_i_33": 1.30 },
      "B_prime": { "epsilon_i_11": 0.46, "epsilon_i_33": 0.38 },
      "B_doubleprime": { "epsilon_i_11": 0.16, "epsilon_i_33": -0.23 },
      "O1": { "epsilon_i_11": 1.77, "epsilon_i_33": 1.57 },
      "O2": { "epsilon_i_11": 3.31, "epsilon_i_33": 1.89 }
    },
    "BMN": {
      "Ba1": { "epsilon_i_11": 1.45, "epsilon_i_33": -0.42 },
      "Ba2": { "epsilon_i_11": 0.54, "epsilon_i_33": 1.59 },
      "B_prime": { "epsilon_i_11": 0.71, "epsilon_i_33": 0.43 },
      "B_doubleprime": { "epsilon_i_11": 1.58, "epsilon_i_33": 0.04 },
      "O1": { "epsilon_i_11": 2.23, "epsilon_i_33": 1.87 },
      "O2": { "epsilon_i_11": 5.70, "epsilon_i_33": 2.19 }
    },
    "BZN": {
      "Ba1": { "epsilon_i_11": 1.16, "epsilon_i_33": -0.44 },
      "Ba2": { "epsilon_i_11": 0.64, "epsilon_i_33": 1.55 },
      "B_prime": { "epsilon_i_11": 2.47, "epsilon_i_33": 1.66 },
      "B_doubleprime": { "epsilon_i_11": 1.61, "epsilon_i_33": 0.05 },
      "O1": { "epsilon_i_11": 2.96, "epsilon_i_33": 2.42 },
      "O2": { "epsilon_i_11": 6.85, "epsilon_i_33": 2.96 }
    }
  }
}
EOF
