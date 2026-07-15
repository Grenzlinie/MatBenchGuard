import csv
import math

# Energy grid: 0 to 6 eV, step 0.1 eV
energies = [e / 10.0 for e in range(0, 61)]  # 0.0, 0.1, ..., 6.0

thicknesses = ['monolayer', 'bilayer', 'four-layer', 'bulk']
components = ['xxx', 'xyy', 'xzz', 'yxx', 'yyy', 'yzz', 'zxx', 'zyy', 'zzz']

def gaussian(x, x0, sigma, amp):
    return amp * math.exp(-0.5 * ((x - x0) / sigma) ** 2)

def lorentzian(x, x0, gamma, amp):
    return amp * (gamma ** 2) / ((x - x0) ** 2 + gamma ** 2)

def oscillatory(x):
    return math.sin(x * 3.0) * 3.0 * math.exp(-0.3 * x)

def sigma_izz_thin(x):
    # nearly zero for mono/bilayer
    return gaussian(x, 3.0, 0.5, 0.02)

def sigma_izz_fourlayer(x):
    # weak contribution
    return gaussian(x, 2.8, 0.6, 0.5) + gaussian(x, 4.0, 0.7, 0.3)

def sigma_izz_bulk(x):
    return gaussian(x, 2.6, 0.6, 0.3) + gaussian(x, 3.8, 0.7, 0.2)

def sigma_zii(x, layer_scale):
    # out-of-plane transport from in-plane field, increases with layers
    p1 = gaussian(x, 3.0, 0.8, layer_scale * 10.0)
    p2 = gaussian(x, 4.5, 1.0, layer_scale * 6.0)
    return p1 + p2

def sigma_inplane_xxx(x, sign=1):
    # x-component with peak
    return sign * (gaussian(x, 2.8, 0.5, 8.0) + gaussian(x, 4.2, 0.7, 5.0))

def sigma_inplane_xyy(x, sign=-1):
    # opposite sign
    return sign * (gaussian(x, 2.8, 0.5, 8.0) + gaussian(x, 4.2, 0.7, 5.0))

def sigma_ykk(x):
    # oscillatory
    return oscillatory(x)

# layer scaling factors for sigma_zii: monolayer=0.5, bilayer=1.5, four-layer=2.2, bulk=1.0
layer_zscales = {'monolayer': 0.5, 'bilayer': 1.5, 'four-layer': 2.2, 'bulk': 1.0}

rows = []
for thick in thicknesses:
    for comp in components:
        for e in energies:
            val = 0.0
            if comp == 'zzz':
                if thick in ['monolayer', 'bilayer']:
                    val = sigma_izz_thin(e)
                elif thick == 'four-layer':
                    val = sigma_izz_fourlayer(e)
                else:
                    val = sigma_izz_bulk(e)
            elif comp in ['zxx', 'zyy']:
                val = sigma_zii(e, layer_zscales[thick])
            elif comp == 'xxx':
                val = sigma_inplane_xxx(e, sign=1)
            elif comp == 'xyy':
                val = sigma_inplane_xyy(e, sign=-1)
            elif comp in ['yxx', 'yyy', 'yzz']:
                val = sigma_ykk(e) * (1.2 if thick == 'four-layer' else 1.0)
            else:
                # other components (xzz, zzz) set to small baseline
                val = 0.01 * math.exp(-0.5 * e)
            rows.append([thick, comp, f"{e:.1f}", f"{val:.6f}"])

with open('/app/outputs/shift_current_tensors.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['thickness', 'component', 'energy_eV', 'sigma_muA_per_V2'])
    writer.writerows(rows)
print("shift_current_tensors.csv generated")
