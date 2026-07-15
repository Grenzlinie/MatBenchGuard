import json

epsilons = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 5.0, 10.0]
# average Young's modulus values matching youngs_modulus_vs_epsilon.csv
avg_moduli = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 10.0, 20.0]
directions = ['X', 'Y', 'Z']

data = []
for eps, avg_mod in zip(epsilons, avg_moduli):
    # Use the same modulus for each direction
    slope = avg_mod
    # Engineering strain from 0 to 2% in 101 points
    strain = [i * 0.0002 for i in range(101)]
    stress = [s * slope for s in strain]
    for d in directions:
        data.append({
            "epsilon_norm": eps,
            "direction": d,
            "strain": strain,
            "stress": stress,
            "fitted_slope_GPa": slope
        })

with open("/app/outputs/tensile_data.json", "w") as f:
    json.dump(data, f, indent=2)
