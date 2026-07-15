import json, math, csv

def sigmoid(x, x0, k, ymin, ymax):
    return ymin + (ymax - ymin) / (1.0 + math.exp(-k * (x - x0)))

initial_density = 1.01
final_density = 1.172
density_std = 0.001
shrinkage_std = 0.3

extents = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.915]
density_vals = [round(sigmoid(x, 0.5, 15, initial_density, final_density), 5) for x in extents]
shrinkage_vals = [round(100.0 * (1.0 - initial_density / d), 3) if d != 0 else 0.0 for d in density_vals]

physical = {
    'extents': extents,
    'density': density_vals,
    'density_std': density_std,
    'shrinkage': shrinkage_vals,
    'shrinkage_std': shrinkage_std
}

# Mechanical
bulk_min = 2.5
bulk_max = 6.67
bulk_std = 0.09
bulk_vals = [round(sigmoid(x, 0.5, 15, bulk_min, bulk_max), 5) for x in extents]

shear_vals = []
for x in extents:
    if x <= 0.3:
        shear = 0.0
    else:
        shear = round(sigmoid(x, 0.55, 20, 0.0, 1.18), 5)
    shear_vals.append(shear)
shear_std = 0.02

youngs_vals = []
poisson_vals = []
for i, x in enumerate(extents):
    K = bulk_vals[i]
    G = shear_vals[i]
    if G == 0:
        E = 0.0
        nu = 0.5
    else:
        E = 9.0 * K * G / (3.0 * K + G)
        nu = (3.0 * K - 2.0 * G) / (6.0 * K + 2.0 * G)
    youngs_vals.append(round(E, 3))
    poisson_vals.append(round(nu, 4))
youngs_std = 0.08
poisson_std = 0.01

yield_vals = []
for x in extents:
    if x <= 0.3:
        y = 0.0
    else:
        y = round(sigmoid(x, 0.55, 20, 0.0, 245.6), 1)
    yield_vals.append(y)
yield_std = 10.0

mechanical = {
    'extents': extents,
    'bulk': bulk_vals,
    'bulk_std': bulk_std,
    'shear': shear_vals,
    'shear_std': shear_std,
    'youngs': youngs_vals,
    'youngs_std': youngs_std,
    'poisson': poisson_vals,
    'poisson_std': poisson_std,
    'yield': yield_vals,
    'yield_std': yield_std
}

# Thermal
thermal_extents = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.915]
tg_slope = (116.7 - 45.0) / (0.915 - 0.4)
tg_intercept = 45.0 - tg_slope * 0.4
tg_vals = [round(tg_intercept + tg_slope * x, 1) for x in thermal_extents]
tg_std = 7.0

cte_below_intercept = 16.04
cte_below_slope = -10.097
cte_below_vals = [round(cte_below_intercept + cte_below_slope * x, 3) for x in thermal_extents]
cte_below_std = 0.5

cte_above_intercept = 22.66
cte_above_slope = -11.65
cte_above_vals = [round(cte_above_intercept + cte_above_slope * x, 3) for x in thermal_extents]
cte_above_std = 1.0

thermal = {
    'extents': thermal_extents,
    'tg': tg_vals,
    'tg_std': tg_std,
    'cte_below': cte_below_vals,
    'cte_below_std': cte_below_std,
    'cte_above': cte_above_vals,
    'cte_above_std': cte_above_std
}

with open('/tmp/data.json', 'w') as f:
    json.dump({'physical': physical, 'mechanical': mechanical, 'thermal': thermal}, f, indent=2)
