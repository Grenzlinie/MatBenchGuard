import json
import math
import numpy as np
from scipy import integrate, special

# parameters (alpha=1, g=1, beta=5, mu=0.4, initial conditions)
c = 2 + 5  # g*beta = 5
times = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
lam3_0 = 0.5
lam1_0 = 0.375
lam2_0 = 0.375
mu = 0.4
mu2 = mu ** 2

# tau
tau = math.sqrt(c)  # sqrt((2+g*beta)/alpha^2) with alpha=1

# eta_inf
z = mu2 * c
eta_inf = mu2 * c * math.exp(z) * special.exp1(z)

def eta(t):
    factor = 4 * c
    def integrand(r):
        sq = np.sqrt(mu2 + r ** 2)
        return r ** 3 / (mu2 + r ** 2) * np.exp(-c * r ** 2) * np.sin(t * sq) ** 2
    val, _ = integrate.quad(integrand, 0, np.inf, limit=200, epsabs=1e-12, epsrel=1e-12)
    return factor * val

def zeta(t):
    factor = 2 * c
    def integrand(r):
        sq = np.sqrt(mu2 + r ** 2)
        return r * np.cos(2 * t * sq) * np.exp(-c * r ** 2)
    val, _ = integrate.quad(integrand, 0, np.inf, limit=200, epsabs=1e-12, epsrel=1e-12)
    return factor * val

def xi(t):
    factor = 2 * c
    def integrand(r):
        sq = np.sqrt(mu2 + r ** 2)
        return r * mu * np.sin(2 * t * sq) / sq * np.exp(-c * r ** 2)
    val, _ = integrate.quad(integrand, 0, np.inf, limit=200, epsabs=1e-12, epsrel=1e-12)
    return factor * val

lambda3 = []
lambda1 = []
for t in times:
    et = eta(t)
    zt = zeta(t)
    xt = xi(t)
    l3 = lam3_0 * (1 - et)
    l1 = lam1_0 * (zt + et / 2) + lam2_0 * xt
    lambda3.append(l3)
    lambda1.append(l1)

result = {
    "t": times,
    "lambda3": lambda3,
    "lambda1": lambda1,
    "eta_inf": eta_inf,
    "tau": tau
}

with open("/app/outputs/bloch_vector_results.json", "w") as f:
    json.dump(result, f, indent=2)
