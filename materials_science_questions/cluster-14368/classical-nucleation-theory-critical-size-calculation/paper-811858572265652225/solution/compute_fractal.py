import sys, os, csv, json, numpy as np
from scipy.stats import linregress

def read_mass(filepath):
    mass = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            x = int(row['x'])
            y = int(row['y'])
            mass[(x,y)] = float(row['solid_mass'])
    arr = np.zeros((100,100))
    for (x,y), val in mass.items():
        arr[x,y] = val
    return arr

def box_counting_dimension(arr, threshold=0.5):
    binary = (arr >= threshold).astype(int)
    nx, ny = binary.shape
    Ls = np.arange(1, min(nx, ny)+1)
    counts = []
    for L in Ls:
        count = 0
        for i in range(0, nx, L):
            for j in range(0, ny, L):
                if np.any(binary[i:i+L, j:j+L]):
                    count += 1
        counts.append(count)
    mask = np.array(counts) > 0
    logL = np.log(Ls[mask])
    logN = np.log(np.array(counts)[mask])
    if len(logL) < 2:
        return 0.0
    slope, *_ = linregress(logL, logN)
    Df = -slope
    return Df

outdir = os.environ['OUTDIR']
arr_da16 = read_mass(os.path.join(outdir, 'step_02_growth_da16.csv'))
arr_da400 = read_mass(os.path.join(outdir, 'step_03_growth_da400.csv'))

df16 = box_counting_dimension(arr_da16)
df400 = box_counting_dimension(arr_da400)

out = {'da16': df16, 'da400': df400}
with open(os.path.join(outdir, 'step_04_fractal_dimensions.json'), 'w') as f:
    json.dump(out, f, indent=2)
