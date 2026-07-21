#!/usr/bin/env python3
import math
import csv
import json
from collections import defaultdict

# Keating parameters for Si-centered tetrahedra (all in mdyne/angstrom)
beta_map = {
    ('Si','Si'):0.073, ('Si','N'):0.19, ('Si','H'):0.06,
    ('N','N'):0.3, ('N','H'):0.21, ('H','H'):0.12
}
# Bond lengths (angstrom)
r_bond = {'Si':2.35, 'N':1.72, 'H':1.48}

theta0_rad = math.acos(-1.0/3.0)
theta0_deg = math.degrees(theta0_rad)
cos0 = -1.0/3.0

def deg2rad(d):
    return d * math.pi / 180.0
def rad2deg(r):
    return r * 180.0 / math.pi
def cosd(d):
    return math.cos(deg2rad(d))

def get_beta(t1, t2):
    if t1 > t2:
        t1, t2 = t2, t1
    return beta_map[(t1, t2)]

def compute_ABBB(site_type, A_type, B_type, angle_range, rA, rB):
    beta_BB = get_beta(B_type, B_type)
    beta_AB = get_beta(A_type, B_type)
    rows = []
    for theta_BB in angle_range:
        cos_BB = cosd(theta_BB)
        sin2 = (2.0/3.0) * (1.0 - cos_BB)
        cos_AB = -math.sqrt(max(0.0, 1.0 - sin2))
        theta_AB = math.degrees(math.acos(max(-1.0, min(1.0, cos_AB))))
        # V for bond to B (Si)
        V_Si = (3.0/16.0) * (
            2.0 * beta_BB * rB**2 * (cos_BB - cos0)**2
            + beta_AB * rB * rA * (cos_AB - cos0)**2
        )
        # V for bond to A
        V_A = (3.0/16.0) * (
            3.0 * beta_AB * rA * rB * (cos_AB - cos0)**2
        )
        rows.append({'site_type':site_type, 'mean_angle_deg':theta_BB, 'V_theta':V_Si, 'bond':'Si-Si'})
        rows.append({'site_type':site_type, 'mean_angle_deg':theta_BB, 'V_theta':V_A, 'bond':'Si-'+A_type})
    return rows

def compute_SiHNSi2(angle_range):
    rows_all = []
    for theta_CC in angle_range:
        best_total = float('inf')
        best_angles = None
        for theta_BC in [x*0.2 for x in range(400, 901)]: # 80 to 180 step 0.2
            best_diff = 1e9
            best_theta_AB = None
            for theta_AB in [x*0.1 for x in range(600, 1801)]: # 60 to 180
                theta_AC = theta0_deg - 3.5*(theta_AB - theta0_deg)
                if theta_AC < 0 or theta_AC > 180:
                    continue
                c_AC_expected = cosd(theta_AC)
                c_BC = cosd(theta_BC)
                s_BC = math.sin(deg2rad(theta_BC))
                s_AB = math.sin(deg2rad(theta_AB))
                s_half_CC = math.sin(deg2rad(theta_CC/2.0))
                c_AC_calc = c_BC * cosd(theta_AB) + s_AB * s_BC * s_half_CC
                diff = abs(c_AC_expected - c_AC_calc)
                if diff < best_diff:
                    best_diff = diff
                    best_theta_AB = theta_AB
            if best_theta_AB is None: continue
            theta_AB = best_theta_AB
            theta_AC = theta0_deg - 3.5*(theta_AB - theta0_deg)
            # Compute total V
            V_H = (3.0/16.0)*(
                get_beta('H','N') * r_bond['H'] * r_bond['N'] * (cosd(theta_AB) - cos0)**2
                + 2* get_beta('H','Si') * r_bond['H'] * r_bond['Si'] * (cosd(theta_AC) - cos0)**2
            )
            V_N = (3.0/16.0)*(
                get_beta('H','N') * r_bond['N'] * r_bond['H'] * (cosd(theta_AB) - cos0)**2
                + 2* get_beta('N','Si') * r_bond['N'] * r_bond['Si'] * (cosd(theta_BC) - cos0)**2
            )
            V_Si = (3.0/16.0)*(
                get_beta('H','Si') * r_bond['Si'] * r_bond['H'] * (cosd(theta_AC) - cos0)**2
                + get_beta('N','Si') * r_bond['Si'] * r_bond['N'] * (cosd(theta_BC) - cos0)**2
                + get_beta('Si','Si') * r_bond['Si']**2 * (cosd(theta_CC) - cos0)**2
            )
            total = V_H + V_N + 2*V_Si
            if total < best_total:
                best_total = total
                best_angles = (theta_AB, theta_AC, theta_BC, theta_CC)
        if best_angles is not None:
            theta_AB, theta_AC, theta_BC, theta_CC = best_angles
            V_Si_final = (3.0/16.0)*(
                get_beta('H','Si') * r_bond['Si'] * r_bond['H'] * (cosd(theta_AC) - cos0)**2
                + get_beta('N','Si') * r_bond['Si'] * r_bond['N'] * (cosd(theta_BC) - cos0)**2
                + get_beta('Si','Si') * r_bond['Si']**2 * (cosd(theta_CC) - cos0)**2
            )
            V_N_final = (3.0/16.0)*(
                get_beta('H','N') * r_bond['N'] * r_bond['H'] * (cosd(theta_AB) - cos0)**2
                + 2* get_beta('N','Si') * r_bond['N'] * r_bond['Si'] * (cosd(theta_BC) - cos0)**2
            )
            V_H_final = (3.0/16.0)*(
                get_beta('H','N') * r_bond['H'] * r_bond['N'] * (cosd(theta_AB) - cos0)**2
                + 2* get_beta('H','Si') * r_bond['H'] * r_bond['Si'] * (cosd(theta_AC) - cos0)**2
            )
            avg = (V_Si_final + V_N_final) / 2.0
            rows_all.append({'site_type':'SiHNSi2', 'mean_angle_deg':theta_CC, 'V_theta':V_Si_final, 'bond':'Si-Si'})
            rows_all.append({'site_type':'SiHNSi2', 'mean_angle_deg':theta_CC, 'V_theta':V_N_final, 'bond':'Si-N'})
            rows_all.append({'site_type':'SiHNSi2', 'mean_angle_deg':theta_CC, 'V_theta':V_H_final, 'bond':'Si-H'})
            rows_all.append({'site_type':'SiHNSi2', 'mean_angle_deg':theta_CC, 'V_theta':avg, 'bond':'average'})
    return rows_all

def compute_all_equal(site_type, neighbors, angle_range):
    rows = []
    for theta in angle_range:
        cos_t = cosd(theta)
        V_by_type = defaultdict(list)
        for i, t_i in enumerate(neighbors):
            r_i = r_bond[t_i]
            sum_k = 0.0
            for k, t_k in enumerate(neighbors):
                if k == i: continue
                r_k = r_bond[t_k]
                beta = get_beta(t_i, t_k)
                sum_k += beta * r_i * r_k * (cos_t - cos0)**2
            V = (3.0/16.0) * sum_k
            V_by_type['Si-'+t_i].append(V)
        all_vals = []
        for bt, vals in V_by_type.items():
            v_avg = sum(vals)/len(vals)
            rows.append({'site_type':site_type, 'mean_angle_deg':theta, 'V_theta':v_avg, 'bond':bt})
            all_vals.append(v_avg)
        if all_vals:
            overall = sum(all_vals)/len(all_vals)
            rows.append({'site_type':site_type, 'mean_angle_deg':theta, 'V_theta':overall, 'bond':'average'})
    return rows

def main():
    angle_range = list(range(90, 131))
    all_rows = []
    # SiSi4
    all_rows.extend(compute_all_equal('SiSi4', ['Si','Si','Si','Si'], angle_range))
    # SiNSi3 via ABBB
    all_rows.extend(compute_ABBB('SiNSi3', 'N', 'Si', angle_range, r_bond['N'], r_bond['Si']))
    # SiHSi3 via ABBB
    all_rows.extend(compute_ABBB('SiHSi3', 'H', 'Si', angle_range, r_bond['H'], r_bond['Si']))
    # SiHNSi2 via optimized
    all_rows.extend(compute_SiHNSi2(angle_range))
    # dihydrogenated sites using all-equal
    all_rows.extend(compute_all_equal('SiH2Si2', ['H','H','Si','Si'], angle_range))
    all_rows.extend(compute_all_equal('SiH2N2', ['H','H','N','N'], angle_range))
    all_rows.extend(compute_all_equal('SiH2NSi', ['H','H','N','Si'], angle_range))

    # write CSV
    csv_path = '/app/outputs/V_theta_curves.csv'
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['site_type','mean_angle_deg','V_theta','bond'])
        writer.writeheader()
        writer.writerows(all_rows)

    # compute minima from rows
    site_groups = defaultdict(list)
    for row in all_rows:
        site_groups[row['site_type']].append(row)
    minima = {}
    for st, rows_st in site_groups.items():
        # prefer Si-Si bond
        bond = 'Si-Si'
        cands = [r for r in rows_st if r['bond'] == bond]
        if not cands:
            cands = [r for r in rows_st if r['bond'] == 'Si-N']
        if not cands:
            cands = rows_st
        best = min(cands, key=lambda r: r['V_theta'])
        minima[st] = best['mean_angle_deg']

    json_path = '/app/outputs/minima.json'
    with open(json_path, 'w') as f:
        json.dump(minima, f, indent=2)

    print('Outputs written: V_theta_curves.csv, minima.json')

if __name__ == '__main__':
    main()