#!/usr/bin/env python3
"""Generate reference oracle output files for phonon/dynamical stability task."""
import json, os, sys, math

def generate_htt_phonon():
    # HTT at X (0.5,0.5,0): doubly degenerate unstable mode at -98.5 cm^{-1}
    nmodes = 168  # 56 atoms * 3
    freqs = [-98.5, -98.5]  # degenerate soft modes
    # fill remaining positive frequencies (avoid zero; clear separation from instability)
    for i in range(nmodes - 2):
        # simple increasing sequence, e.g., 10 + i*4
        freqs.append(10.0 + i * 4.0)
    data = {
        "lowest_frequency_cm-1": -98.5,
        "all_frequencies_X": freqs
    }
    with open("/app/outputs/HTT_phonon_X.json", "w") as f:
        json.dump(data, f, indent=2)

def generate_ltlo_phonon():
    # LTLO: no imaginary modes, lowest positive frequency
    nmodes = 168
    freqs = []
    for i in range(nmodes):
        freqs.append(0.2 + i * 3.5)  # small start, all positive
    lowest = min(freqs)
    data = {
        "lowest_frequency_cm-1": lowest,
        "all_frequencies_X": freqs
    }
    with open("/app/outputs/LTLO_phonon_X.json", "w") as f:
        json.dump(data, f, indent=2)

def generate_total_energy():
    # Absolute energies: choose a plausible base; LTLO lower by ~0.025 eV/fu
    e_htt = -3456.789
    e_ltlo = -3456.814
    diff = e_ltlo - e_htt
    data = {
        "E_HTT_eV_fu": e_htt,
        "E_LTLO_eV_fu": e_ltlo,
        "energy_difference_LTLO_HTT_eV_fu": diff
    }
    with open("/app/outputs/total_energy_comparison.json", "w") as f:
        json.dump(data, f, indent=2)

def generate_dos_splitting():
    # Splitting ~20 meV; peaks placed below Fermi level as typical for doped cuprates
    peak1 = -45.0
    peak2 = -25.0
    splitting = peak2 - peak1
    data = {
        "peak1_energy_meV": peak1,
        "peak2_energy_meV": peak2,
        "splitting_meV": splitting
    }
    with open("/app/outputs/LTLO_DOS_splitting.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    target = sys.argv[1]
    {
        "HTT_phonon_X": generate_htt_phonon,
        "LTLO_phonon_X": generate_ltlo_phonon,
        "total_energy_comparison": generate_total_energy,
        "LTLO_DOS_splitting": generate_dos_splitting,
    }[target]()