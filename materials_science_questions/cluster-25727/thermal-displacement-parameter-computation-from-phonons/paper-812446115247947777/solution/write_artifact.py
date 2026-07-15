import sys, json, math, os

output_dir = sys.argv[1]
artifact = sys.argv[2]

if artifact == "mori":
    data = {
        "delta1_sq_over_wD2": 1/3,
        "delta2_sq_over_wD2": 4/15,
        "delta3_sq_over_wD2": 9/35,
        "delta4_sq_over_wD2": 16/63,
        "gamma1_over_wD": math.pi/6,
        "gamma2_over_wD": 8/(5*math.pi),
        "gamma3_over_wD": 9*math.pi/56,
        "gamma4_over_wD": 0.16*math.pi
    }
    fn = "step_01_mori_chain_params.json"
elif artifact == "laplace":
    data = {
        "Phi0_laplace_over_wD": math.pi/2,
        "Phi0_vel_laplace_over_wD": 0.0
    }
    fn = "step_02_correlation_laplace.json"

with open(os.path.join(output_dir, fn), "w") as f:
    json.dump(data, f, indent=2)
