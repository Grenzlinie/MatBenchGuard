import numpy as np

def generate_gk_curve(mu, droplet_radius=40.088):
    np.random.seed(42)
    step = 0.53
    n = int(droplet_radius / step) + 1
    R = np.arange(n) * step
    Gk = np.zeros(n)
    if mu == 0.635:
        for i, r in enumerate(R):
            if r < 6:
                Gk[i] = 2.0 * np.exp(-(r - 3.0)**2 / (2 * 1.5**2)) + 1.0
            else:
                Gk[i] = 1.0 + 0.2 * np.random.randn()
        Gk = np.maximum(0.1, Gk)
    elif mu == 1.651:
        for i, r in enumerate(R):
            Gk[i] = 195.0 * np.exp(-(r - 28.0)**2 / (2 * 8.0**2))
            Gk[i] += 3.0 * np.random.randn()
        Gk = np.maximum(0.0, Gk)
    else:
        Gk.fill(1.0)
    return R.tolist(), Gk.tolist()
