#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: extrapolated_values_ccsd.csv ===
#!/bin/bash
mkdir -p /app/outputs
cat > /app/outputs/extrapolated_values_ccsd.csv <<'FFEOF'
molecule,property,extrapolated_value,method
GeH4,AE,274.13,CCSD(T)
AsH,AE,63.54,CCSD(T)
AsH2,AE,131.78,CCSD(T)
AsH3,AE,204.67,CCSD(T)
SeH,AE,74.62,CCSD(T)
SeH2,AE,152.39,CCSD(T)
HBr,AE,86.44,CCSD(T)
GeO,AE,155.99,CCSD(T)
GeS2,AE,194.39,CCSD(T)
As2,AE,90.29,CCSD(T)
BrCl,AE,52.07,CCSD(T)
BrF,AE,59.66,CCSD(T)
BrO,AE,54.83,CCSD(T)
BBr,AE,100.50,CCSD(T)
Br2,AE,45.40,CCSD(T)
CH3Br,AE,357.12,CCSD(T)
GaCl,AE,109.73,CCSD(T)
KrF2,AE,21.31,CCSD(T)
NaBr,AE,87.73,CCSD(T)
Ga,IE,5.953,CCSD(T)
Ge,IE,7.841,CCSD(T)
As,IE,9.741,CCSD(T)
Se,IE,9.734,CCSD(T)
Br,IE,11.822,CCSD(T)
Kr,IE,13.978,CCSD(T)
AsH,IE,9.625,CCSD(T)
AsH2,IE,9.387,CCSD(T)
SeH,IE,9.868,CCSD(T)
SeH2,IE,9.884,CCSD(T)
HBr,IE,11.649,CCSD(T)
BrF,IE,11.759,CCSD(T)
HOBr,IE,10.693,CCSD(T)
Br2,IE,10.544,CCSD(T)
NaBr,IE,8.467,CCSD(T)
Ge,EA,1.261,CCSD(T)
Br,EA,3.399,CCSD(T)
SeH,EA,2.219,CCSD(T)
BrO,EA,2.464,CCSD(T)
HBr,PA,13.956,CCSD(T)
CH3Br,PA,6.814,CCSD(T)
FFEOF

# === solve block: extrapolated_values_b3lyp.csv ===
cat > /app/outputs/extrapolated_values_b3lyp.csv <<'FFEOF'
molecule,property,extrapolated_value,method
GeH4,AE,273.79,B3LYP
AsH,AE,67.40,B3LYP
AsH2,AE,137.24,B3LYP
AsH3,AE,209.76,B3LYP
SeH,AE,76.41,B3LYP
SeH2,AE,153.01,B3LYP
HBr,AE,85.28,B3LYP
GeO,AE,154.52,B3LYP
GeS2,AE,186.80,B3LYP
As2,AE,92.72,B3LYP
BrCl,AE,49.03,B3LYP
BrF,AE,58.54,B3LYP
BrO,AE,58.05,B3LYP
BBr,AE,97.70,B3LYP
Br2,AE,42.69,B3LYP
CH3Br,AE,355.84,B3LYP
GaCl,AE,107.16,B3LYP
KrF2,AE,26.73,B3LYP
NaBr,AE,80.64,B3LYP
Ga,IE,6.090,B3LYP
Ge,IE,7.844,B3LYP
As,IE,9.658,B3LYP
Se,IE,9.952,B3LYP
Br,IE,11.910,B3LYP
Kr,IE,13.935,B3LYP
AsH,IE,9.598,B3LYP
AsH2,IE,9.503,B3LYP
SeH,IE,9.967,B3LYP
SeH2,IE,9.866,B3LYP
HBr,IE,11.603,B3LYP
BrF,IE,11.659,B3LYP
HOBr,IE,10.533,B3LYP
Br2,IE,10.331,B3LYP
NaBr,IE,8.566,B3LYP
Ge,EA,1.257,B3LYP
Br,EA,3.396,B3LYP
SeH,EA,2.233,B3LYP
BrO,EA,2.293,B3LYP
HBr,PA,13.969,B3LYP
CH3Br,PA,6.844,B3LYP
FFEOF

# === solve block: metrics_summary.json ===
cat > /app/outputs/metrics_summary.json <<'FFEOF'
[
  {
    "method": "CCSD(T)",
    "per_property_mad": [
      {"property": "AE", "mad_kcal_mol": 1.06},
      {"property": "IE", "mad_kcal_mol": 0.646},
      {"property": "EA", "mad_kcal_mol": 1.038},
      {"property": "PA", "mad_kcal_mol": 0.577}
    ],
    "total_mad_kcal_mol": 0.87
  },
  {
    "method": "B3LYP",
    "per_property_mad": [
      {"property": "AE", "mad_kcal_mol": 2.53},
      {"property": "IE", "mad_kcal_mol": 2.491},
      {"property": "EA", "mad_kcal_mol": 0.830},
      {"property": "PA", "mad_kcal_mol": 0.634}
    ],
    "total_mad_kcal_mol": 2.25
  }
]
FFEOF

# === solve finalize ===
echo 'Oracle artifacts written.'
