import numpy as np
from scipy.special import ellipk, ellipe
import csv
import os

# ----- Case 3 parameters (Table 1) -----
ALPHA_DEG = 0.0
BETA_DEG = 45.0
A0 = 0.1            # initial crack radius, m
SIGMAX = 92e6
SIGMAY = 92e6
SIGMAZ = 63e6
P = 80e6
NU = 0.25
INC = 0.01
N_STEPS = 20

# ----- helper trig -----
def sind(x): return np.sin(np.deg2rad(x))
def cosd(x): return np.cos(np.deg2rad(x))
def tand(x): return np.tan(np.deg2rad(x))
def arctand(x): return np.rad2deg(np.arctan(x))

# ----- stress resolution on a plane given dip_dir (alpha) and dip_angle (beta) -----
def stress_on_plane(alpha_deg, beta_deg):
    """Return sigma_n_eff, tau_eff, omega (rad), l_vec, m_vec, n_vec, tau_vec."""
    a = np.deg2rad(alpha_deg)
    b = np.deg2rad(beta_deg)
    # normal vector (Eq. 3)
    l = np.cos(np.pi/2 - b) * np.cos(a)
    m = np.cos(np.pi/2 - b) * np.sin(a)
    n = np.sin(b - np.pi/2)
    # external normal stress (Eq. 4)
    sigma_n_ext = SIGMAX*l*l + SIGMAY*m*m + SIGMAZ*n*n
    sigma_n_eff = P - sigma_n_ext   # Eq. (8)
    # shear stress magnitude (Eq. 4/9)
    tau = np.sqrt((SIGMAX*l)**2 + (SIGMAY*m)**2 + (SIGMAZ*n)**2 - sigma_n_ext**2)
    tau_eff = tau
    # shear direction (Eq. 5)
    l_tau = (SIGMAX - sigma_n_ext) * l / tau if tau > 1e-12 else 0.0
    m_tau = (SIGMAY - sigma_n_ext) * m / tau if tau > 1e-12 else 0.0
    n_tau = (SIGMAZ - sigma_n_ext) * n / tau if tau > 1e-12 else 0.0
    # projection of dip direction on the crack plane (Eq. 6)
    l_o = np.cos(b) * np.cos(a)
    m_o = np.cos(b) * np.sin(a)
    n_o = np.sin(b)
    # dot product
    dot = l_tau*l_o + m_tau*m_o + n_tau*n_o
    # clamp
    dot = max(-1.0, min(1.0, dot))
    omega = np.arccos(dot)  # rad, shear angle
    return sigma_n_eff, tau_eff, omega, (l,m,n), (l_tau,m_tau,n_tau), (l_o,m_o,n_o)

# ----- circular crack SIFs (Eq. 2) -----
def circular_sifs(varphi_rad, a, sigma_n_eff, tau_eff, omega):
    prefactor = 2 * np.sqrt(a/np.pi)
    KI = prefactor * sigma_n_eff
    den = 2.0 - NU
    KII = - (4.0 * np.cos(varphi_rad - omega) / den) * np.sqrt(a/np.pi) * tau_eff
    KIII = (4.0 * (1.0 - NU) * np.sin(varphi_rad - omega) / den) * np.sqrt(a/np.pi) * tau_eff
    return KI, KII, KIII

# ----- MTS critical angle (Eq. 12) -----
def mts_critical_angle(KI, KII):
    """Return theta_c in radians, ensuring tensile sigma_theta."""
    theta = np.zeros_like(KI)
    mask_zero = np.abs(KII) < 1e-15
    theta[mask_zero] = 0.0
    mask_nonzero = ~mask_zero
    if np.any(mask_nonzero):
        KI_nz = KI[mask_nonzero]
        KII_nz = KII[mask_nonzero]
        # two solutions
        arg1 = (KI_nz + np.sqrt(KI_nz**2 + 8*KII_nz**2)) / (4*KII_nz)
        arg2 = (KI_nz - np.sqrt(KI_nz**2 + 8*KII_nz**2)) / (4*KII_nz)
        th1 = 2 * np.arctan(arg1)
        th2 = 2 * np.arctan(arg2)
        # evaluate sigma_theta (omit denominator)
        st1 = np.cos(th1/2)**2 * (KI_nz * np.cos(th1/2) - 3*KII_nz * np.sin(th1/2))
        st2 = np.cos(th2/2)**2 * (KI_nz * np.cos(th2/2) - 3*KII_nz * np.sin(th2/2))
        # choose the one giving max tensile sigma_theta (most positive)
        theta_nz = np.where(st1 >= st2, th1, th2)
        theta[mask_nonzero] = theta_nz
    return theta

# ----- elliptical crack SIFs (Eq. 14) -----
def elliptical_sifs(varphi_rad, a, b, gamma, sigma_n_eff, tau_eff, omega):
    """
    varphi_rad: apparent angle measured from major axis of ellipse (rad)
    gamma: orientation of ellipse major axis relative to the dip direction projection (rad)
    All other inputs as described.
    """
    # compute ellipse parameters
    if a < b:
        # ensure a >= b
        a, b = b, a
        gamma = gamma + np.pi/2  # adjust orientation
    if b <= 0:
        b = 1e-12
    kprime = b / a
    k2 = 1 - kprime**2
    if k2 < 0:
        k2 = 0.0
    k = np.sqrt(k2)
    # elliptic integrals
    if k < 1e-12:
        # circular case: use limiting values
        Kk = np.pi/2
        Ek = np.pi/2
    else:
        Kk = ellipk(k2)
        Ek = ellipe(k2)
    B = (k2 - NU) * Ek + NU * kprime**2 * Kk
    C = (k2 + NU * kprime**2) * Ek - NU * kprime**2 * Kk
    # denominator for KI
    den_KI = Ek * np.sqrt(np.pi * b / a)  # careful: formula is sigma_n_eff / E(k) * sqrt(pi b / a) * [...]. We'll compute KI directly.
    # prefactor for KI
    KI_pre = sigma_n_eff / Ek * np.sqrt(np.pi * b / a)  # This is (sigma_n_eff/Ek) * sqrt(pi b/a)
    # KI = KI_pre * (a^2 sin^2(varphi) + b^2 cos^2(varphi))^{1/4}
    sin2 = a**2 * np.sin(varphi_rad)**2 + b**2 * np.cos(varphi_rad)**2
    KI_term = sin2**0.25
    KI = KI_pre * KI_term

    # KII and KIII
    pref = (tau_eff * k2 * np.sqrt(np.pi * a * b)) / (sin2**0.25)
    term1 = kprime / B * np.cos(omega) * np.cos(varphi_rad)
    term2 = 1.0 / C * np.sin(omega) * np.sin(varphi_rad)
    KII = -pref * (term1 + term2)

    term3 = 1.0 / B * np.cos(omega) * np.sin(varphi_rad)
    term4 = - kprime / C * np.sin(omega) * np.cos(varphi_rad)
    KIII = pref * (1.0 - NU) * (term3 + term4)

    return KI, KII, KIII

# ----- find phi_zero for elliptical crack (Eq. B.2) -----
def ellipse_phi_zero(a, b, gamma, omega, B, C, kprime):
    """Return phi_zero (rad) in [0, 2pi)."""
    den = B * np.tan(omega) if np.abs(B*np.tan(omega)) > 1e-15 else 0.0
    num = -kprime * C
    if np.abs(den) > 1e-15:
        phi0 = np.arctan2(num, den)
    else:
        if num >= 0:
            phi0 = np.pi/2
        else:
            phi0 = 3*np.pi/2
    # adjust quadrant: np.arctan2 returns in [-pi, pi]; ensure in [0, 2pi)
    if phi0 < 0:
        phi0 += 2*np.pi
    # There are two phi_zero 180 deg apart; return this one
    return phi0

# ----- actual angle on ellipse from apparent angle (Eq. B.1) -----
def actual_angle(varphi_rad, a, b):
    """Return varphi_actual (rad) in [0, 2pi)."""
    a_cos = a * np.cos(varphi_rad)
    b_sin = b * np.sin(varphi_rad)
    if np.abs(a_cos) < 1e-15:
        if b_sin >= 0:
            return np.pi/2
        else:
            return 3*np.pi/2
    phi_actual = np.arctan2(b_sin, a_cos)
    if phi_actual < 0:
        phi_actual += 2*np.pi
    return phi_actual

# ----- fit plane through origin to points in local (f,g,h) system -----
def fit_plane_local(f, g, h):
    """
    Given arrays f,g,h of points on the new crack front in the current local coords,
    find plane normal (a,b,c) passing through origin that best fits them (least-squares).
    Use SVD.
    """
    # points matrix [N x 3]
    pts = np.column_stack((f, g, h))
    # find plane via SVD of pts (center at origin already)
    U, s, Vt = np.linalg.svd(pts, full_matrices=False)
    # normal is the last row of Vt (singular vector with smallest singular value)
    normal = Vt[-1, :]
    # ensure a positive z component for consistent orientation
    if normal[2] < 0:
        normal = -normal
    return normal

# ----- transform local (f,g,h) to global coordinates given dip_dir, dip_angle (Eq. A.8) -----
def local_to_global(f, g, h, alpha_deg, beta_deg):
    a = np.deg2rad(alpha_deg)
    b = np.deg2rad(beta_deg)
    cb = np.cos(b)
    sb = np.sin(b)
    ca = np.cos(a)
    sa = np.sin(a)
    x = f * cb * ca - g * sa - h * ca * sb
    y = f * cb * sa + g * ca - h * sa * sb
    z = f * sb + h * cb
    return x, y, z

# ----- compute dip direction and dip angle from normal vector in global coords (Eqs. A.9, A.10) -----
def normal_to_dip(xn, yn, zn):
    norm_horiz = np.sqrt(xn**2 + yn**2)
    if norm_horiz < 1e-15:
        beta = 0.0 if zn >= 0 else 180.0
        alpha = 0.0
    else:
        beta = 90.0 - np.abs(np.arctan(zn / norm_horiz)) * 180.0/np.pi
        # dip direction
        if np.abs(xn) > 1e-15:
            alpha = np.arctan2(yn, xn) * 180.0/np.pi
            if alpha < 0:
                alpha += 360.0
        else:
            alpha = 90.0 if yn >= 0 else 270.0
    return alpha, beta

# ----- main functions for writing outputs -----
def write_sifs_initial_crack(outdir):
    alpha = ALPHA_DEG
    beta = BETA_DEG
    sigma_n_eff, tau_eff, omega, _, _, _ = stress_on_plane(alpha, beta)
    a = A0
    phi_deg = np.arange(0, 360, 10)
    phi_rad = np.deg2rad(phi_deg)
    KI, KII, KIII = circular_sifs(phi_rad, a, sigma_n_eff, tau_eff, omega)
    path = os.path.join(outdir, 'sifs_initial_crack.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['phi_deg', 'KI', 'KII', 'KIII'])
        for i, p in enumerate(phi_deg):
            writer.writerow([f"{p}", f"{KI[i]:.6e}", f"{KII[i]:.6e}", f"{KIII[i]:.6e}"])

def write_final_crack_front(outdir):
    # initial crack
    alpha = ALPHA_DEG
    beta = BETA_DEG
    a_ell = A0
    b_ell = A0
    gamma = 0.0  # ellipse orientation, arbitrary for circle
    # loop
    for step in range(1, N_STEPS+1):
        # effective stresses on current plane
        sigma_n_eff, tau_eff, omega, _, _, _ = stress_on_plane(alpha, beta)
        phi_deg = np.arange(0, 360, 10)
        phi_rad = np.deg2rad(phi_deg)

        if step == 1:
            # circular SIFs
            KI, KII, KIII = circular_sifs(phi_rad, a_ell, sigma_n_eff, tau_eff, omega)
            # phi_zero for circle (Eq. A.2): phi_zero = omega +/- 90 deg
            phi_zero_1 = omega - np.pi/2
            phi_zero_2 = omega + np.pi/2
            # take the one that yields positive phi if possible; difference is 180 deg, so we can use phi_zero_1
            phi_zero = phi_zero_1 if phi_zero_1 >= 0 else phi_zero_1 + 2*np.pi
            # phi_max = phi_zero +/- 90 deg
            phi_max = phi_zero + np.pi/2  # this is 90 deg from phi_zero
            if phi_max >= 2*np.pi:
                phi_max -= 2*np.pi
        else:
            # elliptical SIFs
            # compute elliptic integrals and constants
            if a_ell < b_ell:
                a_ell, b_ell = b_ell, a_ell
                gamma += np.pi/2
            kprime = b_ell / a_ell if a_ell > 0 else 1.0
            k2 = 1 - kprime**2
            if k2 < 0:
                k2 = 0.0
            k = np.sqrt(k2)
            if k < 1e-12:
                Kk = np.pi/2
                Ek = np.pi/2
            else:
                Kk = ellipk(k2)
                Ek = ellipe(k2)
            B = (k2 - NU) * Ek + NU * kprime**2 * Kk
            C = (k2 + NU * kprime**2) * Ek - NU * kprime**2 * Kk
            # SIFs
            KI, KII, KIII = elliptical_sifs(phi_rad, a_ell, b_ell, gamma, sigma_n_eff, tau_eff, omega)
            # phi_zero (Eq. B.2)
            phi_zero = ellipse_phi_zero(a_ell, b_ell, gamma, omega, B, C, kprime)
            # actual angle for phi_zero
            phi_zero_actual = actual_angle(phi_zero, a_ell, b_ell)
            # phi_max actual is 90 deg from phi_zero_actual
            phi_max_actual = phi_zero_actual + np.pi/2
            if phi_max_actual >= 2*np.pi:
                phi_max_actual -= 2*np.pi
            # we need the apparent angle corresponding to this actual angle
            # invert relationship: actual angle phi_a = arctan2(b sin(phi_app), a cos(phi_app))
            # tan(phi_a) = b sin(phi_app) / (a cos(phi_app)) = (b/a) tan(phi_app) => phi_app = arctan( (a/b) tan(phi_a) ) with quadrant corrections.
            # So from phi_max_actual, compute phi_max (apparent):
            if a_ell > 0 and b_ell > 0:
                tan_act = np.tan(phi_max_actual)
                phi_max_app = np.arctan2(a_ell * tan_act, b_ell)  # ? Actually tan(phi_app) = (a/b) tan(phi_act) because phi_act = arctan(b sin(phi_app)/(a cos(phi_app))) = arctan( (b/a) tan(phi_app) ). So tan(phi_act) = (b/a) tan(phi_app) => tan(phi_app) = (a/b) tan(phi_act). So phi_app = arctan2(a * sin(phi_act)/cos(phi_act)? Let's use arctan2.
                # Better: phi_act = arctan2(b*sin(phi_app), a*cos(phi_app)). So given phi_act, we need phi_app such that b*sin(phi_app) = R*sin(phi_act) and a*cos(phi_app) = R*cos(phi_act) for some R>0. Then tan(phi_act) = (b/a) tan(phi_app). So indeed phi_app = arctan( (a/b) tan(phi_act) ) with quadrant adjustments.
                phi_max = np.arctan2(a_ell * np.sin(phi_max_actual), b_ell * np.cos(phi_max_actual))
                if phi_max < 0:
                    phi_max += 2*np.pi
            else:
                phi_max = phi_max_actual

        # critical angles
        theta_c = mts_critical_angle(KI, KII)

        # get theta_c at phi_max (apparent)
        # find closest phi index
        idx_max = np.argmin(np.abs(phi_rad - phi_max % (2*np.pi)))
        theta_max = theta_c[idx_max]
        hmax = INC * np.sin(theta_max)
        length_at_max = (a_ell if step==1 else np.sqrt((a_ell*np.cos(phi_max))**2 + (b_ell*np.sin(phi_max))**2))  # approximate length for circle
        # Actually for circle, length at phi_max is just a0.
        if step == 1:
            length_at_max = a_ell
        else:
            length_at_max = np.sqrt((a_ell*np.cos(phi_max))**2 + (b_ell*np.sin(phi_max))**2)
        # slope (Eq. A.3) gives hmax/length_at_max, but we use h(varphi) directly from cos projection
        # h(varphi) = inc * sin(theta_max) * cos(phis - phi_max)   (Eq. A.4)
        h = INC * np.sin(theta_max) * np.cos(phi_rad - phi_max)

        # compute length(varphi)
        length = np.zeros_like(phi_rad)
        # base radius from current ellipse boundary in the direction of phi_actual
        if step == 1:
            base_radius = np.full_like(phi_rad, a_ell)  # circle
        else:
            # ellipse boundary distance from origin in local (f,g) along phi_actual
            # use Eq. B.4: first term sqrt([a cos(phi)cos(gamma)-b sin(phi)sin(gamma)]^2 + [a cos(phi)sin(gamma)+b sin(phi)cos(gamma)]^2)
            f_base = a_ell * np.cos(phi_rad) * np.cos(gamma) - b_ell * np.sin(phi_rad) * np.sin(gamma)
            g_base = a_ell * np.cos(phi_rad) * np.sin(gamma) + b_ell * np.sin(phi_rad) * np.cos(gamma)
            base_radius = np.sqrt(f_base**2 + g_base**2)

        # handle theta_c = 0
        zero_theta = np.abs(theta_c) < 1e-9
        length[zero_theta] = base_radius[zero_theta]  # no growth; stay on ellipse
        mask = ~zero_theta
        tan_tc = np.tan(theta_c[mask])
        # prevent division by small tan
        length[mask] = base_radius[mask] + h[mask] / tan_tc

        # radial distance R
        R = np.sqrt(length**2 + h**2)

        # fit ellipse: major/minor axes and orientation
        a_new = np.max(R)
        b_new = np.min(R)
        idx_max_R = np.argmax(R)
        gamma_new = phi_rad[idx_max_R]  # orientation of major axis relative to f-direction

        # compute local front points (f,g,h) using length and h (Eq. A.7/B.5 with actual angles)
        if step == 1:
            # actual angle = phi_rad since circle
            phi_actual_arr = phi_rad
        else:
            phi_actual_arr = np.array([actual_angle(p, a_ell, b_ell) for p in phi_rad])
        f_pts = length * np.cos(phi_actual_arr)
        g_pts = length * np.sin(phi_actual_arr)
        h_pts = h

        # fit plane to (f,g,h) in local system
        normal_local = fit_plane_local(f_pts, g_pts, h_pts)

        # transform normal to global coords using current plane orientation
        # current local to global transformation uses alpha, beta. We need to convert normal_local into global using the same rotation.
        # The local system (f,g,h) to global transformation matrix R_glob is given by Eq. A.8. So global normal = R_glob * normal_local
        # compute R_glob
        a_r = np.deg2rad(alpha)
        b_r = np.deg2rad(beta)
        cb = np.cos(b_r); sb = np.sin(b_r); ca = np.cos(a_r); sa = np.sin(a_r)
        M = np.array([
            [ cb*ca,  -sa,  -ca*sb ],
            [ cb*sa,   ca,  -sa*sb ],
            [ sb,       0,    cb ]
        ])
        normal_glob = M @ normal_local
        # normalize
        nrm = np.linalg.norm(normal_glob)
        if nrm > 1e-12:
            normal_glob = normal_glob / nrm
        # compute new dip direction and dip angle from normal_glob
        alpha_new, beta_new = normal_to_dip(normal_glob[0], normal_glob[1], normal_glob[2])

        # update for next step
        alpha = alpha_new
        beta = beta_new
        a_ell = a_new
        b_ell = b_new
        gamma = gamma_new

    # after loop, output final elliptical crack front at 36 apparent angles
    phi_deg_out = np.arange(0, 360, 10)
    phi_rad_out = np.deg2rad(phi_deg_out)
    # ellipse points in local plane (final fitted ellipse, not propagated points)
    f_final = a_ell * np.cos(phi_rad_out) * np.cos(gamma) - b_ell * np.sin(phi_rad_out) * np.sin(gamma)
    g_final = a_ell * np.cos(phi_rad_out) * np.sin(gamma) + b_ell * np.sin(phi_rad_out) * np.cos(gamma)
    h_final = np.zeros_like(f_final)

    # transform to global coords using final dip_dir, dip_angle
    x, y, z = local_to_global(f_final, g_final, h_final, alpha, beta)

    path = os.path.join(outdir, 'final_crack_front.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['phi_deg', 'x', 'y', 'z'])
        for i, p in enumerate(phi_deg_out):
            writer.writerow([f"{p}", f"{x[i]:.6f}", f"{y[i]:.6f}", f"{z[i]:.6f}"])
