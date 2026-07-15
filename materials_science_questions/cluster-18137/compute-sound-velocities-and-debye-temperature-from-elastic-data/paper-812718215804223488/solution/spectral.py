import json

data = {
    "Si46": {"spectral_width": 480.0},
    "Ge46": {"spectral_width": 280.0},
    "Na8Si46": {"reduction_percent": 30.0},
    "K8Si46": {"reduction_percent": 30.0},
    "Ba8Si46": {"reduction_percent": 30.0},
    "K8Ge44\u25a12": {"reduction_percent": 10.0},
    "Ba8Ge43\u25a13": {"reduction_percent": 10.0}
}

with open("/app/outputs/spectral_width_report.json", "w") as f:
    json.dump(data, f, indent=2)
