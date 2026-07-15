import json

bulk_data = [
  {
    "system": "Mg-Mg7H16",
    "y": 16,
    "total_energy": -1000.0,
    "a": 6.4085,
    "b": 6.4085,
    "c": 6.0562,
    "reaction_energy": 0.617,
    "zpe_correction": -0.078,
    "helmholtz_enthalpy": 0.539
  },
  {
    "system": "Mg-Mg7H15",
    "y": 15,
    "total_energy": -1000.0,
    "a": 6.4010,
    "b": 6.4010,
    "c": 6.0849,
    "reaction_energy": 0.419,
    "zpe_correction": -0.067,
    "helmholtz_enthalpy": 0.353
  },
  {
    "system": "Co-Mg7H16",
    "y": 16,
    "total_energy": -1000.0,
    "a": 6.2714,
    "b": 6.2714,
    "c": 5.9224,
    "reaction_energy": 0.417,
    "zpe_correction": -0.137,
    "helmholtz_enthalpy": 0.280
  },
  {
    "system": "Co-Mg7H15",
    "y": 15,
    "total_energy": -1000.0,
    "a": 6.1849,
    "b": 6.3834,
    "c": 5.8730,
    "reaction_energy": 0.347,
    "zpe_correction": -0.138,
    "helmholtz_enthalpy": 0.210
  },
  {
    "system": "Ni-Mg7H16",
    "y": 16,
    "total_energy": -1000.0,
    "a": 6.3161,
    "b": 6.3161,
    "c": 5.9276,
    "reaction_energy": 0.386,
    "zpe_correction": -0.097,
    "helmholtz_enthalpy": 0.289
  },
  {
    "system": "Ni-Mg7H15",
    "y": 15,
    "total_energy": -1000.0,
    "a": 6.2438,
    "b": 6.3432,
    "c": 5.9493,
    "reaction_energy": 0.362,
    "zpe_correction": -0.075,
    "helmholtz_enthalpy": 0.287
  }
]

surface_data = [
  # Mg-Mg13H28(001) layers
  {"system": "Mg-Mg13H28(001)", "layer": "L0", "rumpling": -0.323, "relaxation": -6.2, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  {"system": "Mg-Mg13H28(001)", "layer": "L1", "rumpling": 0.212, "relaxation": 3.4, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  {"system": "Mg-Mg13H28(001)", "layer": "L2", "rumpling": -0.092, "relaxation": -0.7, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  # Mg-Mg13H28(001) adsorbed
  {"system": "Mg-Mg13H28(001)", "layer": "adsorbed", "rumpling": 0.0, "relaxation": 0.0, "adsorption_energy": -1.252, "desorption_energy": 0.894, "desorption_frequency": 837.57, "relative_residence_time_percent": 100.0},

  # Co-Mg13H28(001) layers
  {"system": "Co-Mg13H28(001)", "layer": "L0", "rumpling": -0.289, "relaxation": -20.9, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  {"system": "Co-Mg13H28(001)", "layer": "L1", "rumpling": 0.140, "relaxation": 6.5, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  {"system": "Co-Mg13H28(001)", "layer": "L2", "rumpling": -0.069, "relaxation": -0.3, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  # Co-Mg13H28(001) adsorbed
  {"system": "Co-Mg13H28(001)", "layer": "adsorbed", "rumpling": 0.0, "relaxation": 0.0, "adsorption_energy": 0.336, "desorption_energy": 0.231, "desorption_frequency": 519.75, "relative_residence_time_percent": 83.04},

  # Ni-Mg13H28(001) layers
  {"system": "Ni-Mg13H28(001)", "layer": "L0", "rumpling": -0.426, "relaxation": -27.1, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  {"system": "Ni-Mg13H28(001)", "layer": "L1", "rumpling": -0.035, "relaxation": 15.2, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  {"system": "Ni-Mg13H28(001)", "layer": "L2", "rumpling": -0.086, "relaxation": -0.2, "adsorption_energy": 0.0, "desorption_energy": 0.0, "desorption_frequency": 0.0, "relative_residence_time_percent": 0.0},
  # Ni-Mg13H28(001) adsorbed
  {"system": "Ni-Mg13H28(001)", "layer": "adsorbed", "rumpling": 0.0, "relaxation": 0.0, "adsorption_energy": -0.129, "desorption_energy": 0.721, "desorption_frequency": 1016.49, "relative_residence_time_percent": 69.34}
]

with open("/app/outputs/bulk_results.json", "w") as f:
    json.dump(bulk_data, f, indent=2)

with open("/app/outputs/surface_results.json", "w") as f:
    json.dump(surface_data, f, indent=2)
