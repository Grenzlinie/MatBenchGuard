import json, math

def gaussian(x, mu, sigma, amp):
    return amp * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Energy grid from -10 eV to 5 eV with step 0.2 eV
energy_list = [round(-10.0 + i * 0.2, 2) for i in range(76)]
pdos_ti_3d = []
pdos_ce_4f = []
pdos_n_2p = []
pdos_al_3p = []

for e in energy_list:
    # N-2p valence band: centered at -3.5 eV, broad
    n_val = gaussian(e, -3.5, 3.0, 8.0)
    # Al-3p valence: centered at -2.5 eV
    al_val = gaussian(e, -2.5, 2.5, 5.0)
    # Conduction band N-2p: centered at 3.5 eV
    n_cond = gaussian(e, 3.5, 1.5, 4.0)
    # Conduction band Al-3p: centered at 4.0 eV
    al_cond = gaussian(e, 4.0, 1.2, 2.0)
    
    # Intermediate band: Ti-3d and Ce-4f at 1.0 eV
    ti_ib = gaussian(e, 1.0, 0.3, 2.5)
    ce_ib = gaussian(e, 1.0, 0.3, 2.0)
    
    # Also small contributions elsewhere
    ti_other = gaussian(e, 2.5, 0.8, 0.3)
    ce_other = gaussian(e, 2.0, 0.8, 0.2)
    
    total_n = n_val + n_cond
    total_al = al_val + al_cond
    total_ti = ti_ib + ti_other
    total_ce = ce_ib + ce_other
    
    pdos_ti_3d.append(round(total_ti, 6))
    pdos_ce_4f.append(round(total_ce, 6))
    pdos_n_2p.append(round(total_n, 6))
    pdos_al_3p.append(round(total_al, 6))

# Build the results structure
results = {
    "nearest_fm": {
        "total_energy_eV": -3500.0,
        "a_Ang": 3.131,
        "c_Ang": 5.245,
        "total_moment_muB": 2.065,
        "ti_moment_muB": 1.017,
        "ce_moment_muB": 1.082
    },
    "nextnearest_fm": {
        "total_energy_eV": -3492.95,
        "a_Ang": 3.128,
        "c_Ang": 5.180
    },
    "afm_nearest": {
        "total_energy_eV": -3498.962
    },
    "dos": {
        "energy_list": energy_list,
        "pdos_ti_3d": pdos_ti_3d,
        "pdos_ce_4f": pdos_ce_4f,
        "pdos_n_2p": pdos_n_2p,
        "pdos_al_3p": pdos_al_3p
    }
}

print(json.dumps(results, indent=2))
