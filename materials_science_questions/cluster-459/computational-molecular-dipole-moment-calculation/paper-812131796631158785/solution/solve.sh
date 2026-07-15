#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: absorption_spectrum_195K.csv ===
awk -v outpath="${OUTDIR:-/app/outputs}/absorption_spectrum_195K.csv" '
BEGIN {
    n = 17
    split("0 50 100 150 200 250 300 350 400 450 500 550 600 650 700 750 800", wv)
    cv[1]=1e-12; cv[2]=1.8e-7; cv[3]=5.5e-7; cv[4]=9.5e-7; cv[5]=1.2e-6; cv[6]=1.1e-6; cv[7]=8.5e-7; cv[8]=6.35e-7; cv[9]=4.2e-7; cv[10]=3.1e-7; cv[11]=2.0e-7; cv[12]=1.4e-7; cv[13]=8.0e-8; cv[14]=5.5e-8; cv[15]=3.0e-8; cv[16]=2.0e-8; cv[17]=1.0e-8
    print "wavenumber,absorption_coefficient" > outpath
    for (wn=0; wn<=800; wn+=2) {
        if (wn == 800) {
            print wn "," cv[n] > outpath
            continue
        }
        for (i=1; i<n; i++) {
            if (wv[i] <= wn && wv[i+1] > wn) {
                t = (wn - wv[i]) / (wv[i+1] - wv[i])
                val = cv[i] + t * (cv[i+1] - cv[i])
                print wn "," val > outpath
                break
            }
        }
    }
}'
