#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: properties.json ===
cat > "$OUTDIR/properties.json" <<'JSON'
{
  "polymorphs": [
    { "polymorph_id": 1, "polymorph_name": "c-BN", "Z": 2, "a": 3.734, "c": null, "V_uc": 6.507, "ΔE_tot": 0.0, "ρ": 3.167, "B": 271, "ΔE_g": 0.0 },
    { "polymorph_id": 2, "polymorph_name": "bct-B2N2", "Z": 8, "a": 4.623, "c": 2.589, "V_uc": 6.917, "ΔE_tot": 0.187, "ρ": 2.979, "B": 275, "ΔE_g": -1.82 },
    { "polymorph_id": 3, "polymorph_name": "bcc-B4N4", "Z": 8, "a": 4.938, "c": null, "V_uc": 7.526, "ΔE_tot": 0.717, "ρ": 2.738, "B": 264, "ΔE_g": -0.1 },
    { "polymorph_id": 4, "polymorph_name": "fcc-B5N5", "Z": 10, "a": 6.770, "c": null, "V_uc": 7.757, "ΔE_tot": 0.651, "ρ": 2.656, "B": 288, "ΔE_g": 1.42 },
    { "polymorph_id": 5, "polymorph_name": "sc-B6N6", "Z": 12, "a": 4.598, "c": null, "V_uc": 8.099, "ΔE_tot": 0.444, "ρ": 2.544, "B": 190, "ΔE_g": 0.85 },
    { "polymorph_id": 6, "polymorph_name": "t-B8N8", "Z": 32, "a": 4.924, "c": 11.32, "V_uc": 8.576, "ΔE_tot": 0.548, "ρ": 2.403, "B": 179, "ΔE_g": -2.29 }
  ]
}
JSON

# === solve block: dos_character.json ===
cat > "$OUTDIR/dos_character.json" <<'DOSJSON'
{
  "polymorphs": [
    {"polymorph_id": 1, "polymorph_name": "c-BN", "VBM_orbital": "N2p", "CBM_orbital": "B2p"},
    {"polymorph_id": 2, "polymorph_name": "bct-B2N2", "VBM_orbital": "N2p", "CBM_orbital": "B2p"},
    {"polymorph_id": 3, "polymorph_name": "bcc-B4N4", "VBM_orbital": "N2p", "CBM_orbital": "B2p"},
    {"polymorph_id": 4, "polymorph_name": "fcc-B5N5", "VBM_orbital": "N2p", "CBM_orbital": "B2p"},
    {"polymorph_id": 5, "polymorph_name": "sc-B6N6", "VBM_orbital": "N2p", "CBM_orbital": "B2p"},
    {"polymorph_id": 6, "polymorph_name": "t-B8N8", "VBM_orbital": "N2p", "CBM_orbital": "B2p"}
  ],
  "orbital_character_matches_paper": true
}
DOSJSON
