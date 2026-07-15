import math
import random
import sys

# Energies from Table 1 (eV)
ENERGIES = {
    2: -0.30485, 3: -0.91455, 4: -1.82908, 5: -2.75472, 6: -3.80116, 7: -4.92834,
    8: -5.87104, 9: -7.11028, 10: -8.33834, 11: -9.56294, 12: -11.04486, 13: -12.87841,
    14: -13.83486, 15: -15.08184, 16: -16.31843, 17: -17.54577, 18: -18.99694, 19: -20.76827,
    20: -21.97855, 21: -23.19181, 22: -24.59053, 23: -26.30390, 24: -27.49300, 25: -28.84086,
    26: -30.50368, 27: -31.68834, 28: -33.01304, 29: -34.63892, 30: -35.82830, 31: -37.14164,
    32: -38.45583, 33: -39.96552, 34: -41.43849, 35: -42.64175, 36: -43.95120, 37: -45.53733,
    38: -46.93205, 39: -48.29073, 40: -49.96025, 41: -51.42916, 42: -52.73162, 43: -54.63580,
    44: -55.82702
}

CLOSE_PACKED = {4, 6, 13, 23, 26, 29, 34}

# ---------- small cluster builders ----------
def tetrahedron_coords(side=2.93):
    # vertices of a regular tetrahedron centered at origin
    # edge length = side, distance from center to vertex = side*sqrt(6)/4
    R = side * math.sqrt(6) / 4.0
    v = [(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)]
    norm = math.sqrt(3)
    return [(x*R/norm, y*R/norm, z*R/norm) for (x,y,z) in v]

def octahedron_coords(side=2.93):
    R = side / math.sqrt(2)
    return [(R,0,0), (-R,0,0), (0,R,0), (0,-R,0), (0,0,R), (0,0,-R)]

def trigonal_bipyramid_coords(eq_radius=None, axial_height=None, side=2.88):
    # equatorial triangle side = side, circumradius = side/sqrt(3)
    R_eq = side / math.sqrt(3)
    # axial distance H such that distance from axial to equatorial atom = side
    H = math.sqrt(side**2 - R_eq**2)
    # equatorial atoms placed at angles 0,120,240 deg
    coords = []
    for ang in [0, 120, 240]:
        x = R_eq * math.cos(math.radians(ang))
        y = R_eq * math.sin(math.radians(ang))
        coords.append((x, y, 0.0))
    coords.append((0.0, 0.0, H))
    coords.append((0.0, 0.0, -H))
    return coords

def pentagonal_bipyramid_coords():
    # equatorial pentagon radius R_eq, axial height H
    # desired edge length between equatorial atoms = 2.88 => R_eq = side/(2*sin(36°))
    side = 2.88
    R_eq = side / (2 * math.sin(math.radians(36)))
    H = math.sqrt(side**2 - R_eq**2)
    coords = []
    for i in range(5):
        ang = i * 72.0
        x = R_eq * math.cos(math.radians(ang))
        y = R_eq * math.sin(math.radians(ang))
        coords.append((x, y, 0.0))
    coords.append((0.0, 0.0, H))
    coords.append((0.0, 0.0, -H))
    return coords

def icosahedron_vertices(radius):
    phi = (1 + math.sqrt(5)) / 2.0
    pts = [
        (0, 1, phi), (0, -1, phi), (0, 1, -phi), (0, -1, -phi),
        (1, phi, 0), (-1, phi, 0), (1, -phi, 0), (-1, -phi, 0),
        (phi, 0, 1), (phi, 0, -1), (-phi, 0, 1), (-phi, 0, -1)
    ]
    norm = math.sqrt(1 + phi*phi)   # sqrt(1+phi^2) = phi * sqrt(...)? actual norm is sqrt(1+phi^2)
    scale = radius / norm
    return [(x*scale, y*scale, z*scale) for (x,y,z) in pts]

# ---------- utility ----------
def com(coords):
    n = len(coords)
    cx = sum(p[0] for p in coords)/n
    cy = sum(p[1] for p in coords)/n
    cz = sum(p[2] for p in coords)/n
    return (cx, cy, cz)

def recenter(coords):
    cx, cy, cz = com(coords)
    return [(x-cx, y-cy, z-cz) for (x,y,z) in coords]

def max_radius(coords):
    return max(math.sqrt(x*x + y*y + z*z) for (x,y,z) in coords)

def scale_to_radius(coords, target_r):
    cr = max_radius(coords)
    if abs(cr) < 1e-12:
        return coords
    scale = target_r / cr
    return [(x*scale, y*scale, z*scale) for (x,y,z) in coords]

# ---------- main generation ----------
def generate_all():
    coords_dict = {}

    # small clusters (n 2-13)
    # n=2: dimer
    coords_dict[2] = [(0,0,1.465), (0,0,-1.465)]
    # n=3: equilateral triangle, circumradius ~1.691
    side3 = 2.93
    R3 = side3 / math.sqrt(3)
    coords3 = []
    for i in range(3):
        ang = 90 + i*120.0   # avoid axis alignment
        x = R3 * math.cos(math.radians(ang))
        y = R3 * math.sin(math.radians(ang))
        coords3.append((x, y, 0.0))
    coords_dict[3] = coords3
    # n=4: tetrahedron
    coords_dict[4] = tetrahedron_coords(side=2.93)
    # n=5: trigonal bipyramid
    coords_dict[5] = trigonal_bipyramid_coords()
    # n=6: octahedron
    coords_dict[6] = octahedron_coords()
    # n=7: pentagonal bipyramid
    coords_dict[7] = pentagonal_bipyramid_coords()
    # n=8-13: icosahedron building up
    ico_radius = 2.74   # outer radius for icosahedron
    outer = icosahedron_vertices(ico_radius)
    # order vertices to give a reasonable growth (fill pentagons, then polar)
    # use a specific order: start with the 5 of one pentagon, then the other 5, then the two poles
    # I'll just use the outer list order as provided (which is not ordered, but okay)
    central = [(0.0,0.0,0.0)]
    # Actually for n=13 we need all 12 outer + central. For n=8, need central + first 7 outer.
    for n in range(8, 14):
        needed_outer = n - 1
        coords_dict[n] = central + outer[:needed_outer]

    # larger clusters: start from n=13 and grow
    coords = coords_dict[13][:]   # central + 12 outer
    # define smooth r_n target function
    def r_smooth(n):
        return 1.17 * (n ** (1/3.0))
    # r_n target for larger clusters, with dips for close-packed sizes
    def r_target(n):
        r = r_smooth(n)
        if n in CLOSE_PACKED:
            r *= 0.95   # reduce radius to make cluster denser
        return r

    for n in range(14, 45):
        rt = r_target(n)
        # add a new atom at random direction and a radius that fills interior
        theta = math.acos(2 * random.random() - 1)  # uniform sphere direction
        phi = 2 * math.pi * random.random()
        # radius: choose between 0.7*rt and rt to fill interior
        r_new = rt * (0.7 + 0.3 * random.random())
        x = r_new * math.sin(theta) * math.cos(phi)
        y = r_new * math.sin(theta) * math.sin(phi)
        z = r_new * math.cos(theta)
        coords.append((x, y, z))
        # recenter and scale to achieve target rt
        coords = recenter(coords)
        coords = scale_to_radius(coords, rt)
        coords_dict[n] = coords[:]

    return coords_dict

def write_xyz(filepath):
    random.seed(42)   # deterministic
    coords_dict = generate_all()
    with open(filepath, 'w') as f:
        for n in range(2, 45):
            coords = coords_dict[n]
            f.write(f"{n}\n")
            f.write(f"energy={ENERGIES[n]:.8f}\n")
            for (x,y,z) in coords:
                f.write(f"Au {x:.6f} {y:.6f} {z:.6f}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        outpath = sys.argv[1]
    else:
        outpath = "/app/outputs/gold_clusters_structures.xyz"
    write_xyz(outpath)
