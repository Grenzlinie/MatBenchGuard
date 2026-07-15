import json

data = {
    "Si46": {
        "avg_gamma": 0.95,
        "gamma_TA": 0.5,
        "gamma_LA": 0.9,
        "v_TA": 4.5,
        "v_LA": 7.8,
        "v_s": 5.0,
        "theta_TA": 125,
        "theta_LA": 145,
        "theta_D": 522,
        "kappa_l": 16.0
    },
    "Na8Si46": {
        "avg_gamma": 1.10,
        "gamma_TA": 0.4,
        "gamma_LA": 1.2,
        "v_TA": 4.4,
        "v_LA": 7.3,
        "v_s": 4.8,
        "theta_TA": 92,
        "theta_LA": 94,
        "theta_D": 535,
        "kappa_l": 2.7
    },
    "K8Si46": {
        "avg_gamma": 1.10,
        "gamma_TA": 0.5,
        "gamma_LA": 1.3,
        "v_TA": 4.0,
        "v_LA": 6.4,
        "v_s": 4.4,
        "theta_TA": 100,
        "theta_LA": 102,
        "theta_D": 481,
        "kappa_l": 5.2
    },
    "Ba8Si46": {
        "avg_gamma": 1.50,
        "gamma_TA": 1.1,
        "gamma_LA": 1.6,
        "v_TA": 3.0,
        "v_LA": 5.2,
        "v_s": 3.3,
        "theta_TA": 65,
        "theta_LA": 65,
        "theta_D": 360,
        "kappa_l": 1.0
    },
    "Ge46": {
        "avg_gamma": 1.00,
        "gamma_TA": 0.2,
        "gamma_LA": 1.1,
        "v_TA": 2.7,
        "v_LA": 4.6,
        "v_s": 3.0,
        "theta_TA": 75,
        "theta_LA": 87,
        "theta_D": 300,
        "kappa_l": 14.5
    },
    "K8Ge44\u25a12": {
        "avg_gamma": 1.20,
        "gamma_TA": 0.6,
        "gamma_LA": 1.6,
        "v_TA": 2.3,
        "v_LA": 3.7,
        "v_s": 2.5,
        "theta_TA": 51,
        "theta_LA": 57,
        "theta_D": 264,
        "kappa_l": 1.1
    },
    "Ba8Ge43\u25a13": {
        "avg_gamma": 1.60,
        "gamma_TA": 0.0,
        "gamma_LA": 0.0,
        "v_TA": 1.5,
        "v_LA": 3.0,
        "v_s": 1.6,
        "theta_TA": 20,
        "theta_LA": 25,
        "theta_D": 185,
        "kappa_l": 0.0
    }
}

with open("/app/outputs/table1_results.json", "w") as f:
    json.dump(data, f, indent=2)
