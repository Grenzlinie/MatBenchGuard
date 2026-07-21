# solution/compute.py
import csv, sys, os
import numpy as np
from scipy.special import i0

p = 3
beta = 100.0
beta0 = 2.0

def f_ideal(m, s, tau):
    m = np.maximum(m, 0)
    spm = s * p * m**(p-1)
    term1 = (1 - tau) * np.sqrt(spm**2 + 1)
    term2 = tau * spm
    return s * (p-1) * m**p - term1 - term2

def f_finiteT(m, s, tau):
    spm = s * p * m**(p-1)
    t1 = np.sqrt(spm**2 + 1)
    t2 = np.abs(spm)
    term = (1 - tau) * np.log(2 * np.cosh(beta * t1)) + tau * np.log(2 * np.cosh(beta * t2))
    return s * (p-1) * m**p - (1/beta) * term

def f_svmc(m, s, tau):
    spm = s * p * m**(p-1)
    t1 = np.sqrt(spm**2 + 1)
    t2 = np.abs(spm)
    logI0_t1 = np.log(i0(beta * t1))
    logI0_t2 = np.log(i0(beta * t2))
    term = (1 - tau) * (np.log(2*np.pi) + logI0_t1) + tau * (np.log(2*np.pi) + logI0_t2)
    return s * (p-1) * m**p - (1/beta) * term

def f_sa(m, tau):
    return 2 * m**3 - tau * np.log(2 * np.cosh(6 * m**2))

def find_min(model, s, tau):
    mgrid = np.linspace(0, 1.5, 300)
    if model == 'ideal':
        vals = f_ideal(mgrid, s, tau)
    elif model == 'finiteT':
        vals = f_finiteT(mgrid, s, tau)
    elif model == 'svmc':
        vals = f_svmc(mgrid, s, tau)
    elif model == 'sa':
        vals = f_sa(mgrid, tau)
    else:
        raise ValueError
    idx = np.argmin(vals)
    m_opt = mgrid[idx]
    if idx > 0 and idx < len(mgrid)-1:
        m_fine = np.linspace(mgrid[idx-1], mgrid[idx+1], 100)
        if model == 'sa':
            vals_fine = f_sa(m_fine, tau)
        elif model == 'ideal':
            vals_fine = f_ideal(m_fine, s, tau)
        elif model == 'finiteT':
            vals_fine = f_finiteT(m_fine, s, tau)
        elif model == 'svmc':
            vals_fine = f_svmc(m_fine, s, tau)
        idx2 = np.argmin(vals_fine)
        m_opt = m_fine[idx2]
    return m_opt

s_vals = np.linspace(0, 1, 101)
tau_vals = np.linspace(0, 1, 101)
model = sys.argv[1]

if model == 'jump':
    outfile = '/app/outputs/jump_magnetization.csv'
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['tau', 'delta_m'])
        for tau in tau_vals:
            m_vals = []
            for s in s_vals:
                m = find_min('finiteT', s, tau)
                m_vals.append(m)
            jump_detected = None
            for i in range(1, len(s_vals)):
                diff = m_vals[i] - m_vals[i-1]
                if diff > 0.005:
                    if jump_detected is None or diff > jump_detected:
                        jump_detected = diff
            if jump_detected is not None:
                writer.writerow([round(tau, 4), round(jump_detected, 6)])
else:
    if model == 'ideal':
        outfile = '/app/outputs/idealized_magnetization.csv'
    elif model == 'finiteT':
        outfile = '/app/outputs/finiteT_magnetization.csv'
    elif model == 'svmc':
        outfile = '/app/outputs/SVMC_magnetization.csv'
    elif model == 'sa':
        outfile = '/app/outputs/SA_magnetization.csv'
    else:
        raise ValueError('Unknown model')
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['s', 'tau', 'm'])
        for s in s_vals:
            for tau in tau_vals:
                m = find_min(model, s, tau)
                writer.writerow([round(s, 4), round(tau, 4), round(m, 6)])
