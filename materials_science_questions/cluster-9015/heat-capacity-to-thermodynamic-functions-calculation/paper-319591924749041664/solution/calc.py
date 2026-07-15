import sys, csv

comp = sys.argv[1]
outfile = sys.argv[2]

if comp == 'Y04Bi06VO4':
    Cp = [146.9,147.3,147.6,148.0,148.4,148.7,149.1,149.5,149.8,150.2,150.6,150.9,151.3,151.7]
    T = list(range(350,1050,50))
elif comp == 'Y06Bi04VO4':
    Cp = [124.4,129.2,132.6,135.2,137.4,139.1,140.6,141.9,143.0,144.1,145.0,145.9,146.8,147.6]
    T = list(range(350,1050,50))
else:
    raise ValueError('unknown composition')

assert len(Cp) == len(T) == 14

delta_H = [0.0] * len(T)
delta_S = [0.0] * len(T)

for i in range(1, len(T)):
    dt = T[i] - T[i-1]
    delta_H[i] = delta_H[i-1] + 0.5 * (Cp[i-1] + Cp[i]) * dt / 1000.0
    delta_S[i] = delta_S[i-1] + 0.5 * (Cp[i-1]/T[i-1] + Cp[i]/T[i]) * dt

with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['T (K)', 'Cp (J/(mol·K))', 'delta_H (kJ/mol)', 'delta_S (J/(mol·K))'])
    for j in range(len(T)):
        w.writerow([T[j], Cp[j], delta_H[j], delta_S[j]])
