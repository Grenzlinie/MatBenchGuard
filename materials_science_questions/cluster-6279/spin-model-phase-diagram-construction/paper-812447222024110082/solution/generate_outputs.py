import csv, json, sys

OUTDIR = "/app/outputs"

p = 7
alpha_A = 4.8
T_A = 2.78
alpha_B = 5.0
T_B = 2.64

def write_triple_points():
    data = {
        "p": p,
        "alpha_A": alpha_A,
        "T_A": T_A,
        "alpha_B": alpha_B,
        "T_B": T_B
    }
    with open(f"{OUTDIR}/triple_points.json", "w") as f:
        json.dump(data, f, indent=2)

def write_boundary():
    alphas = [round(i*0.1, 1) for i in range(0, 101)]
    with open(f"{OUTDIR}/phase_boundary.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["alpha", "temperature", "transition_type"])
        for a in alphas:
            if a < alpha_A - 1e-9:
                # KT line
                t_kt = 3.0 - (3.0 - T_A) * (a / alpha_A)
                writer.writerow([a, round(t_kt, 4), "KT"])
                # dipolar line
                t_dip = 2.0 + (T_A - 2.0) * (a / alpha_A)
                writer.writerow([a, round(t_dip, 4), "dipolar"])
            elif a > alpha_B + 1e-9:
                # KT line
                t_kt = T_B + (4.0 - T_B) * ((a - alpha_B) / (10.0 - alpha_B))
                writer.writerow([a, round(t_kt, 4), "KT"])
                # dipolar line
                t_dip = T_B + (3.5 - T_B) * ((a - alpha_B) / (10.0 - alpha_B))
                writer.writerow([a, round(t_dip, 4), "dipolar"])
            else:
                # only dipolar transition between alpha_A and alpha_B
                t_dip = T_A - (T_A - T_B) * ((a - alpha_A) / (alpha_B - alpha_A))
                writer.writerow([a, round(t_dip, 4), "dipolar"])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "triple":
        write_triple_points()
    elif len(sys.argv) > 1 and sys.argv[1] == "boundary":
        write_boundary()
    else:
        write_triple_points()
        write_boundary()
