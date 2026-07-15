import sys, json

# Reference values extracted from the paper:
#   Table 3(b) for bulk properties,
#   Table 4 for vacancy formation energies (potential I; II same as I),
#   Table 5 for O-vacancy displacements / saddle point / migration energy.

data = {
    "potential_I": {
        "cohesive_energy": -175.52,
        "elastic_constants": {"c11": 371, "c12": 116, "c44": 127},
        "permittivities": {"epsilon_s": 115.5, "epsilon_inf": 1.80},
        "soft_mode_frequency": 96,
        "vacancy_formation_energies": {"V_O": 20.44, "V_K": 5.76, "V_Nb": 122.83},
        "O_vacancy": {
            "displacements": {
                "Nb": 8.16,
                "O": -2.80,
                "K": 1.11
            },
            "saddle_point_displacements": {
                "O_i": 1.25,
                "Nb1": 8.10,
                "Nb2": 7.14,
                "Nb3": 1.70,
                "O1": 1.58,
                "K": 1.1
            },
            "migration_energy": 0.68
        }
    },
    "potential_II": {
        "cohesive_energy": -175.34,
        "elastic_constants": {"c11": 373, "c12": 118, "c44": 129},
        "permittivities": {"epsilon_s": 249, "epsilon_inf": 2.22},
        "soft_mode_frequency": 69,
        "vacancy_formation_energies": {"V_O": 20.44, "V_K": 5.76, "V_Nb": 122.83},
        "O_vacancy": {
            "displacements": {
                "Nb": 8.70,
                "O": -2.35,
                "K": 1.31
            },
            "saddle_point_displacements": {
                "O_i": 1.54,
                "Nb1": 8.50,
                "Nb2": 7.40,
                "Nb3": 1.06,
                "O1": 1.61,
                "K": 2.20
            },
            "migration_energy": 0.67
        }
    }
}

pot = sys.argv[1]
if pot not in data:
    sys.exit(f"Unknown potential {pot}")
print(json.dumps(data[pot], indent=2))
