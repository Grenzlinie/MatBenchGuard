#!/usr/bin/env python3
import csv, json, math, os, sys

outdir = "/app/outputs"

tp_params = {"Tm0": 1250.0, "a": 28.25, "b": 0.59}
sm_params = {"Tm0": 1250.0, "a": 22.97, "b": 0.55}
pressures = list(range(0, 151, 10))  # 0,10,...,150

def compute_tm(p, params):
    return params["Tm0"] * (p / params["a"] + 1) ** params["b"]

def write_csv(filename, params):
    path = os.path.join(outdir, filename)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pressure_GPa", "melting_temperature_K"])
        for p in pressures:
            tm = round(compute_tm(p, params), 2)
            w.writerow([p, tm])

def write_json(filename):
    data = {
        "method_tp": {"Tm0": 1250.0, "a": 28.25, "b": 0.59},
        "method_sm": {"Tm0": 1250.0, "a": 22.97, "b": 0.55}
    }
    path = os.path.join(outdir, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else ""
    if target == "tp_melting_curve.csv":
        write_csv(target, tp_params)
    elif target == "sm_melting_curve.csv":
        write_csv(target, sm_params)
    elif target == "simon_fit.json":
        write_json(target)
    else:
        print("Unknown target", file=sys.stderr)
        sys.exit(1)
