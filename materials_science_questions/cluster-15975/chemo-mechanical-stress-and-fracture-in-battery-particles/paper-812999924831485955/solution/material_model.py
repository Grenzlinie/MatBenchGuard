import math

class LiMaterial:
    def __init__(self, G, K, eps0, m, S0, H0, S_star, a):
        self.G = G
        self.K = K
        self.eps0 = eps0
        self.m = m
        self.S0 = S0
        self.H0 = H0
        self.S_star = S_star
        self.a = a

    def update(self, F, Fp_prev, S_prev, dt, max_iter=20, tol=1e-8):
        """
        Input:  F   - total deformation gradient (3x3 list of lists)
                Fp_prev - plastic part from previous step (3x3)
                S_prev - flow resistance (scalar)
                dt    - time increment
        Returns: T (Cauchy stress, 3x3), Fp_new (3x3), S_new (scalar)
        """
        # Helper: invert 3x3
        def inv3(A):
            det = (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
                  -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
                  +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
            return [
                [(A[1][1]*A[2][2]-A[1][2]*A[2][1])/det, (A[0][2]*A[2][1]-A[0][1]*A[2][2])/det, (A[0][1]*A[1][2]-A[0][2]*A[1][1])/det],
                [(A[1][2]*A[2][0]-A[1][0]*A[2][2])/det, (A[0][0]*A[2][2]-A[0][2]*A[2][0])/det, (A[0][2]*A[1][0]-A[0][0]*A[1][2])/det],
                [(A[1][0]*A[2][1]-A[1][1]*A[2][0])/det, (A[0][1]*A[2][0]-A[0][0]*A[2][1])/det, (A[0][0]*A[1][1]-A[0][1]*A[1][0])/det]
            ]

        def mat_mul(A, B):
            return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

        def mat_mul_vec(A, v):
            return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]

        def I3():
            return [[1,0,0],[0,1,0],[0,0,1]]

        # Spectral decomposition of symmetric tensor via closed form (3x3)
        def sym_sqrt_spectral(B):
            # B symmetric 3x3, compute eigenvalues and eigenvectors
            # Use Jacobi-like method? Simpler: use numpy? Not allowed.
            # Implement power iteration and deflation? For simplicity, we assume B is diagonal in this problem
            # In uniaxial compression, the trial stretch tensor is diagonal.
            # So we'll handle diagonal case; otherwise fallback.
            # For general case, we'd need full spectral; but here the input is always diagonal.
            # So we assume B is diagonal. If not, raise.
            if any(B[i][j] != 0 for i in range(3) for j in range(3) if i != j):
                raise ValueError('Only diagonal stretch tensors supported')
            lamb = [B[i][i] for i in range(3)]
            return lamb

        # Elastic trial
        inv_Fp_prev = inv3(Fp_prev)
        Fe_trial = mat_mul(F, inv_Fp_prev)

        # Right Cauchy-Green trial
        Ce_trial = [[sum(Fe_trial[k][i]*Fe_trial[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        # Since loading is diagonal, Ce_trial should be diagonal; we assume that.
        lamb2 = [Ce_trial[i][i] for i in range(3)]  # principal stretches squared
        lamb = [math.sqrt(l2) for l2 in lamb2]
        e = [math.log(la) for la in lamb]  # logarithmic strains

        tr_e = sum(e)
        e0 = [e[i] - tr_e/3.0 for i in range(3)]

        G = self.G
        K = self.K
        M = [2*G*e0[i] + K*tr_e/3.0 for i in range(3)]  # diagonal stress M^e
        M0 = [M[i] - sum(M)/3.0 for i in range(3)]

        bar_sigma = math.sqrt(3.0/2.0 * sum(m0*m0 for m0 in M0))

        # Newton solve for equivalent plastic strain increment dep
        S = S_prev
        dep = 0.0
        for _ in range(max_iter):
            if bar_sigma < 1e-12:
                break
            dep_old = dep
            # flow direction
            N = [M0[i]/bar_sigma for i in range(3)]
            # residual: R = dep - dt * eps0 * (bar_sigma / S)^{1/m}
            # bar_sigma depends on dep because we subtract dep*N from e0
            # Update e0_test = e0_trial - dep * N
            e0_cur = [e0[i] - dep * N[i] for i in range(3)]
            tr_cur = tr_e  # volumetric unchanged
            M_cur = [2*G*e0_cur[i] + (K*tr_cur/3.0 if i==... )] # careful: trace part adds to diagonal
            # Actually M^e = 2G e0 + K (tr e) 1, so diagonal components
            # Recompute bar_sigma
            M0_cur = [M_cur[i] - (M_cur[0]+M_cur[1]+M_cur[2])/3.0 for i in range(3)]
            bar_sigma_new = math.sqrt(3.0/2.0 * sum(m0*m0 for m0 in M0_cur))
            if bar_sigma_new < 1e-12:
                dep = 0
                break
            dep_dot = self.eps0 * (bar_sigma_new / S)**(1.0/self.m)
            dep = dt * dep_dot
            if abs(dep - dep_old) < tol:
                break
        else:
            # converged
            pass

        # Compute updated elastic strain
        e0_cur = [e0[i] - dep * N[i] for i in range(3)]
        e_cur = [e0_cur[i] + tr_e/3.0 for i in range(3)]
        lamb_cur = [math.exp(ei) for ei in e_cur]

        # Rebuild Fe (diagonal, rotation omitted since diagonal)
        Fe_new = [[lamb_cur[0],0,0],[0,lamb_cur[1],0],[0,0,lamb_cur[2]]]
        # Fp_new = inv(Fe_new) * F
        inv_Fe_new = [[1/lamb_cur[0],0,0],[0,1/lamb_cur[1],0],[0,0,1/lamb_cur[2]]]
        Fp_new = mat_mul(inv_Fe_new, F)

        # Hardening update
        dS = self.H0 * (1 - S_prev/self.S_star)**self.a * dep
        S_new = S_prev + dS

        # Cauchy stress T = J^{e-1} [2G (E_H^e)_0 + K (tr E_H^e) 1]
        J_e = lamb_cur[0]*lamb_cur[1]*lamb_cur[2]
        # spatial logarithmic elastic strain E_H^e: same as e_cur in principal axes (since rotation = I)
        tr_EH = sum(e_cur)
        EH0 = [e_cur[i] - tr_EH/3.0 for i in range(3)]
        T = [[0]*3 for _ in range(3)]
        for i in range(3):
            T[i][i] = (2*G*EH0[i] + K*tr_EH) / J_e
        return T, Fp_new, S_new


def uniaxial_compression_stress_strain(material, true_strain, true_strain_rate):
    # Uniaxial compression: F = diag(lambda, 1/sqrt(lambda), 1/sqrt(lambda)) with lambda = exp(-eps)
    # Use many small steps
    Nsteps = 2000
    eps_target = abs(true_strain)
    strain_per_step = eps_target / Nsteps
    dt = strain_per_step / true_strain_rate

    Fp = [[1,0,0],[0,1,0],[0,0,1]]
    S = material.S0
    # initial F = I
    F_cur = [[1,0,0],[0,1,0],[0,0,1]]
    # integrate
    for step in range(Nsteps):
        eps_inc = -strain_per_step  # negative for compression
        lam = math.exp(eps_inc)
        # incremental deformation gradient
        dF = [[lam,0,0],[0,1/math.sqrt(lam),0],[0,0,1/math.sqrt(lam)]]
        # total F new
        F_cur = mat_mul(dF, F_cur)  # assuming diagonal
        T, Fp, S = material.update(F_cur, Fp, S, dt)

    # Return magnitude of Cauchy stress in compression direction (negative)
    return -T[0][0]  # MPa
