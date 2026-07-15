#!/usr/bin/env python3
"""Oracle writer for /app/outputs/results.json. Produces the paper-reported
CO2RR limiting potentials, product identities, and plausible reaction
free-energy profiles for the five MOF catalysts."""

import json

output = {
    "Cu3HIB2": {
        "product": "HCOOH",
        "limiting_potential": -0.03,
        "rate_limiting_step": "CO2 + H+ + e- -> *HCOO",
        "delta_G_steps": [
            {"step": "HER: * + H+ + e- -> *H", "DG": 0.20},
            {"step": "CO2 + H+ + e- -> *HCOO", "DG": 0.03},
            {"step": "*HCOO + H+ + e- -> *HCOOH", "DG": -0.10},
            {"step": "*HCOOH -> HCOOH + *", "DG": -0.05}
        ]
    },
    "Cu3HITP2": {
        "product": "HCOOH",
        "limiting_potential": -0.03,
        "rate_limiting_step": "CO2 + H+ + e- -> *HCOO",
        "delta_G_steps": [
            {"step": "HER: * + H+ + e- -> *H", "DG": 0.18},
            {"step": "CO2 + H+ + e- -> *HCOO", "DG": 0.03},
            {"step": "*HCOO + H+ + e- -> *HCOOH", "DG": -0.08},
            {"step": "*HCOOH -> HCOOH + *", "DG": -0.04}
        ]
    },
    "Ni3HHB": {
        "product": "CH2O",
        "limiting_potential": -0.62,
        "rate_limiting_step": "CO2 + H+ + e- -> *HCOO",
        "delta_G_steps": [
            {"step": "HER: * + H+ + e- -> *H", "DG": 0.70},
            {"step": "CO2 + H+ + e- -> *HCOO", "DG": 0.62},
            {"step": "*HCOO + H+ + e- -> *HCOOH", "DG": -0.30},
            {"step": "*HCOOH + H+ + e- -> *CHO", "DG": -0.20},
            {"step": "*CHO + H+ + e- -> CH2O + *", "DG": -0.10}
        ]
    },
    "Co3HIB": {
        "product": "CH4",
        "limiting_potential": -0.24,
        "rate_limiting_step": "*CHO + H+ + e- -> *CHOH",
        "delta_G_steps": [
            {"step": "HER: * + H+ + e- -> *H", "DG": 0.30},
            {"step": "CO2 + H+ + e- -> *COOH", "DG": 0.10},
            {"step": "*COOH + H+ + e- -> *CO + H2O", "DG": -0.20},
            {"step": "*CO + H+ + e- -> *CHO", "DG": 0.05},
            {"step": "*CHO + H+ + e- -> *CHOH", "DG": 0.24},
            {"step": "*CHOH + H+ + e- -> *CH2OH", "DG": -0.15},
            {"step": "*CH2OH + H+ + e- -> *CH3OH", "DG": -0.10},
            {"step": "*CH3OH + H+ + e- -> *CH3 + H2O", "DG": -0.12},
            {"step": "*CH3 + H+ + e- -> CH4 + *", "DG": -0.08}
        ]
    },
    "Cr3HTB": {
        "product": "CH4",
        "limiting_potential": -0.29,
        "rate_limiting_step": "*HCOO + H+ + e- -> *HCOOH",
        "delta_G_steps": [
            {"step": "HER: * + H+ + e- -> *H", "DG": 0.35},
            {"step": "CO2 + H+ + e- -> *HCOO", "DG": 0.15},
            {"step": "*HCOO + H+ + e- -> *HCOOH", "DG": 0.29},
            {"step": "*HCOOH + H+ + e- -> *CHO", "DG": -0.10},
            {"step": "*CHO + H+ + e- -> *CH2O", "DG": -0.12},
            {"step": "*CH2O + H+ + e- -> *CH3O", "DG": -0.08},
            {"step": "*CH3O + H+ + e- -> *O + CH4", "DG": -0.05},
            {"step": "*O + H+ + e- -> *OH", "DG": -0.10},
            {"step": "*OH + H+ + e- -> H2O + *", "DG": -0.15}
        ]
    },
    "summary": [
        {"MOF": "Cu3HIB2", "product": "HCOOH", "U_L": -0.03},
        {"MOF": "Cu3HITP2", "product": "HCOOH", "U_L": -0.03},
        {"MOF": "Ni3HHB", "product": "CH2O", "U_L": -0.62},
        {"MOF": "Co3HIB", "product": "CH4", "U_L": -0.24},
        {"MOF": "Cr3HTB", "product": "CH4", "U_L": -0.29}
    ]
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(output, f, indent=2)
