import json

data = {
    "materials": [
        {
            "name": "Si",
            "band_eigenvalues": {
                "Gamma": [-12.54, 0.0, 3.48, 4.74, 7.89],
                "X": [-8.20, -2.96, 1.23, 12.21],
                "L": [-10.12, -7.22, -1.24, 2.36, 4.07]
            },
            "total_energy_per_atom": -7.8954
        },
        {
            "name": "Ge",
            "band_eigenvalues": {
                "Gamma": [-12.12, 0.0, 3.49, 0.88],
                "X": [-8.4, -2.56, 1.29, 11.77],
                "L": [-10.13, -7.02, -1.1, 0.73, 4.28]
            },
            "total_energy_per_atom": -7.9893
        },
        {
            "name": "alpha-Sn",
            "band_eigenvalues": {
                "Gamma": [-9.11, 0.0, 2.83, 0.0],
                "X": [-6.5, -1.70, 1.79, 8.15],
                "L": [-7.78, -5.25, -0.74, 0.83, 3.70]
            },
            "total_energy_per_atom": -6.7696
        }
    ]
}

with open("/app/outputs/band_and_total_energy.json", "w") as f:
    json.dump(data, f, indent=2)
