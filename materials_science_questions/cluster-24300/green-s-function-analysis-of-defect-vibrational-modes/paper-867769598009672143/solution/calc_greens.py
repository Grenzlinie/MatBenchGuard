import json
import numpy as np
from scipy.integrate import nquad

def main():
    # Parameters from the paper (mu, C) and the band-gap frequency
    mu = 0.01
    C = 0.1
    omega = 9.8
    f_w = -1.0  # out-of-plane force

    def zeta(P, Q):
        """Repeated function zeta(P,Q) from the paper."""
        return -2.0 * C * np.cos(P) + 2.0 * C + 4.0 * np.cos(Q) - mu * omega**2 + 8.0

    def sigma(k1, k2):
        """Dispersion function sigma(omega, k1, k2)."""
        z1 = zeta(k1, k2)
        z2 = zeta(k2, k1)
        term1 = 144.0 * np.sin(k1)**2 * z1
        term2 = 144.0 * np.sin(k2)**2 * z2
        term3 = (24.0 * np.cos(k2) + 24.0 * np.cos(k1) + omega**2 - 48.0) * z1 * z2
        return term1 + term2 + term3

    def WF(k1, k2):
        """Spectral flexural displacement for out-of-plane forcing f_w only."""
        return zeta(k1, k2) * zeta(k2, k1) * f_w / sigma(k1, k2)

    def integrand_real(k2, k1, m, n):
        """
        Integrand real part for the inverse Fourier transform.
        Because WF is real and even, the imaginary part integrates to zero.
        """
        return WF(k1, k2) * np.cos(k1 * m + k2 * n)

    # Integration domain
    a, b = -np.pi, np.pi
    ranges = [[a, b], [a, b]]
    opts = {'epsabs': 1e-12, 'epsrel': 1e-12, 'limit': 200}

    results = []
    for m in range(-2, 3):
        for n in range(-2, 3):
            integral, err = nquad(
                integrand_real,
                ranges,
                args=(m, n),
                opts=[opts, opts]
            )
            w = integral / (4.0 * np.pi**2)
            results.append({"m": m, "n": n, "w": float(w)})

    # Ensure exactly 25 entries
    assert len(results) == 25
    json.dump(results, None, allow_nan=False)

if __name__ == "__main__":
    main()
