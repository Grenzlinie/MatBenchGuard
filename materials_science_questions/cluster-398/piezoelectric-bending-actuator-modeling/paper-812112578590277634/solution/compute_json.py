import math
import json
import sys

def compute_nu(Q):
    return math.sqrt(1.0 - 1.0/(4.0*Q*Q))

def compute_ustat(eta, Q, gamma, alpha=1.0, Cp=1.0, xhat=1.0):
    nu = compute_nu(Q)
    if nu <= 0:
        raise ValueError("Q too small")
    exp_term = math.exp(-math.pi/(2.0*Q*nu))
    denom = 1.0 - exp_term
    if denom == 0:
        raise ValueError("unexpected zero denominator")
    
    eta_pi = math.pi * eta
    half_eta_pi = eta_pi / 2.0
    
    # first term (SSDI)
    term1_num = math.cos(half_eta_pi) + (1.0 + exp_term) * (nu * eta / math.pi) * math.sin(eta_pi / (2.0*nu))
    term1 = 2.0 * (alpha / Cp) * term1_num / denom * xhat
    
    # second term (voltage source)
    term2 = ((1.0 + exp_term) / denom) * gamma * xhat   # V_s = gamma * xhat
    
    return term1 + term2

def main():
    # 1. Voltage table: define a set of parameter tuples (eta, Q, a, b, gamma)
    # The approximate formulas (21)/(22) assume optimal switching a=0, b=1/(2ν),
    # but a,b are still recorded.  α=Cp=1, x_p_hat=1.
    tuples = []
    # mix of parameters
    etas = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
    Qs = [5, 10, 20]
    for eta in etas:
        for Q in Qs:
            nu = compute_nu(Q)
            bopt = 1.0/(2.0*nu)
            # optimal a=0, b=1/(2ν)
            tuples.append((eta, Q, 0.0, bopt, 0.0))
            # also a non-zero gamma case
            if eta == 0.5 and Q == 10:
                tuples.append((eta, Q, 0.25, bopt, 0.0))  # heuristic a
                tuples.append((eta, Q, 0.0, bopt, 0.5))
                tuples.append((eta, Q, 0.0, bopt, 0.2))
    # add a few more with non-optimal b
    tuples.append((0.5, 10, 0.0, 0.3, 0.0))
    tuples.append((0.5, 10, 0.0, 0.7, 0.0))
    tuples.append((0.3, 8, 0.0, 1.0/(2.0*compute_nu(8)), 0.0))
    
    voltage_table = []
    for eta, Q, a, b, gamma in tuples:
        u = compute_ustat(eta, Q, gamma)
        voltage_table.append({
            "eta": eta,
            "Q": Q,
            "a": a,
            "b": b,
            "u_stat": u
        })
    
    # 2. Optimal switching law for baseline eta=0.5, Q=10, gamma=0
    Q_baseline = 10
    eta_baseline = 0.5
    nu_baseline = compute_nu(Q_baseline)
    b_opt = 1.0/(2.0*nu_baseline)
    a_opt = 0.0
    peak_voltage = compute_ustat(eta_baseline, Q_baseline, 0.0)
    optimal_law = {
        "a_opt": a_opt,
        "b_opt": b_opt,
        "peak_voltage": peak_voltage
    }
    
    # 3. Equivalence: compute alpha_eff and compare to alpha + Cp*gamma
    gamma_test = 0.5
    u_with = compute_ustat(eta_baseline, Q_baseline, gamma_test)
    u_without = peak_voltage  # gamma=0
    # u_stat = k1*alpha + k2*gamma, with k1,k2 derived from formula
    # k1 = (term1 evaluated with alpha=1, xhat=1, gamma=0) / 1 = u_without (since alpha=1, gamma=0)
    # k2 = (u_with - u_without)/gamma_test
    k1 = u_without
    if u_without == 0:
        k2 = 0
    else:
        k2 = (u_with - u_without) / gamma_test
    
    # Effective alpha such that u_stat(alpha_eff, gamma=0) == u_stat(alpha=1, gamma=gamma_test)
    # u_stat(alpha_eff,0) = k1 * alpha_eff
    # u_stat(1,gamma_test) = k1*1 + k2*gamma_test
    # => alpha_eff = 1 + (k2/k1)*gamma_test
    if k1 == 0:
        alpha_eff = 1.0
    else:
        alpha_eff = 1.0 + (k2/k1) * gamma_test
    alpha_plus = 1.0 + gamma_test  # Cp=1, alpha=1
    tol = 1e-5
    match = abs(alpha_eff - alpha_plus) / max(abs(alpha_plus), 1e-12) <= tol
    
    equivalence = {
        "gamma": gamma_test,
        "alpha_eff": alpha_eff,
        "alpha_plus": alpha_plus,
        "match": match
    }
    
    result = {
        "voltage_table": voltage_table,
        "optimal_law": optimal_law,
        "equivalence": equivalence
    }
    json.dump(result, sys.stdout, indent=2)

if __name__ == "__main__":
    main()
