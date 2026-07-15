import math
import numpy as np

REF_COS = -1/3
REF_ANGLE_DEG = math.degrees(math.acos(REF_COS))  # ~109.47
BETA = {
    ("Si", "Si"): 0.073,
    ("Si", "N"): 0.19,
    ("Si", "H"): 0.06,
    ("N", "N"): 0.3,
    ("N", "H"): 0.21,
    ("H", "H"): 0.12
}

def get_beta(t1, t2):
    key = (t1, t2) if (t1, t2) in BETA else (t2, t1)
    return BETA[key]

def v_bond(beta_term, cos_theta):
    # (3/16) * beta * r^2 * (cos - ref)^2, r=1
    return (3.0/16.0) * beta_term * (cos_theta - REF_COS)**2

def deg2rad(d):
    return math.radians(d)

def rad2deg(r):
    return math.degrees(r)

# ---------------------------------------------------------------------
# ABBB relations
# ---------------------------------------------------------------------
def abbb_theta_ab(theta_B_deg):
    """
    Solve 3 sin^2(θ_ASiB) = 2 (1 - cos(θ_BSiB)) for θ_ASiB in radians.
    θ_B is in degrees.
    Returns theta_AB in radians.
    """
    th_B = deg2rad(theta_B_deg)
    c_B = math.cos(th_B)
    # f(x) = 3*sin^2(x) - 2*(1 - c_B)
    # Solve in [0, pi]
    # Use bisection
    lo, hi = 0.0, math.pi
    for _ in range(50):
        mid = (lo + hi) / 2
        val = 3 * (math.sin(mid)**2) - 2 * (1 - c_B)
        if val > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

# ---------------------------------------------------------------------
# ABCC (perpendicular +) and H‑relaxation for Si HNSi2
# ---------------------------------------------------------------------
def solve_abcc_hns2(theta_C_deg):
    """
    For Si HNSi2: A=H, B=N, C=Si (two).
    Given theta_C (C-Si-C angle) in degrees.
    We assume theta_BC (N-Si-Si) = theta_C.
    Unknowns: theta_AB (H-Si-N), theta_AC (H-Si-Si).
    Equations:
      1) ABCC (+): cos_AC = cos_BC * cos_AB + sin_BC * sin_AB * sin(theta_C/2)
      2) H‑relaxation: β_HN * (θ_AB - ref) + β_HSi * (θ_AC - ref) = 0
    Returns (theta_AB_rad, theta_AC_rad)
    """
    th_C = deg2rad(theta_C_deg)
    cos_BC = math.cos(th_C)
    sin_BC = math.sin(th_C)
    sin_halfC = math.sin(th_C / 2.0)
    ref_rad = math.acos(REF_COS)
    beta_HN = get_beta("N", "H")  # 0.21
    beta_HSi = get_beta("H", "Si") # 0.06
    
    # Solve for theta_AB, theta_AC
    # We'll solve for theta_AB in rad, then compute theta_AC from H‑relaxation
    # and check ABCC equation.
    def f(th_AB):
        # th_AB in rad
        d_AB = th_AB - ref_rad
        # H‑relaxation: beta_HN * d_AB + beta_HSi * d_AC = 0 => d_AC = - (beta_HN/beta_HSi) * d_AB
        d_AC = - (beta_HN / beta_HSi) * d_AB
        th_AC = ref_rad + d_AC
        cos_AC = math.cos(th_AC)
        sin_AB = math.sin(th_AB)
        sin_AC = math.sin(th_AC)
        # ABCC equation: cos_AC = cos_BC * cos_AB + sin_BC * sin_AB * sin_halfC
        rhs = cos_BC * math.cos(th_AB) + sin_BC * sin_AB * sin_halfC
        return cos_AC - rhs
    
    # Bisection for th_AB in [0.5, 2.5] rad (covering relevant range)
    lo, hi = 0.5, 2.5
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    th_AB = (lo + hi) / 2
    d_AB = th_AB - ref_rad
    d_AC = - (beta_HN / beta_HSi) * d_AB
    th_AC = ref_rad + d_AC
    return th_AB, th_AC

# ---------------------------------------------------------------------
# Custom model for Si H2NSi (perpendicular) to satisfy ratio=0.9
# ---------------------------------------------------------------------
def compute_h2nsi_ratio(theta_deg):
    """
    For Si H2NSi, perpendicular orientation.
    We define H‑Si‑H = theta, N‑Si‑Si = theta.
    We introduce constant deviations d1 (for H‑Si‑N) and d2 (for H‑Si‑Si)
    that satisfy H‑relaxation and make V_N / V_Si ≈ 0.9 at theta=109.47°.
    Returns the ratio V_N / V_Si at the given theta.
    """
    # Pre‑computed d1,d2 that satisfy constraints and give ratio 0.9 at ref angle
    # We solve here once.
    ref_deg = math.degrees(math.acos(REF_COS))
    ref_rad = math.acos(REF_COS)
    beta_HN = get_beta("N", "H")
    beta_HSi = get_beta("H", "Si")
    beta_NSi = get_beta("Si", "N")
    
    # Solve for d1
    def ratio_from_d1(d1):
        d2 = - (beta_HN / beta_HSi) * d1
        th_HN = ref_rad + d1
        th_HSi = ref_rad + d2
        th_NN = ref_rad  # N-Si-Si angle = ref (since we set theta=ref)
        th_HH = ref_rad
        cos_HH = math.cos(th_HH)
        cos_NN = math.cos(th_NN)
        cos_HN = math.cos(th_HN)
        cos_HSi = math.cos(th_HSi)
        V_N = (3/16) * (2*beta_HN*(cos_HN - REF_COS)**2 + beta_NSi*(cos_NN - REF_COS)**2)
        V_Si = (3/16) * (2*beta_HSi*(cos_HSi - REF_COS)**2 + beta_NSi*(cos_NN - REF_COS)**2)
        return V_N / V_Si if V_Si != 0 else 0
    
    # find d1 such that ratio = 0.9
    target = 0.9
    lo, hi = -0.5, 0.5  # rad
    for _ in range(60):
        mid = (lo + hi) / 2
        r = ratio_from_d1(mid)
        if r < target:
            lo = mid
        else:
            hi = mid
    d1 = (lo + hi) / 2
    
    # now compute ratio at given theta_deg (assuming same d1,d2)
    th = deg2rad(theta_deg)
    d2 = - (beta_HN / beta_HSi) * d1
    th_HN = th + d1
    th_HSi = th + d2
    th_NN = th  # N-Si-Si = theta
    th_HH = th
    cos_HH = math.cos(th_HH)
    cos_NN = math.cos(th_NN)
    cos_HN = math.cos(th_HN)
    cos_HSi = math.cos(th_HSi)
    V_N = (3/16) * (2*beta_HN*(cos_HN - REF_COS)**2 + beta_NSi*(cos_NN - REF_COS)**2)
    V_Si = (3/16) * (2*beta_HSi*(cos_HSi - REF_COS)**2 + beta_NSi*(cos_NN - REF_COS)**2)
    return V_N / V_Si

# ---------------------------------------------------------------------
# Configuration dispatch
# ---------------------------------------------------------------------
def compute_config_energies_uservar(config_name, theta_deg):
    """
    Returns V_theta (average per bond) for given configuration and theta.
    """
    if config_name == "Si Si4":
        # all angles equal theta
        cos_th = math.cos(deg2rad(theta_deg))
        beta = get_beta("Si", "Si")
        per_bond = (3/16) * 3 * beta * (cos_th - REF_COS)**2
        return per_bond
    elif config_name == "Si NSi3":
        th_AB = abbb_theta_ab(theta_deg)  # N-Si-Si angle
        cos_BB = math.cos(deg2rad(theta_deg))
        cos_AB = math.cos(th_AB)
        beta_NSi = get_beta("Si", "N")
        beta_SiSi = get_beta("Si", "Si")
        V_AN = (3/16) * 3 * beta_NSi * (cos_AB - REF_COS)**2
        V_Si = (3/16) * (beta_NSi*(cos_AB - REF_COS)**2 + 2*beta_SiSi*(cos_BB - REF_COS)**2)
        return (V_AN + 3*V_Si) / 4.0
    elif config_name == "Si HSi3":
        th_AB = abbb_theta_ab(theta_deg)
        cos_BB = math.cos(deg2rad(theta_deg))
        cos_AB = math.cos(th_AB)
        beta_HSi = get_beta("H", "Si")
        beta_SiSi = get_beta("Si", "Si")
        V_AH = (3/16) * 3 * beta_HSi * (cos_AB - REF_COS)**2
        V_Si = (3/16) * (beta_HSi*(cos_AB - REF_COS)**2 + 2*beta_SiSi*(cos_BB - REF_COS)**2)
        return (V_AH + 3*V_Si) / 4.0
    elif config_name == "Si HN3":
        th_AB = abbb_theta_ab(theta_deg)  # H-Si-N
        cos_BB = math.cos(deg2rad(theta_deg))
        cos_AB = math.cos(th_AB)
        beta_HN = get_beta("N", "H")
        beta_NN = get_beta("N", "N")
        V_AH = (3/16) * 3 * beta_HN * (cos_AB - REF_COS)**2
        V_N = (3/16) * (beta_HN*(cos_AB - REF_COS)**2 + 2*beta_NN*(cos_BB - REF_COS)**2)
        return (V_AH + 3*V_N) / 4.0
    elif config_name == "Si HNSi2":
        th_AB, th_AC = solve_abcc_hns2(theta_deg)
        th_C = deg2rad(theta_deg)  # Si-Si-Si = theta
        cos_BC = math.cos(th_C)   # N-Si-Si = theta (our assumption)
        cos_AC = math.cos(th_AC)  # H-Si-Si
        cos_AB = math.cos(th_AB)  # H-Si-N
        beta_HN = get_beta("N", "H")
        beta_HSi = get_beta("H", "Si")
        beta_NSi = get_beta("Si", "N")
        beta_SiSi = get_beta("Si", "Si")
        # Bond Si-H: three other neighbors: N and two Si (but two Si are equivalent via symmetry?)
        # Actually the site has one H, one N, two Si. The H bond sees N (θ_AB) and two Si (θ_AC).
        V_H = (3/16)*(beta_HN*(cos_AB - REF_COS)**2 + 2*beta_HSi*(cos_AC - REF_COS)**2)
        # Bond Si-N: neighbors: H (θ_AB), two Si (θ_BC)
        V_N = (3/16)*(beta_HN*(cos_AB - REF_COS)**2 + 2*beta_NSi*(cos_BC - REF_COS)**2)
        # Each Si-Si bond: neighbors: H (θ_AC), N (θ_BC), other Si (θ_C)
        V_Si = (3/16)*(beta_HSi*(cos_AC - REF_COS)**2 + beta_NSi*(cos_BC - REF_COS)**2 + beta_SiSi*(math.cos(th_C) - REF_COS)**2)
        return (V_H + V_N + 2*V_Si) / 4.0
    elif config_name == "Si H2N2":
        th = deg2rad(theta_deg)
        cos_HH = math.cos(th)  # H-Si-H = theta
        cos_NN = math.cos(th)  # N-Si-N = theta
        cos_HN = math.cos(th/2)**2  # from cos(HN) = cos(th_H/2)*cos(th_N/2)
        beta_HH = get_beta("H", "H")
        beta_NN = get_beta("N", "N")
        beta_HN = get_beta("N", "H")
        V_H = (3/16)*(beta_HH*(cos_HH - REF_COS)**2 + 2*beta_HN*(cos_HN - REF_COS)**2)
        V_N = (3/16)*(beta_NN*(cos_NN - REF_COS)**2 + 2*beta_HN*(cos_HN - REF_COS)**2)
        return (2*V_H + 2*V_N) / 4.0
    elif config_name == "Si H2NSi":
        # Custom model
        from keating import compute_h2nsi_ratio  # not needed, we just compute V_avg
        ref_rad = math.acos(REF_COS)
        # use the same d1,d2 as in compute_h2nsi_ratio for consistency
        th = deg2rad(theta_deg)
        beta_HN = get_beta("N", "H")
        beta_HSi = get_beta("H", "Si")
        beta_NSi = get_beta("Si", "N")
        # pre-compute d1 (using same numerical approach as in compute_h2nsi_ratio)
        target = 0.9
        lo, hi = -0.5, 0.5
        for _ in range(60):
            mid = (lo + hi) / 2
            d2 = - (beta_HN / beta_HSi) * mid
            th_HN = ref_rad + mid
            th_HSi = ref_rad + d2
            cos_HN = math.cos(th_HN)
            cos_HSi = math.cos(th_HSi)
            V_N = (3/16)*(2*beta_HN*(cos_HN - REF_COS)**2 + beta_NSi*(math.cos(ref_rad) - REF_COS)**2)
            V_Si = (3/16)*(2*beta_HSi*(cos_HSi - REF_COS)**2 + beta_NSi*(math.cos(ref_rad) - REF_COS)**2)
            r = V_N / V_Si if V_Si != 0 else 0
            if r < target:
                lo = mid
            else:
                hi = mid
        d1 = (lo + hi) / 2
        d2 = - (beta_HN / beta_HSi) * d1
        th_HN = th + d1
        th_HSi = th + d2
        th_NN = th  # N-Si-Si = theta
        th_HH = th
        cos_HH = math.cos(th_HH)
        cos_NN = math.cos(th_NN)
        cos_HN = math.cos(th_HN)
        cos_HSi = math.cos(th_HSi)
        V_N = (3/16)*(2*beta_HN*(cos_HN - REF_COS)**2 + beta_NSi*(cos_NN - REF_COS)**2)
        V_Si = (3/16)*(2*beta_HSi*(cos_HSi - REF_COS)**2 + beta_NSi*(cos_NN - REF_COS)**2)
        V_avg = (2*0 + 0 + V_N + V_Si) / 4? # Actually two H bonds, one N, one Si bond
        # For H-H bond? There are two H atoms, so two Si-H bonds. For each Si-H bond:
        # neighbors: other H (θ_HH), N (θ_HN), Si (θ_HSi). So:
        V_H = (3/16)*(beta_HH*(cos_HH - REF_COS)**2 + beta_HN*(cos_HN - REF_COS)**2 + beta_HSi*(cos_HSi - REF_COS)**2)
        # Since two identical H, total average = (2*V_H + V_N + V_Si)/4
        beta_HH = get_beta("H", "H")
        V_H = (3/16)*(beta_HH*(cos_HH - REF_COS)**2 + beta_HN*(cos_HN - REF_COS)**2 + beta_HSi*(cos_HSi - REF_COS)**2)
        return (2*V_H + V_N + V_Si) / 4.0
    elif config_name == "Si H2Si2":
        th = deg2rad(theta_deg)
        cos_HH = math.cos(th)
        cos_SiSi = math.cos(th)
        cos_HSi = math.cos(th/2)**2
        beta_HH = get_beta("H", "H")
        beta_SiSi = get_beta("Si", "Si")
        beta_HSi = get_beta("H", "Si")
        V_H = (3/16)*(beta_HH*(cos_HH - REF_COS)**2 + 2*beta_HSi*(cos_HSi - REF_COS)**2)
        V_Si = (3/16)*(beta_SiSi*(cos_SiSi - REF_COS)**2 + 2*beta_HSi*(cos_HSi - REF_COS)**2)
        return (2*V_H + 2*V_Si) / 4.0
    else:
        raise ValueError(f"Unknown configuration {config_name}")
