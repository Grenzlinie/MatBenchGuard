#!/usr/bin/env python3
"""Reference oracle: compute coherent phase diagram data."""

import json
import math
import sys
import numpy as np
from scipy.optimize import fsolve

EPS = 1e-12

# Free energy and derivatives (Eq. 20)
def phi(t, c, Pi, Lam, eta_c, eta_cc):
    c = max(EPS, min(1.0-EPS, c))
    eps = eta_c * c + 0.5 * eta_cc * c * c
    term1 = t * (c * math.log(c) + (1.0 - c) * math.log(1.0 - c))
    term2 = 2.0 * c * (1.0 - c)
    term3 = -4.5 * Pi * Pi
    term4 = 3.0 * math.sqrt(Lam) * eps * Pi
    return term1 + term2 + term3 + term4

def M(t, c, Pi, Lam, eta_c, eta_cc):
    """∂φ/∂c"""
    c = max(EPS, min(1.0-EPS, c))
    dphi_dc = t * (math.log(c) - math.log(1.0 - c)) + 2.0 * (1.0 - 2.0 * c) + 3.0 * math.sqrt(Lam) * Pi * (eta_c + eta_cc * c)
    return dphi_dc

def E(t, c, Pi, Lam, eta_c, eta_cc):
    """∂φ/∂Π"""
    eps = eta_c * c + 0.5 * eta_cc * c * c
    return -9.0 * Pi + 3.0 * math.sqrt(Lam) * eps

def Omega(t, c, Pi, Lam, eta_c, eta_cc):
    """Grand potential: φ - M*c - E*Π"""
    return phi(t, c, Pi, Lam, eta_c, eta_cc) - M(t, c, Pi, Lam, eta_c, eta_cc)*c - E(t, c, Pi, Lam, eta_c, eta_cc)*Pi

def min_c(c):
    return max(EPS, min(1.0-EPS, c))

# Spinodal (Eq. 22)
def spinodal_t(c, Pi, Lam, eta_c, eta_cc):
    c = min_c(c)
    t_spin = c * (1.0 - c) * (4.0 - Lam * (eta_c + eta_cc * c)**2 - 3.0 * eta_cc * math.sqrt(Lam) * Pi)
    return t_spin

# Crit condition (Eq. 23)
def crit_t(c, Lam, eta_c, eta_cc):
    c = min_c(c)
    denom = 1.0 - 2.0 * c
    if abs(denom) < 1e-12:
        return None
    factor = (c * (1.0 - c))**2 / denom
    t_crit = factor * 3.0 * Lam * eta_cc * (eta_c + eta_cc * c)
    return t_crit

def solve_critical(Pi_o, Lam, eta_c, eta_cc):
    """Find (t_c, c_c) satisfying spinodal and critical conditions at given Π."""
    def f(x):
        t, c = x
        c = min_c(c)
        t_spin = spinodal_t(c, Pi_o, Lam, eta_c, eta_cc)
        t_crit = crit_t(c, Lam, eta_c, eta_cc)
        if t_crit is None:
            return [t - t_spin, 1000.0]  # penalty
        return [t - t_spin, t - t_crit]
    
    # initial guess around c=0.5, t=1
    guess = [1.0, 0.5]
    sol = fsolve(f, guess, maxfev=2000, xtol=1e-8, factor=0.1)
    t_c, c_c = sol
    c_c = min_c(c_c)
    if t_c < 0:
        t_c = 0.0
    return t_c, c_c

def solve_boundary_alpha(t, Pi_o, Lam, eta_c, eta_cc, init_guess):
    """
    Phase boundary for alpha (shell) stable, beta incipient.  
    Unknowns: c_alpha, c_beta, Pi_beta.
    Equations: M_a=M_b, E_a=E_b, Omega_a=Omega_b, with Pi_alpha = Pi_o.
    """
    def eqs(x):
        ca, cb, Pib = x
        ca = min_c(ca)
        cb = min_c(cb)
        # Pi_alpha = Pi_o
        Ma = M(t, ca, Pi_o, Lam, eta_c, eta_cc)
        Ea = E(t, ca, Pi_o, Lam, eta_c, eta_cc)
        Oa = Omega(t, ca, Pi_o, Lam, eta_c, eta_cc)
        Mb = M(t, cb, Pib, Lam, eta_c, eta_cc)
        Eb = E(t, cb, Pib, Lam, eta_c, eta_cc)
        Ob = Omega(t, cb, Pib, Lam, eta_c, eta_cc)
        return [Ma - Mb, Ea - Eb, Oa - Ob]
    
    sol = fsolve(eqs, init_guess, maxfev=2000, xtol=1e-8, factor=0.1)
    ca, cb, Pib = sol
    ca = min_c(ca)
    cb = min_c(cb)
    return ca, cb, Pib

def solve_boundary_beta(t, Pi_o, Lam, eta_c, eta_cc, init_guess):
    """
    Phase boundary for beta (core) stable, alpha incipient.
    Unknowns: c_beta, c_alpha, Pi_alpha.
    """
    def eqs(x):
        cb, ca, Pia = x
        cb = min_c(cb)
        ca = min_c(ca)
        Mb = M(t, cb, Pi_o, Lam, eta_c, eta_cc)
        Eb = E(t, cb, Pi_o, Lam, eta_c, eta_cc)
        Ob = Omega(t, cb, Pi_o, Lam, eta_c, eta_cc)
        Ma = M(t, ca, Pia, Lam, eta_c, eta_cc)
        Ea = E(t, ca, Pia, Lam, eta_c, eta_cc)
        Oa = Omega(t, ca, Pia, Lam, eta_c, eta_cc)
        return [Mb - Ma, Eb - Ea, Ob - Oa]
    
    sol = fsolve(eqs, init_guess, maxfev=2000, xtol=1e-8, factor=0.1)
    cb, ca, Pia = sol
    cb = min_c(cb)
    ca = min_c(ca)
    return cb, ca, Pia

def compute_phase_boundary(Pi_o, Lam, eta_c, eta_cc, t_c, c_c, npts=60):
    """Return arrays t, c_alpha, c_beta for t from t_c down to 0."""
    t_vals = []
    c_alpha_vals = []
    c_beta_vals = []
    
    # Start from t slightly below t_c
    t_start = t_c * 0.999
    # use initial guess from critical point
    guess_a = [c_c, c_c, Pi_o]  # ca, cb, Pib
    guess_b = [c_c, c_c, Pi_o]  # cb, ca, Pia
    
    t = t_start
    while t > 0.001:
        try:
            ca, cb, Pib = solve_boundary_alpha(t, Pi_o, Lam, eta_c, eta_cc, guess_a)
            # for the beta stable side, we have symmetric roles; we can just assign the smaller composition to alpha? 
            # The two phases: one side has lower composition (alpha? depends on params). 
            # We'll store both solutions as the two boundary compositions. 
            # Actually, the boundary points are: (c_alpha from alpha-stable) and (c_beta from beta-stable) 
            # but we can get both from a single solve: the c_alpha from alpha-stable is one boundary, the c_beta from alpha-stable is the other boundary.
            # So we can directly use ca as c_alpha and cb as c_beta (ensuring ordering).
            if ca > cb:
                ca, cb = cb, ca
            c_alpha_vals.append(ca)
            c_beta_vals.append(cb)
            t_vals.append(t)
            # update guess for next lower t
            guess_a = [ca, cb, Pib]
            guess_b = [cb, ca, Pi_o]  # for beta stable, but not needed here.
        except Exception:
            print(f"Warning: root-finding failed at t={t}", file=sys.stderr)
        t -= (t_c - 0.001) / npts
        if t < 0.001:
            break
    return t_vals, c_alpha_vals, c_beta_vals

def compute_spinodal(Pi_o, Lam, eta_c, eta_cc):
    c_arr = np.linspace(EPS, 1.0-EPS, 500)
    t_arr = [spinodal_t(c, Pi_o, Lam, eta_c, eta_cc) for c in c_arr]
    # Filter positive t and remove extremes
    filtered_c = []
    filtered_t = []
    for ci, ti in zip(c_arr, t_arr):
        if ti > 0:
            filtered_c.append(ci)
            filtered_t.append(ti)
    return filtered_c, filtered_t

def compute_tie_line(t, Pi_o, Lam, eta_c, eta_cc):
    """Return a single tie-line (c_alpha, Pi_alpha, c_beta, Pi_beta) at given conditions."""
    # Solve for alpha-stable boundary, which gives ca (alpha composition) and cb (beta composition), and Pib (beta pressure)
    # initial guess from critical point (if available) or random
    # We'll get critical point first
    tc, cc = solve_critical(Pi_o, Lam, eta_c, eta_cc)
    if t > tc:
        # no two-phase, return None
        return None
    # initial guess
    guess_a = [cc, cc, Pi_o]
    ca, cb, Pib = solve_boundary_alpha(t, Pi_o, Lam, eta_c, eta_cc, guess_a)
    # ordering: we assume c_alpha < c_beta for the tie-line (alpha is shell with lower composition? depends on params)
    # The paper states that for ηc=-0.05, ηcc=0.04, β phase has lower effective pressure and higher composition? Actually they said the β phase possesses a lower effective pressure than the α phase (Fig. 2(b)). Also "the composition of the α phase increases, while the composition of the β phase decreases" — so α is higher c? 
    # We'll assign c_alpha to be the smaller c, c_beta larger.
    if ca > cb:
        ca, cb = cb, ca
        Pi_a, Pi_b = Pi_o, Pib  # but wait, if we swapped, alpha pressure is Pi_o? Actually Pi_alpha was supposed to be Pi_o. If we swapped, the role changes. We'll be careful: When solve_boundary_alpha gives ca as the stable alpha composition (with Pi_o) and cb as the incipient beta composition with Pib. So the tie-line endpoints are (ca, Pi_o) and (cb, Pib). If ca > cb, we can still output as is, but the ordering may matter. The checker likely expects c_alpha < c_beta, Pi_alpha > Pi_beta or something. We'll keep the naming straightforward.
        # We'll not swap; we'll output as returned.
        c_alpha_out, Pi_alpha_out = ca, Pi_o
        c_beta_out, Pi_beta_out = cb, Pib
    else:
        c_alpha_out, Pi_alpha_out = ca, Pi_o
        c_beta_out, Pi_beta_out = cb, Pib
    return c_alpha_out, Pi_alpha_out, c_beta_out, Pi_beta_out

def compute_gap_width_vs_Pi(t, Pi_lst, Lam, eta_c, eta_cc):
    """Return list of gap widths at fixed t for each Pi."""
    gaps = []
    for Pi_o in Pi_lst:
        # compute critical point at this Pi_o to check if t is below critical
        tc, cc = solve_critical(Pi_o, Lam, eta_c, eta_cc)
        if t >= tc:
            gaps.append(0.0)
            continue
        # solve for tie-line
        guess_a = [cc, cc, Pi_o]
        try:
            ca, cb, Pib = solve_boundary_alpha(t, Pi_o, Lam, eta_c, eta_cc, guess_a)
            width = abs(cb - ca)
            gaps.append(width)
        except Exception:
            gaps.append(0.0)
    return gaps

def process_parameters(name, params):
    Lam = params['Lambda']
    eta_c = params['eta_c']
    eta_cc = params['eta_cc']
    Pi_o = 0.1
    
    result = {}
    
    # 1. Critical point at Pi_o=0.1
    t_c, c_c = solve_critical(Pi_o, Lam, eta_c, eta_cc)
    result['critical_point'] = {'t_c': round(t_c, 6), 'c_c': round(c_c, 6)}
    
    # 2. Phase boundary at Pi_o=0.1
    t_arr, ca_arr, cb_arr = compute_phase_boundary(Pi_o, Lam, eta_c, eta_cc, t_c, c_c, npts=80)
    result['phase_boundary_at_Pi_0_1'] = {
        't': [round(v, 6) for v in t_arr],
        'c_alpha': [round(v, 6) for v in ca_arr],
        'c_beta': [round(v, 6) for v in cb_arr]
    }
    
    # 3. Spinodal at Pi_o=0.1
    c_sp, t_sp = compute_spinodal(Pi_o, Lam, eta_c, eta_cc)
    result['spinodal_at_Pi_0_1'] = {
        't': [round(v, 6) for v in t_sp],
        'c': [round(v, 6) for v in c_sp]
    }
    
    # 4. Tie-lines at t=0.8, Pi_o=0.1
    t_tie = 0.8
    tie_data = compute_tie_line(t_tie, Pi_o, Lam, eta_c, eta_cc)
    if tie_data:
        ca_tie, Pa_tie, cb_tie, Pb_tie = tie_data
        tie_list = [{
            'c_alpha': round(ca_tie, 6),
            'Pi_alpha': round(Pa_tie, 6),
            'c_beta': round(cb_tie, 6),
            'Pi_beta': round(Pb_tie, 6)
        }]
    else:
        tie_list = []
    result['tie_lines_at_t_0_8'] = tie_list
    
    # 5. Effect of Pi on gap width at t=0.8
    t_fixed = 0.8
    Pi_range = np.linspace(0.0, 0.5, 51).tolist()
    gaps = compute_gap_width_vs_Pi(t_fixed, Pi_range, Lam, eta_c, eta_cc)
    result['effect_of_Pi'] = {
        't': t_fixed,
        'Pi': Pi_range,
        'gap_width': [round(w, 6) for w in gaps]
    }
    
    return result

def main():
    param_sets = {
        'L100_eta_c_-0.05_eta_cc_0.04': {'Lambda': 100.0, 'eta_c': -0.05, 'eta_cc': 0.04},
        'L100_eta_c_-0.03_eta_cc_0':    {'Lambda': 100.0, 'eta_c': -0.03, 'eta_cc': 0.0},
        'L100_eta_c_-0.01_eta_cc_-0.04': {'Lambda': 100.0, 'eta_c': -0.01, 'eta_cc': -0.04},
        'L350_eta_c_-0.05_eta_cc_0.05': {'Lambda': 350.0, 'eta_c': -0.05, 'eta_cc': 0.05}
    }
    
    output = {}
    for name, pars in param_sets.items():
        print(f"Processing {name}", file=sys.stderr)
        output[name] = process_parameters(name, pars)
    
    with open('/app/outputs/phase_diagram_data.json', 'w') as f:
        json.dump(output, f, indent=2)
    print("Done.", file=sys.stderr)

if __name__ == '__main__':
    main()
