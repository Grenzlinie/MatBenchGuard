#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: Re_Y.tdb ===
cat <<'TDBEOF' > $OUTDIR/Re_Y.tdb
$ ===================================================================
$ Thermodynamic database for Re-Y system (Paper 811737742726660096)
$ ===================================================================
ELEMENT RE HCP  1.86207E+02  0.0  0.0 !
ELEMENT Y  HCP  8.89059E+01  0.0  0.0 !

FUNCTION GHSERRE  2.98150E+02  -7.99391E+03+1.10527E+02*T-1.86572E+01*T*LN(T)-4.57635E-03*T**2+3.46885E-08*T**3-1.5469E+04*T**(-1);  3.45300E+03 Y  -8.53853E+03+1.21392E+02*T-2.12303E+01*T*LN(T)-2.79198E-03*T**2+5.69003E-09*T**3-7.925E-09*T**4;  6.00000E+03 N !
FUNCTION GHSERY   2.98150E+02  -1.23660E+04+5.82690E+01*T-1.07970E+01*T*LN(T)-1.81220E-02*T**2+9.04550E-07*T**3-1.39960E+04*T**(-1);  1.75000E+03 Y  -1.46260E+04+8.92020E+01*T-1.61190E+01*T*LN(T)-1.70000E-03*T**2-1.20000E-08*T**3;  3.60000E+03 N !

SPECIES RE2Y RE 2 Y 1 !

$ -------------------------- LIQUID PHASE --------------------------
PHASE LIQUID:L 1  1.0  RE , Y !
CONSTITUENT LIQUID:L :RE , Y : !

PARAMETER G(LIQUID,RE;0)  2.98150E+02  +6.56000E+03-1.90000E+00*T+GHSERRE#;  3.45300E+03 Y  +6.56000E+03-1.90000E+00*T+GHSERRE#;  6.00000E+03 N !
PARAMETER G(LIQUID,Y;0)   2.98150E+02  +1.76400E+03-4.81500E+00*T+GHSERY#;  1.75000E+03 Y  +1.76400E+03-4.81500E+00*T+GHSERY#;  3.60000E+03 N !
PARAMETER G(LIQUID,RE,Y;0)  2.98150E+02  1.25800E+05-5.01050E+01*T;  6.00000E+03 N !
PARAMETER G(LIQUID,RE,Y;1)  2.98150E+02  3.29230E+04;  6.00000E+03 N !

$ -------------------------- HCP_A3 PHASE --------------------------
PHASE HCP_A3 % 1  1.0  RE , Y !
CONSTITUENT HCP_A3 :RE , Y : !

PARAMETER G(HCP_A3,RE;0)  2.98150E+02  GHSERRE#;  3.45300E+03 Y  GHSERRE#;  6.00000E+03 N !
PARAMETER G(HCP_A3,Y;0)   2.98150E+02  GHSERY#;  1.75000E+03 Y  GHSERY#;  3.60000E+03 N !
PARAMETER G(HCP_A3,RE,Y;0)  2.98150E+02  3.20000E+05;  6.00000E+03 N !

$ -------------------------- BCC_A2 PHASE --------------------------
PHASE BCC_A2 % 1  1.0  RE , Y !
CONSTITUENT BCC_A2 :RE , Y : !

PARAMETER G(BCC_A2,RE;0)  2.98150E+02  +1.50000E+04-2.50000E+00*T+GHSERRE#;  3.45300E+03 Y  +1.50000E+04-2.50000E+00*T+GHSERRE#;  6.00000E+03 N !
PARAMETER G(BCC_A2,Y;0)   2.98150E+02  +1.00000E+04-2.00000E+00*T+GHSERY#;  1.75000E+03 Y  +1.00000E+04-2.00000E+00*T+GHSERY#;  3.60000E+03 N !
PARAMETER G(BCC_A2,RE,Y;0)  2.98150E+02  1.70000E+05;  6.00000E+03 N !

$ -------------------------- RE2Y COMPOUND --------------------------
PHASE RE2Y % 1 1  RE2Y !
CONSTITUENT RE2Y :RE2Y : !

PARAMETER G(RE2Y,RE2Y;0)  2.98150E+02  -8.13820E+04+3.65480E+02*T-7.09820E+01*T*LN(T)-7.63000E-03*T**2-3.59840E+03*T**(-1);  6.00000E+03 N !

$ ===================================================================
TDBEOF

# === solve block: Ni_Re.tdb ===
python3 /solution/generate_all_tdb.py Ni_Re

# === solve block: Ni_Re_Y.tdb ===
python3 /solution/generate_all_tdb.py Ni_Re_Y
