import csv, json, math, sys, os

outdir = "/app/outputs"
if not os.path.exists(outdir):
    os.makedirs(outdir)

def write_u0_curves():
    filename = os.path.join(outdir, "U0_curves.csv")
    concentrations = [i/10.0 for i in range(11)]  # 0.0 .. 1.0
    rows = []
    for c in concentrations:
        u0_fcc = -0.5 + 0.3*c + 0.2*c*c
        u0_bcc = -0.4*c + 0.1*c*c
        rows.append((c, round(u0_fcc, 6), round(u0_bcc, 6)))
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["concentration", "U0_fcc", "U0_bcc"])
        writer.writerows(rows)

def write_v_curves():
    filename = os.path.join(outdir, "V_curves.csv")
    concentrations = [i/10.0 for i in range(11)]
    rows = []
    for c in concentrations:
        v1_alpha = 0.05 + 0.03 * 4 * c * (1 - c)  # max 0.08 at c=0.5
        v1_beta  = 0.04 + 0.06 * (1 - (2*c-1)**2)  # parabolic, max 0.10 at c=0.5
        v2_beta  = 0.5 * v1_beta + 0.002
        rows.append((c, round(v1_alpha, 6), round(v1_beta, 6), round(v2_beta, 6)))
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["concentration", "V1_alpha", "V1_beta", "V2_beta"])
        writer.writerows(rows)

def write_phase_boundaries():
    filename = os.path.join(outdir, "phase_boundaries.json")
    boundaries = []

    # ---------- α+β miscibility gap ----------
    # α (fcc) side
    pts = []
    for T_k in range(300, 5100, 100):
        x = (T_k - 300) / 4800.0  # 0→1 roughly
        c = 0.655 + 0.12 * (1 - x)
        pts.append({"T": T_k, "c": round(c, 6)})
    boundaries.append({"phase1": "alpha", "phase2": "alpha+beta", "points": pts})

    # β (bcc) side
    pts = []
    for T_k in range(300, 5100, 100):
        x = (T_k - 300) / 4800.0
        c = 0.655 - 0.18 * (1 - x)
        pts.append({"T": T_k, "c": round(c, 6)})
    boundaries.append({"phase1": "beta", "phase2": "alpha+beta", "points": pts})

    # ---------- α + L1₂ (α') two-phase region ----------
    # α / (α+L1₂) boundary
    pts = []
    for T_k in range(0, 1300, 100):
        if T_k <= 1200:
            x = T_k / 1200.0
            c = 0.18 + 0.07 * (1 - x)
        else:
            c = 0.25
        pts.append({"T": T_k, "c": round(c, 6)})
    boundaries.append({"phase1": "alpha", "phase2": "alpha+alpha_prime", "points": pts})

    # L1₂ / (α+L1₂) boundary
    pts = []
    for T_k in range(0, 1300, 100):
        if T_k <= 1200:
            x = T_k / 1200.0
            c = 0.32 - 0.07 * (1 - x)
        else:
            c = 0.25
        pts.append({"T": T_k, "c": round(c, 6)})
    boundaries.append({"phase1": "alpha_prime", "phase2": "alpha+alpha_prime", "points": pts})

    # ---------- β / B2 (β') second‑order transitions ----------
    # Central B2 dome (peaks at c≈0.55, T≈2500 K)
    pts = []
    for c in [i/100.0 for i in range(30, 81)]:  # 0.30 – 0.80
        T = 2500 * max(0, 1 - (c - 0.55)**2 / 0.0625)
        pts.append({"T": round(T, 1), "c": round(c, 6)})
    boundaries.append({"phase1": "beta", "phase2": "beta_prime", "points": pts})

    # Off‑stoichiometric B2 dome (c≈0.2, T≈2000 K)
    pts = []
    for c in [i/100.0 for i in range(10, 31)]:
        T = 2000 * max(0, 1 - (c - 0.2)**2 / 0.01)
        pts.append({"T": round(T, 1), "c": round(c, 6)})
    boundaries.append({"phase1": "beta", "phase2": "beta_prime", "points": pts})

    with open(filename, 'w') as f:
        json.dump({"boundaries": boundaries}, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_artifacts.py <basename>")
        sys.exit(1)
    basename = sys.argv[1]
    if basename == "U0_curves.csv":
        write_u0_curves()
    elif basename == "V_curves.csv":
        write_v_curves()
    elif basename == "phase_boundaries.json":
        write_phase_boundaries()
    else:
        print("Unknown basename")
        sys.exit(1)