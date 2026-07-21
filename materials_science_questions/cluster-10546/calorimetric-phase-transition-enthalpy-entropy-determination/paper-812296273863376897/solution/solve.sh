#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: moments.json ===
cat > /app/outputs/moments.json << 'JSONEOF'
{
  "Ia": 2.097e-38,
  "Ib": 2.569e-38,
  "Ic": 4.454e-38,
  "product_IA": 2.399e-113,
  "symmetry_number": 4,
  "I_red": 5.186e-40
}
JSONEOF

# === solve block: assigned_frequencies.csv ===
cat > /app/outputs/assigned_frequencies.csv << 'FFEOF'
mode,frequency_cm1
A_g C=C stretch,1674
A_g CH3 rock,944
A_g C-C stretch,691
A_g Skeletal bend,411
A_u CH3 rock,990
A_u Skeletal twist,165
B_1g C-C stretch,1454
B_1g CH3 rock,1028
B_1g Skeletal bend,503
B_2g CH3 rock,1072
B_2g Skeletal bend,503
B_3g CH3 rock,961