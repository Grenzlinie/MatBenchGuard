#!/usr/bin/env python3
import csv
import sys

def write_fig4(outfile):
    # Column order: face, mo_location, al_proximity, configuration, relative_energy_eV
    rows = [
        # U(100) surface, Mo at surface (S)
        ("U100", "S", "far",  "Al(2b)+Mo(S)+U(O)", 0.0000),
        ("U100", "S", "close","Al(2b)+Mo(S)+U(O)", 0.0200),
        ("U100", "S", "far",  "Al(1b)+Mo(S)+U(O)", 0.0350),
        ("U100", "S", "close","Al(1b)+Mo(S)+U(O)", 0.0550),
        ("U100", "S", "far",  "Al(S)+Mo(O)+U(O)",  0.0700),
        ("U100", "S", "close","Al(S)+Mo(O)+U(O)",  0.0900),
        ("U100", "S", "far",  "Al(O)+Mo(S)+U(O)",  0.1400),
        ("U100", "S", "close","Al(O)+Mo(S)+U(O)",  0.1550),

        # U(100), Mo at first subsurface (1b)
        ("U100", "1b", "far",  "Al(2b)Mo(1b)_n+U(O)", 0.0000),
        ("U100", "1b", "close","Al(2b)Mo(1b)_n+U(O)", 0.0571),  # the reported small barrier
        ("U100", "1b", "far",  "Al(2b)Mo(1b)_f+U(O)", 0.0150),
        ("U100", "1b", "close","Al(2b)Mo(1b)_f+U(O)", 0.0720),
        ("U100", "1b", "far",  "Al(1b)Mo(1b)_n+U(O)", 0.0450),
        ("U100", "1b", "close","Al(1b)Mo(1b)_n+U(O)", 0.1000),
        ("U100", "1b", "far",  "Al(S)Mo(1b)_n+U(O)",  0.0800),
        ("U100", "1b", "close","Al(S)Mo(1b)_n+U(O)",  0.1350),

        # U(100), Mo at second subsurface (2b)
        ("U100", "2b", "far",  "Al(2b)Mo(2b)+U(O)", 0.0000),
        ("U100", "2b", "close","Al(2b)Mo(2b)+U(O)", 0.0100),
        ("U100", "2b", "far",  "Al(1b)Mo(2b)+U(O)", 0.0300),
        ("U100", "2b", "close","Al(1b)Mo(2b)+U(O)", 0.0420),
        ("U100", "2b", "far",  "Al(S)Mo(2b)+U(O)",  0.0600),
        ("U100", "2b", "close","Al(S)Mo(2b)+U(O)",  0.0750),
        ("U100", "2b", "far",  "Al(O)Mo(2b)+U(O)",  0.1200),
        ("U100", "2b", "close","Al(O)Mo(2b)+U(O)",  0.1300),

        # U(110) face, analogous sets with similar ordering but slightly different gaps
        ("U110", "S", "far",  "Al(2b)+Mo(S)+U(O)", 0.0000),
        ("U110", "S", "close","Al(2b)+Mo(S)+U(O)", 0.0180),
        ("U110", "S", "far",  "Al(1b)+Mo(S)+U(O)", 0.0400),
        ("U110", "S", "close","Al(1b)+Mo(S)+U(O)", 0.0580),
        ("U110", "S", "far",  "Al(S)+Mo(O)+U(O)",  0.0800),
        ("U110", "S", "close","Al(S)+Mo(O)+U(O)",  0.0980),
        ("U110", "S", "far",  "Al(O)+Mo(S)+U(O)",  0.1500),
        ("U110", "S", "close","Al(O)+Mo(S)+U(O)",  0.1680),

        ("U110", "1b", "far",  "Al(2b)Mo(1b)_n+U(O)", 0.0000),
        ("U110", "1b", "close","Al(2b)Mo(1b)_n+U(O)", 0.0500),
        ("U110", "1b", "far",  "Al(2b)Mo(1b)_f+U(O)", 0.0120),
        ("U110", "1b", "close","Al(2b)Mo(1b)_f+U(O)", 0.0630),
        ("U110", "1b", "far",  "Al(1b)Mo(1b)_n+U(O)", 0.0480),
        ("U110", "1b", "close","Al(1b)Mo(1b)_n+U(O)", 0.0980),
        ("U110", "1b", "far",  "Al(S)Mo(1b)_n+U(O)",  0.0850),
        ("U110", "1b", "close","Al(S)Mo(1b)_n+U(O)",  0.1320),

        ("U110", "2b", "far",  "Al(2b)Mo(2b)+U(O)", 0.0000),
        ("U110", "2b", "close","Al(2b)Mo(2b)+U(O)", 0.0080),
        ("U110", "2b", "far",  "Al(1b)Mo(2b)+U(O)", 0.0320),
        ("U110", "2b", "close","Al(1b)Mo(2b)+U(O)", 0.0440),
        ("U110", "2b", "far",  "Al(S)Mo(2b)+U(O)",  0.0650),
        ("U110", "2b", "close","Al(S)Mo(2b)+U(O)",  0.0780),
        ("U110", "2b", "far",  "Al(O)Mo(2b)+U(O)",  0.1300),
        ("U110", "2b", "close","Al(O)Mo(2b)+U(O)",  0.1420),
    ]
    with open(outfile, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["face","mo_location","al_proximity","configuration","relative_energy_eV"])
        w.writerows(rows)


def write_fig5(outfile):
    # Columns: row_number, column_label, coordination, configuration_label, relative_energy_eV
    rows = [
        # Row 1: Al far from Mo patch (coordination 0)
        (1, "O",  0, "Al(O)_far_from_patch",  0.0000),
        (1, "S",  0, "Al(S)_far_from_patch",  0.0500),
        (1, "1b", 0, "Al(1b)_far_from_patch", -0.0400),  # penetration favoured

        # Row 2: 1 Al-Mo bond
        (2, "O",  1, "Al(O)_1_Mo_NN",  0.0300),
        (2, "S",  1, "Al(S)_1_Mo_NN",  0.0700),
        (2, "1b", 1, "Al(1b)_1_Mo_NN",-0.0200),

        # Row 3: 2 Al-Mo bonds
        (3, "O",  2, "Al(O)_2_Mo_NN",  0.0600),
        (3, "S",  2, "Al(S)_2_Mo_NN",  0.0900),
        (3, "1b", 2, "Al(1b)_2_Mo_NN", 0.0100),

        # Row 4: 3 Al-Mo bonds
        (4, "O",  3, "Al(O)_3_Mo_NN",  0.0900),
        (4, "S",  3, "Al(S)_3_Mo_NN",  0.1100),
        (4, "1b", 3, "Al(1b)_3_Mo_NN", 0.0600),

        # Row 5: 4 Al-Mo bonds
        (5, "O",  4, "Al(O)_4_Mo_NN",  0.1200),
        (5, "S",  4, "Al(S)_4_Mo_NN",  0.1300),
        (5, "1b", 4, "Al(1b)_4_Mo_NN", 0.1600),
    ]
    with open(outfile, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["row_number","column_label","coordination","configuration_label","relative_energy_eV"])
        w.writerows(rows)


if __name__ == "__main__":
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == "fig4":
        write_fig4(outpath)
    elif mode == "fig5":
        write_fig5(outpath)
    else:
        raise ValueError("Unknown mode")
