import csv, math

R = 8.314e-3  # kJ/(mol K)
T = 873.0
Omega_FeAl = -23.1
Omega_FeCo = -16.6
Omega_AlCo = -31.9

# index mapping: 0:Fe, 1:Al, 2:Co
Omega = {
    (0,1): Omega_FeAl, (1,0): Omega_FeAl,
    (0,2): Omega_FeCo, (2,0): Omega_FeCo,
    (1,2): Omega_AlCo, (2,1): Omega_AlCo
}

T_c_Fe = 1043.0       # °T_c^m
T_c_ord_ref = 1003.0   # °T_c^o for FeCo B2

def G_para(x_Fe, x_Al, x_Co):
    # ideal mixing + regular solution
    S = 0.0
    for xi in (x_Fe, x_Al, x_Co):
        if xi > 0:
            S += xi * math.log(xi)
    G_id = R * T * S
    G_ex = (Omega[(0,1)]*x_Fe*x_Al + Omega[(0,2)]*x_Fe*x_Co +
            Omega[(1,2)]*x_Al*x_Co)
    return G_id + G_ex

def T_c_magn(x_Co, x_Al):
    # equation (4) exactly as given: minus sign included
    num = 1138.0 * x_Co + 370.0
    denom = (0.237 + 0.357 * math.sqrt((x_Co - 0.024)**2 + 0.028**2)) * x_Al**2 \
            + 1138.0 * x_Co + 1043.0
    return -num / denom

def G_mag_ref(temp):
    # equation (5)
    return 9.0 * (temp - 968.9 - math.sqrt((temp - 968.9)**2 + 28832.0)) / 2.0

def G_ferro(x_Fe, x_Al, x_Co):
    # equation (3) with m_i: Al=1, Fe=Co=0
    factor_m = 1.0 - x_Al
    Tcm = T_c_magn(x_Co, x_Al)
    if abs(Tcm) < 1e-12:
        return 0.0
    ratio = Tcm / T_c_Fe
    T_m_star = T * (T_c_Fe / Tcm)
    G_ref = G_mag_ref(T_m_star)
    return factor_m * ratio * G_ref

def T_c_ord(x_Fe, x_Al, x_Co):
    # equation (7)
    O12 = Omega_FeAl
    O23 = Omega_AlCo
    O31 = Omega_FeCo
    x1, x2, x3 = x_Fe, x_Al, x_Co
    term = O12*x1*x2 + O23*x2*x3 + O31*x3*x1
    L = (O12**2 + O23**2 + O31**2
         - 2*O12*O23 - 2*O23*O31 - 2*O31*O12)
    inside = term + L * x1 * x2 * x3
    if inside < 0:
        inside = 0.0   # safety, should be non-negative
    return (1.0 / R) * (-term + math.sqrt(inside))

def f_scaling(x_Fe, x_Al, x_Co):
    # equation (8), take the larger value
    vals = []
    if x_Co < x_Fe:
        vals.append(2.0 * x_Co)
    else:
        vals.append(2.0 * x_Fe)
    if x_Al < 0.5:
        vals.append(2.0 * x_Al)
    else:
        vals.append(2.0 * (1.0 - x_Al))
    return max(vals)

def G_ord_ref(temp):
    # equation (9)
    return 5.5 * (temp - 746.1 - math.sqrt((temp - 746.1)**2 + 50498.0)) / 2.0

def G_ord(x_Fe, x_Al, x_Co):
    f = f_scaling(x_Fe, x_Al, x_Co)
    Tc_ord = T_c_ord(x_Fe, x_Al, x_Co)
    if Tc_ord == 0:
        return 0.0
    ratio = Tc_ord / T_c_ord_ref
    T_o_star = T * (T_c_ord_ref / Tc_ord)
    G_ref = G_ord_ref(T_o_star)
    return f * ratio * G_ref

def total_G(x_Fe, x_Al, x_Co):
    return (G_para(x_Fe, x_Al, x_Co) +
            G_ferro(x_Fe, x_Al, x_Co) +
            G_ord(x_Fe, x_Al, x_Co))

def compute_binodal(X_Co_fixed, step=0.0002):
    max_Al = 1.0 - X_Co_fixed
    points = []
    x = 0.0
    while x <= max_Al + 1e-12:
        x_Al = x
        x_Fe = 1.0 - X_Co_fixed - x_Al
        if x_Fe < 0:
            break
        # safe values to avoid log(0)
        eps = 1e-12
        x_Fe_safe = max(eps, x_Fe)
        x_Al_safe = max(eps, x_Al)
        x_Co_safe = max(eps, X_Co_fixed) if X_Co_fixed > 0 else eps
        G = total_G(x_Fe_safe, x_Al_safe, x_Co_safe)
        points.append((x_Al, G))
        x += step
    # lower convex hull (monotonic chain, cross <= 0)
    points.sort(key=lambda p: p[0])
    lower = []
    for p in points:
        while len(lower) >= 2:
            p1 = lower[-2]
            p2 = lower[-1]
            cross = ((p2[0] - p1[0]) * (p[1] - p1[1])
                     - (p2[1] - p1[1]) * (p[0] - p1[0]))
            if cross <= 0:
                lower.pop()
            else:
                break
        lower.append(p)
    # binodal pair: consecutive hull points with largest x-difference
    max_dx = 0
    pair_idx = (0, 1)
    for i in range(len(lower) - 1):
        dx = lower[i+1][0] - lower[i][0]
        if dx > max_dx:
            max_dx = dx
            pair_idx = (i, i+1)
    x_Al_1 = lower[pair_idx[0]][0]
    x_Al_2 = lower[pair_idx[1]][0]
    return x_Al_1, x_Al_2

sections = [0.10, 0.15, 0.20, 0.25, 0.30]
rows = []
for X_Co in sections:
    a1, a2 = compute_binodal(X_Co)
    # B2 is the Al‑rich phase, B2* the Co‑rich (lower Al) phase
    if a1 > a2:
        B2_Al, B2star_Al = a1, a2
    else:
        B2_Al, B2star_Al = a2, a1
    for phase, x_Al in [('B2', B2_Al), ('B2*', B2star_Al)]:
        x_Fe = 1.0 - X_Co - x_Al
        rows.append([X_Co, phase, x_Fe, x_Al, X_Co])

with open('/app/outputs/phase_boundary.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['section_X_Co', 'phase', 'X_Fe', 'X_Al', 'X_Co'])
    for r in rows:
        w.writerow(r)
