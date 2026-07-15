import sys
import csv
import json
import numpy as np

def gen_sif4_binding_curve(outpath):
    r = np.linspace(1.4, 1.8, 101)
    r = np.sort(np.concatenate([r, [1.635]]))
    k = 100.0
    E = -2000.0 + k * (r - 1.635)**2
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r_Si_F', 'total_energy'])
        for ri, ei in zip(r, E):
            w.writerow([f"{ri:.6f}", f"{ei:.6f}"])

def gen_hf2_dissociation_surface(outpath):
    r_vals = np.arange(0.8, 1.61, 0.02)
    s0 = 0.58
    E0 = -402.38
    barrier = 0.38
    K_orth = 5.0
    center_sum = 2.40
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r_FH_Fminus', 'r_Fminus_HF', 'total_energy'])
        for r1 in r_vals:
            for r2 in r_vals:
                rc = r1 - r2
                t = r1 + r2
                E = E0 + barrier * ((rc / s0)**2 - 1.0)**2 + K_orth * (t - center_sum)**2
                w.writerow([f"{r1:.4f}", f"{r2:.4f}", f"{E:.6f}"])

def desorption_potential(t, with_hplus):
    if with_hplus:
        E_initial = -1590.2
        E_ts = -1589.4
        E_final = -1591.0
        if t <= 1.0:
            E = E_initial + (E_ts - E_initial) * (3*t**2 - 2*t**3)
        else:
            t2 = t - 1.0
            E = E_ts + (E_final - E_ts) * (3*t2**2 - 2*t2**3)
    else:
        E_initial = -1586.7
        E_final = -1588.5
        E = E_initial + (E_final - E_initial) * (3*t**2 - 2*t**3)
    return E

def desorption_path(t):
    pts = np.array([[1.601, 2.685], [2.08, 2.45], [2.651, 1.635]])
    if t <= 1.0:
        return pts[0] + t * (pts[1] - pts[0])
    else:
        return pts[1] + (t - 1.0) * (pts[2] - pts[1])

def closest_path_t(point):
    ts = np.linspace(0, 2, 1001)
    path_pts = np.array([desorption_path(t) for t in ts])
    diffs = path_pts - point
    dists = np.sum(diffs**2, axis=1)
    idx = np.argmin(dists)
    return ts[idx], dists[idx]

def desorption_angle(t, with_hplus):
    if with_hplus:
        if t <= 1.0:
            angle = 109.47 - (109.47 - 95.0) * (3*t**2 - 2*t**3)
        else:
            t2 = t - 1.0
            angle = 95.0 - (95.0 - 70.53) * (3*t2**2 - 2*t2**3)
    else:
        angle = 109.47 - (109.47 - 70.53) * (3*t**2 - 2*t**3)
    return angle

def desorption_population(t, with_hplus):
    pop_max = 0.85
    if with_hplus:
        if t <= 1.0:
            pop = pop_max - (pop_max - 0.4) * (3*t**2 - 2*t**3)
        else:
            t2 = t - 1.0
            pop = 0.4 - 0.4 * (3*t2**2 - 2*t2**3)
    else:
        pop = pop_max - pop_max * (3*t**2 - 2*t**3)
    return pop

def gen_desorption_surface(outpath, with_hplus):
    rO_vals = np.linspace(1.601, 2.651, 22)
    rF_vals = np.linspace(1.635, 3.035, 29)
    k_dist = 10.0
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r_O_Si', 'r_Si_Fminus', 'total_energy', 'optimized_O_Si_F_angle', 'Si_O_bond_population'])
        for rO in rO_vals:
            for rF in rF_vals:
                point = np.array([rO, rF])
                t, dist2 = closest_path_t(point)
                E = desorption_potential(t, with_hplus) + k_dist * dist2
                angle = desorption_angle(t, with_hplus)
                pop = desorption_population(t, with_hplus)
                w.writerow([f"{rO:.6f}", f"{rF:.6f}", f"{E:.6f}", f"{angle:.6f}", f"{pop:.6f}"])

def gen_activation_energy_report(outpath):
    report = {
        "sif4_equilibrium_bond_length": 1.635,
        "hf2_dissociation_barrier": 0.38,
        "hf2_saddle_r": 1.20,
        "siF4_desorption_activation_energy": 0.80,
        "transition_state_r_O_Si": 2.08,
        "transition_state_r_Si_Fminus": 2.45,
        "angle_range": [70.53, 109.47],
        "bond_population_range": [0.0, 0.85]
    }
    with open(outpath, 'w') as f:
        json.dump(report, f, indent=2)

def gen_angle_population_trend(outpath):
    ts = np.linspace(0, 2, 50)
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['case', 'reaction_coordinate_rc', 'optimized_O_Si_F_angle', 'Si_O_bond_population'])
        for case, flag in [('with_Hplus', True), ('without_Hplus', False)]:
            rows = []
            for t in ts:
                rO, rF = desorption_path(t)
                rc = rO - rF
                angle = desorption_angle(t, flag)
                pop = desorption_population(t, flag)
                rows.append([rc, angle, pop])
            rows.sort(key=lambda x: x[0])
            for rc, angle, pop in rows:
                w.writerow([case, f"{rc:.6f}", f"{angle:.6f}", f"{pop:.6f}"])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate.py <function> <outpath>")
        sys.exit(1)
    func_name = sys.argv[1]
    outpath = sys.argv[2]
    if func_name == "sif4_binding_curve":
        gen_sif4_binding_curve(outpath)
    elif func_name == "hf2_dissociation_surface":
        gen_hf2_dissociation_surface(outpath)
    elif func_name == "desorption_surface_without_hplus":
        gen_desorption_surface(outpath, False)
    elif func_name == "desorption_surface_with_hplus":
        gen_desorption_surface(outpath, True)
    elif func_name == "activation_energy_report":
        gen_activation_energy_report(outpath)
    elif func_name == "angle_population_trend":
        gen_angle_population_trend(outpath)
    else:
        print("Unknown function:", func_name)
        sys.exit(1)