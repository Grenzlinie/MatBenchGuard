import math, json

def safe_fermi(eps, eta):
    arg = eps - eta
    if arg > 0:
        return math.exp(-arg) / (1.0 + math.exp(-arg))
    else:
        return 1.0 / (1.0 + math.exp(arg))

def integrand(eps, eta, epsilon_t):
    if epsilon_t == 0:
        if eps < 0:
            return 0.0
        return math.sqrt(eps) * safe_fermi(eps, eta)
    else:
        if eps < epsilon_t:
            return math.sqrt(epsilon_t) * math.exp((eps - epsilon_t) / (2.0 * epsilon_t)) * safe_fermi(eps, eta)
        else:
            return math.sqrt(eps) * safe_fermi(eps, eta)

def integrate_trap(f, a, b, n=200000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def compute_F(eta, epsilon_t):
    if epsilon_t == 0:
        L = 0.0
    else:
        L = -20.0 * epsilon_t
    U = max(10.0, eta + 40.0)
    if epsilon_t > U:
        U = epsilon_t + 20.0
    f = lambda eps: integrand(eps, eta, epsilon_t)
    integral = integrate_trap(f, L, U)
    return integral / math.gamma(1.5)

eta_values = [round(-4.0 + 0.5 * i, 2) for i in range(17)]
results = []
for eps_t in (0, 1, 10):
    for eta in eta_values:
        F = compute_F(eta, eps_t)
        results.append({"eta": eta, "epsilon_t": eps_t, "F": round(F, 8)})

with open("/app/outputs/fermi_integral_values.json", "w") as f:
    json.dump(results, f, indent=2)
