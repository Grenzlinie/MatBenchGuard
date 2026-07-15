#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: crystal_geometry.json ===
cat > /app/outputs/crystal_geometry.json <<'EOF'
{
  "bond_lengths": [
    {"id": "N8-C2", "value_angstrom": 1.431},
    {"id": "N8-C1", "value_angstrom": 1.456},
    {"id": "N15-C2", "value_angstrom": 1.436},
    {"id": "N15-C17", "value_angstrom": 1.419},
    {"id": "N8-N7", "value_angstrom": 1.351},
    {"id": "N15-N18", "value_angstrom": 1.363},
    {"id": "N7-O12", "value_angstrom": 1.247},
    {"id": "N7-O11", "value_angstrom": 1.254},
    {"id": "N18-O25", "value_angstrom": 1.243},
    {"id": "N18-O24", "value_angstrom": 1.249},
    {"id": "C2-H6", "value_angstrom": 1.106},
    {"id": "C2-H5", "value_angstrom": 1.104},
    {"id": "C17-H23", "value_angstrom": 1.106},
    {"id": "C17-H22", "value_angstrom": 1.105},
    {"id": "H5...O12", "value_angstrom": 2.140}
  ],
  "bond_angles": [
    {"id": "O12-N7-O11", "value_degree": 125.5},
    {"id": "N8-N7-O12", "value_degree": 118.6},
    {"id": "N8-N7-O11", "value_degree": 115.9},
    {"id": "N7-N8-C1", "value_degree": 116.1},
    {"id": "N7-N8-C2", "value_degree": 118.8},
    {"id": "C2-N8-C1", "value_degree": 123.1},
    {"id": "N8-C2-N15", "value_degree": 111.2},
    {"id": "N8-C2-H6", "value_degree": 111.9},
    {"id": "N8-C2-H5", "value_degree": 107.3},
    {"id": "N15-C2-H6", "value_degree": 107.2},
    {"id": "N15-C2-H5", "value_degree": 111.9},
    {"id": "H6-C2-H5", "value_degree": 107.3},
    {"id": "O25-N18-O24", "value_degree": 126.3},
    {"id": "N15-N18-O25", "value_degree": 116.7},
    {"id": "N15-N18-O24", "value_degree": 117.0},
    {"id": "N18-N15-C2", "value_degree": 118.6},
    {"id": "N18-N15-C17", "value_degree": 117.7},
    {"id": "C2-N15-C17", "value_degree": 123.7},
    {"id": "N21-C17-N15", "value_degree": 110.0},
    {"id": "N15-C17-H22", "value_degree": 107.5},
    {"id": "N15-C17-H23", "value_degree": 109.9},
    {"id": "N21-C17-H22", "value_degree": 110.3},
    {"id": "N21-C17-H23", "value_degree": 109.7},
    {"id": "H23-C17-H22", "value_degree": 109.4}
  ]
}
EOF

# === solve block: mulliken_population.json ===
cat > /app/outputs/mulliken_population.json <<'EOF'
{
  "crystal": {
    "atomic_charges": {
      "C1": -0.28,
      "C2": -0.30,
      "H3": 0.34,
      "H4": 0.37,
      "H5": 0.37,
      "H6": 0.36,
      "N7": 0.52,
      "N8": -0.14,
      "N9": -0.16,
      "N10": 0.52,
      "O11": -0.41,
      "O12": -0.39,
      "O13": -0.41,
      "O14": -0.39
    },
    "bond_populations": {
      "N8-N7": 0.76,
      "N7-O12": 0.76,
      "N7-O11": 0.74,
      "N8-C2": 0.67,
      "C2-H5": 0.80,
      "C2-H6": 0.83,
      "C2-N15": 0.66,
      "N15-N18": 0.71,
      "N18-O24": 0.75,
      "N18-O25": 0.77,
      "N15-C17": 0.70,
      "C17-H23": 0.82,
      "C17-H22": 0.83,
      "C17-N21": 0.61,
      "H5...O12": 0.01,
      "H19...O24": 0.01
    }
  },
  "gas": {
    "atomic_charges": {
      "C1": 0.09,
      "C2": 0.14,
      "H3": 0.16,
      "H4": 0.21,
      "H5": 0.20,
      "H6": 0.16,
      "N7": 0.68,
      "N8": -0.32,
      "N9": -0.36,
      "N10": 0.67,
      "O11": -0.40,
      "O12": -0.41,
      "O13": -0.40,
      "O14": -0.40
    },
    "bond_populations": {
      "N8-N7": 0.188,
      "N7-O12": 0.323,
      "N7-O11": 0.339,
      "N8-C2": 0.207,
      "C2-H5": 0.393,
      "C2-H6": 0.386,
      "C2-N15": 0.215,
      "N15-N18": 0.152,
      "N18-O24": 0.329,
      "N18-O25": 0.326,
      "N15-C17": 0.222,
      "C17-H23": 0.380,
      "C17-H22": 0.392,
      "C17-N21": 0.246,
      "H5...O12": 0.005,
      "H19...O24": 0.0
    }
  }
}
EOF

# === solve block: pDOS_hb_output.json ===
cat > /app/outputs/pDOS_hb_output.json <<'EOF'
{
  "overlap_energy_range": "-7 eV to -6 eV",
  "hydrogen_bonds": [
    {"donor": "H5", "acceptor": "O12", "type": "intramolecular", "max_overlap_energy": -6.5},
    {"donor": "H19", "acceptor": "O28", "type": "intramolecular", "max_overlap_energy": -6.5},
    {"donor": "H19", "acceptor": "O24", "type": "intermolecular", "max_overlap_energy": -6.5}
  ]
}
EOF
