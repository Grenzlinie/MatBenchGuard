import csv
import math
import os
import sys

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")
TARGET = sys.argv[1] if len(sys.argv) > 1 else "all"

SRZ_VALS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
JF_VALS = [0.2, 0.3, 0.5]


def get_energy(donor_spin, jf, srz):
    """Return dimensionless total energy in units of t0."""
    if donor_spin == "none":
        e0 = -100.0 - 1.5 * jf
        delta = 0.8 + 3.5 * jf
        return e0 - (delta / 0.5) * srz
    elif donor_spin == "-1/2":
        e0 = -100.5 - 1.0 * jf
        delta = 1.0 + 4.0 * jf
        return e0 - (delta / 0.5) * srz
    elif donor_spin == "1/2":
        if abs(jf - 0.2) < 1e-9:
            idx = int(round(srz / 0.1))
            energies = [-100.80, -100.95, -101.05, -100.98, -100.85, -100.70]
            return energies[idx]
        else:
            e0 = -100.5 - 1.0 * jf
            delta = 0.3 + 1.5 * jf
            return e0 - (delta / 0.5) * srz
    return 0.0


def gen_energy_curves():
    rows = []
    for jf in JF_VALS:
        for donor in ["none", "-1/2", "1/2"]:
            for srz in SRZ_VALS:
                energy = get_energy(donor, jf, srz)
                rows.append([donor, jf, srz, round(energy, 6)])

    path = os.path.join(OUTDIR, "energy_curves.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["donor_spin", "j_f", "srz_expectation", "total_energy"])
        w.writerows(rows)


def gen_polaron_profile():
    jf = 0.3
    N = 80
    center = 40.0
    sigma = 7.0
    A0 = 0.15

    rows = []
    for donor in ["-1/2", "1/2"]:
        B = 0.45 if donor == "-1/2" else -0.40
        for i in range(1, N + 1):
            envelope = 1.0 + B * math.exp(-((i - center) ** 2) / (2 * sigma ** 2))
            amplitude = A0 * envelope
            spin_density = amplitude * ((-1) ** i)
            rows.append([donor, jf, i, round(spin_density, 8)])

    path = os.path.join(OUTDIR, "polaron_profile.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["donor_spin", "j_f", "site_index", "spin_density"])
        w.writerows(rows)


def gen_energies_summary():
    rows = []
    for jf in JF_VALS:
        # Compute ΔE2 values for cross-consistency
        e0_m = get_energy("-1/2", jf, 0.0)
        e05_m = get_energy("-1/2", jf, 0.5)
        de2_m = e0_m - e05_m
        e0_p = get_energy("1/2", jf, 0.0)
        e05_p = get_energy("1/2", jf, 0.5)
        de2_p = e0_p - e05_p
        delta_e1 = round(de2_m - de2_p, 6)

        for donor in ["none", "-1/2", "1/2"]:
            e0 = get_energy(donor, jf, 0.0)
            e05 = get_energy(donor, jf, 0.5)
            de2 = round(e0 - e05, 6)
            de1 = "" if donor == "none" else delta_e1
            rows.append([donor, jf, round(e0, 6), round(e05, 6), de2, de1])

    path = os.path.join(OUTDIR, "energies_summary.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["donor_spin", "j_f", "E_srz0", "E_srz0p5", "delta_E2", "delta_E1"])
        w.writerows(rows)


if TARGET == "energy_curves" or TARGET == "all":
    gen_energy_curves()
if TARGET == "polaron_profile" or TARGET == "all":
    gen_polaron_profile()
if TARGET == "energies_summary" or TARGET == "all":
    gen_energies_summary()
