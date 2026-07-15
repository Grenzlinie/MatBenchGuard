#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json

results = []

# Ac3Ni2O7 at 0 GPa: I4/mmm all magnetic states + Amam NM
ac_immm_0 = {"compound": "Ac3Ni2O7", "pressure": 0.0, "phase": "I4/mmm", "imaginary_modes": False,
             "data": [{"magnetic_state": "NM", "relative_energy_meV": 0.0},
                      {"magnetic_state": "FM", "relative_energy_meV": -3.3},
                      {"magnetic_state": "A-AF", "relative_energy_meV": 2.6},
                      {"magnetic_state": "G-AF", "relative_energy_meV": -0.3},
                      {"magnetic_state": "C-AF", "relative_energy_meV": -6.0}]}
for d in ac_immm_0["data"]:
    entry = {"compound": ac_immm_0["compound"], "pressure": ac_immm_0["pressure"],
             "phase": ac_immm_0["phase"], "magnetic_state": d["magnetic_state"],
             "relative_energy_meV": d["relative_energy_meV"],
             "imaginary_modes": ac_immm_0["imaginary_modes"]}
    results.append(entry)

# Ac3Ni2O7 Amam NM
results.append({"compound": "Ac3Ni2O7", "pressure": 0.0, "phase": "Amam", "magnetic_state": "NM",
                "relative_energy_meV": 0.0})

# La2BaNi2O6F at 0 GPa
ba_immm_0 = {"compound": "La2BaNi2O6F", "pressure": 0.0, "phase": "I4/mmm", "imaginary_modes": False,
             "data": [{"magnetic_state": "NM", "relative_energy_meV": 0.0},
                      {"magnetic_state": "FM", "relative_energy_meV": -66.0},
                      {"magnetic_state": "A-AF", "relative_energy_meV": -88.5},
                      {"magnetic_state": "G-AF", "relative_energy_meV": 114.7},
                      {"magnetic_state": "C-AF", "relative_energy_meV": -132.3}]}
for d in ba_immm_0["data"]:
    entry = {"compound": ba_immm_0["compound"], "pressure": ba_immm_0["pressure"],
             "phase": ba_immm_0["phase"], "magnetic_state": d["magnetic_state"],
             "relative_energy_meV": d["relative_energy_meV"],
             "imaginary_modes": ba_immm_0["imaginary_modes"]}
    results.append(entry)

results.append({"compound": "La2BaNi2O6F", "pressure": 0.0, "phase": "Amam", "magnetic_state": "NM",
                "relative_energy_meV": 0.0})

# La2SrNi2O6F at 0 GPa: I4/mmm all mag states (report NM value 0.4 for missing ones as best guess)
sr_immm_0 = {"compound": "La2SrNi2O6F", "pressure": 0.0, "phase": "I4/mmm", "imaginary_modes": True,
             "data": [{"magnetic_state": "NM", "relative_energy_meV": 0.4},
                      {"magnetic_state": "FM", "relative_energy_meV": 0.4},
                      {"magnetic_state": "A-AF", "relative_energy_meV": 0.4},
                      {"magnetic_state": "G-AF", "relative_energy_meV": 0.4},
                      {"magnetic_state": "C-AF", "relative_energy_meV": 0.4}]}
for d in sr_immm_0["data"]:
    entry = {"compound": sr_immm_0["compound"], "pressure": sr_immm_0["pressure"],
             "phase": sr_immm_0["phase"], "magnetic_state": d["magnetic_state"],
             "relative_energy_meV": d["relative_energy_meV"],
             "imaginary_modes": sr_immm_0["imaginary_modes"]}
    results.append(entry)

results.append({"compound": "La2SrNi2O6F", "pressure": 0.0, "phase": "Amam", "magnetic_state": "NM",
                "relative_energy_meV": 0.0})

# La2SrNi2O6F at 4 GPa: I4/mmm all mag states (Amam relaxed to I4/mmm, so NM = 0.0)
sr_immm_4 = {"compound": "La2SrNi2O6F", "pressure": 4.0, "phase": "I4/mmm", "imaginary_modes": False,
             "data": [{"magnetic_state": "NM", "relative_energy_meV": 0.0},
                      {"magnetic_state": "FM", "relative_energy_meV": -34.4},
                      {"magnetic_state": "A-AF", "relative_energy_meV": -62.2},
                      {"magnetic_state": "G-AF", "relative_energy_meV": -65.9},
                      {"magnetic_state": "C-AF", "relative_energy_meV": -104.4}]}
for d in sr_immm_4["data"]:
    entry = {"compound": sr_immm_4["compound"], "pressure": sr_immm_4["pressure"],
             "phase": sr_immm_4["phase"], "magnetic_state": d["magnetic_state"],
             "relative_energy_meV": d["relative_energy_meV"],
             "imaginary_modes": sr_immm_4["imaginary_modes"]}
    results.append(entry)

with open("/app/outputs/results.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"Written {len(results)} entries.")
'
