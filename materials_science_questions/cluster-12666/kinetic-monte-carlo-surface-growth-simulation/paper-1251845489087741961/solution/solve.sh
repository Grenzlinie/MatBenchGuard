#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: scaling_exponents.csv ===
# Write scaling_exponents.csv from paper Tables 1 and 2
python3 <<'PYEOF'
import csv, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
path = os.path.join(outdir, "scaling_exponents.csv")

# Data from Tables 1 and 2 of the paper
# Columns: exponent_1z_x, exponent_1z_y, exponent_beta_x, exponent_beta_y, n_DS, surface_type
rows = [
    # Flat surface (x=y, same values for both directions)
    [0.2,  0.2,  1.8, 1.8, 1,  "flat"],
    [0.2,  0.2,  1.9, 1.9, 2,  "flat"],
    [0.25, 0.25, 2.0, 2.0, 5,  "flat"],
    [0.25, 0.25, 2.0, 2.0, 10, "flat"],
    [0.25, 0.25, 2.0, 2.0, 15, "flat"],
    [0.25, 0.25, 2.0, 2.0, 20, "flat"],
    # Vicinal surface
    [0.33, 0.2,  1.8,  1.8,  1,  "vicinal"],
    [0.33, 0.2,  1.8,  1.8,  2,  "vicinal"],
    [0.5,  0.25, 1.25, 1.25, 5,  "vicinal"],
    [0.5,  0.25, 1.25, 1.25, 10, "vicinal"],
    [0.75, 0.4,  1.1,  1.1,  15, "vicinal"],
    [0.75, 0.4,  0.75, 1.1,  20, "vicinal"],
]

with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["exponent_1z_x", "exponent_1z_y", "exponent_beta_x", "exponent_beta_y", "n_DS", "surface_type"])
    for row in rows:
        w.writerow(row)

print(f"Wrote {len(rows)} rows to {path}")
PYEOF

# === solve block: morphology_diagram_es.csv ===
# Write morphology_diagram_es.csv from paper Fig.9 / transition law
python3 <<'PYEOF'
import csv, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
path = os.path.join(outdir, "morphology_diagram_es.csv")

# Morphology classification derived from the paper's transition scaling
# law sqrt(n_DS)*exp(-E_ES) = const and explicit descriptions (Sections 3.2-3.4, Figs 5-9).
# Columns: E_ES, morphology, n_DS
# Grid: n_DS in [1,2,5,10,15,20]; E_ES in [0.0,1.0,2.0,2.2,2.4,2.5,2.6,2.8,3.0,4.0,5.0,6.0,7.0,8.0]

def classify(n_DS, E_ES):
    """Classify morphology based on transition scaling law."""
    # Meander region: the paper says 'For small E_ES, meandered structures always appear, irrespective of the diffusion rate'
    # Mound region: large E_ES, limited diffusion
    # Mixed: intermediate region where both features coexist
    # The transition follows sqrt(n_DS)*exp(-E_ES) ~ const
    # Boundaries calibrated from the detailed n_DS=5 scan (Fig.6): meander up to E_ES=2.0, mixed 2.2-2.8, mound at 3.0+
    import math
    val = math.sqrt(n_DS) * math.exp(-E_ES)
    if E_ES == 0.0:
        return "meander"
    if n_DS == 5:
        if E_ES <= 2.0: return "meander"
        if E_ES <= 2.8: return "mixed"
        return "mound"
    if n_DS == 1:
        if E_ES <= 1.0: return "meander"
        if E_ES <= 2.0: return "mixed"
        return "mound"
    if n_DS == 2:
        if E_ES <= 1.0: return "meander"
        if E_ES <= 2.5: return "mixed"
        return "mound"
    if n_DS == 10:
        if E_ES <= 2.5: return "meander"
        if E_ES <= 3.0: return "mixed"
        return "mound"
    if n_DS == 15:
        if E_ES <= 2.5: return "meander"
        if E_ES <= 3.0: return "mixed"
        return "mound"
    if n_DS == 20:
        if E_ES <= 3.0: return "meander"
        if E_ES <= 4.0: return "mound"  # no mixed at this n_DS in the sampled E_ES grid
        return "mound"
    # fallback
    if val > 0.24: return "meander"
    if val < 0.13: return "mound"
    return "mixed"

n_DS_vals = [1, 2, 5, 10, 15, 20]
E_ES_vals = [0.0, 1.0, 2.0, 2.2, 2.4, 2.5, 2.6, 2.8, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

rows = []
for n_DS in n_DS_vals:
    for E_ES in E_ES_vals:
        morph = classify(n_DS, E_ES)
        rows.append([E_ES, morph, n_DS])

with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["E_ES", "morphology", "n_DS"])
    for row in rows:
        w.writerow(row)

print(f"Wrote {len(rows)} rows to {path}")
PYEOF

# === solve finalize ===
echo "All scored artifacts written to $OUTDIR:"
ls -la "$OUTDIR/"
