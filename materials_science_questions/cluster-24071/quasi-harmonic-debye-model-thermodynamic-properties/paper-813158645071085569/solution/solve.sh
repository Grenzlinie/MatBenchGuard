#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_02_elastic_properties.json ===
cat > /app/outputs/step_02_elastic_properties.json <<'EOF'
{
  "phases": [
    {
      "name": "α-Zr",
      "a": 3.231,
      "c": 5.171,
      "C11": 148.0,
      "C12": 62.1,
      "C13": 68.5,
      "C33": 168.0,
      "C44": 25.3,
      "E": 94.1,
      "B": 98.6,
      "G": 35.1
    },
    {
      "name": "γ-ZrH",
      "a": 4.58,
      "c": 5.02,
      "C11": 122.0,
      "C12": 116.0,
      "C13": 98.0,
      "C33": 183.0,
      "C44": 47.5,
      "C66": 61.1,
      "E": 69.5,
      "B": 116.0,
      "G": 25.3
    },
    {
      "name": "δ-ZrH₁.₅",
      "a": 4.77,
      "c": 4.80,
      "C11": 162.0,
      "C12": 103.0,
      "C13": 109.0,
      "C33": 166.0,
      "C44": 69.3,
      "C66": 66.8,
      "E": 127.0,
      "B": 126.0,
      "G": 47.7
    },
    {
      "name": "ε-ZrH₂",
      "a": 5.01,
      "c": 4.42,
      "C11": 166.0,
      "C12": 149.0,
      "C13": 109.0,
      "C33": 149.0,
      "C44": 26.5,
      "C66": 55.8,
      "E": 70.1,
      "B": 133.0,
      "G": 24.9
    }
  ]
}
EOF

# === solve block: step_03_thermodynamic_data.json ===
cat > /app/outputs/step_03_thermodynamic_data.json <<'EOF'
{
  "phases": [
    {
      "name": "α-Zr",
      "entropy": [0.0, 9.0, 22.0, 37.0, 48.0, 57.0, 64.0, 70.0, 75.0, 80.0, 84.0],
      "heat_capacity": [0.0, 17.5, 23.0, 25.0, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0],
      "enthalpy": [0.0, 0.9, 2.8, 5.3, 7.8, 10.5, 13.2, 15.9, 18.7, 21.5, 24.3],
      "enthalpy_of_formation": 0.0,
      "Debye_temperature": 277.0,
      "electronic_heat_constant": 2.50
    },
    {
      "name": "γ-ZrH",
      "entropy": [0.0, 8.0, 22.0, 36.0, 47.0, 55.0, 62.0, 68.0, 73.0, 77.0, 81.0],
      "heat_capacity": [0.0, 15.0, 35.0, 43.0, 47.0, 49.0, 50.5, 51.5, 52.0, 52.5, 52.8],
      "enthalpy": [0.0, 0.7, 2.5, 5.5, 9.0, 12.5, 16.0, 19.5, 23.0, 26.5, 30.0],
      "enthalpy_of_formation": -75.6,
      "Debye_temperature": 228.0,
      "electronic_heat_constant": 2.33
    },
    {
      "name": "δ-ZrH₁.₅",
      "entropy": [0.0, 5.0, 15.0, 28.0, 39.0, 48.0, 55.0, 61.0, 66.0, 70.0, 74.0],
      "heat_capacity": [0.0, 10.0, 25.0, 36.0, 44.0, 50.0, 55.0, 58.0, 60.0, 61.5, 62.0],
      "enthalpy": [0.0, 0.5, 2.0, 5.0, 9.0, 13.5, 18.0, 22.5, 27.0, 31.5, 36.0],
      "enthalpy_of_formation": -112.0,
      "Debye_temperature": 343.0,
      "electronic_heat_constant": 1.15
    },
    {
      "name": "ε-ZrH₂",
      "entropy": [0.0, 6.0, 18.0, 32.0, 43.0, 52.0, 59.0, 65.0, 70.0, 74.0, 78.0],
      "heat_capacity": [0.0, 12.0, 32.0, 45.0, 52.0, 56.0, 59.0, 61.0, 62.5, 63.5, 64.0],
      "enthalpy": [0.0, 0.6, 2.0, 5.0, 9.5, 14.5, 19.5, 24.5, 29.5, 34.5, 39.5],
      "enthalpy_of_formation": -153.0,
      "Debye_temperature": 284.0,
      "electronic_heat_constant": 1.30
    }
  ]
}
EOF
