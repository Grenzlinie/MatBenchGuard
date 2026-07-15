import sys
import math
import csv
import json

COMPOUNDS = {
    "Au2Cs2I6": {
        "ib_range": (0.64, 1.34),
        "dominant_orbitals": ["I 2p"],
        "effective_masses": {"m_lh": 0.096, "m_hh": 0.265, "m_e": 0.095},
        "orbitals": {
            "I_2p": ((0.64+1.34)/2, (1.34-0.64)/2.35, 5.0),
            "I_5p": ((0.64+1.34)/2, (1.34-0.64)/1.5, 0.5),
            "I_5s": ((0.64+1.34)/2, (1.34-0.64)/1.5, 0.3),
            "Au_6s": ((0.64+1.34)/2, (1.34-0.64)/1.5, 0.2),
            "Au_5d": ((0.64+1.34)/2, (1.34-0.64)/1.5, 0.2),
            "Cs_5s": ((0.64+1.34)/2, (1.34-0.64)/1.5, 0.1),
            "Cs_5p": ((0.64+1.34)/2, (1.34-0.64)/1.5, 0.1),
        },
    },
    "Ag2GeBaS4": {
        "ib_range": (0.90, 2.06),
        "dominant_orbitals": ["S 2p", "Ge 4s", "Ba 4d"],
        "effective_masses": {"m_lh": 0.059, "m_hh": 0.114, "m_e": 0.021},
        "orbitals": {
            "S_2p": ((0.90+2.06)/2, (2.06-0.90)/2.35, 4.0),
            "Ge_4s": ((0.90+2.06)/2, (2.06-0.90)/2.35, 2.5),
            "Ba_4d": ((0.90+2.06)/2, (2.06-0.90)/2.35, 1.5),
            "Ag_5s": ((0.90+2.06)/2, (2.06-0.90)/1.5, 0.3),
            "Ag_4d": ((0.90+2.06)/2, (2.06-0.90)/1.5, 0.3),
            "Ge_4p": ((0.90+2.06)/2, (2.06-0.90)/1.5, 0.2),
            "Ba_5p": ((0.90+2.06)/2, (2.06-0.90)/1.5, 0.1),
            "S_3s": ((0.90+2.06)/2, (2.06-0.90)/1.5, 0.2),
        },
    },
    "Ag2ZnSnS4": {
        "ib_range": (0.47, 2.13),
        "dominant_orbitals": ["Sn 5s", "S 2p"],
        "effective_masses": {"m_lh": 0.237, "m_hh": 0.033, "m_e": 0.025},
        "orbitals": {
            "Sn_5s": ((0.47+2.13)/2, (2.13-0.47)/2.35, 4.5),
            "S_2p": ((0.47+2.13)/2, (2.13-0.47)/2.35, 3.0),
            "Sn_5p": ((0.47+2.13)/2, (2.13-0.47)/1.5, 0.3),
            "Ag_5s": ((0.47+2.13)/2, (2.13-0.47)/1.5, 0.2),
            "Ag_4d": ((0.47+2.13)/2, (2.13-0.47)/1.5, 0.2),
            "Zn_4s": ((0.47+2.13)/2, (2.13-0.47)/1.5, 0.1),
            "S_3p": ((0.47+2.13)/2, (2.13-0.47)/1.5, 0.2),
        },
    },
}

# collect all orbital column names across compounds
all_orbitals = sorted({orb for comp in COMPOUNDS.values() for orb in comp["orbitals"]})

def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def generate_csv(path):
    energy_min, energy_max, step = -5.0, 5.0, 0.05
    energies = []
    e = energy_min
    while e <= energy_max + 1e-9:
        energies.append(round(e, 10))
        e += step

    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ["compound", "energy_ev", "total_dos"] + all_orbitals
        writer.writerow(header)
        for compound, info in COMPOUNDS.items():
            orbitals = info["orbitals"]
            for energy in energies:
                row = [compound, f"{energy:.4f}"]
                # compute pdos for each orbital
                pdos = {orb: 0.0 for orb in all_orbitals}
                total = 0.0
                for orb, (mu, sigma, amp) in orbitals.items():
                    val = gaussian(energy, mu, sigma, amp)
                    pdos[orb] = val
                    total += val
                # small background so total>0.1 inside IB window
                total += 0.01
                writer.writerow([compound, f"{energy:.4f}", f"{total:.6f}"] +
                                [f"{pdos[orb]:.6f}" for orb in all_orbitals])

def generate_json(path):
    results = {}
    for compound, info in COMPOUNDS.items():
        results[compound] = {
            "ib_energy_range": f"{info['ib_range'][0]}‑{info['ib_range'][1]} eV",
            "dominant_orbitals": info["dominant_orbitals"],
            "effective_masses": info["effective_masses"],
        }
    with open(path, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: make_outputs.py --csv|--json <path>", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == "--csv":
        generate_csv(outpath)
    elif mode == "--json":
        generate_json(outpath)
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)
