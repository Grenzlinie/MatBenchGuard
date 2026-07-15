#!/usr/bin/env python3
import sys, csv

def write_bond_lengths(outpath):
    rows = [
        ("NH2", "CH3X", 1.465),
        ("NH2", "CH3XH+", 1.508),
        ("NH2", "dotCH2X", 1.402),
        ("NH2", "dotCH2XH+", 1.471),
        ("OH", "CH3X", 1.424),
        ("OH", "CH3XH+", 1.516),
        ("OH", "dotCH2X", 1.373),
        ("OH", "dotCH2XH+", 1.468),
        ("OCH3", "CH3X", 1.414),
        ("OCH3", "CH3XH+", 1.494),
        ("OCH3", "dotCH2X", 1.363),
        ("OCH3", "dotCH2XH+", 1.437),
        ("F", "CH3X", 1.390),
        ("F", "CH3XH+", 1.603),
        ("F", "dotCH2X", 1.350),
        ("F", "dotCH2XH+", 1.550),
        ("PH2", "CH3X", 1.860),
        ("PH2", "CH3XH+", 1.800),
        ("PH2", "dotCH2X", 1.790),
        ("PH2", "dotCH2XH+", 1.764),
        ("SH", "CH3X", 1.814),
        ("SH", "CH3XH+", 1.818),
        ("SH", "dotCH2X", 1.728),
        ("SH", "dotCH2XH+", 1.762),
        ("Cl", "CH3X", 1.778),
        ("Cl", "CH3XH+", 1.845),
        ("Cl", "dotCH2X", 1.718),
        ("Cl", "dotCH2XH+", 1.773),
        ("Br", "CH3X", 1.949),
        ("Br", "CH3XH+", 2.001),
        ("Br", "dotCH2X", 1.863),
        ("Br", "dotCH2XH+", 1.925),
        ("CN", "CH3X", 1.461),
        ("CN", "CH3XH+", 1.448),
        ("CN", "dotCH2X", 1.412),
        ("CN", "dotCH2XH+", 1.407),
        ("CHO", "CH3X", 1.502),
        ("CHO", "CH3XH+", 1.457),
        ("CHO", "dotCH2X", 1.456),
        ("CHO", "dotCH2XH+", 1.408),
        ("NO2", "CH3X", 1.486),
        ("NO2", "CH3XH+", 1.480),
        ("NO2", "dotCH2X", 1.431),
        ("NO2", "dotCH2XH+", 1.330),
    ]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["X", "species", "r_CX_angstrom"])
        w.writerows(rows)

def write_rse(outpath):
    rows = [
        ("NH2", "dotCH2X", 46.9),
        ("NH2", "dotCH2XH+", -19.7),
        ("OH", "dotCH2X", 33.9),
        ("OH", "dotCH2XH+", -25.2),
        ("OCH3", "dotCH2X", 34.1),
        ("OCH3", "dotCH2XH+", -20.5),
        ("F", "dotCH2X", 12.7),
        ("F", "dotCH2XH+", -50.6),
        ("PH2", "dotCH2X", 25.6),
        ("PH2", "dotCH2XH+", -5.6),
        ("SH", "dotCH2X", 38.1),
        ("SH", "dotCH2XH+", -12.4),
        ("Cl", "dotCH2X", 20.7),
        ("Cl", "dotCH2XH+", -27.2),
        ("Br", "dotCH2X", 15.5),
        ("Br", "dotCH2XH+", -25.5),
        ("CN", "dotCH2X", 33.0),
        ("CN", "dotCH2XH+", 13.7),
        ("CHO", "dotCH2X", 36.7),
        ("CHO", "dotCH2XH+", 45.7),
        ("NO2", "dotCH2X", 12.0),
        ("NO2", "dotCH2XH+", 19.6),
    ]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["X", "state", "RSE_kJmol"])
        w.writerows(rows)

def write_pa(outpath):
    rows = [
        ("NH2", "CH3X", 900.9),
        ("NH2", "dotCH2X", 834.3),
        ("OH", "CH3X", 753.2),
        ("OH", "dotCH2X", 695.3),
        ("OCH3", "CH3X", 792.0),
        ("OCH3", "dotCH2X", 739.9),
        ("F", "CH3X", 597.6),
        ("F", "dotCH2X", 534.3),
        ("PH2", "CH3X", 855.0),
        ("PH2", "dotCH2X", 823.8),
        ("SH", "CH3X", 776.3),
        ("SH", "dotCH2X", 725.8),
        ("Cl", "CH3X", 649.7),
        ("Cl", "dotCH2X", 601.1),
        ("Br", "CH3X", 663.3),
        ("Br", "dotCH2X", 622.3),
        ("CN", "CH3X", 780.1),
        ("CN", "dotCH2X", 763.0),
        ("CHO", "CH3X", 770.2),
        ("CHO", "dotCH2X", 779.8),
        ("NO2", "CH3X", 745.6),
        ("NO2", "dotCH2X", 752.1),
    ]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["X", "species", "PA_kJmol"])
        w.writerows(rows)

def write_heats_of_formation(outpath):
    rows = [
        ("NH2", "CH3X", -22.8),
        ("NH2", "CH3XH+", 606.9),
        ("NH2", "dotCH2X", 154.3),
        ("NH2", "dotCH2XH+", 851.2),
        ("OH", "CH3X", -206.7),
        ("OH", "CH3XH+", 568.6),
        ("OH", "dotCH2X", -16.0),
        ("OH", "dotCH2XH+", 819.5),
        ("OCH3", "CH3X", -192.4),
        ("OCH3", "CH3XH+", 546.3),
        ("OCH3", "dotCH2X", -2.0),
        ("OCH3", "dotCH2XH+", 791.4),
        ("F", "CH3X", -244.5),
        ("F", "CH3XH+", 688.7),
        ("F", "dotCH2X", -32.6),
        ("F", "dotCH2XH+", 963.8),
        ("PH2", "CH3X", -19.4),
        ("PH2", "CH3XH+", 656.4),
        ("PH2", "dotCH2X", 179.6),
        ("PH2", "dotCH2XH+", 886.6),
        ("SH", "CH3X", -20.4),
        ("SH", "CH3XH+", 733.9),
        ("SH", "dotCH2X", 166.1),
        ("SH", "dotCH2XH+", 970.9),
        ("Cl", "CH3X", -84.6),
        ("Cl", "CH3XH+", 796.2),
        ("Cl", "dotCH2X", 118.4),
        ("Cl", "dotCH2XH+", 1048.0),
        ("Br", "CH3X", -34.0),
        ("Br", "CH3XH+", 833.5),
        ("Br", "dotCH2X", 175.1),
        ("Br", "dotCH2XH+", 1083.6),
        ("CN", "CH3X", 75.7),
        ("CN", "CH3XH+", 825.6),
        ("CN", "dotCH2X", 267.2),
        ("CN", "dotCH2XH+", 1036.5),
        ("CHO", "CH3X", -174.3),
        ("CHO", "CH3XH+", 589.3),
        ("CHO", "dotCH2X", 16.6),
        ("CHO", "dotCH2XH+", 768.2),
        ("NO2", "CH3X", -86.7),
        ("NO2", "CH3XH+", 700.4),
        ("NO2", "dotCH2X", 125.9),
        ("NO2", "dotCH2XH+", 905.3),
    ]
    with open(outpath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["X", "species", "HOF_kJmol"])
        w.writerows(rows)

def main():
    if len(sys.argv) != 3:
        print("Usage: generate.py {bond_lengths|rse|pa|heats_of_formation} <outfile>")
        sys.exit(1)
    tp = sys.argv[1]
    out = sys.argv[2]
    if tp == "bond_lengths":
        write_bond_lengths(out)
    elif tp == "rse":
        write_rse(out)
    elif tp == "pa":
        write_pa(out)
    elif tp == "heats_of_formation":
        write_heats_of_formation(out)
    else:
        print(f"Unknown type: {tp}")
        sys.exit(1)

if __name__ == "__main__":
    main()
