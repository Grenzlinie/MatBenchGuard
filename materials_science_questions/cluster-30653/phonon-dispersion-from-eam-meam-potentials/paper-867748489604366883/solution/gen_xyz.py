import sys, math

diameter = float(sys.argv[1])
dz = 2.56          # bulk Cu nearest-neighbor distance
length = 40.0      # target wire length
nlayers = int(length / dz) + 1

if abs(diameter - 4.0) < 0.01:
    shells = [
        ('central', 0.0, 1),
        ('outer', 2.09, 5)
    ]
elif abs(diameter - 6.0) < 0.01:
    shells = [
        ('inner', 1.08, 3),
        ('outer', 3.08, 8)
    ]
elif abs(diameter - 12.0) < 0.01:
    shells = [
        ('central', 0.0, 1),
        ('shell2', 2.36, 6),
        ('shell3', 4.40, 11),
        ('outer', 6.47, 16)
    ]
else:
    raise ValueError("Unsupported diameter")

twist = 0.15   # arbitrary twist per layer to produce helical rows
atoms = []

for name, R, n_rows in shells:
    if R == 0.0 and n_rows == 1:
        # central single-atom chain
        for k in range(nlayers):
            z = k * dz
            atoms.append(('Cu', 0.0, 0.0, z))
    else:
        for k in range(nlayers):
            z = k * dz
            for j in range(n_rows):
                angle = 2.0 * math.pi * (j / n_rows + k * twist)
                x = R * math.cos(angle)
                y = R * math.sin(angle)
                atoms.append(('Cu', x, y, z))

print(len(atoms))
print("structure Dc={}".format(diameter))
for sym, x, y, z in atoms:
    print("{} {:.6f} {:.6f} {:.6f}".format(sym, x, y, z))
