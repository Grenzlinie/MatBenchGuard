import csv
import math

OUTDIR = "/app/outputs"

# Experimental enthalpies of formation (ΔfH° at 298.15 K, kJ/mol)
EXPT = {
    "CH4": -74.9,
    "CH3F": -232.6,
    "CH2F2": -452.2,
    "CHF3": -697.6,
    "CF4": -933.0,
    "CH3Cl": -83.7,
    "CH2Cl2": -95.5,
    "CHCl3": -103.2,
    "CCl4": -96.0,
    "CH2FCl": -261.9,
    "CHF2Cl": -481.6,
    "CF3Cl": -707.9,
    "CHFCl2": -283.3,
    "CF2Cl2": -491.6,
    "CFCl3": -288.7,
}

# Ordered species list
SPECIES = [
    "CH4", "CH3F", "CH2F2", "CHF3", "CF4",
    "CH3Cl", "CH2Cl2", "CHCl3", "CCl4",
    "CH2FCl", "CHF2Cl", "CF3Cl", "CHFCl2", "CF2Cl2", "CFCl3"
]

# Methods
METHODS = ["G2", "G2(MP2)", "CBS-4", "CBS-Q"]

# Uncorrected enthalpies (kJ/mol) from Table 3A
UNCORRECTED = {
    ("G2", "CH4"): -77.7, ("G2", "CH3F"): -244.1, ("G2", "CH2F2"): -463.7,
    ("G2", "CHF3"): -714.0, ("G2", "CF4"): -956.5, ("G2", "CH3Cl"): -85.5,
    ("G2", "CH2Cl2"): -98.1, ("G2", "CHCl3"): -107.6, ("G2", "CCl4"): -107.7,
    ("G2", "CH2FCl"): -273.3, ("G2", "CHF2Cl"): -498.1, ("G2", "CF3Cl"): -731.8,
    ("G2", "CHFCl2"): -295.8, ("G2", "CF2Cl2"): -513.9, ("G2", "CFCl3"): -305.2,

    ("G2(MP2)", "CH4"): -75.6, ("G2(MP2)", "CH3F"): -245.0, ("G2(MP2)", "CH2F2"): -466.9,
    ("G2(MP2)", "CHF3"): -718.9, ("G2(MP2)", "CF4"): -962.6, ("G2(MP2)", "CH3Cl"): -88.1,
    ("G2(MP2)", "CH2Cl2"): -105.2, ("G2(MP2)", "CHCl3"): -119.2, ("G2(MP2)", "CCl4"): -123.2,
    ("G2(MP2)", "CH2FCl"): -278.3, ("G2(MP2)", "CHF2Cl"): -504.7, ("G2(MP2)", "CF3Cl"): -739.6,
    ("G2(MP2)", "CHFCl2"): -304.7, ("G2(MP2)", "CF2Cl2"): -524.0, ("G2(MP2)", "CFCl3"): -317.8,

    ("CBS-4", "CH4"): -77.6, ("CBS-4", "CH3F"): -236.9, ("CBS-4", "CH2F2"): -451.1,
    ("CBS-4", "CHF3"): -696.9, ("CBS-4", "CF4"): -936.6, ("CBS-4", "CH3Cl"): -88.9,
    ("CBS-4", "CH2Cl2"): -108.6, ("CBS-4", "CHCl3"): -126.5, ("CBS-4", "CCl4"): -143.8,
    ("CBS-4", "CH2FCl"): -272.5, ("CBS-4", "CHF2Cl"): -494.4, ("CBS-4", "CF3Cl"): -725.9,
    ("CBS-4", "CHFCl2"): -304.8, ("CBS-4", "CF2Cl2"): -522.1, ("CBS-4", "CFCl3"): -326.0,

    ("CBS-Q", "CH4"): -74.0, ("CBS-Q", "CH3F"): -238.7, ("CBS-Q", "CH2F2"): -457.6,
    ("CBS-Q", "CHF3"): -706.7, ("CBS-Q", "CF4"): -947.7, ("CBS-Q", "CH3Cl"): -86.3,
    ("CBS-Q", "CH2Cl2"): -105.6, ("CBS-Q", "CHCl3"): -125.3, ("CBS-Q", "CCl4"): -137.3,
    ("CBS-Q", "CH2FCl"): -272.3, ("CBS-Q", "CHF2Cl"): -495.9, ("CBS-Q", "CF3Cl"): -728.2,
    ("CBS-Q", "CHFCl2"): -301.4, ("CBS-Q", "CF2Cl2"): -517.4, ("CBS-Q", "CFCl3"): -318.8,
}

# BAC-corrected enthalpies (kJ/mol) from Table 3B
CORRECTED = {
    ("G2", "CH4"): -77.7, ("G2", "CH3F"): -237.6, ("G2", "CH2F2"): -450.7,
    ("G2", "CHF3"): -694.5, ("G2", "CF4"): -930.5, ("G2", "CH3Cl"): -82.7,
    ("G2", "CH2Cl2"): -92.4, ("G2", "CHCl3"): -99.2, ("G2", "CCl4"): -96.5,
    ("G2", "CH2FCl"): -264.0, ("G2", "CHF2Cl"): -482.3, ("G2", "CF3Cl"): -709.4,
    ("G2", "CHFCl2"): -283.7, ("G2", "CF2Cl2"): -495.3, ("G2", "CFCl3"): -290.3,

    ("G2(MP2)", "CH4"): -75.6, ("G2(MP2)", "CH3F"): -237.0, ("G2(MP2)", "CH2F2"): -450.9,
    ("G2(MP2)", "CHF3"): -695.0, ("G2(MP2)", "CF4"): -930.7, ("G2(MP2)", "CH3Cl"): -81.6,
    ("G2(MP2)", "CH2Cl2"): -92.1, ("G2(MP2)", "CHCl3"): -99.5, ("G2(MP2)", "CCl4"): -97.1,
    ("G2(MP2)", "CH2FCl"): -263.7, ("G2(MP2)", "CHF2Cl"): -482.2, ("G2(MP2)", "CF3Cl"): -709.1,
    ("G2(MP2)", "CHFCl2"): -283.6, ("G2(MP2)", "CF2Cl2"): -495.0, ("G2(MP2)", "CFCl3"): -290.2,

    ("CBS-4", "CH4"): -77.6, ("CBS-4", "CH3F"): -235.6, ("CBS-4", "CH2F2"): -448.5,
    ("CBS-4", "CHF3"): -693.1, ("CBS-4", "CF4"): -931.2, ("CBS-4", "CH3Cl"): -78.3,
    ("CBS-4", "CH2Cl2"): -87.4, ("CBS-4", "CHCl3"): -94.7, ("CBS-4", "CCl4"): -101.3,
    ("CBS-4", "CH2FCl"): -260.6, ("CBS-4", "CHF2Cl"): -481.2, ("CBS-4", "CF3Cl"): -711.4,
    ("CBS-4", "CHFCl2"): -282.3, ("CBS-4", "CF2Cl2"): -498.3, ("CBS-4", "CFCl3"): -292.9,

    ("CBS-Q", "CH4"): -74.0, ("CBS-Q", "CH3F"): -235.2, ("CBS-Q", "CH2F2"): -450.6,
    ("CBS-Q", "CHF3"): -696.2, ("CBS-Q", "CF4"): -933.7, ("CBS-Q", "CH3Cl"): -77.8,
    ("CBS-Q", "CH2Cl2"): -88.6, ("CBS-Q", "CHCl3"): -99.8, ("CBS-Q", "CCl4"): -103.3,
    ("CBS-Q", "CH2FCl"): -260.3, ("CBS-Q", "CHF2Cl"): -480.4, ("CBS-Q", "CF3Cl"): -709.2,
    ("CBS-Q", "CHFCl2"): -280.9, ("CBS-Q", "CF2Cl2"): -493.4, ("CBS-Q", "CFCl3"): -289.8,
}


def write_enthalpies():
    fieldnames = ["species", "method", "enthalpy_type", "delta_H", "deviation_from_expt"]
    rows = []
    for sp in SPECIES:
        exp = EXPT[sp]
        for m in METHODS:
            unc_dh = UNCORRECTED[(m, sp)]
            dev_unc = round(unc_dh - exp, 1)
            rows.append({
                "species": sp,
                "method": m,
                "enthalpy_type": "uncorrected",
                "delta_H": unc_dh,
                "deviation_from_expt": dev_unc,
            })
            cor_dh = CORRECTED[(m, sp)]
            dev_cor = round(cor_dh - exp, 1)
            rows.append({
                "species": sp,
                "method": m,
                "enthalpy_type": "corrected",
                "delta_H": cor_dh,
                "deviation_from_expt": dev_cor,
            })

    with open(f"{OUTDIR}/step_03_enthalpies.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_summary():
    # collect corrected deviations per method
    devs = {m: [] for m in METHODS}
    for sp in SPECIES:
        exp = EXPT[sp]
        for m in METHODS:
            cor_dh = CORRECTED[(m, sp)]
            dev = cor_dh - exp
            devs[m].append(dev)

    summary_rows = []
    for m in METHODS:
        d_list = devs[m]
        mean_dev = sum(d_list) / len(d_list)
        mean_sq = sum(d*d for d in d_list) / len(d_list)
        rms_dev = math.sqrt(mean_sq)
        summary_rows.append({
            "method": m,
            "enthalpy_type": "corrected",
            "rms_deviation": round(rms_dev, 1),
            "avg_deviation": round(mean_dev, 1),
        })

    fieldnames = ["method", "enthalpy_type", "rms_deviation", "avg_deviation"]
    with open(f"{OUTDIR}/step_04_summary.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)


if __name__ == "__main__":
    write_enthalpies()
    write_summary()
