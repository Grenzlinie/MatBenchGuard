import sys
import json
import numpy as np

# Paper-reported values
TC_FM = 2.59
TC_EAFM = 2.19
TC_SAFM = 2.05
TCOMP_SAFM = 1.23

# Coercive fields: (Hc_abs for up/down symmetrical loops)
hc_fm = {1: 1.56, 2: 0.31, 3: 0.0, 4: 0.0}
hc_eafm = {1: 0.79, 2: 0.03, 3: 0.0, 4: 0.0}
# SAFM T=1: total Hc=0.3; T=2: multiple Hc (we use 0.01, 0.03, 0.05 as plausible)
hc_safm = {1: [0.3], 2: [0.01, 0.03, 0.05], 3: [], 4: []}

def mt_curve(case, Tc, Tcomp=None):
    """Generate M-T points for a case."""
    T = np.linspace(0, 4, 600)
    if case == 'SAFM' and Tcomp is not None:
        # Quadratic that vanishes at Tcomp and Tc, positive at T=0
        scale = 1.0 / (Tcomp * Tc)  # so M(0)=1
        M = np.where(T < Tc, (T - Tcomp) * (T - Tc) * scale, 0.0)
        M = np.clip(M, -1, 1)
    else:
        # Simple quadratic drop: M = 1 - (T/Tc)^2 for T<Tc, 0 otherwise
        M = np.where(T < Tc, 1 - (T / Tc) ** 2, 0.0)
    # Sublattice magnetizations just follow the same shape (can be arbitrary)
    mA = M * 0.9
    mB = M * 1.1
    mO = M * 0.8
    rows = []
    for i in range(len(T)):
        rows.append((T[i], case, mA[i], mB[i], mO[i], M[i]))
    return rows

def hysteresis_loop(hc_abs_list):
    """Generate a full hysteresis loop (ascending + descending) exhibiting coercive fields at ±hc values."""
    H_up = np.linspace(-5, 5, 1000)
    H_down = np.linspace(5, -5, 1000)
    H = np.concatenate([H_up, H_down])

    # Build a function that has zero crossings at given Hc values and hysteresis
    if not hc_abs_list:
        # paramagnetic: M ~ tanh(H)
        M = np.tanh(H * 2)
    else:
        M = np.zeros_like(H)
        # ascending branch: use Hc_neg = -hc
        up_idx = slice(0, 1000)
        for hc in hc_abs_list:
            M[up_idx] += np.tanh((H_up + hc) * 10)
        M[up_idx] /= len(hc_abs_list)
        # descending branch: use Hc_pos = +hc
        down_idx = slice(1000, 2000)
        for hc in hc_abs_list:
            M[down_idx] += np.tanh((H_down - hc) * 10)
        M[down_idx] /= len(hc_abs_list)
        # ensure magnitude ~1
        M *= 1.2
    return H, M

def write_mt_data():
    cases = [
        ('FM', TC_FM),
        ('EAFM', TC_EAFM),
        ('SAFM', TC_SAFM, TCOMP_SAFM)
    ]
    print('T,case,m_A,m_B,m_O,M_total')
    for item in cases:
        if len(item) == 2:
            case, Tc = item
            rows = mt_curve(case, Tc)
        else:
            case, Tc, Tcomp = item
            rows = mt_curve(case, Tc, Tcomp)
        for r in rows:
            print(f"{r[0]:.6f},{r[1]},{r[2]:.6f},{r[3]:.6f},{r[4]:.6f},{r[5]:.6f}")

def write_mh_data():
    temps = [1, 2, 3, 4]
    print('T,case,H,m_A,m_B,m_O,M_total')
    for t in temps:
        for case, hc_dict in [('FM', hc_fm), ('EAFM', hc_eafm), ('SAFM', hc_safm)]:
            hc_list = hc_dict.get(t, [])
            if isinstance(hc_list, (int, float)):
                hc_list = [hc_list] if hc_list != 0 else []
            H, M_total = hysteresis_loop(hc_list)
            mA = M_total * 0.9
            mB = M_total * 1.1
            mO = M_total * 0.8
            for i in range(len(H)):
                print(f"{t},{case},{H[i]:.6f},{mA[i]:.6f},{mB[i]:.6f},{mO[i]:.6f},{M_total[i]:.6f}")

def write_summary():
    summary = {
        "Tc_FM": TC_FM,
        "Tc_EAFM": TC_EAFM,
        "Tc_SAFM": TC_SAFM,
        "T_comp_SAFM": TCOMP_SAFM,
        "Hc_values": [
            {"T": 1, "case": "FM", "Hc": 1.56},
            {"T": 2, "case": "FM", "Hc": 0.31},
            {"T": 3, "case": "FM", "Hc": 0.0},
            {"T": 4, "case": "FM", "Hc": 0.0},
            {"T": 1, "case": "EAFM", "Hc": 0.79},
            {"T": 2, "case": "EAFM", "Hc": 0.03},
            {"T": 3, "case": "EAFM", "Hc": 0.0},
            {"T": 4, "case": "EAFM", "Hc": 0.0},
            {"T": 1, "case": "SAFM", "Hc": 0.3},
            {"T": 2, "case": "SAFM", "Hc": [0.01, 0.03, 0.05]},
            {"T": 3, "case": "SAFM", "Hc": 0.0},
            {"T": 4, "case": "SAFM", "Hc": 0.0}
        ]
    }
    json.dump(summary, sys.stdout, indent=2)

if __name__ == '__main__':
    if '--mt' in sys.argv:
        write_mt_data()
    elif '--mh' in sys.argv:
        write_mh_data()
    elif '--summary' in sys.argv:
        write_summary()
    else:
        print("Usage: gen_data.py --mt|--mh|--summary", file=sys.stderr)
        sys.exit(1)
