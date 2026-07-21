import csv, math

def main():
    # material constants (SI)
    c44 = 5.0e10
    R   = 1.2e9
    K   = 3.0e8
    e15 = -0.138
    e15p = -0.160   # e15'
    eps11 = 82.6e-12
    rho = 5.1e3

    # piezoelectrically stiffened moduli
    c44_bar = c44 + e15*e15/eps11
    K_bar   = K   + e15p*e15p/eps11
    R_bar   = R   + e15*e15p/eps11

    # alpha, epsilon1, epsilon2
    delta_sq = (c44_bar - K_bar)**2 + 4*R_bar*R_bar
    sqrt_delta = math.sqrt(delta_sq)
    alpha   = (c44_bar - K_bar + sqrt_delta) / 2.0
    eps1    = (c44_bar + K_bar + sqrt_delta) / 2.0
    eps2    = (c44_bar + K_bar - sqrt_delta) / 2.0

    # wave speeds
    s1 = math.sqrt(eps1/rho)
    s2 = math.sqrt(eps2/rho)

    # common denominator for Lambda1-Lambda8
    denom = (alpha*alpha + R_bar*R_bar) * (c44_bar*K_bar - R_bar*R_bar)

    # Λ1, Λ2 (dimensionless)
    Lambda1 = ( (c44_bar*alpha + R_bar*R_bar) * (alpha*K_bar - R_bar*R_bar) ) / denom
    Lambda2 = ( R_bar*R_bar * (c44_bar - alpha) * (alpha + K_bar) ) / denom

    # speeds to evaluate
    speeds = [
        ("v0",  0.0),
        ("v99", 0.99 * s2)
    ]

    # precompute beta values for each speed
    beta_cache = {}
    for label, v in speeds:
        beta1 = math.sqrt(1.0 - (v/s1)**2) if v < s1 else 0.0
        beta2 = math.sqrt(1.0 - (v/s2)**2) if v < s2 else 0.0
        beta_cache[label] = (beta1, beta2)

    # output rows
    rows = []
    for deg in range(0, 181):
        psi = math.radians(deg)
        sp = math.sin(psi)
        cp = math.cos(psi)

        # stationary case: cos(psi/2)
        stat = math.cos(psi/2.0)

        # scaled_stress_v0: v=0 -> beta1=beta2=1, Δ=1, C1=C2=cos(ψ/2)
        # the bracket is (Λ1+Λ2)*cos(ψ/2) = cos(ψ/2)
        scaled_v0 = 1e5 * math.cos(psi/2.0)

        # scaled_stress_v99
        b1, b2 = beta_cache["v99"]

        # helper for each k
        def compute_k_term(k, Lam):
            # Δ_k
            D = (cp*cp + k*k*sp*sp) ** 0.25
            # Φ_k with quadrant adjustment
            if abs(cp) < 1e-15:   # psi = 90° or 270°
                phi = math.pi/2.0
            else:
                tan_val = sp / cp
                raw = math.atan(k * tan_val)
                if psi > math.pi/2.0:
                    phi = raw + math.pi
                else:
                    phi = raw
            # C_k
            Ck = (1.0/k) * math.sin(phi/2.0) * sp + math.cos(phi/2.0) * cp
            return Lam / D * Ck

        term1 = compute_k_term(b1, Lambda1)
        term2 = compute_k_term(b2, Lambda2)
        scaled_v99 = 1e5 * (term1 + term2)

        rows.append([deg, scaled_v0, scaled_v99, stat])

    # write CSV
    with open("/app/outputs/scaled_stress.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["psi_deg", "scaled_stress_v0", "scaled_stress_v99", "scaled_stress_stationary"])
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    main()