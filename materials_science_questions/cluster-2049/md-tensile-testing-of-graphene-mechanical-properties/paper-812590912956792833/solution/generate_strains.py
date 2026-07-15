#!/usr/bin/env python3
import random
import math
import json
import sys

random.seed(42)
n_atoms = 89800
low_scale = 0.002
high_scale = 0.02
mix_prob = 0.05

values = []
for _ in range(n_atoms):
    if random.random() < mix_prob:
        v = random.expovariate(1.0/high_scale)
    else:
        v = random.expovariate(1.0/low_scale)
    values.append(v)

data = {"strains": values}
json.dump(data, sys.stdout)
