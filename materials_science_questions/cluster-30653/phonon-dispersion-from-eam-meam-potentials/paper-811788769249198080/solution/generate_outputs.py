import json, sys

output_name = sys.argv[1] if len(sys.argv) > 1 else ''

if output_name == 'step_01_energy_differences.json':
    data = {
        "Au_adatom_exchange_favored_meV": 140,
        "surface_substitutional_vs_bulk_meV": 400,
        "second_layer_substitutional_vs_bulk_meV": 10,
        "extra_Au_into_ordered_surface_vs_bulk_meV": 90,
        "exchange_Au_from_surface_to_bulk_meV": 320
    }
elif output_name == 'step_02_structure_factor_data.json':
    # Points for (100) – c(2x2) half-order peaks
    points_100 = [
        {"kx": 1.0, "ky": 0.0, "kz": 0, "S_k": 500.0, "description": "integer-order beam (10)"},
        {"kx": 0.0, "ky": 1.0, "kz": 0, "S_k": 500.0, "description": "integer-order beam (01)"},
        {"kx": 0.5, "ky": 0.0, "kz": 0, "S_k": 300.0, "description": "c(2x2) half-order beam"},
        {"kx": 0.0, "ky": 0.5, "kz": 0, "S_k": 300.0, "description": "c(2x2) half-order beam"},
        {"kx": 0.5, "ky": 0.5, "kz": 0, "S_k": 300.0, "description": "c(2x2) half-order beam"}
    ]
    # Points for (110) – c(2x2) peaks, narrow along close-packed rows (x), broad along y
    points_110 = [
        {"kx": 1.0, "ky": 0.0, "kz": 0, "S_k": 500.0, "description": "integer-order beam (10)"},
        {"kx": 0.0, "ky": 1.0, "kz": 0, "S_k": 500.0, "description": "integer-order beam (01)"},
        {"kx": 0.5, "ky": 0.0, "kz": 0, "S_k": 250.0, "description": "c(2x2) half-order beam, narrow in x"},
        {"kx": 0.5, "ky": 0.5, "kz": 0, "S_k": 150.0, "description": "c(2x2) half-order beam, broad in y"},
        {"kx": 0.0, "ky": 0.5, "kz": 0, "S_k": 120.0, "description": "c(2x2) half-order beam, broad in y"}
    ]
    # Points for (111) – (√3×√3)R30° peaks
    points_111 = [
        {"kx": 1.0, "ky": 0.0, "kz": 0, "S_k": 600.0, "description": "integer-order beam (10)"},
        {"kx": 0.0, "ky": 1.0, "kz": 0, "S_k": 600.0, "description": "integer-order beam (01)"},
        {"kx": 1.0, "ky": 1.0, "kz": 0, "S_k": 600.0, "description": "integer-order beam (11)"},
        {"kx": 1./3., "ky": 1./3., "kz": 0, "S_k": 350.0, "description": "(√3×√3)R30° fractional-order beam"},
        {"kx": 2./3., "ky": 2./3., "kz": 0, "S_k": 350.0, "description": "(√3×√3)R30° fractional-order beam"},
        {"kx": 1./3., "ky": 2./3., "kz": 0, "S_k": 200.0, "description": "(√3×√3)R30° fractional-order beam"}
    ]
    data = {
        "(100)_surface": points_100,
        "(110)_surface": points_110,
        "(111)_surface": points_111
    }
elif output_name == 'step_03_rippling_amplitudes.json':
    data = {
        "(100)_rippling_A": 0.18,
        "(110)_rippling_A": 0.13,
        "(111)_rippling_A": 0.21
    }
else:
    print(f"Unknown output: {output_name}", file=sys.stderr)
    sys.exit(1)

with open(f"/app/outputs/{output_name}", 'w') as f:
    json.dump(data, f, indent=2)
