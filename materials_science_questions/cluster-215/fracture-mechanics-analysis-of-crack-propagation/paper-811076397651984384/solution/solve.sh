#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

cat > /tmp/gen.py << 'GENEOF'
import csv, json, math, sys, os

# ---- read critical length curve fixture ----
def load_critical_curve(path):
    kk, ll = [], []
    with open(path) as f:
        r = csv.DictReader(f)
        for row in r:
            kk.append(float(row['KI']))
            ll.append(float(row['critical_length']))
    # sort
    pairs = sorted(zip(kk, ll))
    return [p[0] for p in pairs], [p[1] for p in pairs]

def interp(x, xs, ys):
    # linear interpolation
    if x <= xs[0]: return ys[0]
    if x >= xs[-1]: return ys[-1]
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            t = (x - xs[i])/(xs[i+1]-xs[i])
            return ys[i] + t*(ys[i+1]-ys[i])
    return ys[-1]

# ---- desired velocity curve (stage I/II) ----
v_KI_points = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 10.0, 11.0, 12.0, 14.0]
v_v_values   = [1.e-9,2.e-9,5.e-9,1.e-8,1.2e-8,1.3e-8,1.4e-8,1.5e-8,1.5e-8,1.5e-8,1.5e-8]

def velocity(KI):
    return interp(KI, v_KI_points, v_v_values)

# ---- main ----
def generate(target):
    # load critical length
    ki_crit, l_crit = load_critical_curve('/solution/critical_length.csv')
    
    # KI range for growth curves and velocity table
    KI_min, KI_max, dKI = 6.0, 14.0, 0.5
    ki_vals = [round(KI_min + i*dKI, 2) for i in range(int((KI_max-KI_min)/dKI)+1)]
    
    if target == 'hydride_growth_curves.csv':
        with open(os.path.join(os.environ['OUTDIR'], 'hydride_growth_curves.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['KI','time_label','hydride_length'])
            for KI in ki_vals:
                L_crit_val = interp(KI, ki_crit, l_crit)  # um
                v = velocity(KI)  # m/s
                # fracture time in hours
                t_frac_hr = L_crit_val * 1e-6 / (v * 3600)  # hours
                # maximum hydride length (saturation)
                L_max = L_crit_val + 10.0  # um
                if L_max <= L_crit_val:
                    L_max = L_crit_val + 0.1
                # logistic growth parameter
                ratio = L_crit_val / L_max
                if ratio >= 1.0:
                    k = 0.0
                else:
                    k = -math.log(1.0 - ratio) / t_frac_hr
                # generate point labels
                time_hrs = [0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0]
                # add the fracture time rounded to 0.01 h
                tf_rounded = round(t_frac_hr, 2)
                if tf_rounded not in time_hrs:
                    time_hrs.append(tf_rounded)
                time_hrs.sort()
                for th in time_hrs:
                    if k <= 0:
                        l = L_max if th >= t_frac_hr else 0.0
                    else:
                        l = L_max * (1.0 - math.exp(-k * th))
                    # clamp at zero
                    if l < 0: l = 0.0
                    lbl = f"{th:.2f}h" if '.' in str(th) else f"{th:.1f}h"
                    # simplify label
                    if th == int(th): lbl = f"{int(th)}h"
                    else:
                        # keep one decimal if non-integer
                        lbl = f"{th:.1f}h"
                        if th == round(th,1) == round(th,2):
                            lbl = f"{th:.1f}h"
                        else:
                            lbl = f"{th:.2f}h"
                    # ensure unique
                    w.writerow([KI, lbl, round(l, 3)])
    
    elif target == 'dhc_velocity_vs_KI.csv':
        with open(os.path.join(os.environ['OUTDIR'], 'dhc_velocity_vs_KI.csv'), 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['KI','velocity'])
            for KI in ki_vals:
                v = velocity(KI)
                w.writerow([KI, v])
    
    elif target == 'transition_analysis.json':
        # find stage I/II transition from velocity curve
        # compute slope on log scale, pick KI where slope change is greatest
        import itertools
        kiv, vv = zip(*[(kv, velocity(kv)) for kv in ki_vals])
        slopes = []
        for i in range(1, len(kiv)):
            dlogv = (math.log10(vv[i]) - math.log10(vv[i-1])) / (kiv[i] - kiv[i-1])
            slopes.append(dlogv)
        # find max change in slope (second difference)
        max_change = -1e9
        trans_ki_idx = 0
        for i in range(1, len(slopes)):
            change = abs(slopes[i] - slopes[i-1])
            if change > max_change:
                max_change = change
                trans_ki_idx = i  # index of point after transition
        # transition KI is the midpoint of the interval with largest slope change
        trans_ki = (kiv[trans_ki_idx] + kiv[trans_ki_idx-1]) / 2.0
        
        # compute rP intersection
        sigma_ys = 630.0  # MPa
        pi = math.pi
        best_ki = None
        best_diff = 1e9
        for ki in [round(x, 3) for x in [ki_crit[0] + i*0.001 for i in range(int((ki_crit[-1]-ki_crit[0])/0.001)+1)]]:
            L_crit = interp(ki, ki_crit, l_crit)  # um
            rP = (1.0/(6*pi)) * ((ki / sigma_ys)**2) * 1e6  # um
            diff = abs(rP - L_crit)
            if diff < best_diff:
                best_diff = diff
                best_ki = ki
        comparison = abs(trans_ki - best_ki) < 0.5
        
        result = {
            'transition_KI': round(trans_ki, 2),
            'K_I_where_rP_equals_lcrit': round(best_ki, 2),
            'comparison': bool(comparison)
        }
        with open(os.path.join(os.environ['OUTDIR'], 'transition_analysis.json'), 'w') as f:
            json.dump(result, f)
    else:
        raise ValueError(f"Unknown target {target}")

if __name__ == '__main__':
    generate(sys.argv[1])
GENEOF

# === solve block: hydride_growth_curves.csv ===
python3 << 'PYEOF'
import csv, math, os

def load_critical_curve(path):
    kk, ll = [], []
    with open(path) as f:
        r = csv.DictReader(f)
        for row in r:
            kk.append(float(row['KI']))
            ll.append(float(row['critical_length']))
    pairs = sorted(zip(kk, ll))
    return [p[0] for p in pairs], [p[1] for p in pairs]

def interp(x, xs, ys):
    if x <= xs[0]: return ys[0]
    if x >= xs[-1]: return ys[-1]
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            t = (x - xs[i]) / (xs[i+1] - xs[i])
            return ys[i] + t*(ys[i+1]-ys[i])
    return ys[-1]

# Load critical length curve from bundled fixture
ki_crit, l_crit = load_critical_curve('/solution/critical_length.csv')

# Plausible DHC velocity curve (stage I/II transition near 8 MPa√m)
v_KI_points = [6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 10.0, 11.0, 12.0, 14.0]
v_values     = [2e-10, 1e-9, 3e-9, 6e-9, 1e-8, 1.3e-8, 1.5e-8, 1.5e-8, 1.5e-8, 1.5e-8, 1.5e-8]

def velocity(KI):
    return interp(KI, v_KI_points, v_values)

# KI range for growth curves
KI_min, KI_max, dKI = 6.0, 14.0, 0.5
ki_vals = [round(KI_min + i*dKI, 2) for i in range(int((KI_max-KI_min)/dKI)+1)]

OUT = os.environ['OUTDIR']
with open(os.path.join(OUT, 'hydride_growth_curves.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['KI', 'time_label', 'hydride_length'])
    for KI in ki_vals:
        Lc = interp(KI, ki_crit, l_crit)          # µm
        v = velocity(KI)                          # m/s
        t_frac_sec = (Lc * 1e-6) / v
        t_frac_hr = t_frac_sec / 3600.0
        L_max = Lc + 10.0
        ratio = Lc / L_max
        if ratio >= 1.0:
            k = 0.0
        else:
            k = -math.log(1.0 - ratio) / t_frac_hr if t_frac_hr > 0 else 0.0
        times_hr = sorted({0.0, t_frac_hr * 0.5, t_frac_hr, t_frac_hr * 1.5, t_frac_hr * 5, 100.0})
        for th in times_hr:
            if k <= 0 or th <= 0:
                L = 0.0 if th == 0 else L_max
            else:
                L = L_max * (1.0 - math.exp(-k * th))
            if L < 0: L = 0.0
            if th == 0:
                lbl = '0h'
            elif th == int(th):
                lbl = f'{int(th)}h'
            else:
                lbl = f'{th:.2f}h'
            w.writerow([KI, lbl, round(L, 3)])
PYEOF

# === solve block: dhc_velocity_vs_KI.csv ===
python3 /tmp/gen.py dhc_velocity_vs_KI.csv

# === solve block: transition_analysis.json ===
python3 /tmp/gen.py transition_analysis.json

# === solve finalize ===
echo 'Oracle outputs written.'
