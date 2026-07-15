#!/usr/bin/env python3
import json
import sys


def gen_sic2h4():
    si_dzp = -288.937156
    c2h4_dzp = -78.351857
    sum_dzp = si_dzp + c2h4_dzp

    si_tz2p = -289.090686
    c2h4_tz2p = -78.427223
    sum_tz2p = si_tz2p + c2h4_tz2p

    hartree_to_kcal = 627.509474

    data = []

    # DZP fragments
    data.append({"isomer": "Si", "symmetry": "3P", "basis": "DZP",
                 "total_energy_hartree": si_dzp, "relative_energy_kcal_per_mol": 0.0})
    data.append({"isomer": "C2H4", "symmetry": "1Ag", "basis": "DZP",
                 "total_energy_hartree": c2h4_dzp, "relative_energy_kcal_per_mol": 0.0})

    # DZP isomers
    dzp_isomers = {
        "1a": ("3A2", -367.316615),
        "1b": ("3B1", -367.295348),
        "2":  ("3A''", -367.314908),
        "3":  ("3A''", -367.314829),
        "4b": ("3A2", -367.290456),
        "6":  ("3A''", -367.305731),
    }
    for name, (sym, e) in dzp_isomers.items():
        rel = round((e - sum_dzp) * hartree_to_kcal, 4)
        data.append({"isomer": name, "symmetry": sym, "basis": "DZP",
                     "total_energy_hartree": e, "relative_energy_kcal_per_mol": rel})

    # TZ2P fragments
    data.append({"isomer": "Si", "symmetry": "3P", "basis": "TZ2P",
                 "total_energy_hartree": si_tz2p, "relative_energy_kcal_per_mol": 0.0})
    data.append({"isomer": "C2H4", "symmetry": "1Ag", "basis": "TZ2P",
                 "total_energy_hartree": c2h4_tz2p, "relative_energy_kcal_per_mol": 0.0})

    # TZ2P isomers
    tz2p_isomers = {
        "1a": ("3A2", -367.547896),
        "2":  ("3A''", -367.543723),
        "3":  ("3A''", -367.543304),
    }
    for name, (sym, e) in tz2p_isomers.items():
        rel = round((e - sum_tz2p) * hartree_to_kcal, 4)
        data.append({"isomer": name, "symmetry": sym, "basis": "TZ2P",
                     "total_energy_hartree": e, "relative_energy_kcal_per_mol": rel})

    return data


def gen_sic2h2():
    si_dzp = -288.937156
    c2h2_dzp = -77.115507
    sum_dzp = si_dzp + c2h2_dzp

    si_tz2p = -289.090686
    c2h2_tz2p = -77.188354
    sum_tz2p = si_tz2p + c2h2_tz2p

    hartree_to_kcal = 627.509474

    data = []

    # DZP fragments
    data.append({"isomer": "Si", "symmetry": "3P", "basis": "DZP",
                 "total_energy_hartree": si_dzp, "relative_energy_kcal_per_mol": 0.0})
    data.append({"isomer": "C2H2", "symmetry": "1Ag", "basis": "DZP",
                 "total_energy_hartree": c2h2_dzp, "relative_energy_kcal_per_mol": 0.0})

    dzp_isomers = {
        "19": ("3A",  -366.090899),
        "20": ("3A2", -366.090136),
        "21": ("3A",  -366.064744),
        "22": ("3A''", -366.060565),
    }
    for name, (sym, e) in dzp_isomers.items():
        rel = round((e - sum_dzp) * hartree_to_kcal, 4)
        data.append({"isomer": name, "symmetry": sym, "basis": "DZP",
                     "total_energy_hartree": e, "relative_energy_kcal_per_mol": rel})

    # TZ2P fragments
    data.append({"isomer": "Si", "symmetry": "3P", "basis": "TZ2P",
                 "total_energy_hartree": si_tz2p, "relative_energy_kcal_per_mol": 0.0})
    data.append({"isomer": "C2H2", "symmetry": "1Ag", "basis": "TZ2P",
                 "total_energy_hartree": c2h2_tz2p, "relative_energy_kcal_per_mol": 0.0})

    tz2p_isomers = {
        "19": ("3A",  -366.317386),
        "20": ("3A2", -366.313454),
    }
    for name, (sym, e) in tz2p_isomers.items():
        rel = round((e - sum_tz2p) * hartree_to_kcal, 4)
        data.append({"isomer": name, "symmetry": sym, "basis": "TZ2P",
                     "total_energy_hartree": e, "relative_energy_kcal_per_mol": rel})

    return data


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "sic2h4"
    if target == "sic2h4":
        output = gen_sic2h4()
    else:
        output = gen_sic2h2()
    json.dump(output, sys.stdout, indent=2)
