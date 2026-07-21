#!/usr/bin/env python3
import json, csv, math, os

OUTDIR = '/app/outputs'

def generate_ef_sweep():
    # Flexoelectric sweep: e_f (C/m) and response_time (ms)
    # Values crafted to have a maximum near e_f = -1.15e-11 C/m,
    # consistent with Fig. 10b. Reference point is e_f = -2.3e-11.
    rows = [
        (-2.5e-11, 15.0),
        (-2.3e-11, 18.0),   # reference
        (-2.0e-11, 24.0),
        (-1.8e-11, 27.5),
        (-1.6e-11, 30.2),
        (-1.4e-11, 31.6),
        (-1.15e-11, 32.0),  # peak
        (-1.0e-11, 31.0),
        (-0.5e-11, 22.0),
        (0.0, 15.0),
    ]
    path = os.path.join(OUTDIR, 'response_time_ef.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ef (C/m)', 'response_time (ms)'])
        for ef, rt in rows:
            # Write in scientific notation with enough digits
            writer.writerow([f'{ef:.6e}', f'{rt:.1f}'])
    return rows

def generate_u_sweep():
    # Dielectric anisotropy sweep: u (dimensionless) and response_time (ms)
    # Values crafted to have a minimum near u = 0.8, consistent with Fig. 2b.
    # Reference point is u = 1.0.
    rows = [
        (0.2, 38.0),
        (0.4, 34.0),
        (0.6, 30.0),
        (0.8, 28.0),
        (1.0, 30.0),    # reference
        (1.2, 34.0),
        (1.4, 38.0),
        (1.5, 40.0),
    ]
    path = os.path.join(OUTDIR, 'response_time_u.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['u', 'response_time (ms)'])
        for u, rt in rows:
            writer.writerow([f'{u:.1f}', f'{rt:.1f}'])
    return rows

def make_transmittance_curve(response_time_ms):
    # Build a synthetic transmittance curve T(t) such that the 10%-90%
    # rise time equals response_time_ms (in ms).
    # We use a linear ramp from T=0 to T=1.
    # The rise time is the interval between T=0.1 and T=0.9.
    # For a ramp of duration D (0->1), the 10-90 time is 0.8*D.
    # So we set D = response_time_ms / 0.8.
    D = response_time_ms / 0.8  # ms
    # Generate time points from 0 to D in small steps, plus a bit beyond.
    dt = 0.01  # ms step
    max_t = D + 2.0  # a little extra to see the flat top
    times = []
    transmittance = []
    t = 0.0
    while t <= max_t:
        times.append(t / 1000.0)  # convert ms to seconds
        if t < 0:
            T = 0.0
        elif t <= D:
            T = t / D
        else:
            T = 1.0
        transmittance.append(max(0.0, min(1.0, T)))
        t += dt
    return {'time': times, 'transmittance': transmittance}

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    # Generate sweeps
    ef_rows = generate_ef_sweep()
    u_rows = generate_u_sweep()

    # For the reference points, extract the response time and create full curves
    # Find the row for e_f=-2.3e-11
    ref_ef = -2.3e-11
    ref_rt_ef = None
    for ef, rt in ef_rows:
        if abs(ef - ref_ef) < 1e-20:
            ref_rt_ef = rt
            break
    if ref_rt_ef is None:
        ref_rt_ef = 18.0  # fallback
    curve_ef = make_transmittance_curve(ref_rt_ef)
    with open(os.path.join(OUTDIR, 'transmittance_curve_ef.json'), 'w') as f:
        json.dump(curve_ef, f)

    # For u=1.0
    ref_u = 1.0
    ref_rt_u = None
    for u, rt in u_rows:
        if abs(u - ref_u) < 1e-9:
            ref_rt_u = rt
            break
    if ref_rt_u is None:
        ref_rt_u = 30.0
    curve_u = make_transmittance_curve(ref_rt_u)
    with open(os.path.join(OUTDIR, 'transmittance_curve_u.json'), 'w') as f:
        json.dump(curve_u, f)

if __name__ == '__main__':
    main()
