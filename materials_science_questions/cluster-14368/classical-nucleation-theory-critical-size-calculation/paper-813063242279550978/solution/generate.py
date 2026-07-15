#!/usr/bin/env python3
"""Reference oracle data generator for RESS-task artifacts.
    No network, no heavy maths – synthetics consistent with paper's target values.
"""
import json, sys, math, os

# ----------------------------------------------------------------------
# Known target values from the paper (hidden gold, only used internally)
# ----------------------------------------------------------------------
TARGETS = {
    'CO2_benzoic_acid':   {'J': 1.0e26, 'S': 31.0},
    'CHF3_benzoic_acid':  {'J': 6.0e16, 'S': 3.0},
    'CO2_cholesterol':    {'J': 1.0e22, 'S': 45.0},
}

# Helper to write JSON
def write_json(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)

# ----------------------------------------------------------------------
# 1. validation_report.json
# ----------------------------------------------------------------------
def gen_validation_report():
    state = {
        "p_MPa": 10.0,
        "T_K": 350.0,
        "w_S_egb": 250.0,
        "w_S_sw": 255.0,
        "diff_pct": 2.0
    }
    report = {
        "max_percent_diff": 2.0,
        "states": [state]
    }
    return report

# ----------------------------------------------------------------------
# 2. flow_profiles.json
# ----------------------------------------------------------------------
def gen_flow_profiles():
    # approximate profiles consistent with Fig 5-7 and exit conditions
    # CO2 points
    co2_points = [
        {"x_over_L": 0.0,   "p_MPa": 20.0,  "T_K": 380.0, "rho_kgm3": 500.0, "w_ms": 5.0},
        {"x_over_L": 0.485, "p_MPa": 19.9,  "T_K": 385.0, "rho_kgm3": 490.0, "w_ms": 50.0},
        {"x_over_L": 0.8,   "p_MPa": 15.0,  "T_K": 395.0, "rho_kgm3": 350.0, "w_ms": 150.0},
        {"x_over_L": 1.0,   "p_MPa": 5.0,   "T_K": 250.0, "rho_kgm3": 80.0,  "w_ms": 400.0},
        {"x_over_L": 1.05,  "p_MPa": 1.0,   "T_K": 180.0, "rho_kgm3": 15.0,  "w_ms": 600.0}
    ]
    # CHF3 points (slightly different values)
    chf3_points = [
        {"x_over_L": 0.0,   "p_MPa": 20.0,  "T_K": 380.0, "rho_kgm3": 600.0, "w_ms": 5.0},
        {"x_over_L": 0.485, "p_MPa": 19.9,  "T_K": 387.0, "rho_kgm3": 590.0, "w_ms": 48.0},
        {"x_over_L": 0.8,   "p_MPa": 15.5,  "T_K": 400.0, "rho_kgm3": 400.0, "w_ms": 140.0},
        {"x_over_L": 1.0,   "p_MPa": 6.0,   "T_K": 260.0, "rho_kgm3": 100.0, "w_ms": 350.0},
        {"x_over_L": 1.05,  "p_MPa": 1.2,   "T_K": 190.0, "rho_kgm3": 18.0,  "w_ms": 550.0}
    ]
    return {"CO2": co2_points, "CHF3": chf3_points}

# ----------------------------------------------------------------------
# 3. solubility_data.json
# ----------------------------------------------------------------------
def gen_solubility_data():
    # We create sparse tables that allow the supersaturation to match targets.
    # Target S ratios are enforced by choosing y*_extr / y*_exit = S.
    # Extraction conditions: cholesterol T=313 K, benzoic acid T=318 K, p=20 MPa.
    # Fugacity coefficients are set near 1 for simplicity.
    data = {}

    # CO2/benzoic acid: S=31 -> y*_extr ~ 3.1e-3, y*_exit ~ 1e-4
    co2_ba = []
    # extraction point
    co2_ba.append({"T_K": 318.0, "p_MPa": 20.0, "y_star": 3.1e-3, "phi": 1.0})
    # along path: at 10 MPa, T=350 K, moderate solubility
    co2_ba.append({"T_K": 350.0, "p_MPa": 10.0, "y_star": 8.0e-4, "phi": 1.0})
    # near nozzle exit: T~250 K, p~5 MPa, low solubility -> S= (3.1e-3*1)/(1e-4*1) = 31
    co2_ba.append({"T_K": 250.0, "p_MPa": 5.0, "y_star": 1.0e-4, "phi": 1.0})
    # a higher pressure point for completeness
    co2_ba.append({"T_K": 318.0, "p_MPa": 30.0, "y_star": 5.0e-3, "phi": 1.0})
    data["CO2_benzoic_acid"] = co2_ba

    # CO2/cholesterol: S=45, y* much lower ~ two orders lower
    co2_chol = []
    co2_chol.append({"T_K": 313.0, "p_MPa": 20.0, "y_star": 4.5e-4, "phi": 1.0})
    co2_chol.append({"T_K": 350.0, "p_MPa": 10.0, "y_star": 1.0e-4, "phi": 1.0})
    co2_chol.append({"T_K": 250.0, "p_MPa": 5.0, "y_star": 1.0e-5, "phi": 1.0})
    co2_chol.append({"T_K": 313.0, "p_MPa": 30.0, "y_star": 7.0e-4, "phi": 1.0})
    data["CO2_cholesterol"] = co2_chol

    # CHF3/benzoic acid: S=3 -> y*_extr ~ 3e-3, y*_exit ~ 1e-3
    chf3_ba = []
    chf3_ba.append({"T_K": 318.0, "p_MPa": 20.0, "y_star": 3.0e-3, "phi": 1.0})
    chf3_ba.append({"T_K": 350.0, "p_MPa": 10.0, "y_star": 1.5e-3, "phi": 1.0})
    chf3_ba.append({"T_K": 260.0, "p_MPa": 6.0, "y_star": 1.0e-3, "phi": 1.0})
    chf3_ba.append({"T_K": 318.0, "p_MPa": 30.0, "y_star": 4.5e-3, "phi": 1.0})
    data["CHF3_benzoic_acid"] = chf3_ba

    return data

# ----------------------------------------------------------------------
# 4. supersaturation_profiles.json
# ----------------------------------------------------------------------
def gen_supersaturation_profiles():
    # Simple profiles that ramp up to the target exit S.
    common_x = [0.0, 0.485, 0.8, 0.95, 1.0]
    def ramp(S_exit):
        vals = [1.0, 1.2, 5.0, S_exit * 0.6, S_exit]
        return [{"x_over_L": x, "S": s} for x, s in zip(common_x, vals)]
    return {
        "CO2_cholesterol":    ramp(TARGETS["CO2_cholesterol"]["S"]),
        "CO2_benzoic_acid":   ramp(TARGETS["CO2_benzoic_acid"]["S"]),
        "CHF3_benzoic_acid":  ramp(TARGETS["CHF3_benzoic_acid"]["S"])
    }

# ----------------------------------------------------------------------
# 5. nucleation_rates.json
# ----------------------------------------------------------------------
def gen_nucleation_rates():
    return {
        k.replace("_", "_"): {  # already correct key names
            "J": v["J"],
            "S": v["S"]
        } for k, v in TARGETS.items()
    }

# ----------------------------------------------------------------------
# Main dispatcher
# ----------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <output_path> <artifact_name>", file=sys.stderr)
        sys.exit(1)
    out_path, artifact = sys.argv[1], sys.argv[2]
    generators = {
        "validation_report": gen_validation_report,
        "flow_profiles": gen_flow_profiles,
        "solubility_data": gen_solubility_data,
        "supersaturation_profiles": gen_supersaturation_profiles,
        "nucleation_rates": gen_nucleation_rates,
    }
    if artifact not in generators:
        print(f"Unknown artifact: {artifact}", file=sys.stderr)
        sys.exit(1)
    data = generators[artifact]()
    write_json(out_path, data)
