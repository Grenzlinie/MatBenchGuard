import csv, sys

# Phase and cluster names use Greek letters as in Table 2.
rows = [
    ("\u03b1-Fe",        "\u03b1-Fe6",      37.765),
    ("\u03b1'-FeN",      "\u03b1'-Fe6N",    69.391),
    ("\u03b1'-FeC",      "\u03b1'-Fe6C",    65.750),
    ("\u03b3'-Fe4N",     "\u03b3'-Fe6N",    89.390),
    ("\u03b3'-Fe4C",     "\u03b3'-Fe6C",    94.620),
    ("\u03b5'-Fe3N",     "\u03b5'-Fe6N",    85.611),
    ("\u03b5'-Fe3C",     "\u03b5'-Fe6C",    83.852),
    ("\u03b5'-Fe2N",     "\u03b5'-Fe6N",    83.381),
    ("\u03b5'-Fe2C",     "\u03b5'-Fe6C",    80.560),
]

with open(sys.argv[1], 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["phase", "cluster", "binding_energy"])
    writer.writerows(rows)
