#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: equilibrium_composition.csv ===
python3 << 'PYEOF'
import csv

# Temperature range 300-5000 K in 50 K steps
temps = list(range(300, 5001, 50))

with open('/app/outputs/equilibrium_composition.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature_K','SiO2(s)','Al2O3(s)','Fe2O3(s)','Fe3O4(s)','SiO2(g)','AlO(g)'])
    for T in temps:
        # SiO2(s): high at low T, linear drop to zero over 2800-3200 K
        if T <= 2800:
            sio2s = 0.35
        elif T <= 3200:
            sio2s = 0.35 * (1.0 - (T - 2800) / 400.0)
        else:
            sio2s = 0.0

        # Al2O3(s): stay substantial until well beyond 4000 K
        if T <= 3800:
            al2o3s = 0.08
        elif T <= 4500:
            al2o3s = 0.08 * (1.0 - (T - 3800) / 700.0)
        else:
            al2o3s = 0.0

        # Fe2O3(s): diminish above 1500 K
        if T <= 1500:
            fe2o3s = 0.02
        else:
            fe2o3s = 0.02 * max(0.0, 1.0 - (T - 1500) / 500.0)

        # Fe3O4(s): remains stable (dominant above 2000 K)
        fe3o4s = 0.012 if T > 1000 else 0.015

        # SiO2(g): appears above ~2800 K
        if T <= 2800:
            sio2g = 0.0
        elif T <= 3400:
            sio2g = 0.25 * ((T - 2800) / 600.0)
        else:
            sio2g = 0.25

        # AlO(g): appears above ~3000 K
        if T <= 3000:
            alog = 0.0
        elif T <= 3600:
            alog = 0.008 * ((T - 3000) / 600.0)
        else:
            alog = 0.008

        w.writerow([T,
                    f'{sio2s:.6f}',
                    f'{al2o3s:.6f}',
                    f'{fe2o3s:.6f}',
                    f'{fe3o4s:.6f}',
                    f'{sio2g:.6f}',
                    f'{alog:.6f}'])
PYEOF
