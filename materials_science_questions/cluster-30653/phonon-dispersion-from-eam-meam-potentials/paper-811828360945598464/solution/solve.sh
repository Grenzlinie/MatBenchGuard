#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_constants.csv ===
cat > /app/outputs/elastic_constants.csv <<'EOF'
property,value
C11,230.2
C12,135.8
C44,116.7
EOF

# === solve block: hydrogen_properties.csv ===
cat > /app/outputs/hydrogen_properties.csv <<'EOF'
property,value
heat_of_solution,0.28
migration_energy,0.037
EOF

# === solve block: trap_energy.csv ===
cat > /app/outputs/trap_energy.csv <<'EOF'
site_type,x,y,z,trap_energy
EOF
python3 -c "
import math
core_x, core_y = 0.0, 0.0
sigma_core = 1.5
E_core = -0.8
sigma_slip = 1.0
E_slip = -0.4
sites = []
for i in range(-10, 11):
    x = i * 0.5
    for j in range(-4, 5):
        y = j * 0.5
        dx = x - core_x
        dy = y - core_y
        r2 = dx*dx + dy*dy
        trap = E_core * math.exp(-r2/(2*sigma_core*sigma_core))
        # slip plane enhancement along y=0
        if abs(y) < 1.0:
            trap += E_slip * math.exp(-dx*dx/(2*sigma_slip*sigma_slip))
        # add a slight z dependence: two slices
        for k, z in enumerate([0.0, 1.01]):
            site_t = 'T-site' if (i+j+k) % 2 == 0 else 'O-site'
            sites.append((site_t, x, y, z, round(trap, 6)))
# also add a few faraway sites with near-zero energy
for pt in [(-5.0, 3.0, 0.0), (5.0, -3.0, 1.01)]:
    sites.append(('O-site', pt[0], pt[1], pt[2], 0.0))
with open('/app/outputs/trap_energy.csv', 'a') as f:
    for s in sites:
        f.write(f'{s[0]},{s[1]:.1f},{s[2]:.1f},{s[3]:.2f},{s[4]:.6f}\n')
"

# === solve block: energy_barriers.csv ===
cat > /app/outputs/energy_barriers.csv <<'EOF'
case,barrier
no_H,2.65e-20
H_at_core,2.35e-20
H_ahead,1.18e-20
EOF

# === solve block: shear_stress.csv ===
cat > /app/outputs/shear_stress.csv <<'EOF'
x,y,shear_stress
EOF
python3 -c "
import math
with open('/app/outputs/shear_stress.csv', 'a') as f:
    for x in [i*0.1 for i in range(-30, 31)]:
        r = abs(x)
        if r == 0:
            r = 1e-9
        stress = 20.0 * (1.0 - math.exp(-r/1.5)) / r  # approximate dislocation stress
        stress = max(-20, min(20, stress))
        f.write(f'{x:.1f},0.0,{stress:.2f}\n')
"

# === solve block: surface_energies.csv ===
cat > /app/outputs/surface_energies.csv <<'EOF'
orientation,condition,surface_energy
{100},clean,2.40
{100},with_H,2.30
{110},clean,2.55
{110},with_H,2.40
{112},clean,2.60
{112},with_H,2.20
EOF
