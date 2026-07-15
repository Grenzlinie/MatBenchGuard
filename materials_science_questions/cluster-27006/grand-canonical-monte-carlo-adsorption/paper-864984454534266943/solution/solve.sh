#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: structural_properties.json ===
cat > "$OUTDIR/structural_properties.json" <<'FFEOF'
[
  {
    "mof": "MFM-126",
    "pld": 3.80,
    "lcd": 8.00,
    "lcd_pl": 2.105,
    "total_sa": 1250.0,
    "volume": 0.72,
    "void_fraction": 0.55
  },
  {
    "mof": "MFM-127",
    "pld": 4.80,
    "lcd": 9.20,
    "lcd_pl": 1.917,
    "total_sa": 1820.0,
    "volume": 0.78,
    "void_fraction": 0.58
  },
  {
    "mof": "MFM-128",
    "pld": 3.70,
    "lcd": 7.60,
    "lcd_pl": 2.054,
    "total_sa": 1700.0,
    "volume": 0.76,
    "void_fraction": 0.56
  },
  {
    "mof": "MFM-136",
    "pld": 6.20,
    "lcd": 12.40,
    "lcd_pl": 2.000,
    "total_sa": 1980.0,
    "volume": 1.02,
    "void_fraction": 0.61
  },
  {
    "mof": "MFM-137",
    "pld": 3.50,
    "lcd": 7.20,
    "lcd_pl": 2.057,
    "total_sa": 1890.0,
    "volume": 1.35,
    "void_fraction": 0.64
  },
  {
    "mof": "MFM-138",
    "pld": 3.60,
    "lcd": 7.50,
    "lcd_pl": 2.083,
    "total_sa": 1780.0,
    "volume": 1.06,
    "void_fraction": 0.62
  }
]
FFEOF

# === solve block: selectivity_summary.json ===
cat > "$OUTDIR/selectivity_summary.json" <<'FFEOF'
{
  "S_50_50_273_0.01": {
    "MFM-126": 61.0,
    "MFM-127": 51.98,
    "MFM-128": 36.0,
    "MFM-136": 55.0,
    "MFM-137": 48.0,
    "MFM-138": 54.0
  },
  "S_50_50_273_10": {
    "MFM-126": 4.14,
    "MFM-127": 7.0,
    "MFM-128": 5.5,
    "MFM-136": 6.0,
    "MFM-137": 9.22,
    "MFM-138": 8.5
  },
  "S_50_50_298_0.01": {
    "MFM-126": 51.65,
    "MFM-127": 52.16,
    "MFM-128": 35.29,
    "MFM-136": 46.21,
    "MFM-137": 40.64,
    "MFM-138": 45.91
  },
  "S_50_50_298_10": {
    "MFM-126": 3.99,
    "MFM-127": 5.73,
    "MFM-128": 4.96,
    "MFM-136": 5.19,
    "MFM-137": 7.96,
    "MFM-138": 8.37
  },
  "S_20_80_273_0.01": {
    "MFM-126": 23.0,
    "MFM-127": 27.26,
    "MFM-128": 22.0,
    "MFM-136": 20.0,
    "MFM-137": 19.56,
    "MFM-138": 28.0
  },
  "S_20_80_273_10": {
    "MFM-126": 5.01,
    "MFM-127": 8.5,
    "MFM-128": 7.0,
    "MFM-136": 7.5,
    "MFM-137": 9.5,
    "MFM-138": 10.12
  },
  "S_20_80_298_0.01": {
    "MFM-126": 19.15,
    "MFM-127": 20.36,
    "MFM-128": 19.01,
    "MFM-136": 18.34,
    "MFM-137": 15.24,
    "MFM-138": 23.33
  },
  "S_20_80_298_10": {
    "MFM-126": 4.85,
    "MFM-127": 6.57,
    "MFM-128": 6.35,
    "MFM-136": 6.19,
    "MFM-137": 8.37,
    "MFM-138": 8.93
  }
}
FFEOF

# === solve block: thermodynamic_properties.json ===
cat > "$OUTDIR/thermodynamic_properties.json" <<'FFEOF'
{
  "Qst_Xe": {
    "MFM-126": 26.31,
    "MFM-127": 25.29,
    "MFM-128": 26.44,
    "MFM-136": 25.74,
    "MFM-137": 25.08,
    "MFM-138": 28.40
  },
  "Qst_Kr": {
    "MFM-126": 18.95,
    "MFM-127": 18.22,
    "MFM-128": 19.03,
    "MFM-136": 18.62,
    "MFM-137": 18.54,
    "MFM-138": 20.34
  },
  "K_H_Xe": {
    "MFM-126": 22.2,
    "MFM-127": 20.8,
    "MFM-128": 24.2,
    "MFM-136": 19.9,
    "MFM-137": 16.5,
    "MFM-138": 36.0
  },
  "K_H_Kr": {
    "MFM-126": 2.23,
    "MFM-127": 2.08,
    "MFM-128": 2.27,
    "MFM-136": 2.15,
    "MFM-137": 1.95,
    "MFM-138": 3.08
  },
  "Henry_selectivity": {
    "MFM-126": 9.96,
    "MFM-127": 9.98,
    "MFM-128": 10.66,
    "MFM-136": 9.34,
    "MFM-137": 8.46,
    "MFM-138": 11.68
  }
}
FFEOF
