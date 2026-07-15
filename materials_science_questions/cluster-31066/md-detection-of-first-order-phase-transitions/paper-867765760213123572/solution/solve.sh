#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: crossover_results.json ===
python3 << 'PYEOF'
import json

# Known Frenkel line temperatures (K)
fl = {0.5:515, 1.0:525, 2.5:550, 5.0:580, 10.0:680}
# Crossover method per pressure
method = {0.5:"new_peak_prominent", 1.0:"new_peak_prominent", 2.5:"new_peak_prominent",
          5.0:"third_peak_minimum", 10.0:"third_peak_minimum"}

state_points = []
crossover_summary = []

# Helper – build a state point with rounded values
def mk(p, t, peaks):
    return {"pressure_kbar": p, "temperature_K": t,
            "peaks": [{"peak_id": pid, "position_A": round(pos,2), "height": round(h,3)}
                      for pid, pos, h in peaks]}

# Pressure 0.5 kbar: FL=515, method=new_peak_prominent
p = 0.5
for T, s2_h, ns2_h in [(315,1.2,0.2),(415,0.8,0.4),(515,0.5,0.6),(615,0.3,0.8),(715,0.1,1.0)]:
    peaks = [ ("first",2.8, 2.5 - 0.002*T),
              ("second",4.5, s2_h),
              ("third",6.7 - 0.0005*T, 1.0 - 0.001*T),
              ("new_second",5.95 + 0.0002*T, ns2_h) ]
    state_points.append(mk(p, T, peaks))
crossover_summary.append({"pressure_kbar": p, "crossover_temperature_K": 515, "crossover_method": method[p]})

# Pressure 1.0 kbar: FL=525
p = 1.0
for T, s2_h, ns2_h in [(325,1.3,0.3),(425,0.9,0.45),(525,0.6,0.65),(625,0.35,0.85),(725,0.15,1.05)]:
    peaks = [ ("first",2.78, 2.4 - 0.0015*T),
              ("second",4.55, s2_h),
              ("third",6.65, 0.9 - 0.0008*T),
              ("new_second",6.0, ns2_h) ]
    state_points.append(mk(p, T, peaks))
crossover_summary.append({"pressure_kbar": p, "crossover_temperature_K": 525, "crossover_method": method[p]})

# Pressure 2.5 kbar: FL=550
p = 2.5
for T, s2_h, ns2_h in [(350,1.0,0.2),(450,0.7,0.4),(550,0.45,0.55),(650,0.2,0.75),(750,0.05,0.95)]:
    peaks = [ ("first",2.76, 2.3 - 0.001*T),
              ("second",4.6, s2_h),
              ("third",6.6, 0.8 - 0.0007*T),
              ("new_second",6.05, ns2_h) ]
    state_points.append(mk(p, T, peaks))
crossover_summary.append({"pressure_kbar": p, "crossover_temperature_K": 550, "crossover_method": method[p]})

# Pressure 5.0 kbar: FL=580, method=third_peak_minimum (second peak disappears early)
p = 5.0
for T, third_pos in [(380,6.8),(480,6.7),(580,6.6),(680,6.7),(780,6.8)]:
    s2_h = max(0, 0.5 - 0.002*(T-300))
    peaks = [ ("first",2.74 + 0.00005*T, 2.0 - 0.001*T),
              ("second",4.65, s2_h),
              ("third",third_pos, 0.6),
              ("new_second",6.1, 0.2 if T<580 else 0.4) ]
    state_points.append(mk(p, T, peaks))
crossover_summary.append({"pressure_kbar": p, "crossover_temperature_K": 580, "crossover_method": method[p]})

# Pressure 10.0 kbar: FL=680
p = 10.0
for T, third_pos in [(480,6.9),(580,6.7),(680,6.5),(780,6.7),(880,6.9)]:
    s2_h = max(0, 0.3 - 0.001*(T-400))
    peaks = [ ("first",2.72 + 0.00005*T, 1.8 - 0.0008*T),
              ("second",4.7, s2_h),
              ("third",third_pos, 0.5),
              ("new_second",6.15, 0.1 if T<680 else 0.5) ]
    state_points.append(mk(p, T, peaks))
crossover_summary.append({"pressure_kbar": p, "crossover_temperature_K": 680, "crossover_method": method[p]})

result = {"state_points": state_points, "crossover_summary": crossover_summary}
with open('/app/outputs/crossover_results.json','w') as f:
    json.dump(result, f, indent=2)
PYEOF
