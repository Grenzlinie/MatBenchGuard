import json

data = [
    {
        "name": "Si46",
        "gamma_300": 0.95,
        "gamma_TA": 0.5,
        "gamma_LA": 0.9,
        "v_TA": 4.5,
        "v_LA": 7.8,
        "v_s": 5.0,
        "theta_TA": 125,
        "theta_LA": 145,
        "theta_D": 522,
        "kappa_l_300": 16.0,
        "spectral_width": 480,
        "rattler_freq": None
    },
    {
        "name": "Na8Si46",
        "gamma_300": 1.10,
        "gamma_TA": 0.4,
        "gamma_LA": 1.2,
        "v_TA": 4.4,
        "v_LA": 7.3,
        "v_s": 4.8,
        "theta_TA": 92,
        "theta_LA": 94,
        "theta_D": 535,
        "kappa_l_300": 2.7,
        "spectral_width": 340,
        "rattler_freq": 110
    },
    {
        "name": "K8Si46",
        "gamma_300": 1.10,
        "gamma_TA": 0.5,
        "gamma_LA": 1.3,
        "v_TA": 4.0,
        "v_LA": 6.4,
        "v_s": 4.4,
        "theta_TA": 100,
        "theta_LA": 102,
        "theta_D": 481,
        "kappa_l_300": 5.2,
        "spectral_width": 350,
        "rattler_freq": 130
    },
    {
        "name": "Ge46",
        "gamma_300": 1.00,
        "gamma_TA": 0.2,
        "gamma_LA": 1.1,
        "v_TA": 2.7,
        "v_LA": 4.6,
        "v_s": 3.0,
        "theta_TA": 75,
        "theta_LA": 87,
        "theta_D": 300,
        "kappa_l_300": 14.5,
        "spectral_width": 300,
        "rattler_freq": None
    },
    {
        "name": "K8Ge44\u25a12",
        "gamma_300": 1.20,
        "gamma_TA": 0.6,
        "gamma_LA": 1.6,
        "v_TA": 2.3,
        "v_LA": 3.7,
        "v_s": 2.5,
        "theta_TA": 51,
        "theta_LA": 57,
        "theta_D": 264,
        "kappa_l_300": 1.1,
        "spectral_width": 270,
        "rattler_freq": 80
    }
]

with open("/app/outputs/computed_properties.json", "w") as f:
    json.dump(data, f, indent=2)