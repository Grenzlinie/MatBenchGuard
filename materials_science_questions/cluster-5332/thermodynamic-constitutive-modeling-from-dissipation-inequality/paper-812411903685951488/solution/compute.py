import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

B0, B1, B2 = 0.16095, 70.2299, 10.0144
alphas = [1e-6, 5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 2e-2]

def temp(t, alpha):
    return 20.0 + 780.0 * np.exp(-alpha * t)

def tau_in(T):
    U = 1.0 / (825.0 - T)
    return 10.0 ** (B0 + B1 * U + B2 * U * U)

def S_trad(T):
    return 1.0

def S_gen(T):
    return 1.083 - 0.00106 * T

def integrand(tu, alpha, S_func):
    if tu == 0.0:
        return 0.0
    Tu = temp(tu, alpha)
    s = S_func(Tu)
    return s * (tu ** (s - 1)) / (tau_in(Tu) ** s)

def G(t, alpha, S_func):
    return quad(integrand, 0, t, args=(alpha, S_func), limit=200, epsabs=1e-12, epsrel=1e-12)[0]

def find_tf(alpha, S_func):
    a = 1e-10
    b = 1.0
    while True:
        if G(b, alpha, S_func) >= 1.0:
            break
        b *= 2.0
        if b > 1e12:
            raise ValueError("Could not bracket root")
    return brentq(lambda t: G(t, alpha, S_func) - 1.0, a, b, xtol=1e-10, rtol=1e-10, maxiter=100)

def main():
    out_path = "/app/outputs/transformation_start_temperatures.csv"
    with open(out_path, "w") as f:
        for alpha in alphas:
            tf_trad = find_tf(alpha, S_trad)
            T_trad = temp(tf_trad, alpha)
            tf_gen = find_tf(alpha, S_gen)
            T_gen = temp(tf_gen, alpha)
            f.write(f"{alpha:.10e},{T_trad:.6f},{T_gen:.6f}\n")

if __name__ == "__main__":
    main()
