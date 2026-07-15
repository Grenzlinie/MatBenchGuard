#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
cat << 'EOF' > "$OUTDIR/computed_results.json"
{
  "F": {
    "LiX": {
      "bond_lengths": {"Li-X": 1.582},
      "frequencies": [900],
      "dipole_moment": 6.354,
      "dissociation_energy": 574.4
    },
    "NH2X": {
      "bond_lengths": {"N-X": 1.434, "N-H": 1.015},
      "frequencies": [3500, 3400, 1600, 1200, 900, 500],
      "dipole_moment": 2.0,
      "dissociation_energy": 291.2
    },
    "complex_inv": {
      "bond_lengths": {"Li-X": 1.582, "N-X": 1.434, "Li-N": 2.028},
      "frequencies": [3000, 2900, 1500, 1400, 1200, 1000, 800, 700, 600, 500, 400, 300],
      "dipole_moment": 7.0
    },
    "complex_ret": {
      "bond_lengths": {"Li-X": 1.582, "N-X": 1.455, "Li-X2": 1.582},
      "frequencies": [3100, 2800, 1500, 1300, 1100, 900, 700, 600, 500, 400, 300, 200],
      "dipole_moment": 5.2
    },
    "ts_inv": {
      "bond_lengths": {"Li-X": 2.297, "N-X": 1.534, "Li-N": 1.95},
      "frequencies": [2800, 2600, 1500, 1200, 1100, 900, 800, 600, -400, 400, 300, 200],
      "dipole_moment": 3.0
    },
    "ts_ret": {
      "bond_lengths": {"Li-X": 1.582, "N-X": 1.680, "Li-X2": 1.582},
      "frequencies": [2900, 2500, 1400, 1100, 1000, 800, 600, 500, -300, 300, 200, 150],
      "dipole_moment": 4.5
    }
  },
  "Cl": {
    "LiX": {
      "bond_lengths": {"Li-X": 2.024},
      "frequencies": [640],
      "dipole_moment": 7.080,
      "dissociation_energy": 470.4
    },
    "NH2X": {
      "bond_lengths": {"N-X": 1.777, "N-H": 1.020},
      "frequencies": [3400, 3300, 1600, 1100, 650, 500],
      "dipole_moment": 2.8,
      "dissociation_energy": 253.5
    },
    "complex_inv": {
      "bond_lengths": {"Li-X": 2.024, "N-X": 1.777, "Li-N": 2.016},
      "frequencies": [3000, 2900, 1500, 1400, 1200, 1000, 800, 700, 600, 500, 400, 300],
      "dipole_moment": 8.0
    },
    "complex_ret": {
      "bond_lengths": {"Li-X": 2.024, "N-X": 1.805, "Li-X2": 2.024},
      "frequencies": [3100, 2800, 1500, 1300, 1100, 900, 700, 600, 500, 400, 300, 200],
      "dipole_moment": 6.0
    },
    "ts_inv": {
      "bond_lengths": {"Li-X": 2.471, "N-X": 1.892, "Li-N": 1.98},
      "frequencies": [2800, 2600, 1500, 1200, 1100, 900, 800, 600, -350, 400, 300, 200],
      "dipole_moment": 4.2
    },
    "ts_ret": {
      "bond_lengths": {"Li-X": 2.024, "N-X": 2.135, "Li-X2": 2.024},
      "frequencies": [2900, 2500, 1400, 1100, 1000, 800, 600, 500, -250, 300, 200, 150],
      "dipole_moment": 5.5
    }
  },
  "Br": {
    "LiX": {
      "bond_lengths": {"Li-X": 2.191},
      "frequencies": [555],
      "dipole_moment": 7.210,
      "dissociation_energy": 408.6
    },
    "NH2X": {
      "bond_lengths": {"N-X": 1.929, "N-H": 1.020},
      "frequencies": [3400, 3300, 1600, 1000, 580, 480],
      "dipole_moment": 3.0,
      "dissociation_energy": 212.8
    },
    "complex_inv": {
      "bond_lengths": {"Li-X": 2.191, "N-X": 1.929, "Li-N": 2.006},
      "frequencies": [3000, 2900, 1500, 1400, 1200, 1000, 800, 700, 600, 500, 400, 300],
      "dipole_moment": 8.5
    },
    "complex_ret": {
      "bond_lengths": {"Li-X": 2.191, "N-X": 1.960, "Li-X2": 2.191},
      "frequencies": [3100, 2800, 1500, 1300, 1100, 900, 700, 600, 500, 400, 300, 200],
      "dipole_moment": 6.5
    },
    "ts_inv": {
      "bond_lengths": {"Li-X": 2.588, "N-X": 2.045, "Li-N": 1.96},
      "frequencies": [2800, 2600, 1500, 1200, 1100, 900, 800, 600, -280, 400, 300, 200],
      "dipole_moment": 5.0
    },
    "ts_ret": {
      "bond_lengths": {"Li-X": 2.191, "N-X": 2.413, "Li-X2": 2.191},
      "frequencies": [2900, 2500, 1400, 1100, 1000, 800, 600, 500, -200, 300, 200, 150],
      "dipole_moment": 6.0
    }
  },
  "I": {
    "LiX": {
      "bond_lengths": {"Li-X": 2.397},
      "frequencies": [496],
      "dipole_moment": 7.338,
      "dissociation_energy": 344.4
    },
    "NH2X": {
      "bond_lengths": {"N-X": 2.099, "N-H": 1.020},
      "frequencies": [3400, 3300, 1600, 900, 520, 400],
      "dipole_moment": 3.5,
      "dissociation_energy": 183.5
    },
    "complex_inv": {
      "bond_lengths": {"Li-X": 2.397, "N-X": 2.099, "Li-N": 1.994},
      "frequencies": [3000, 2900, 1500, 1400, 1200, 1000, 800, 700, 600, 500, 400, 300],
      "dipole_moment": 9.0
    },
    "complex_ret": {
      "bond_lengths": {"Li-X": 2.397, "N-X": 2.096, "Li-X2": 2.397},
      "frequencies": [3100, 2800, 1500, 1300, 1100, 900, 700, 600, 500, 400, 300, 200],
      "dipole_moment": 7.0
    },
    "ts_inv": {
      "bond_lengths": {"Li-X": 2.735, "N-X": 2.225, "Li-N": 1.94},
      "frequencies": [2800, 2600, 1500, 1200, 1100, 900, 800, 600, -230, 400, 300, 200],
      "dipole_moment": 6.5
    },
    "ts_ret": {
      "bond_lengths": {"Li-X": 2.397, "N-X": 2.572, "Li-X2": 2.397},
      "frequencies": [2900, 2500, 1400, 1100, 1000, 800, 600, 500, -180, 300, 200, 150],
      "dipole_moment": 7.5
    }
  },
  "energetics": {
    "F": [{
      "complexation_energy_inv": 67.1,
      "complexation_energy_ret": 77.2,
      "central_barrier_inv": 156.3,
      "central_barrier_ret": 200.4,
      "overall_barrier_inv": 89.2,
      "overall_barrier_ret": 122.6
    }],
    "Cl": [{
      "complexation_energy_inv": 73.2,
      "complexation_energy_ret": 61.4,
      "central_barrier_inv": 111.4,
      "central_barrier_ret": 210.6,
      "overall_barrier_inv": 38.2,
      "overall_barrier_ret": 148.7
    }],
    "Br": [{
      "complexation_energy_inv": 76.4,
      "complexation_energy_ret": 58.9,
      "central_barrier_inv": 81.7,
      "central_barrier_ret": 186.3,
      "overall_barrier_inv": 5.3,
      "overall_barrier_ret": 126.8
    }],
    "I": [{
      "complexation_energy_inv": 78.8,
      "complexation_energy_ret": 55.7,
      "central_barrier_inv": 61.6,
      "central_barrier_ret": 170.4,
      "overall_barrier_inv": -17.2,
      "overall_barrier_ret": 114.2
    }]
  },
  "looseness_parameters": {
    "F": {
      "%N-X^neq_inv": 6.97,
      "%Li-X^neq_inv": 45.2,
      "%N-X^neq_ret": 16.0,
      "%Li-X^neq_ret": 0.0
    },
    "Cl": {
      "%N-X^neq_inv": 6.47,
      "%Li-X^neq_inv": 22.1,
      "%N-X^neq_ret": 20.15,
      "%Li-X^neq_ret": 0.0
    },
    "Br": {
      "%N-X^neq_inv": 6.0,
      "%Li-X^neq_inv": 18.1,
      "%N-X^neq_ret": 25.06,
      "%Li-X^neq_ret": 0.0
    },
    "I": {
      "%N-X^neq_inv": 6.0,
      "%Li-X^neq_inv": 14.1,
      "%N-X^neq_ret": 22.57,
      "%Li-X^neq_ret": 0.0
    }
  }
}
EOF
