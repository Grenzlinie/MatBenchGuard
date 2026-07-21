#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bounded_case_results.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy >/dev/null 2>&1

# Create /solution/generate.py to handle both cases robustly
cat > /solution/generate.py << 'GENEOF'
import sys, numpy as np, math

def run(mode):
    if mode == 'bounded':
        t1_val = 0.8
        b_val = 0.9
    elif mode == 'unbounded':
        t1_val = 1.2
        b_val = 1.5
    else:
        sys.exit(1)
    N = 610
    t2 = 1.0
    alpha = (math.sqrt(5) - 1) / 2
    theta = 0.0
    L = 2 * N
    Lprime = N
    start_trace = N // 2
    end_trace = start_trace + N
    Gamma = np.kron(np.eye(N), np.array([[1, 0], [0, -1]]))
    lambs = np.arange(0, 6.1, 0.1)
    print('lambda,winding_number,ln_gap,lyapunov_exponent')
    for lam in lambs:
        n_vals = np.arange(1, N + 1)
        cos_term = np.cos(2 * math.pi * alpha * n_vals + theta)
        # sanitize: replace inf/nan that arise from division by (near)zero in unbounded case
        with np.errstate(divide='ignore', invalid='ignore'):
            raw = lam * cos_term / (1.0 - b_val * cos_term)
        raw = np.nan_to_num(raw, nan=0.0, posinf=1e10, neginf=-1e10)
        t1_prime = t1_val + raw
        # Lyapunov exponent
        log_arg = np.abs(t1_prime)
        log_arg[log_arg < 1e-300] = 1e-300   # avoid log(0)
        gamma_val = float(np.abs(np.mean(np.log(log_arg))))

        # OBC Hamiltonian
        H = np.zeros((L, L), dtype=float)
        for i in range(N):
            H[2*i, 2*i+1] = t1_prime[i]
            H[2*i+1, 2*i] = t1_prime[i]
            if i < N - 1:
                H[2*(i+1), 2*i+1] = t2
                H[2*i+1, 2*(i+1)] = t2
        eigvals, eigvecs = np.linalg.eigh(H)
        mask = eigvals < 0
        P = eigvecs[:, mask] @ eigvecs[:, mask].T
        Q = P - Gamma @ P @ Gamma
        X = np.diag(np.repeat(np.arange(1, N + 1), 2))
        comm = Q @ X - X @ Q
        M = Gamma @ Q @ comm
        tr = np.trace(M[start_trace:end_trace, start_trace:end_trace])
        nu = int(round(tr / Lprime))

        # PBC Hamiltonian
        H_pbc = np.zeros((L, L), dtype=float)
        for i in range(N):
            H_pbc[2*i, 2*i+1] = t1_prime[i]
            H_pbc[2*i+1, 2*i] = t1_prime[i]
            j = (i + 1) % N
            H_pbc[2*j, 2*i+1] = t2
            H_pbc[2*i+1, 2*j] = t2
        eigvals_pbc = np.linalg.eigvalsh(H_pbc)
        gap = eigvals_pbc[N] - eigvals_pbc[N-1]
        ln_gap = float(np.log(max(gap, 1e-16)))
        print(f"{lam},{nu},{ln_gap},{gamma_val}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    run(sys.argv[1])
GENEOF

# Write bounded_case_results.csv using generate.py
python3 /solution/generate.py bounded > "$OUTDIR/bounded_case_results.csv"

# === solve block: unbounded_case_results.csv ===
python3 /solution/generate.py unbounded > /app/outputs/unbounded_case_results.csv
