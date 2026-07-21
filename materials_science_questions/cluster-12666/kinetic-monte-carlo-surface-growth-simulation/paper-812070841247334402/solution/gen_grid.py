import math, sys

SIZE = 50
CENTER = (SIZE/2.0 - 0.5, SIZE/2.0 - 0.5)  # cell indices 0..49
R_CORE = 16
R_TOTAL = 22
BRANCH_THICKNESS = 2.0  # cells
BRANCH_ANGLES = [0.0, math.pi/3.0, 2.0*math.pi/3.0, math.pi, 4.0*math.pi/3.0, 5.0*math.pi/3.0]
ANGLE_TOL = BRANCH_THICKNESS / R_CORE  # approx angular half-width at rim of core

grid = []
for y in range(SIZE):
    row = []
    for x in range(SIZE):
        dx = x - CENTER[0]
        dy = y - CENTER[1]
        r = math.hypot(dx, dy)
        if r > R_TOTAL:
            row.append(0)
        elif r <= R_CORE:
            angle = math.atan2(dy, dx)
            on_branch = False
            for a in BRANCH_ANGLES:
                da = angle - a
                da = (da + math.pi) % (2*math.pi) - math.pi
                if abs(da) < ANGLE_TOL:
                    on_branch = True
                    break
            row.append(1 if on_branch else 0)
        else:
            row.append(1)  # compact outer rim
    grid.append(row)

for row in grid:
    print(' '.join(str(v) for v in row))
