import json

data = {
    "P-SeMoS": {
        "band_gap_PBE": 1.02,
        "band_gap_HSE06": 1.82,
        "VBM_energy_vacuum": 1.74,
        "CBM_energy_vacuum": -0.084,
        "VBM_localization": "SMoSe",
        "CBM_localization": "SMoSe",
        "alignment_type": "I",
        "water_splitting_type": "overall"
    },
    "P-SMoSe": {
        "band_gap_PBE": 0.93,
        "band_gap_HSE06": 1.30,
        "VBM_energy_vacuum": 1.58,
        "CBM_energy_vacuum": 0.076,
        "VBM_localization": "blueP",
        "CBM_localization": "SMoSe",
        "alignment_type": "II",
        "water_splitting_type": "oxidation_only"
    },
    "P-SeWS": {
        "band_gap_PBE": 0.92,
        "band_gap_HSE06": 1.62,
        "VBM_energy_vacuum": 1.60,
        "CBM_energy_vacuum": -0.25,
        "VBM_localization": "blueP",
        "CBM_localization": "SWSe",
        "alignment_type": "II",
        "water_splitting_type": "overall"
    },
    "P-SWSe": {
        "band_gap_PBE": 0.90,
        "band_gap_HSE06": 1.60,
        "VBM_energy_vacuum": 1.59,
        "CBM_energy_vacuum": -0.013,
        "VBM_localization": "blueP",
        "CBM_localization": "SWSe",
        "alignment_type": "II",
        "water_splitting_type": "overall"
    }
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
