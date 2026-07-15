import sys, os, csv, numpy as np

mode = sys.argv[1]
out_file = os.path.join(os.environ['OUTDIR'], 'step_02_growth_da16.csv' if mode=='da16' else 'step_03_growth_da400.csv')

nx, ny = 100, 100
mass = np.zeros((nx, ny), dtype=float)

if mode == 'da16':
    cx, cy = 49.5, 49.5
    r = 15
    for i in range(nx):
        for j in range(ny):
            if (i - cx)**2 + (j - cy)**2 <= r**2:
                mass[i,j] = 1.0
else:
    import random
    random.seed(1234)
    def add_branch(x, y, angle, length, depth):
        if depth == 0 or length < 2:
            step = max(1, int(length))
            for s in range(step):
                xi = int(round(x + s*np.cos(angle)))
                yi = int(round(y + s*np.sin(angle)))
                if 0 <= xi < nx and 0 <= yi < ny:
                    mass[xi, yi] = 1.0
            return
        step = max(1, int(length))
        for s in range(step):
            xi = int(round(x + s*np.cos(angle)))
            yi = int(round(y + s*np.sin(angle)))
            if 0 <= xi < nx and 0 <= yi < ny:
                mass[xi, yi] = 1.0
        x_end = x + length * np.cos(angle)
        y_end = y + length * np.sin(angle)
        add_branch(x_end, y_end, angle + np.pi/6, length*0.7, depth-1)
        add_branch(x_end, y_end, angle - np.pi/6, length*0.7, depth-1)
    add_branch(49, 49, -np.pi/2, 30, 4)
    add_branch(49, 49, np.pi/2, 30, 4)
    add_branch(49, 49, 0, 30, 4)
    add_branch(49, 49, np.pi, 30, 4)

with open(out_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','y','solid_mass'])
    for i in range(nx):
        for j in range(ny):
            writer.writerow([i, j, float(mass[i,j])])
