import csv, math, random
random.seed(42)
reversal = {}
with open('/app/outputs/reversal_times.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        s_val = float(row['s'])
        h_val = float(row['h'])
        tau_val = float(row['tau'])
        if s_val == 3.5:
            reversal[h_val] = tau_val
h_targets = [-0.2, -0.5, -0.8]
for h in h_targets:
    if h not in reversal:
        raise ValueError(f"Missing reversal tau for h={h}")
k = 0.5
epsilon_noise = 0.005
def compute_weights(t, tau, t_peaks, sigma):
    raw = [math.exp(- (t - t_peaks[i])**2 / (2*sigma**2)) for i in range(4)]
    total_raw = sum(raw)
    return [r / total_raw for r in raw]
with open('/app/outputs/avrami_decay.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['h','t','N_7_2','N_5_2','N_3_2','N_1_2'])
    for h in h_targets:
        tau = reversal[h]
        t_peaks = [0.0, 0.15*tau, 0.35*tau, 0.6*tau]
        sigma = tau * 0.1
        w_at_tau = compute_weights(tau, tau, t_peaks, sigma)
        max_t = int(3 * tau) + 5
        for t in range(max_t+1):
            if t <= tau:
                w = compute_weights(t, tau, t_peaks, sigma)
                N = w
            else:
                x = ((t - tau) / tau) ** 3
                total_clean = math.exp(-k * x)
                noise = random.gauss(0, 1)
                total = total_clean * (1 + epsilon_noise * noise)
                if total < 0:
                    total = 0
                N = [w_at_tau[i] * total for i in range(4)]
            writer.writerow([h, t, N[0], N[1], N[2], N[3]])
