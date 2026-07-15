import csv, math, sys

def gaussian(x, mu, sigma, amplitude):
    return amplitude * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

temperatures = [0, 300, 800, 1600]
peak_amps = {0: 0.0, 300: 0.8, 800: 0.9, 1600: 0.85}
baseline = 0.05

distances = [1.0 + i * 0.01 for i in range(101)]  # 1.0 to 2.0 Å

out = sys.argv[1] if len(sys.argv) > 1 else '/app/outputs/rdf_data.csv'
with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature', 'distance', 'intensity'])
    for t in temperatures:
        amp = peak_amps[t]
        for d in distances:
            intensity = baseline + gaussian(d, 1.55, 0.04, amp)
            writer.writerow([t, round(d, 2), round(intensity, 6)])
