import json, sys

# All model parameters from Table 2, units J/mol, J/(mol·K)
data = {
    "phases": {
        "Liquid": {
            "model": "MQM",
            "coordination_numbers": {
                "Z_FeFe_Fe": 6,
                "Z_AlAl_Al": 6,
                "Z_PP_P": 6,
                "Z_PFe_P": 6,
                "Z_PAl_P": 6,
                "Z_FeAl_Fe": 6,
                "Z_AlFe_Al": 6,
                "Z_AlP_Al": 6,
                "Z_FeP_Fe": 3
            },
            "binary_energies": {
                "FeP": {
                    "terms": [
                        {"X_FeFe": 0, "X_PP": 0, "A": -56902.0, "B": 6.569},
                        {"X_FeFe": 1, "X_PP": 0, "A": 5481.0, "B": 3.033},
                        {"X_FeFe": 2, "X_PP": 0, "A": -11966.0, "B": 2.51},
                        {"X_FeFe": 0, "X_PP": 1, "A": -9623.0, "B": 0.0}
                    ]
                },
                "AlP": {
                    "terms": [
                        {"X_AlAl": 0, "X_PP": 0, "A": -21443.0, "B": 6.9036}
                    ]
                },
                "FeAl": {
                    "terms": [
                        {"X_FeFe": 0, "X_AlAl": 0, "A": -20292.0, "B": 3.347},
                        {"X_FeFe": 1, "X_AlAl": 0, "A": -1674.0, "B": -1.255},
                        {"X_FeFe": 2, "X_AlAl": 0, "A": -1046.0, "B": 0.0},
                        {"X_FeFe": 0, "X_AlAl": 1, "A": -10460.0, "B": 4.184}
                    ]
                }
            },
            "ternary_terms": {
                "g_FeP_Al_101": {"A": -20920.0, "B": 5.6484},
                "g_FeP_Al_011": {"A": -104600.0, "B": 0.0}
            },
            "interpolation": "Toop with Al as asymmetric component"
        },
        "FCC_A1": {
            "model": "CEF",
            "sublattice_sites": [1, 1],
            "endmembers": {
                "Fe:Va": "G_Fe_FCC",
                "Al:Va": "G_Al_FCC",
                "P:Va": "G_P_FCC"
            },
            "interactions": [
                {
                    "elements": ["Fe", "P"],
                    "Va": 1,
                    "L0": {"A": -139787.44, "B": 6.4852}
                },
                {
                    "elements": ["Al", "P"],
                    "Va": 1,
                    "L0": {"A": -18828.0, "B": 0.0}
                },
                {
                    "elements": ["Fe", "Al"],
                    "Va": 1,
                    "L0": {"A": -105855.0, "B": 30.65},
                    "L1_redlich": {"A": -29017.0, "B": -4.91},
                    "L2_redlich": {"A": 32200.0, "B": -17.0}
                }
            ],
            "magnetic": {
                "Tc": {"Fe:Va": -201.0},
                "beta": {"Fe:Va": -2.1}
            }
        },
        "BCC_A2": {
            "model": "CEF",
            "sublattice_sites": [1, 3],
            "endmembers": {
                "Fe:Va": "G_Fe_BCC",
                "Al:Va": "G_Al_BCC",
                "P:Va": "G_P_BCC"
            },
            "interactions": [
                {
                    "elements": ["Fe", "P"],
                    "Va": 1,
                    "L0": {"A": -203476.3, "B": 15.4808},
                    "L1_redlich": {"A": 33472.0, "B": 0.0}
                },
                {
                    "elements": ["Al", "P"],
                    "Va": 1,
                    "L0": {"A": -6276.0, "B": 0.0}
                },
                {
                    "elements": ["Fe", "Al"],
                    "Va": 1,
                    "L0": {"A": -123044.0, "B": 31.99},
                    "L1_redlich": {"A": -2945.0, "B": 0.0},
                    "L2_redlich": {"A": -3347.0, "B": 0.0}
                }
            ],
            "magnetic": {
                "Tc": {"Fe:Va": 1043.0, "Fe,P:Va": -285.0, "Fe,Al:Va": -438.0},
                "beta": {"Fe:Va": 2.22}
            }
        },
        "BCC_B2": {
            "model": "ordered_CEF",
            "sublattice_sites": [0.5, 0.5, 3],
            "endmembers": {
                "Fe:Al:Va": -14462.0 - 3.973,
                "Al:Fe:Va": -14462.0 - 3.973,
                "Fe:Fe:Va": 0.0,
                "Al:Al:Va": 0.0,
                "P:P:Va": 0.0,
                "Fe:P:Va": 0.0,
                "Al:P:Va": 0.0,
                "P:Fe:Va": 0.0,
                "P:Al:Va": 0.0
            },
            "interactions": [
                {
                    "type": "L_Fe,Al:Al",
                    "L0": {"A": 1665.37, "B": -4.0},
                    "L1": {"A": 524.0, "B": 0.0},
                    "L2": {"A": -1560.0, "B": 0.0}
                },
                {
                    "type": "L_Al:Fe,Al",
                    "L0": {"A": 1665.37, "B": -4.0},
                    "L1": {"A": 524.0, "B": 0.0},
                    "L2": {"A": -1560.0, "B": 0.0}
                },
                {
                    "type": "L_Fe,Al:Fe",
                    "L0": {"A": -5346.0, "B": -1.6},
                    "L1": {"A": 524.0, "B": 0.0},
                    "L2": {"A": -1560.0, "B": 0.0}
                },
                {
                    "type": "L_Fe:Fe,Al",
                    "L0": {"A": -5346.0, "B": -1.6},
                    "L1": {"A": 524.0, "B": 0.0},
                    "L2": {"A": -1560.0, "B": 0.0}
                },
                {
                    "type": "L_Fe,Al:Fe,Al",
                    "L0": {"A": -16800.0, "B": -3.6}
                }
            ],
            "magnetic": {
                "Tc": {"Fe:Al:Va": -250.0, "Al:Fe:Va": -250.0, "Fe,Al:Al:Va": -250.0, "Fe,Al:Fe:Va": -250.0, "Fe:Fe,Al:Va": -250.0, "Al:Fe,Al:Va": -250.0},
                "beta": {"Fe:Al:Va": -2.72, "Al:Fe:Va": -2.72, "Fe,Al:Al:Va": -0.6, "Fe,Al:Fe:Va": -0.6, "Fe:Fe,Al:Va": -0.6, "Al:Fe,Al:Va": -0.6}
            }
        },
        "Al8Fe5": {
            "model": "CEF",
            "sublattice_sites": [8, 5],
            "endmembers": {
                "Al:Al": "13*G_Al_BCC",
                "Fe:Fe": "13*G_Fe_BCC + 13000",
                "Al:Fe": "8*G_Al_BCC + 5*G_Fe_BCC - 384500 + 30*T",
                "Fe:Al": "8*G_Fe_BCC + 5*G_Al_BCC + 200000 + 30*T"
            },
            "interactions": [
                {"elements": ["Al"], "L_Al:Al,Fe": {"A": -133888.0, "B": 0.0}},
                {"elements": ["Fe"], "L_Al,Fe:Fe": {"A": -174000.0, "B": 0.0}}
            ]
        },
        "Al13Fe4": {
            "model": "CEF",
            "sublattice_sites": [32, 12, 7],
            "endmembers": {
                "Al:Fe:Al": "39*G_Al_FCC + 12*G_Fe_BCC - 1564680 + 377*T",
                "Al:Fe:Va": "32*G_Al_FCC + 12*G_Fe_BCC - 1433100 + 377*T"
            }
        },
        "Me3P": {
            "model": "CEF",
            "sublattice_sites": [3, 1],
            "endmembers": {
                "Fe:P": "G_Fe3P_ref",
                "Al:P": "3*G_Al_FCC + G_P_White - 14830 + 85*T"
            },
            "interactions": [
                {"elements": ["Fe", "Al"], "L_Fe,Al:P": {"A": -346025.0, "B": 50.0}}
            ]
        },
        "Me2P": {
            "model": "CEF",
            "sublattice_sites": [2, 1],
            "endmembers": {
                "Fe:P": "G_Fe2P_ref",
                "Al:P": "2*G_Al_FCC + G_P_White + 50000"
            },
            "interactions": [
                {"elements": ["Fe", "Al"], "L_Fe,Al:P": {"A": -175728.0, "B": 0.0}}
            ]
        },
        "Stoichiometric": {
            "FeP": {
                "delta_H": -126100.0,
                "S": 47.77,
                "Cp": {
                    "a": 43.7878,
                    "b": 0.01985,
                    "c": -232000.0
                }
            },
            "FeP2": {
                "delta_H": -191100.0,
                "S": 51.05,
                "Cp": {
                    "a": 77.52563,
                    "b": 0.009348,
                    "c": -443846.0,
                    "d": -1.1e-06
                }
            },
            "AlP": {
                "delta_H": -163000.0,
                "S": 40.34,
                "Cp": {
                    "a": 48.53,
                    "b": 0.00457,
                    "c": -690000.0
                }
            },
            "Al2Fe": {
                "G0": "2*G_Al_FCC + G_Fe_BCC - 94850 + 13.42*T"
            },
            "Al5Fe2": {
                "G0": "5*G_Al_FCC + 2*G_Fe_BCC - 217301 + 34.83*T"
            }
        }
    }
}

with open(sys.argv[1], 'w') as f:
    json.dump(data, f, indent=2)
