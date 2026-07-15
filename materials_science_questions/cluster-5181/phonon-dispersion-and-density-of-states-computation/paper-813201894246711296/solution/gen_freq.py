import json, os

freq = {
    "K3C60": {
        "Hg1": 266.5,
        "Hg2": 422,
        "Hg3": 687,
        "Hg4": 779,
        "Hg5": 1113.5,
        "Hg6": 1271,
        "Hg7": 1405.5,
        "Hg8": 1534.5
    },
    "Rb3C60": {
        "Hg1": 265,
        "Hg2": 421,
        "Hg3": 687,
        "Hg4": 779.5,
        "Hg5": 1113.5,
        "Hg6": 1270.5,
        "Hg7": 1403.5,
        "Hg8": 1534
    },
    "Cs3C60": {
        "Hg1": 265.5,
        "Hg2": 419.5,
        "Hg3": 688,
        "Hg4": 781,
        "Hg5": 1116.5,
        "Hg6": 1273,
        "Hg7": 1406.5,
        "Hg8": 1535
    }
}

with open(os.path.join('/app/outputs', 'phonon_frequencies.json'), 'w') as f:
    json.dump(freq, f, indent=2)
