#!/usr/bin/env python3
"""Generate projected density of states (step_03_dft2_dos.dat) for both
stoichiometric and oxygen-deficient dislocations.  Synthetic data shows
occupied Ti3+ gap states near the valence band maximum only for the
oxygen-deficient core."""
import sys, math

def write_section(fout, label, has_gap_states=False):
    fout.write(f"# {label}\n")
    e0 = 0.0   # Fermi energy
    # energy grid from -6 to 4 eV, step 0.1
    energies = [e0 + i*0.1 for i in range(-60, 41)]
    for energy in energies:
        # Total DOS: band gap between -1.0 and 1.0 (rutile ~3 eV gap, Fermi near VBM)
        # Fill with smooth background outside gap
        if energy < -2.0:
            tot = 50 * math.exp(-0.5 * ((energy+2.5)/0.5)**2)
        elif -1.0 < energy < 1.0:
            tot = 0.0
        else:
            tot = 20 * math.exp(-0.5 * ((energy-2.0)/1.0)**2)
        # Projections: B1 and B2 similar to total, D may have extra states
        pdos_b1 = tot * 0.3
        pdos_b2 = tot * 0.4
        pdos_d  = tot * 0.3
        if has_gap_states and 0.0 < energy < 0.8:
            # occupied states near VBM in gap
            extra = 10.0 * math.exp(-0.5 * ((energy-0.4)/0.15)**2)
            pdos_d += extra
            tot += extra
        fout.write(f"{energy:.4f} {tot:.6f} {pdos_b1:.6f} {pdos_b2:.6f} {pdos_d:.6f}\n")

def main(out_path):
    with open(out_path, 'w') as f:
        write_section(f, "Ti230O460 stoichiometric", has_gap_states=False)
        write_section(f, "Ti231O461 oxygen-deficient", has_gap_states=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate_dos.py <output_file>")
        sys.exit(1)
    main(sys.argv[1])