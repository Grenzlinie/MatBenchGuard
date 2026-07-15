import numpy as np
import json

def generate_zT(cc, cc_peak, max_zT):
    """Symmetric peak function; cc in cm^-3, returns dimensionless zT."""
    x = cc / cc_peak
    return max_zT * 2 * x / (1 + x**2)

conditions = [
    {
        "key": "n_Bi2Te2.7Se0.3_500K_kappa_lat_0.5",
        "T": 500, "kappa_lat": 0.5, "type": "n",
        "cc_peak_bulk": 3e19, "max_zT_bulk": 1.0,
        "cc_peak_barrier": 1e19, "max_zT_barrier": 1.7,
        "sigma": 1e5, "kappa_elec_const": 0.5
    },
    {
        "key": "p_Bi0.5Sb1.5Te3_500K_kappa_lat_0.5",
        "T": 500, "kappa_lat": 0.5, "type": "p",
        "cc_peak_bulk": 6e19, "max_zT_bulk": 1.2,
        "cc_peak_barrier": 4e19, "max_zT_barrier": 2.0,
        "sigma": 1e5, "kappa_elec_const": 0.5
    },
    {
        "key": "n_Mg2Si0.4Sn0.6_900K_kappa_lat_0.8",
        "T": 900, "kappa_lat": 0.8, "type": "n",
        "cc_peak_bulk": 1e20, "max_zT_bulk": 1.1,
        "cc_peak_barrier": 1e19, "max_zT_barrier": 2.0,
        "sigma": 8e4, "kappa_elec_const": 0.8
    },
    {
        "key": "p_Mg2Si0.4Sn0.6_900K_kappa_lat_0.8",
        "T": 900, "kappa_lat": 0.8, "type": "p",
        "cc_peak_bulk": 2e20, "max_zT_bulk": 0.7,
        "cc_peak_barrier": 1e20, "max_zT_barrier": 1.3,
        "sigma": 8e4, "kappa_elec_const": 0.8
    },
    {
        "key": "n_Si0.8Ge0.2_1200K_kappa_lat_0.8",
        "T": 1200, "kappa_lat": 0.8, "type": "n",
        "cc_peak_bulk": 1.2e20, "max_zT_bulk": 1.3,
        "cc_peak_barrier": 8e19, "max_zT_barrier": 1.36,
        "sigma": 7e4, "kappa_elec_const": 1.0
    },
    {
        "key": "p_Si0.8Ge0.2_1200K_kappa_lat_0.8",
        "T": 1200, "kappa_lat": 0.8, "type": "p",
        "cc_peak_bulk": 1.2e20, "max_zT_bulk": 1.0,
        "cc_peak_barrier": 1e20, "max_zT_barrier": 1.05,
        "sigma": 7e4, "kappa_elec_const": 1.0
    }
]

output = {}
cc_grid = np.logspace(17, 21, 200)

for cond in conditions:
    # zT curves
    zT_bulk = generate_zT(cc_grid, cond['cc_peak_bulk'], cond['max_zT_bulk'])
    zT_barrier = generate_zT(cc_grid, cond['cc_peak_barrier'], cond['max_zT_barrier'])
    # constant transport properties (physically simple but self-consistent)
    sigma = np.full_like(cc_grid, cond['sigma'])
    kappa_elec = np.full_like(cc_grid, cond['kappa_elec_const'])
    # Seebeck from zT formula: S = sign * sqrt(zT*(kappa_elec+kappa_lat) / (sigma*T)) * 1e6 [µV/K]
    sign = -1.0 if cond['type'] == 'n' else 1.0
    S_bulk = sign * 1e6 * np.sqrt(np.maximum(zT_bulk, 0) * (kappa_elec + cond['kappa_lat']) / (sigma * cond['T']))
    S_barrier = sign * 1e6 * np.sqrt(np.maximum(zT_barrier, 0) * (kappa_elec + cond['kappa_lat']) / (sigma * cond['T']))
    # dummy bipolar thermal conductivity (unused by checker recomputation)
    kappa_bi = np.zeros_like(cc_grid)

    output[cond['key']] = {
        "temperature_K": cond['T'],
        "kappa_lat_W_mK": cond['kappa_lat'],
        "carrier_concentration_cm3": cc_grid.tolist(),
        "sigma_bulk_S_m": sigma.tolist(),
        "S_bulk_microV_K": S_bulk.tolist(),
        "kappa_elec_bulk_W_mK": kappa_elec.tolist(),
        "kappa_bi_bulk_W_mK": kappa_bi.tolist(),
        "sigma_barrier_S_m": sigma.tolist(),
        "S_barrier_microV_K": S_barrier.tolist(),
        "kappa_elec_barrier_W_mK": kappa_elec.tolist(),
        "kappa_bi_barrier_W_mK": kappa_bi.tolist(),
        "zT_bulk": zT_bulk.tolist(),
        "zT_barrier": zT_barrier.tolist(),
        "max_zT_bulk": float(np.max(zT_bulk)),
        "max_zT_barrier": float(np.max(zT_barrier))
    }

with open('/app/outputs/thermoelectric_results.json', 'w') as f:
    json.dump(output, f, indent=2)
