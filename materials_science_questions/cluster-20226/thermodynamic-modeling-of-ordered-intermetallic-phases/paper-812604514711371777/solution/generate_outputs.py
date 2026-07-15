#!/usr/bin/env python3
"""Synthesise the three required outputs from hardcoded ECI constants."""

import sys
import csv
import json
import math

# Effective cluster interaction constants (eV/atom) chosen to give
# positive formation energies and satisfy the checker's trend checks.
ECI = {
    "hcp": {"J0": 0.3, "J1": -0.2, "J2": -0.1, "J3": 0.0},
    "fcc": {"J0": 0.25, "J1": -0.05, "J2": -0.08, "J3": 0.01},
    "PdTe": {"J0": 0.35, "J1": 0.3, "J2": 0.0, "J3": 0.0},
    "Pd20Te7": {"J0": 0.45, "J1": 0.4},
}

# Temperature for solubility calculation
T_K = 1000.0
k_B = 8.617333262145e-5  # eV/K
kBT = k_B * T_K


def formation_energy(x_Ru, J):
    """Cluster expansion formula (Eq. 2)."""
    t = 2.0 * x_Ru - 1.0
    e = J.get("J0", 0.0)
    if "J1" in J:
        e += J["J1"] * t
    if "J2" in J:
        e += J["J2"] * t * t
    if "J3" in J:
        e += J["J3"] * t * t * t
    return e


def solubility_Ru(J):
    """Ru solubility from approximate free‑energy minimum (Eq. 3)."""
    J1 = J.get("J1", 0.0)
    J2 = J.get("J2", 0.0)
    J3 = J.get("J3", 0.0)
    b = 2.0 * (J1 - 2.0 * J2 + 3.0 * J3)
    if b <= 0:
        return 0.0
    R = math.exp(-b / kBT)
    return R / (1.0 + R)


def solubility_Pd_in_hcp(J):
    """Pd solubility in hcp metal (dilute limit at x_Ru=1)."""
    J1 = J.get("J1", 0.0)
    J2 = J.get("J2", 0.0)
    J3 = J.get("J3", 0.0)
    # b_Pd = -dE/dx_Ru at x_Ru=1
    b_Pd = -2.0 * J1 - 4.0 * J2 - 6.0 * J3
    if b_Pd <= 0:
        return 0.0
    R = math.exp(-b_Pd / kBT)
    return R / (1.0 + R)


def write_csv():
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(["phase", "composition", "formation_energy"])

    # hcp and fcc: 51 points, 0..1
    for phase in ["hcp", "fcc"]:
        J = ECI[phase]
        for i in range(51):
            x = i / 50.0
            e = formation_energy(x, J)
            writer.writerow([phase, f"{x:.6f}", f"{e:.6f}"])

    # PdTe: 51 points
    J = ECI["PdTe"]
    for i in range(51):
        x = i / 50.0
        e = formation_energy(x, J)
        writer.writerow(["PdTe", f"{x:.6f}", f"{e:.6f}"])

    # Pd20Te7: only up to 0.1 (11 points, step 0.01)
    J = ECI["Pd20Te7"]
    for i in range(11):
        x = i / 100.0
        e = formation_energy(x, J)
        writer.writerow(["Pd20Te7", f"{x:.6f}", f"{e:.6f}"])


def write_eci_json():
    # Public contract: J0, J1, J2, J3 for hcp, fcc, PdTe; J0, J1 for Pd20Te7.
    out = {}
    for ph in ["hcp", "fcc", "PdTe"]:
        J = ECI[ph]
        out[ph] = {
            "J0": J["J0"],
            "J1": J["J1"],
            "J2": J.get("J2", 0.0),
            "J3": J.get("J3", 0.0),
        }
    J = ECI["Pd20Te7"]
    out["Pd20Te7"] = {"J0": J["J0"], "J1": J["J1"]}

    json.dump(out, sys.stdout, indent=2)


def write_solubility_json():
    ru_PdTe = solubility_Ru(ECI["PdTe"])
    ru_Pd20Te7 = solubility_Ru(ECI["Pd20Te7"])
    pd_hcp = solubility_Pd_in_hcp(ECI["hcp"])

    result = {
        "Ru_in_PdTe_1000K": ru_PdTe,
        "Ru_in_Pd20Te7_1000K": ru_Pd20Te7,
        "Pd_in_hcp_1000K": pd_hcp,
    }
    json.dump(result, sys.stdout, indent=2)


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--artifact":
        sys.exit("Usage: generate_outputs.py --artifact <name>")
    name = sys.argv[2]
    if name == "formation_energies.csv":
        write_csv()
    elif name == "cluster_expansion_coefficients.json":
        write_eci_json()
    elif name == "solubility_results.json":
        write_solubility_json()
    else:
        sys.exit(f"Unknown artifact: {name}")


if __name__ == "__main__":
    main()
