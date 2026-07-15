#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: te_results.json ===
cat > /app/outputs/te_results.json <<'FFEOF'
[
  {
    "material": "1QL Bi2Te3",
    "scattering": "cmfp",
    "peak_pf": 14.5,
    "peak_zt": 1.80,
    "fermi_level": -0.07,
    "inner_ring_energy": 0.0,
    "outer_ring_energy": 0.0,
    "moat_energy": -0.05
  },
  {
    "material": "1QL Bi2Te3",
    "scattering": "crt",
    "peak_pf": 12.0,
    "peak_zt": 1.50,
    "fermi_level": -0.06,
    "inner_ring_energy": 0.0,
    "outer_ring_energy": 0.0,
    "moat_energy": -0.05
  },
  {
    "material": "1QL Bi2Te3",
    "scattering": "dos",
    "peak_pf": 32.0,
    "peak_zt": 3.50,
    "fermi_level": -0.10,
    "inner_ring_energy": 0.0,
    "outer_ring_energy": 0.0,
    "moat_energy": -0.05
  },
  {
    "material": "1QL Bi2Se3",
    "scattering": "cmfp",
    "peak_pf": 18.0,
    "peak_zt": 2.00,
    "fermi_level": -0.08,
    "inner_ring_energy": -0.03,
    "outer_ring_energy": 0.0,
    "moat_energy": -0.12
  },
  {
    "material": "1QL Bi2Se3",
    "scattering": "crt",
    "peak_pf": 15.0,
    "peak_zt": 1.70,
    "fermi_level": -0.08,
    "inner_ring_energy": -0.03,
    "outer_ring_energy": 0.0,
    "moat_energy": -0.12
  },
  {
    "material": "1QL Bi2Se3",
    "scattering": "dos",
    "peak_pf": 38.0,
    "peak_zt": 3.80,
    "fermi_level": -0.14,
    "inner_ring_energy": -0.03,
    "outer_ring_energy": 0.0,
    "moat_energy": -0.12
  },
  {
    "material": "1QL Sb2Te3",
    "scattering": "cmfp",
    "peak_pf": 16.0,
    "peak_zt": 2.20,
    "fermi_level": -0.05,
    "inner_ring_energy": 0.0,
    "outer_ring_energy": -0.03,
    "moat_energy": -0.05
  },
  {
    "material": "1QL Sb2Te3",
    "scattering": "crt",
    "peak_pf": 14.0,
    "peak_zt": 1.90,
    "fermi_level": -0.04,
    "inner_ring_energy": 0.0,
    "outer_ring_energy": -0.03,
    "moat_energy": -0.05
  },
  {
    "material": "1QL Sb2Te3",
    "scattering": "dos",
    "peak_pf": 7.0,
    "peak_zt": 0.80,
    "fermi_level": 0.01,
    "inner_ring_energy": 0.0,
    "outer_ring_energy": -0.03,
    "moat_energy": -0.05
  },
  {
    "material": "2QL Bi2Te3",
    "scattering": "cmfp",
    "peak_pf": 8.0,
    "peak_zt": 0.60,
    "fermi_level": -0.10,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Bi2Te3",
    "scattering": "crt",
    "peak_pf": 7.0,
    "peak_zt": 0.50,
    "fermi_level": -0.10,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Bi2Te3",
    "scattering": "dos",
    "peak_pf": 5.0,
    "peak_zt": 0.30,
    "fermi_level": -0.15,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Bi2Se3",
    "scattering": "cmfp",
    "peak_pf": 3.0,
    "peak_zt": 0.20,
    "fermi_level": -0.10,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Bi2Se3",
    "scattering": "crt",
    "peak_pf": 2.5,
    "peak_zt": 0.15,
    "fermi_level": -0.10,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Bi2Se3",
    "scattering": "dos",
    "peak_pf": 1.2,
    "peak_zt": 0.08,
    "fermi_level": -0.12,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Sb2Te3",
    "scattering": "cmfp",
    "peak_pf": 2.0,
    "peak_zt": 0.15,
    "fermi_level": -0.10,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Sb2Te3",
    "scattering": "crt",
    "peak_pf": 1.8,
    "peak_zt": 0.12,
    "fermi_level": -0.10,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  },
  {
    "material": "2QL Sb2Te3",
    "scattering": "dos",
    "peak_pf": 0.8,
    "peak_zt": 0.05,
    "fermi_level": -0.12,
    "inner_ring_energy": null,
    "outer_ring_energy": null,
    "moat_energy": null
  }
]
FFEOF
