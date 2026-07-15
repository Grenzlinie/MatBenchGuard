import json
import sys

bulk = {
    "CY-EAM": {
        "lattice_constant_A": 3.92,
        "cohesive_energy_eV": 5.72,
        "vacancy_formation_energy_eV": 1.49,
        "C11_GPa": 309,
        "C12_GPa": 259,
        "C44_GPa": 79.3
    },
    "CY-XEAM2": {
        "lattice_constant_A": 3.92,
        "cohesive_energy_eV": 5.77,
        "vacancy_formation_energy_eV": 1.51,
        "C11_GPa": 319,
        "C12_GPa": 266,
        "C44_GPa": 77.5
    }
}

cluster = {
    "CY-EAM": {
        "dimer": {"bond_length_A": 2.31, "binding_energy_eV_per_atom": 3.94},
        "trimer": {"bond_length_A": 2.46, "binding_energy_eV_per_atom": 4.14},
        "tetrahedron": {"bond_length_A": 2.51, "binding_energy_eV_per_atom": 4.31}
    },
    "CY-XEAM2": {
        "dimer": {"bond_length_A": 2.32, "binding_energy_eV_per_atom": 1.95},
        "trimer": {"bond_length_A": 2.45, "binding_energy_eV_per_atom": 2.70},
        "tetrahedron": {"bond_length_A": 2.53, "binding_energy_eV_per_atom": 3.04}
    }
}

surface = {
    "CY-EAM": {
        "surface_energy_111_eV_per_A2": 0.070,
        "surface_energy_100_eV_per_A2": 0.077,
        "adatom_diffusion_barrier_eV": 0.096
    },
    "CY-XEAM2": {
        "surface_energy_111_eV_per_A2": 0.092,
        "surface_energy_100_eV_per_A2": 0.111,
        "adatom_diffusion_barrier_eV": 0.38
    }
}

mapping = {
    "bulk": bulk,
    "cluster": cluster,
    "surface": surface
}

artifact = sys.argv[1]
data = mapping[artifact]
with open(f"/app/outputs/{artifact}_properties.json", "w") as f:
    json.dump(data, f, indent=2)
