#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" << 'FFEOF'
{
  "Pb2ScSbO6_GGA_bandgap": 2.712,
  "Pb2ScSbO6_mBJ_bandgap": 3.842,
  "Pb2ScTaO6_GGA_bandgap": 2.657,
  "Pb2ScTaO6_mBJ_bandgap": 3.889
}
FFEOF

# === solve block: epsilon2_onset.json ===
cat > /app/outputs/epsilon2_onset.json << 'FFEOF'
{
  "Pb2ScSbO6_GGA_onset": 2.5,
  "Pb2ScSbO6_mBJ_onset": 3.5,
  "Pb2ScTaO6_GGA_onset": 2.4,
  "Pb2ScTaO6_mBJ_onset": 3.6
}
FFEOF

# === solve block: epsilon2_peak.json ===
cat > /app/outputs/epsilon2_peak.json << 'FFEOF'
{
  "Pb2ScSbO6_GGA_peak": 6.0,
  "Pb2ScSbO6_mBJ_peak": 7.0,
  "Pb2ScTaO6_GGA_peak": 6.0,
  "Pb2ScTaO6_mBJ_peak": 7.0
}
FFEOF
