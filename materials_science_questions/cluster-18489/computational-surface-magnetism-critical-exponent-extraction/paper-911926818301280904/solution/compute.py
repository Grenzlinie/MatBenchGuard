import sys
import json
import math
import cmath
import numpy as np
from scipy.integrate import quad


def parse_a(a_str):
    """Convert a string like '0.6i' into a complex number a where Re(a)=0."""
    s = a_str.strip()
    if s == '0':
        return 0.0
    if 'i' in s:
        return complex(0, float(s.replace('i', '')))
    return float(s)


def e_b_integrand(p, a):
    """
    Return a function of k that is the integrand for e_b(p) from 0 to ∞.
    The factor (4a^2-1)/4 is included.
    """
    coeff = (4 * a**2 - 1) / 4
    def f(k):
        if k == 0:
            return 0.0
        # Terms that are real-valued (a is imaginary, so cosh(ak) = cos(|a|k))
        e_minus_k = math.exp(-k)
        cosh_ak = cmath.cosh(a * k)   # actually real when a is imaginary
        denom = math.exp(-k/2) * math.cosh(k/2)
        if denom == 0:
            return 0.0
        # Use abs(p) because the formula uses |p|
        numerator = (1 - e_minus_k) * cosh_ak * math.exp(-abs(p) * k)
        return coeff * numerator / denom
    # The integrand is even? For k>=0 we integrate from 0; the full integral from -∞ to ∞ is 2 * this.
    # But the original integral is over whole real line and the integrand is even, so multiply by 2.
    # We'll integrate from 0 to inf and multiply by 2.
    val, _ = quad(lambda k: f(k).real, 0, np.inf, limit=200)
    return 2 * val


def e_b0_part(a):
    """
    The e_{b0} contribution: integral from -∞ to ∞ of
    (4a^2-1)/4 * (1-e^{-|k|}) * cosh(a k) * (e^{-|k|} - e^{-|k|/2}) / (e^{-|k|/2} cosh(k/2))
    """
    coeff = (4 * a**2 - 1) / 4
    def f(k):
        if k == 0:
            return 0.0
        e_minus_k = math.exp(-k)
        e_minus_half_k = math.exp(-k/2)
        cosh_ak = cmath.cosh(a * k)
        denom = e_minus_half_k * math.cosh(k/2)
        if denom == 0:
            return 0.0
        numerator = (1 - e_minus_k) * cosh_ak * (e_minus_k - e_minus_half_k)
        return coeff * numerator / denom
    val, _ = quad(lambda k: f(k).real, 0, np.inf, limit=200)
    return 2 * val


def surface_energy(a_str, p, q, xi):
    a = parse_a(a_str)
    q_bar = q / math.sqrt(1 + xi**2)
    return e_b_integrand(p, a) + e_b_integrand(q_bar, a) + e_b0_part(a)


def bulk_excitation_energy(a_str, z):
    a = parse_a(a_str)
    coeff = -(4 * a**2 - 1)
    return (coeff * (math.pi / cmath.cosh(z + 1j * a) + math.pi / cmath.cosh(z - 1j * a))).real


def boundary_excitation_energy(a_str, p):
    a = parse_a(a_str)
    coeff = -math.pi * (4 * a**2 - 1)
    p_abs = abs(p)
    return (coeff * (1 / cmath.sin(math.pi * (p_abs + a)) + 1 / cmath.sin(math.pi * (p_abs - a)))).real


def ferromagnetic_surface_energy(a_str, p, q, xi):
    a = parse_a(a_str)
    q_bar = q / math.sqrt(1 + xi**2)
    p_abs = abs(p)
    q_bar_abs = abs(q_bar)
    coeff = (4 * a**2 - 1) / 2
    term1 = 2 * p_abs / (p**2 - a**2)
    term2 = 2 * q_bar_abs / (q_bar**2 - a**2)
    term3 = 2 / (1 - a**2)
    term4 = 1 / (0.25 - a**2)
    return (coeff * (term1 + term2 + term3 - term4)).real


# Parameter tuples
SURFACE_TUPLES = [
    ('0',    0.1, 0.1, 0.5),
    ('0',    0.5, 0.5, 1.2),
    ('0.6i', 0.2, 0.3, 0.5),
    ('0.6i', 0.5, 0.5, 1.2),
    ('0.6i', 0.7, 0.7, 1.2),
    ('0.8i', 0.3, 0.4, 0.5),
    ('0.8i', 0.6, 0.6, 1.2),
    ('0.8i', 0.9, 0.9, 1.2),
]

BULK_TUPLES = [
    ('0', -2.0),
    ('0', -1.0),
    ('0',  0.0),
    ('0',  1.0),
    ('0',  2.0),
    ('0.6i', -2.0),
    ('0.6i', -1.0),
    ('0.6i',  0.0),
    ('0.6i',  1.0),
    ('0.6i',  2.0),
    ('0.8i', -2.0),
    ('0.8i', -1.0),
    ('0.8i',  0.0),
    ('0.8i',  1.0),
    ('0.8i',  2.0),
]

BOUNDARY_TUPLES = [
    ('0',    0.1),
    ('0',    0.3),
    ('0',    0.45),
    ('0.6i', 0.1),
    ('0.6i', 0.25),
    ('0.6i', 0.45),
    ('0.8i', 0.1),
    ('0.8i', 0.3),
    ('0.8i', 0.45),
]

def write_surface_energy(path):
    rows = []
    for a_str, p, q, xi in SURFACE_TUPLES:
        e_b = surface_energy(a_str, p, q, xi)
        rows.append({"a": a_str, "p": p, "q": q, "xi": xi, "E_b": float(e_b)})
    with open(path, 'w') as f:
        json.dump(rows, f, indent=2)

def write_bulk_excitation(path):
    rows = []
    for a_str, z in BULK_TUPLES:
        energy = bulk_excitation_energy(a_str, z)
        rows.append({"a": a_str, "z": z, "energy": float(energy)})
    with open(path, 'w') as f:
        json.dump(rows, f, indent=2)

def write_boundary_excitation(path):
    rows = []
    for a_str, p in BOUNDARY_TUPLES:
        energy = boundary_excitation_energy(a_str, p)
        rows.append({"a": a_str, "p": p, "energy": float(energy)})
    with open(path, 'w') as f:
        json.dump(rows, f, indent=2)

def write_ferromagnetic_surface(path):
    rows = []
    for a_str, p, q, xi in SURFACE_TUPLES:
        e_b_ferr = ferromagnetic_surface_energy(a_str, p, q, xi)
        rows.append({"a": a_str, "p": p, "q": q, "xi": xi, "E_b_ferr": float(e_b_ferr)})
    with open(path, 'w') as f:
        json.dump(rows, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: compute.py <output_file> <mode>", file=sys.stderr)
        sys.exit(1)
    outpath = sys.argv[1]
    mode = sys.argv[2]
    if mode == "surface_energy":
        write_surface_energy(outpath)
    elif mode == "bulk_excitation":
        write_bulk_excitation(outpath)
    elif mode == "boundary_excitation":
        write_boundary_excitation(outpath)
    elif mode == "ferromagnetic_surface":
        write_ferromagnetic_surface(outpath)
    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)
