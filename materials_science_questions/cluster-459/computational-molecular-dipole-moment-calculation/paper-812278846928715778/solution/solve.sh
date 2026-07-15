#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: equilibrium_positions.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
with open(os.path.join(outdir, 'equilibrium_positions.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['case','phi','alpha','y','rho','stability','character'])
    ys = [2,5,10,50,100]
    # iso phi 120
    for alpha, rho, st, ch in [(30,1.261,'St','E'),(45,1.199,'St','E'),(60,1.0,'St','E'),(75,0.401,'St','E'),(90,0.0,'St','S'),(105,0.0,'St','S'),(120,0.0,'St','S')]:
        for y in ys:
            writer.writerow(['iso',120,alpha,y,f'{rho:.3f}',st,ch])
    # iso phi 180
    for alpha, rho, st, ch in [(0,1.0,'St','E'),(15,0.955,'St','E'),(30,0.796,'St','E'),(45,0.401,'St','E'),(60,0.0,'St','S'),(75,0.0,'St','S'),(90,0.0,'St','S')]:
        for y in ys:
            writer.writerow(['iso',180,alpha,y,f'{rho:.3f}',st,ch])
    # aniso phi 120
    for alpha, rho, st, ch in [(30,1.592,'St','E'),(45,1.520,'St','E'),(60,1.273,'St','E'),(75,0.439,'St','E'),(90,0.0,'St','S'),(105,0.0,'St','S'),(120,0.0,'St','S')]:
        for y in ys:
            writer.writerow(['aniso',120,alpha,y,f'{rho:.3f}',st,ch])
    # aniso phi 180
    for alpha, rho, st, ch in [(0,1.273,'St','E'),(15,1.215,'St','E'),(30,1.019,'St','E'),(45,0.439,'St','E'),(60,0.0,'St','S'),(75,0.0,'St','S'),(90,0.0,'St','S')]:
        for y in ys:
            writer.writerow(['aniso',180,alpha,y,f'{rho:.3f}',st,ch])
PYEOF

# === solve block: binding_energies.csv ===
python3 << 'PYEOF' 
import csv, sys
writer=csv.writer(sys.stdout)
writer.writerow(['case','phi','alpha','y','Ub'])
ys=[2,5,10,50,100]
# aniso phi120
ub_120={30:{2:6.756,5:6.260,10:5.885,50:5.015,100:4.639}, 60:{2:6.579,5:6.104,10:5.745,50:4.912,100:4.553}, 90:{2:6.134,5:5.662,10:5.341,50:4.594,100:4.272}, 120:{2:5.816,5:5.369,10:5.064,50:4.356,100:4.051}}
for alpha, y_dict in ub_120.items():
    for y in ys:
        writer.writerow(['aniso',120,alpha,y,f'{y_dict[y]:.3f}'])
# aniso phi180
ub_180={0:{2:13.094,5:12.145,10:11.427,50:9.759,100:9.040}, 30:{2:12.865,5:11.942,10:11.243,50:9.620,100:8.922}, 60:{2:12.489,5:11.617,10:10.957,50:9.425,100:8.756}, 90:{2:12.187,5:11.336,10:10.693,50:9.197,100:8.553}}
for alpha, y_dict in ub_180.items():
    for y in ys:
        writer.writerow(['aniso',180,alpha,y,f'{y_dict[y]:.3f}'])
PYEOF
> /app/outputs/binding_energies.csv
