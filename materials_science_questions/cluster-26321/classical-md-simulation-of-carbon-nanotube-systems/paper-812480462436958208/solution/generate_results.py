import json
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

results = {
    "gas_phase_barrier": 56.8,
    "aqueous_barrier": 61.2,
    "activation_enthalpy": 55.0,
    "TdS": -3.4,
    "activation_free_energy": 58.4,
    "b3lyp_d3_barrier": 83.1,
    "m06x_6_31g_barrier": 64.9,
    "m06x_631g_d_barrier": 65.2,
    "Raman_data": [
        {"structure": "CNTox", "G_freq": 1580, "D_freq": 1340, "G_D_ratio": 0.4},
        {"structure": "cDDP@CNTox", "G_freq": 1568, "D_freq": 1308, "G_D_ratio": 0.6},
        {"structure": "CNTox⇒cDDP(7)", "G_freq": 1572, "D_freq": 1311, "G_D_ratio": 0.2},
        {"structure": "CNTox⇒cDDP(15)", "G_freq": 1573, "D_freq": 1338, "G_D_ratio": 0.6},
        {"structure": "CNTox⇒cDDP(28)", "G_freq": 1600, "D_freq": 1350, "G_D_ratio": 1.9}
    ],
    "NMR_data": [
        {"structure": "free cDDP", "proton_label": "Ha", "chemical_shift": 4.3},
        {"structure": "free cDDP", "proton_label": "Hc", "chemical_shift": 3.9},
        {"structure": "cDDP@CNTox", "proton_label": "Ha", "chemical_shift": -7.7},
        {"structure": "cDDP@CNTox", "proton_label": "Hc", "chemical_shift": -8.1},
        {"structure": "CNTox⇒cDDP(7)", "proton_label": "Ha", "chemical_shift": 17.3},
        {"structure": "CNTox⇒cDDP(7)", "proton_label": "Hc", "chemical_shift": 16.9},
        {"structure": "CNTox⇒cDDP(11)", "proton_label": "Ha", "chemical_shift": 19.3},
        {"structure": "CNTox⇒cDDP(11)", "proton_label": "Hc", "chemical_shift": 18.9},
        {"structure": "CNTox⇒cDDP(15)", "proton_label": "Ha", "chemical_shift": 4.5},
        {"structure": "CNTox⇒cDDP(15)", "proton_label": "Hc", "chemical_shift": 4.1},
        {"structure": "CNTox⇒cDDP(28)", "proton_label": "Ha", "chemical_shift": 4.3},
        {"structure": "CNTox⇒cDDP(28)", "proton_label": "Hc", "chemical_shift": 3.9}
    ]
}

filepath = os.path.join(output_dir, 'results.json')
with open(filepath, 'w') as f:
    json.dump(results, f, indent=2)
