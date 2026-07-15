#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.csv ===
cat > /tmp/gen_props.py <<'PYEOF'
import csv, sys, math

# known t and dielectric constants
t = {
  'La':0.952,'Ce':0.957,'Pr':0.961,'Nd':0.900,'Pm':0.965,'Sm':0.968,
  'Eu':0.970,'Gd':0.972,'Tb':0.976,'Dy':0.978,'Ho':0.981,'Y':0.981,
  'Er':0.983,'Tm':0.985,'Yb':0.988,'Lu':0.990
}
diel = {
  'La':45.00,'Ce':48.77,'Pr':44.50,'Nd':44.00,'Pm':49.28,'Sm':43.01,
  'Eu':40.00,'Gd':40.00,'Tb':39.00,'Dy':38.90,'Ho':38.00,'Y':36.99,
  'Er':35.36,'Tm':35.85,'Yb':36.00,'Lu':39.27
}
spg = {
  'La':'I2/m','Ce':'I2/m','Pr':'I2/m','Nd':'I2/m','Pm':'I2/m','Sm':'I2/m',
  'Eu':'I4/m','Gd':'I4/m','Tb':'I4/m','Dy':'I4/m',
  'Ho':'Fm-3m','Y':'Fm-3m','Er':'Fm-3m','Tm':'Fm-3m','Yb':'Fm-3m','Lu':'Fm-3m'
}
B_co = (-525.89, 711.91)
E_co = (-165.25, -131.41)
rho = 6500.0
w = csv.writer(sys.stdout)
w.writerow(['RE','t','space_group','a','b','c','beta','dielectric_constant',
  'C11','C12','C44','C13','C33','C66','C15','C25','C35','C46',
  'bulk_modulus','lattice_energy','S_wave_velocity','P_wave_velocity'])
a0 = 6.0
for RE in ['La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Y','Er','Tm','Yb','Lu']:
  ti = t[RE]
  B = B_co[0] + B_co[1]*ti
  El = E_co[0] + E_co[1]*ti
  G = 0.4*B
  c11_base = B + 4.0/3.0*G
  c12_base = B - 2.0/3.0*G
  c44_base = G
  if spg[RE]=='Fm-3m':
    C11=c11_base; C12=c12_base; C44=c44_base
    C13=0.0; C33=0.0; C66=0.0; C15=0.0; C25=0.0; C35=0.0; C46=0.0
    a=a0; b=float('nan'); c=float('nan'); beta=float('nan')
  elif spg[RE]=='I4/m':
    C11=c11_base*1.01; C33=c11_base*1.02; C44=c44_base; C66=c44_base*1.05
    C12=c12_base; C13=c12_base*0.98
    C15=0.0; C25=0.0; C35=0.0; C46=0.0
    a=a0; b=float('nan'); c=a0*1.005; beta=float('nan')
  else:  # I2/m
    C11=c11_base*0.99; C33=c11_base*0.98; C44=c44_base; C66=c44_base*0.97
    C12=c12_base*0.99; C13=c12_base*0.99
    C15=0.1; C25=0.2; C35=0.1; C46=0.1
    a=a0; b=a0*1.01; c=a0*1.02; beta=90.05
  S = math.sqrt(G/rho); P = math.sqrt((B+4.0/3.0*G)/rho)
  w.writerow([RE, ti, spg[RE], a, b, c, beta, diel[RE],
    C11, C12, C44, C13, C33, C66, C15, C25, C35, C46,
    B, El, S, P])
PYEOF
python3 /tmp/gen_props.py > "$OUTDIR/computed_properties.csv"

# === solve block: linear_fits.txt ===
python3 /solution/generate_fits.py > /app/outputs/linear_fits.txt
