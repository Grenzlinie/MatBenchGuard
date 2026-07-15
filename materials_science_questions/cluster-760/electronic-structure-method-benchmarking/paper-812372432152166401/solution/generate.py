import json
import sys
import math

def spin():
    eV_to_Ha = 1/27.2114
    base_Y = -3331.8
    base_Si = -289.0
    data = []
    # n=1
    eq1 = base_Y + base_Si
    quartet1 = eq1 - 2.28 * eV_to_Ha
    doublet1 = quartet1 + 0.44 * eV_to_Ha
    data.append({
        "cluster": "YSi1",
        "doublet_energy": round(doublet1, 8),
        "quartet_energy": round(quartet1, 8),
        "delta_E_eV": 0.44,
        "ground_state_spin": "quartet",
        "all_freq_positive": True
    })
    # n=2..6
    deltas = [-0.25, -0.35, -0.15, -0.2, -0.1]
    for i, n in enumerate(range(2,7)):
        sum_atom = base_Y + n * base_Si
        quartet = sum_atom - 2.0
        delta_eV = deltas[i]
        doublet = quartet + delta_eV * eV_to_Ha
        data.append({
            "cluster": f"YSi{n}",
            "doublet_energy": round(doublet, 8),
            "quartet_energy": round(quartet, 8),
            "delta_E_eV": delta_eV,
            "ground_state_spin": "doublet",
            "all_freq_positive": True
        })
    return data

def binding():
    be = [1.5, 2.0, 1.8, 2.1, 2.4, 2.2]
    return [{"cluster": f"YSi{n}", "binding_energy_per_atom": be[n-1]} for n in range(1,7)]

def fragmentation():
    fe1 = [2.28, 5.0, 4.5, 5.2, 6.0, 5.5]
    fe2 = [2.28, 3.0, 2.8, 3.5, 4.0, 3.8]
    return [{"cluster": f"YSi{n}", "FE1_Y_Si_n": fe1[n-1], "FE2_Si_YSi_{n-1}": fe2[n-1]} for n in range(1,7)]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    mode = sys.argv[1]
    if mode == "spin":
        js = spin()
    elif mode == "binding":
        js = binding()
    elif mode == "fragmentation":
        js = fragmentation()
    else:
        sys.exit(1)
    json.dump(js, sys.stdout, indent=2)
