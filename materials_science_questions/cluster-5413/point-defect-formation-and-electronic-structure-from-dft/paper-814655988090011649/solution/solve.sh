#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_bulk_verification.csv ===
cat > "$OUTDIR/step_01_bulk_verification.csv" <<'CSVEOF'
property,value,unit
lattice_constant,1.0545,nm
bulk_modulus,148.0,GPa
band_gap,4.01,eV
CSVEOF

# === solve block: step_03_adsorption_energies.csv ===
cat > "$OUTDIR/step_03_adsorption_energies.csv" <<'CSVEOF'
site,adsorption_energy_kJ_per_mol,adsorption_energy_with_ZPE_kJ_per_mol,notes
A,-299.52,-295.68,most stable fourfold hollow site; strong chemisorption
C,-262.08,-257.28,on top of oxygen in second layer
E,-261.12,-256.32,Er-Er bridge site
CSVEOF

# === solve block: step_04_penetration_and_diffusion.json ===
cat > "$OUTDIR/step_04_penetration_and_diffusion.json" <<'JSONEOF'
{
  "penetration_energy_barrier_eV": 1.60,
  "TS_to_TS_barrier_eV": 0.16,
  "TS_to_OS_barrier_eV": 0.41,
  "OS_to_OS_barrier_eV": 1.64
}
JSONEOF

# === solve block: step_05_vacancy_trapping.json ===
cat > "$OUTDIR/step_05_vacancy_trapping.json" <<'JSONEOF'
{
  "h_near_vacancy_relative_energy_eV": -0.5
}
JSONEOF
