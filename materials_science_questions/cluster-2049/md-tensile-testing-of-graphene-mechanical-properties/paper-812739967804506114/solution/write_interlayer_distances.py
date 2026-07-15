import json

data = {
    "Y_d1": None,
    "Y_d2": 0.3592,
    "Y_d3": 0.3473,
    "Y_d_i": 0.9219,
    "Y_d_o": 1.9038,
    "Z_d1": 0.3472,
    "Z_d2": 0.3353,
    "Z_d3": 0.3352,
    "Z_d_i": 0.6945,
    "Z_d_o": 1.7122
}
print(json.dumps(data, indent=2))
