import math

# Bond lengths and angles from paper Table 1 (MP2/6-311G(3df,2p))
d_N_Hc = 1.0037
d_N_Ht = 1.0010
d_C_N  = 1.3530
d_C_O  = 1.2095
d_C_H  = 1.1004

ang_N_C_O  = 124.81
ang_O_C_H  = 122.82
ang_C_N_Hc = 119.20
ang_C_N_Ht = 121.26

# Place atoms in xy-plane; C at origin, O along +x
C = (0.0, 0.0, 0.0)
O = (d_C_O, 0.0, 0.0)

# H on C: angle O-C-H = 122.82°, so from C-O direction (+x) the C-H direction is 180-122.82 = 57.18° (in plane)
theta_CH = math.radians(180.0 - ang_O_C_H)
H = (d_C_H * math.cos(theta_CH), d_C_H * math.sin(theta_CH), 0.0)

# N on C: angle N-C-O = 124.81°, direction from C to N is at that angle from +x
theta_CN = math.radians(ang_N_C_O)
N = (d_C_N * math.cos(theta_CN), d_C_N * math.sin(theta_CN), 0.0)

# Direction from N to C, normalized
v_NC = (C[0] - N[0], C[1] - N[1], 0.0)
norm_NC = math.hypot(v_NC[0], v_NC[1])
u_NC = (v_NC[0] / norm_NC, v_NC[1] / norm_NC, 0.0)

def rotate_2d(u, angle_deg):
    a = math.radians(angle_deg)
    cos_a = math.cos(a)
    sin_a = math.sin(a)
    return (u[0]*cos_a - u[1]*sin_a, u[0]*sin_a + u[1]*cos_a, 0.0)

# Hc (cis to O): rotate u_NC by +ang_C_N_Hc
v_Hc_dir = rotate_2d(u_NC, ang_C_N_Hc)
Hc = (N[0] + d_N_Hc * v_Hc_dir[0], N[1] + d_N_Hc * v_Hc_dir[1], 0.0)

# Ht (trans to O): rotate u_NC by -ang_C_N_Ht
v_Ht_dir = rotate_2d(u_NC, -ang_C_N_Ht)
Ht = (N[0] + d_N_Ht * v_Ht_dir[0], N[1] + d_N_Ht * v_Ht_dir[1], 0.0)

# Write XYZ
print("6")
print("formamide optimized geometry")
atoms = [
    ("C",  *C),
    ("O",  *O),
    ("N",  *N),
    ("H",  *H),
    ("H",  *Hc),
    ("H",  *Ht),
]
for sym, x, y, z in atoms:
    print(f"{sym:<2} {x:10.6f} {y:10.6f} {z:10.6f}")
