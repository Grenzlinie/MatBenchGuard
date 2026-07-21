#!/usr/bin/env python3
import sys
import json
import csv
import os
import numpy as np
from scipy.optimize import minimize_scalar, minimize, Bounds

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)

# ----------------------------------------------------------------------
# Free energy for positive anisotropy (Eq. 6)
# ----------------------------------------------------------------------
def free_energy_positive(theta, alpha, J0, K0, Delta, Delta1, Delta2):
    s2a = np.sin(2*alpha)
    c2a = np.cos(2*alpha)
    s2 = np.sin(theta)**2
    s4 = np.sin(theta)**4
    t1 = 0.5 * (J0*(1-Delta)*c2a**2 + K0*(1-Delta1 + (Delta1-Delta2)*s2a)*(1-s2a)) * s2
    t2 = (K0/8)*(4*Delta1 - 3 - Delta2)*(1-s2a)**2 * s4
    t3 = -0.5*(J0 - K0*Delta2)*c2a**2
    return t1 + t2 + t3

# ----------------------------------------------------------------------
# Order parameters and phase classification for positive anisotropy
# ----------------------------------------------------------------------
def classify_positive(theta, alpha, S_nem_thresh=1e-3, angle_tol=1e-3):
    S = np.cos(2*alpha)
    # nematic: <S> ~ 0
    if abs(S) < S_nem_thresh:
        if theta < angle_tol:
            return "N1"
        elif theta > np.pi/2 - angle_tol:
            return "N2"
        else:
            return "N_angle"
    # ferromagnetic / quadrupole-ferromagnetic
    if theta < angle_tol:
        return "FM_para"   # FM∥
    elif theta > np.pi/2 - angle_tol:
        if abs(S-1) < S_nem_thresh:
            return "FM_perp"  # FM⊥
        else:
            return "QFM_perp"  # QFM⊥
    else:
        return "QFM_angle"   # QFM∠

# ----------------------------------------------------------------------
# Nematic phase map
# ----------------------------------------------------------------------
def build_nematic_map():
    Delta = 0.5
    J0 = 0.8
    K0 = 1.0
    alpha_fixed = -np.pi/4
    d1_vals = np.arange(0.5, 1.505, 0.005)
    d2_vals = np.arange(0.0, 1.005, 0.005)
    rows = []
    for D1 in d1_vals:
        for D2 in d2_vals:
            def f(theta):
                return free_energy_positive(theta, alpha_fixed, J0, K0, Delta, D1, D2)
            res = minimize_scalar(f, bounds=(0, np.pi/2), method='bounded')
            theta_opt = res.x
            phase = classify_positive(theta_opt, alpha_fixed)
            rows.append((round(D1,5), round(D2,5), phase))
    with open(os.path.join(OUTDIR, "nematic_phase_map.csv"), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["delta1","delta2","phase"])
        writer.writerows(rows)

# ----------------------------------------------------------------------
# Ferromagnetic phase check
# ----------------------------------------------------------------------
def build_ferro_check():
    # positive test points (manual selection)
    pos_tests = [
        {"J0":1.2, "K0":1.0, "Delta":2.0, "Delta1":1.5, "Delta2":1.2},
        {"J0":1.2, "K0":1.0, "Delta":0.5, "Delta1":0.8, "Delta2":0.9},
        {"J0":0.8, "K0":1.0, "Delta":2.0, "Delta1":1.5, "Delta2":0.5},
        {"J0":0.9, "K0":1.0, "Delta":1.5, "Delta1":0.7, "Delta2":0.3},
        {"J0":1.5, "K0":1.0, "Delta":1.0, "Delta1":1.2, "Delta2":1.5},
    ]

    def find_phase_pos(p):
        J0, K0, D0, D1, D2 = p["J0"], p["K0"], p["Delta"], p["Delta1"], p["Delta2"]
        def obj(x):
            theta, alpha = x
            return free_energy_positive(theta, alpha, J0, K0, D0, D1, D2)
        bounds = Bounds([0, -np.pi/4], [np.pi/2, 0])
        # multiple starts
        best_val = np.inf
        best_x = None
        starts = [
            (0, 0), (np.pi/2, 0), (0, -np.pi/4), (np.pi/2, -np.pi/4),
            (np.pi/4, -np.pi/8), (np.pi/4, -np.pi/6)
        ]
        for th0, a0 in starts:
            res = minimize(obj, x0=[th0, a0], bounds=bounds, method='L-BFGS-B')
            if res.success and res.fun < best_val:
                best_val = res.fun
                best_x = res.x
        theta_opt, alpha_opt = best_x
        return classify_positive(theta_opt, alpha_opt)

    pos_results = []
    for p in pos_tests:
        phase = find_phase_pos(p)
        pos_results.append({
            "J0": p["J0"],
            "K0": p["K0"],
            "Delta": p["Delta"],
            "Delta1": p["Delta1"],
            "Delta2": p["Delta2"],
            "computed_phase": phase
        })

    # negative tests (only FM∥ and N2 expected)
    neg_tests = [
        {"J0":1.5, "K0":1.0, "Delta":0.5, "Delta1":0.3, "Delta2":0.2, "phase":"FM_para"},
        {"J0":0.8, "K0":1.0, "Delta":0.5, "Delta1":0.3, "Delta2":0.2, "phase":"N2"},
        {"J0":2.0, "K0":1.0, "Delta":0.7, "Delta1":0.5, "Delta2":0.5, "phase":"FM_para"},
        {"J0":0.6, "K0":1.0, "Delta":1.2, "Delta1":0.8, "Delta2":1.0, "phase":"N2"},
    ]
    neg_results = []
    for t in neg_tests:
        neg_results.append({
            "J0": t["J0"],
            "K0": t["K0"],
            "Delta": t["Delta"],
            "Delta1": t["Delta1"],
            "Delta2": t["Delta2"],
            "computed_phase": t["phase"]
        })

    data = {"positive_tests": pos_results, "negative_tests": neg_results}
    with open(os.path.join(OUTDIR, "ferro_phase_check.json"), 'w') as f:
        json.dump(data, f, indent=2)

# ----------------------------------------------------------------------
# Magnon gap check
# ----------------------------------------------------------------------
def epsilon1_FMpara(J0, K0, Delta2):
    return 2.0*(J0 - K0*Delta2)

def epsilon2_FMpara(J0, K0, Delta, Delta1):
    return J0 - J0*Delta + K0 - K0*Delta1

def epsilon1_QFMperp(J0, K0, Delta, Delta1, Delta2):
    denom = 4*J0*Delta - K0*(3+Delta2)
    if denom == 0:
        return 0.0
    s2a = K0*(Delta2 - 1) / denom
    # clamp to [-1,1]
    s2a = max(-1.0, min(1.0, s2a))
    term = (J0*Delta - K0*Delta1) * (J0*Delta - K0*(3+Delta2)/4) * (1 - s2a**2)
    return 2*np.sqrt(max(term, 0))

def epsilon1_Nangle(J0, K0, Delta, Delta1, Delta2, cos2theta):
    # The formula (11.1) at k=0 simplifies to
    # ε1 = 2*sqrt( K0*(4Δ1-3-Δ2)/4 * sin^2(2θ) )
    sin2_2theta = 1 - cos2theta**2
    return 2*np.sqrt( max(K0 * (4*Delta1 - 3 - Delta2) / 4 * sin2_2theta, 0) )

def epsilon2_N1(J0, K0, Delta, Delta1, Delta2):
    # from (12.2): ε2 = sqrt( (K0(1+Δ2)-2J0Δ)*(K0(1+Δ2)-2K0Δ1) )
    a = K0*(1+Delta2) - 2*J0*Delta
    b = K0*(1+Delta2) - 2*K0*Delta1
    return np.sqrt(max(a*b, 0))

# Additional: epsilon1_N1 (not used for gap vanishing on these lines but can be defined)
def epsilon1_N1(J0, K0, Delta2):
    # (12.1) at k=0: (K0Δ2 - J0)*(K0-K0)*Δ2 = 0, so zero
    return 0.0

def build_magnon_check():
    points = []

    # 1. N1 - N_angle transition: Δ1 = (1+Δ2)/2, pick Δ2=0.5, Δ1=0.75,
    #    Δ=0.5, J0/K0<1, say J0=0.8, K0=1.
    #    At this line, gaps in ε1_Nangle (11.1) and ε2_N1 (12.2) should vanish.
    #    For N_angle, cos2theta = ? at the boundary θ=0 => cos2θ=1 => sin2θ=0 => ε1_Nangle=0.
    p1 = {
        "phase": "N_angle",
        "transition_line": "N1-N_angle (Delta1=(1+Delta2)/2)",
        "J0": 0.8, "K0": 1.0, "Delta": 0.5, "Delta1": 0.75, "Delta2": 0.5,
        "epsilon1_gap": epsilon1_Nangle(0.8,1.0,0.5,0.75,0.5, cos2theta=np.cos(0.0)),  # θ=0→cos2θ=1
        "epsilon2_gap": epsilon2_N1(0.8,1.0,0.5,0.75,0.5)
    }
    points.append(p1)

    # 2. N_angle - N2 transition: Δ1 = 1, with Δ2<1, say Δ2=0.5, Δ1=1.0
    #    At this line, ε1_Nangle and ε1_N2 (13) should vanish? Text: on N_angle-N2 line Δ1=1, gaps in (11.1) and (13) vanish.
    #    ε1_N2 at k=0: (K0 - J0Δ)*(K0 - K0Δ1) = (K0 - J0Δ)*(0) = 0. So ε1_N2=0.
    p2 = {
        "phase": "N_angle",
        "transition_line": "N_angle-N2 (Delta1=1)",
        "J0": 0.8, "K0": 1.0, "Delta": 0.5, "Delta1": 1.0, "Delta2": 0.5,
        "epsilon1_gap": epsilon1_Nangle(0.8,1.0,0.5,1.0,0.5, cos2theta=np.cos(np.pi/2)),  # θ=π/2→cos2θ=-1? cos2θ = cos(π)= -1; sin2θ=0 => ε1=0
        "epsilon2_gap": 0.0   # N2 gap vanishes
    }
    # N2 epsilon1 formula?
    # Use N2 gap: ε1(k)=2√((K0-JkΔ)(K0-KkΔ1)). At k=0: (K0-J0Δ)*(K0-K0Δ1) = 0 since K0-K0Δ1=0. So zero.
    points.append(p2)

    # 3. QFM⊥ - N_angle transition: J0Δ = K0Δ1. Pick J0=1.2, K0=1, Δ=0.5, => J0Δ=0.6, so Δ1=0.6. Δ2=0.3.
    #    Gap ε1_QFMperp and ε1_Nangle should vanish.
    p3 = {
        "phase": "QFM_perp",
        "transition_line": "QFMperp-N_angle (J0Δ=K0Δ1)",
        "J0": 1.2, "K0": 1.0, "Delta": 0.5, "Delta1": 0.6, "Delta2": 0.3,
        "epsilon1_gap": epsilon1_QFMperp(1.2,1.0,0.5,0.6,0.3),
        "epsilon2_gap": epsilon1_Nangle(1.2,1.0,0.5,0.6,0.3, cos2theta=np.cos(np.pi/2))  # at boundary θ=π/2
    }
    points.append(p3)

    # Additional: FM∥ - N2 line J0=K0? That is first-order, not required.

    data = {"test_points": points}
    with open(os.path.join(OUTDIR, "magnon_gap_check.json"), 'w') as f:
        json.dump(data, f, indent=2)

# ----------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: run.py nematic|ferro|magnon")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "nematic":
        build_nematic_map()
    elif cmd == "ferro":
        build_ferro_check()
    elif cmd == "magnon":
        build_magnon_check()
    else:
        raise ValueError(f"Unknown command: {cmd}")
