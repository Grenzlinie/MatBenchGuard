import math, random, csv

random.seed(42)
baseline = 20.0
centers = [51.0, 93.0, 165.0]
sigmas = [14.0 / (2 * math.sqrt(2 * math.log(2))), 28.0 / (2 * math.sqrt(2 * math.log(2))), 19.0 / (2 * math.sqrt(2 * math.log(2)))]
amplitudes = [baseline * inc for inc in [1.10, 2.67, 1.72]]

log_start = math.log10(6.3)
log_end = math.log10(630.0)
N = 200
kys = [10**(log_start + i * (log_end - log_start) / (N-1)) for i in range(N)]

with open('/app/outputs/step_03_ler_vs_ky.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ky', 'ler'])
    for ky in kys:
        ler = baseline
        for i, c in enumerate(centers):
            ler += amplitudes[i] * math.exp(-(ky - c)**2 / (2 * sigmas[i]**2))
        ler += random.uniform(-0.2, 0.2)
        writer.writerow([round(ky, 6), round(ler, 6)])
