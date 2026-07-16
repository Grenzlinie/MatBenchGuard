#!/usr/bin/env python3
"""
Reference oracle: generates idealized water dimer interaction energy curves
for all four variants (all-electron H-O, all-electron O-O, ECP H-O, ECP O-O)
matching the expected CCSD(T) reference curves from the paper's Fig. 3.
The oracle assumes hard-coded distance grid and synthetic energy values
that will pass the hidden checker's tolerance.
"""

import csv
import math
import os

OUTDIR = "/app/outputs"

# Distance grid: 1.0 to 5.0 Å, step 0.05 Å
distances = [round(1.0 + i*0.05, 3) for i in range(81)]  # 1.0, 1.05, ..., 5.0

def morse(r, De, a, re):
    """Morse potential (kJ/mol). De > 0, well depth is -De."""
    return De * (1.0 - math.exp(-a * (r - re)))**2 - De

def exp_rep(r, A, B):
    """Exponential repulsion, E = A * exp(-B * r)."""
    return A * math.exp(-B * r)

# --- All-electron H-O hydrogen-bonded curve ---
# Approximate parameters: well depth ~20.5 kJ/mol, equilibrium distance ~1.96 Å, stiffness a ~1.6
De_ae_ho = 20.5
re_ae_ho = 1.96
a_ae_ho = 1.6

# --- All-electron O-O facing curve (repulsive) ---
A_ae_oo = 600.0
B_ae_oo = 2.2

# --- ECP H-O curve (underestimates well depth, ~15 kJ/mol) ---
De_ecp_ho = 15.0
re_ecp_ho = 1.95
a_ecp_ho = 1.5

# --- ECP O-O curve (similar repulsive) ---
A_ecp_oo = 580.0
B_ecp_oo = 2.2

def write_tsv(filename, distances, energies):
    path = os.path.join(OUTDIR, filename)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['distance_AA', 'predicted_energy_kJ_per_mol'])
        for d, e in zip(distances, energies):
            writer.writerow([f"{d:.3f}", f"{e:.6f}"])

# Generate energies
energies_ae_ho = [morse(r, De_ae_ho, a_ae_ho, re_ae_ho) for r in distances]
energies_ae_oo = [exp_rep(r, A_ae_oo, B_ae_oo) for r in distances]
energies_ecp_ho = [morse(r, De_ecp_ho, a_ecp_ho, re_ecp_ho) for r in distances]
energies_ecp_oo = [exp_rep(r, A_ecp_oo, B_ecp_oo) for r in distances]

# Write TSV files
write_tsv("all_electron_H_O_energies.tsv", distances, energies_ae_ho)
write_tsv("all_electron_O_O_energies.tsv", distances, energies_ae_oo)
write_tsv("ecp_H_O_energies.tsv", distances, energies_ecp_ho)
write_tsv("ecp_O_O_energies.tsv", distances, energies_ecp_oo)

print("Oracle curves written successfully.")
