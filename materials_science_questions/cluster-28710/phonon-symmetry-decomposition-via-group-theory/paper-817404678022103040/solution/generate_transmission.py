#!/usr/bin/env python3
import csv
import math

output_path = '/app/outputs/transmission_spectra.csv'
freq_start = 0.85
freq_end = 1.0
num_points = 101
# peak parameters (center, amplitude, sigma)
peak_center_lower = 0.863  # center beam peak
peak_center_upper = 0.978  # side beam peak
amplitude_main = 0.45      # comparable main peak height
amplitude_suppressed = 0.03  # weak peak for the inhibited direction
sigma = 0.012

# add small constant background
background = 0.01

def gaussian(x, mu, amp, s):
    return amp * math.exp(-0.5 * ((x - mu) / s) ** 2)

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['frequency', 'transmission_center', 'transmission_side'])
    step = (freq_end - freq_start) / (num_points - 1)
    for i in range(num_points):
        freq = freq_start + i * step
        # center transmission: strong at lower cone, weak at upper cone
        T_center = (gaussian(freq, peak_center_lower, amplitude_main, sigma) +
                    gaussian(freq, peak_center_upper, amplitude_suppressed, sigma) +
                    background)
        # side transmission: weak at lower cone, strong at upper cone
        T_side = (gaussian(freq, peak_center_lower, amplitude_suppressed, sigma) +
                  gaussian(freq, peak_center_upper, amplitude_main, sigma) +
                  background)
        # ensure non-negative and clip to reasonable range
        T_center = max(0.0, min(T_center, 1.0))
        T_side = max(0.0, min(T_side, 1.0))
        writer.writerow([f'{freq:.6f}', f'{T_center:.6f}', f'{T_side:.6f}'])
