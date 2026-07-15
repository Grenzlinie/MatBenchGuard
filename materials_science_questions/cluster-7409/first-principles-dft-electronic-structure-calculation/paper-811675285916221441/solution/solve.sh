#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: excitation_energies.csv ===
cat > /app/outputs/excitation_energies.csv <<'CSVFEOF'
system,hole_location,spin_state,excitation_energy_eV
TiO2,none,triplet,2.07
TiO2,none,singlet,2.90
(TiO2)_6,out-of-plane,triplet,2.26
(TiO2)_6,out-of-plane,singlet,2.34
(TiO2)_6,in-plane/outside,triplet,2.17
(TiO2)_6,in-plane/outside,singlet,2.59
(TiO2)_6,in-plane/inside,triplet,2.15
(TiO2)_6,in-plane/inside,singlet,2.23
(TiO2)_8,out-of-plane,triplet,2.44
(TiO2)_8,out-of-plane,singlet,2.62
(TiO2)_8,in-plane/outside,triplet,2.99
(TiO2)_8,in-plane/outside,singlet,3.35
(TiO2)_8,in-plane/inside,triplet,2.81
(TiO2)_8,in-plane/inside,singlet,3.00
(TiO2)_10,out-of-plane,triplet,2.65
(TiO2)_10,out-of-plane,singlet,2.87
(TiO2)_10,in-plane/outside,triplet,3.05
(TiO2)_10,in-plane/outside,singlet,3.37
(TiO2)_10,in-plane/inside,triplet,3.05
(TiO2)_10,in-plane/inside,singlet,3.14
(TiO2)_12,out-of-plane,triplet,2.80
(TiO2)_12,out-of-plane,singlet,3.03
(TiO2)_12,in-plane/outside,triplet,3.16
(TiO2)_12,in-plane/outside,singlet,3.46
(TiO2)_12,in-plane/inside,triplet,3.51
(TiO2)_12,in-plane/inside,singlet,3.56
(TiO2)_14,out-of-plane,triplet,2.91
(TiO2)_14,out-of-plane,singlet,3.08
(TiO2)_14,in-plane/outside,triplet,3.23
(TiO2)_14,in-plane/outside,singlet,3.53
(TiO2)_14,in-plane/inside,triplet,3.60
(TiO2)_14,in-plane/inside,singlet,3.65
(TiO2)_16,out-of-plane,triplet,3.19
(TiO2)_16,out-of-plane,singlet,3.46
(TiO2)_16,in-plane/outside,triplet,3.29
(TiO2)_16,in-plane/outside,singlet,3.60
(TiO2)_16,in-plane/inside,triplet,3.84
(TiO2)_16,in-plane/inside,singlet,3.89
(TiO2)_18,out-of-plane,triplet,3.21
(TiO2)_18,out-of-plane,singlet,3.49
(TiO2)_18,in-plane/outside,triplet,3.33
(TiO2)_18,in-plane/outside,singlet,3.62
(TiO2)_18,in-plane/inside,triplet,3.83
(TiO2)_18,in-plane/inside,singlet,3.88
(TiO2)_8,delocalized,triplet,4.64
CSVFEOF
