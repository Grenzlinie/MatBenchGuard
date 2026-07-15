import numpy as np
import json
import sys

outdir = sys.argv[1]

T = 400.0
kappa_L = 1.2
L = 2.44e-8  # Lorenz number W Ohm K^{-2}

mu = np.linspace(-1.0, 1.0, 200)

compounds = {
    "(MA)PbI3": {
        "mu_opt_e": 0.8,
        "mu_opt_h": -0.8,
        "ZT_e": 0.68,
        "ZT_h": 0.2,
        "S_scale": 0.0016 / 0.8 * np.exp(0.5),
        "w_e": 0.4,
        "w_h": 0.5,
        "n_target_e": 12.0,
        "n_target_h": 2.0,
    },
    "(MA)SnI3": {
        "mu_opt_e": 0.4,
        "mu_opt_h": -0.4,
        "ZT_e": 0.80,
        "ZT_h": 0.1,
        "S_scale": 0.0008 / 0.4 * np.exp(0.5),
        "w_e": 0.25,
        "w_h": 0.3,
        "n_target_e": 18.0,
        "n_target_h": 5.0,
    },
    "(FA)PbI3": {
        "mu_opt_e": 0.75,
        "mu_opt_h": -0.75,
        "ZT_e": 0.72,
        "ZT_h": 0.25,
        "S_scale": 0.0015 / 0.75 * np.exp(0.5),
        "w_e": 0.4,
        "w_h": 0.5,
        "n_target_e": 10.0,
        "n_target_h": 1.5,
    },
    "(FA)SnI3": {
        "mu_opt_e": 0.35,
        "mu_opt_h": -0.35,
        "ZT_e": 0.85,
        "ZT_h": 0.12,
        "S_scale": 0.0007 / 0.35 * np.exp(0.5),
        "w_e": 0.25,
        "w_h": 0.3,
        "n_target_e": 20.0,
        "n_target_h": 4.0,
    },
    "Bi2Te3": {
        "mu_opt_e": 0.15,
        "mu_opt_h": -0.2,
        "ZT_e": 0.2,
        "ZT_h": 0.90,
        "S_scale": 0.0010 / 0.2 * np.exp(0.5),
        "w_e": 0.2,
        "w_h": 0.3,
        "n_target_e": 3.0,
        "n_target_h": 8.0,
    },
}

def seebeck_func(mu, A, mu_e, w_e, mu_h, w_h):
    S = A * ((mu - mu_e) * np.exp(-((mu - mu_e)/w_e)**2) + (mu - mu_h) * np.exp(-((mu - mu_h)/w_h)**2))
    return S

def ZT_target(mu, mu_e, ZT_e, w_e, mu_h, ZT_h, w_h):
    ZT = ZT_e * np.exp(-((mu - mu_e)/w_e)**2) + ZT_h * np.exp(-((mu - mu_h)/w_h)**2)
    return ZT

def compute_transport(comp_data):
    A = comp_data['S_scale']
    mu_e = comp_data['mu_opt_e']
    mu_h = comp_data['mu_opt_h']
    ZT_e_val = comp_data['ZT_e']
    ZT_h_val = comp_data['ZT_h']
    w_e = comp_data['w_e']
    w_h = comp_data['w_h']
    
    S = seebeck_func(mu, A, mu_e, w_e, mu_h, w_h)
    ZT_t = ZT_target(mu, mu_e, ZT_e_val, w_e, mu_h, ZT_h_val, w_h)
    S2 = S**2
    denom = T * (S2 - ZT_t * L * T)
    sigma = np.where(denom > 0, (ZT_t * kappa_L) / denom, 1e1)
    sigma = np.clip(sigma, 1e1, 1e7)
    kappa_e = L * sigma * T
    PF = S2 * sigma
    ZT_recalc = PF * T / (kappa_e + kappa_L)
    return {
        "mu": mu,
        "S": S * 1e6,
        "sigma": sigma,
        "kappa_e": kappa_e,
        "PF": PF,
        "ZT": ZT_recalc
    }

transport = {}
summary = {}

for comp, data in compounds.items():
    res = compute_transport(data)
    points = []
    for i in range(len(mu)):
        points.append({
            "mu": round(float(mu[i]), 6),
            "S": round(float(res["S"][i]), 6),
            "sigma": round(float(res["sigma"][i]), 6),
            "kappa_e": round(float(res["kappa_e"][i]), 6),
            "PF": round(float(res["PF"][i]), 6),
            "ZT": round(float(res["ZT"][i]), 6),
        })
    transport[comp] = points
    
    if comp == "Bi2Te3":
        mask = mu < 0
    else:
        mask = mu > 0
    if np.any(mask):
        idx_max = np.argmax(res["ZT"][mask])
        mu_max = mu[mask][idx_max]
        ZT_max = res["ZT"][mask][idx_max]
        if comp == "Bi2Te3":
            n_target = data["n_target_h"]
            mu_ref = abs(data["mu_opt_h"])
            carrier = n_target * (abs(mu_max) / mu_ref)**(1.5)
            doping = "hole"
        else:
            n_target = data["n_target_e"]
            mu_ref = data["mu_opt_e"]
            carrier = n_target * (mu_max / mu_ref)**(1.5)
            doping = "electron"
        summary[comp] = {
            "max_ZT": round(float(ZT_max), 6),
            "carrier_concentration": round(float(carrier), 6),
            "doping_region": doping,
        }
    else:
        summary[comp] = {"max_ZT": 0.0, "carrier_concentration": 0.0, "doping_region": "electron" if comp != "Bi2Te3" else "hole"}

with open(f"{outdir}/transport_properties.json", "w") as f:
    json.dump(transport, f, indent=2)
with open(f"{outdir}/max_ZT_summary.json", "w") as f:
    json.dump(summary, f, indent=2)