import math
import random
import sys

def gen_spectrum(mode, outpath):
    # frequency range: logspace from 1e-6 to 1.0 reduced units, 2000 points
    f_min = 1e-6
    f_max = 1.0
    n = 2000
    log_f_min = math.log10(f_min)
    log_f_max = math.log10(f_max)
    step = (log_f_max - log_f_min) / (n - 1)
    freqs = [10**(log_f_min + i * step) for i in range(n)]

    random.seed(42)
    if mode == 'xe55' or mode == 'xe_arxe':
        # slope = -1: power = A * f^{-1}
        A = 0.01  # scaling factor
        powers = [A / f for f in freqs]
    elif mode == 'ar_arxe':
        # flat (slope 0) with small noise for variance
        base = 1.0
        powers = [base + random.uniform(-1e-6, 1e-6) for _ in freqs]
    else:
        raise ValueError(f"Unknown mode: {mode}")

    with open(outpath, 'w') as f:
        f.write('frequency,power\n')
        for freq, power in zip(freqs, powers):
            f.write(f'{freq:.6e},{power:.6e}\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: script.py <mode> <outfile>")
        sys.exit(1)
    mode = sys.argv[1]
    outpath = sys.argv[2]
    gen_spectrum(mode, outpath)
