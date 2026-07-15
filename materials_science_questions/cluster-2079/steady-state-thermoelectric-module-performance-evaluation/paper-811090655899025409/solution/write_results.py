import json, sys

data = {
    "max_power": {
        "S_nh_opt": 0.93,
        "S_ph_opt": 0.76,
        "a_opt": 0.56,
        "P_m_max": 1725.33,
        "eta_max": 12.70
    },
    "max_efficiency": {
        "S_nh_opt": 0.89,
        "S_ph_opt": 0.73,
        "a_opt": 0.43,
        "P_m_max": 1637.37,
        "eta_max": 13.35
    }
}

with open(sys.argv[1], 'w') as f:
    json.dump(data, f, indent=2)
