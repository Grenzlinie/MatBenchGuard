#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_perfect_crystal.json ===
cat > "$OUTDIR/step_01_perfect_crystal.json" <<'S1EOF'
{
  "a": 5.3390,
  "b": 7.3727,
  "c": 5.1746,
  "density": 5.345,
  "static_dielectric_constant": 15.96,
  "high_frequency_dielectric_constant": 3.82,
  "lattice_energy": -155.92,
  "interatomic_distances": [
    {"atom_pair": "Y-Y", "calculated": 3.640, "experimental": 3.642},
    {"atom_pair": "Al-Al", "calculated": 3.686, "experimental": 3.687},
    {"atom_pair": "Y-Al (3.145)", "calculated": 3.145, "experimental": 3.184},
    {"atom_pair": "Y-Al (3.234)", "calculated": 3.234, "experimental": 3.236},
    {"atom_pair": "Y-Al (3.023)", "calculated": 3.023, "experimental": 3.015},
    {"atom_pair": "Y-Al (3.471)", "calculated": 3.471, "experimental": 3.475},
    {"atom_pair": "Al-Oi", "calculated": 1.899, "experimental": 1.901},
    {"atom_pair": "Al-Oii (1.910)", "calculated": 1.910, "experimental": 1.911},
    {"atom_pair": "Al-O (1.929)", "calculated": 1.929, "experimental": 1.921},
    {"atom_pair": "Y-Oi (2.326)", "calculated": 2.326, "experimental": 2.306},
    {"atom_pair": "Y-Oi (3.097)", "calculated": 3.097, "experimental": 3.119},
    {"atom_pair": "Y-Oi (2.232)", "calculated": 2.232, "experimental": 2.237},
    {"atom_pair": "Y-Oi (3.002)", "calculated": 3.002, "experimental": 3.010},
    {"atom_pair": "Y-Oii (2.495)", "calculated": 2.495, "experimental": 2.480},
    {"atom_pair": "Y-Oii (3.268)", "calculated": 3.268, "experimental": 3.262},
    {"atom_pair": "Y-Oii (2.266)", "calculated": 2.266, "experimental": 2.283},
    {"atom_pair": "Y-Oii (2.567)", "calculated": 2.567, "experimental": 2.570}
  ]
}
S1EOF

# === solve block: step_02_isolated_defects.json ===
cat > "$OUTDIR/step_02_isolated_defects.json" <<'S2EOF'
{
  "O_vacancy": 18.87,
  "O_interstitial": -44.34,
  "Al_vacancy": 65.84,
  "Al_interstitial": -53.67,
  "Y_vacancy": 52.01,
  "Y_interstitial": -31.42,
  "Y_antisite_on_Al": 16.71,
  "Al_antisite_on_Y": -9.34
}
S2EOF

# === solve block: step_03_disorder_energies.json ===
cat > "$OUTDIR/step_03_disorder_energies.json" <<'S3EOF'
{
  "oxygen_Frenkel": -12.74,
  "yttrium_Frenkel": 10.30,
  "aluminum_Frenkel": 6.09,
  "YAlO3_Schottky": 3.71,
  "Al2O3_Schottky": 3.54,
  "Y2O3_Schottky": 3.81
}
S3EOF

# === solve block: step_04_redox_energies.json ===
cat > "$OUTDIR/step_04_redox_energies.json" <<'S4EOF'
{
  "oxidation_vacancy_filling": 9.09,
  "oxidation_interstitial": -16.38,
  "reduction": 20.63,
  "band_gap_estimate": 7.43
}
S4EOF

# === solve block: step_05_migration_barriers.json ===
cat > "$OUTDIR/step_05_migration_barriers.json" <<'S5EOF'
{
  "1->2": 0.99,
  "2->6": 0.99,
  "1->3": 0.52,
  "3->6": 0.52,
  "1->4": 0.30,
  "4->6": 0.30,
  "1->5": 0.15,
  "5->6": 0.15,
  "2->3": 0.31,
  "3->4": 0.69,
  "4->5": 0.29,
  "5->2": 0.69
}
S5EOF
