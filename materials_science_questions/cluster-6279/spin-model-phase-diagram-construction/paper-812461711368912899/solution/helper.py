import json, math, itertools

# Parameter sets for cases I-VI, satisfying Delta_BC < Delta_AC < Delta_AB.
CASES_PARAMS = {
    "case_I":    {"delta_AB": 0.5, "delta_AC": 0.3, "delta_BC": 0.1, "delta": 1.0},
    "case_II":   {"delta_AB": 2.0, "delta_AC": 0.5, "delta_BC": 0.3, "delta": 1.0},
    "case_III":  {"delta_AB": -0.5, "delta_AC": -1.5, "delta_BC": -2.0, "delta": -1.0},
    "case_IV":   {"delta_AB": 5.0, "delta_AC": 3.0, "delta_BC": 1.0, "delta": 1.0},
    "case_V":    {"delta_AB": 1.0, "delta_AC": -1.0, "delta_BC": -2.0, "delta": -1.0},
    "case_VI":   {"delta_AB": 3.0, "delta_AC": 1.0, "delta_BC": 0.5, "delta": -1.0}
}

# Mapping from case label to ground state type (from Table 3 in the paper)
CASE_TO_TYPE = {
    "case_I": "homochiral",
    "case_II": "unusual_racemic",
    "case_III": "racemic",
    "case_IV": "none",
    "case_V": "none",
    "case_VI": "none"
}

# Neighbour permutations (as strings)
NEIGHBOUR_PERMS = ["".join(p) for p in itertools.permutations("ABC")]

# Psi formulas for pair 1 (A direction), 2 (B direction), 3 (C direction) from Table 1
def psi_1(neigh_str, dAB, dAC, dBC, d):
    if neigh_str == "ABC":   return dAB + dAC
    if neigh_str == "ACB":   return dAB + dAC + 2*d
    if neigh_str == "BAC":   return dAC + d
    if neigh_str == "BCA":   return dAC + 2*d
    if neigh_str == "CAB":   return dAB + 2*d
    if neigh_str == "CBA":   return dAB + d
    raise ValueError(f"Unknown permutation {neigh_str}")

def psi_2(neigh_str, dAB, dAC, dBC, d):
    if neigh_str == "ABC":   return dAB + dBC
    if neigh_str == "ACB":   return dAB + d
    if neigh_str == "BAC":   return dBC + d
    if neigh_str == "BCA":   return dAB + 2*d
    if neigh_str == "CAB":   return dBC + 2*d
    if neigh_str == "CBA":   return dAB + dBC + 2*d
    raise ValueError(f"Unknown permutation {neigh_str}")

def psi_3(neigh_str, dAB, dAC, dBC, d):
    if neigh_str == "ABC":   return dAC + dBC
    if neigh_str == "ACB":   return dAC + d
    if neigh_str == "BAC":   return dAC + dBC + 2*d
    if neigh_str == "BCA":   return dBC + 2*d
    if neigh_str == "CAB":   return dAC + 2*d
    if neigh_str == "CBA":   return dBC + d
    raise ValueError(f"Unknown permutation {neigh_str}")

def compute_min_phi_T(dAB, dAC, dBC, d):
    """Enumerate all 6^3 triangle configurations, return minimal Phi_T."""
    min_val = float("inf")
    for n1 in NEIGHBOUR_PERMS:
        for n2 in NEIGHBOUR_PERMS:
            for n3 in NEIGHBOUR_PERMS:
                val = (psi_1(n1, dAB, dAC, dBC, d) +
                       psi_2(n2, dAB, dAC, dBC, d) +
                       psi_3(n3, dAB, dAC, dBC, d))
                if val < min_val:
                    min_val = val
    return min_val

def write_ground_state_results():
    results = {}
    for case_label, params in CASES_PARAMS.items():
        dAB = params["delta_AB"]
        dAC = params["delta_AC"]
        dBC = params["delta_BC"]
        d = params["delta"]
        min_phi = compute_min_phi_T(dAB, dAC, dBC, d)
        gs_type = CASE_TO_TYPE[case_label]
        results[case_label] = {
            "delta_AB": dAB,
            "delta_AC": dAC,
            "delta_BC": dBC,
            "delta": d,
            "min_phi_T": min_phi,
            "ground_state_type": gs_type
        }
    with open("/app/outputs/ground_state_results.json", "w") as f:
        json.dump(results, f, indent=2)

def write_residual_entropy():
    # W = sqrt(3) / (2*pi) * Gamma(1/3)^(3/2)
    W = math.sqrt(3) / (2 * math.pi) * (math.gamma(1/3) ** 1.5)
    with open("/app/outputs/residual_entropy.txt", "w") as f:
        f.write(f"{W:.7f}\n")

if __name__ == "__main__":
    # Allow selective execution via command-line argument
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "ground_state_results":
            write_ground_state_results()
        elif sys.argv[1] == "residual_entropy":
            write_residual_entropy()
        else:
            print("Unknown target", file=sys.stderr)
            sys.exit(1)
    else:
        write_ground_state_results()
        write_residual_entropy()
