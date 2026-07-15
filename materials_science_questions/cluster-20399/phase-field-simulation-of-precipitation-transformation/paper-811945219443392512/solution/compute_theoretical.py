import csv
import math
import scipy.integrate as integrate
from scipy.optimize import root_scalar

def integrand(u, lam, ra, rb):
    denom = math.sqrt((u**2 - ra**2) * (u**2 - rb**2))
    if denom == 0.0:
        return 0.0
    return math.exp(-lam**2 * u**2) / denom

def compute_lambda(S, ra, rb):
    """Solve for lambda given supersaturation S and geometry parameters."""
    # For sphere, S = 2*lam^2*exp(lam^2)*int_1^inf exp(-lam^2 u^2)/u^2 du
    # For ellipsoids, the formula as in the paper.
    factor = math.sqrt((1 - ra**2) * (1 - rb**2))  # as in equation

    def eq(lam):
        if lam <= 0.0:
            return float('inf')
        I, err = integrate.quad(integrand, 1.0, math.inf, args=(lam, ra, rb), limit=200)
        rhs = 2.0 * lam**2 * math.exp(lam**2) * factor * I
        return S - rhs

    # bracket for lambda: start small, increase up to large values if needed
    lo, hi = 1e-5, 10.0
    # find a bracket
    f_lo = eq(lo)
    f_hi = eq(hi)
    if f_lo * f_hi > 0:
        # try wider bracket
        hi = 50.0
        f_hi = eq(hi)
        if f_lo * f_hi > 0:
            lo = 1e-6
            f_lo = eq(lo)
            if f_lo * f_hi > 0:
                # fallback: use very large hi
                hi = 100.0
                f_hi = eq(hi)
                if f_lo * f_hi > 0:
                    raise RuntimeError("Cannot bracket root for S=%f, ra=%f, rb=%f" % (S, ra, rb))
    sol = root_scalar(eq, bracket=[lo, hi], method='bisect', xtol=1e-12)
    return sol.root

def main():
    # read supersaturation
    supersat = {}
    with open('/solution/supersaturation.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            T = float(row['temperature'])
            S = float(row['S'])
            supersat[T] = S

    # read carbon diffusivity
    diffusivity = {}
    with open('/solution/carbon_diffusivity.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            T = float(row['temperature'])
            D = float(row['D'])
            diffusivity[T] = D

    morphologies = [
        {
            'name': 'idiomorph',
            'v': 1.0,
            'ra': 0.0,
            'rb': 0.0
        },
        {
            'name': 'face_allotriomorph',
            'v': 1.0/3.0,
            'ra': 0.0,
            'rb': math.sqrt(1.0 - (1.0/3.0)**2)
        },
        {
            'name': 'edge_allotriomorph',
            'v': 1.0/3.0,
            'ra': math.sqrt(1.0 - (1.0/3.0)**2),
            'rb': math.sqrt(1.0 - (1.0/3.0)**2)
        }
    ]

    out_rows = []
    for T, S in supersat.items():
        if T not in diffusivity:
            raise ValueError(f"Temperature {T} not found in diffusivity data")
        D = diffusivity[T]
        for morph in morphologies:
            lam = compute_lambda(S, morph['ra'], morph['rb'])
            k = 2.0 * math.sqrt(D) * morph['v'] * lam
            out_rows.append({
                'morphology_type': morph['name'],
                'temperature': T,
                'theoretical_k': k
            })

    # sort rows by temperature and morphology for reproducibility
    out_rows.sort(key=lambda x: (x['temperature'], x['morphology_type']))

    with open('/app/outputs/step_01_theoretical_k.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['morphology_type', 'temperature', 'theoretical_k'])
        writer.writeheader()
        writer.writerows(out_rows)

if __name__ == '__main__':
    main()
