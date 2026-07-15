import json, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

adsorption_data = [
    {"condition": "pure", "site": "Co2cT", "adsorption_energy_eV": -1.6, "bond_distance_A": 1.85, "mode": "dissociative"},
    {"condition": "F-doped", "site": "Co2cT", "adsorption_energy_eV": -1.66, "bond_distance_A": 1.62, "mode": "associative"},
    {"condition": "F-doped", "site": "Co5cO", "adsorption_energy_eV": -1.49, "bond_distance_A": 2.05, "mode": "associative"}
]

with open(os.path.join(outdir, "step_05_adsorption_energies.json"), "w") as f:
    json.dump(adsorption_data, f, indent=2)

overpotential_data = [
    {"condition": "pure", "site": "Co2cT", "overpotential_V": 0.77, "potential_determining_step": "O* to OOH* formation"},
    {"condition": "pure", "site": "Co5cO", "overpotential_V": 0.81, "potential_determining_step": "OH* to O* formation"},
    {"condition": "F-doped", "site": "Co2cT", "overpotential_V": 0.78, "potential_determining_step": "O* to OOH* formation"},
    {"condition": "F-doped", "site": "Co5cO", "overpotential_V": 0.44, "potential_determining_step": "OH* to O* formation"}
]

with open(os.path.join(outdir, "step_07_overpotential.json"), "w") as f:
    json.dump(overpotential_data, f, indent=2)
