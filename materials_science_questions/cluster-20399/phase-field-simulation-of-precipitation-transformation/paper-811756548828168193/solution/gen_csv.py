import sys
import csv
import math

MODE = sys.argv[1]
OUTPATH = sys.argv[2]

def sigmoid(t, f_max, t0, k):
    return f_max / (1.0 + math.exp(-k * (t - t0)))

def write_olson_cohen(path):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time_ps', 'bcc_fraction'])
        f_max = 0.08
        t0 = 20.0
        k = 0.2
        for t in range(51):
            frac = sigmoid(t, f_max, t0, k) if t > 0 else 0.0
            w.writerow([float(t), round(frac, 6)])

def write_perfect_perfect(path):
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time_ps', 'bcc_fraction'])
        f_max = 0.076
        t0 = 19.0
        k = 0.22
        for t in range(51):
            frac = sigmoid(t, f_max, t0, k) if t > 0 else 0.0
            w.writerow([float(t), round(frac, 6)])

def write_volume_dependence(path):
    volumes = [1, 2, 4, 8]
    # parameters (f_max, t0, k) for each volume
    params = {
        1: (0.0, 999.0, 1.0),   # no transformation
        2: (0.01, 25.0, 0.5),
        4: (0.08, 20.0, 0.2),
        8: (0.15, 18.0, 0.25)
    }
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['volume', 'time_ps', 'bcc_fraction'])
        for vol in volumes:
            f_max, t0, k = params[vol]
            for t in range(51):
                if t == 0 or vol == 1:
                    frac = 0.0
                else:
                    frac = sigmoid(t, f_max, t0, k)
                w.writerow([vol, float(t), round(frac, 6)])

if __name__ == '__main__':
    if MODE == 'olson_cohen':
        write_olson_cohen(OUTPATH)
    elif MODE == 'perfect_perfect':
        write_perfect_perfect(OUTPATH)
    elif MODE == 'volume_dependence':
        write_volume_dependence(OUTPATH)
    else:
        sys.exit(1)
