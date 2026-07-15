#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: oscillator_strengths_odd_vibrations.json ===
python3 -c '
import json
data = [
  {"transition": "6A1g→4T2g(1)", "vibration_mode": "T1u(nu3)", "oscillator_strength": 5.56e-07},
  {"transition": "6A1g→4T2g(1)", "vibration_mode": "T1u(nu4)", "oscillator_strength": 3.44e-07},
  {"transition": "6A1g→4T2g(1)", "vibration_mode": "T2u(nu6)", "oscillator_strength": 4.7e-08},
  {"transition": "6A1g→4Eg(1)",  "vibration_mode": "T1u(nu3)", "oscillator_strength": 3.94e-07},
  {"transition": "6A1g→4Eg(1)",  "vibration_mode": "T1u(nu4)", "oscillator_strength": 1.22e-07},
  {"transition": "6A1g→4Eg(1)",  "vibration_mode": "T2u(nu6)", "oscillator_strength": 4.59e-07},
  {"transition": "6A1g→4A1g",    "vibration_mode": "T1u(nu3)", "oscillator_strength": 2.69e-07},
  {"transition": "6A1g→4A1g",    "vibration_mode": "T1u(nu4)", "oscillator_strength": 8.9e-08},
  {"transition": "6A1g→4A1g",    "vibration_mode": "T2u(nu6)", "oscillator_strength": 2.95e-07},
  {"transition": "6A1g→4T1g(1)", "vibration_mode": "T1u(nu3)", "oscillator_strength": 1.52e-07},
  {"transition": "6A1g→4T1g(1)", "vibration_mode": "T1u(nu4)", "oscillator_strength": 2.61e-07},
  {"transition": "6A1g→4T1g(1)", "vibration_mode": "T2u(nu6)", "oscillator_strength": 1.1e-08}
]
with open("/app/outputs/oscillator_strengths_odd_vibrations.json", "w") as f:
  json.dump(data, f, indent=2)
'

# === solve block: oscillator_strengths_odd_crystal_field.json ===
python3 -c '
import json
data = [
  {"transition": "6A1g→4T2g(1):→4E", "polarization": "σ", "oscillator_strength": 3.47e-07},
  {"transition": "6A1g→4Eg(1):→4E",  "polarization": "σ", "oscillator_strength": 3.75e-07},
  {"transition": "6A1g→4T1g(1):→4E", "polarization": "σ", "oscillator_strength": 4.49e-07},
  {"transition": "6A1g→4T1g(1):→4A2","polarization": "π", "oscillator_strength": 2.24e-07}
]
with open("/app/outputs/oscillator_strengths_odd_crystal_field.json", "w") as f:
  json.dump(data, f, indent=2)
'

# === solve block: faraday_parameters_odd_vibrations.json ===
python3 -c '
import json
data = [
  {"transition": "6A1g→4T2g(1)", "vibration_mode": "T1u(nu3)", "A": -251.5, "B": 0.180, "C": 649.4, "B_plus_C_over_kT": 3.427},
  {"transition": "6A1g→4T2g(1)", "vibration_mode": "T1u(nu4)", "A": -42.1, "B": 0.039, "C": 148.1, "B_plus_C_over_kT": 0.780},
  {"transition": "6A1g→4T2g(1)", "vibration_mode": "T2u(nu6)", "A": 6.8, "B": 0.040, "C": -20.5, "B_plus_C_over_kT": -0.063},
  {"transition": "6A1g→4Eg(1)",  "vibration_mode": "T1u(nu3)", "A": -170.6, "B": -0.411, "C": 331.6, "B_plus_C_over_kT": 1.247},
  {"transition": "6A1g→4Eg(1)",  "vibration_mode": "T1u(nu4)", "A": -15.7, "B": 0.231, "C": 30.6, "B_plus_C_over_kT": 0.384},
  {"transition": "6A1g→4Eg(1)",  "vibration_mode": "T2u(nu6)", "A": 180.2, "B": 0.033, "C": -350.3, "B_plus_C_over_kT": -1.719},
  {"transition": "6A1g→4A1g",    "vibration_mode": "T1u(nu3)", "A": 107.8, "B": 0.342, "C": -209.6, "B_plus_C_over_kT": -0.706},
  {"transition": "6A1g→4A1g",    "vibration_mode": "T1u(nu4)", "A": 35.2, "B": -0.214, "C": -68.4, "B_plus_C_over_kT": -0.556},
  {"transition": "6A1g→4A1g",    "vibration_mode": "T2u(nu6)", "A": -118.8, "B": 0.057, "C": 231.0, "B_plus_C_over_kT": 1.212}
]
with open("/app/outputs/faraday_parameters_odd_vibrations.json", "w") as f:
  json.dump(data, f, indent=2)
'

# === solve block: faraday_parameters_odd_crystal_field.json ===
python3 -c '
import json
data = [
  {"transition": "6A1g→4T2g(1):→4E", "A": 176.5, "B": -0.104, "C": -338.0, "B_plus_C_over_kT": -1.794},
  {"transition": "6A1g→4Eg(1):→4E",  "A": -74.8, "B": 0.104, "C": 145.4, "B_plus_C_over_kT": 0.831}
]
with open("/app/outputs/faraday_parameters_odd_crystal_field.json", "w") as f:
  json.dump(data, f, indent=2)
'
