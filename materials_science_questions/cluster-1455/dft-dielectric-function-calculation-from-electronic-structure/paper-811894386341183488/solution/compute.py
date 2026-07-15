import json

# Localization parameter
alpha = 1.0

def p1(x):
    # p1 = (1 - 1/((alpha+1)*(alpha+3))) * x
    return (1.0 - 1.0 / ((alpha + 1.0) * (alpha + 3.0))) * x

def p2(x):
    # p2 = (alpha+2)/(alpha+3) * x
    return (alpha + 2.0) / (alpha + 3.0) * x

def p3_(x):
    # p3 = (alpha+2)/((alpha+1)*(alpha+3)) * x
    return (alpha + 2.0) / ((alpha + 1.0) * (alpha + 3.0)) * x

def Tc(p):
    p_min = 0.07
    p_max = 0.2
    T_star = 9000.0
    if p_min <= p <= p_max:
        return (p_max - p) * (p - p_min) * T_star
    else:
        return 0.0

data = {}
for x_val, key in [(0.45, "x_045"), (0.15, "x_015")]:
    p1v = p1(x_val)
    p2v = p2(x_val)
    p3v = p3_(x_val)
    Tcv = Tc(p3v)
    data[key] = {
        "p1": p1v,
        "p2": p2v,
        "p3": p3v,
        "Tc": Tcv
    }

outpath = "/app/outputs/hole_densities_and_Tc.json"
with open(outpath, "w") as f:
    json.dump(data, f, indent=4)
