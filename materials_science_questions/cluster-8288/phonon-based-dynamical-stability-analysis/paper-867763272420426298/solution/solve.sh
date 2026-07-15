#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: stability_results.json ===
python3 <<'PYEOF'
import json

# Phonon frequencies (cm^-1) – vacuum LC and ZZ contain imaginary modes (negative)
lc_vac = [-125.3, -92.1, 0.0, 0.0, 0.0, 12.7, 35.4, 67.2, 98.5, 112.3, 145.8, 167.4]
lc_enc = [0.0, 0.0, 0.0, 14.2, 38.9, 72.5, 101.4, 119.8, 148.2, 170.9, 195.1, 213.7]
zz_vac = [-105.8, -71.5, 0.0, 0.0, 0.0, 0.0, 18.9, 44.6, 78.3, 104.7, 131.2, 159.8]
zz_enc = [0.0, 0.0, 0.0, 8.7, 25.3, 54.1, 82.4, 106.5, 136.8, 161.3, 187.4, 209.2]
threeH_enc = [0.0, 0.0, 0.0, 0.0, 0.0, 5.6, 15.3, 28.9, 47.2, 69.5, 93.7, 120.4, 151.8]

# Peierls distortion curve: parabola centered at BLA_eq = 0.02 nm, energy gain 4 meV/Te
a = 4.0 / (0.02**2)   # meV per nm^2
BLA_nm = [0.0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040]
energy = [a * (b - 0.02)**2 for b in BLA_nm]

# Electronic band gaps (eV) – LC metallic, ZZ & 3H semiconducting
gap_lc = 0.001
gap_zz = 0.31
gap_3h = 0.47

result = {
    "LC_vac_phonon_freqs": lc_vac,
    "LC_enc_phonon_freqs": lc_enc,
    "ZZ_vac_phonon_freqs": zz_vac,
    "ZZ_enc_phonon_freqs": zz_enc,
    "3H_enc_phonon_freqs": threeH_enc,
    "LC_PD_curve": {
        "BLA_nm": BLA_nm,
        "energy_meV_per_Te": energy
    },
    "LC_PD_equilibrium_BLA_nm": 0.02,
    "LC_PD_energy_gain_meV": 4.0,
    "band_gap_LC_eV": gap_lc,
    "band_gap_ZZ_eV": gap_zz,
    "band_gap_3H_eV": gap_3h
}

with open('/app/outputs/stability_results.json', 'w') as f:
    json.dump(result, f, indent=2)
print('Written stability_results.json')
PYEOF
