import math

n = 0.15          # fm^-3
T = 10.0          # MeV
sigma = 1.0       # MeV·fm^-2
tau = 2.2

# derive r0 from the liquid density n
r0 = (3.0 / (4.0 * math.pi * n)) ** (1.0 / 3.0)

def deltaG(r, S):
    """ΔG(r) from Eq. (6) with the given parameters."""
    term1 = 4.0 * math.pi * r**2 * sigma
    term2 = -(4.0/3.0) * math.pi * r**3 * n * T * math.log(S)
    term3 = 3.0 * T * tau * math.log(r / r0)
    return term1 + term2 + term3

S_values = [2, 3, 4]
r_start = 0.1
r_end   = 10.0
r_step  = 0.01

with open('/app/outputs/free_energy_curves.csv', 'w') as f:
    f.write('S,r,DeltaG\n')
    for S in S_values:
        r = r_start
        while r <= r_end + 1e-12:
            dg = deltaG(r, S)
            f.write(f'{S},{r:.6f},{dg:.6f}\n')
            r += r_step
