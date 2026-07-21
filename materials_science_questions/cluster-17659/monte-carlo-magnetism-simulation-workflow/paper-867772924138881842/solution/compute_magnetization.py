import sys
import math

J = 1.0

def phi(x):
    """Standard normal CDF"""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def p_n(n, h):
    """p_n(h) = probability a spin with n up neighbours flips up at field h"""
    t = 2.0 * (1.0 - n) - h
    return 1.0 - phi(t)

def P_star(h):
    p0 = p_n(0, h)
    p1 = p_n(1, h)
    denom = 1.0 - (p1 - p0)
    if denom == 0.0:
        return 0.0
    return p0 / denom

def prob_up_main(h):
    Ps = P_star(h)
    p0 = p_n(0, h)
    p1 = p_n(1, h)
    p2 = p_n(2, h)
    return (Ps**2) * p2 + 2.0 * Ps * (1.0 - Ps) * p1 + ((1.0 - Ps)**2) * p0

def magnetization_main(h):
    return 2.0 * prob_up_main(h) - 1.0

def f_func(h):
    Ps = P_star(h)
    p1 = p_n(1, h)
    p2 = p_n(2, h)
    return (1.0 - p2) * Ps + (1.0 - p1) * (1.0 - Ps)

def q_a(h, hp):
    f = f_func(h)
    p1_h = p_n(1, h)
    p1_hp = p_n(1, hp)
    denom = 1.0 - (p1_h - p1_hp)
    if denom == 0.0:
        return 0.0
    return f / denom

def q_b(h, hp):
    Ps = P_star(h)
    p2_h = p_n(2, h)
    p2_hp = p_n(2, hp)
    p1_h = p_n(1, h)
    p1_hp = p_n(1, hp)
    denom = 1.0 - (p1_h - p1_hp)
    if denom == 0.0:
        return 0.0
    return (p2_h - p2_hp) * Ps / denom

def prob_up_return(h, hp):
    # h is reversal point, hp is current field on return loop
    p_h = prob_up_main(h)
    Ps = P_star(h)
    p0_h = p_n(0, h)
    p0_hp = p_n(0, hp)
    p1_h = p_n(1, h)
    p1_hp = p_n(1, hp)
    p2_h = p_n(2, h)
    p2_hp = p_n(2, hp)

    qa = q_a(h, hp)
    qb = q_b(h, hp)
    q_sum = qa + qb

    q_r2 = (Ps**2) * (p2_h - p2_hp)
    q_r1 = 2.0 * Ps * q_sum * (p1_h - p1_hp)
    q_r0 = (q_sum**2) * (p0_h - p0_hp)

    return p_h - q_r2 - q_r1 - q_r0

def magnetization_return(h, hp):
    return 2.0 * prob_up_return(h, hp) - 1.0

def compute_main():
    # h from -5 to 5 step 0.1
    print("h,m")
    h = -5.0
    while h <= 5.0 + 1e-12:
        m = magnetization_main(h)
        print(f"{h:.10f},{m:.10f}")
        h += 0.1

def compute_return():
    # reversal point
    h_rev = 1.0
    # reversed field from 1 down to -1 step 0.05
    print("h_prime,m_prime")
    hp = 1.0
    while hp >= -1.0 - 1e-12:
        mp = magnetization_return(h_rev, hp)
        print(f"{hp:.10f},{mp:.10f}")
        hp -= 0.05

if __name__ == "__main__":
    task = sys.argv[1]
    if task == "main":
        compute_main()
    elif task == "return":
        compute_return()
    else:
        raise ValueError("Unknown task")
