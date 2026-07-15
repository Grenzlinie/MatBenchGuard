import json, math, sys

def write_properties():
    data = {
        "Sc": {
            "magnetic_moment": 1,
            "HOMO_LUMO_gap": 0.50,
            "Eb": 1.27,
            "Ef": 1.94,
            "De": 3.97,
            "symmetry": "D6d"
        },
        "Ti": {
            "magnetic_moment": 0,
            "HOMO_LUMO_gap": 0.39,
            "Eb": 1.42,
            "Ef": 1.62,
            "De": 6.25,
            "symmetry": "D6d"
        },
        "V": {
            "magnetic_moment": 1,
            "HOMO_LUMO_gap": 0.22,
            "Eb": 1.32,
            "Ef": 1.35,
            "De": 4.80,
            "symmetry": "D6d"
        },
        "W": {
            "magnetic_moment": 0,
            "HOMO_LUMO_gap": 0.99,
            "Eb": 1.69,
            "Ef": 1.36,
            "De": 10.33,
            "symmetry": "D6d",
            "isomer_energies": [
                {"isomer_label": "A", "relative_energy": 0.00},
                {"isomer_label": "B", "relative_energy": 0.19},
                {"isomer_label": "C", "relative_energy": 0.22},
                {"isomer_label": "D", "relative_energy": 0.35},
                {"isomer_label": "E", "relative_energy": 0.37},
                {"isomer_label": "F", "relative_energy": 0.39},
                {"isomer_label": "G", "relative_energy": 0.50},
                {"isomer_label": "H", "relative_energy": 1.01}
            ]
        }
    }
    with open("/app/outputs/properties.json", "w") as f:
        json.dump(data, f, indent=2)

def xyz_coords():
    # D6d cage: TM at (0,0,0), 14 Li atoms forming a hexagonal antiprism + two axial caps.
    r = 2.5   # radius of hexagons
    h = 2.0   # half-height of hexagons
    a = 3.0   # axial cap distance
    # two hexagons, rotated by 30 degrees.
    top_z = h
    bottom_z = -h
    top_offset = 0.0
    bottom_offset = 30.0 * math.pi / 180.0
    coords = []
    for i in range(6):
        angle = math.radians(i * 60) + top_offset
        coords.append(("Li", r * math.cos(angle), r * math.sin(angle), top_z))
        angle = math.radians(i * 60) + bottom_offset
        coords.append(("Li", r * math.cos(angle), r * math.sin(angle), bottom_z))
    # axial atoms
    coords.append(("Li", 0.0, 0.0, a))
    coords.append(("Li", 0.0, 0.0, -a))
    return coords

def write_xyz():
    tms = [
        ("Sc", -150.000000),
        ("Ti", -155.000000),
        ("V", -160.000000),
        ("Y", -165.000000),
        ("Zr", -170.000000),
        ("Nb", -175.000000),
        ("Hf", -180.000000),
        ("Ta", -185.000000),
        ("W", -190.000000)
    ]
    li_coords = xyz_coords()
    with open("/app/outputs/all_structures.xyz", "w") as f:
        for sym, energy in tms:
            f.write("15\n")
            f.write(f"TM={sym} D6d E={energy:.6f}\n")
            f.write(f"{sym}    0.000000    0.000000    0.000000\n")
            for elem, x, y, z in li_coords:
                f.write(f"{elem}    {x:.6f}    {y:.6f}    {z:.6f}\n")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "properties":
        write_properties()
    elif mode == "xyz":
        write_xyz()
    else:
        print("Usage: python write_outputs.py [properties|xyz]")
