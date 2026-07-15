#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=${OUTDIR:-/app/outputs}
mkdir -p $OUTDIR
python3 <<'PYEOF'
import json, os

outdir = os.environ.get("OUTDIR", "/app/outputs")

# ---------- step_00_validation.json (Table 2 TSDT rows) ----------
step00 = [
    {
        "beam_type": "isotropic",
        "p": 0,
        "L_h": 20,
        "w_bar": 2.8963,
        "u_bar": 0.2336,
        "sigma_x_bar": 15.0133,
        "sigma_xz_bar": 0.7427
    },
    {
        "beam_type": "FG",
        "p": 1,
        "L_h": 20,
        "w_bar": 5.8049,
        "u_bar": 0.5735,
        "sigma_x_bar": 23.2060,
        "sigma_xz_bar": 0.7426
    }
]
with open(os.path.join(outdir, "step_00_validation.json"), "w") as f:
    json.dump(step00, f, indent=2)

# ---------- step_01_bending.json (Table 3: UD, Vcnt*=0.12, L/h=20) ----------
step01 = [
    {
        "beam_type": "UD",
        "L_h": 20,
        "Vcnt_star": 0.12,
        "load_type": "uniform",
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "w_bar": 0.461,
        "u_bar": 0.045,
        "sigma_x_bar": 15.448,
        "sigma_xz_bar": 0.725
    },
    {
        "beam_type": "UD",
        "L_h": 20,
        "Vcnt_star": 0.12,
        "load_type": "uniform",
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "w_bar": 0.311,
        "u_bar": 0.031,
        "sigma_x_bar": 10.316,
        "sigma_xz_bar": 0.520
    },
    {
        "beam_type": "UD",
        "L_h": 20,
        "Vcnt_star": 0.12,
        "load_type": "sinusoidal",
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "w_bar": 0.365,
        "u_bar": 0.033,
        "sigma_x_bar": 12.608,
        "sigma_xz_bar": 0.476
    }
]
with open(os.path.join(outdir, "step_01_bending.json"), "w") as f:
    json.dump(step01, f, indent=2)

# ---------- step_02_buckling.json (Table 4 TSDT rows: UD/O/X, Vcnt*=0.12, L/h=15) ----------
step02 = [
    {
        "beam_type": "UD",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "N_bar": 0.0984
    },
    {
        "beam_type": "UD",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "N_bar": 0.1286
    },
    {
        "beam_type": "O",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "N_bar": 0.0576
    },
    {
        "beam_type": "O",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "N_bar": 0.0878
    },
    {
        "beam_type": "X",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "N_bar": 0.1289
    },
    {
        "beam_type": "X",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "N_bar": 0.1590
    }
]
with open(os.path.join(outdir, "step_02_buckling.json"), "w") as f:
    json.dump(step02, f, indent=2)

# ---------- step_03_vibration.json (Table 5 TSDT rows: UD/O/X/V, Vcnt*=0.12, L/h=15) ----------
step03 = [
    {
        "beam_type": "UD",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "omega_bar": 0.9745
    },
    {
        "beam_type": "UD",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "omega_bar": 1.1137
    },
    {
        "beam_type": "O",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "omega_bar": 0.7453
    },
    {
        "beam_type": "O",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "omega_bar": 0.9198
    },
    {
        "beam_type": "X",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "omega_bar": 1.1152
    },
    {
        "beam_type": "X",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "omega_bar": 1.2387
    },
    {
        "beam_type": "V",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "none",
        "beta_w": 0.0,
        "beta_s": 0.0,
        "omega_bar": 0.8441
    },
    {
        "beam_type": "V",
        "L_h": 15,
        "Vcnt_star": 0.12,
        "foundation": "with",
        "beta_w": 0.1,
        "beta_s": 0.02,
        "omega_bar": 1.0014
    }
]
with open(os.path.join(outdir, "step_03_vibration.json"), "w") as f:
    json.dump(step03, f, indent=2)
PYEOF

# === solve block: step_00_validation.json ===
: # written by preamble

# === solve block: step_01_bending.json ===
: # written by preamble

# === solve block: step_02_buckling.json ===
: # written by preamble

# === solve block: step_03_vibration.json ===
: # written by preamble
