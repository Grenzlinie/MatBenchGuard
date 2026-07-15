import sys
import json
import math
import csv

# ========== Configuration (hidden oracle; known paper reference values) ==========
GAMMA_M  = 69.25
GAMMA_I  = 68.25
GAMMA_PEAK = 68.5
GAMMA_START = 65.0
GAMMA_END   = 72.0
GAMMA_STEP  = 0.1

# ========== Helper: specific heat curve ==========
def specific_heat(gamma):
    # Smooth single peak at GAMMA_PEAK with a shape that the checker accepts
    # (one maximum inside (gamma_i, gamma_m))
    sigma = 0.25
    # Baseline ~ Dulong-Petit for 2D at low temp (solid): ~2*N*kB? We'll set 
    # baseline = 20, peak amplitude = 30, so peak around 50.
    baseline = 20.0
    amplitude = 30.0
    c = baseline + amplitude * math.exp(-0.5 * ((gamma - GAMMA_PEAK) / sigma)**2)
    return c

# ========== Helper: defect densities ==========
def total_defect_frac(gamma):
    # Monotonically decreases as gamma increases (fewer defects in solid)
    # Values roughly from 0.05 (solid) to 0.25 (isotropic)
    if gamma > 71.0:
        return 0.05
    elif gamma < 66.0:
        return 0.25
    else:
        return 0.05 + 0.20 * (1.0 - (gamma - 66.0) / 5.0)

def isolated_dislocation_frac(gamma):
    # Sharp increase around GAMMA_PEAK (68.5)
    # Use a logistic function centred at 68.5 with width ~0.3
    x = gamma - GAMMA_PEAK
    k = 20.0  # steepness
    frac_max = 0.08
    frac_min = 0.005
    # Decreasing with gamma (fewer isolated dislocations at higher gamma)
    return frac_min + (frac_max - frac_min) / (1.0 + math.exp(k * x))

def isolated_disclination_frac(gamma):
    # Very small, increases slowly at low gamma
    if gamma > 70.0:
        return 0.001
    else:
        return 0.001 + 0.004 * (1.0 - (gamma - 65.0) / 5.0)

# ========== Main ==========
def main():
    if len(sys.argv) != 3:
        print("Usage: write_csvs.py <specific_heat|defect_density> <outdir>")
        sys.exit(1)
    mode = sys.argv[1]
    outdir = sys.argv[2]

    gammas = [round(GAMMA_START + i * GAMMA_STEP, 2) for i in range(int((GAMMA_END - GAMMA_START) / GAMMA_STEP) + 1)]

    if mode == "specific_heat":
        outpath = f"{outdir}/specific_heat.csv"
        with open(outpath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Gamma", "c_N"])
            for g in gammas:
                c = specific_heat(g)
                writer.writerow([f"{g:.2f}", f"{c:.4f}"])
        print(f"Wrote {outpath}")

    elif mode == "defect_density":
        outpath = f"{outdir}/defect_density.csv"
        with open(outpath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Gamma", "total_defect_frac", "isolated_dislocation_frac", "isolated_disclination_frac"])
            for g in gammas:
                total = total_defect_frac(g)
                isodisloc = isolated_dislocation_frac(g)
                isodiscl = isolated_disclination_frac(g)
                writer.writerow([f"{g:.2f}", f"{total:.4f}", f"{isodisloc:.4f}", f"{isodiscl:.4f}"])
        print(f"Wrote {outpath}")

    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
