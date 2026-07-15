#!/usr/bin/env python3
"""Compute reference values for the λ1 coefficient task."""
import sys
import json
import mpmath as mp
# Set high precision
mp.mp.dps = 50

def lam1a_scale(zeta):
    """Λ1^a(ζ) from Eq. (16)."""
    kd = (1 - zeta) ** (1/3)
    ku = (1 + zeta) ** (1/3)
    pi = mp.pi
    f1 = 3 / (pi**2 - 6)
    t1 = (pi**2/6 + 1/4) * (kd**2 + ku**2)
    t2 = -1.5 * kd * ku
    t3 = -(kd**2 + ku**2) / (kd**2 - ku**2) * kd * ku * mp.log(kd/ku)
    arg1 = (kd - ku) / (kd + ku)
    arg2 = (ku - kd) / (kd + ku)
    dilog1 = mp.polylog(2, arg1)
    dilog2 = mp.polylog(2, arg2)
    t4 = -(kd**2 - ku**2) / 2 * (dilog1 - dilog2)
    return f1 * (t1 + t2 + t3 + t4)

def lam1b_scale(zeta):
    """Λ1^b(ζ) from Eq. (17)."""
    kd = (1 - zeta) ** (1/3)
    ku = (1 + zeta) ** (1/3)
    pi = mp.pi
    ln2 = mp.log(2)
    f2 = 3 / (pi**2 - 12*ln2)
    t1 = pi**2/6 * (kd**2 + ku**2)
    t2 = (1 - ln2) * (kd - ku)**2
    arg1 = (kd - ku) / (kd + ku)
    arg2 = (ku - kd) / (kd + ku)
    t3 = -kd**2/2 * mp.polylog(2, arg1) - ku**2/2 * mp.polylog(2, arg2)
    log_part = (kd**4 * mp.log(kd/(kd+ku))
                + kd**2 * ku**2 * mp.log(kd*ku/(kd+ku)**2)
                + ku**4 * mp.log(ku/(kd+ku))) / (kd*ku)
    return f2 * (t1 + t2 + t3 + log_part)

def step01():
    pi = mp.pi
    alpha = (4/(9*pi))**(1/3)   # (9π/4)^{-1/3}
    # RPA and exchange components at zeta=0
    la0 = alpha / (24 * pi**3) * (pi**2 - 6)
    lb0 = alpha / (4 * pi**3) * (pi**2 - 12 * mp.log(2))
    l0 = la0 + lb0
    # Ferromagnetic limits
    la1 = (alpha / (24 * pi**3) * (pi**2 + 6)) * mp.power(2, -mp.mpf(7)/3)
    lb1 = lb0 * mp.power(2, -mp.mpf(4)/3)
    l1 = la1 + lb1
    return {
        'lambda1_0': float(l0),
        'lambda1_1': float(l1),
        'lambda1_a_0': float(la0),
        'lambda1_a_1': float(la1),
        'lambda1_b_0': float(lb0),
        'lambda1_b_1': float(lb1)
    }

def step02():
    zeta = mp.mpf('0.5')
    pi = mp.pi
    La = lam1a_scale(zeta)
    Lb = lam1b_scale(zeta)
    # Eq. (32) and (33)
    La_upup = (1/8) * (pi**2 + 6) / (pi**2 - 6) * ((1 + zeta)**(2/3)) / La
    Lb_upup = (1/4) * ((1 + zeta)**(2/3)) / Lb
    return {
        'Lambda1_a_upup_05': float(La_upup),
        'Lambda1_b_upup_05': float(Lb_upup)
    }

def step03():
    pi = mp.pi
    alpha = (4/(9*pi))**(1/3)
    delta = mp.power(2, -mp.mpf(1)/3) * alpha / (8 * pi**3)
    return {'delta_lambda1a_1': float(delta)}

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] != '--step':
        sys.exit("Usage: compute.py --step step01|step02|step03")
    step = sys.argv[2]
    if step == 'step01':
        result = step01()
    elif step == 'step02':
        result = step02()
    elif step == 'step03':
        result = step03()
    else:
        sys.exit(f"Unknown step: {step}")
    json.dump(result, sys.stdout, indent=2)
