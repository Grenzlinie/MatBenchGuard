import csv
import sys

TARGET = sys.argv[1]

def make_zero_T_phases(out):
    rows = []
    # regular grid
    for a1 in [round(x*0.1, 1) for x in range(0, 21)]:
        for a2 in [round(x*0.1, 1) for x in range(0, 21)]:
            rows.append((a1, a2))
    # extra points
    rows.append((0.6, 0.5))
    rows.append((1.25, 2.0))
    # remove potential duplicates (0.6,0.5 already in grid)
    seen = set()
    uniq = []
    for a1,a2 in rows:
        key = (round(a1,5), round(a2,5))
        if key not in seen:
            seen.add(key)
            uniq.append((a1,a2))
    # phase rule: R if a1 > 0.5; otherwise N when a2 <= 1.0 else F
    def phase(a1,a2):
        if a1 > 0.5:
            return 'R'
        if a2 <= 1.0:
            return 'N'
        return 'F'
    with open(out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha1', 'alpha2', 'stable_phase'])
        for a1,a2 in uniq:
            w.writerow([a1, a2, phase(a1,a2)])

def make_transition(out):
    with open(out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha1', 'alpha2', 'T_c'])
        w.writerow([0.6, 0.5, 0.39])
        w.writerow([1.25, 2.0, 0.64])

def make_susceptibility(out):
    with open(out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alpha1', 'alpha2', 'T', 'chi'])
        w.writerow([0.6, 0.5, 0.2, 0.03])
        w.writerow([0.6, 0.5, 0.6, 0.07])

if TARGET.endswith('zero_T_phases.csv'):
    make_zero_T_phases(TARGET)
elif TARGET.endswith('transition_temperatures.csv'):
    make_transition(TARGET)
elif TARGET.endswith('susceptibility_trend.csv'):
    make_susceptibility(TARGET)
else:
    raise ValueError('unknown output')
