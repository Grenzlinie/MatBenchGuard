import json

barriers = {
    "3E→2O": {"E_R": -0.68, "barrier": 2.52},
    "3A→2O": {"E_R": -0.74, "barrier": 2.33},
    "3C→2C": {"E_R": -1.16, "barrier": 1.64},
    "2C→V2": {"E_R": -1.85, "barrier": 4.33},
    "2O→V2": {"E_R": -3.06, "barrier": 2.46}
}

print(json.dumps(barriers, indent=2))
