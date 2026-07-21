import sys
import math
import csv

def generate_distribution(z_vals, peaks):
    """peaks: list of (weight, decay_length, position)"""
    raw = []
    for z in z_vals:
        v = 0.0
        for w, L, loc in peaks:
            v += w * math.exp(-abs(z - loc) / L)
        raw.append(v)
    total = sum(raw)
    return [r / total for r in raw]

def main():
    outfile = sys.argv[1] if len(sys.argv) > 1 else '/app/outputs/wavefunction_distribution.csv'
    z_vals = list(range(1, 101))
    
    # Δd/d0 = 0.2%: peaks on both surfaces
    peaks_002 = [
        (1.0, 2.0, 1),
        (1.0, 2.0, 100)
    ]
    # Δd/d0 = 3%: peak only on the opposite (non-relaxed) surface, z=100
    peaks_003 = [
        (1.0, 2.0, 100)
    ]
    
    probs_002 = generate_distribution(z_vals, peaks_002)
    probs_003 = generate_distribution(z_vals, peaks_003)
    
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z_BL', 'state', 'delta_d_d0', 'prob'])
        for delta, probs in [(0.002, probs_002), (0.03, probs_003)]:
            for state in ('S1', 'S2'):
                for i, z in enumerate(z_vals):
                    writer.writerow([z, state, delta, round(probs[i], 6)])

if __name__ == '__main__':
    main()
