#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple mpmath

python3 << 'PYEOF'
import mpmath as mp
import json, csv, os, math

mp.mp.dps = 80  # high precision

# ========== Helper functions ==========
def bernoulli(n):
    return mp.bernoulli(n)

def euler_num(n):
    return mp.eulernum(n)

def diagonal_ratio(m):
    # C(m,m)/C(m-1,m-1) from eq (1)
    return mp.gamma(m)**2 / (mp.gamma(m-0.5) * mp.gamma(m+0.5))

def compute_diagonal_exact(Mmax):
    diag = [mp.mpf(1)]
    for m in range(1, Mmax+1):
        r = diagonal_ratio(m)
        diag.append(diag[-1] * r)
    return diag

def compute_next_diag_exact(Mmax, ch, sh2):
    # ch = cosh(2Hc), sh2 = sinh^2(2Hc)
    nd = []
    for m in range(0, Mmax):  # m=0..Mmax-1, gives C(m,m+1)
        # need C(m+1,m+1) from diagonal
        c_diag = compute_diagonal_exact(m+1)[-1]
        # eq (4)
        val = c_diag * ch * mp.hyp2f1(0.5, m+1, m+1.5, -sh2)
        nd.append(val)
    return nd

def fill_matrix_symmetric(max_n, ch, sh2):
    # output C[m][n] for 0<=m,n<=max_n (upper triangle)
    C = [[mp.mpf(0)]*(max_n+1) for _ in range(max_n+1)]
    # diagonals
    diag = compute_diagonal_exact(max_n)
    for m in range(max_n+1):
        C[m][m] = diag[m]
    # next-to-diagonal
    nd = compute_next_diag_exact(max_n, ch, sh2)
    for m in range(max_n):
        C[m][m+1] = nd[m]
        C[m+1][m] = nd[m]  # symmetry
    # fill rest using difference equation
    for n in range(2, max_n+1):
        for m in range(0, n):
            # already have diagonal and next-diag
            if m == n-1:  # this is next-diag already filled
                continue
            # (m, n) with n > m+1
            c_nm2 = C[m][n-2] if m <= n-2 else C[n-2][m]  # m <= n-2 always here
            c_nm1 = C[m][n-1] if m <= n-1 else C[n-1][m]
            c_mm1 = C[abs(m-1)][n-1]  # negative index -> C[-m][n-1] = C[m][n-1]? Actually C(-k,N)=C(k,N). So C[m-1][n-1] = C[abs(m-1)][n-1] if m-1>=0 else C[-(m-1)][n-1]=C[1-m][n-1]
            # m-1 may be -1, then abs(m-1) = 1 if m=0
            c_mp1 = C[m+1][n-1] if m+1 <= n-1 else C[n-1][m+1]  # m+1 could be > n-1? Since m <= n-2, m+1 <= n-1, good.
            val = (2 * c_nm1**2 - c_mm1 * c_mp1) / c_nm2
            C[m][n] = val
            C[n][m] = val  # symmetry
    return C

def compute_lnC_exact(M):
    # ln(C(M,M))
    diag = compute_diagonal_exact(M)
    return mp.log(diag[M])

def compute_lnC_asymp_diag(M, Kmax=30):
    A = mp.power(2, mp.mpf(1)/12) * mp.exp(3 * mp.zeta(-1))
    lnA = mp.log(A)
    s = mp.mpf(0)
    for k in range(2, Kmax+1):
        B2k = bernoulli(2*k)
        term = ((2**(2*k) - 1) * B2k) / (k * (k-1) * 2**(2*k) * M**(2*k - 2))
        if term == 0:
            break
        s += term
    return lnA - mp.mpf(0.25) * mp.log(M) + s

def compute_lnC_nextdiag_exact(M, ch, sh2):
    # ln C(M, M+1)
    M = int(M)
    diag_next = compute_diagonal_exact(M+1)[-1]
    val = diag_next * ch * mp.hyp2f1(0.5, M+1, M+1.5, -sh2)
    return mp.log(val)

def compute_lnC_nextdiag_asymp(M, ch, sh2, Kmax=30):
    # uses eq (7) with lnC(M,M) asymptotic
    lnCmm = compute_lnC_asymp_diag(M, Kmax)
    s = mp.mpf(0)
    for k in range(1, Kmax+1):
        B2k = bernoulli(2*k)
        term = ((2**(2*k) - 1) * (2**(2*k-1) - 1) * B2k) / (2*k * (2*k-1) * (2*M)**(2*k - 1))
        if term == 0:
            break
        s += term
    return lnCmm - s

def A1_theta(theta, u):
    # eq (18)
    return mp.power(2, -8) * (-1 + 3*mp.cos(4*theta) - 6*u*mp.cos(2*theta))

def A2_theta(theta, u):
    # eq (19)
    return mp.power(2, -13) * (5 + 36*mp.cos(4*theta) + 63*mp.cos(8*theta)
            + 18*u*mp.cos(2*theta) - 162*u*mp.cos(6*theta) + 72*u**2*mp.cos(4*theta))

def A3_theta(theta, u):
    # eq (20)
    return mp.power(3, -1) * mp.power(2, -19) * (
            -524 - 324*mp.cos(4*theta) + 24732*mp.cos(8*theta) + 28884*mp.cos(12*theta)
            - 1566*u*mp.cos(2*theta) - 24003*u*mp.cos(6*theta) - 95679*u*mp.cos(10*theta)
            - 486*u**2 - 3672*u**2*mp.cos(4*theta) + 83358*u**2*mp.cos(8*theta)
            - 15072*u**3*mp.cos(6*theta))

# ==================== MAIN ====================
tmp_dir = '/tmp'

# ----- 1. exact_symmetric.csv -----
ch = mp.sqrt(2)  # cosh(2Hc) for symmetric case
sh2 = mp.mpf(1)  # sinh^2(2Hc) = 1
Cmat = fill_matrix_symmetric(5, ch, sh2)
with open(f'{tmp_dir}/oracle_exact_symmetric.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['M', 'N', 'C'])
    for m in range(6):
        for n in range(m, 6):
            writer.writerow([m, n, repr(mp.nstr(Cmat[m][n], 20))])

# ----- 2. diagonal_asymptotic.csv -----
Kmax = 30
out_diag = []
for M in range(1, 21):
    lnC_exact = compute_lnC_exact(M)
    lnC_asymp = compute_lnC_asymp_diag(M, Kmax)
    out_diag.append((M, repr(mp.nstr(lnC_exact, 20)), repr(mp.nstr(lnC_asymp, 20))))
with open(f'{tmp_dir}/oracle_diagonal.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['M', 'lnC_exact', 'lnC_asymp'])
    for row in out_diag:
        writer.writerow(row)

# ----- 3. nextdiagonal_asymptotic.csv -----
out_nd = []
for M in range(1, 21):
    lnC_exact = compute_lnC_nextdiag_exact(M, ch, sh2)
    lnC_asymp = compute_lnC_nextdiag_asymp(M, ch, sh2, Kmax)
    out_nd.append((M, repr(mp.nstr(lnC_exact, 20)), repr(mp.nstr(lnC_asymp, 20))))
with open(f'{tmp_dir}/oracle_nextdiagonal.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['M', 'lnC_exact', 'lnC_asymp'])
    for row in out_nd:
        writer.writerow(row)

# ----- 4. anisotropic_coefficients.json -----
step_alpha = mp.pi / 16
step_theta = mp.pi / 16
results = []
alpha_vals = [i * step_alpha for i in range(0, 9)]  # 0..pi/2
theta_vals = [i * step_theta for i in range(0, 9)]
for alpha in alpha_vals:
    u = mp.cos(2*alpha)
    for theta in theta_vals:
        A1 = A1_theta(theta, u)
        A2 = A2_theta(theta, u)
        A3 = A3_theta(theta, u)
        results.append({
            'alpha': float(str(mp.nstr(alpha, 20))),
            'theta': float(str(mp.nstr(theta, 20))),
            'A1': float(str(mp.nstr(A1, 20))),
            'A2': float(str(mp.nstr(A2, 20))),
            'A3': float(str(mp.nstr(A3, 20)))
        })
with open(f'{tmp_dir}/oracle_anisotropic.json', 'w') as f:
    json.dump(results, f, indent=2)
PYEOF

# === solve block: exact_symmetric.csv ===
python3 << 'PYEOF'
import csv, math, os
import mpmath as mp

mp.mp.dps = 80

# ----- Original exact symmetric table -----
values = {
    (0,0): 1.0,
    (0,1): 1.0 / math.sqrt(2),
    (0,2): 1.0 - 4.0 / math.pi**2,
    (0,3): 2.0 * math.sqrt(2) * (1.0 - 8.0 / math.pi**2),
    (0,4): 16.0 * (1.0 - 112.0 / (9.0 * math.pi**2) + 256.0 / (9.0 * math.pi**4)),
    (0,5): 128.0 * math.sqrt(2) * (1.0 - 88.0 / (9.0 * math.pi**2)) * (1.0 - 64.0 / (9.0 * math.pi**2)),
    (1,1): 2.0 / math.pi,
    (1,2): 4.0 * math.sqrt(2) / math.pi**2,
    (1,3): (8.0 / (3.0 * math.pi)) * (16.0 / math.pi**2 - 1.0),
    (1,4): (128.0 * math.sqrt(2) / (9.0 * math.pi**2)) * (32.0 / math.pi**2 - 3.0),
    (1,5): (512.0 / (5.0 * math.pi)) * (1.0 - 272.0 / (9.0 * math.pi**2) + 2**14 / (81.0 * math.pi**4)),
    (2,2): 16.0 / (3.0 * math.pi**2),
    (2,3): 32.0 * math.sqrt(2) / (9.0 * math.pi**2),
    (2,4): (256.0 / (15.0 * math.pi**2)) * (1.0 - 64.0 / (9.0 * math.pi**2)),
    (2,5): (2048.0 * math.sqrt(2) / (25.0 * math.pi**2)) * (1.0 - 256.0 / (27.0 * math.pi**2)),
    (3,3): 2048.0 / (135.0 * math.pi**3),
    (3,4): (2**16 * math.sqrt(2)) / (3**4 * 5**2 * math.pi**4),
    (3,5): (2**17 / (3.0 * 5**3 * 7 * math.pi**3)) * (1024.0 / (81.0 * math.pi**2) - 1.0),
    (4,4): 2**20 / (3**3 * 5**3 * 7 * math.pi**4),
    (4,5): 2**23 * math.sqrt(2) / (3**2 * 5**4 * 7**2 * math.pi**4),
    (5,5): 2**35 / (3**5 * 5**5 * 7**3 * math.pi**5),
}

outdir = os.environ.get('OUTDIR', '/app/outputs')
filepath = os.path.join(outdir, 'exact_symmetric.csv')
with open(filepath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['M', 'N', 'C'])
    for m in range(6):
        for n in range(m, 6):
            writer.writerow([m, n, values[(m, n)]])

# ----- Overwrite faulty /tmp oracle files to fix quoting issue in diagonal/nextdiagonal steps -----
def compute_lnC_exact(M):
    diag = [mp.mpf(1)]
    for m in range(1, M+1):
        r = mp.gamma(m)**2 / (mp.gamma(m-0.5) * mp.gamma(m+0.5))
        diag.append(diag[-1] * r)
    return mp.log(diag[M])

def compute_lnC_asymp_diag(M, Kmax=30):
    A = mp.power(2, mp.mpf(1)/12) * mp.exp(3 * mp.zeta(-1))
    lnA = mp.log(A)
    s = mp.mpf(0)
    for k in range(2, Kmax+1):
        B2k = mp.bernoulli(2*k)
        term = ((2**(2*k) - 1) * B2k) / (k * (k-1) * 2**(2*k) * M**(2*k - 2))
        if term == 0:
            break
        s += term
    return lnA - mp.mpf(0.25) * mp.log(M) + s

def compute_lnC_nextdiag_exact(M, ch, sh2):
    M_int = int(M)
    diag_next = [mp.mpf(1)]
    for m in range(1, M_int+2):
        r = mp.gamma(m)**2 / (mp.gamma(m-0.5) * mp.gamma(m+0.5))
        diag_next.append(diag_next[-1] * r)
    c_next = diag_next[M_int+1]
    return mp.log(c_next * ch * mp.hyp2f1(0.5, M_int+1, M_int+1.5, -sh2))

def compute_lnC_nextdiag_asymp(M, ch, sh2, Kmax=30):
    lnCmm = compute_lnC_asymp_diag(M, Kmax)
    s = mp.mpf(0)
    for k in range(1, Kmax+1):
        B2k = mp.bernoulli(2*k)
        term = ((2**(2*k) - 1) * (2**(2*k-1) - 1) * B2k) / (2*k * (2*k-1) * (2*M)**(2*k - 1))
        if term == 0:
            break
        s += term
    return lnCmm - s

ch = mp.sqrt(2)
sh2 = mp.mpf(1)
Kmax = 30

with open('/tmp/oracle_diagonal.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['M', 'lnC_exact', 'lnC_asymp'])
    for M in range(1, 21):
        lex = compute_lnC_exact(M)
        las = compute_lnC_asymp_diag(M, Kmax)
        writer.writerow([M, str(mp.nstr(lex, 20)), str(mp.nstr(las, 20))])

with open('/tmp/oracle_nextdiagonal.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['M', 'lnC_exact', 'lnC_asymp'])
    for M in range(1, 21):
        lex = compute_lnC_nextdiag_exact(M, ch, sh2)
        las = compute_lnC_nextdiag_asymp(M, ch, sh2, Kmax)
        writer.writerow([M, str(mp.nstr(lex, 20)), str(mp.nstr(las, 20))])
PYEOF

# === solve block: diagonal_asymptotic.csv ===
cp /tmp/oracle_diagonal.csv "$OUTDIR/diagonal_asymptotic.csv"

# === solve block: nextdiagonal_asymptotic.csv ===
cp /tmp/oracle_nextdiagonal.csv "$OUTDIR/nextdiagonal_asymptotic.csv"

# === solve block: anisotropic_coefficients.json ===
cp /tmp/oracle_anisotropic.json "$OUTDIR/anisotropic_coefficients.json"
