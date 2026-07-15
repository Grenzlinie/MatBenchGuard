import json
from fractions import Fraction

def compute_tetragonal():
    g2 = Fraction(3,10)  # 0.3
    f = Fraction(1,20)   # 0.05
    p = Fraction(2,1)    # 2.0

    # coefficients
    A = 1 + g2 * (2 - Fraction(179,280)*f)
    B = g2 * (Fraction(6,5) - Fraction(4,35)*f)
    C = g2 * (Fraction(9,20) + Fraction(13,140)*f)

    # F asymptotic
    inner = A * p**2 - B * p**3 + C * p**4
    F = (1/g2) * inner

    # p_b
    D = Fraction(6,5) - Fraction(4,35)*f
    bracket = 1/g2 + (2 - Fraction(179,280)*f)
    p_b = Fraction(2,1) / D * bracket

    # p_s
    p_s = Fraction(4,3) / D * bracket

    # binodal check
    common1 = Fraction(9,10) + Fraction(13,70)*f
    num1 = Fraction(9,5) - Fraction(2,7)*f
    den1 = 9 + Fraction(13,7)*f
    term_b = Fraction(4,1) * g2 * num1 / den1
    g1_bin = - g2**2 * common1 * (1 - term_b)
    binodal_check = g1_bin < 0

    # spinodal check
    term_s = Fraction(9,2) * g2 * num1 / den1
    g1_spin = - g2**2 * common1 * (1 - term_s)
    spinodal_check = g1_spin < 0

    return {
        "g2": float(g2),
        "f": float(f),
        "p": float(p),
        "F_asymptotic": float(F),
        "p_b": float(p_b),
        "p_s": float(p_s),
        "binodal_check": bool(binodal_check),
        "spinodal_check": bool(spinodal_check)
    }

def compute_rhombohedral():
    g1 = Fraction(2,10)  # 0.2
    f = Fraction(1,20)   # 0.05
    p = Fraction(2,1)    # 2.0

    A = 1 + g1 * (2 + Fraction(2,5)*f)
    B = g1 * (Fraction(6,5) + Fraction(229,630)*f)
    C = g1 * (Fraction(9,20) + Fraction(8,63)*f)

    inner = A * p**2 - B * p**3 + C * p**4
    F = (1/g1) * inner

    D = Fraction(6,5) + Fraction(229,630)*f
    bracket = 1/g1 + (2 + Fraction(2,5)*f)
    p_b = Fraction(2,1) / D * bracket
    p_s = Fraction(4,3) / D * bracket

    # binodal check
    common2 = Fraction(27,20) + Fraction(8,21)*f
    num2 = Fraction(36,25) + Fraction(229,315)*f
    den2 = Fraction(9,5) + Fraction(32,63)*f
    term_b = g1 * num2 / den2
    g2_bin = - g1/2 - g1**2 * common2 * (1 - term_b)
    binodal_check = g2_bin < 0

    # spinodal check
    den_s = Fraction(9,20) + Fraction(8,63)*f
    term_s = Fraction(9,32) * g1 * num2 / den_s
    g2_spin = - g1/2 - g1**2 * common2 * (1 - term_s)
    spinodal_check = g2_spin < 0

    return {
        "g1": float(g1),
        "f": float(f),
        "p": float(p),
        "F_asymptotic": float(F),
        "p_b": float(p_b),
        "p_s": float(p_s),
        "binodal_check": bool(binodal_check),
        "spinodal_check": bool(spinodal_check)
    }

def main():
    res = {
        "tetragonal": compute_tetragonal(),
        "rhombohedral": compute_rhombohedral()
    }
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
