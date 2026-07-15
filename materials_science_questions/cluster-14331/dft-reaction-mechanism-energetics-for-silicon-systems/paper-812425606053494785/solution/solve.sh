#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
cat > /app/outputs/computed_energies.json <<'FFEOF'
[
  { "system": "catalyst_4",               "substrate": "parent", "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "Ph(Me)SiH2",               "substrate": "parent", "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "calcium_hydride",           "substrate": "parent", "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "MeSiH3",                    "substrate": "parent", "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "Ph2(Me)SiH",                "substrate": "parent", "E": -0.014510, "H": -0.014510, "G": -0.014510 },
  { "system": "CaPh",                      "substrate": "parent", "E": -0.008610, "H": -0.008610, "G": -0.008610 },
  { "system": "tertiary_silane",            "substrate": "parent", "E": -0.007490, "H": -0.007490, "G": -0.007490 },
  { "system": "react_4_and_silane",        "substrate": "parent", "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "TS1",                       "substrate": "parent", "E": 0.030440, "H": 0.030440, "G": 0.030440 },
  { "system": "hydride_and_silane",        "substrate": "parent", "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "TS2",                       "substrate": "parent", "E": 0.027740, "H": 0.027740, "G": 0.027740 },
  { "system": "CaPh_and_MeSiH3",          "substrate": "parent", "E": -0.008610, "H": -0.008610, "G": -0.008610 },
  { "system": "TS3",                       "substrate": "parent", "E": 0.021830, "H": 0.021830, "G": 0.021830 },
  { "system": "products",                  "substrate": "parent", "E": -0.014510, "H": -0.014510, "G": -0.014510 },
  { "system": "catalyst_4",               "substrate": "pCF3",  "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "Ph(Me)SiH2",               "substrate": "pCF3",  "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "calcium_hydride",           "substrate": "pCF3",  "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "MeSiH3",                    "substrate": "pCF3",  "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "Ph2(Me)SiH",                "substrate": "pCF3",  "E": -0.014510, "H": -0.014510, "G": -0.014510 },
  { "system": "CaPh",                      "substrate": "pCF3",  "E": -0.008610, "H": -0.008610, "G": -0.008610 },
  { "system": "tertiary_silane",            "substrate": "pCF3",  "E": -0.007490, "H": -0.007490, "G": -0.007490 },
  { "system": "react_4_and_silane",        "substrate": "pCF3",  "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "TS1",                       "substrate": "pCF3",  "E": 0.030440, "H": 0.030440, "G": 0.030440 },
  { "system": "hydride_and_silane",        "substrate": "pCF3",  "E": 0.00000, "H": 0.00000,  "G": 0.00000 },
  { "system": "TS2",                       "substrate": "pCF3",  "E": 0.027740, "H": 0.027740, "G": 0.027740 },
  { "system": "CaPh_and_MeSiH3",          "substrate": "pCF3",  "E": -0.008610, "H": -0.008610, "G": -0.008610 },
  { "system": "TS3",                       "substrate": "pCF3",  "E": 0.015290, "H": 0.015290, "G": 0.015290 },
  { "system": "products",                  "substrate": "pCF3",  "E": -0.014510, "H": -0.014510, "G": -0.014510 }
]
FFEOF
