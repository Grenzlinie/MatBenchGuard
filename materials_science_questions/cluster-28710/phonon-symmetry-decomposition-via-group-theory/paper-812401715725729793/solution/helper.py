#!/usr/bin/env python3
import json, os

decompositions = {
    "rutile": {
        "decomposition": "A1g(R) + A2g(-) + B1g(R) + B2g(R) + Eg(R) + A2u(IR, E||c) + 2B1u(-) + 3Eu(IR, E⊥c)",
        "space_group": "P42/mnm"
    },
    "anatase": {
        "decomposition": "A1g(R) + 2B1g(R) + 3Eg(R) + A2u(IR, E||c) + B2u(-) + 2Eu(IR, E⊥c)",
        "space_group": "I41/amd"
    },
    "brookite": {
        "decomposition": "9Ag(R) + 9B1g(R) + 9B2g(R) + 9B3g(R) + 9Au(-) + 8B1u(IR, E||c) + 8B2u(IR, E||b) + 8B3u(IR, E||a)",
        "space_group": "Pbca"
    },
    "corundum_alpha_Ga2O3": {
        "decomposition": "2A1g(R) + 3A2g(-) + 5Eg(R) + 2A1u(-) + 2A2u(IR, E||c) + 4Eu(IR, E⊥c)",
        "space_group": "R-3c"
    },
    "beta_Ga2O3": {
        "decomposition": "20Ag(R) + 10Bg(R) + 9Au(IR, E||b) + 18Bu(IR, E⊥b)",
        "space_group": "C2/m"
    },
    "cubic_ZrO2": {
        "decomposition": "T2g(R) + T1u(IR)",
        "space_group": "Fm-3m"
    },
    "monoclinic_ZrO2": {
        "decomposition": "9Ag(R) + 9Bg(R) + 8Au(IR, E||b) + 7Bu(IR, E⊥b)",
        "space_group": "P21/c"
    },
    "Li3NbO4": {
        "decomposition": "8A1(R) + 8E(R) + 23T(IR+R)",
        "space_group": "I23"
    },
    "ilmenite_MnTiO3": {
        "decomposition": "6Ag(R) + 5Eg(R) + 4Au(IR, E||c) + 4Eu(IR, E⊥c)",
        "space_group": "R-3"
    },
    "ordered_LiAl5O8": {
        "decomposition": "6A1(R) + 8A2(-) + 14E(R) + 21T1(IR) + 20T2(R)",
        "space_group": "P4_332"
    },
    "trirutile_ZnSb2O6": {
        "decomposition": "3A1g(R) + 3A2g(-) + 3B1g(R) + 3B2g(R) + 3Eg(R) + 5A2u(IR, E||c) + 6B1u(-) + 11Eu(IR, E⊥c)",
        "space_group": "P42/mnm"
    },
    "trirutile_MgSb2O6": {
        "decomposition": "3A1g(R) + 3A2g(-) + 3B1g(R) + 3B2g(R) + 3Eg(R) + 5A2u(IR, E||c) + 6B1u(-) + 11Eu(IR, E⊥c)",
        "space_group": "P42/mnm"
    }
}

os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/factor_group_decompositions.json", "w") as f:
    json.dump(decompositions, f, indent=2)
