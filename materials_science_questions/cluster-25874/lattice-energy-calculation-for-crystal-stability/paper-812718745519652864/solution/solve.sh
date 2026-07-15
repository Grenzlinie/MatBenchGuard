#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: table1_results.json ===
cat > /app/outputs/table1_results.json <<'EOF'
{
  "1Si": {
    "exp": {
      "Elatt": 15.9,
      "Eform": 14.5,
      "Volume": 181.5,
      "HS_area": 188.0,
      "Elatt_HS_ratio": 0.0846
    },
    "DFT": {
      "Elatt": 16.1,
      "Eform": 13.8,
      "Volume": 157.2,
      "HS_area": 172.8,
      "Elatt_HS_ratio": 0.0932
    },
    "DFT in [1C]": {
      "Elatt": 15.3,
      "Eform": 13.4,
      "Volume": 162.3,
      "HS_area": 168.5,
      "Elatt_HS_ratio": 0.0908
    }
  },
  "1C": {
    "exp": {
      "Elatt": 13.5,
      "Eform": 13.1,
      "Volume": 155.4,
      "HS_area": 159.4,
      "Elatt_HS_ratio": 0.0847
    },
    "DFT": {
      "Elatt": 13.7,
      "Eform": 12.5,
      "Volume": 141.3,
      "HS_area": 150.7,
      "Elatt_HS_ratio": 0.0909
    },
    "DFT in [1Si]": {
      "Elatt": 12.4,
      "Eform": 10.9,
      "Volume": 146.4,
      "HS_area": 160.5,
      "Elatt_HS_ratio": 0.0772
    }
  }
}
EOF
