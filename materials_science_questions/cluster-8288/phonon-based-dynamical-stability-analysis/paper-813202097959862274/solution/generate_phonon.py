import json

qpath = ["Gamma", "Y", "T", "Z", "Gamma", "S", "R", "Z"]
npoints = len(qpath)
branches = []
for i in range(12):
    freq = []
    for j in range(npoints):
        x = j / (npoints - 1) if npoints > 1 else 0
        if i < 3:
            # acoustic-like branches (start at 0)
            val = (i + 1) * 40 * x
        else:
            # optical-like branches (start higher)
            val = 150 + (i - 3) * 50 * (1 - abs(x - 0.5) * 2)
        freq.append(max(0.1, val))
    branches.append(freq)

output = {
    "qpoints": qpath,
    "frequencies": branches,
    "unit": "cm^{-1}"
}
print(json.dumps(output))
