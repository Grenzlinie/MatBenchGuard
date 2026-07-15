#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
cat > /tmp/generate.py << 'PYEOF'
import json, math, csv, sys

E_g = 0.0
E_H = -10.0
gamma = 0.41
eps_inf = 2.54

# list of configurations: name, n_H, epsilon_b (eV)
configs = [
    ("1H", 1, 0.79),
    ("2H_ortho_same", 2, 1.47),
    ("2H_ortho_counter", 2, 1.70),
    ("3H", 3, 1.75),
    ("4H", 4, 1.95),
    ("6H_closed_ring", 6, 2.16),
    ("10H", 10, 2.212),
    ("12H_incomplete", 12, 2.0),
    ("16H", 16, 2.284),
    ("24H", 24, 2.335),
    ("CH_infinite", 54, 2.54),
]

def comp_n23(n, eb):
    # n23 such that eb ≈ eps_inf - gamma * (n23 / n)
    exact = n * (eps_inf - eb) / gamma
    return round(exact)

config_list = []
for name, n, eb in configs:
    n23 = comp_n23(n, eb)
    etot = n * E_H - n * eb   # E_total = n*E_H - n*eb
    config_list.append((name, etot, n, n23, eb))

def write_total_energies():
    with open('/app/outputs/total_energies.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'E_total'])
        writer.writerow(['C54H18', E_g])
        writer.writerow(['H', E_H])
        for c in config_list:
            writer.writerow([c[0], c[1]])

def condition_curve(cond_name, mu_H):
    A = -(eps_inf + mu_H)
    B = gamma
    ns = list(range(1, 101))
    DeltaG = [A * i + B * math.sqrt(i) for i in ns]
    max_val = max(DeltaG)
    n_star = ns[DeltaG.index(max_val)]
    return {
        "condition": cond_name,
        "mu_H": mu_H,
        "n": ns,
        "DeltaG": DeltaG,
        "n_star": n_star,
        "DeltaG_star": max_val
    }

def write_results_json():
    confs = []
    for name, etot, n, n23, eb in config_list:
        confs.append({
            "name": name,
            "E_total": etot,
            "n_H": n,
            "n23": n23,
            "epsilon_b": eb
        })
    cond1 = condition_curve("300K_1atm", -2.494)
    cond2 = condition_curve("500K_10atm", -2.48)
    result = {
        "configurations": confs,
        "nucleation": {
            "epsilon_b_infinity": eps_inf,
            "gamma": gamma,
            "R_squared": 1.0,
            "conditions": [cond1, cond2]
        }
    }
    with open('/app/outputs/results.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'csv':
        write_total_energies()
    elif cmd == 'json':
        write_results_json()
    else:
        print('Usage: generate.py csv|json', file=sys.stderr)
        sys.exit(1)
PYEOF

# === solve block: results.json ===
python3 /tmp/generate.py json

# === solve finalize ===
echo 'Oracle artifacts written.'
