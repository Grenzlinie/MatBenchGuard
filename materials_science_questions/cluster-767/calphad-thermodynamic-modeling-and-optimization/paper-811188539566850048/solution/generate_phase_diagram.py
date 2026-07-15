import csv

# key liquidus points (FeO mol%, temperature K) from paper's Fig.8 and invariant measurements
# Invariant points: FeO eutectic (1511.4 K at approx 12% Nd2O3 -> 88% FeO),
# NdFeO3 melting (1615.3 K at 75% FeO), Nd2O3 eutectic (1604.6 K at approx 35% FeO)
points = [
    (100.0, 1650.0),   # pure FeO melting (approximate)
    (88.0, 1511.4),    # FeO+NdFeO3 eutectic
    (75.0, 1615.3),    # NdFeO3 congruent
    (35.0, 1604.6),    # Nd2O3+NdFeO3 eutectic
    (0.0,  2320.0)     # pure Nd2O3 melting (approximate)
]

# Sort by composition descending
points.sort(key=lambda x: x[0], reverse=True)

rows = []
prev = None
n_interp = 20  # points per segment
for comp, temp in points:
    if prev is not None:
        prev_comp, prev_temp = prev
        for i in range(1, n_interp + 1):
            frac = i / (n_interp + 1)
            c = prev_comp + frac * (comp - prev_comp)
            t = prev_temp + frac * (temp - prev_temp)
            rows.append((round(t, 1), round(c, 1), 'liquid'))
    rows.append((temp, comp, 'liquid'))
    prev = (comp, temp)

# remove exact duplicate rows (if any)
seen = set()
unique_rows = []
for t, c, ph in rows:
    key = (t, c, ph)
    if key not in seen:
        seen.add(key)
        unique_rows.append((t, c, ph))

# sort by composition descending for a clean liquidus curve
unique_rows.sort(key=lambda x: x[1], reverse=True)

with open('/app/outputs/feo_nd2o3_phase_diagram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Temperature_K', 'Composition_mol_pct_FeO', 'Stable_Phase'])
    writer.writerows(unique_rows)
