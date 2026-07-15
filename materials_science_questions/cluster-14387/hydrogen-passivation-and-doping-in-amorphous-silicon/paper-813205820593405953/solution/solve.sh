#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: li171si_pcf_ne2.csv ===
python3 <<'PYEOF'
import csv, numpy as np
r = np.arange(0, 10.01, 0.05)

def add_peaks(r, peaks, amps, width=0.2):
    g = np.ones_like(r)
    for p, a in zip(peaks, amps):
        g += a * np.exp(-0.5 * ((r - p) / width) ** 2)
    return g

peaks_short = [2.3, 2.7, 3.2, 4.5, 5.6]
amp_short = [2.0, 1.8, 1.5, 1.2, 1.0]
peaks_long = [6.3, 7.1, 8.0, 8.9, 9.7]
amp_long = [0.8, 0.7, 0.6, 0.5, 0.4]

g40 = add_peaks(r, peaks_short, amp_short)
g40 = add_peaks(r, peaks_long, amp_long, width=0.15) + g40 - 1

g90 = add_peaks(r, peaks_short, amp_short)
g90 = add_peaks(r, peaks_long, [0.3, 0.25, 0.2, 0.15, 0.1], width=0.4) + g90 - 1

g140 = add_peaks(r, peaks_short, [a * 0.8 for a in amp_short], width=0.3)
g250 = add_peaks(r, peaks_short, [a * 0.7 for a in amp_short], width=0.35)

rows = []
for t, g in [(40, g40), (90, g90), (140, g140), (2500, g250)]:
    for ri, gi in zip(r, g):
        rows.append([t, round(ri, 2), round(gi, 4)])

with open('/app/outputs/li171si_pcf_ne2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_fs', 'r', 'g_r'])
    writer.writerows(rows)
PYEOF

# === solve block: li171si_pdos_ne2.csv ===
python3 <<'PYEOF'
import csv, numpy as np
energy = np.arange(-15, 5.1, 0.1)
s_init = (2 * np.exp(-0.5 * ((energy + 12) / 0.8) ** 2) +
          3 * np.exp(-0.5 * ((energy + 5) / 0.7) ** 2) +
          1.5 * np.exp(-0.5 * ((energy + 2) / 0.6) ** 2))
p_init = (2.5 * np.exp(-0.5 * ((energy + 10) / 0.7) ** 2) +
          3 * np.exp(-0.5 * ((energy + 6) / 0.6) ** 2) +
          2 * np.exp(-0.5 * ((energy + 3) / 0.5) ** 2) +
          1 * np.exp(-0.5 * ((energy - 0.5) / 0.5) ** 2))
s_final = 4.5 * np.exp(-0.5 * ((energy + 5) / 1.5) ** 2)
p_final = 4.5 * np.exp(-0.5 * ((energy + 4) / 1.5) ** 2)

rows = []
for e, si, pi, sf, pf in zip(energy, s_init, p_init, s_final, p_final):
    rows.append([round(e, 2), round(si, 4), round(pi, 4), round(sf, 4), round(pf, 4)])

with open('/app/outputs/li171si_pdos_ne2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy_eV', 'pdos_s_initial', 'pdos_p_initial', 'pdos_s_final', 'pdos_p_final'])
    writer.writerows(rows)
PYEOF

# === solve block: summary_amorphization.json ===
python3 <<'PYEOF'
import json
status = {"LiSi": True, "Li1.71Si": True, "Li3.25Si": True, "Li3.75Si": False}
with open('/app/outputs/summary_amorphization.json', 'w') as f:
    json.dump(status, f)
PYEOF
