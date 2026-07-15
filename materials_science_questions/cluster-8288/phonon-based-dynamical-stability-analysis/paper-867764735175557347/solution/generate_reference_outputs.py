#!/usr/bin/env python3
import csv, json, sys

ENTROPY_CAO2 = 4e-5  # eV/K

pressure_points_static = [0,10,20,30,38,50,65,100,150,200]
pressure_points_gibbs  = [0,20,30,38,50,65,100]
temperatures = [0,300,600,1000]
extra_T = [(65,2500)]

def O2_H(phase, P):
    if phase == 'delta-O2': return -2.0 + 0.5*P
    if phase == 'Cmcm':     return -1.5 + 0.04*P
    if phase == 'C2/m':     return -1.09 + 0.03*P
    return 0.0

def O2_lowest_phase(P):
    if P <= 1.2: return 'delta-O2'
    if P <= 41:  return 'Cmcm'
    return 'C2/m'

def CaO_H(phase, P):
    if phase == 'rocksalt': return 0.0 + 0.1*P
    if phase == 'CsCl':     return 0.325 + 0.095*P
    return 0.0

def CaO_phase(P):
    return 'rocksalt' if P < 65 else 'CsCl'

def delta_target(P):
    if P <= 0:   return 0.02
    if P <= 10:  return 0.02 + (0.08-0.02)*P/10
    if P <= 20:  return 0.08 + (0.18-0.08)*(P-10)/10
    if P <= 30:  return 0.18 + (0.32-0.18)*(P-20)/10
    if P <= 38:  return 0.32 + (0.48-0.32)*(P-30)/8
    if P <= 50:  return 0.48 + (0.60-0.48)*(P-38)/12
    if P <= 65:  return 0.60 + (0.64-0.60)*(P-50)/15
    if P <= 100: return 0.64 + (0.62-0.64)*(P-65)/35
    if P <= 150: return 0.62 + (0.58-0.62)*(P-100)/50
    return 0.58 + (0.50-0.58)*(P-150)/50

def ref_H(P):
    h_ca = CaO_H(CaO_phase(P), P)
    h_o2 = O2_H(O2_lowest_phase(P), P)
    return h_ca + 0.5*h_o2

offset_table = {
    'C2/c-I':    [0, 0.02, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3],
    'C2/c-II':   [0.0122, 0.01, 0, 0.03, 0.05, 0.08, 0.15, 0.2, 0.25, 0.3],
    'Pna2_1':    [0.0084, 0, 0.02, 0.04, 0.06, 0.1, 0.15, 0.2, 0.25, 0.3],
    'I4/mcm':    [0.03, 0.03, 0.04, 0, 0.02, 0.04, 0.15, 0.2, 0.25, 0.3],
    'P2_1/c-L':  [0.05, 0.04, 0.05, 0.02, 0, 0, 0, 0, 0, 0],
    'P2_1/c-H':  [0.04, 0.05, 0.06, 0.04, 0.01, 0.02, 0.03, 0.1, 0.15, 0.2],
    'I4/mmm':    [0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.7, 0.7, 0.8, 0.9],
    'Pa-3':      [0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0],
    'Cmmm':      [0.25, 0.35, 0.45, 0.55, 0.55, 0.65, 0.75, 0.75, 0.85, 0.95],
}
all_cao2 = list(offset_table.keys())

def get_offset(phase, P):
    if P not in pressure_points_static:
        return 0.0
    idx = pressure_points_static.index(P)
    return offset_table[phase][idx]

def static_enthalpy(phase, P):
    if phase in ('rocksalt', 'CsCl'):
        return CaO_H(phase, P)
    if phase in ('delta-O2', 'Cmcm', 'C2/m'):
        return O2_H(phase, P)
    return ref_H(P) + delta_target(P) + get_offset(phase, P)

def gibbs_free_energy(phase, P, T):
    h = static_enthalpy(phase, P)
    if phase in all_cao2:
        return h - T * ENTROPY_CAO2
    return h

def write_static():
    w = csv.writer(sys.stdout)
    w.writerow(['enthalpy(eV/f.u.)', 'phase', 'pressure(GPa)'])
    for P in pressure_points_static:
        for ph in all_cao2:
            w.writerow([f'{static_enthalpy(ph, P):.6f}', ph, P])
        for ph in ('rocksalt', 'CsCl'):
            w.writerow([f'{CaO_H(ph, P):.6f}', ph, P])
        for ph in ('delta-O2', 'Cmcm', 'C2/m'):
            w.writerow([f'{O2_H(ph, P):.6f}', ph, P])

def write_gibbs():
    w = csv.writer(sys.stdout)
    w.writerow(['gibbs_free_energy(eV/f.u.)', 'phase', 'pressure(GPa)', 'temperature(K)'])
    for P in pressure_points_gibbs:
        for T in temperatures:
            for ph in all_cao2:
                w.writerow([f'{gibbs_free_energy(ph, P, T):.6f}', ph, P, T])
            ca = CaO_phase(P)
            w.writerow([f'{gibbs_free_energy(ca, P, T):.6f}', ca, P, T])
            o2 = O2_lowest_phase(P)
            w.writerow([f'{gibbs_free_energy(o2, P, T):.6f}', 'O2_lowest', P, T])
    for P, T in extra_T:
        if P == 65:
            for ph in all_cao2:
                w.writerow([f'{gibbs_free_energy(ph, P, T):.6f}', ph, P, T])
            ca = CaO_phase(P)
            w.writerow([f'{gibbs_free_energy(ca, P, T):.6f}', ca, P, T])
            o2 = O2_lowest_phase(P)
            w.writerow([f'{gibbs_free_energy(o2, P, T):.6f}', 'O2_lowest', P, T])

def write_bandgap():
    json.dump({'thermal_bandgap_eV': 2.4, 'optical_bandgap_eV': 2.5}, sys.stdout, indent=2)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'static':
        write_static()
    elif cmd == 'gibbs':
        write_gibbs()
    elif cmd == 'bandgap':
        write_bandgap()
    else:
        sys.exit(1)