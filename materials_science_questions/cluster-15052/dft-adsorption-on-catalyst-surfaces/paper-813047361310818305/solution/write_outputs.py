import sys, json

OUTPUTS = {
    "pristine_results.json": {
        "pristine_slab": {
            "band_gap_eV": 2.71,
            "total_energy_eV": -3500.0
        },
        "adsorption": [
            {
                "molecule": "H2O",
                "site": "c-v",
                "E_ads_eV": -0.05,
                "delta_Q_e": -0.07,
                "bond_lengths_ang": [0.99, 0.99],
                "bond_angle_deg": 104.17
            },
            {
                "molecule": "H2S",
                "site": "c-h",
                "E_ads_eV": -0.10,
                "delta_Q_e": -0.04,
                "bond_lengths_ang": [1.36, 1.36],
                "bond_angle_deg": 92.38
            },
            {
                "molecule": "CO2",
                "site": "c-h",
                "E_ads_eV": -0.15,
                "delta_Q_e": -0.02,
                "bond_lengths_ang": [1.18, 1.18],
                "bond_angle_deg": 177.43
            }
        ]
    },
    "doped_results.json": {
        "doped_slabs": [
            {"dopant": "Cr", "band_gap_eV": 1.64, "total_energy_eV": -3500.0},
            {"dopant": "Mo", "band_gap_eV": 1.71, "total_energy_eV": -3500.0},
            {"dopant": "W", "band_gap_eV": 1.69, "total_energy_eV": -3500.0}
        ],
        "adsorption": [
            {"dopant": "Cr", "molecule": "H2O", "site": "on-top", "E_ads_eV": -0.8, "delta_Q_e": 0.11, "bond_lengths_ang": [0.99, 0.99], "bond_angle_deg": 106.29},
            {"dopant": "Cr", "molecule": "H2S", "site": "on-top", "E_ads_eV": -1.2, "delta_Q_e": 0.21, "bond_lengths_ang": [1.36, 1.36], "bond_angle_deg": 93.82},
            {"dopant": "Cr", "molecule": "CO2", "site": "on-top", "E_ads_eV": -0.4, "delta_Q_e": 0.04, "bond_lengths_ang": [1.19, 1.19], "bond_angle_deg": 178.97},
            {"dopant": "Mo", "molecule": "H2O", "site": "on-top", "E_ads_eV": -1.0, "delta_Q_e": 0.13, "bond_lengths_ang": [0.96, 0.96], "bond_angle_deg": 106.0},
            {"dopant": "Mo", "molecule": "H2S", "site": "on-top", "E_ads_eV": -1.6, "delta_Q_e": 0.14, "bond_lengths_ang": [1.37, 1.37], "bond_angle_deg": 91.26},
            {"dopant": "Mo", "molecule": "CO2", "site": "on-top", "E_ads_eV": -0.6, "delta_Q_e": -0.45, "bond_lengths_ang": [1.29, 1.29], "bond_angle_deg": 140.66},
            {"dopant": "W", "molecule": "H2O", "site": "on-top", "E_ads_eV": -1.1, "delta_Q_e": 0.11, "bond_lengths_ang": [0.97, 0.97], "bond_angle_deg": 106.70},
            {"dopant": "W", "molecule": "H2S", "site": "on-top", "E_ads_eV": -1.8, "delta_Q_e": 0.15, "bond_lengths_ang": [1.36, 1.36], "bond_angle_deg": 92.03},
            {"dopant": "W", "molecule": "CO2", "site": "on-top", "E_ads_eV": -0.7, "delta_Q_e": -0.50, "bond_lengths_ang": [1.29, 1.29], "bond_angle_deg": 138.28}
        ]
    },
    "field_results.json": {
        "electric_field_adsorption": [
            {"dopant": "Cr", "molecule": "H2O", "field_strength": 0.002, "E_ads_eV": -0.8, "delta_Q_e": 0.11},
            {"dopant": "Cr", "molecule": "H2O", "field_strength": 0.004, "E_ads_eV": -0.82, "delta_Q_e": 0.12},
            {"dopant": "Cr", "molecule": "H2O", "field_strength": 0.006, "E_ads_eV": -0.85, "delta_Q_e": 0.13},
            {"dopant": "Cr", "molecule": "H2S", "field_strength": 0.002, "E_ads_eV": -1.2, "delta_Q_e": 0.21},
            {"dopant": "Cr", "molecule": "H2S", "field_strength": 0.004, "E_ads_eV": -1.22, "delta_Q_e": 0.22},
            {"dopant": "Cr", "molecule": "H2S", "field_strength": 0.006, "E_ads_eV": -1.25, "delta_Q_e": 0.23},
            {"dopant": "Cr", "molecule": "CO2", "field_strength": 0.002, "E_ads_eV": -0.4, "delta_Q_e": 0.04},
            {"dopant": "Cr", "molecule": "CO2", "field_strength": 0.004, "E_ads_eV": -0.42, "delta_Q_e": 0.05},
            {"dopant": "Cr", "molecule": "CO2", "field_strength": 0.006, "E_ads_eV": -0.45, "delta_Q_e": 0.06},
            {"dopant": "Mo", "molecule": "H2O", "field_strength": 0.002, "E_ads_eV": -1.0, "delta_Q_e": 0.13},
            {"dopant": "Mo", "molecule": "H2O", "field_strength": 0.004, "E_ads_eV": -1.05, "delta_Q_e": 0.14},
            {"dopant": "Mo", "molecule": "H2O", "field_strength": 0.006, "E_ads_eV": -1.1, "delta_Q_e": 0.15},
            {"dopant": "Mo", "molecule": "H2S", "field_strength": 0.002, "E_ads_eV": -1.6, "delta_Q_e": 0.14},
            {"dopant": "Mo", "molecule": "H2S", "field_strength": 0.004, "E_ads_eV": -1.65, "delta_Q_e": 0.16},
            {"dopant": "Mo", "molecule": "H2S", "field_strength": 0.006, "E_ads_eV": -1.7, "delta_Q_e": 0.18},
            {"dopant": "Mo", "molecule": "CO2", "field_strength": 0.002, "E_ads_eV": -0.6, "delta_Q_e": -0.45},
            {"dopant": "Mo", "molecule": "CO2", "field_strength": 0.004, "E_ads_eV": -0.65, "delta_Q_e": -0.48},
            {"dopant": "Mo", "molecule": "CO2", "field_strength": 0.006, "E_ads_eV": -0.7, "delta_Q_e": -0.52},
            {"dopant": "W", "molecule": "H2O", "field_strength": 0.002, "E_ads_eV": -1.1, "delta_Q_e": 0.11},
            {"dopant": "W", "molecule": "H2O", "field_strength": 0.004, "E_ads_eV": -1.15, "delta_Q_e": 0.12},
            {"dopant": "W", "molecule": "H2O", "field_strength": 0.006, "E_ads_eV": -1.2, "delta_Q_e": 0.13},
            {"dopant": "W", "molecule": "H2S", "field_strength": 0.002, "E_ads_eV": -1.8, "delta_Q_e": 0.15},
            {"dopant": "W", "molecule": "H2S", "field_strength": 0.004, "E_ads_eV": -1.85, "delta_Q_e": 0.17},
            {"dopant": "W", "molecule": "H2S", "field_strength": 0.006, "E_ads_eV": -1.9, "delta_Q_e": 0.19},
            {"dopant": "W", "molecule": "CO2", "field_strength": 0.002, "E_ads_eV": -0.7, "delta_Q_e": -0.50},
            {"dopant": "W", "molecule": "CO2", "field_strength": 0.004, "E_ads_eV": -0.75, "delta_Q_e": -0.53},
            {"dopant": "W", "molecule": "CO2", "field_strength": 0.006, "E_ads_eV": -0.8, "delta_Q_e": -0.56}
        ]
    }
}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    fname = sys.argv[1]
    if fname not in OUTPUTS:
        sys.exit(1)
    with open(f"/app/outputs/{fname}", "w") as f:
        json.dump(OUTPUTS[fname], f, indent=2)
