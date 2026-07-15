#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: single_reinforced_yield_curve.csv ===
python3 -c '
import csv, math

gamma = 0.2
rho = 0.3

# generate eta points from -1 to 1 step 0.01, plus extra points for the subdifferential segment at eta=rho
eta_points = []

# dense grid: -1 to 1 step 0.01
eta = -1.0
while eta <= 1.0 + 1e-9:
    eta_points.append(round(eta, 6))
    eta += 0.01

# replace the point at eta=rho with a few points along the straight segment
# endpoints:
eta_rho = rho
n_tension = gamma - (1.0 + eta_rho) / 2.0
m_tension = 2.0 * gamma * rho + (1.0 - eta_rho**2) / 2.0
n_compression = -gamma - (1.0 + eta_rho) / 2.0
m_compression = -2.0 * gamma * rho + (1.0 - eta_rho**2) / 2.0

rows = []
seen_rho = False
for eta in eta_points:
    if abs(eta - rho) < 1e-6:
        seen_rho = True
        # generate 11 points on the segment
        for i in range(11):
            s = i / 10.0
            n = n_tension + s * (n_compression - n_tension)
            m = m_tension + s * (m_compression - m_tension)
            rows.append((eta, round(n, 8), round(m, 8)))
    elif eta < rho:
        # fully in tension
        n = gamma - (1.0 + eta) / 2.0
        m = 2.0 * gamma * rho + (1.0 - eta**2) / 2.0
        rows.append((eta, round(n, 8), round(m, 8)))
    else:
        # fully in compression
        n = -gamma - (1.0 + eta) / 2.0
        m = -2.0 * gamma * rho + (1.0 - eta**2) / 2.0
        rows.append((eta, round(n, 8), round(m, 8)))

# write csv
with open("/app/outputs/single_reinforced_yield_curve.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["eta", "n", "m"])
    w.writerows(rows)
'

# === solve block: double_reinforced_yield_curve.csv ===
python3 -c '
import csv, math

gamma = 0.2
rho = 0.3

# outer regime (eta < -rho or eta > rho): n = -(1+eta)/2 - 2*gamma, m = (1-eta**2)/2
# inner regime (-rho < eta < rho): n = -(1+eta)/2, m = (1-eta**2)/2 + 4*gamma*rho
# straight segments at eta = -rho and eta = rho

eta_points = []
eta = -1.0
while eta <= 1.0 + 1e-9:
    eta_points.append(round(eta, 6))
    eta += 0.01

rows = []

for eta in eta_points:
    if abs(eta + rho) < 1e-6:
        # segment at eta = -rho:
        # endpoints: outer regime at eta = -rho yields
        n_outer = -(1.0 + (-rho)) / 2.0 - 2.0 * gamma
        m_outer = (1.0 - (-rho)**2) / 2.0
        # inner regime at eta = -rho yields
        n_inner = -(1.0 + (-rho)) / 2.0
        m_inner = (1.0 - (-rho)**2) / 2.0 + 4.0 * gamma * rho
        for i in range(11):
            s = i / 10.0
            n = n_outer + s * (n_inner - n_outer)
            m = m_outer + s * (m_inner - m_outer)
            rows.append((eta, round(n, 8), round(m, 8)))
    elif abs(eta - rho) < 1e-6:
        # segment at eta = rho:
        # endpoints: inner regime at eta = rho
        n_inner = -(1.0 + rho) / 2.0
        m_inner = (1.0 - rho**2) / 2.0 + 4.0 * gamma * rho
        # outer regime at eta = rho
        n_outer = -(1.0 + rho) / 2.0 - 2.0 * gamma
        m_outer = (1.0 - rho**2) / 2.0
        for i in range(11):
            s = i / 10.0
            n = n_inner + s * (n_outer - n_inner)
            m = m_inner + s * (m_outer - m_inner)
            rows.append((eta, round(n, 8), round(m, 8)))
    elif eta < -rho:
        n = -(1.0 + eta) / 2.0 - 2.0 * gamma
        m = (1.0 - eta**2) / 2.0
        rows.append((eta, round(n, 8), round(m, 8)))
    elif -rho < eta < rho:
        n = -(1.0 + eta) / 2.0
        m = (1.0 - eta**2) / 2.0 + 4.0 * gamma * rho
        rows.append((eta, round(n, 8), round(m, 8)))
    else:
        # eta > rho
        n = -(1.0 + eta) / 2.0 - 2.0 * gamma
        m = (1.0 - eta**2) / 2.0
        rows.append((eta, round(n, 8), round(m, 8)))

with open("/app/outputs/double_reinforced_yield_curve.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["eta", "n", "m"])
    w.writerows(rows)
'
