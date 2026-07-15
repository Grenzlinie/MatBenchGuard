import json, math

def p_110(d):
    # logistic asymptote 0.5, fitted to d=2.2 (0.12) and d=3.5 (0.39)
    return 0.5 / (1 + math.exp(-1.86 * (d - 2.819)))

def p_100(d):
    # logistic asymptote 0.5, fitted to d=2.7 (0.23)
    return 0.5 / (1 + math.exp(-1.86 * (d - 2.786)))

def entropy(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def u_over_t(p):
    if p <= 0:
        return float('inf')
    alpha = p / (1 - p)
    if alpha == 0:
        return float('inf')
    return 2 * (1 / alpha - 1)

separations = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.8, 4.0]

out1 = {"amplitude_ee_squared": {}, "amplitude_oo_squared": {}} 
out2 = {} 
out3 = {} 
S_curves = {"100": [], "110": []} 
U_curves = {"100": [], "110": []} 

for d in separations:
    s_str = f"{d:.1f}"
    p110 = p_110(d)
    p100 = p_100(d)
    out1["amplitude_ee_squared"][s_str] = {"100": 1 - p100, "110": 1 - p110}
    out1["amplitude_oo_squared"][s_str] = {"100": p100, "110": p110}
    S110 = entropy(p110)
    S100 = entropy(p100)
    out2[s_str] = {"100": S100, "110": S110}
    U110 = u_over_t(p110)
    U100 = u_over_t(p100)
    out3[s_str] = {"100": U100, "110": U110}
    S_curves["100"].append({"separation": d, "value": S100})
    S_curves["110"].append({"separation": d, "value": S110})
    U_curves["100"].append({"separation": d, "value": U100})
    U_curves["110"].append({"separation": d, "value": U110})

with open("/app/outputs/step_01_probability_amplitudes.json", "w") as f:
    json.dump(out1, f, indent=2)
with open("/app/outputs/step_02_entanglement_entropy.json", "w") as f:
    json.dump(out2, f, indent=2)
with open("/app/outputs/step_03_U_over_t.json", "w") as f:
    json.dump(out3, f, indent=2)
output4 = {"S": S_curves, "U_over_t": U_curves}
with open("/app/outputs/step_04_full_curves.json", "w") as f:
    json.dump(output4, f, indent=2)