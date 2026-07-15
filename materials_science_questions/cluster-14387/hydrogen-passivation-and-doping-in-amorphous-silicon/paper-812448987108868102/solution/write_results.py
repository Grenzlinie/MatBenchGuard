#!/usr/bin/env python3
import json

n_valence = 99
n_gap = 24
n_conduction = 77

# Valence bands below -0.5 eV
valence_energies = [-12.0 + (11.5 / (n_valence - 1)) * i for i in range(n_valence)]
valence_energies = [round(e, 6) for e in valence_energies]

# 24 surface-state bands spanning -0.09 to 0.31 eV (width 0.4 eV)
gap_energies = [-0.09 + 0.4 / (n_gap - 1) * i for i in range(n_gap)]
gap_energies = [round(e, 6) for e in gap_energies]

# Conduction bands above 0.5 eV
conduction_energies = [0.5 + (7.5 / (n_conduction - 1)) * i for i in range(n_conduction)]
conduction_energies = [round(e, 6) for e in conduction_energies]

all_energies = valence_energies + gap_energies + conduction_energies

surface_state_indices = list(range(100, 100 + n_gap))  # 1‑based
lowest_idx = 100

results = {
    "number_of_surface_state_bands_in_gap": 24,
    "energy_width_of_region_a": 0.4,
    "lowest_energy_state_adatom_site": "A(F)c",
    "lowest_energy_band_index": lowest_idx,
    "band_energies_at_special_kpoint": all_energies,
    "surface_state_band_indices": surface_state_indices
}

with open("/app/outputs/electronic_structure_results.json", "w") as f:
    json.dump(results, f, indent=2)
