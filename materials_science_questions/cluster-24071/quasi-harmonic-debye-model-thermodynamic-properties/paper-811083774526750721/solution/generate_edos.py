import sys
import math

def total_dos(E):
    # pseudogap at Fermi level: dip, then rise
    if abs(E) < 0.1:
        return 0.02 + abs(E)*0.3
    return 0.2 * abs(E) * math.exp(-abs(E)/5.0)

def p_dos(E):
    # p-orbital dominates near conduction edge (E>0)
    if E > 0:
        return total_dos(E) * 0.85
    else:
        return total_dos(E) * 0.2

def main(outfile):
    with open(outfile, 'w') as f:
        # emit header optional; we'll skip header to match no-header contract
        for i in range(201):
            E = -10.0 + i * 0.1
            td = total_dos(E)
            pd = p_dos(E)
            f.write(f"{E:.1f},{td:.6f},{pd:.6f}\n")

if __name__ == '__main__':
    main(sys.argv[1])
