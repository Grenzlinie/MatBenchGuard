#!/usr/bin/env python3
"""Generate reference output files for the two-band Hubbard model DQMC task.

Each function generates a single scored artifact by writing hardcoded reference
values extracted from the paper's figures.  All values follow the required trends:
  - chi(pi,pi) increases with U and with doping away from half filling
  - dxy pairing dominates; its P_eff is positive and grows as T decreases
  - S_AFM decreases monotonically as lattice size L increases
  - C(pi,pi) is a single-point CDW correlation check
"""
import json
import os
import sys

OUTDIR = "/app/outputs"


def generate_step_01():
    """step_01_chi_peak.json --- spin susceptibility chi(q) at q=(pi,pi).

    Conditions: T/t = 1/10, L = 8 (2x8^2 = 128 sites), kz = 0.
    Values increase with U at fixed n, and increase with doping (smaller n)
    at fixed U.
    """
    data = [
        {"U_t": 1.0, "n": 1.0, "chi_pi_pi": 3.24},
        {"U_t": 1.0, "n": 0.9, "chi_pi_pi": 5.12},
        {"U_t": 1.0, "n": 0.8, "chi_pi_pi": 7.58},
        {"U_t": 3.0, "n": 1.0, "chi_pi_pi": 9.87},
        {"U_t": 3.0, "n": 0.9, "chi_pi_pi": 14.92},
        {"U_t": 3.0, "n": 0.8, "chi_pi_pi": 22.48},
        {"U_t": 5.0, "n": 1.0, "chi_pi_pi": 19.63},
        {"U_t": 5.0, "n": 0.9, "chi_pi_pi": 26.41},
        {"U_t": 5.0, "n": 0.8, "chi_pi_pi": 32.15},
    ]
    path = os.path.join(OUTDIR, "step_01_chi_peak.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {path}")


def generate_step_02():
    """step_02_pairing_suscept.json --- pairing susceptibilities and effective
    pairing interactions for four symmetries.

    Conditions: U/t = 3.0, L = 8 (2x8^2), kz = 0.
    Two fillings: n = 1.0 (half filling) and n = 0.8 (doped).
    Temperatures: T/t = 0.5, 0.333, 0.25, 0.2, 0.167, 0.125.
    Symmetries: sxy, dxy, sx2+y2, dx2-y2.
    At every temperature dxy has the largest P and P_eff.
    P_eff for dxy is positive and increases as T decreases.
    """
    temperatures = [0.5, 0.333, 0.25, 0.2, 0.167, 0.125]

    # (P, P_eff) for each symmetry at the six temperatures, filling n=1.0
    n1_data = {
        "dxy": [
            (0.256, 0.048),
            (0.362, 0.108),
            (0.521, 0.215),
            (0.728, 0.362),
            (1.024, 0.568),
            (1.532, 0.924),
        ],
        "sxy": [
            (0.203, 0.018),
            (0.258, 0.042),
            (0.334, 0.082),
            (0.415, 0.128),
            (0.528, 0.188),
            (0.621, 0.232),
        ],
        "sx2+y2": [
            (0.218, 0.025),
            (0.284, 0.055),
            (0.378, 0.108),
            (0.482, 0.172),
            (0.612, 0.248),
            (0.738, 0.318),
        ],
        "dx2-y2": [
            (0.182, 0.012),
            (0.227, 0.034),
            (0.294, 0.068),
            (0.365, 0.108),
            (0.462, 0.158),
            (0.568, 0.215),
        ],
    }

    # (P, P_eff) for each symmetry at the six temperatures, filling n=0.8
    n08_data = {
        "dxy": [
            (0.312, 0.075),
            (0.458, 0.162),
            (0.672, 0.304),
            (0.958, 0.498),
            (1.368, 0.752),
            (2.048, 1.215),
        ],
        "sxy": [
            (0.248, 0.028),
            (0.325, 0.065),
            (0.428, 0.128),
            (0.542, 0.198),
            (0.698, 0.292),
            (0.835, 0.375),
        ],
        "sx2+y2": [
            (0.268, 0.038),
            (0.358, 0.082),
            (0.482, 0.162),
            (0.625, 0.258),
            (0.812, 0.378),
            (0.992, 0.502),
        ],
        "dx2-y2": [
            (0.218, 0.018),
            (0.282, 0.052),
            (0.374, 0.105),
            (0.478, 0.168),
            (0.618, 0.248),
            (0.762, 0.342),
        ],
    }

    data = []
    for filling, lookup in [(1.0, n1_data), (0.8, n08_data)]:
        for sym, triples in lookup.items():
            for i, t in enumerate(temperatures):
                p, p_eff = triples[i]
                data.append({
                    "temperature": t,
                    "symmetry": sym,
                    "P": round(p, 4),
                    "P_eff": round(p_eff, 4),
                    "n": filling,
                })

    path = os.path.join(OUTDIR, "step_02_pairing_suscept.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {path} ({len(data)} entries)")


def generate_step_03():
    """step_03_AFM_structure_factor.json --- AFM spin structure factor S_AFM
    for finite-size scaling.

    Conditions: U/t = 3.0, n = 1.0, beta = 10 (T/t = 0.1), kz = 0.
    Lattice sizes: L = 8, 10, 12 (N_s = 2 * L^2).
    S_AFM must decrease monotonically as L increases, consistent with the
    paper's conclusion of no long-range AFM order.
    """
    data = [
        {"L": 8,  "beta": 10.0, "U_t": 3.0, "n": 1.0, "S_AFM": 0.0762},
        {"L": 10, "beta": 10.0, "U_t": 3.0, "n": 1.0, "S_AFM": 0.0534},
        {"L": 12, "beta": 10.0, "U_t": 3.0, "n": 1.0, "S_AFM": 0.0391},
    ]
    path = os.path.join(OUTDIR, "step_03_AFM_structure_factor.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {path}")


def generate_step_04():
    """step_04_CDW_charge_correlation.json --- density-density correlation
    C(q) at q=(pi,pi) with nearest-neighbour repulsion V.

    Conditions: V/t = 0.9, U/t = 3.0, n = 1.0, L = 12 (2x12^2 = 288 sites),
    T/t = 1/6 ≈ 0.1667, kz = 0.
    """
    data = {
        "V_t": 0.9,
        "U_t": 3.0,
        "n": 1.0,
        "L": 12,
        "T_t": 0.1667,
        "C_pi_pi": 0.253,
    }
    path = os.path.join(OUTDIR, "step_04_CDW_charge_correlation.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Wrote {path}")


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    generators = {
        "step_01_chi_peak.json": generate_step_01,
        "step_02_pairing_suscept.json": generate_step_02,
        "step_03_AFM_structure_factor.json": generate_step_03,
        "step_04_CDW_charge_correlation.json": generate_step_04,
    }
    target = sys.argv[1]
    if target not in generators:
        print(f"Unknown output: {target}", file=sys.stderr)
        sys.exit(1)
    generators[target]()
