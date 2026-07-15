import sys, math

pi = math.pi
omega_Eu = 2*pi*24.42       # rad/ps, from paper Table S2
gamma_Eu = 0.5              # 1/ps (damping, chosen to give realistic ringdown)
tau = 0.2548                # ps (FWHM 600 fs) 
eps0c = 2.6544e-3           # J/(V^2 m^2) for V/m field (eps0*c)
Z_star = 1.0                # effective charge taken as 1 (absorbed into scaling)

def fluence_to_E0(F_mJcm2, scale):
    F_SI = F_mJcm2 * 10.0   # 1 mJ/cm^2 = 10 J/m^2
    E0 = math.sqrt(F_SI / (eps0c * math.sqrt(pi) * tau))
    return E0 * scale

def solve_single(scale, fluence, helicity, regime):
    """
    Solve ODEs for given parameters.
    regime: 'below' or 'above'
    helicity: 'right' or 'left'
    Returns (ts, QAs) lists.
    """
    dt = 0.002   # ps
    t_start = -5.0
    t_end = 10.0
    n_steps = int((t_end - t_start) / dt)
    
    # state: [Qx, vx, Qy, vy, QA, vA]
    if regime == 'below':
        state = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0]   # start in A+ well
    else:
        state = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   # para-axial
    
    E0 = fluence_to_E0(fluence, scale)
    sign = 1.0 if helicity == 'right' else -1.0  # defines rotation direction
    
    def derivatives(s, t):
        Qx, vx, Qy, vy, QA, vA = s
        env = math.exp(-0.5 * (t / tau)**2)
        cos_wt = math.cos(omega_Eu * t)
        sin_wt = math.sin(omega_Eu * t)
        Ex = E0 * env * cos_wt
        Ey = E0 * env * sin_wt * sign   # sign flips for opposite helicity
        # driven phonon equations
        ax = -gamma_Eu * vx - omega_Eu**2 * Qx + Z_star * Ex
        ay = -gamma_Eu * vy - omega_Eu**2 * Qy + Z_star * Ey
        # axial order parameter
        if regime == 'below':
            # double well U = b Q^4 - a Q^2, a=0.4, b=0.2
            dU = 0.8 * QA**3 - 0.8 * QA
        else:
            # harmonic above Tc: U = 0.5 * omega^2 * Q^2, omega=0.5 rad/ps
            dU = 0.25 * QA          # omega^2=0.25
        coupling = 0.026 * (Qx * Ey - Qy * Ex)   # alpha*(Q x E)_z
        aA = -0.2 * vA - dU + coupling   # gamma_A=0.2 chosen
        return [vx, ax, vy, ay, vA, aA]
    
    ts = []
    QAs = []
    t = t_start
    for _ in range(n_steps + 1):
        ts.append(t)
        QAs.append(state[4])
        # RK4 step
        k1 = [dt * f for f in derivatives(state, t)]
        s2 = [s + 0.5*k for s, k in zip(state, k1)]
        k2 = [dt * f for f in derivatives(s2, t + 0.5*dt)]
        s3 = [s + 0.5*k for s, k in zip(state, k2)]
        k3 = [dt * f for f in derivatives(s3, t + 0.5*dt)]
        s4 = [s + k for s, k in zip(state, k3)]
        k4 = [dt * f for f in derivatives(s4, t + dt)]
        for i in range(6):
            state[i] = state[i] + (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6.0
        t += dt
    return ts, QAs

def switched(scale, fluence, regime='below', helicity='right'):
    _, QAs = solve_single(scale, fluence, helicity, regime)
    # check final value at t_end
    return QAs[-1] < -0.5   # switched if deeply negative

def threshold_fluence(scale):
    """Find smallest fluence that switches, with 0.1 resolution."""
    lo, hi = 0.0, 30.0
    if not switched(scale, hi):
        return float('inf')
    for _ in range(30):   # binary search
        mid = (lo + hi) / 2.0
        if switched(scale, mid):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0

def calibrate_scale():
    """Find scale so that threshold fluence = 14.0."""
    s_lo, s_hi = 0.1, 10.0
    # find bracket where target is crossed
    f_lo = threshold_fluence(s_lo) - 14.0
    f_hi = threshold_fluence(s_hi) - 14.0
    while f_lo * f_hi > 0:
        if f_lo < 0:
            s_lo = s_hi
            s_hi *= 2.0
        else:
            s_hi = s_lo
            s_lo /= 2.0
        f_lo = threshold_fluence(s_lo) - 14.0
        f_hi = threshold_fluence(s_hi) - 14.0
    # bisection
    for _ in range(20):
        mid = (s_lo + s_hi) / 2.0
        f_mid = threshold_fluence(mid) - 14.0
        if f_mid > 0:
            s_hi = mid
        else:
            s_lo = mid
    return (s_lo + s_hi) / 2.0

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "below":
        scale = calibrate_scale()
        fluences = [0.0, 5.0, 10.0, 12.5, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 20.0]
        # output CSV: Q_A,fluence_mJcm2,time_ps (matching scaffold order)
        print("Q_A,fluence_mJcm2,time_ps")
        for fluence in fluences:
            ts, QAs = solve_single(scale, fluence, 'right', 'below')
            for t, qa in zip(ts, QAs):
                # sample every 0.1 ps for smaller file
                if abs(t - round(t * 10) / 10) < 0.0001:
                    print(f"{qa:.6f},{fluence:.2f},{t:.6f}")
    elif mode == "above":
        # use same scale as below (the physical conversion) to keep consistency
        scale = calibrate_scale()
        fluence = 6.0
        print("Q_A,helicity,time_ps")
        for helicity in ["right", "left"]:
            ts, QAs = solve_single(scale, fluence, helicity, 'above')
            for t, qa in zip(ts, QAs):
                if abs(t - round(t * 10) / 10) < 0.0001:
                    print(f"{qa:.6f},{helicity},{t:.6f}")
