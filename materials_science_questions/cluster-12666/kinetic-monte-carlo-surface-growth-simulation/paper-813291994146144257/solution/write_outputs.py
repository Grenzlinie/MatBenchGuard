import math
import json

c = 4e4
Theta = 0.03

def alpha(i):
    return 0.436 * i

def beta(i):
    return 0.538 * i

results = []
densities = {}
for i in range(3, 9):
    N = c * (Theta ** alpha(i)) * math.exp(beta(i))
    results.append({"critical_island_size": i, "island_density_per_um2": N})
    densities[i] = N

with open("/app/outputs/island_density_vs_i.json", "w") as f:
    json.dump(results, f, indent=2)

target = 35.0
best_i = None
best_diff = float('inf')
for i in range(3, 9):
    diff = abs(densities[i] - target)
    if diff < best_diff:
        best_diff = diff
        best_i = i
    elif diff == best_diff and (best_i is None or i < best_i):
        best_i = i

with open("/app/outputs/selected_critical_island_size.txt", "w") as f:
    f.write(str(best_i) + "\n")
