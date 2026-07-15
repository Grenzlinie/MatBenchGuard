#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relative_energies.json ===
# Write the electromer energies as a JSON array
cat > "$OUTDIR/relative_energies.json" << 'FFEOF'
[
  {"complex": "I_n0", "electromer": "LS_LS", "S": 2, "E_au": -6377.080699, "dE_kcal": 0.0, "S2": 6.031},
  {"complex": "I_n0", "electromer": "LS_HS", "S": 3, "E_au": -6377.071280, "dE_kcal": 5.9, "S2": 12.027},
  {"complex": "I_n0", "electromer": "HS_HS", "S": 4, "E_au": -6377.061871, "dE_kcal": 11.8, "S2": 20.024},
  {"complex": "I_n0", "electromer": "LS_LS_cat", "S": 0, "E_au": -6377.051979, "dE_kcal": 18.0, "S2": 0.000},
  {"complex": "I_n2", "electromer": "LS_LS", "S": 3, "E_au": -6991.796253, "dE_kcal": 0.0, "S2": 12.064},
  {"complex": "I_n2", "electromer": "LS_HS", "S": 4, "E_au": -6991.786625, "dE_kcal": 6.0, "S2": 20.060},
  {"complex": "I_n2", "electromer": "HS_HS", "S": 5, "E_au": -6991.777278, "dE_kcal": 11.9, "S2": 30.057},
  {"complex": "II_n1", "electromer": "LS_LS", "S": 3, "E_au": -6606.928851, "dE_kcal": 0.0, "S2": 12.082},
  {"complex": "II_n1", "electromer": "LS_HS", "S": 4, "E_au": -6606.919454, "dE_kcal": 5.9, "S2": 20.079},
  {"complex": "II_n1", "electromer": "HS_HS", "S": 5, "E_au": -6606.909993, "dE_kcal": 11.8, "S2": 30.075},
  {"complex": "III_n2", "electromer": "LS", "S": 2, "E_au": -4304.242415, "dE_kcal": 0.0, "S2": 6.049},
  {"complex": "III_n2", "electromer": "HS", "S": 3, "E_au": -4304.232424, "dE_kcal": 6.3, "S2": 12.045},
  {"complex": "IV_n1", "electromer": "LS", "S": 2, "E_au": -3919.375659, "dE_kcal": 0.0, "S2": 6.067},
  {"complex": "IV_n1", "electromer": "HS", "S": 3, "E_au": -3919.365839, "dE_kcal": 6.2, "S2": 12.064}
]
FFEOF

# === solve block: exchange_parameters.json ===
# Write the exchange coupling constants as a JSON object
cat > "$OUTDIR/exchange_parameters.json" << 'FFEOF'
{
  "I_n0_LS_LS": {
    "J12": 535,
    "J13": 1,
    "J14": 9,
    "J23": -17,
    "J24": 1,
    "J34": 535
  },
  "I_n0_LS_HS": {
    "J12": 570,
    "J13": 47,
    "J14": 15,
    "J23": -49,
    "J24": -10,
    "J34": -92
  },
  "I_n0_HS_HS": {
    "J12": -78,
    "J13": 1,
    "J14": 4,
    "J23": -53,
    "J24": 1,
    "J34": -78
  },
  "III_n2_LS": {
    "J12": 426,
    "J13": -81,
    "J14": 556,
    "J23": -503,
    "J24": 82,
    "J34": -1694
  },
  "III_n2_HS": {
    "J12": -183,
    "J13": -160,
    "J14": 49,
    "J23": -785,
    "J24": -241,
    "J34": -1832
  },
  "IV_n1_LS": {
    "J12": 610,
    "J13": -123,
    "J14": -123,
    "J23": -388,
    "J24": -388,
    "J34": -1277
  },
  "IV_n1_HS": {
    "J12": -154,
    "J13": 23,
    "J14": 23,
    "J23": -544,
    "J24": -544,
    "J34": -1207
  }
}
FFEOF
