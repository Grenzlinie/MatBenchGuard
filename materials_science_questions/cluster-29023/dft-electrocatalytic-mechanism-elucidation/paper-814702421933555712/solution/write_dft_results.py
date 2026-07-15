import json

data = {
    "substitution_energies": [
        {"site": "Mn(1)", "energy_kJ_mol": -331.5},
        {"site": "Mn(2)", "energy_kJ_mol": -281.4}
    ],
    "fukui_functions": [
        {"material": "K-OMS-2", "atom": "K", "f_minus": 0.024},
        {"material": "K-OMS-2", "atom": "Mn(1)", "f_minus": 0.044},
        {"material": "K-OMS-2", "atom": "Mn(2)", "f_minus": 0.026},
        {"material": "Nb(1)-K-OMS-2", "atom": "K", "f_minus": 0.024},
        {"material": "Nb(1)-K-OMS-2", "atom": "Mn(1)", "f_minus": 0.044},
        {"material": "Nb(1)-K-OMS-2", "atom": "Mn(2)", "f_minus": 0.025},
        {"material": "Nb(1)-K-OMS-2", "atom": "Nb", "f_minus": 0.044},
        {"material": "Nb(2)-K-OMS-2", "atom": "K", "f_minus": 0.010},
        {"material": "Nb(2)-K-OMS-2", "atom": "Mn(1)", "f_minus": 0.047},
        {"material": "Nb(2)-K-OMS-2", "atom": "Mn(2)", "f_minus": 0.032},
        {"material": "Nb(2)-K-OMS-2", "atom": "Nb", "f_minus": 0.086}
    ],
    "co_adsorption": [
        {"site": "Mn(1)", "bond_length_angstrom": 2.04, "adsorption_energy_kJ_mol": -88.5},
        {"site": "Mn(2)", "bond_length_angstrom": 2.00, "adsorption_energy_kJ_mol": -53.5},
        {"site": "Nb(1)", "bond_length_angstrom": 2.24, "adsorption_energy_kJ_mol": -110.1},
        {"site": "Nb(2)", "bond_length_angstrom": 2.21, "adsorption_energy_kJ_mol": -131.4}
    ]
}

with open("/app/outputs/dft_results.json", "w") as f:
    json.dump(data, f, indent=2)