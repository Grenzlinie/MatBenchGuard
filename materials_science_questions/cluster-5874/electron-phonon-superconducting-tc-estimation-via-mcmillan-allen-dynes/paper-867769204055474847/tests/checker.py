import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os

# Pure-Python emulations of numpy and scipy.signal used by the scorer

class _Array:
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, idx):
        # boolean indexing
        if isinstance(idx, _Array) and len(idx) > 0 and isinstance(idx.data[0], bool):
            return _Array([self.data[i] for i, b in enumerate(idx.data) if b])
        # integer list indexing
        if isinstance(idx, (list, _Array)):
            idx_list = idx.data if isinstance(idx, _Array) else idx
            return _Array([self.data[i] for i in idx_list])
        return self.data[idx]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __ge__(self, other):
        return _Array([x >= other for x in self.data])

    def __le__(self, other):
        return _Array([x <= other for x in self.data])

    def __abs__(self):
        return _Array([abs(x) for x in self.data])

    def max(self):
        return max(self.data)

    def any(self):
        return any(self.data)


class _NP:
    @staticmethod
    def array(x):
        return _Array(x)

    @staticmethod
    def max(x):
        if isinstance(x, _Array):
            return x.max()
        return max(x)

    @staticmethod
    def argmax(x):
        if isinstance(x, _Array):
            return x.data.index(x.max())
        return x.index(max(x))

    @staticmethod
    def logical_and(a, b):
        if isinstance(a, _Array) and isinstance(b, _Array):
            return _Array([ai and bi for ai, bi in zip(a.data, b.data)])
        return _Array([])

    @staticmethod
    def any(x):
        if isinstance(x, _Array):
            return x.any()
        return any(x)

    @staticmethod
    def abs(x):
        if isinstance(x, _Array):
            return abs(x)
        return abs(x)


class _SP:
    @staticmethod
    def find_peaks(x, height=None, prominence=None):
        """Minimal pure-Python peak finder."""
        if isinstance(x, _Array):
            x = x.data
        n = len(x)
        if n < 3:
            return ([], {})
        peaks = []
        for i in range(1, n - 1):
            if x[i] > x[i - 1] and x[i] > x[i + 1]:
                # height filter
                if height is not None and x[i] < height:
                    continue
                # approximate prominence
                if prominence is not None and prominence > 0:
                    left_max = max(x[:i]) if i > 0 else x[i]
                    right_max = max(x[i + 1:]) if i + 1 < n else x[i]
                    drop_left = x[i] - left_max if left_max < x[i] else 0.0
                    drop_right = x[i] - right_max if right_max < x[i] else 0.0
                    prom = min(drop_left, drop_right)
                    if prom < prominence:
                        continue
                peaks.append(i)
        if not peaks:
            return ([], {})
        properties = {'peak_heights': [x[i] for i in peaks]}
        return (peaks, properties)


np = _NP()
sp = _SP()


import os as _ff_os
import json as _ff_json


def _ff_validate_output_contract():
    """Return a list of shape violations against grading_spec['output_contract']."""
    spec_path = "/tests/grading_spec.json"
    if not _ff_os.path.exists(spec_path):
        return []
    with open(spec_path) as _f:
        _spec = _ff_json.load(_f)
    contract = _spec.get("output_contract", {}) or {}
    outputs = contract.get("outputs", []) or []
    out_dir = "/app/outputs"
    violations = []
    for out in outputs:
        base = str(out.get("file", "")).split("/")[-1]
        if not base:
            continue
        path = _ff_os.path.join(out_dir, base)
        if not _ff_os.path.isfile(path):
            violations.append("missing output_contract file: " + base)
            continue
        fmt = out.get("format", "")
        schema = out.get("schema", {}) or {}
        if fmt == "json":
            try:
                data = _ff_json.load(open(path))
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": invalid JSON (" + str(exc) + ")")
                continue
            required = schema.get("required", {})
            fields = required.keys() if isinstance(required, dict) else (required or [])
            if isinstance(data, dict):
                for field in fields:
                    if field not in data:
                        violations.append(base + ": missing JSON field '" + str(field) + "'")
        elif fmt in ("csv", "tsv"):
            import csv as _ff_csv
            delim = "\t" if fmt == "tsv" else ","
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:  # noqa: BLE001
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations


def _ff_contract_gate():
    """Zero the reward and exit if the submission violates the output_contract shape."""
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


def load_artifact(path):
    if not path or not os.path.exists(path):
        return None
    if path.endswith(".json"):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:  # noqa: BLE001
            return None
    if path.endswith(".csv") or path.endswith(".tsv"):
        delim = "\t" if path.endswith(".tsv") else ","
        with open(path, newline="") as f:
            return list(csv.DictReader(f, delimiter=delim))
    with open(path) as f:
        return f.read()


def prepare(outputs_dir, spec):
    step_ref = None
    for s in spec.get('steps', []):
        if s.get('id') == 'recompute_peaks_and_trends':
            step_ref = s.get('reference', {})
            break
    return {'spec': spec, 'step_ref': step_ref}


# === block: score_0 (check id='recompute_peaks_and_trends') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0

    # Parse CSV
    reader = artifact
    rows_by_condition = {}
    for row in reader:
        cond = row.get('condition', '').strip()
        try:
            omega = float(row.get('omega', 0))
            n_val = float(row.get('alpha2F_n', 0))
            p_val = float(row.get('alpha2F_p', 0))
        except (TypeError, ValueError):
            continue
        if not cond:
            continue
        rows_by_condition.setdefault(cond, []).append((omega, n_val, p_val))

    ref = ctx.get('step_ref', {})
    if not ref:
        return 0.0

    meta_map = ref.get('condition_meta', {})
    low_w = ref.get('low_window', [0, 20])
    broad_w = ref.get('broad_window', [20, 60])
    min_height = ref.get('min_peak_height', 0.001)
    min_prominence = ref.get('min_prominence', 0.0005)
    tolerances = ref.get('tolerances', {})
    gold_peaks = ref.get('gold_peaks', {})

    # Helper to find dominant peak in a window
    def find_peak(omegas, values, window, min_h, min_p):
        lo, hi = window
        mask = np.logical_and(omegas >= lo, omegas <= hi)
        local_omegas = omegas[mask]
        local_vals = values[mask]
        if len(local_omegas) == 0:
            return None, None
        peaks_idx, props = sp.find_peaks(local_vals, height=min_h, prominence=min_p)
        if len(peaks_idx) == 0:
            return None, None
        # take the highest peak
        best_i = peaks_idx[np.argmax(local_vals[peaks_idx])]
        peak_pos = local_omegas[best_i]
        peak_val = local_vals[best_i]
        return peak_pos, peak_val

    # Compute peaks for all conditions
    computed = {}
    for cond, rows in rows_by_condition.items():
        if not rows:
            continue
        omegas = np.array([r[0] for r in rows])
        n_vals = np.array([r[1] for r in rows])
        p_vals = np.array([r[2] for r in rows])
    
        lp_n, lv_n = find_peak(omegas, n_vals, low_w, min_height, min_prominence)
        bp_n, bv_n = find_peak(omegas, n_vals, broad_w, min_height, min_prominence)
        lp_p, lv_p = find_peak(omegas, p_vals, low_w, min_height, min_prominence)
        bp_p, bv_p = find_peak(omegas, p_vals, broad_w, min_height, min_prominence)
    
        # also compute max amplitudes in windows
        low_mask = np.logical_and(omegas >= low_w[0], omegas <= low_w[1])
        max_n_low = np.max(np.abs(n_vals[low_mask])) if np.any(low_mask) else 0.0
        max_p_low = np.max(np.abs(p_vals[low_mask])) if np.any(low_mask) else 0.0
        max_n_all = np.max(np.abs(n_vals))
        max_p_all = np.max(np.abs(p_vals))
    
        computed[cond] = {
            'lp_n': lp_n, 'lv_n': lv_n if lv_n is not None else 0,
            'bp_n': bp_n, 'bv_n': bv_n if bv_n is not None else 0,
            'lp_p': lp_p, 'lv_p': lv_p if lv_p is not None else 0,
            'bp_p': bp_p, 'bv_p': bv_p if bv_p is not None else 0,
            'max_n_low': max_n_low,
            'max_p_low': max_p_low,
            'max_n_all': max_n_all,
            'max_p_all': max_p_all,
        }

    # ---- sub-checks ----
    sub_scores = []
    sub_weights = []

    # 1. Absolute peak positions for AN 0.15 (weight 0.25)
    gold = gold_peaks.get('AN_delta0.15_T0.002J', None)
    if gold and 'AN_delta0.15_T0.002J' in computed:
        c = computed['AN_delta0.15_T0.002J']
        low_tol = tolerances.get('low_peak', 2.0)
        broad_tol = tolerances.get('broad_peak', 5.0)
        ok = True
        if c['lp_n'] is None or abs(c['lp_n'] - gold.get('low_peak_n', 5.0)) > low_tol:
            ok = False
        if c['bp_n'] is None or abs(c['bp_n'] - gold.get('broad_peak_n', 40.0)) > broad_tol:
            ok = False
        if c['lp_p'] is None or abs(c['lp_p'] - gold.get('low_peak_p', 5.0)) > low_tol:
            ok = False
        if c['bp_p'] is None or abs(c['bp_p'] - gold.get('broad_peak_p', 40.0)) > broad_tol:
            ok = False
        sub_scores.append(1.0 if ok else 0.0)
    else:
        sub_scores.append(0.0)
    sub_weights.append(0.25)

    # 2. Doping shift at antinode (weight 0.25)
    doping_conds = ['AN_delta0.06_T0.002J', 'AN_delta0.09_T0.002J', 'AN_delta0.12_T0.002J', 'AN_delta0.15_T0.002J']
    bp_n_positions = []
    bp_p_positions = []
    for cond in doping_conds:
        if cond in computed and computed[cond]['bp_n'] is not None:
            bp_n_positions.append(computed[cond]['bp_n'])
        else:
            bp_n_positions.append(None)
        if cond in computed and computed[cond]['bp_p'] is not None:
            bp_p_positions.append(computed[cond]['bp_p'])
        else:
            bp_p_positions.append(None)

    def is_strictly_increasing(pos_list):
        """Check if the list of non-None values is strictly increasing."""
        valid = [p for p in pos_list if p is not None]
        if len(valid) < 2:
            return False
        return all(x < y for x, y in zip(valid, valid[1:]))

    shift_ok = is_strictly_increasing(bp_n_positions) and is_strictly_increasing(bp_p_positions)
    sub_scores.append(1.0 if shift_ok else 0.0)
    sub_weights.append(0.25)

    # 3. Momentum AN->HS decrease, energy shift, and HS near-zero (weight 0.25)
    an_cond = 'AN_delta0.15_T0.002J'
    hs_cond = 'HS_delta0.15_T0.002J'
    an_c = computed.get(an_cond)
    hs_c = computed.get(hs_cond)
    if an_c and hs_c:
        # Amplitude decrease: low-energy normal amplitude at HS < at AN
        amp_an = an_c['max_n_low']
        amp_hs = hs_c['max_n_low']
        decrease_ok = (amp_hs < amp_an)
        # Energy shift: if low-energy peaks exist, they must be lower at HS
        shift_ok = True
        if an_c['lp_n'] is not None and hs_c['lp_n'] is not None:
            if hs_c['lp_n'] >= an_c['lp_n']:
                shift_ok = False
        if an_c['lp_p'] is not None and hs_c['lp_p'] is not None:
            if hs_c['lp_p'] >= an_c['lp_p']:
                shift_ok = False
        # HS near-zero: overall amplitude < 0.01
        hs_zero_ok = (hs_c['max_n_all'] < 0.01) and (hs_c['max_p_all'] < 0.01)
        sub_scores.append(1.0 if (decrease_ok and shift_ok and hs_zero_ok) else 0.0)
    else:
        sub_scores.append(0.0)
    sub_weights.append(0.25)

    # 4. Pairing at node zero (weight 0.1)
    nd_cond = 'ND_delta0.15_T0.002J'
    nd_c = computed.get(nd_cond)
    if nd_c:
        pairing_zero_ok = (nd_c['max_p_all'] < 1e-6)
        sub_scores.append(1.0 if pairing_zero_ok else 0.0)
    else:
        sub_scores.append(0.0)
    sub_weights.append(0.1)

    # 5. Temperature persistence (weight 0.15)
    low_temp_cond = 'AN_delta0.09_T0.002J'
    high_temp_cond = 'AN_delta0.09_T0.06J'
    lt_c = computed.get(low_temp_cond)
    ht_c = computed.get(high_temp_cond)
    if lt_c and ht_c:
        # peaks must still be detected in normal channel
        peaks_exist = (ht_c['lp_n'] is not None) and (ht_c['bp_n'] is not None)
        # amplitudes reduced
        reduced = (ht_c['lv_n'] < lt_c['lv_n']) and (ht_c['bv_n'] < lt_c['bv_n'])
        temp_ok = peaks_exist and reduced
        sub_scores.append(1.0 if temp_ok else 0.0)
    else:
        sub_scores.append(0.0)
    sub_weights.append(0.15)

    # Aggregate
    if len(sub_scores) == 0:
        return 0.0
    total = sum(s * w for s, w in zip(sub_scores, sub_weights)) / sum(sub_weights)
    return max(0.0, min(1.0, total))


# === block: score_1 (check id='check_reported_peaks') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, dict):
        return 0.0

    reported = artifact
    # Load CSV to recompute peaks
    csv_path = '/app/outputs/eliashberg_functions.csv'
    if not os.path.exists(csv_path):
        return 0.0

    import csv
    with open(csv_path, newline='') as f:
        reader = list(csv.DictReader(f))
    if not reader:
        return 0.0

    # recompute peaks (same logic as above but reusable helper not available; duplicate necessary code)
    rows_by = {}
    for row in reader:
        cond = row.get('condition', '').strip()
        try:
            omega = float(row.get('omega', 0))
            n = float(row.get('alpha2F_n', 0))
            p = float(row.get('alpha2F_p', 0))
        except:
            continue
        if not cond:
            continue
        rows_by.setdefault(cond, []).append((omega, n, p))

    low_w = [0, 20]
    broad_w = [20, 60]
    min_h = 0.001
    min_p = 0.0005

    def find_peak(omegas, values, window, min_h, min_p):
        lo, hi = window
        mask = np.logical_and(omegas >= lo, omegas <= hi)
        lo_om = omegas[mask]
        lo_val = values[mask]
        if len(lo_om) == 0:
            return None, None
        peaks, props = sp.find_peaks(lo_val, height=min_h, prominence=min_p)
        if len(peaks) == 0:
            return None, None
        best = peaks[np.argmax(lo_val[peaks])]
        return lo_om[best], lo_val[best]

    computed = {}
    for cond, rows in rows_by.items():
        if not rows:
            continue
        omegas = np.array([r[0] for r in rows])
        n_vals = np.array([r[1] for r in rows])
        p_vals = np.array([r[2] for r in rows])
        lp_n, _ = find_peak(omegas, n_vals, low_w, min_h, min_p)
        bp_n, _ = find_peak(omegas, n_vals, broad_w, min_h, min_p)
        lp_p, _ = find_peak(omegas, p_vals, low_w, min_h, min_p)
        bp_p, _ = find_peak(omegas, p_vals, broad_w, min_h, min_p)
        computed[cond] = {
            'low_peak_omega_n': lp_n,
            'broad_peak_omega_n': bp_n,
            'low_peak_omega_p': lp_p,
            'broad_peak_omega_p': bp_p
        }

    tol = step.get('reference', {}).get('tolerance', 0.1)
    total_fields = 0
    matched = 0
    for cond, exp in computed.items():
        rep = reported.get(cond)
        if rep is None:
            continue
        for key in ['low_peak_omega_n','broad_peak_omega_n','low_peak_omega_p','broad_peak_omega_p']:
            total_fields += 1
            comp_val = exp.get(key)
            rep_val = rep.get(key)
            if comp_val is None and rep_val is None:
                matched += 1
            elif comp_val is not None and rep_val is not None:
                if abs(comp_val - rep_val) <= tol:
                    matched += 1

    if total_fields == 0:
        return 0.0
    return float(matched) / float(total_fields)


_SCORERS = {
    'recompute_peaks_and_trends': score_0,
    'check_reported_peaks': score_1,
}


def _step_id(step, index):
    sid = str(step.get("id", "")).strip()
    if sid:
        return sid
    output = str(step.get("output_file", "")).split("/")[-1].rsplit(".", 1)[0]
    kind = str(step.get("kind") or step.get("metric") or "score").strip()
    base = "_".join(part for part in (output, kind) if part).strip("_")
    return base or ("check_" + str(index))


def main():
    _ff_contract_gate()
    with open("/tests/grading_spec.json") as f:
        spec = json.load(f)
    outputs_dir = "/app/outputs"
    ctx = prepare(outputs_dir, spec)
    steps = spec.get("steps", spec.get("checks", [])) or []
    breakdown = {}
    total = 0.0
    for index, step in enumerate(steps):
        sid = _step_id(step, index)
        output_file = str(step.get("output_file", "")).split("/")[-1]
        weight = float(step.get("weight", 0.0))
        artifact = load_artifact(os.path.join(outputs_dir, output_file)) if output_file else None
        fn = _SCORERS.get(sid)
        if fn is None:
            score = 0.0
        else:
            try:
                score = float(fn(artifact, step, ctx))
            except Exception as exc:  # noqa: BLE001
                score = 0.0
                breakdown.setdefault("_errors", {})[sid] = repr(exc)
        score = max(0.0, min(1.0, score))
        breakdown[sid or output_file] = {"score": score, "weight": weight}
        total += score * weight
    os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as f:
        f.write(str(round(total, 6)))
    with open("/logs/verifier/breakdown.json", "w") as f:
        json.dump(breakdown, f, indent=2)


if __name__ == "__main__":
    main()
