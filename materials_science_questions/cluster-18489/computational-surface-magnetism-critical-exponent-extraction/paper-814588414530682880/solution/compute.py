#!/usr/bin/env python3
import argparse, math, csv, sys, itertools

def make_f(omega):
    def f(x, t):
        if t == 0.0:
            if omega == 0.0:
                if x == 0.0:
                    return 0.0
                return 1.0 if x > 0 else -1.0
            else:
                return x / math.sqrt(x*x + omega*omega)
        else:
            if omega == 0.0:
                if x == 0.0:
                    return 0.0
                return math.copysign(1.0, x) * math.tanh(abs(x)/t)
            y = math.sqrt(x*x + omega*omega)
            return (x / y) * math.tanh(y / t)
    return f

def apply_mixed_op(terms, alpha, var):
    new_terms = []
    for c, s, ps, pc in terms:
        # cosh part
        new_terms.append((c * 0.5, s + alpha, ps, pc))
        new_terms.append((c * 0.5, s - alpha, ps, pc))
        # sinh part
        if var == 's':
            np, nq = ps + 1, pc
        elif var == 'c':
            np, nq = ps, pc + 1
        else:
            np, nq = ps, pc
        new_terms.append((c * 0.5, s + alpha, np, nq))
        new_terms.append((-c * 0.5, s - alpha, np, nq))
    return new_terms

def generate_mixed_sequence(alpha_seq, var_seq):
    terms = [(1.0, 0.0, 0, 0)]
    for a, v in zip(alpha_seq, var_seq):
        terms = apply_mixed_op(terms, a, v)
    return terms

def evaluate_terms(terms, f, t, ms, mc):
    val = 0.0
    for coeff, shift, ps, pc in terms:
        if ps == 0 and pc == 0:
            mfactor = 1.0
        else:
            mfactor = (ms ** ps) * (mc ** pc)
        val += coeff * mfactor * f(shift, t)
    return val

def generate_constant_terms(ops):
    terms = [(1.0, 0.0, 0, 0)]
    for typ, alpha in ops:
        new_terms = []
        for c, s, _, _ in terms:
            if typ == 'C':
                new_terms.append((c * 0.5, s + alpha, 0, 0))
                new_terms.append((c * 0.5, s - alpha, 0, 0))
            else:
                new_terms.append((c * 0.5, s + alpha, 0, 0))
                new_terms.append((-c * 0.5, s - alpha, 0, 0))
        terms = new_terms
    return terms

def compute_k(ops, f, t):
    terms = generate_constant_terms(ops)
    return evaluate_terms(terms, f, t, 0.0, 0.0)

def transition_F(t, A, B, C, omega_s, omega_b):
    f_s = make_f(omega_s)
    f_c = make_f(omega_b)
    k1_ops = [('S', A), ('C', A), ('C', B), ('C', C)]
    k2_ops = [('C', A), ('C', A), ('S', B), ('C', C)]
    k3_ops = [('C', A), ('C', A), ('C', B), ('S', C)]
    k4_ops = [('C', B), ('S', C)] + [('C', C)]*5
    k5_ops = [('S', B)] + [('C', C)]*6
    k1 = compute_k(k1_ops, f_s, t)
    k2 = compute_k(k2_ops, f_s, t)
    k3 = compute_k(k3_ops, f_s, t)
    k4 = compute_k(k4_ops, f_c, t)
    k5 = compute_k(k5_ops, f_c, t)
    return (1 - (2*k1 + k2)) * (1 - k5) - 6*k3*k4

def find_all_tc(A, B, C, omega_s, omega_b):
    roots = []
    t_prev = 0.0
    f_prev = None
    for t in [0.001 + i*0.01 for i in range(2000)]:
        f = transition_F(t, A, B, C, omega_s, omega_b)
        if f_prev is not None and f_prev * f < 0:
            a, b = t_prev, t
            fa, fb = f_prev, f
            for _ in range(50):
                mid = (a + b) / 2
                fmid = transition_F(mid, A, B, C, omega_s, omega_b)
                if fmid == 0 or (b - a) < 1e-12:
                    roots.append(mid)
                    break
                if fa * fmid < 0:
                    b, fb = mid, fmid
                else:
                    a, fa = mid, fmid
        t_prev = t
        f_prev = f
    uniq = []
    for r in roots:
        if not any(abs(r - u) < 1e-6 for u in uniq):
            uniq.append(r)
    return sorted(uniq) if uniq else [0.0]

def mode_t_c_vs_delta_s(outpath):
    ds_vals = [i*0.5 for i in range(11)]
    r_vals = [0.0, 1.5]
    omega_s = omega_b = 0.0
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['delta_s', 'r', 't_c'])
        for ds in ds_vals:
            A = 1+ds
            for r in r_vals:
                B = r
                C = 1.0
                roots = find_all_tc(A, B, C, omega_s, omega_b)
                for tc in roots:
                    w.writerow([ds, r, tc])

def mode_t_c_vs_r(outpath):
    ds_vals = [0.0, 1.5]
    r_vals = [i*1.0 for i in range(11)]
    omega_s = omega_b = 0.0
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r', 'delta_s', 't_c'])
        for r in r_vals:
            B = r
            for ds in ds_vals:
                A = 1+ds
                C = 1.0
                roots = find_all_tc(A, B, C, omega_s, omega_b)
                for tc in roots:
                    w.writerow([r, ds, tc])

def mode_t_c_vs_q(outpath):
    r_vals = [1.0, 3.0, 7.5]
    q_vals = [i*0.5 for i in range(21)]
    h = 1.0
    ds = 0.0
    A = 1+ds
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r', 'q', 't_c'])
        for r in r_vals:
            B = r
            for q in q_vals:
                omega_s = q * h
                omega_b = h
                C = 1.0
                roots = find_all_tc(A, B, C, omega_s, omega_b)
                for tc in roots:
                    w.writerow([r, q, tc])

def solve_magnetization(r, ds, h, q, t_vals, outpath):
    omega_s = q * h
    omega_b = h
    A = 1+ds
    B = r
    C = 1.0
    f_s = make_f(omega_s)
    f_c = make_f(omega_b)
    # generate mixed terms
    ms_seq = [A, A, C, B]
    ms_var = ['s', 's', 'c', 's']
    ms_terms = generate_mixed_sequence(ms_seq, ms_var)
    mc_seq = [C]*6 + [B]
    mc_var = ['s']*6 + ['c']
    mc_terms = generate_mixed_sequence(mc_seq, mc_var)
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r', 't', 'm_T'])
        for t in t_vals:
            ms, mc = 1.0, 1.0
            for _ in range(1000):
                ms_new = evaluate_terms(ms_terms, f_s, t, ms, mc)
                mc_new = evaluate_terms(mc_terms, f_c, t, ms, mc)
                diff = max(abs(ms_new-ms), abs(mc_new-mc))
                ms, mc = ms_new, mc_new
                if diff < 1e-9:
                    break
            mT = (6*ms + mc) / 7
            w.writerow([r, t, mT])

def mode_m_T_vs_T(outpath):
    r_vals = [1.0, 4.0, 7.0, 10.0]
    ds = 0.0
    h = 1.0
    q = 1.0
    t_vals = [i*0.1 for i in range(101)]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r', 't', 'm_T'])
    for r in r_vals:
        solve_magnetization(r, ds, h, q, t_vals, outpath)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', required=True, choices=['t_c_vs_delta_s', 't_c_vs_r', 't_c_vs_q', 'm_T_vs_T'])
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    if args.mode == 't_c_vs_delta_s':
        mode_t_c_vs_delta_s(args.out)
    elif args.mode == 't_c_vs_r':
        mode_t_c_vs_r(args.out)
    elif args.mode == 't_c_vs_q':
        mode_t_c_vs_q(args.out)
    elif args.mode == 'm_T_vs_T':
        mode_m_T_vs_T(args.out)

if __name__ == '__main__':
    main()
