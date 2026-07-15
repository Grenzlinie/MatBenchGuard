#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_frequencies.json ===
cat > /app/outputs/computed_frequencies.json <<'JSONEOF'
[
  {"cluster": "K4[Si3Ge]", "mode": "v1(A1)", "frequency": 435.0, "symmetry": "A1"},
  {"cluster": "K4[Si3Ge]", "mode": "v3(E)", "frequency": 322.0, "symmetry": "E"},
  {"cluster": "K4[Si3Ge]", "mode": "v2(A1)", "frequency": 255.0, "symmetry": "A1"},
  {"cluster": "K4[Si3Ge]", "mode": "v4(E)", "frequency": 232.0, "symmetry": "E"},
  {"cluster": "K4[Si2Ge2]", "mode": "v1(A1)", "frequency": 394.0, "symmetry": "A1"},
  {"cluster": "K4[Si2Ge2]", "mode": "v5(B1)", "frequency": 285.0, "symmetry": "B1"},
  {"cluster": "K4[Si2Ge2]", "mode": "v2(A1)", "frequency": 256.0, "symmetry": "A1"},
  {"cluster": "K4[Si2Ge2]", "mode": "v6(B2)", "frequency": 237.0, "symmetry": "B2"},
  {"cluster": "K4[Si2Ge2]", "mode": "v4(A2)", "frequency": 212.0, "symmetry": "A2"},
  {"cluster": "K4[Si2Ge2]", "mode": "v3(A1)", "frequency": 177.0, "symmetry": "A1"},
  {"cluster": "K4[SiGe3]", "mode": "v1(A1)", "frequency": 340.0, "symmetry": "A1"},
  {"cluster": "K4[SiGe3]", "mode": "v3(E)", "frequency": 225.0, "symmetry": "E"},
  {"cluster": "K4[SiGe3]", "mode": "v2(A1)", "frequency": 214.0, "symmetry": "A1"},
  {"cluster": "K4[SiGe3]", "mode": "v4(E)", "frequency": 162.0, "symmetry": "E"},
  {"cluster": "K4[Ge3Sn]", "mode": "v1(A1)", "frequency": 231.0, "symmetry": "A1"},
  {"cluster": "K4[Ge3Sn]", "mode": "v3(E)", "frequency": 168.0, "symmetry": "E"},
  {"cluster": "K4[Ge3Sn]", "mode": "v3(E)", "frequency": 164.0, "symmetry": "E"},
  {"cluster": "K4[Ge3Sn]", "mode": "v2(A1)", "frequency": 152.0, "symmetry": "A1"},
  {"cluster": "K4[Ge3Sn]", "mode": "v4(E)", "frequency": 134.0, "symmetry": "E"},
  {"cluster": "K4[Ge3Sn]", "mode": "v4(E)", "frequency": 127.0, "symmetry": "E"},
  {"cluster": "K4[Ge2Sn2]", "mode": "v1(A1)", "frequency": 213.0, "symmetry": "A1"},
  {"cluster": "K4[Ge2Sn2]", "mode": "v5(B1)", "frequency": 156.0, "symmetry": "B1"},
  {"cluster": "K4[Ge2Sn2]", "mode": "v2(A1)", "frequency": 148.0, "symmetry": "A1"},
  {"cluster": "K4[Ge2Sn2]", "mode": "v6(B2)", "frequency": 141.0, "symmetry": "B2"},
  {"cluster": "K4[Ge2Sn2]", "mode": "v4(A2)", "frequency": 122.0, "symmetry": "A2"},
  {"cluster": "K4[Ge2Sn2]", "mode": "v3(A1)", "frequency": 119.0, "symmetry": "A1"},
  {"cluster": "K4[GeSn3]", "mode": "v1(A1)", "frequency": 190.0, "symmetry": "A1"},
  {"cluster": "K4[GeSn3]", "mode": "v3(E)", "frequency": 139.0, "symmetry": "E"},
  {"cluster": "K4[GeSn3]", "mode": "v3(E)", "frequency": 131.0, "symmetry": "E"},
  {"cluster": "K4[GeSn3]", "mode": "v2(A1)", "frequency": 129.0, "symmetry": "A1"},
  {"cluster": "K4[GeSn3]", "mode": "v4(E)", "frequency": 111.0, "symmetry": "E"},
  {"cluster": "K4[GeSn3]", "mode": "v4(E)", "frequency": 104.0, "symmetry": "E"}
]
JSONEOF
