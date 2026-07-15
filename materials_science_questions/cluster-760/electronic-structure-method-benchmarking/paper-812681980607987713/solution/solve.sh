#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_energies.json ===
python3 <<'PYEOF'
import json, sys

systems = [
  {"system": "BH", "basis": "cc-pVDZ", "fci": -25.215324, "scf_err": 0.090137, "ccsd_err": 0.001853, "ccsdt_err": 0.000483},
  {"system": "CH2(3B1)", "basis": "DZP", "fci": -39.046260, "scf_err": 0.113215, "ccsd_err": 0.002090, "ccsdt_err": 0.000360},
  {"system": "NH2(2B1)", "basis": "DZP", "fci": -55.742620, "scf_err": 0.165438, "ccsd_err": 0.003273, "ccsdt_err": 0.000547},
  {"system": "Ne", "basis": "cc-pVDZ", "fci": -128.679025, "scf_err": 0.190249, "ccsd_err": 0.001233, "ccsdt_err": 0.000188},
  {"system": "F-", "basis": "cc-pVDZ", "fci": -99.558917, "scf_err": 0.192933, "ccsd_err": 0.001071, "ccsdt_err": 0.000464},
  {"system": "H2O", "basis": "cc-pVDZ", "fci": -76.241860, "scf_err": 0.217821, "ccsd_err": 0.003744, "ccsdt_err": 0.000658},
  {"system": "N2", "basis": "cc-pVDZ", "fci": -109.278340, "scf_err": 0.328783, "ccsd_err": 0.014442, "ccsdt_err": 0.001862},
]

results = []
for s in systems:
    e_scf = s["fci"] + s["scf_err"]
    e_ccsd = s["fci"] + s["ccsd_err"]
    e_ccsdt = s["fci"] + s["ccsdt_err"]
    d1 = e_scf
    d2 = e_ccsd - e_scf
    d3 = e_ccsdt - e_ccsd
    e_cf = d1 / (1.0 - (d2 / d1) / (1.0 - d3 / d2))
    results.append({
        "system": s["system"],
        "basis": s["basis"],
        "E_SCF": round(e_scf, 10),
        "E_CCSD": round(e_ccsd, 10),
        "E_CCSD(T)": round(e_ccsdt, 10),
        "E_CCSD(T)-cf": round(e_cf, 10),
    })

with open("/app/outputs/step_01_energies.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF
