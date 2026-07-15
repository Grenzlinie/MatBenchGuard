#!/usr/bin/env python3
"""Generate reflection spectrum CSV for a CCGF device from given peak parameters."""
import sys
import math
import csv

DEVICE_PEAKS = {
    'I': [
        {'label': 'A', 'center': 608.5, 'height': 0.527, 'fwhm': 13.5},
        {'label': 'B', 'center': 700.5, 'height': 0.519, 'fwhm': 18.0}
    ],
    'II': [
        {'label': 'C', 'center': 639.5, 'height': 0.535, 'fwhm': 12.0},
        {'label': 'D', 'center': 722.0, 'height': 0.504, 'fwhm': 10.0}
    ]
}

BASELINE = 0.12
WAVELENGTH_START = 550.0
WAVELENGTH_END = 800.0
WAVELENGTH_STEP = 0.5

def gaussian(wl, center, amplitude, sigma):
    return amplitude * math.exp(-0.5 * ((wl - center) / sigma) ** 2)

def generate_spectrum(device):
    peaks = DEVICE_PEAKS[device]
    # Convert FWHM to sigma
    sigma_factor = 2.0 * math.sqrt(2.0 * math.log(2.0))
    peaks_data = []
    for p in peaks:
        amplitude = p['height'] - BASELINE
        sigma = p['fwhm'] / sigma_factor
        peaks_data.append((p['center'], amplitude, sigma))

    wl = WAVELENGTH_START
    rows = []
    while wl <= WAVELENGTH_END + 1e-9:
        ref = BASELINE
        for center, amp, sig in peaks_data:
            ref += gaussian(wl, center, amp, sig)
        rows.append((round(wl, 3), round(ref, 6)))
        wl += WAVELENGTH_STEP
    return rows

def main():
    if len(sys.argv) != 5 or sys.argv[1] != '--device' or sys.argv[3] != '--output':
        sys.exit('Usage: synthesize.py --device {I|II} --output path')
    device = sys.argv[2]
    out_path = sys.argv[4]

    rows = generate_spectrum(device)
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['wavelength_nm', 'reflectivity'])
        writer.writerows(rows)

if __name__ == '__main__':
    main()
