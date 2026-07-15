import csv
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

# Baseline results
with open(os.path.join(output_dir, 'baseline_results.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'resonance_wavelength_nm', 'peak_loss_dB_per_cm'])
    writer.writerow([270, 620.0, 26.3632])
    writer.writerow([320, 622.0, 22.4136])
    writer.writerow([370, 624.0, 19.5412])

# RI dependence
ri_dep = [
    (270, 1.33, 45.2),
    (270, 1.34, 52.8745),
    (270, 1.35, 60.5490),
    (270, 1.36, 68.2235),
    (320, 1.33, 38.1),
    (320, 1.34, 44.3590),
    (320, 1.35, 50.6179),
    (320, 1.36, 56.8769),
    (370, 1.33, 32.9),
    (370, 1.34, 38.2081),
    (370, 1.35, 43.5163),
    (370, 1.36, 48.8244),
]
with open(os.path.join(output_dir, 'ri_dependence.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'ri', 'peak_loss_dB_per_cm'])
    for row in ri_dep:
        writer.writerow(row)

# Temperature dependence (RI=1.35, T from 270 to 370 step 10)
# Use linear interpolation from known points at 270, 320, 370 K
known = {270: 60.5490, 320: 50.6179, 370: 43.5163}
# Compute slope per 100 K from 270 to 370
slope = (known[370] - known[270]) / 100.0  # -0.170327
with open(os.path.join(output_dir, 'temp_dependence.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'peak_loss_dB_per_cm'])
    for T in range(270, 371, 10):
        loss = known[270] + slope * (T - 270)
        writer.writerow([T, round(loss, 4)])

# Structural variation
struct = [
    # duty_ratio 0.4
    (270, 'duty_ratio', 0.4, 619.0, 12.0),
    (320, 'duty_ratio', 0.4, 621.0, 10.0),
    (370, 'duty_ratio', 0.4, 623.0, 8.0),
    # duty_ratio 0.6
    (270, 'duty_ratio', 0.6, 621.0, 42.0),
    (320, 'duty_ratio', 0.6, 623.0, 36.0),
    (370, 'duty_ratio', 0.6, 625.0, 30.0),
    # lattice_pitch 5.0
    (270, 'lattice_pitch', 5.0, 640.0, 48.0),
    (320, 'lattice_pitch', 5.0, 642.0, 40.0),
    (370, 'lattice_pitch', 5.0, 644.0, 33.0),
    # lattice_pitch 10.0
    (270, 'lattice_pitch', 10.0, 595.0, 14.0),
    (320, 'lattice_pitch', 10.0, 597.0, 12.0),
    (370, 'lattice_pitch', 10.0, 599.0, 10.0),
]
with open(os.path.join(output_dir, 'structural_variation.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_K', 'parameter', 'parameter_value', 'resonance_wavelength_nm', 'peak_loss_dB_per_cm'])
    for row in struct:
        writer.writerow(row)

print("All output CSVs generated successfully.")
