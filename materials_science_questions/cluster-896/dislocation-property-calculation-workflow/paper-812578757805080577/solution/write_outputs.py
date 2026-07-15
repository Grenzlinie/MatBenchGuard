import json, csv, sys, os

filename = sys.argv[1]

with open("/tmp/oracle_data.json") as f:
    data = json.load(f)

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)

path = os.path.join(outdir, filename)

if filename == "initial_microstructure.csv":
    cells = data["initial_microstructure"]
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["cell_id", "radius", "r1", "r2", "r3"])
        for i, c in enumerate(cells):
            w.writerow([i+1, c["radius"], c["r1"], c["r2"], c["r3"]])
elif filename == "recrystallization_kinetics.csv":
    k = data["kinetics"]
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["t", "X", "rho_rx", "mean_R_rx"])
        for i in range(len(k["t"])):
            w.writerow([k["t"][i], k["X"][i], k["rho_rx"][i], k["mean_R_rx"][i]])
elif filename == "orientation_distribution.json":
    o = data["orientation"]
    with open(path, "w") as f:
        json.dump({
            "bin_edges": o["bin_edges"],
            "all_grains_area_fraction": o["all_grains_area_fraction"],
            "recrystallized_area_fraction": o["recrystallized_area_fraction"]
        }, f)
elif filename == "boundary_moments.csv":
    b = data["boundary"]
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["t", "mean_theta", "sqrt_second_moment"])
        for i in range(len(b["t"])):
            w.writerow([b["t"][i], b["mean_theta"][i], b["sqrt_second_moment"][i]])
else:
    print("Unknown file")
    sys.exit(1)
