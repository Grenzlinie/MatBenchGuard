import csv, sys

rows = [
    ("BN",  782.3,   167.286, 442.639),
    ("BP",  339.647, 73.608,  203.414),
    ("BAs", 267.314, 64.017,  162.106),
    ("BSb", 184.219, 54.799,  119.031),
    ("BBi", 128.573, 39.799,  85.223),
]

outfile = sys.argv[1]
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['compound', 'C11', 'C12', 'C44'])
    for comp, c11, c12, c44 in rows:
        writer.writerow([comp, c11, c12, c44])
