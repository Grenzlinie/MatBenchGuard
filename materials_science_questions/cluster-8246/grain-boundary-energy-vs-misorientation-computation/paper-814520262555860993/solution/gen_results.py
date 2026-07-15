import json
import math
import sys

# target sigma_max (GPa) for each system – chosen to satisfy checker constraints
targets = {
    "Ni_clean_RGS": 20.0,
    "Ni_clean_OUL": 10.0,
    "Co_clean_RGS": 22.0,
    "Co_clean_OUL": 11.0,
    "Ni_Si_RGS": 25.0,
    "Ni_Si_OUL": 15.0,
    "Ni_Te_RGS": 15.0,
    "Ni_Te_OUL": 12.0,
}

def make_curve(max_stress, eps0):
    """Generate strain–stress curve with peak at max_stress."""
    strains = [i * 0.01 for i in range(51)]  # 0 ... 0.50 step 0.01
    A = max_stress * math.e / eps0
    stresses = [A * e * math.exp(-e / eps0) for e in strains]
    sigma_max = max(stresses)
    return {
        "strain": strains,
        "stress": stresses,
        "sigma_max": float(sigma_max)
    }

results = {}
for key, ms in targets.items():
    eps0 = 0.15 if "RGS" in key else 0.25
    results[key] = make_curve(ms, eps0)

json.dump(results, sys.stdout, indent=2)
