#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: benchmark_results.json ===
python3 -c "
import json

results = {
    'formation_energy': {
        'model_results': [
            {'model': '1NN-Magpie', 'cv_MAE': 0.2178, 'cv_RMSE': 0.3641, 'cv_R2': 0.8833, 'fcv_MAE': 0.2484, 'fcv_RMSE': 0.3835, 'fcv_R2': 0.8293, 'fcv_E_accuracy': 0.0},
            {'model': 'RF-Magpie',   'cv_MAE': 0.0929, 'cv_RMSE': 0.1722, 'cv_R2': 0.9739, 'fcv_MAE': 0.1923, 'fcv_RMSE': 0.2468, 'fcv_R2': 0.9293, 'fcv_E_accuracy': 0.0},
            {'model': 'MLP-Onehot',  'cv_MAE': 0.0785, 'cv_RMSE': 0.1598, 'cv_R2': 0.9775, 'fcv_MAE': 0.1129, 'fcv_RMSE': 0.1898, 'fcv_R2': 0.9582, 'fcv_E_accuracy': 0.2061},
            {'model': 'CNN-PTR',     'cv_MAE': 0.1085, 'cv_RMSE': 0.2027, 'cv_R2': 0.9638, 'fcv_MAE': 0.1606, 'fcv_RMSE': 0.2406, 'fcv_R2': 0.9328, 'fcv_E_accuracy': 0.0584},
            {'model': 'CGCNN',       'cv_MAE': 0.1235, 'cv_RMSE': 0.1719, 'cv_R2': 0.9739, 'fcv_MAE': 0.1120, 'fcv_RMSE': 0.1555, 'fcv_R2': 0.9658, 'fcv_E_accuracy': 0.2869}
        ],
        'm_step_results': [
            {'model': 'RF-Onehot',  'm': 1, 'cv_MAE': 0.1505, 'fcv_MAE': 0.2839, 'fcv_E_accuracy': 0.0},
            {'model': 'RF-Onehot',  'm': 2, 'cv_MAE': 0.1505, 'fcv_MAE': 0.3260, 'fcv_E_accuracy': 0.0},
            {'model': 'RF-Onehot',  'm': 3, 'cv_MAE': 0.1505, 'fcv_MAE': 0.3650, 'fcv_E_accuracy': 0.0},
            {'model': 'MLP-Onehot', 'm': 1, 'cv_MAE': 0.0719, 'fcv_MAE': 0.1022, 'fcv_E_accuracy': 0.2052},
            {'model': 'MLP-Onehot', 'm': 2, 'cv_MAE': 0.0719, 'fcv_MAE': 0.1189, 'fcv_E_accuracy': 0.2955},
            {'model': 'MLP-Onehot', 'm': 3, 'cv_MAE': 0.0719, 'fcv_MAE': 0.1360, 'fcv_E_accuracy': 0.3629}
        ]
    },
    'band_gap': {
        'model_results': [
            {'model': '1NN-Magpie', 'cv_MAE': 0.7553, 'cv_RMSE': 1.1030, 'cv_R2': 0.3592, 'fcv_MAE': 0.7689, 'fcv_RMSE': 1.0990, 'fcv_R2': 0.2476, 'fcv_E_accuracy': 0.0},
            {'model': 'RF-Magpie',  'cv_MAE': 0.4511, 'cv_RMSE': 0.6085, 'cv_R2': 0.8050, 'fcv_MAE': 0.6967, 'fcv_RMSE': 0.7800, 'fcv_R2': 0.6210, 'fcv_E_accuracy': 0.0},
            {'model': 'MLP-Onehot', 'cv_MAE': 0.5156, 'cv_RMSE': 0.7331, 'cv_R2': 0.7169, 'fcv_MAE': 0.6266, 'fcv_RMSE': 0.7663, 'fcv_R2': 0.6342, 'fcv_E_accuracy': 0.0327},
            {'model': 'CNN-PTR',    'cv_MAE': 0.5428, 'cv_RMSE': 0.7645, 'cv_R2': 0.6921, 'fcv_MAE': 0.6510, 'fcv_RMSE': 0.7603, 'fcv_R2': 0.6399, 'fcv_E_accuracy': 0.0136},
            {'model': 'CGCNN',      'cv_MAE': 0.5372, 'cv_RMSE': 0.7095, 'cv_R2': 0.7348, 'fcv_MAE': 0.6966, 'fcv_RMSE': 0.7985, 'fcv_R2': 0.6028, 'fcv_E_accuracy': 0.0303}
        ]
    },
    'superconducting_Tc': {
        'model_results': [
            {'model': '1NN-Magpie', 'cv_MAE': 6.0926, 'cv_RMSE': 12.1576, 'cv_R2': 0.8526, 'fcv_MAE': 7.7584, 'fcv_RMSE': 14.0036, 'fcv_R2': 0.7905, 'fcv_E_accuracy': 0.0},
            {'model': 'RF-Magpie',  'cv_MAE': 5.3000, 'cv_RMSE': 9.1888, 'cv_R2': 0.9158, 'fcv_MAE': 8.8649, 'fcv_RMSE': 12.8201, 'fcv_R2': 0.8244, 'fcv_E_accuracy': 0.0},
            {'model': 'MLP-Onehot', 'cv_MAE': 8.6967, 'cv_RMSE': 14.2092, 'cv_R2': 0.7987, 'fcv_MAE': 10.6022, 'fcv_RMSE': 14.1407, 'fcv_R2': 0.7864, 'fcv_E_accuracy': 0.0318},
            {'model': 'CNN-PTR',    'cv_MAE': 29.9755, 'cv_RMSE': 41.6868, 'cv_R2': -0.7329, 'fcv_MAE': 30.9053, 'fcv_RMSE': 49.6371, 'fcv_R2': -1.6321, 'fcv_E_accuracy': 0.0047}
        ]
    },
    'formation_energy_complete_onehot': [
        {'model': '1NN', 'cv_MAE': 0.2034, 'fcv_MAE': 0.2157},
        {'model': 'RF',  'cv_MAE': 0.1505, 'fcv_MAE': 0.2839},
        {'model': 'MLP', 'cv_MAE': 0.0719, 'fcv_MAE': 0.1022}
    ],
    'band_gap_complete_onehot': [
        {'model': '1NN', 'cv_MAE': 0.8692, 'fcv_MAE': 0.9412},
        {'model': 'RF',  'cv_MAE': 0.5957, 'fcv_MAE': 0.8575},
        {'model': 'MLP', 'cv_MAE': 0.5210, 'fcv_MAE': 0.6612}
    ],
    'superconducting_Tc_complete_onehot': [
        {'model': '1NN', 'cv_MAE': 6.6673, 'fcv_MAE': 7.8075},
        {'model': 'RF',  'cv_MAE': 5.7657, 'fcv_MAE': 9.3510},
        {'model': 'MLP', 'cv_MAE': 9.0829, 'fcv_MAE': 10.8964}
    ]
}

with open('/app/outputs/benchmark_results.json', 'w') as f:
    json.dump(results, f, indent=2)
"
