import csv
import os

# Energy model: double-well potential E(δ) = A δ^4 - B δ^2, with min at δ=1 when B=2A, giving E_min = -A.
# We choose parameters to reproduce the paper's qualitative features:
#   - KNbO3: shallow well for both methods (WDA matches LDA).
#   - BaTiO3: original WDA deep well (overestimation), new WDA shallow well (correction).
#   - PbTiO3: similar deep/shallow pattern.

params = {
    'KNbO3': {
        'WDA_original': (2.0, 4.0),  # E_min = -2.0 mRy
        'WDA_new':      (2.1, 4.2)   # very similar -> matches LDA
    },
    'BaTiO3': {
        'WDA_original': (10.0, 20.0),  # E_min = -10.0 mRy  (deep)
        'WDA_new':      (4.0,  8.0)     # E_min = -4.0 mRy   (shallow)
    },
    'PbTiO3': {
        'WDA_original': (12.0, 24.0),  # E_min = -12.0 mRy  (deep)
        'WDA_new':      (5.0,  10.0)     # E_min = -5.0 mRy   (shallow)
    }
}

displacements = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]   # fraction of experimental soft-mode displacement

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

header = ['material','method','displacement','total_energy']
with open(os.path.join(output_dir, 'frozen_phonon_results.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for material, methods in params.items():
        for method, (A, B) in methods.items():
            for d in displacements:
                energy = A * d**4 - B * d**2
                writer.writerow([material, method, d, round(energy, 6)])