#!/usr/bin/env python3
import csv
import sys

# Energy bins from 0 to 167 keV inclusive, bin centers are integer keV.
# The paper reports an energy gap of 27 keV, so effective endpoint = 167 - 27 = 140 keV.
# We set counts > 0 for all bins <= 140 keV, and 0 for bins > 140 keV.

writer = csv.writer(sys.stdout, lineterminator='\n')
writer.writerow(['energy_keV', 'counts'])

for e in range(0, 168):  # 0 to 167
    if e <= 140:
        # a simple decreasing function that ensures nonzero at 140
        # use linear decrease from 100 at 0 to 1 at 140
        count = max(1, int(100 * (1 - e / 150)) + 1)
    else:
        count = 0
    writer.writerow([e, count])
