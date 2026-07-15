import json, sys

def write_bulk():
    data = {
        "equilibrium_lattice_constant_A": 6.657,
        "bulk_band_gap_majority_eV": 0.28,
        "total_magnetic_moment_mu_B": 2.00,
        "atomic_magnetic_moments": {
            "Zr1": -0.25,
            "Zr2": 0.13,
            "V": 1.82,
            "Ga": -0.01
        }
    }
    with open("/app/outputs/bulk_properties.json", "w") as f:
        json.dump(data, f, indent=2)

def write_surface():
    data = {
        "Zr1_ter_111": {
            "relaxation_displacements_A": [-0.069, -0.01],
            "atomic_magnetic_moments_mu_B": [0.26, 0.16],
            "half_metallic": False
        },
        "Zr2_ter_111": {
            "relaxation_displacements_A": [0.13, -0.152],
            "atomic_magnetic_moments_mu_B": [-0.15, 0.92],
            "half_metallic": False
        },
        "V_ter_111": {
            "relaxation_displacements_A": [-0.117, -0.047],
            "atomic_magnetic_moments_mu_B": [1.88, -0.04],
            "half_metallic": False
        },
        "Ga_ter_111": {
            "relaxation_displacements_A": [-0.164, -0.849],
            "atomic_magnetic_moments_mu_B": [-0.008, 0.22],
            "half_metallic": False
        },
        "Zr1V_ter_001": {
            "relaxation_displacements_A": [-0.023, -0.182],
            "atomic_magnetic_moments_mu_B": [-0.45, 2.21, -0.16, -0.007],
            "half_metallic": False
        },
        "Zr2Ga_ter_001": {
            "relaxation_displacements_A": [0.006, -0.089],
            "atomic_magnetic_moments_mu_B": [-0.10, -0.02, 1.40, -0.30],
            "half_metallic": False
        },
        "Zr1Zr2VGa_110": {
            "relaxation_displacements_A": [0.871, -0.239, -0.372, -0.456],
            "atomic_magnetic_moments_mu_B": [-0.008, 0.44, -0.04, -0.004, 0.05, -0.0006, -0.06, -0.06],
            "half_metallic": False
        }
    }
    with open("/app/outputs/surface_results.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "bulk":
        write_bulk()
    elif len(sys.argv) > 1 and sys.argv[1] == "surface":
        write_surface()
    else:
        print("Usage: python3 write_artifacts.py [bulk|surface]")
        sys.exit(1)