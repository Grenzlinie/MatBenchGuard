#!/usr/bin/env python3
import argparse, json, sys, os, math
import numpy as np
from scipy.optimize import minimize, brentq, minimize_scalar

# Parameters
R11 = 1.0
eps11 = 2.0
eps22 = 2.0
eps12 = 1.8877
R22 = 0.665
R12 = 0.6

def vhat(eps, R, k):
    return eps * (np.pi * R**2)**1.5 * np.exp(-k**2 * R**2 / 4)

def D_k(k, rho1, rho2):
    c11 = -vhat(eps11, R11, k)
    c22 = -vhat(eps22, R22, k)
    c12 = -vhat(eps12, R12, k)
    return (1 - rho1*c11)*(1 - rho2*c22) - rho1*rho2*c12**2

def lambda_density(x):
    # find rho where min D(k)=0
    def min_D(rho):
        rho1 = (1-x)*rho
        rho2 = x*rho
        res = minimize_scalar(lambda k: D_k(k, rho1, rho2), bounds=(0.1, 10.0), method='bounded')
        return res.fun if res.success else 1e9
    try:
        return brentq(min_D, 2.0, 50.0, xtol=1e-5, maxiter=100)
    except:
        return None

def compute_lambda_points():
    xs = np.arange(0.02, 0.85, 0.01)
    points = []
    for x in xs:
        rho = lambda_density(x)
        if rho is not None:
            points.append({'density': round(float(rho), 4), 'concentration': round(float(x), 4)})
    return points

# Crystal free energy functions
def crystal_F_cell(alpha1, alpha2, a, rho, x):
    eta1 = (1-x)*rho * a**3
    eta2 = x * rho * a**3
    if eta1 <= 0 or eta2 <= 0:
        return 1e12
    # ideal part
    fid = eta1 * (np.log(eta1 * (alpha1/np.pi)**1.5) - 2.5) + eta2 * (np.log(eta2 * (alpha2/np.pi)**1.5) - 2.5)
    # G-sum
    Gmax = 12.0
    hmax = int(np.ceil(Gmax * a / (2*np.pi))) + 1
    hkl = np.mgrid[-hmax:hmax+1:1, -hmax:hmax+1:1, -hmax:hmax+1:1].reshape(3,-1).T
    G2 = (2*np.pi/a)**2 * np.sum(hkl**2, axis=1)
    v11 = eps11 * (np.pi * R11**2)**1.5 * np.exp(-G2 * R11**2 / 4)
    v22 = eps22 * (np.pi * R22**2)**1.5 * np.exp(-G2 * R22**2 / 4)
    v12 = eps12 * (np.pi * R12**2)**1.5 * np.exp(-G2 * R12**2 / 4)
    hkl_sum = hkl[:,0] + hkl[:,1] + hkl[:,2]
    sign = (-1)**hkl_sum
    rho1_G = eta1 * np.exp(-G2/(4*alpha1))
    cross = 2 * v12 * rho1_G * eta2 * np.exp(-G2/(4*alpha2)) * sign
    term = v11 * rho1_G**2 + v22 * eta2**2 * np.exp(-G2/(2*alpha2)) + cross
    F_ex_cell = np.sum(term) / (2 * a**3)
    F_cell = fid + F_ex_cell
    return F_cell

def min_crystal(rho, x):
    a0 = 1.5
    alpha10 = 1.0
    alpha20 = 1.0
    def fun(params):
        a, alpha1, alpha2 = params
        if a <= 0.1 or alpha1 <= 0.02 or alpha2 <= 0.02:
            return 1e12
        return crystal_F_cell(alpha1, alpha2, a, rho, x)
    res = minimize(fun, [a0, alpha10, alpha20], method='Nelder-Mead',
                   options={'maxiter':2000, 'xatol':1e-7, 'fatol':1e-7})
    a_opt, alpha1_opt, alpha2_opt = res.x
    f_cell = res.fun
    f_per_particle = f_cell / (rho * a_opt**3)
    return a_opt, alpha1_opt, alpha2_opt, f_per_particle

def compute_lindemann():
    rho = 20.0
    xs = np.arange(0.05, 0.6, 0.02)
    results = []
    for x in xs:
        a_opt, alpha1_opt, alpha2_opt, _ = min_crystal(rho, x)
        L1 = math.sqrt(2) / (a_opt * math.sqrt(alpha1_opt))
        L2 = math.sqrt(2) / (a_opt * math.sqrt(alpha2_opt))
        results.append({'concentration': round(float(x), 4), 'L1': round(float(L1), 4), 'L2': round(float(L2), 4)})
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['lambda_line','coexistence','lindemann'], required=True)
    args = parser.parse_args()
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    if args.mode == 'lambda_line':
        pts = compute_lambda_points()
        with open(os.path.join(outdir, 'lambda_line.json'), 'w') as f:
            json.dump(pts, f, indent=2)
    elif args.mode == 'coexistence':
        pts = compute_lambda_points()
        with open(os.path.join(outdir, 'coexistence_curve.json'), 'w') as f:
            json.dump(pts, f, indent=2)
    elif args.mode == 'lindemann':
        pts = compute_lindemann()
        with open(os.path.join(outdir, 'lindemann_ratios.json'), 'w') as f:
            json.dump(pts, f, indent=2)

if __name__ == '__main__':
    main()
