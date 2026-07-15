import csv, math, os

output_path = os.path.join('/app','outputs','reflectance_spectrum.csv')

wl0 = 625.0
max_r = 0.85
min_r = 0.30
gamma = 40.0
depth = max_r - min_r

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['wavelength_nm', 'reflectance'])
    for i in range(500):
        wl = 400.0 + (900.0 - 400.0) * i / 499.0
        r = max_r - depth * (gamma*gamma / ((wl - wl0)**2 + gamma*gamma))
        writer.writerow([wl, r])
