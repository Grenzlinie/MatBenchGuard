import csv
import math

a = 1.025
b = -0.247e-3
c = 0.395e-6
d_param = -11550.0

cp_solid2 = 1.689
cp_liquid = 1.187
T_ref = 298.0
T_trans = 1424.0
T_fus = 1695.0
delta_H_tr = 13.2
delta_H_fus = 393.0

def integ_solid1(T1, T2):
    if T1 == T2:
        return (0.0, 0.0)
    delta_H = (a*(T2 - T1) 
               + (b/2.0)*(T2**2 - T1**2) 
               + (c/3.0)*(T2**3 - T1**3) 
               + d_param*(1.0/T1 - 1.0/T2))
    delta_S = (a*math.log(T2/T1) 
               + b*(T2 - T1) 
               + (c/2.0)*(T2**2 - T1**2) 
               + d_param*(0.5/T1**2 - 0.5/T2**2))
    return (delta_H, delta_S)

def integ_const(cp, T1, T2):
    if T1 == T2:
        return (0.0, 0.0)
    delta_H = cp * (T2 - T1)
    delta_S = cp * math.log(T2/T1)
    return (delta_H, delta_S)

H_solid1_to1424, S_solid1_to1424 = integ_solid1(T_ref, T_trans)
H_solid2_to1695, S_solid2_to1695 = integ_const(cp_solid2, T_trans, T_fus)

points = [
    (298, 'start'),
    (400, 'solid1'),
    (500, 'solid1'),
    (600, 'solid1'),
    (700, 'solid1'),
    (800, 'solid1'),
    (900, 'solid1'),
    (1000, 'solid1'),
    (1100, 'solid1'),
    (1200, 'solid1'),
    (1300, 'solid1'),
    (1400, 'solid1'),
    (1424, 'pre_trans'),
    (1424, 'post_trans'),
    (1500, 'solid2'),
    (1600, 'solid2'),
    (1695, 'pre_fus'),
    (1695, 'post_fus'),
    (1700, 'liquid'),
    (1800, 'liquid'),
    (1900, 'liquid')
]

rows = []
for T, state in points:
    if state == 'start':
        cp_val = (a + b*T + c*T**2 + d_param/(T**2))
        H = 0.0
        S = 0.0
    elif state == 'solid1':
        cp_val = (a + b*T + c*T**2 + d_param/(T**2))
        H, S = integ_solid1(T_ref, T)
    elif state == 'pre_trans':
        cp_val = (a + b*T + c*T**2 + d_param/(T**2))
        H, S = integ_solid1(T_ref, T)
    elif state == 'post_trans':
        cp_val = cp_solid2
        H = H_solid1_to1424 + delta_H_tr
        S = S_solid1_to1424 + delta_H_tr / T_trans
    elif state == 'solid2':
        cp_val = cp_solid2
        H = H_solid1_to1424 + integ_const(cp_solid2, T_trans, T)[0] + delta_H_tr
        S = S_solid1_to1424 + integ_const(cp_solid2, T_trans, T)[1] + delta_H_tr / T_trans
    elif state == 'pre_fus':
        cp_val = cp_solid2
        H = H_solid1_to1424 + integ_const(cp_solid2, T_trans, T)[0] + delta_H_tr
        S = S_solid1_to1424 + integ_const(cp_solid2, T_trans, T)[1] + delta_H_tr / T_trans
    elif state == 'post_fus':
        cp_val = cp_liquid
        H = H_solid1_to1424 + H_solid2_to1695 + delta_H_tr + delta_H_fus
        S = (S_solid1_to1424 + S_solid2_to1695 + 
             delta_H_tr / T_trans + delta_H_fus / T_fus)
    elif state == 'liquid':
        cp_val = cp_liquid
        H = (H_solid1_to1424 + H_solid2_to1695 + 
             integ_const(cp_liquid, T_fus, T)[0] + delta_H_tr + delta_H_fus)
        S = (S_solid1_to1424 + S_solid2_to1695 + 
             integ_const(cp_liquid, T_fus, T)[1] + 
             delta_H_tr / T_trans + delta_H_fus / T_fus)
    rows.append([T, cp_val, H, S])

with open('/app/outputs/thermodynamic_functions_caf2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['T', 'cp', 'enthalpy_increment', 'entropy_increment'])
    for row in rows:
        writer.writerow(row)
