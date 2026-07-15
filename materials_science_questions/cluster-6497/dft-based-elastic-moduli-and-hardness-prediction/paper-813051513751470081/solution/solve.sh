#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.csv ===
python3 << 'EOF' > "$OUTDIR/elastic_constants.csv"
import csv, sys
writer = csv.writer(sys.stdout)
writer.writerow(['functional','C11','C22','C33','C12','C13','C23','C44','C55','C66','C15','C25','C35','C46'])
writer.writerow(['LDA',23.51,27.51,32.63,11.76,12.34,10.89,12.53,7.16,10.54,-1.43,2.60,-5.26,2.10])
writer.writerow(['PBE',3.36,5.81,5.85,3.11,1.88,2.69,1.34,0.40,2.05,0.09,0.63,-0.68,0.90])
writer.writerow(['PL/2',13.435,16.66,19.24,7.435,7.11,6.79,6.935,3.78,6.295,-0.67,1.615,-2.97,1.50])
EOF

# === solve block: mechanical_properties.csv ===
python3 /solution/compute.py mechanical > "$OUTDIR/mechanical_properties.csv"

# === solve block: acoustic_properties.csv ===
python3 << 'EOF' > "$OUTDIR/acoustic_properties.csv"
import csv, math, sys

# Hardcoded elastic constants (GPa) and unit cell volume (A^3) from paper Tables 1-2
DATA = {
    'LDA': {'C11':23.51,'C22':27.51,'C33':32.63,'C12':11.76,'C13':12.34,'C23':10.89,
            'C44':12.53,'C55':7.16,'C66':10.54,'C15':-1.43,'C25':2.60,'C35':-5.26,'C46':2.10,
            'V':299.9},
    'PBE': {'C11':3.36,'C22':5.81,'C33':5.85,'C12':3.11,'C13':1.88,'C23':2.69,
            'C44':1.34,'C55':0.40,'C66':2.05,'C15':0.09,'C25':0.63,'C35':-0.68,'C46':0.90,
            'V':401.7},
    'PL/2': {'C11':13.435,'C22':16.66,'C33':19.24,'C12':7.435,'C13':7.11,'C23':6.79,
             'C44':6.935,'C55':3.78,'C66':6.295,'C15':-0.67,'C25':1.615,'C35':-2.97,'C46':1.50,
             'V':350.8}
}
M = 128.17        # molecular mass g/mol
NA = 6.02214076e23
Z = 2             # formula units per unit cell

def vrh_bulk_shear(c):
    # Build Voigt 6x6 matrix (in GPa)
    Cmat = [
        [c['C11'], c['C12'], c['C13'], 0, c['C15'], 0],
        [c['C12'], c['C22'], c['C23'], 0, c['C25'], 0],
        [c['C13'], c['C23'], c['C33'], 0, c['C35'], 0],
        [0,0,0,2*c['C44'],0,2*c['C46']],
        [c['C15'],c['C25'],c['C35'],0,2*c['C55'],0],
        [0,0,0,2*c['C46'],0,2*c['C66']]
    ]
    n=6
    a = [row[:] for row in Cmat]
    inv = [[float(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = a[i][i]
        if abs(pivot) < 1e-15:
            return None, None
        for j in range(n):
            a[i][j] /= pivot
            inv[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(n):
                    a[k][j] -= factor * a[i][j]
                    inv[k][j] -= factor * inv[i][j]
    # compliance S
    S = [[inv[i][j]/2 if (i>=3 and j>=3) else inv[i][j] for j in range(6)] for i in range(6)]
    # Voigt bounds
    BV = (c['C11']+c['C22']+c['C33'] + 2*(c['C12']+c['C13']+c['C23']))/9
    GV = (c['C11']+c['C22']+c['C33'] + 3*(c['C44']+c['C55']+c['C66']) - (c['C12']+c['C13']+c['C23']))/15
    S11, S22, S33 = S[0][0], S[1][1], S[2][2]
    S12, S13, S23 = S[0][1], S[0][2], S[1][2]
    S44, S55, S66 = S[3][3]/4, S[4][4]/4, S[5][5]/4
    denom = (S11+S22+S33) + 2*(S12+S13+S23)
    if denom == 0:
        return None, None
    BR = 1/denom
    GR = 15/( 4*(S11+S22+S33) - 4*(S12+S13+S23) + 3*(S44+S55+S66) )
    B = (BV+BR)/2
    G = (GV+GR)/2
    return B, G

def acoustic(B_GPa, G_GPa, V_A3):
    rho = (M * Z * 1e27) / (NA * V_A3)   # kg/m^3
    B_Pa = B_GPa * 1e9
    G_Pa = G_GPa * 1e9
    if G_Pa <= 0 or rho <= 0:
        return (0,0,0,0,0)
    v_s = math.sqrt(G_Pa / rho)
    v_p = math.sqrt((B_Pa + 4*G_Pa/3) / rho)
    if v_s == 0 or v_p == 0:
        return (0,0,0,0,0)
    inv_avg = (1/3) * (2/(v_s**3) + 1/(v_p**3))
    if inv_avg <= 0:
        v_avg = 0
    else:
        v_avg = inv_avg ** (-1/3)
    n_atoms = 18
    hbar = 1.054571817e-34
    kB = 1.380649e-23
    factor = hbar/kB * (6*math.pi**2 * n_atoms * (NA * rho / (M*1e-3))) ** (1/3)
    TD = factor * v_avg if v_avg > 0 else 0
    gamma = 9*(v_p**2 - 4*v_s**2/3) / (2*(v_p**2 + 2*v_s**2))
    return v_s, v_p, v_avg, TD, gamma

writer = csv.writer(sys.stdout)
writer.writerow(['functional','v_s','v_p','v_avg','Theta_D','gamma_a'])
for func in ['LDA','PBE','PL/2']:
    d = DATA[func]
    B, G = vrh_bulk_shear(d)
    if B is None:
        print("Error computing B,G for", func, file=sys.stderr)
        continue
    v_s, v_p, v_avg, TD, gamma = acoustic(B, G, d['V'])
    writer.writerow([func, round(v_s,1), round(v_p,1), round(v_avg,1), round(TD,1), round(gamma,2)])
EOF
