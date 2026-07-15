import csv

samples = [
    {"id": "sample_1_Fe", "P": [0,3,5], "n_10p18": [4.80, 4.50, 4.21]},
    {"id": "sample_2_Fe", "P": [0,3,5], "n_10p18": [4.63, 4.30, 4.04]},
    {"id": "Co", "P": [0,3,5], "n_10p18": [1.68, 1.69, 1.70]},
]

def linreg(x, y):
    n = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum(x[i]*y[i] for i in range(n))
    sumx2 = sum(x[i]**2 for i in range(n))
    denom = n*sumx2 - sumx**2
    slope = (n*sumxy - sumx*sumy) / denom
    intercept = (sumy - slope*sumx) / n
    ymean = sumy / n
    ss_res = sum((y[i] - (slope*x[i] + intercept))**2 for i in range(n))
    ss_tot = sum((y[i] - ymean)**2 for i in range(n))
    r_squared = 1 - ss_res/ss_tot if ss_tot != 0 else 1.0
    return slope, intercept, r_squared

with open('/app/outputs/linear_fits.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sample_id','slope','intercept','r_squared'])
    for samp in samples:
        n23 = [(n*1e18)**(2/3) for n in samp['n_10p18']]  # cm^{-2}
        slope, intercept, r2 = linreg(samp['P'], n23)
        writer.writerow([samp['id'], slope, intercept, r2])
