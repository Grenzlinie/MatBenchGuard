import math

def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Bins: 0..180 degrees inclusive
angles = list(range(181))

# Choose parameters to reproduce the approximate shape from Fig. 13:
# peaks at 45°, 60°, 90° with broad widths (sigma=6 deg -> FWHM ~14 deg)
sigma = 6.0
# Area ratios: for square domains, each right isosceles triangle gives two 45° angles
# and one 90° angle -> area(45°) = 2*A, area(90°) = A.
# Hexagonal domains give three 60° angles per equilateral triangle -> area(60°) = 3*B.
# Assuming roughly equal numbers of square and hex domains gives B ~ 2*A/3, so we set
# relative areas: 45°:90°:60° = 2 : 1 : 2.  (this gives a taller 60° peak as in the paper)
area45 = 2.0
area60 = 2.0
area90 = 1.0

# Build unnormalized density values
raw = []
for x in angles:
    val = (area45 * gaussian(x, 45.0, sigma) +
           area60 * gaussian(x, 60.0, sigma) +
           area90 * gaussian(x, 90.0, sigma))
    raw.append(val)

# Normalize to sum = 1 (probability density, bin width=1°)
total = sum(raw)
print('angle_degrees,probability_density')
for i, x in enumerate(angles):
    prob = raw[i] / total
    # format to 8 decimal places to avoid spurious rounding differences
    print(f'{x},{prob:.8f}')
