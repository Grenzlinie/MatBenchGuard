#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_phonon_decomposition.json ===
cat > "$OUTDIR/step_01_phonon_decomposition.json" <<'FFEOF'
{
  "orbit_decompositions": [
    {
      "orbit": "a",
      "multiplicity": 2,
      "irreps": ["Γ5−", "Γ3−"]
    },
    {
      "orbit": "e",
      "multiplicity": 3,
      "irreps": ["Γ5−", "Γ3−", "Γ5+", "Γ1+"]
    },
    {
      "orbit": "g",
      "multiplicity": 1,
      "irreps": ["Γ5−", "Γ5−", "Γ4−", "Γ3−", "Γ5+", "Γ5+", "Γ2+", "Γ1+"]
    }
  ],
  "total_decomposition": {
    "Γ5−": 7,
    "Γ4−": 1,
    "Γ3−": 6,
    "Γ5+": 5,
    "Γ1+": 4,
    "Γ2+": 1
  },
  "mode_counts": [
    {
      "orbit": "a",
      "activity": "IR",
      "polarization": "x,y from Γ5− (doubly degenerate), z from Γ3−",
      "count": "1 each"
    },
    {
      "orbit": "a",
      "activity": "Raman",
      "polarization": "none",
      "count": "0"
    },
    {
      "orbit": "e",
      "activity": "IR",
      "polarization": "x,y from Γ5−, z from Γ3−",
      "count": "1 each"
    },
    {
      "orbit": "e",
      "activity": "Raman",
      "polarization": "x,y from Γ5+, z^2 from Γ1+",
      "count": "1 each"
    },
    {
      "orbit": "g",
      "activity": "IR",
      "polarization": "x,y from two Γ5−, z from Γ3−",
      "count": "2 (doubly degenerate) each for x/y, 1 for z"
    },
    {
      "orbit": "g",
      "activity": "Raman",
      "polarization": "two Γ5+ pairs, Γ2+, Γ1+",
      "count": "2 (doubly degenerate) each for x,y, 1 for Γ2+, 1 for Γ1+"
    }
  ]
}
FFEOF
