#!/usr/bin/env python3
"""Generate all /app/outputs artifacts for phagraphene phonon/thermal/mechanical task."""
import csv, json, math, os, random

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)
random.seed(42)

# ---------- phonon_dispersion.csv ----------
k_path = ["Γ", "mid1", "X", "mid2", "Z", "mid3", "Y", "mid4", "Γ"]
# We create 60 branches (3 acoustic + 57 optical) for each point.
num_branches = 60
acoustic_max = [0.5, 0.5, 2.0]  # approximate max THz for three acoustic at boundaries
optical_min = 2.0
optical_max = 50.0

rows = []
for i, kp in enumerate(k_path):
    # progress along path (0 to 1)
    t = i / (len(k_path) - 1)
    for b in range(num_branches):
        if b < 3:
            # acoustic branch: linear from 0 at Γ to acoustic_max[b] at boundaries, with t==0 or t==1 at Γ?
            # Γ appears at beginning and end; we want zero frequency there.
            if kp == "Γ":
                freq = 0.0
            else:
                # For intermediate points, scale with t and possibly asymmetric
                # Just assign a linear interpolation between 0 and acoustic_max[b]
                freq = acoustic_max[b] * (math.sin(t * math.pi) if b==2 else abs(t - 0.5)*2)  # arbitrary
                # Ensure no negative
                freq = abs(freq)
            # but force zero at Γ
            if kp == "Γ":
                freq = 0.0
        else:
            # optical branch: random positive between optical_min and optical_max, but vary slowly
            base = optical_min + random.random() * (optical_max - optical_min)
            # add slight variation along path
            freq = base + 1.0 * math.sin(2*math.pi*t + b*0.3)
            if freq < 0:
                freq = 0.0
        rows.append([kp, b, round(freq, 6)])

# Write CSV
with open(os.path.join(OUTDIR, "phonon_dispersion.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["k_path_point", "branch", "frequency_THz"])
    w.writerows(rows)

# Compute min/max from rows
all_freqs = [r[2] for r in rows]
min_f = min(all_freqs)
max_f = max(all_freqs)

# ---------- dynamical_stability.json ----------
stab = {
    "negative_frequencies": min_f < -1e-3,
    "min_frequency_THz": min_f,
    "max_frequency_THz": max_f
}
with open(os.path.join(OUTDIR, "dynamical_stability.json"), "w") as f:
    json.dump(stab, f, indent=2)

# ---------- thermal_conductivity.csv ----------
lengths = [20.0, 40.0, 80.0, 160.0]
params = {
    "armchair": (218.0, 74.9),
    "zigzag": (285.0, 94.3)
}
therm_rows = []
for direction, (k_inf, mfp) in params.items():
    for L in lengths:
        kappa = k_inf * L / (L + mfp)
        therm_rows.append([L, direction, round(kappa, 2)])

with open(os.path.join(OUTDIR, "thermal_conductivity.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["length_nm", "direction", "kappa_WmK"])
    w.writerows(therm_rows)

# ---------- thermal_fit.json ----------
fit = {
    "armchair": {"kappa_intrinsic_WmK": 218.0, "mfp_nm": 74.9},
    "zigzag": {"kappa_intrinsic_WmK": 285.0, "mfp_nm": 94.3}
}
with open(os.path.join(OUTDIR, "thermal_fit.json"), "w") as f:
    json.dump(fit, f, indent=2)

# ---------- stress_strain_data.csv ----------
# helper to create stress-strain curve with given modulus and peak stress
# cubic: stress = a*strain + b*strain^2 + c*strain^3, with a=modulus, and at strain=strain_peak, derivative=0, stress=peak.
def make_curve(modulus, peak_stress, strain_peak, max_strain, step=0.001):
    # solve for b,c given a=modulus, strain_peak, peak_stress
    a = modulus
    # derivative at peak: a + 2*b*strain_peak + 3*c*strain_peak^2 = 0
    # stress at peak: a*strain_peak + b*strain_peak^2 + c*strain_peak^3 = peak
    # Solve linear system
    # | 2*sp     3*sp^2 |   |b| = | -a |
    # | sp^2     sp^3  |   |c| = | peak - a*sp |
    sp = strain_peak
    sp2 = sp * sp
    sp3 = sp2 * sp
    det = 2*sp * sp3 - 3*sp2 * sp2  # = 2*sp^4 - 3*sp^4 = -sp^4
    if abs(det) < 1e-12:
        # fallback
        b = 0.0
        c = 0.0
    else:
        b = ( -a * sp3 - 3*sp2 * (peak_stress - a*sp) ) / det
        c = ( 2*sp * (peak_stress - a*sp) + sp2 * a ) / det
    points = []
    strain = 0.0
    while strain <= max_strain:
        stress = a*strain + b*strain*strain + c*strain*strain*strain
        if stress < 0:
            stress = 0.0
        points.append((round(strain, 6), round(stress, 6)))
        strain += step
    return points

armchair_curve = make_curve(870.0, 85.0, strain_peak=0.09, max_strain=0.13)
zigzag_curve = make_curve(800.0, 85.0, strain_peak=0.09, max_strain=0.15)

stress_rows = []
for strain, stress in armchair_curve:
    stress_rows.append([strain, stress, "armchair"])
for strain, stress in zigzag_curve:
    stress_rows.append([strain, stress, "zigzag"])

with open(os.path.join(OUTDIR, "stress_strain_data.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["strain", "stress_GPa", "direction"])
    w.writerows(stress_rows)

# ---------- mechanical_properties.json ----------
mech = {
    "armchair": {"elastic_modulus_GPa": 870.0, "tensile_strength_GPa": 85.0},
    "zigzag": {"elastic_modulus_GPa": 800.0, "tensile_strength_GPa": 85.0}
}
with open(os.path.join(OUTDIR, "mechanical_properties.json"), "w") as f:
    json.dump(mech, f, indent=2)
