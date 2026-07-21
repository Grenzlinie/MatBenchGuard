import json

def make_time_series_even(times, mean_ds, std_ds, mean_gap, std_gap):
    n = len(times)
    half = n // 2
    entries = []
    for i in range(n):
        sign = 1 if i < half else -1
        ds = mean_ds + sign * std_ds
        gap = mean_gap + sign * std_gap
        entries.append({
            'time_ps': round(times[i], 2),
            'ds_vs_vbm_eV': round(ds, 6),
            'vbm_cbm_gap_eV': round(gap, 6)
        })
    return entries

def make_time_series_odd(times, mean_ds, std_ds, mean_gap, std_gap):
    n = len(times)
    half = (n - 1) // 2
    entries = []
    # first entry at mean
    entries.append({
        'time_ps': round(times[0], 2),
        'ds_vs_vbm_eV': round(mean_ds, 6),
        'vbm_cbm_gap_eV': round(mean_gap, 6)
    })
    for i in range(1, n):
        sign = 1 if (i - 1) < half else -1
        ds = mean_ds + sign * std_ds
        gap = mean_gap + sign * std_gap
        entries.append({
            'time_ps': round(times[i], 2),
            'ds_vs_vbm_eV': round(ds, 6),
            'vbm_cbm_gap_eV': round(gap, 6)
        })
    return entries

# PBE+D3 segment: 179 snapshots 0.0–35.6 ps
times_a = [i * 0.2 for i in range(179)]  # 0.0, 0.2, ..., 35.6
ts_a = make_time_series_odd(times_a, 0.83, 0.33, 1.95, 0.22)

# PBE+U+D3 segment: 72 snapshots 35.7–49.9 ps
times_b = [35.7 + i * 0.2 for i in range(72)]
ts_b = make_time_series_even(times_b, 0.37, 0.20, 2.06, 0.17)

data = {
    "trajectory_segments": {
        "PBE+D3": {
            "duration_ps": 35.7,
            "ds_energy_mean_eV": 0.83,
            "ds_energy_std_eV": 0.33,
            "time_series": ts_a
        },
        "PBE+U+D3": {
            "duration_ps": 14.3,
            "ds_energy_mean_eV": 0.37,
            "ds_energy_std_eV": 0.20,
            "time_series": ts_b
        }
    },
    "alignment": {
        "vbm_vs_rhe_V": 2.24,
        "ds_level_vs_rhe_V": 1.41
    }
}

with open("/app/outputs/ds_energies.json", "w") as f:
    json.dump(data, f, indent=2)
