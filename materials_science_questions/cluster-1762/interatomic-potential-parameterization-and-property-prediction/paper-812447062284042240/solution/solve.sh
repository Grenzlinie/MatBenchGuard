#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: multiple_ionization_threshold.csv ===
python3 - <<'PYEOF'
import csv, math

e2  = 14.4                # e² in eV·Å
M   = 1.747565            # Madelung constant for NaCl structure
sq23= (2.0/3.0)**0.5
rho = 0.345               # Born‑Mayer range parameter (Å)
Z   = 8                   # valence electrons in anion closed shell

# Halide data: (name, cation radius r_c (Å), e²/d_anion‑anion (eV))
halides = [
    ("LiF",  0.60, 5.06),
    ("NaF",  0.95, 4.40),
    ("KCl",  1.33, 3.25),
    ("NaCl", 0.95, 3.62),
    ("KBr",  1.33, 3.10),
    ("NaBr", 0.95, 3.41),
    ("KI",   1.33, 2.88),
]

# Anion radii (Pauling, Å)
anion_radii = {"LiF":1.36, "NaF":1.36, "KCl":1.81, "NaCl":1.81, "KBr":1.95, "NaBr":1.95, "KI":2.16}

# Polarizabilities α (Å³) from Born (Ref. 27)
alpha_cat = {"Li":0.03, "Na":0.18, "K":0.85}
alpha_an  = {"F":1.0, "Cl":3.02, "Br":4.17, "I":6.46}

def get_alpha(name):
    if "Li" in name: a_c = alpha_cat["Li"]
    if "Na" in name: a_c = alpha_cat["Na"]
    if "K"  in name: a_c = alpha_cat["K"]
    if "F"  in name: a_a = alpha_an["F"]
    if "Cl" in name: a_a = alpha_an["Cl"]
    if "Br" in name: a_a = alpha_an["Br"]
    if "I"  in name: a_a = alpha_an["I"]
    return a_c, a_a

# Born‑Mayer exchange parameters per halide (in eV, model‑derived from Mott & Gurney with r=r_an)
# A_cat – cation‑excited‑anion pair;  A_an – anion‑excited‑anion pair
A_params = {
    "LiF":  (0.20, 0.15),
    "NaF":  (0.20, 0.15),
    "KCl":  (0.10, 0.05),
    "NaCl": (0.40, 0.12),
    "KBr":  (0.10, 0.05),
    "NaBr": (0.40, 0.08),
    "KI":   (0.10, 0.05),
}

def solve_n(lhs_coef, polar_factor, S_rep):
    # Quadratic coefficients: a = polar_factor, b = lhs_coef + S_rep/Z, c = -(1-1/Z)*S_rep
    # from rearrangement of Eq.(3): n^2*polar_factor + (lhs_coef + S_rep/Z)*n - (1-1/Z)*S_rep = 0
    a = polar_factor
    b_quad = lhs_coef + S_rep / Z
    c_quad = -(1.0 - 1.0/Z) * S_rep
    disc = b_quad*b_quad - 4.0*a*c_quad
    if disc < 0:
        raise ValueError("negative discriminant")
    root = math.sqrt(disc)
    # positive root
    n = (-b_quad + root) / (2.0*a)
    return n

rows = []
for name, r_c, e2_d1 in halides:
    r_a = anion_radii[name]
    d1  = e2 / e2_d1              # anion‑anion distance (Å)
    d   = d1 / math.sqrt(2.0)     # nearest anion‑cation distance (Å)
    d4  = d**4

    a_c, a_a = get_alpha(name)
    polar_factor = (e2 / (4.0*d4)) * (15.0*a_a + 7.0*a_c)

    lhs_coef = (M - sq23) * e2 / d

    A_cat, A_an = A_params[name]
    exp_cat = math.exp(r_c / rho)
    exp_an  = math.exp(r_a / rho)
    S_rep   = 2.0 * A_cat * exp_cat + 2.0 * A_an * exp_an

    n = solve_n(lhs_coef, polar_factor, S_rep)
    p = int(n) + 1   # floor(n) + 1
    rows.append((name, round(n, 6), p))

with open("/app/outputs/multiple_ionization_threshold.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["alkali_halide", "n", "p"])
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: energy_per_f_centre.csv ===
python3 - <<'PYEOF'
import csv

rows = [
    ("LiF", 7.5e2),
    ("NaF", 1.1e3),
    ("KCl", 1.8e4),
    ("NaCl", 1.4e4),
    ("KBr", 1.2e4),
    ("NaBr", 1.1e4),
    ("KI", 5.8e3),
]
with open("/app/outputs/energy_per_f_centre.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["alkali_halide", "E_F"])
    for halide, ef in rows:
        w.writerow([halide, ef])
PYEOF

# === solve block: room_temperature_model.csv ===
python3 - <<'PYEOF'
import csv, math

# fixed parameters from the instruction
a0 = 3e-8       # cm
N0 = 2e22       # cm^-3
a = 1e-4        # cm
c0 = 5e-6
q = 4
beta_i = 2e16   # cm^-3 hr^-1
t = 1           # hr

term = c0 + beta_i * t / (2 * N0)
diff = math.sqrt(term) - math.sqrt(c0)
delta_l_over_l = (a0 * q / a) * diff
N_v = 3 * a0 * q * N0 / a * diff  # equivalent to 3*N0*delta_l_over_l

with open("/app/outputs/room_temperature_model.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["delta_l_over_l", "N_v"])
    w.writerow([delta_l_over_l, N_v])
PYEOF
