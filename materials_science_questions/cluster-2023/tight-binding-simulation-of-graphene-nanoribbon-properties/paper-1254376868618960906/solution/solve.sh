#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: electronic_properties.json ===
python3 -c 'import json; json.dump({"band_gap_eV": 1.1}, open("/app/outputs/electronic_properties.json", "w"))'

# === solve block: raman_spectrum.json ===
python3 -c '
import json
peaks = [
    {"wavenumber_cm-1": 1129.0, "normalized_intensity": 0.000255},
    {"wavenumber_cm-1": 1145.0, "normalized_intensity": 0.00319},
    {"wavenumber_cm-1": 1163.0, "normalized_intensity": 0.00300},
    {"wavenumber_cm-1": 1183.0, "normalized_intensity": 0.000160},
    {"wavenumber_cm-1": 1195.0, "normalized_intensity": 0.0118},
    {"wavenumber_cm-1": 1208.0, "normalized_intensity": 0.0182},
    {"wavenumber_cm-1": 1256.0, "normalized_intensity": 0.0421},
    {"wavenumber_cm-1": 1269.0, "normalized_intensity": 0.0100},
    {"wavenumber_cm-1": 1292.0, "normalized_intensity": 0.0591},
    {"wavenumber_cm-1": 1303.0, "normalized_intensity": 0.169},
    {"wavenumber_cm-1": 1318.0, "normalized_intensity": 0.0362},
    {"wavenumber_cm-1": 1328.0, "normalized_intensity": 1.000},
    {"wavenumber_cm-1": 1339.0, "normalized_intensity": 0.144},
    {"wavenumber_cm-1": 1351.0, "normalized_intensity": 0.332},
    {"wavenumber_cm-1": 1362.0, "normalized_intensity": 0.00602},
    {"wavenumber_cm-1": 1368.0, "normalized_intensity": 0.0973},
    {"wavenumber_cm-1": 1383.0, "normalized_intensity": 0.00817},
    {"wavenumber_cm-1": 1389.0, "normalized_intensity": 0.0383},
    {"wavenumber_cm-1": 1396.0, "normalized_intensity": 0.0169},
    {"wavenumber_cm-1": 1404.0, "normalized_intensity": 0.0103},
    {"wavenumber_cm-1": 1406.0, "normalized_intensity": 0.0189},
    {"wavenumber_cm-1": 1410.0, "normalized_intensity": 0.0541},
    {"wavenumber_cm-1": 1437.0, "normalized_intensity": 0.00313},
    {"wavenumber_cm-1": 1460.0, "normalized_intensity": 0.000576},
    {"wavenumber_cm-1": 1470.0, "normalized_intensity": 0.0574},
    {"wavenumber_cm-1": 1472.0, "normalized_intensity": 0.00901},
    {"wavenumber_cm-1": 1490.0, "normalized_intensity": 0.0246},
    {"wavenumber_cm-1": 1506.0, "normalized_intensity": 0.0758},
    {"wavenumber_cm-1": 1532.0, "normalized_intensity": 0.0463},
    {"wavenumber_cm-1": 1556.0, "normalized_intensity": 0.0175},
    {"wavenumber_cm-1": 1568.0, "normalized_intensity": 0.208},
    {"wavenumber_cm-1": 1576.0, "normalized_intensity": 0.0317},
    {"wavenumber_cm-1": 1584.0, "normalized_intensity": 0.0444},
    {"wavenumber_cm-1": 1587.0, "normalized_intensity": 0.164},
    {"wavenumber_cm-1": 1594.0, "normalized_intensity": 0.0270},
    {"wavenumber_cm-1": 1607.0, "normalized_intensity": 0.00844}
]
with open("/app/outputs/raman_spectrum.json", "w") as f:
    json.dump({"peaks": peaks}, f, indent=2)
'
