#!/usr/bin/env python3
import sys, math, csv

direction = sys.argv[1]
outfile = sys.argv[2]

if direction == 'z':
    L = 30.0
    step = 0.1
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z', 'ACD_no_Cs', 'ACD_Cs'])
        z = 0.0
        while z <= L:
            # Material region roughly 2 < z < 28; outside is vacuum (zero charge density)
            if 2.0 < z < 28.0:
                base = 0.15
                # baseline oscillation (period 2 Å)
                osc_no = 0.03 * math.sin(2 * math.pi * z / 2.0)
                # Cs-enhanced oscillation: same baseline plus an extra bump at the Cs site
                osc_cs = osc_no + 0.02 * math.exp(-((z - 15.0) ** 2) / (2 * 1.0 ** 2))
                writer.writerow([round(z, 2), round(base + osc_no, 6), round(base + osc_cs, 6)])
            else:
                writer.writerow([round(z, 2), 0.0, 0.0])
            z = round(z + step, 2)
elif direction == 'x':
    L = 28.6
    step = 0.1
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'ACD_no_Cs', 'ACD_Cs'])
        x = 0.0
        while x <= L:
            base = 0.12
            # baseline oscillation along the cleavage surface
            osc_no = 0.02 * math.sin(2 * math.pi * x / 4.0)
            # enhanced oscillation with Cs plus a localised increase near the grain boundary
            osc_cs = 0.06 * math.sin(2 * math.pi * x / 4.0) + 0.01 * math.exp(-((x - 15.0) ** 2) / (2 * 2.0 ** 2))
            writer.writerow([round(x, 2), round(base + osc_no, 6), round(base + osc_cs, 6)])
            x = round(x + step, 2)
else:
    raise ValueError(f'Unknown direction: {direction}')
