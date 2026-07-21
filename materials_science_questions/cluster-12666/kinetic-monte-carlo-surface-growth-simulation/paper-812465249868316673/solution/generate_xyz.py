import sys, math

a = 3.567
d = a / math.sqrt(2)
a_z = a / 4.0

disp_1x1 = {1: (0.0, -0.127), 2: (0.0, 0.013), 3: (0.0, -0.004), 4: (0.0, -0.001), 5: (0.0, -0.001), 6: (0.0, -0.001)}

disp_2x1_sym = {
    1: (0.491, -0.183, -0.490, -0.183),
    2: (0.023, 0.114, -0.023, 0.114),
    3: (0.000, 0.082, 0.000, -0.078),
    4: (0.000, 0.037, 0.000, -0.037),
    5: (-0.006, -0.001, 0.007, -0.001),
    6: (-0.007, -0.001, 0.007, -0.001),
}

disp_2x1a = {
    1: (0.582, -0.236, -0.453, -0.238),
    2: (0.112, 0.003, 0.198, 0.290),
    3: (0.028, 0.144, -0.155, -0.214),
    4: (-0.007, 0.082, 0.009, -0.073),
    5: (0.017, 0.020, 0.016, 0.012),
    6: (-0.016, -0.001, 0.016, 0.001),
}

structure = sys.argv[1]

atoms = []
for idx in range(20):  # 0 bottom to 19 top
    z_base = idx * a_z
    if idx % 2 == 0:
        ox, oy = 0.0, 0.0
    else:
        ox, oy = d/2, d/2

    # top-down layer number N=1..6 for top six layers
    N = 20 - idx
    for i in range(6):
        for j in range(6):
            x_base = i * d + ox
            y_base = j * d + oy
            dx, dy, dz = 0.0, 0.0, 0.0
            if idx >= 4:  # movable layers
                if idx >= 14:  # top six layers
                    if structure == '1x1_relaxed':
                        if N in disp_1x1:
                            _, dz = disp_1x1[N]
                    elif structure == '2x1_sym':
                        if N in disp_2x1_sym:
                            dy0, dz0, dy1, dz1 = disp_2x1_sym[N]
                            if j % 2 == 0:
                                dy = dy0
                                dz = dz0
                            else:
                                dy = dy1
                                dz = dz1
                    elif structure == '2x1a_asym':
                        if N in disp_2x1a:
                            dy0, dz0, dy1, dz1 = disp_2x1a[N]
                            if j % 2 == 0:
                                dy = dy0
                                dz = dz0
                            else:
                                dy = dy1
                                dz = dz1
            x = x_base + dx
            y = y_base + dy
            z = z_base + dz
            atoms.append((x, y, z))

print("720")
print(f"Relaxed {structure} structure (Tersoff potential)")
for (x, y, z) in atoms:
    print(f"C {x:.6f} {y:.6f} {z:.6f}")