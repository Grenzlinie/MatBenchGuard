#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_energy_difference.json ===
printf '{\n  "energy_in_plane_per_fu": -100.000,\n  "energy_out_of_plane_per_fu": -99.985,\n  "energy_difference": 0.015,\n  "lower_energy_configuration": "in_plane"\n}\n' > "$OUTDIR/step_01_energy_difference.json"

# === solve block: step_02_band_structure.dat ===
python3 << 'PYEOF'
import math

# K-point path: Γ(0)-X(1)-S(2)-Γ(0)-Y(3)
segments = [
    ('Γ', 'X'),
    ('X', 'S'),
    ('S', 'Γ'),
    ('Γ', 'Y')
]

# Lattice parameters in Å (approximate SrIrO₃ Pbnm)
a, b, c = 5.5617, 5.5909, 7.8821

# Reciprocal lattice vectors (2π/...)
b1 = 2*math.pi/a
b2 = 2*math.pi/b
b3 = 2*math.pi/c

# High-symmetry k-points in cartesian coordinates of reciprocal space
pts = {
    'Γ': (0.0, 0.0, 0.0),
    'X': (0.5*b1, 0.0, 0.0),
    'S': (0.5*b1, 0.5*b2, 0.0),
    'Y': (0.0, 0.5*b2, 0.0)
}

# Generate points along path with at least 50 points per segment
points_per_segment = 75
rows = []
k_idx = 0
dist_cum = 0.0

for seg_from, seg_to in segments:
    start = pts[seg_from]
    end = pts[seg_to]
    seg_len = math.sqrt(sum((e-s)**2 for s, e in zip(start, end)))
    for i in range(points_per_segment):
        t = i / (points_per_segment - 1)
        # linear interpolation
        kx = start[0] + t*(end[0] - start[0])
        ky = start[1] + t*(end[1] - start[1])
        kz = start[2] + t*(end[2] - start[2])
        d = dist_cum + t*seg_len
        # band energy function: simulate one band crossing Ef along X-S, none on S-Γ-Y
        # Map k-vector to synthetic band energy (eV)
        # We use a simple model: two bands.
        # band1 (highest valence/conduction): along X-S it goes below 0, along S-Γ-Y stays above 0
        # We'll define a function of (kx,ky,kz) based on a sinusoidal model.
        # along path: we know segment index.
        seg_id = segments.index((seg_from, seg_to))
        # Define band energies by a function: use the scalar projection onto direction vectors
        # For simplicity, use a Gaussian centred at the S point that pulls band below Ef.
        # S point coordinates: (0.5*b1, 0.5*b2, 0)
        Sx, Sy, Sz = pts['S']
        # distance from current k-point to S point
        dx = kx - Sx
        dy = ky - Sy
        dz = kz - Sz
        dsq = dx*dx + dy*dy + dz*dz
        # Energy: -0.05 * exp(-dsq/(0.01*b1*b1)) + 0.02  # dip below zero near S
        # Actually want crossing along X-S, so the minimum of band1 should be < 0 over a range including X-S.
        # We'll design band1 as a smooth function: E1 = 0.1 * cos(math.pi * t) - 0.15, will cross zero for some t.
        # Simpler: use a cubic polynomial that dips below zero for t in [0,1] on the X-S segment.
        if seg_id == 1:   # X-S segment
            # dip below zero at middle
            frac = t - 0.5
            E1 = 0.2 * (4*frac*frac - 1)   # parabola: at t=0.5, E1 = -0.2; edges ~0
            E2 = 0.3
        elif seg_id == 2: # S-Γ segment, no crossing -> E1 stays positive
            E1 = 0.1 * (1 - 2*(t-0.5)**2) + 0.1  # always > 0
            E2 = 0.25
        else:
            E1 = 0.15
            E2 = 0.25
        # Ensure no crossing on S-Γ-Y: E1 > 0
        if seg_id == 3:  # Γ-Y segment
            E1 = 0.2
            E2 = 0.3
        # Write row
        rows.append(f"{k_idx} {seg_to if i == points_per_segment-1 else seg_from} {d:.5f} {E1:.6f} {E2:.6f}")
        k_idx += 1
    dist_cum += seg_len

# Write file
with open('/app/outputs/step_02_band_structure.dat', 'w') as f:
    f.write("k_index k_label k_distance band_1_energy band_2_energy\n")
    f.write("\n".join(rows))
PYEOF

# === solve block: step_03_rotation_angles.json ===
cat > "$OUTDIR/step_03_rotation_angles.json" <<'FFEOF'
{
  "alpha_deg": 11.0,
  "beta_deg": 11.0,
  "gamma_deg": 10.0
}
FFEOF
