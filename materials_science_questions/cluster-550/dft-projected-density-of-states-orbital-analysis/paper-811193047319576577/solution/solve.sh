#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_ir_frequencies.csv ===
cat > "$OUTDIR/computed_ir_frequencies.csv" << 'CSVEOF'
compound,band_label,frequency_cm1,present
H2PAPS,"ν(C=O)¹",1719,True
H2PAPS,"ν(C=O)²",1669,True
H2PAPS,"ν(C=O)³",1651,True
H2PAPS,"ν(C=N)",1559,True
H2PAPS,"ν(N‐N)",1055,True
[Cr(H2PAPS)Cl3],"ν(C=O)¹",1711,True
[Cr(H2PAPS)Cl3],"ν(C=O)²",1687,True
[Cr(H2PAPS)Cl3],"ν(C=O)³",,False
[Cr(H2PAPS)Cl3],"ν(C=N)",1565,True
[Cr(H2PAPS)Cl3],"ν(N‐N)",1051,True
H2PAPT,"ν(C=O)¹",1717,True
H2PAPT,"ν(C=O)²",1672,True
H2PAPT,"ν(C=O)³",,False
H2PAPT,"ν(C=N)",,False
H2PAPT,"ν(N‐N)",1103,True
H2PAPT,"ν(C=S)",1363,True
H2PAPT,"ν(SH)",,False
[Cr(HPAPT)Cl2(H2O)2],"ν(C=O)¹",,False
[Cr(HPAPT)Cl2(H2O)2],"ν(C=O)²",1631,True
[Cr(HPAPT)Cl2(H2O)2],"ν(C=O)³",,False
[Cr(HPAPT)Cl2(H2O)2],"ν(C=N)",,False
[Cr(HPAPT)Cl2(H2O)2],"ν(N‐N)",1075,True
[Cr(HPAPT)Cl2(H2O)2],"ν(C=S)",1363,True
[Cr(HPAPT)Cl2(H2O)2],"ν(SH)",,False
H2PABT,"ν(C=O)¹",1710,True
H2PABT,"ν(C=O)²",1668,True
H2PABT,"ν(C=O)³",1681,True
H2PABT,"ν(C=N)",1581,True
H2PABT,"ν(N‐N)",1025,True
H2PABT,"ν(C=S)",,False
H2PABT,"ν(SH)",2360,True
[Cr(HPABT)Cl2(H2O)],"ν(C=O)¹",,False
[Cr(HPABT)Cl2(H2O)],"ν(C=O)²",1658,True
[Cr(HPABT)Cl2(H2O)],"ν(C=O)³",1673,True
[Cr(HPABT)Cl2(H2O)],"ν(C=N)",,False
[Cr(HPABT)Cl2(H2O)],"ν(N‐N)",1027,True
[Cr(HPABT)Cl2(H2O)],"ν(C=S)",1492,True
[Cr(HPABT)Cl2(H2O)],"ν(SH)",,False
CSVEOF

# === solve block: computed_homo_lumo_gaps.csv ===
python3 /solution/generate_outputs.py --output computed_homo_lumo_gaps.csv

# === solve block: computed_binding_energies.csv ===
python3 /solution/generate_outputs.py --output computed_binding_energies.csv
