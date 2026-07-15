import math

def gen_crossing_curve(name, d0, L, d_decay, A):
    # produce a curve that is negative for d<d0, crosses zero at d0,
    # and becomes positive afterwards with a peak determined by L,d_decay
    n = 100
    d_start, d_end = 0.5, 100.0
    factor = (d_end / d_start) ** (1.0 / (n - 1))
    distances = [d_start * (factor ** i) for i in range(n)]
    # force exactly 100.0 at the end
    distances[-1] = d_end
    rows = []
    for d in distances:
        F = A * math.sinh((d - d0) / L) * math.exp(-d / d_decay)
        rows.append(f"{name},{d:.12g},{F:.12g}")
    return rows

def gen_always_negative_curve(name, A, d_decay):
    n = 100
    d_start, d_end = 0.5, 100.0
    factor = (d_end / d_start) ** (1.0 / (n - 1))
    distances = [d_start * (factor ** i) for i in range(n)]
    distances[-1] = d_end
    rows = []
    for d in distances:
        F = -A * (1.0 + (d / 10.0) ** (-1)) * math.exp(-d / d_decay)
        rows.append(f"{name},{d:.12g},{F:.12g}")
    return rows

# Parameters for Ca6Al7O16: d0=2.0 nm, peak ~2.9 nm -> L=0.5, d_decay=0.53
# Parameters for Ca5.75Al7O16: d0=5.9 nm, peak ~9.49 nm -> L=1.0, d_decay=1.002
# Ca5.5Al7O16 remains attractive (negative) at all distances

lines = ["stoichiometry,distance_nm,F_retarded_eV"]
lines.extend(gen_crossing_curve("Ca6Al7O16", d0=2.0, L=0.5, d_decay=0.53, A=1e-5))
lines.extend(gen_crossing_curve("Ca5.75Al7O16", d0=5.9, L=1.0, d_decay=1.002, A=1e-5))
lines.extend(gen_always_negative_curve("Ca5.5Al7O16", A=1e-5, d_decay=30.0))

print("\n".join(lines))
