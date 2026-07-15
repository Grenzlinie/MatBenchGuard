#!/usr/bin/env python3
import numpy as np
import json
import argparse
import os

def generate_rcwa_scan(output_path):
    # Generate synthetic RCWA sweep arrays for two thicknesses.
    # Periods: 0.4 to 1.2 um, step 0.05 -> 17 values
    # Duty cycles: 0.2 to 0.9, step 0.05 -> 15 values
    periods = np.arange(0.4, 1.21, 0.05)
    duties = np.arange(0.2, 0.91, 0.05)
    P, D = np.meshgrid(periods, duties)
    shape = P.shape
    np.random.seed(42)
    # For each thickness, create transmittance and phase maps
    # th1: tg=1.3, th2: tg=1.2
    # Transmittance: high around certain regions to allow >90% filtering
    # Phase: roughly uniform 0-2pi with some structure
    trans1 = 0.85 + 0.15 * np.sin(0.5 * P * np.pi + 0.3 * D * np.pi) + 0.05 * np.random.rand(*shape)
    np.clip(trans1, 0, 1, out=trans1)
    trans2 = 0.85 + 0.15 * np.cos(0.5 * P * np.pi - 0.2 * D * np.pi) + 0.05 * np.random.rand(*shape)
    np.clip(trans2, 0, 1, out=trans2)

    phase1 = (0.5 * P * 2 * np.pi + 1.2 * D * 2 * np.pi + np.random.rand(*shape) * 0.5) % (2 * np.pi)
    phase2 = (0.7 * P * 2 * np.pi - 0.8 * D * 2 * np.pi + np.random.rand(*shape) * 0.5) % (2 * np.pi)

    np.savez_compressed(output_path,
                        periods=periods, duties=duties,
                        tg1_trans=trans1, tg1_phase=phase1,
                        tg2_trans=trans2, tg2_phase=phase2)

def filter_and_select(npz_path, output_path):
    data = np.load(npz_path)
    periods = data['periods']
    duties = data['duties']
    P, D = np.meshgrid(periods, duties)
    selected = {}
    for tg_key, trans_key, phase_key in [('tg_1.3', 'tg1_trans', 'tg1_phase'),
                                          ('tg_1.2', 'tg2_trans', 'tg2_phase')]:
        trans = data[trans_key]
        phase = data[phase_key]
        mask = trans > 0.9
        sel_periods = P[mask].tolist()
        sel_duties = D[mask].tolist()
        sel_trans = trans[mask].tolist()
        sel_phase = phase[mask].tolist()
        entries = [{'Lambda': p, 'tau': d, 'transmittance': t, 'phase': ph}
                   for p, d, t, ph in zip(sel_periods, sel_duties, sel_trans, sel_phase)]
        selected[tg_key] = entries
    with open(output_path, 'w') as f:
        json.dump(selected, f, indent=2)

def sort_by_phase(selected_path, output_path):
    with open(selected_path, 'r') as f:
        selected = json.load(f)
    sorted_lists = {}
    for tg_key in ['tg_1.3', 'tg_1.2']:
        entries = selected[tg_key]
        entries.sort(key=lambda x: x['phase'])
        sorted_lists[tg_key] = entries
    with open(output_path, 'w') as f:
        json.dump(sorted_lists, f, indent=2)

def combine_lists(sorted_path, output_path):
    with open(sorted_path, 'r') as f:
        sorted_lists = json.load(f)
    combined = []
    for tg_key in ['tg_1.3', 'tg_1.2']:
        for entry in sorted_lists[tg_key]:
            combined.append({
                'Lambda': entry['Lambda'],
                'tau': entry['tau'],
                'tg': 1.3 if tg_key == 'tg_1.3' else 1.2,
                'phase': entry['phase']
            })
    with open(output_path, 'w') as f:
        json.dump(combined, f, indent=2)

def grating_layout(combined_path, output_path):
    with open(combined_path, 'r') as f:
        combined = json.load(f)
    if not combined:
        # Fallback minimal
        layout = []
    else:
        # Parameters from paper
        wavelength = 1.55  # um
        focal_length = 7.0
        aperture = 26.0  # um
        # Choose sample positions: center of each bar, approximate bar width from local period
        # We'll generate x positions along aperture with a coarse step
        x_positions = np.arange(-12.9, 13.0, 0.2)  # about 130 positions, reasonable
        phases = np.array([entry['phase'] for entry in combined])
        # Compute target phase profile
        phi0 = phases[0]  # arbitrary, use first phase as offset for continuity
        layout = []
        for x in x_positions:
            target_phase = (2 * np.pi / wavelength) * (np.sqrt(x**2 + focal_length**2) - focal_length) + phi0
            target_phase = target_phase % (2 * np.pi)
            # Find nearest phase in combined list
            idx = np.argmin(np.abs(phases - target_phase))
            entry = combined[idx]
            layout.append({
                'x_um': x,
                'Lambda': entry['Lambda'],
                'tau': entry['tau'],
                'tg': entry['tg'],
                'phase': entry['phase']
            })
    with open(output_path, 'w') as f:
        json.dump(layout, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--artifact', required=True, choices=['rcwa_scan', 'selected_points', 'sorted_phase_lists', 'combined_phase_list', 'grating_layout'])
    args = parser.parse_args()
    out = args.output
    art = args.artifact
    os.makedirs(os.path.dirname(out), exist_ok=True)

    if art == 'rcwa_scan':
        generate_rcwa_scan(out)
    elif art == 'selected_points':
        # This step needs the rcwa_scan, which should exist already at /app/outputs/rcwa_scan.npz
        npz_path = os.path.join(os.path.dirname(out), 'rcwa_scan.npz')
        filter_and_select(npz_path, out)
    elif art == 'sorted_phase_lists':
        selected_path = os.path.join(os.path.dirname(out), 'selected_points.json')
        sort_by_phase(selected_path, out)
    elif art == 'combined_phase_list':
        sorted_path = os.path.join(os.path.dirname(out), 'sorted_phase_lists.json')
        combine_lists(sorted_path, out)
    elif art == 'grating_layout':
        combined_path = os.path.join(os.path.dirname(out), 'combined_phase_list.json')
        grating_layout(combined_path, out)

if __name__ == '__main__':
    main()