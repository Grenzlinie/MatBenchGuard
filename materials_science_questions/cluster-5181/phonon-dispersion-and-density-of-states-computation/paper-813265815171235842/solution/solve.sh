#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_elastic_constants.csv ===
python3 -c "
import csv, os
outfile = os.path.join(os.environ['OUTDIR'], 'step_01_elastic_constants.csv')
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material','c11','c12','c44'])
    w.writerow(['Si',1.732,0.775,0.690])
    w.writerow(['Ge',1.450,0.621,0.630])
    w.writerow(['SiGe',1.587,0.697,0.655])
"

# === solve block: step_02_phonon_frequencies.csv ===
python3 -c "
import csv, math, os

def ta_freqs(mass_u, Fphi_mdynA, fphiphi_mdynA):
    # mass_u: atomic mass in u
    # Fphi, fphiphi in mdyn/A
    # 1 mdyn/A = 1e5 dyn/cm
    conv = 1e5  # dyn/cm per mdyn/A
    m_g = mass_u * 1.66053906660e-24  # g
    c_cm_s = 2.99792458e10
    Fphi_cgs = Fphi_mdynA * conv
    fpp_cgs = fphiphi_mdynA * conv
    om2_X = 12.0 * Fphi_cgs / m_g
    om2_L = 6.0 * (Fphi_cgs - fpp_cgs) / m_g  # fphiphi is negative, so Fphi - fpp > Fphi
    X_cm = math.sqrt(om2_X) / (2*math.pi * c_cm_s)
    L_cm = math.sqrt(om2_L) / (2*math.pi * c_cm_s)
    return round(X_cm,1), round(L_cm,1)

si_X, si_L = ta_freqs(28.0855, 0.0297, -0.00453)
ge_X, ge_L = ta_freqs(72.64, 0.0239, -0.00437)

outfile = os.path.join(os.environ['OUTDIR'], 'step_02_phonon_frequencies.csv')
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material','Gamma_optic_cm-1','X_TA_cm-1','L_TA_cm-1'])
    w.writerow(['Si',513.6,si_X,si_L])
    w.writerow(['Ge',291.3,ge_X,ge_L])
"

# === solve block: step_03_ordering_energy.csv ===
python3 -c "
import csv, os
outfile = os.path.join(os.environ['OUTDIR'], 'step_03_ordering_energy.csv')
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['phase','energy_meV_per_atom','c_over_a'])
    w.writerow(['RH1',16.9,1.037])
    w.writerow(['random',15.5,1.035])
"
