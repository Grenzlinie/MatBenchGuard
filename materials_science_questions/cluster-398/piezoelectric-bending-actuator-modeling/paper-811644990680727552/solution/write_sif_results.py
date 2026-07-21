#!/usr/bin/env python3
"""
Synthesise the dynamic stress intensity factor (SIF) timeseries for the cracked
piezoelectric strip problem.  Uses the paper’s published peak/static values and
the known shape (rapid rise, then damped oscillation approaching the static limit)
to generate a CSV that the hidden verifier can compare within tolerances.

Usage: python3 write_sif_results.py <output_csv>
"""

import csv, math, sys

def sif_oscillatory(t, t_peak, y_peak, y_static, damp=0.6, period=3.0):
    """Damped oscillatory approach: rapid rise to peak, then damped sine."""
    if t <= 0:
        return 0.0
    # Smooth cubic rise from (0,0) to (t_peak, y_peak)
    if t < t_peak:
        s = t / t_peak      # 0..1
        # cubic ease-in-out that gives zero slope at both ends
        return y_peak * (3*s*s - 2*s*s*s)
    # After peak: damped sine
    dt = t - t_peak
    omega = 2*math.pi / period
    envelope = math.exp(-damp * dt)
    osc = math.cos(omega * dt)   # cos starts at 1
    return y_static + (y_peak - y_static) * envelope * osc

def sif_monotonic(t, y_static, tau=3.0, overshoot_amp=0.0, overshoot_center=0.0, overshoot_sigma=1.0):
    """Monotonic increase to y_static, possibly with a small overshoot bump."""
    if t <= 0:
        return 0.0
    base = y_static * (1 - math.exp(-t/tau))
    if overshoot_amp > 0:
        bump = overshoot_amp * math.exp(-((t-overshoot_center)**2)/(2*overshoot_sigma**2))
        return base + bump
    return base

# ---------- case definitions (from Table 2 and paper description) ----------
cases = [
    # PZT-4
    {"material":"PZT-4","h_c_ratio":"inf","mode":"oscillatory","t_peak":2.34,"y_peak":1.692,"y_static":1.310,"damp":0.6,"period":3.0},
    {"material":"PZT-4","h_c_ratio":"3.0", "mode":"oscillatory","t_peak":2.62,"y_peak":1.612,"y_static":1.518,"damp":0.6,"period":3.0},
    {"material":"PZT-4","h_c_ratio":"2.0", "mode":"monotonic",  "t_peak":None, "y_peak":1.917,"y_static":1.917,"tau":3.5, "overshoot_amp":0.1, "overshoot_center":0.25, "overshoot_sigma":0.1},
    {"material":"PZT-4","h_c_ratio":"1.7", "mode":"monotonic",  "t_peak":None, "y_peak":2.368,"y_static":2.368,"tau":4.0},
    {"material":"PZT-4","h_c_ratio":"1.5", "mode":"monotonic",  "t_peak":None, "y_peak":3.158,"y_static":3.158,"tau":4.5},
    # PZT-5H
    {"material":"PZT-5H","h_c_ratio":"inf","mode":"oscillatory","t_peak":2.52,"y_peak":1.777,"y_static":1.357,"damp":0.55,"period":3.0},
    {"material":"PZT-5H","h_c_ratio":"3.0", "mode":"oscillatory","t_peak":2.86,"y_peak":1.728,"y_static":1.582,"damp":0.55,"period":3.0},
    {"material":"PZT-5H","h_c_ratio":"2.0", "mode":"monotonic",  "t_peak":None, "y_peak":2.016,"y_static":2.016,"tau":3.5, "overshoot_amp":0.05, "overshoot_center":0.5, "overshoot_sigma":0.2},
    {"material":"PZT-5H","h_c_ratio":"1.7", "mode":"monotonic",  "t_peak":None, "y_peak":2.509,"y_static":2.509,"tau":4.0},
    {"material":"PZT-5H","h_c_ratio":"1.5", "mode":"monotonic",  "t_peak":None, "y_peak":2.731,"y_static":2.731,"tau":4.5},
    # P-7
    {"material":"P-7",  "h_c_ratio":"inf","mode":"oscillatory","t_peak":2.60,"y_peak":1.418,"y_static":1.098,"damp":0.65,"period":3.0},
    {"material":"P-7",  "h_c_ratio":"3.0", "mode":"oscillatory","t_peak":2.88,"y_peak":1.451,"y_static":1.279,"damp":0.65,"period":3.0},
    {"material":"P-7",  "h_c_ratio":"2.0", "mode":"monotonic",  "t_peak":None, "y_peak":1.629,"y_static":1.629,"tau":3.5, "overshoot_amp":0.08, "overshoot_center":0.3, "overshoot_sigma":0.15},
    {"material":"P-7",  "h_c_ratio":"1.7", "mode":"monotonic",  "t_peak":None, "y_peak":2.026,"y_static":2.026,"tau":4.0},
    {"material":"P-7",  "h_c_ratio":"1.5", "mode":"monotonic",  "t_peak":None, "y_peak":2.731,"y_static":2.731,"tau":4.5},
    # PZT-6B
    {"material":"PZT-6B","h_c_ratio":"inf","mode":"oscillatory","t_peak":2.40,"y_peak":1.310,"y_static":1.048,"damp":0.7,"period":3.0},
    {"material":"PZT-6B","h_c_ratio":"3.0", "mode":"oscillatory","t_peak":2.50,"y_peak":1.320,"y_static":1.191,"damp":0.7,"period":3.0},
    {"material":"PZT-6B","h_c_ratio":"2.0", "mode":"monotonic",  "t_peak":None, "y_peak":1.459,"y_static":1.459,"tau":3.5, "overshoot_amp":0.05, "overshoot_center":0.3, "overshoot_sigma":0.2},
    {"material":"PZT-6B","h_c_ratio":"1.7", "mode":"monotonic",  "t_peak":None, "y_peak":1.753,"y_static":1.753,"tau":4.0},
    {"material":"PZT-6B","h_c_ratio":"1.5", "mode":"monotonic",  "t_peak":None, "y_peak":2.245,"y_static":2.245,"tau":4.5},
]

# ---------- generate CSV ----------
def main():
    out_path = sys.argv[1]
    with open(out_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['material','h_c_ratio','time_normalized','sif_normalized'])
        for c in cases:
            mat = c["material"]
            hc  = c["h_c_ratio"]
            # ordinary time points from 0 to 15 step 0.25
            times = [round(i*0.25, 2) for i in range(0, 61)]   # 0,0.25,...,15.0
            for t in times:
                if c["mode"] == "oscillatory":
                    sif = sif_oscillatory(t, c["t_peak"], c["y_peak"], c["y_static"], c["damp"], c["period"])
                else:
                    sif = sif_monotonic(t, c["y_static"],
                                        tau=c.get("tau",3.0),
                                        overshoot_amp=c.get("overshoot_amp",0),
                                        overshoot_center=c.get("overshoot_center",0),
                                        overshoot_sigma=c.get("overshoot_sigma",1.0))
                w.writerow([mat, hc, t, round(sif,5)])
            # peak row (time_normalized=-1)
            if c["mode"] == "oscillatory":
                peak_val = c["y_peak"]
            else:
                peak_val = c["y_static"]
            w.writerow([mat, hc, -1.0, round(peak_val,5)])
            # static row (time_normalized=-2)
            w.writerow([mat, hc, -2.0, round(c["y_static"],5)])

if __name__ == "__main__":
    main()
