import sys
import math

def g_r(r):
    if r <= 0:
        return 0.0
    # main peaks at 1.45 Å and 2.49 Å
    p1 = 4.0 * math.exp(-((r - 1.45) / 0.05) ** 2)
    p2 = 2.5 * math.exp(-((r - 2.49) / 0.08) ** 2)
    # small shoulder at 3.8
    p3 = 1.0 * math.exp(-((r - 3.8) / 0.1) ** 2)
    return 1.0 + p1 + p2 + p3

def main(outfile):
    with open(outfile, 'w') as f:
        for i in range(301):
            r = i * 0.02
            val = g_r(r)
            f.write(f"{r:.2f},{val:.6f}\n")

if __name__ == '__main__':
    main(sys.argv[1])
