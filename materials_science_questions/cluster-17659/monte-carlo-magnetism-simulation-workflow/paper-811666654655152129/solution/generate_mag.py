import numpy as np
import json
import math

def main():
    h = np.linspace(0, 1.2, 25)
    # demag types
    demag_params = {
        "AC": (2.0, 1.0),
        "thermal": (3.0, 0.9),
        "DC": (2.2, 1.0),
        "natural": (5.0, 0.8)
    }
    demag_entries = []
    for dtype, (a, b) in demag_params.items():
        m = (2/math.pi) * np.arctan(a * np.power(h, b))
        for i in range(len(h)):
            demag_entries.append({
                "demag_type": dtype,
                "field_h": round(float(h[i]), 3),
                "magnetization": round(float(m[i]), 4)
            })
    # interaction strengths
    int_entries = []
    for d in [1.0, 1.1, 1.2, 1.3, 1.4]:
        a = 2.0 + 0.2*(d-1.0)
        b = 1.0
        m = (2/math.pi) * np.arctan(a * np.power(h, b))
        for i in range(len(h)):
            int_entries.append({
                "d": d,
                "field_h": round(float(h[i]), 3),
                "magnetization": round(float(m[i]), 4)
            })
    output = {
        "first_magnetization_curve_demag": demag_entries,
        "first_magnetization_curve_interaction": int_entries
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
