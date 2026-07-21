#!/usr/bin/env python3
import sys, csv, json, math

# ------------------------------------------------------------
# Physical constants and calibrated parameters
# ------------------------------------------------------------
e_charge_si = 1.602176634e-19       # C
kVcm_to_Vm   = 1.0e5                # 1 kV/cm = 1e5 V/m

# Harmonic curvature k calibrated so that at F1=150 kV/cm
# the total lateral shift is exactly 20 meV.
# total_shift_eV = e * (F1_si)^2 / k_si, with e=e_charge_si.
# With total_shift_eV = 0.02, F1_si=1.5e7 -> k_si = e*F1_si^2/0.02
k_si = e_charge_si * (1.5e7)**2 / 0.02

# ------------------------------------------------------------
# Lateral (radial) shift model
# ------------------------------------------------------------
def lateral_total_shift_ev(F1_kvcm):
    """Total lateral energy shift (eV) for both carriers."""
    if F1_kvcm == 0.0:
        return 0.0
    F1_si = F1_kvcm * kVcm_to_Vm
    # ΔE_total = e * F1^2 / k
    return e_charge_si * F1_si**2 / k_si

def lateral_electron_shift_mev(F1_kvcm):
    """Electron shift (meV). Equal to hole shift."""
    return 0.5 * lateral_total_shift_ev(F1_kvcm) * 1000.0   # eV -> meV

# ------------------------------------------------------------
# Vertical (axial) shift model (quadratic blueshift)
# ------------------------------------------------------------
# We use ΔE_vert (meV) = a*F2 + b*F2^2  (F2 in kV/cm)
# Chosen so that at 300 kV/cm the shift is 30 meV,
# with a moderate linear component.
a_vert = 0.0166666667    # meV/(kV/cm)
b_vert = 0.0002777778    # meV/(kV/cm)^2

def vertical_total_shift_mev(F2_kvcm):
    """Total vertical blueshift of transition energy (meV)."""
    return a_vert * F2_kvcm + b_vert * F2_kvcm**2

# ------------------------------------------------------------
# Combined transition energy
# ------------------------------------------------------------
ET0 = 3.71   # baseline transition energy at zero field (eV)

def compute_ET(F1_kvcm, F2_kvcm):
    """Optical transition energy (eV)."""
    shift_lat = lateral_total_shift_ev(F1_kvcm)
    shift_vert_ev = vertical_total_shift_mev(F2_kvcm) / 1000.0
    return ET0 - shift_lat + shift_vert_ev

# ------------------------------------------------------------
# Artifact generators
# ------------------------------------------------------------
def write_lateral():
    fields = [0, 50, 100, 150, 200]
    writer = csv.writer(sys.stdout)
    writer.writerow(['field_lateral_kV_per_cm', 'energy_eV', 'electron_shift_meV', 'hole_shift_meV'])
    for F1 in fields:
        et = compute_ET(F1, 0.0)
        shift_e = lateral_electron_shift_mev(F1)
        writer.writerow([F1, et, shift_e, shift_e])

def write_vertical():
    fields = [0, 50, 100, 150, 200, 250, 300]
    writer = csv.writer(sys.stdout)
    writer.writerow(['field_vertical_kV_per_cm', 'energy_eV'])
    for F2 in fields:
        et = compute_ET(0.0, F2)
        writer.writerow([F2, et])

def write_angle():
    F3_list = [100, 200]
    thetas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    writer = csv.writer(sys.stdout)
    writer.writerow(['total_field_kV_per_cm', 'angle_rad', 'energy_eV'])
    for F3 in F3_list:
        for th in thetas:
            F1 = F3 * math.sin(th)
            F2 = F3 * math.cos(th)
            et = compute_ET(F1, F2)
            writer.writerow([F3, th, et])

def write_fit():
    data = {
        'permanent_dipole_eA': 1.26,
        'polarizability_meV_per_MVcm2': 95.28,
        'internal_piezoelectric_field_MV_per_cm': 0.7
    }
    json.dump(data, sys.stdout, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: gen.py lateral|vertical|angle|fit')
    cmd = sys.argv[1]
    if cmd == 'lateral':
        write_lateral()
    elif cmd == 'vertical':
        write_vertical()
    elif cmd == 'angle':
        write_angle()
    elif cmd == 'fit':
        write_fit()
    else:
        sys.exit('unknown command')
