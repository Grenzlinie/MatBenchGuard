#!/usr/bin/env python3
"""Synthetic data generator for the hidden reference oracle.
Writes the three scored artifacts of the DFT+U spin-crossover task."""
import argparse
import math
import csv
import os

def write_transition_pressure(outdir):
    # Paper-reported static AFM transition pressure
    val = 66.0
    path = os.path.join(outdir, 'static_transition_pressure.txt')
    with open(path, 'w') as f:
        f.write(f"{val}\n")
    print(f"Wrote {path}")

def write_nonideal_mixing_energies(outdir):
    # Generate plausible static energies for HS/LS mixing configurations.
    # We use a simple harmonic E(V) for pure HS and LS states that cross
    # around V=7.2 Å³/atom, plus a small convex excess energy term.
    # For each LS fraction n = 1/6 .. 5/6 we define a few configurations
    # with different multiplicities and energies.
    
    # Parameters
    K = 10.0              # curvature for harmonic energies [eV/(Å³/atom)^2]
    V_HS0 = 7.5           # equilibrium volume HS
    V_LS0 = 6.9           # equilibrium volume LS
    V_cross = 7.2
    # shift energy so both cross near zero at V_cross
    E_HS_cross = 0.0
    E_LS_cross = 0.0
    
    # Energy functions
    def E_HS(V):
        return 0.5 * K * (V - V_HS0)**2 + E_HS_cross - 0.5*K*(V_cross-V_HS0)**2
    def E_LS(V):
        return 0.5 * K * (V - V_LS0)**2 + E_LS_cross - 0.5*K*(V_cross-V_LS0)**2
    
    # Volumes used: 5 points spanning typical crossover range
    volumes = [6.6, 6.9, 7.2, 7.5, 7.8]
    
    # Configurations per LS fraction: (occasionally a small config_index, multiplicity, delta_offset)
    # delta_offset is added to the linear interpolation energy to create non-negligible excess.
    # Multiplicities from paper's Supp. info (approximate) for fp18.
    configs_per_n = {
        1/6: [
            (1, 6, 0.01),
            (2, 30, -0.005),
            (3, 15, 0.02)
        ],
        2/6: [
            (1, 30, 0.015),
            (2, 60, 0.005),
            (3, 30, 0.025)
        ],
        3/6: [
            (1, 20, 0.02),
            (2, 40, 0.03),
            (3, 20, 0.01)
        ],
        4/6: [
            (1, 60, 0.025),
            (2, 30, 0.015),
            (3, 30, 0.005)
        ],
        5/6: [
            (1, 30, 0.02),
            (2, 15, 0.01),
            (3, 6, 0.005)
        ]
    }
    
    rows = []
    for n, confs in configs_per_n.items():
        for (idx, mult, delta) in confs:
            # base energy from linear interpolation
            for V in volumes:
                E_ideal = (1-n)*E_HS(V) + n*E_LS(V)
                E_nonideal = E_ideal + delta
                # round to 6 decimal places
                row = {
                    'n': round(n, 6),
                    'configuration_index': idx,
                    'multiplicity': mult,
                    'volume': round(V, 6),
                    'static_energy': round(E_nonideal, 6),
                    'spin_label': 'HS'  # all mixing configurations contain HS Fe
                }
                rows.append(row)
    
    path = os.path.join(outdir, 'nonideal_mixing_energies.csv')
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['n','configuration_index','multiplicity','volume','static_energy','spin_label'])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path} with {len(rows)} rows")

def write_phase_diagram(outdir):
    # Generate LS fraction n(P,T) approximating Fig. 8(d) of the paper.
    # The transition is broad; onset around 45 GPa at RT, ends around 115 GPa.
    # We model n as a sigmoid with pressure- and temperature-dependent centre.
    def ls_fraction(P_GPa, T_K):
        # centre pressure (mid-point) increases with temperature
        P0 = 80.0 + 0.02 * (T_K - 300.0)
        # width increases with temperature
        width = 10.0 + 0.005 * (T_K - 300.0)
        # sigmoid
        return 1.0 / (1.0 + math.exp((P_GPa - P0) / width))
    
    # Grid
    pressures = range(0, 141, 5)   # 0,5,...,140 GPa
    temperatures = range(300, 4501, 300) # 300,600,...,4500 K
    rows = []
    for T in temperatures:
        for P in pressures:
            n = ls_fraction(P, T)
            row = {
                'pressure_GPa': P,
                'temperature_K': T,
                'LS_fraction': round(n, 6)
            }
            rows.append(row)
    
    path = os.path.join(outdir, 'phase_diagram.csv')
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['pressure_GPa','temperature_K','LS_fraction'])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path} with {len(rows)} rows")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='basename of the output artifact')
    parser.add_argument('--dir', required=True, help='output directory')
    args = parser.parse_args()
    
    os.makedirs(args.dir, exist_ok=True)
    if args.output == 'static_transition_pressure.txt':
        write_transition_pressure(args.dir)
    elif args.output == 'nonideal_mixing_energies.csv':
        write_nonideal_mixing_energies(args.dir)
    elif args.output == 'phase_diagram.csv':
        write_phase_diagram(args.dir)
    else:
        raise ValueError(f"Unknown output: {args.output}")
