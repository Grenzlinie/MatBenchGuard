import csv

pos_frac = [round(x, 1) for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]]

rowdata = []

# thickness 1 ug/cm2
thick1 = 1.0
fw1 = [0.0, 1.0, 2.0, 3.0, 5.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
bw1 = [0.0, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.5, 5.0, 5.0]
for pf, f, b in zip(pos_frac, fw1, bw1):
    rowdata.append([thick1, pf, f, b])

# thickness 10 ug/cm2
thick10 = 10.0
fw10 = [0.0, 5.0, 12.0, 20.0, 30.0, 40.0, 48.0, 50.0, 50.0, 50.0, 50.0]
bw10 = [0.0, 2.0, 5.0, 10.0, 18.0, 25.0, 30.0, 32.0, 34.0, 35.0, 30.0]
for pf, f, b in zip(pos_frac, fw10, bw10):
    rowdata.append([thick10, pf, f, b])

# thickness 100 ug/cm2
thick100 = 100.0
fw100 = [0.0, 8.0, 18.0, 30.0, 42.0, 55.0, 68.0, 75.0, 75.0, 75.0, 75.0]
bw100 = [0.0, 15.0, 35.0, 55.0, 70.0, 80.0, 85.0, 88.0, 90.0, 90.0, 90.0]
for pf, f, b in zip(pos_frac, fw100, bw100):
    rowdata.append([thick100, pf, f, b])

with open('/app/outputs/time_resolved.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['thickness', 'position_fraction', 'forward_percent', 'backward_percent'])
    w.writerows(rowdata)
