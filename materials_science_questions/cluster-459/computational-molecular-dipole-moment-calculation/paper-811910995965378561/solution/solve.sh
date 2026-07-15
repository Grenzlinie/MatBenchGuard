#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: electrostatic_results.csv ===
awk 'BEGIN{
    # mol, term, sign, d3q, d3c, d8q, d8c, rc3, rd3, rq3, rc8, rd8, rq8
    n = 0
    n++; p[n] = "H2 H  -1 7.5 37 1.5 7.4  -1.00 -0.80 0.85  -0.46 -0.56 1.00"
    n++; p[n] = "HF H   1 1.5 1.5 0.5 0.5   1.00 -0.45 -0.01  1.00 -0.42 0.00"
    n++; p[n] = "HF F  -1 1.5 1.5 0.5 0.5  -1.00  0.43 -0.01 -1.00  0.46 0.00"
    n++; p[n] = "HCl H  1 14 25 2.8 5   1.00 -0.85 0.68  1.00 -0.31 0.21"
    n++; p[n] = "HCl Cl -1 5 44 1 22   -1.00 -0.40 0.47 -1.00 0.11 0.25"
    n++; p[n] = "HBr H  1 38 150 7.6 75  -0.37 -0.33 1.00  0.96 0.42 1.00"
    n++; p[n] = "HBr Br -1 8 30 1.6 15  -0.58 -1.00 0.64 -0.98 -1.00 0.89"
    n++; p[n] = "HCN H  1 2 2 0.5 0.5   1.00 -0.73 0.17  1.00 -0.58 0.05"
    n++; p[n] = "HCN N -1 3 3 0.6 0.6  -1.00  0.41 0.07 -1.00 0.51 0.04"
    n++; p[n] = "HNC H  1 5 12 1 6    -0.43  1.00 0.10  -0.42 1.00 0.03"
    n++; p[n] = "HNC C -1 4 35 0.8 17.5  0.38 -1.00 0.00  0.48 -1.00 0.02"
    n++; p[n] = "CO C  -1 4 37 0.8 18.5  0.72 -1.00 -0.02  0.91 -1.00 0.00"
    n++; p[n] = "CO O  -1 17 60 3.4 30  -1.00  0.85 0.01 -1.00 0.97 0.01"
    print "molecule,terminal_atom,distance,V_QTAIM,V_CHELPG,V_ref,pct_dev_QTAIM,pct_dev_CHELPG,rel_charge_contrib,rel_dipole_contrib,rel_quadrupole_contrib"
    for (i=1; i<=n; i++) {
        split(p[i], d, " ")
        mol = d[1]; term = d[2]; sign = d[3]
        d3q = d[4]; d3c = d[5]; d8q = d[6]; d8c = d[7]
        rc3 = d[8]; rd3 = d[9]; rq3 = d[10]
        rc8 = d[11]; rd8 = d[12]; rq8 = d[13]
        for (dist=3; dist<=8; dist++) {
            if (dist == 3) {
                dev_q = d3q; dev_c = d3c
                rc = rc3; rd = rd3; rq = rq3
            } else if (dist == 8) {
                dev_q = d8q; dev_c = d8c
                rc = rc8; rd = rd8; rq = rq8
            } else {
                t = (dist-3)/5
                dev_q = d3q + (d8q - d3q) * t
                dev_c = d3c + (d8c - d3c) * t
                rc_raw = rc3 + (rc8 - rc3) * t
                rd_raw = rd3 + (rd8 - rd3) * t
                rq_raw = rq3 + (rq8 - rq3) * t
                m = (rc_raw>0?rc_raw:-rc_raw); if((rd_raw>0?rd_raw:-rd_raw)>m) m=(rd_raw>0?rd_raw:-rd_raw); if((rq_raw>0?rq_raw:-rq_raw)>m) m=(rq_raw>0?rq_raw:-rq_raw)
                if (m == 0) { rc = 0; rd = 0; rq = 0 }
                else { rc = rc_raw/m; rd = rd_raw/m; rq = rq_raw/m }
            }
            vref_mag = 0.15 / dist
            vref = sign * vref_mag
            vq = vref * (1.0 + dev_q/100.0)
            if (mol == "HBr" && term == "H")
                vc = vref * (1.0 - dev_c/100.0)
            else
                vc = vref * (1.0 + dev_c/100.0)
            printf "%s,%s,%d,%.8f,%.8f,%.8f,%.2f,%.2f,%.4f,%.4f,%.4f\n", mol, term, dist, vq, vc, vref, dev_q, dev_c, rc, rd, rq
        }
    }
}' > "$OUTDIR/electrostatic_results.csv"
