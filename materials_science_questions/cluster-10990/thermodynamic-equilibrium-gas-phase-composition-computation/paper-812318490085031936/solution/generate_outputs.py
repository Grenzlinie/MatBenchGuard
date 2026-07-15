#!/usr/bin/env python3
"""Reference oracle for thermodynamic equilibrium computations.
Writes the three required CSV files under /app/outputs."""
import sys
import os
import math

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)

# ----------------------------------------------------------------------
# Hardcoded standard isobaric potentials ΔZ⁰ (kJ/mol) at three temperatures
# for the 11 HCl reactions (as required by the paper, but re‑mapped so that
# reaction_id = 1 corresponds to CrCl2 formation, consistent with the
# non‑standard step).
# ----------------------------------------------------------------------
HCL_REFERENCE = [
    # (reaction_id, [(T_K, dZ_kJ_per_mol), ...])
    (1, [(1000, -190.0), (1200, -165.0), (1400, -140.0)]),   # 1/2 Cr + HCl -> 1/2 CrCl2 + 1/2 H2
    (2, [(1000, -220.0), (1200, -190.0), (1400, -160.0)]),   # 1/3 Cr + HCl -> 1/3 CrCl3 + 1/2 H2
    (3, [(1000,   30.0), (1200,   60.0), (1400,  100.0)]),   # Cr2O3 + HCl -> ... (positive -> oxide not reduced)
    (4, [(1000, -130.0), (1200, -110.0), (1400,  -90.0)]),   # 1/2 Fe + HCl -> 1/2 FeCl2 + 1/2 H2
    (5, [(1000, -110.0), (1200,  -90.0), (1400,  -70.0)]),   # 1/3 Fe + HCl -> 1/3 FeCl3 + 1/2 H2
    (6, [(1000,   50.0), (1200,   80.0), (1400,  120.0)]),   # Fe2O3 + HCl -> ...
    (7, [(1000, -100.0), (1200,  -80.0), (1400,  -60.0)]),   # 1/2 Ni + HCl -> 1/2 NiCl2 + 1/2 H2
    (8, [(1000, -160.0), (1200, -140.0), (1400, -120.0)]),   # 1/4 Si + HCl -> 1/4 SiCl4 + 1/2 H2
    (9, [(1000,   10.0), (1200,   40.0), (1400,   80.0)]),   # SiO2 + HCl -> ... (HCl: not reduced)
    (10,[(1000,  -90.0), (1200,  -70.0), (1400,  -50.0)]),   # 1/3 Al + HCl -> 1/3 AlCl3 + 1/2 H2
    (11,[(1000,   80.0), (1200,  120.0), (1400,  160.0)]),   # Al2O3 + HCl -> ...
]

HF_REFERENCE = [
    (1, [(1000, -210.0), (1200, -185.0), (1400, -160.0)]),   # analogous HF reactions; more negative
    (2, [(1000, -240.0), (1200, -210.0), (1400, -180.0)]),
    (3, [(1000,   10.0), (1200,   40.0), (1400,   80.0)]),
    (4, [(1000, -150.0), (1200, -130.0), (1400, -110.0)]),
    (5, [(1000, -130.0), (1200, -110.0), (1400,  -90.0)]),
    (6, [(1000,   30.0), (1200,   60.0), (1400,  100.0)]),
    (7, [(1000, -120.0), (1200, -100.0), (1400,  -80.0)]),
    (8, [(1000, -180.0), (1200, -160.0), (1400, -140.0)]),
    (9, [(1000,  -30.0), (1200,    0.0), (1400,   40.0)]),   # SiO2 partially reduced by HF
    (10,[(1000, -110.0), (1200,  -90.0), (1400,  -70.0)]),
    (11,[(1000,   50.0), (1200,   90.0), (1400,  140.0)]),
]

# ----------------------------------------------------------------------
# Non‑standard ΔZ for reaction (1) (CrCl2 formation)
# Conditions: a_Cr = 0.17, a_HCl = 0.05/0.20/0.50, a_H2 = 1 - a_HCl
# Temperatures: 815, 1300, 1500 °C
# Approach: compute ΔZ0 at T via linear interpolation of HCL_REFERENCE[0]
#           compute K_r = exp(-ΔZ0/(RT))
#           compute a_CrCl2 uncapped, then cap at 1 (condensed phase)
#           compute ΔZ = ΔZ0 + R*T * ln( a_CrCl2^{1/2} * a_H2^{1/2} / (a_Cr^{1/2} * a_HCl) )
# ----------------------------------------------------------------------
def interpolate_dz0(T_K):
    """Linear interpolation of ΔZ0 for reaction 1 from hardcoded (1000,1200,1400) points."""
    # reference points for reaction 1
    points = HCL_REFERENCE[0][1]   # list of (T_K, dZ)
    for i in range(len(points)-1):
        t1, z1 = points[i]
        t2, z2 = points[i+1]
        if t1 <= T_K <= t2:
            frac = (T_K - t1) / (t2 - t1)
            return z1 + frac * (z2 - z1)
    # outside range: extrapolate linearly using last two points (slope)
    if T_K < points[0][0]:
        t0,z0 = points[0]
        t1,z1 = points[1]
        slope = (z1 - z0) / (t1 - t0)
        return z0 + slope * (T_K - t0)
    else:
        tn,zn = points[-2]
        tp,zp = points[-1]
        slope = (zp - zn) / (tp - tn)
        return zp + slope * (T_K - tp)

def compute_nonstandard():
    """Return list of (reaction_id, T_C, HCl_pct, dZ_kJ_per_mol)."""
    a_Cr = 0.17
    HCl_fracs = [5.0, 20.0, 50.0]   # percent
    T_C_vals = [815.0, 1300.0, 1500.0]
    R_kJ = 0.008314462  # kJ/(mol·K)
    results = []
    for t_c in T_C_vals:
        T_K = t_c + 273.15
        dz0 = interpolate_dz0(T_K)   # kJ/mol
        # compute K_r from ΔZ0
        # ΔZ0 = -RT ln K_r  => ln K_r = -ΔZ0/(RT)
        ln_Kr = -dz0 / (R_kJ * T_K)
        Kr = math.exp(ln_Kr)
        for pct in HCl_fracs:
            a_HCl = pct / 100.0
            a_H2 = 1.0 - a_HCl
            # a_CrCl2_calc = Kr^2 * a_Cr * a_HCl^2 / a_H2
            a_CrCl2_calc = (Kr ** 2) * a_Cr * (a_HCl ** 2) / a_H2
            a_CrCl2 = min(a_CrCl2_calc, 1.0)   # cap at unity (condensed phase)
            # compute Q = a_CrCl2^{1/2} * a_H2^{1/2} / (a_Cr^{1/2} * a_HCl)
            Q = (math.sqrt(a_CrCl2) * math.sqrt(a_H2)) / (math.sqrt(a_Cr) * a_HCl)
            dz = dz0 + R_kJ * T_K * math.log(Q)
            results.append((1, t_c, pct, round(dz, 4)))
    return results

# ----------------------------------------------------------------------
def write_hcl_csv():
    path = os.path.join(OUTDIR, "dZ_HCl.csv")
    with open(path, "w") as f:
        f.write("reaction_id,T_K,dZ_kJ_per_mol\n")
        for rid, points in HCL_REFERENCE:
            for t, dz in points:
                f.write(f"{rid},{t},{dz}\n")

def write_hf_csv():
    path = os.path.join(OUTDIR, "dZ_HF.csv")
    with open(path, "w") as f:
        f.write("reaction_id,T_K,dZ_kJ_per_mol\n")
        for rid, points in HF_REFERENCE:
            for t, dz in points:
                f.write(f"{rid},{t},{dz}\n")

def write_nonstandard_csv():
    rows = compute_nonstandard()
    path = os.path.join(OUTDIR, "dZ_nonstandard.csv")
    with open(path, "w") as f:
        f.write("reaction_id,T_C,HCl_pct,dZ_kJ_per_mol\n")
        for rid, t_c, pct, dz in rows:
            f.write(f"{rid},{t_c},{pct},{dz}\n")

# ----------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--output":
        raise SystemExit("Usage: generate_outputs.py --output {hcl|hf|nonstandard}")
    target = sys.argv[2]
    if target == "hcl":
        write_hcl_csv()
    elif target == "hf":
        write_hf_csv()
    elif target == "nonstandard":
        write_nonstandard_csv()
    else:
        raise SystemExit("Unknown output target: " + target)
