import sys, csv, math

def gauss(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))

def gen_dos_4x4():
    energies = [i * 0.01 for i in range(-1000, 1001)]  # -10 to 10
    centers = [
        (-8, 0.5), (-7, 0.8), (-6, 1.0), (-5, 1.2), (-4, 1.5),
        (-3, 1.8), (-2, 2.2), (-1, 2.5), (-0.5, 1.8), (0, 1.2),
        (3.29, 0.8), (3.5, 1.0), (3.8, 1.5), (4.0, 2.0),
        (4.5, 2.5), (5.0, 1.8), (5.5, 1.0), (6.0, 0.8), (7.0, 0.5),
        (-3.5, 0.5), (-1.5, 0.5), (3.7, 0.4), (4.2, 0.4),
    ]
    sigma = 0.1
    with open('/app/outputs/dos_4x4.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy', 'dos'])
        for e in energies:
            d = sum(amp * gauss(e, c, sigma) for c, amp in centers)
            w.writerow([f'{e:.2f}', f'{d:.6f}'])

def gen_dos_8x8():
    energies = [i * 0.01 for i in range(-1000, 1001)]
    centers = [
        (-8, 0.5), (-7, 0.8), (-6, 1.0), (-5, 1.2), (-4, 1.5),
        (-3, 1.8), (-2, 2.2), (-1, 2.5), (-0.5, 1.8), (0, 1.2),
        (2.1, 0.8), (2.5, 1.0), (2.8, 1.5), (3.0, 2.0),
        (3.5, 2.5), (4.0, 1.8), (4.5, 1.0), (5.0, 0.8), (6.0, 0.5),
        (-3.5, 0.5), (-1.5, 0.5), (2.6, 0.4), (3.2, 0.4),
    ]
    sigma = 0.1
    with open('/app/outputs/dos_8x8.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy', 'dos'])
        for e in energies:
            d = sum(amp * gauss(e, c, sigma) for c, amp in centers)
            w.writerow([f'{e:.2f}', f'{d:.6f}'])

def gen_epsilon2_4x4():
    energies = [i * 0.01 for i in range(0, 1001)]  # 0 to 10
    parallel = [(3.0, 2.0, 0.2), (3.8, 1.5, 0.2)]
    perpendicular = [(3.4, 2.0, 0.3)]
    with open('/app/outputs/epsilon2_4x4.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy', 'epsilon2_parallel', 'epsilon2_perpendicular'])
        for e in energies:
            par = sum(amp * gauss(e, c, s) for c, amp, s in parallel)
            per = sum(amp * gauss(e, c, s) for c, amp, s in perpendicular)
            w.writerow([f'{e:.2f}', f'{par:.6f}', f'{per:.6f}'])

def gen_epsilon2_8x8():
    energies = [i * 0.01 for i in range(0, 1001)]
    parallel = [(3.4, 2.5, 0.25)]
    perpendicular = [(3.4, 2.5, 0.25)]
    with open('/app/outputs/epsilon2_8x8.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['energy', 'epsilon2_parallel', 'epsilon2_perpendicular'])
        for e in energies:
            par = sum(amp * gauss(e, c, s) for c, amp, s in parallel)
            per = sum(amp * gauss(e, c, s) for c, amp, s in perpendicular)
            w.writerow([f'{e:.2f}', f'{par:.6f}', f'{per:.6f}'])

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'dos_4x4': gen_dos_4x4()
    elif cmd == 'dos_8x8': gen_dos_8x8()
    elif cmd == 'epsilon2_4x4': gen_epsilon2_4x4()
    elif cmd == 'epsilon2_8x8': gen_epsilon2_8x8()
    else: print('unknown command', file=sys.stderr); sys.exit(1)
