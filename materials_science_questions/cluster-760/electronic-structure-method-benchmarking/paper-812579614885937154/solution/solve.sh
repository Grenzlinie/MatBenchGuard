#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ionization_energies.json ===
cat > /app/outputs/ionization_energies.json <<'FFEOF'
[
  {"orbital": "14a", "energy_eV": 9.52, "method": "OVGF/TZVP"},
  {"orbital": "13b", "energy_eV": 9.67, "method": "OVGF/TZVP"},
  {"orbital": "12b", "energy_eV": 11.51, "method": "OVGF/TZVP"},
  {"orbital": "13a", "energy_eV": 11.91, "method": "OVGF/TZVP"},
  {"orbital": "12a", "energy_eV": 12.23, "method": "OVGF/TZVP"},
  {"orbital": "11a", "energy_eV": 12.53, "method": "OVGF/TZVP"},
  {"orbital": "10a", "energy_eV": 13.70, "method": "OVGF/TZVP"},
  {"orbital": "11b", "energy_eV": 13.73, "method": "OVGF/TZVP"},
  {"orbital": "10b", "energy_eV": 13.89, "method": "OVGF/TZVP"},
  {"orbital": "9b", "energy_eV": 14.57, "method": "OVGF/TZVP"},
  {"orbital": "8b", "energy_eV": 14.73, "method": "OVGF/TZVP"},
  {"orbital": "9a", "energy_eV": 14.43, "method": "OVGF/TZVP"},
  {"orbital": "8a", "energy_eV": 14.36, "method": "OVGF/TZVP"},
  {"orbital": "7b", "energy_eV": 15.25, "method": "OVGF/TZVP"},
  {"orbital": "6b", "energy_eV": 16.76, "method": "OVGF/TZVP"},
  {"orbital": "7a", "energy_eV": 16.46, "method": "OVGF/TZVP"},
  {"orbital": "6a", "energy_eV": 17.11, "method": "OVGF/TZVP"},
  {"orbital": "5b", "energy_eV": 17.01, "method": "OVGF/TZVP"}
]
FFEOF
