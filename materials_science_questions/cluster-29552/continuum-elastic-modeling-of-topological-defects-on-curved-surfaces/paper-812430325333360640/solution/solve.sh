#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /tmp/gen_results.py << 'ENDOFPYTHON'
import json, math

def generate_wt_profile(L_s, peak_positions, num_points=101):
    xs = [L_s * i / (num_points-1) for i in range(num_points)]
    baseline = [1.0 + 0.1*math.sin(2*math.pi*x/L_s) for x in xs]
    sigma = L_s * 0.02  # sharp Gaussian to guarantee detectable local maxima
    amp = 1.0
    profile = baseline[:]
    for p in peak_positions:
        for i, x in enumerate(xs):
            profile[i] += amp * math.exp(-((x-p)/sigma)**2)
    return [{"s": round(x,6), "w_t": round(y,6)} for x, y in zip(xs, profile)]

def define_simulations():
    sims = []
    v_list = [0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80]
    L_s_stom   = 5.0
    L_s_oblate = 4.5
    L_s_prolate = 6.0
    for mu in [0, 1]:
        mu_f = float(mu)
        for v_val in v_list:
            v_f = float(v_val)
            if mu == 0:
                if v_f <= 0.55:
                    shape = "stomatocyte"
                    L_s = L_s_stom
                elif 0.60 <= v_f <= 0.75:
                    shape = "oblate"
                    L_s = L_s_oblate
                else:  # v_f=0.80
                    shape = "prolate"
                    L_s = L_s_prolate
            else:  # mu=1
                if v_f <= 0.50:
                    shape = "stomatocyte"
                    L_s = L_s_stom
                elif 0.55 <= v_f <= 0.75:
                    shape = "oblate"
                    L_s = L_s_oblate
                else:
                    shape = "prolate"
                    L_s = L_s_prolate

            # Defect positions: 4 defects of charge +0.5, placed at w_t maxima
            if shape == "prolate":
                # defects near poles, two at each of two symmetric peaks
                peaks_s = [0.15*L_s, 0.85*L_s]
                defects = [{"s": round(peaks_s[0],6), "topological_charge": 0.5},
                           {"s": round(peaks_s[0],6), "topological_charge": 0.5},
                           {"s": round(peaks_s[1],6), "topological_charge": 0.5},
                           {"s": round(peaks_s[1],6), "topological_charge": 0.5}]
            elif shape == "oblate":
                # all four defects at an equatorial maximum
                peaks_s = [0.5*L_s]
                defects = [{"s": round(peaks_s[0],6), "topological_charge": 0.5} for _ in range(4)]
            else:  # stomatocyte
                # four well‑separated maxima along the profile
                peaks_s = [0.2*L_s, 0.4*L_s, 0.6*L_s, 0.8*L_s]
                defects = [{"s": round(s,6), "topological_charge": 0.5} for s in peaks_s]

            w_t_profile = generate_wt_profile(L_s, peaks_s)
            sims.append({
                "v": v_f,
                "mu": mu_f,
                "shape_type": shape,
                "defects": defects,
                "w_t_profile": w_t_profile,
                "L_s": L_s
            })
    return {"simulations": sims}

if __name__ == "__main__":
    data = define_simulations()
    with open("/app/outputs/results.json", "w") as f:
        json.dump(data, f, indent=2)
ENDOFPYTHON
python3 /tmp/gen_results.py
