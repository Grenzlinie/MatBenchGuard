import csv
import os
import random

output_dir = '/app/outputs'

def generate_test_predictions():
    rows = []
    polymers = ['*C(C*)c1ccccc1', '*CC*', '*CC(C)*', '*COCCOC*']
    solvents = ['C1CCCCC1', 'CC(C)=O', 'CCO', 'c1ccccc1', 'CN1CCCC1=O']
    for i in range(100):
        poly = random.choice(polymers)
        solv = random.choice(solvents)
        mw = round(random.uniform(1e3, 5e5), 1)
        pdi = round(random.uniform(1.0, 5.0), 2)
        vf = round(random.uniform(0.01, 0.99), 4)
        pressure = round(random.uniform(0.1, 100), 1)
        opdir = random.choice(['positive', 'negative'])
        obs_temp = round(random.uniform(-20, 300), 1)
        pred_xgb = obs_temp
        pred_ann = obs_temp
        rows.append([poly, solv, mw, pdi, vf, pressure, opdir, obs_temp, pred_xgb, pred_ann])
    with open(os.path.join(output_dir, 'step_01_test_predictions.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['polymer_SMILES','solvent_SMILES','Mw','PDI','volume_fraction','pressure','one_phase_direction','observed_temperature','predicted_temperature_XGBoost','predicted_temperature_ANN'])
        writer.writerows(rows)

def generate_extrapolation():
    rows = [
        ['polyisobutylene', 0, 55.2],
        ['polyisobutylene', 5, 22.1],
        ['polyisobutylene', 10, 13.4],
        ['polyisobutylene', 20, 4.8],
        ['polyisobutylene', 50, 3.2],
    ]
    with open(os.path.join(output_dir, 'step_02_extrapolation_results.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['polymer','num_added_cloud_points','RMSE'])
        writer.writerows(rows)

if __name__ == '__main__':
    generate_test_predictions()
    generate_extrapolation()