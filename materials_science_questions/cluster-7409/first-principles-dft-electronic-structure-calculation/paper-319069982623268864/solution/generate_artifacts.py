#!/usr/bin/env python3
"""Generate total_dos_all_compositions.dat and band_gap_summary.csv
for the α-Al₂O₃ CPA‑DFT reproduction oracle.
"""
import csv, math, sys, os

OUTDIR = sys.argv[1]

# Compositions and their properties
comps = [
    ("pure α-Al₂O₃",           8.3,  False),
    ("Al₁.₉₄Zr₀.₀₆O₃",        None, True),
    ("Al₁.₉₄Nb₀.₀₆O₃",        None, True),
    ("Al₁.₉₄Mo₀.₀₆O₃",        None, True),
    ("Al₁.₉₄O₃",              None, True),   # Al vacancy  – metallic
    ("Al₁.₉₇Ga₀.₀₃O₃",        8.1,  False),
    ("Al₁.₉₆Zr₀.₀₃O₃",        7.2,  False),
    ("Al₁.₉₅Nb₀.₀₃O₃",        5.7,  False),
    ("Al₁.₉₄Mo₀.₀₃O₃",        4.3,  False),
    ("Al₁.₉₇Ga₀.₀₃O₂.₉₇",     2.1,  False),
    ("Al₁.₉₆Zr₀.₀₃O₂.₉₇",     1.6,  False),
    ("Al₁.₉₁Nb₀.₀₃Sn₀.₀₆O₂.₉₇", 1.6,  False),
]

def gauss(e, mu, sigma):
    return math.exp(-0.5 * ((e - mu) / sigma) ** 2)

def make_dos(gap, metallic):
    """Return a function dos(e) for one composition.
    gap: band gap in eV (None for metallic).
    metallic: if True, add impurity band at 0.
    """
    sigma = 1.5
    if gap is not None:
        half = gap / 2.0
        mu_vb = -half - 1.0
        mu_cb =  half + 1.0
        def func(e):
            d = 0.0
            if e < -half:
                d += gauss(e, mu_vb, sigma)
            if e > half:
                d += gauss(e, mu_cb, sigma)
            if metallic:
                d += 0.5 * gauss(e, 0.0, 0.2)
            return d
    else:  # metallic but no explicit gap – still have wide VB/CB
        # Use a gap of 0.1 just to place VB/CB away from 0
        half = 0.05
        mu_vb = -half - 1.0
        mu_cb =  half + 1.0
        def func(e):
            d = gauss(e, mu_vb, sigma) + gauss(e, mu_cb, sigma)
            if metallic:
                d += 0.5 * gauss(e, 0.0, 0.2)
            return d
    return func

# Energy grid
emin, emax, step = -10.0, 10.0, 0.01
npts = int((emax - emin) / step) + 1
energies = [emin + i * step for i in range(npts)]

# Write total_dos file
dos_path = os.path.join(OUTDIR, "total_dos_all_compositions.dat")
with open(dos_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="\t")
    for comp_name, gap, metallic in comps:
        f.write(f"# composition: {comp_name}\n")
        dos_fn = make_dos(gap, metallic)
        for e in energies:
            writer.writerow([comp_name, f"{e:.2f}", f"{dos_fn(e):.6f}"])

# Write band_gap_summary
summary_path = os.path.join(OUTDIR, "band_gap_summary.csv")
with open(summary_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["composition", "band_gap"])
    for comp_name, gap, metallic in comps:
        if metallic:
            writer.writerow([comp_name, "metallic"])
        else:
            writer.writerow([comp_name, f"{gap:.1f}"])
