#!/usr/bin/env python3
"""Synthesize reference outputs for the TaN DFT reproduction task.
Output filenames are given as the first argument; the script writes
the corresponding CSV to /app/outputs/<filename>.
"""
import sys
import csv
import numpy as np

OUTDIR = "/app/outputs"

# Birch-Murnaghan 3rd-order equation of state (energy in eV, volume in Å³/f.u.)
def birch_murnaghan(V, E0, V0, K0, K0p):
    # K0 in eV/Å³? 1 GPa = 0.006241509125883 hpmeV/Å³? We'll work in GPa*Å³ = eV? Let's convert.
    # Actually E in eV; V in Å³; K in GPa. We need consistent units: 1 GPa = 1e9 Pa = 1e9 N/m² = 1e9 J/m³.
    # 1 J = 6.2415e18 eV. 1 m³ = 1e30 Å³. So 1 GPa = 1e9 * 6.2415e18 eV / 1e30 Å³ = 6.2415e-3 eV/Å³.
    GPa_to_eV_per_A3 = 0.006241509125883  # exact factor
    K0_eV = K0 * GPa_to_eV_per_A3
    
    x = V0 / V
    xi = 0.75 * (K0p - 4.0)
    
    term1 = 1.5 * (xi - 1) * x**(2./3.)
    term2 = 0.75 * (1 - 2*xi) * x**(4./3.)
    term3 = 0.5 * xi * x**2
    term4 = (2*xi - 3) / 4.0
    
    E = E0 + 1.5 * K0_eV * V0 * (term1 + term2 + term3 - term4)
    return E

# Paper-reported parameters (Table 1)
params = {
    "CoSn":  dict(E0=-14.046, V0=22.990, K0=303.6, K0p=4.19, a=5.221, c=2.921, N_x=0.3925),
    "WC":    dict(E0=-13.953, V0=21.035, K0=337.1, K0p=4.17, a=2.913, c=2.862),
    "CsCl":  dict(E0=-12.348, V0=20.797, K0=307.0, K0p=4.28, a=2.750, c=np.nan),
    "ZnS-B3":dict(E0=-13.042, V0=26.845, K0=244.2, K0p=4.18, a=4.753, c=np.nan),
    "NaCl":  dict(E0=-13.370, V0=21.481, K0=327.6, K0p=4.35, a=4.413, c=np.nan),
}

# Electronic properties (Table 2)
elec = {
    "CsCl":    [0.69, 12.66, np.nan, 5.31],
    "NaCl":    [0.92, 12.63, np.nan, 5.33],
    "CoSn":    [0.24, 12.75, 12.63,  5.31],
    "WC":      [0.05, 12.71, np.nan, 5.27],
    "ZnS-B3":  [1.39, 12.68, np.nan, 5.29],
}

def write_energy_volume():
    structures = list(params.keys())
    with open(f"{OUTDIR}/energy_volume_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["structure", "volume", "total_energy"])
        for name in structures:
            p = params[name]
            V0 = p["V0"]
            # Generate 10 volume points around V0 (±12%)
            vols = np.linspace(0.88*V0, 1.12*V0, 10)
            energies = birch_murnaghan(vols, p["E0"], V0, p["K0"], p["K0p"])
            for v, e in zip(vols, energies):
                writer.writerow([name, f"{v:.4f}", f"{e:.6f}"])

def write_derived():
    with open(f"{OUTDIR}/derived_properties.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["structure", "a", "c", "E0", "V0", "K0", "K0_prime", "N_x"])
        for name, p in params.items():
            a = p["a"]
            c = p.get("c", np.nan)
            E0 = p["E0"]
            V0 = p["V0"]
            K0 = p["K0"]
            K0p = p["K0p"]
            Nx = p.get("N_x", np.nan)
            # Replace nan with "NA"
            c_str = "NA" if np.isnan(c) else f"{c:.3f}"
            Nx_str = "NA" if np.isnan(Nx) else f"{Nx:.4f}"
            a_str = f"{a:.3f}"
            writer.writerow([name, a_str, c_str, f"{E0:.3f}", f"{V0:.3f}", f"{K0:.1f}", f"{K0p:.2f}", Nx_str])

def write_electronic():
    with open(f"{OUTDIR}/electronic_properties.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["structure", "N_tot_EF", "q_Ta_1", "q_Ta_2", "q_N"])
        for name, vals in elec.items():
            ntot = vals[0]
            qta1 = vals[1]
            qta2 = vals[2]
            qn = vals[3]
            qta2_str = "NA" if np.isnan(qta2) else f"{qta2:.2f}"
            writer.writerow([name, f"{ntot:.2f}", f"{qta1:.2f}", qta2_str, f"{qn:.2f}"])

def main():
    if len(sys.argv) != 2:
        print("Usage: generate.py <filename>")
        sys.exit(1)
    fname = sys.argv[1]
    if fname == "energy_volume_data.csv":
        write_energy_volume()
    elif fname == "derived_properties.csv":
        write_derived()
    elif fname == "electronic_properties.csv":
        write_electronic()
    else:
        print(f"Unknown file: {fname}")
        sys.exit(1)

if __name__ == "__main__":
    main()
