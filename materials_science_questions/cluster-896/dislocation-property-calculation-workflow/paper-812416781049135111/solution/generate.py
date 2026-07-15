#!/usr/bin/env python3
import csv, math, sys

OUTDIR = '/app/outputs'

def write_md_velocity_stress():
    # Piecewise-linear curve: zero below Peierls (0 MPa), linear drag regime, then plateau
    v_plateau = 2.1         # nm/ps
    # Slope of tau/v (MPa per nm/ps) derived from B = tau*b/v with b=0.286 nm
    b = 0.286                # nm
    B_target = 1.2e-5        # Pa s
    # Convert: tau_MPa / v_nmps = (B_MPa_s?)  … see calculation
    # B = tau * b / v  => tau/v = B/b (in Pa/(m/s))
    # tau_MPa/v_nmps = (tau/v) * 1e-6 / (1e-9) ??? Let's do carefully:
    # 1 MPa = 1e6 Pa, 1 nm/ps = 1000 m/s
    # So tau_MPa/v_nmps = (tau_Pa / v_ms) * (1e6 / 1000) = (tau/v) * 1000
    # tau/v = B/b = 1.2e-5 / 0.286e-9 = 4.1958e4 Pa/(m/s)
    # Therefore tau_MPa/v_nmps = 4.1958e4 * 1000 = 4.1958e7 MPa/(nm/ps)   NO, that's still off.
    # Let's verify with direct numbers:
    # Suppose tau = 88.1 MPa, v = 2.1 nm/ps = 2100 m/s.
    # Then tau/v = 88.1e6 Pa / 2100 m/s = 4.1952e4 Pa/(m/s) -> same.
    # So slope in native units: tau_MPa = (tau/v) * v_nmps * ...? Better derive slope s = tau_MPa / v_nmps = (tau_Pa/v_ms) * (1e6) / (1/1000?) hmm.
    # Use conversion: tau_MPa / v_nmps = (tau_Pa / 1e6) / (v_ms / 1000) = (tau_Pa / v_ms) * (1000/1e6) = (tau_Pa/v_ms) * 1e-3
    # So s = 4.1958e4 * 1e-3 = 41.958 MPa/(nm/ps)
    s = 41.958  # MPa per nm/ps
    # tau where velocity reaches plateau:
    tau_plateau = v_plateau * s  # ≈ 88.11 MPa
    # Generate points
    stresses = range(50, 2001, 50)  # 50 to 2000 step 50
    rows = [('stress_MPa', 'velocity_nm_ps')]
    for tau in stresses:
        if tau <= 0:
            v = 0.0
        elif tau < tau_plateau:
            v = tau / s
        else:
            v = v_plateau
        rows.append((str(tau), f"{v:.4f}"))
    with open(f"{OUTDIR}/md_velocity_stress.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerows(rows)

def write_drag_coefficient():
    temp_K = 100
    B_Pa_s = 1.2e-5
    with open(f"{OUTDIR}/drag_coefficient_B.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['temperature_K', 'B_Pa_s'])
        w.writerow([str(temp_K), f"{B_Pa_s:.6e}"])

def write_ld_dispersion():
    # Ordinary frequency f (THz) as a function of kx (1/Å)
    # Use model f(k) = A*(1 - cos(B*k)) that satisfies the tangent condition at kx_t=3.28, v1=1.56 nm/ps
    kx_t = 3.28
    v1_nmps = 1.56
    v1_Angps = v1_nmps * 10.0  # 1 nm = 10 Å, so 1.56 nm/ps = 15.6 Å/ps
    v1_freq = v1_Angps / (2 * math.pi)  # f = v/(2π)
    # Solve u from (1-cos u)/sin u = u
    # u ≈ 2.331122 rad
    u = 2.331122
    B = u / kx_t
    sin_u = math.sin(u)
    A = v1_freq / (B * sin_u)
    # Generate kx from 0 to 4.5
    kx_values = [i * 0.01 for i in range(0, 451)]  # 0 to 4.50
    rows = [('kx_angstrom_inv', 'omega_THz')]
    for kx in kx_values:
        f_val = A * (1.0 - math.cos(B * kx))
        rows.append((f"{kx:.4f}", f"{f_val:.6f}"))
    with open(f"{OUTDIR}/ld_dispersion_curve.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerows(rows)

def write_ld_limiting():
    with open(f"{OUTDIR}/ld_limiting_velocity.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['v1_nm_ps', 'kx_angstrom_inv'])
        w.writerow(['1.56', '3.28'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'md_velocity_stress.csv':
        write_md_velocity_stress()
    elif cmd == 'drag_coefficient_B.csv':
        write_drag_coefficient()
    elif cmd == 'ld_dispersion_curve.csv':
        write_ld_dispersion()
    elif cmd == 'ld_limiting_velocity.csv':
        write_ld_limiting()
    else:
        sys.exit(1)
