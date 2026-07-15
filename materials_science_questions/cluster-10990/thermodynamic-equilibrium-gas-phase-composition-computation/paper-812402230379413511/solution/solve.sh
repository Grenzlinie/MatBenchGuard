#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: step_02_equilibrium_results.json ===
python3 <<'PYEOF' > "$OUTDIR/step_02_equilibrium_results.json"
import json, sys
data = {
    "inert": {
        "gas": {
            "H2": 0.66476,
            "N2": 0.22177,
            "BF2": 2.9063e-5,
            "BF2H": 5.2646e-4,
            "BF3": 9.0041e-2,
            "HF": 2.2879e-2,
            "NH3": 2.9424e-6
        },
        "condensed": {
            "BN": 7.5899e-2
        },
        "eta_BN": 7.58,
        "gamma_BF3": 8.16e-2
    },
    "carbon": {
        "gas": {
            "H2": 6.6431e-1,
            "N2": 2.2178e-1,
            "BF2": 2.9069e-5,
            "BF2H": 5.2639e-4,
            "BF3": 9.0072e-2,
            "HF": 2.2874e-2,
            "NH3": 2.9396e-6,
            "HCN": 9.8370e-5,
            "CH4": 2.9861e-4,
            "C2H2": 6.5447e-6
        },
        "condensed": {
            "BN": 7.5863e-2,
            "C": 9.9959
        },
        "eta_BN": 7.58,
        "gamma_BF3": 8.53e-2,
        "gamma_C": 0.41e-2
    },
    "silica": {
        "gas": {
            "H2": 6.6424e-1,
            "N2": 2.2159e-1,
            "BF2": 2.8437e-5,
            "BF2H": 5.1492e-4,
            "BF3": 8.7133e-2,
            "HF": 2.2618e-2,
            "NH3": 2.9378e-6,
            "B2O3": 3.5053e-6,
            "H2O": 1.5161e-3,
            "SiF3H": 6.0237e-6,
            "SiF3": 5.8980e-6,
            "SiF4": 2.3367e-3
        },
        "condensed": {
            "BN": 8.5208e-2,
            "SiO2": 9.9761,
            "B2O3(l)": 1.0781e-2
        },
        "eta_BN": 8.52,
        "gamma_BF3": 11.23e-2,
        "gamma_SiO2": 2.39e-2
    },
    "SiC": {
        "gas": {
            "H2": 8.1930e-1,
            "N2": 8.7036e-2,
            "BF2": 8.3447e-7,
            "BF2H": 1.6781e-5,
            "BF3": 3.4674e-4,
            "HF": 3.4066e-3,
            "NH3": 2.5222e-6,
            "HCN": 6.8435e-5,
            "CH4": 4.5420e-4,
            "C2H2": 8.0715e-7,
            "SiF3H": 2.4001e-3,
            "SiF3": 1.5885e-3,
            "SiF4": 8.5349e-2
        },
        "condensed": {
            "BN": 9.9695e-1,
            "C": 2.3522,
            "Si3N4": 0.5358,
            "SiC": 7.6430
        },
        "eta_BN": 99.69,
        "gamma_BF3": 99.71e-2,
        "gamma_SiC": 2.357
    },
    "SiC_SiO2": {
        "gas": {
            "H2": 8.2116e-1,
            "N2": 7.5611e-2,
            "BF2": 8.9622e-7,
            "BF2H": 1.8044e-5,
            "BF3": 3.7590e-4,
            "HF": 3.4122e-3,
            "NH3": 2.3588e-6,
            "HCN": 6.3858e-5,
            "CH4": 4.5627e-4,
            "C2H2": 8.0899e-7,
            "H2O": 5.7033e-6,
            "SiF3H": 2.4065e-3,
            "SiF3": 1.5910e-3,
            "SiF4": 8.5525e-2,
            "CO": 9.3350e-3,
            "SiO": 7.8777e-6
        },
        "condensed": {
            "BN": 9.9673e-1,
            "C": 2.3810,
            "SiO2": 1.3764,
            "Si2N2O": 1.1690,
            "SiC": 5.5365
        },
        "eta_BN": 99.67,
        "gamma_BF3": 99.68e-2,
        "gamma_SiC": 2.463,
        "gamma_SiO2": 0.624
    },
    "inert_O2": {
        "gas": {
            "H2": 4.8786e-1,
            "N2": 2.2177e-1,
            "BF2": 1.7517e-5,
            "BF2H": 2.7184e-4,
            "BF3": 4.0243e-2,
            "HF": 1.4533e-1,
            "NH3": 1.8499e-6,
            "B2O3": 3.5053e-6,
            "H2O": 1.0476e-1
        },
        "condensed": {
            "B2O3(l)": 2.7297e-1
        },
        "eta_BN": 0,
        "gamma_BF3": 54.64e-2
    }
}
json.dump(data, sys.stdout, indent=2)
PYEOF
