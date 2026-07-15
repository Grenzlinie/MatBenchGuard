import numpy as np
import sys

def compute_curve(Bx_max, K2, T, n_points=20):
    S = 2
    J = 1.0
    q = 4
    SS1 = S*(S+1)  # 6
    Nk = 60
    kx = np.linspace(0, np.pi, Nk)
    ky = np.linspace(0, np.pi, Nk)
    dk = np.pi/(Nk-1)
    KX, KY = np.meshgrid(kx, ky)
    gamma_k = 2*(np.cos(KX) + np.cos(KY))
    Bx_arr = np.linspace(0, Bx_max, n_points)
    results = []
    prev_moments = (2.0, 4.0, 8.0, 16.0)
    prev_theta = 0.01
    for Bx in Bx_arr:
        theta = prev_theta
        M1, M2, M3, M4 = prev_moments
        alpha = 0.5
        for outer in range(30):
            C = np.zeros(4)
            for ikx in range(Nk):
                for iky in range(Nk):
                    gk = gamma_k[iky, ikx]
                    B = Bx * np.sin(theta)
                    K2eff = K2 * (1 - 1.5 * np.sin(theta)**2)
                    G11 = M1 * J * (q - gk) + B
                    G12 = K2eff
                    G21 = -0.5 * J * gk * (6*M2 - 2*SS1)
                    G22 = J * q * M1 + B - K2eff
                    G23 = 2 * K2eff
                    coeff31 = 0.5*SS1 + (2*SS1-1)*M1 - 1.5*M2 - 4*M3
                    G31 = J * gk * coeff31
                    G33 = J * q * M1 + B - K2eff
                    G34 = 2 * K2eff
                    coeff41 = 0.5*SS1 + (2*SS1-0.5)*M1 + (3*SS1-2.5)*M2 - 4*M3 - 5*M4
                    G41 = J * gk * coeff41 - K2eff * 9/4
                    G42 = - K2eff * 9/4
                    G43 = K2eff * 7/2
                    G44 = J * q * M1 + B + 2 * K2eff
                    Gamma = np.array([
                        [G11, G12, 0, 0],
                        [G21, G22, G23, 0],
                        [G31, 0, G33, G34],
                        [G41, G42, G43, G44]
                    ])
                    A = np.array([
                        2*M1,
                        6*M2 - 2*SS1,
                        8*M3 + 3*M2 - (4*SS1-1)*M1 - SS1,
                        10*M4 + 8*M3 - (6*SS1-5)*M2 - (4*SS1-1)*M1 - SS1
                    ])
                    w, R = np.linalg.eig(Gamma)
                    w_real = np.real(w)
                    try:
                        L = np.linalg.inv(R)
                    except:
                        continue
                    beta = 1.0 / T
                    with np.errstate(over='ignore', invalid='ignore'):
                        occ = 1.0 / (np.exp(beta * w_real) - 1.0)
                    occ = np.where(np.isfinite(occ), occ, 0.0)
                    LA = L @ A
                    for j in range(4):
                        contrib = R[:, j] * occ[j] * LA[j]
                        C += np.real(contrib)
            factor = (dk**2) / (np.pi**2)
            C *= factor
            Mcoeff = np.array([
                [4, 6, 6, 4],
                [-12, -6, 6, 12],
                [12, 0, 6, 24],
                [-12, 0, 6, 48]
            ])
            p_vec = np.linalg.solve(Mcoeff, C)
            p0, p1, p2, p3 = p_vec
            p4 = 1 - (p0+p1+p2+p3)
            if p4 < 0: p4 = 0.0
            M1_new = -2*p0 - p1 + 0 + p3 + 2*p4
            M2_new = 4*p0 + p1 + 0 + p3 + 4*p4
            M3_new = -8*p0 - p1 + 0 + p3 + 8*p4
            M4_new = 16*p0 + p1 + 0 + p3 + 16*p4
            M1 = alpha*M1_new + (1-alpha)*M1
            M2 = alpha*M2_new + (1-alpha)*M2
            M3 = alpha*M3_new + (1-alpha)*M3
            M4 = alpha*M4_new + (1-alpha)*M4
            if Bx > 1e-6:
                if C[1] > 1e-12:
                    sin_theta = Bx * C[0] / (K2 * C[1])
                    sin_theta = np.clip(sin_theta, 0.0, 1.0)
                    theta_new = np.arcsin(sin_theta)
                else:
                    theta_new = theta
            else:
                theta_new = 0.0
            theta = alpha*theta_new + (1-alpha)*theta
        Sz = M1 * np.cos(theta)
        Sx = M1 * np.sin(theta)
        Sz_over_S = Sz / S
        Sx_over_S = Sx / S
        theta_norm = theta / (np.pi/2)
        results.append([Bx, Sz_over_S, Sx_over_S, theta_norm])
        prev_moments = (M1, M2, M3, M4)
        prev_theta = theta
    return results

if __name__ == "__main__":
    outfile = sys.argv[1]
    Bx_max = float(sys.argv[2])
    K2 = float(sys.argv[3])
    T = float(sys.argv[4])
    n_pts = int(sys.argv[5])
    data = compute_curve(Bx_max, K2, T, n_pts)
    with open(f"/app/outputs/{outfile}", "w") as f:
        f.write("B_x,Sz_over_S,Sx_over_S,theta_norm\n")
        for row in data:
            f.write(f"{row[0]:.6f},{row[1]:.6f},{row[2]:.6f},{row[3]:.6f}\n")
