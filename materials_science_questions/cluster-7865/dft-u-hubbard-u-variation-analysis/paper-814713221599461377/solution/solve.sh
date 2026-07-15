#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'EOF'
[
  {"method": "PBE+U", "parameter": 3.0, "spin_state": "LS", "band_gap_eV": 0.6, "total_energy_eV": -36.08325},
  {"method": "PBE+U", "parameter": 5.0, "spin_state": "LS", "band_gap_eV": 1.5, "total_energy_eV": null},
  {"method": "PBE+U", "parameter": 7.0, "spin_state": "LS", "band_gap_eV": 2.3, "total_energy_eV": null},
  {"method": "PBE+U", "parameter": 3.0, "spin_state": "IS_FM", "band_gap_eV": null, "total_energy_eV": -36.20111},
  {"method": "PBE+U", "parameter": 3.0, "spin_state": "LS-HS_1:1_FM", "band_gap_eV": null, "total_energy_eV": -36.15812},
  {"method": "HSE", "parameter": 0.05, "spin_state": "LS", "band_gap_eV": 0.2, "total_energy_eV": null},
  {"method": "HSE", "parameter": 0.15, "spin_state": "LS", "band_gap_eV": 0.6, "total_energy_eV": null},
  {"method": "HSE", "parameter": 0.25, "spin_state": "LS", "band_gap_eV": 2.4, "total_energy_eV": null}
]
EOF
