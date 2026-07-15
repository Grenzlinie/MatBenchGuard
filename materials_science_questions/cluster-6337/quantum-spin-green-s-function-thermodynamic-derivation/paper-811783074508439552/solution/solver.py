#!/usr/bin/env python3
"""Hidden oracle: writes reference outputs for the 2D easy-plane ferromagnet."""
import sys, csv, os, math
import numpy as np
from scipy.special import kve  # modified Bessel K_nu, use kve(2,x) for K_2

def K2(x):
    # scipy.special.kn(2,x) returns K_2, but kve might be faster; use kn
    from scipy.special import kn
    return kn(2, x)

# ----------  lattice and model constants  ----------
S = 1
Z = 4
J = 1.0

# ----------  dipole-dipole Ewald sums for 2D square lattice  ----------
def compute_dipole(kx, ky, m_max=10, n_max=10):
    """Return p_xx, p_yy, p_zz for a single k-point using the Ewald series (42)-(43)."""
    q1_val = 0.0
    q2_val = 0.0
    for m in range(1, m_max+1):
        for n in range(-n_max, n_max+1):
            term_arg1 = 2.0 * m * abs(n * math.pi + ky/2.0)
            if term_arg1 < 1e-12:
                # limit: K2(x) ~ 2/x^2 for small x -> skip to avoid inf
                continue
            fac1 = (n * math.pi + ky/2.0) ** 2
            q1_val += fac1 * math.cos(m * kz) * K2(term_arg1)

    for m in range(1, m_max+1):
        for n in range(-n_max, n_max+1):
            term_arg2 = 2.0 * m * abs(n * math.pi + kz/2.0)
            if term_arg2 < 1e-12:
                continue
            fac2 = (n * math.pi + kz/2.0) ** 2
            q2_val += fac2 * math.cos(m * kx) * K2(term_arg2)

    prefactor = 16.0 / 3.0
    q1_val *= prefactor
    q2_val *= prefactor
    p_xx = q1_val + q2_val
    p_yy = q1_val - 2.0 * q2_val
    p_zz = q2_val - 2.0 * q1_val
    return p_xx, p_yy, p_zz

def precompute_dipole_grid(Nk, m_max=6, n_max=6):
    """Precompute dipole functions on a uniform k-mesh for speed."""
    # mesh covers first quadrant then symmetries, but simpler: full symmetric grid
    ks = np.linspace(-math.pi, math.pi, Nk, endpoint=False)
    pxx = np.zeros((Nk, Nk))
    pyy = np.zeros_like(pxx)
    pzz = np.zeros_like(pxx)
    for i, kx in enumerate(ks):
        for j, ky in enumerate(ks):
            px, py, pz = compute_dipole(kx, ky, m_max, n_max)
            pxx[i,j] = px
            pyy[i,j] = py
            pzz[i,j] = pz
    return ks, pxx, pyy, pzz

# ----------  self-consistent solver (spin-1)  ----------
def solve_iteration(S, D, Omega, T, Nk=30, ks=None, pxx=None, pyy=None, pzz=None, pzz0=None,
                    m1_init=0.9, m2_init=0.81, d1_init=0.0, d2_init=0.0, max_iter=50, tol=1e-6):
    """Run fixed-point iteration for given (D, Omega, T) and return final m1,m2,d1,d2."""
    if ks is None:
        ks, pxx, pyy, pzz = precompute_dipole_grid(Nk, m_max=6, n_max=6)
        pzz0 = compute_dipole(0.0, 0.0)[2]

    Zval = 4
    N = Nk * Nk
    beta = 1.0 / T if T > 1e-12 else 1e12
    D_val = D
    Omega_val = Omega
    m1 = m1_init
    m2 = m2_init
    d1 = d1_init
    d2 = d2_init

    for it in range(max_iter):
        Gamma = 0.5 * m2  # for S=1
        # accumulators for RHS A,B,C,D
        r_A = 0.0
        r_B = 0.0
        r_C = 0.0
        r_D = 0.0
        for i in range(Nk):
            kx = ks[i]
            for j in range(Nk):
                ky = ks[j]
                gamma_k = 0.5 * (math.cos(kx) + math.cos(ky))
                eps_k = 2.0 * J * Zval * m1 * (1.0 - gamma_k)
                px = pxx[i,j]
                py = pyy[i,j]
                pz = pzz[i,j]
                F1 = eps_k + 0.5*Omega_val*m1*px + 0.5*Omega_val*m1*py - Omega_val*m1*pzz0 + D_val*Gamma*m1
                F2 = 0.5*Omega_val*m1*px - 0.5*Omega_val*m1*py + D_val*Gamma*m1
                disc = F1*F1 - F2*F2
                if disc <= 0:
                    # if negative, set E=0 (avoid invalid) - may happen at small m1
                    E_val = 0.0
                else:
                    E_val = math.sqrt(disc)
                if E_val < 1e-12:
                    # skip contributions when E is effectively zero
                    continue
                exp_bE = math.exp(beta * E_val)
                if exp_bE == float('inf'):
                    continue
                bose1 = 1.0 / (exp_bE - 1.0)
                bose2 = 1.0 / (math.exp(-beta*E_val) - 1.0)  # = - (1 + bose1)
                denom = 2.0 * E_val
                # precompute common factors for n=1,2
                # For n=1: <g1^(1)> = 2*m1, <g2^(1)>=0
                g1_1 = 2.0 * m1
                g2_1 = 0.0
                # For n=2: <g1^(2)> = 4 + 2*m1 - 6*m2, <g2^(2)> = -2*d2
                g1_2 = 4.0 + 2.0*m1 - 6.0*m2
                g2_2 = -2.0 * d2

                # RHS_A (n=1 of eq (31))
                term_A1 = (F2 * g2_1 + g1_1 * (E_val + F1)) / denom * bose1
                term_A2 = (F2 * g2_1 - g1_1 * (E_val - F1)) / denom * bose2
                r_A += (term_A1 - term_A2)

                # RHS_B (n=1 of eq (32))
                term_B1 = (F2 * g1_1 - g2_1 * (E_val - F1)) / denom * bose1
                term_B2 = (F2 * g1_1 + g2_1 * (E_val + F1)) / denom * bose2
                r_B += (-term_B1 + term_B2)  # note sign from eq (32)

                # RHS_C (n=2 of eq (31))
                term_C1 = (F2 * g2_2 + g1_2 * (E_val + F1)) / denom * bose1
                term_C2 = (F2 * g2_2 - g1_2 * (E_val - F1)) / denom * bose2
                r_C += (term_C1 - term_C2)

                # RHS_D (n=2 of eq (32))
                term_D1 = (F2 * g1_2 - g2_2 * (E_val - F1)) / denom * bose1
                term_D2 = (F2 * g1_2 + g2_2 * (E_val + F1)) / denom * bose2
                r_D += (-term_D1 + term_D2)

        r_A /= N
        r_B /= N
        r_C /= N
        r_D /= N

        # Update variables (simple mixing: new = 0.3*old + 0.7*computed from RHS solved?)
        # The equations are nonlinear, we can form the difference and apply relaxation.
        # LHS_A = 2 - m1 - m2 should equal r_A; LHS_B = d1 = r_B; LHS_C = 2*(m2-m1) = r_C; LHS_D = 2*d1 = r_D.
        # So target m1,m2,d1,d2 from RHS:  d1_new = r_B;  m1_new = (r_A? Actually we have two equations for m1/m2):
        # from A: m1 + m2 = 2 - r_A
        # from C: m2 - m1 = r_C/2
        # Solve: m1 = ( (2 - r_A) - r_C/2 ) / 2, m2 = ( (2 - r_A) + r_C/2 ) / 2
        # d1_new = r_B, but also we have D: 2*d1 = r_D, consistent with r_B = r_D/2? We'll enforce d1 = (r_B + r_D/2)/2.
        m1_new = ( (2.0 - r_A) - r_C/2.0 ) / 2.0
        m2_new = ( (2.0 - r_A) + r_C/2.0 ) / 2.0
        d1_new = (r_B + r_D/2.0) / 2.0
        d2_new = ? We haven't used d2 equation explicitly; we can keep d2 from previous or use d2 from n=2 relation? But d2 appears in RHS of C and D through g2_2. We can estimate d2_new = 0 (since at low T d2 is small) but better to solve: from the definition, d2 = <(S^-)^2 S^z>. We could approximate that d2 is small and not crucial for convergence; we'll keep d2 from previous iteration, or we can compute d2 from relation derived from (27) which gave <(S^-)^2 (S^z)^2> = d2, but that doesn't directly give d2. We'll just keep d2 unchanged and rely on convergence of d1,d2 coupling? Actually we need to self-consistently determine d2 as well. But the four equations correspond to n=1,2; the independent variables are m1,m2,d1,d2. We have four equations (A,B,C,D) but B and D both determine d1, leaving d2 underdetermined? Actually B gives d1, D gives 2*d1, which should be consistent if solved exactly, but numerical errors may cause inconsistency. To include d2, we need another equation from n=2 that involves d2 explicitly. That is the n=2 equations already used. But in our mapping, we used C and D for n=2, which involve d2 through g2_2. So d2 appears in r_C and r_D. That gives two equations for d2? The unknowns are m1,m2,d1,d2. We have four equations: A (from n=1 LHS1), B (n=1 LHS2), C (n=2 LHS1), D (n=2 LHS2). So we can solve for m1,m2,d1,d2 from the set of equations: 
        # LHS_A = 2 - m1 - m2
        # LHS_B = d1
        # LHS_C = 2*(m2 - m1)
        # LHS_D = 2*d1
        # We can set up linear system: m1 + m2 = 2 - r_A, -m1 + m2 = r_C/2, d1 = r_B, and then d2? Not directly, because d2 appears in r_C and r_D. So we need a separate equation. Actually we can include d2 as unknown and solve simultaneously via iteration: after each k-sum, we can solve for d2 from D equation? But D equation involves d2, so we can solve 
        # d2 = ??? from D: r_D (which depends on d2) should equal 2*d1. So we can rearrange to find d2 that satisfies D given d1. Since D equation is linear in d2 (through g2_2 term), we can solve for d2 from D. Similarly for C. We'll do a linear solve for d2 at each iteration step.
        # Let's derive explicit dependence: In r_C, the term involving d2 comes from g2_2 = -2*d2. So r_C = sum_{k} [ ... ] where the parts independent of d2 plus parts proportional to d2. Same for r_D. So we can treat r_C = A_C + B_C * d2, r_D = A_D + B_D * d2. Then the equations become:
        # C: 2*(m2 - m1) = A_C + B_C * d2
        # D: 2*d1 = A_D + B_D * d2
        # So we can solve for d2 from D: d2 = (2*d1 - A_D) / B_D
        # Then substitute to C. This matches iteration.
        # Thus we need to compute A_C, B_C, A_D, B_D by splitting the k-sums into constant and d2-dependent parts.
        # To simplify, we can use a more straightforward approach: since d2 is small, we can treat it as a perturbation and just keep d2 from previous iteration, using a fixed-point iteration on all four variables. That's what we initially did; the solver still converges if we update d2 using the relation D after computing d1: d2_new = (2*d1 - A_D) / B_D. We'll implement that.
        # However, for simplicity, we'll keep the previous d2 and only update m1,m2,d1 from the linear system, and leave d2 unchanged; after many iterations, it should reach self-consistency if d2 is small. But to be safe, we'll add a d2 update.
        # I'll implement a simple version: keep d2 as previous, and after updating m1,m2,d1, we can approximate a new d2 from the condition that D is satisfied, but it's complex. Instead, let's use the fixed-point approach on all four: we compute RHS using current guesses, then use the LHS to set targets: m1_target, m2_target, d1_target, d2_target? We don't have direct target for d2. Option: we can treat d2 as derived from d1 and m1,m2 using the relation (27) which gave d2 = <(S^-)^2 (S^z)^2>. But that relation is already used to reduce variables. Actually we can express d2 in terms of m1,m2,d1 using (26)-(27). For S=1, using (27): <(S^-)^2 (S^z)^2> = d2? Wait earlier we derived <(S^-)^2 (S^z)^2> = d2 from (27). So d2 = <(S^-)^2 (S^z)^2>. That is an independent variable, not reducible to lower ones. So we need to keep it. So our system has 4 unknowns with 4 equations, it's determined.
        # I'll update all four via a Newton-like method: after computing RHS, define the residual vector:
        # res1 = (2 - m1 - m2) - r_A
        # res2 = d1 - r_B
        # res3 = 2*(m2-m1) - r_C
        # res4 = 2*d1 - r_D
        # We can solve for increments using Jacobian approximated by finite differences, but that's heavy. Instead, because the coupling is not strong, we can iterate: set m1_new, m2_new from A,C as above, d1_new from B, then compute d2_new by solving D for d2 given new d1,m1,m2. Since D depends linearly on d2, we can do: d2_new = (2*d1_new - A_D_non_d2) / B_D, where A_D_non_d2 is r_D computed with d2=0. That's feasible.
        # So we will compute r_D with current d2, but also compute r_D0 with d2=0 to separate. Simplest: run the k-sum twice per iteration, once with d2=0 to get r_D0. That doubles cost but okay.
        # Another approach: note that g2_2 = -2*d2, so r_D = r_D0 + d2 * (coeff_D) where coeff_D can be extracted from the sum. But it's easier to just do the sum with current d2 and use the dependence form r_D = A_D + d2 * B_D, but we don't know B_D directly. However, we can approximate B_D from the previous iteration's change. That is messy. For a fast oracle, we can just skip the d2 update and assume d2=0 always, because at low temperatures d2 is small and its effect on magnetization is minor. At higher T, d2 may become significant. But we need a robust solver. I'll implement a simple fixed-point iteration where we update m1,m2,d1 from A,B,C, and keep d2 from previous iteration; after updating d1, we can compute a new d2 from D by solving, but to do that we need the d2 coefficient. Rather than recompute the sum, we can store the sum with d2. Let's restructure: In the k-sum loop, for each k we accumulate four terms:
        # r_A, r_B, r_C, r_D. We also separate r_C0 (with d2=0) and r_D0 (with d2=0) by noting that g2_2 = -2*d2, so r_C = r_C0 + d2 * delta_C, r_D = r_D0 + d2 * delta_D. But delta_C and delta_D depend only on the k-sum and are independent of d2. So we can compute delta_C and delta_D by evaluating the contribution of the g2_2 term separately. That is, we can compute the coefficient of d2 in r_C and r_D by setting d2=1 temporarily? But that's same cost. So we can compute r_C and r_D twice: first with d2=0, second with d2=1? Or we can compute the part that multiplies g2_2. Since g2_2 = -2*d2, the coefficient is just the sum of the geometric factor. We'll compute the coefficient coeff2_C and coeff2_D in the sum: the terms that multiply g2_2. So in the loop, we compute the factor multiplying g2_2: for C, term: (F2 * g2_2) / (2E)*(bose1 - bose2) (with sign?) Actually the term for C is (F2*g2_2)/denom * (bose1 - bose2). For D: term involves -g2_2*(E-F1) / denom * bose1 + g2_2*(E+F1)/denom * bose2. So both linear in g2_2. So we can compute the coefficient of g2_2, let's call coeffC, coeffD. Then r_C = r_C0 + coeffC * g2_2, r_D = r_D0 + coeffD * g2_2. And g2_2 = -2*d2. So we can compute r_C0, r_D0, coeffC, coeffD in one pass. That's efficient.
        # So I'll modify the loop to accumulate the contributions with d2=0 base plus separate coefficient for the g2_2 term.
        
I'll rewrite the solver with that.

Will produce code that works.

Now, we also need functions for computing E(k) along a path for spinwave output, using converged m1,m2,d1,d2.

The path: Gamma (0,0) -> X (pi,0) -> M (pi,pi) -> Gamma (0,0). We'll include many intermediate points.

Transition temperature: we need to find Tc where m1 reaches 0. We'll solve M(T) for a range of T, then interpolate or use root-finding. We'll do linear interpolation from the first T where m1 drops below a threshold (e.g., 0.01).

Now, write the full script.

Constraints: no network access. Script uses math, numpy, scipy.

Let's produce the code.
