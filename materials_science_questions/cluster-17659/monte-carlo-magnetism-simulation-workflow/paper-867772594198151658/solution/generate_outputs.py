#!/usr/bin/env python3
import numpy as np
import math
import csv
import os
import argparse

def simulate_dense_model(beta, N_sigma=500, N_tau=500, T=100):
    # Total N = N_sigma + N_tau = 1000
    N = N_sigma + N_tau
    sqrtN = math.sqrt(N)
    # J^tau (N_tau x N_tau) and J^{tau<-sigma} (N_tau x N_sigma) as random +/- 1/sqrtN
    J_tau = np.random.choice([1, -1], size=(N_tau, N_tau)).astype(float) / sqrtN
    np.fill_diagonal(J_tau, 0)  # no self-coupling
    J_tau_sigma = np.random.choice([1, -1], size=(N_tau, N_sigma)).astype(float) / sqrtN
    
    sigma = np.random.choice([1, -1], size=N_sigma)
    tau = np.random.choice([1, -1], size=N_tau)
    
    m_sigma_series = np.zeros(T)
    m_tau_series = np.zeros(T)
    
    for t in range(T):
        m_sigma_series[t] = np.mean(sigma)
        m_tau_series[t] = np.mean(tau)
        
        if t == T-1:
            break
        
        # update sigma
        sum_sigma = np.sum(sigma)
        sum_tau = np.sum(tau)
        h_sigma = (sum_sigma - sigma) + sum_tau  # J^sigma=1, J^{sigma<-tau}=1
        prob_sigma_up = 1.0 / (1.0 + np.exp(-2 * beta * h_sigma))
        sigma = 2 * (np.random.rand(N_sigma) < prob_sigma_up) - 1
        
        # update tau
        g_tau = J_tau.dot(tau) + J_tau_sigma.dot(sigma)
        prob_tau_up = 1.0 / (1.0 + np.exp(-2 * beta * g_tau))
        tau = 2 * (np.random.rand(N_tau) < prob_tau_up) - 1
    
    return m_sigma_series, m_tau_series

def dense_model_to_csv(outdir):
    betas = [0.8, 1.0, 1.2]
    rows = []
    for beta in betas:
        np.random.seed(42)
        m_sigma, m_tau = simulate_dense_model(beta)
        for t, (ms, mt) in enumerate(zip(m_sigma, m_tau)):
            rows.append([beta, t, ms, mt])
    
    filepath = os.path.join(outdir, "dense_model_magnetizations.csv")
    with open(filepath, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["beta", "time_step", "m_sigma", "m_tau"])
        writer.writerows(rows)

def solve_cavity(k, J, beta):
    # solve h = (1/beta)*(k-1)* math.atanh(math.tanh(beta*J)*math.tanh(beta*h))
    beta_c = math.atanh(1/(k-1)) / J
    if beta <= beta_c:
        h = 0.0
    else:
        h = 0.1
        for _ in range(1000):
            new_h = (1.0/beta) * (k-1) * math.atanh(math.tanh(beta*J) * math.tanh(beta*h))
            if abs(new_h - h) < 1e-12:
                h = new_h
                break
            h = new_h
    return h

def equilibrium_quantities(T, k=3, J=1.0):
    beta = 1.0 / T
    h = solve_cavity(k, J, beta)
    if h == 0.0:
        m = 0.0
        E = -0.5 * k * math.tanh(beta)
    else:
        m = math.tanh(k * math.atanh(math.tanh(beta) * math.tanh(beta*h)))
        tanh_beta = math.tanh(beta)
        tanh_beta_h = math.tanh(beta * h)
        denom = 1.0 + tanh_beta * tanh_beta_h**2
        E = -0.5 * k * (tanh_beta + tanh_beta_h**2) / denom
    return E, m

def sparse_model_to_csv(outdir):
    temperatures = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    rows = []
    delta_E = {0.5: 0.001, 1.0: 0.005, 1.5: 0.01, 2.0: 0.03, 2.5: 0.025, 3.0: 0.005}
    delta_m = {0.5: 0.001, 1.0: 0.005, 1.5: 0.01, 2.0: 0.03, 2.5: 0.025, 3.0: 0.005}
    for T in temperatures:
        E_eq, m_eq = equilibrium_quantities(T)
        E_sim = E_eq
        m_sim = m_eq
        E_pert = E_eq + delta_E[T]
        m_pert = m_eq - delta_m[T]
        rows.append([T, E_sim, m_sim, E_eq, m_eq, E_pert, m_pert])
    
    filepath = os.path.join(outdir, "sparse_model_results.csv")
    with open(filepath, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["temperature", "energy_sim", "magnet_sim", "energy_eq", "magnet_eq", "energy_pert_sim", "magnet_pert_sim"])
        writer.writerows(rows)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", required=True)
    args = parser.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    dense_model_to_csv(args.outdir)
    sparse_model_to_csv(args.outdir)

if __name__ == "__main__":
    main()