import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict

# ---------------------------------------------------------------------------
# Lightweight replacements for numpy / scipy.interpolate that avoid any
# third‑party dependency.  The verifier sandbox ships only stdlib.
# ---------------------------------------------------------------------------

def _ensure_seq(x, dtype=float):
    """Turn a scalar or iterable into a list of dtype."""
    try:
        return [dtype(v) for v in x]
    except TypeError:
        return [dtype(x)]

def _vec_op(op, a, b):
    """Element‑wise arithmetic between two sequences (scalars handled)."""
    a = _ensure_seq(a)
    b = _ensure_seq(b)
    return [op(av, bv) for av, bv in zip(a, b)]

def _add(a, b): return _vec_op(float.__add__, a, b)
def _sub(a, b): return _vec_op(float.__sub__, a, b)
def _mul(a, b): return _vec_op(float.__mul__, a, b)

def _sqrt(x):
    x = _ensure_seq(x)
    return [math.sqrt(v) for v in x]

def _mean(x):
    x = _ensure_seq(x)
    if not x:
        return 0.0
    return sum(x) / len(x)

def _clip(x, low, high):
    x = _ensure_seq(x)
    return [max(low, min(high, v)) for v in x]

def _argsort(seq):
    """Return indices that sort seq ascending."""
    return sorted(range(len(seq)), key=seq.__getitem__)

def _linspace(start, stop, num):
    if num <= 1:
        return [start]
    dx = (stop - start) / (num - 1)
    return [start + i * dx for i in range(num)]

# ---------------------------------------------------------------------------
# Minimal linear interpolation (replaces scipy.interpolate.interp1d)
# ---------------------------------------------------------------------------
class _Interp1d:
    def __init__(self, x, y, kind='linear', fill_value='extrapolate'):
        self.x = _ensure_seq(x)
        self.y = _ensure_seq(y)
        if len(self.x) != len(self.y):
            raise ValueError('x and y must have same length')
        # sort by x
        order = _argsort(self.x)
        self.x = [self.x[i] for i in order]
        self.y = [self.y[i] for i in order]
        self.kind = kind
        self.fill_value = fill_value

    def __call__(self, xnew):
        xnew = _ensure_seq(xnew)
        result = []
        for xv in xnew:
            # find bracketing interval
            if xv <= self.x[0]:
                if self.fill_value == 'extrapolate':
                    # linear extrapolation using first two points
                    if len(self.x) >= 2:
                        dx = self.x[1] - self.x[0]
                        dy = self.y[1] - self.y[0]
                        if dx != 0:
                            result.append(self.y[0] + dy * (xv - self.x[0]) / dx)
                        else:
                            result.append(self.y[0])
                    else:
                        result.append(self.y[0])
                else:
                    result.append(self.y[0])
                continue
            if xv >= self.x[-1]:
                if self.fill_value == 'extrapolate':
                    n = len(self.x)
                    if n >= 2:
                        dx = self.x[-1] - self.x[-2]
                        dy = self.y[-1] - self.y[-2]
                        if dx != 0:
                            result.append(self.y[-1] + dy * (xv - self.x[-1]) / dx)
                        else:
                            result.append(self.y[-1])
                    else:
                        result.append(self.y[-1])
                else:
                    result.append(self.y[-1])
                continue
            # binary search for interval
            lo, hi = 0, len(self.x) - 1
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if self.x[mid] <= xv:
                    lo = mid
                else:
                    hi = mid
            dx = self.x[hi] - self.x[lo]
            if dx == 0:
                result.append(self.y[lo])
            else:
                t = (xv - self.x[lo]) / dx
                result.append(self.y[lo] + t * (self.y[hi] - self.y[lo]))
        return result

# Provide aliases so existing scorer code works unchanged (they use "np.array" etc.)
class _Np:
    """Minimal numpy‑compatible namespace."""
    @staticmethod
    def array(x, dtype=None):
        lst = _ensure_seq(x)
        # if dtype is specified, just return list — scorers treat it as list anyway
        return lst
    sqrt = math.sqrt
    mean = _mean
    clip = _clip
    argsort = _argsort
    max = max
    min = min
    abs = abs

np = _Np()
interp1d = _Interp1d


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
        ctx = {}
        steps = spec.get('steps', [])
        ctx['step_details'] = {step['id']: step for step in steps if 'id' in step}
        ctx['nominal_capacity_As'] = 10 * 3600
        ctx['current_map'] = {'C_5': 2, 'C_2': 5, '1C': 10, '2C': 20}
        return ctx


# === block: score_0 (check id='step_validation_check') ===
def score_0(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        ref_data = step.get('reference_data', {}).get('conditions', {})
        tol_voltage = step.get('tol_voltage_nrmse', 0.05)
        tol_swelling = step.get('tol_swelling_nrmse', 0.05)
        tol_force = step.get('tol_jig_force_nrmse', 0.10)
        nominal_cap = ctx['nominal_capacity_As']
        current_map = ctx['current_map']
        # Group rows by configuration and C-rate
        from collections import defaultdict
        groups = defaultdict(list)
        for row in artifact:
            try:
                key = (row['configuration'], row['c_rate'])
                groups[key].append((float(row['time_s']), float(row['voltage_V']), float(row['swelling_m']), float(row['jig_force_N'])))
            except (KeyError, ValueError):
                continue
        if not groups:
            return 0.0
        scores = []
        for key, rows in groups.items():
            config, crate = key
            I = current_map.get(crate)
            if I is None:
                continue
            rows.sort(key=lambda r: r[0])
            t = np.array([r[0] for r in rows])
            v_agent = np.array([r[1] for r in rows])
            s_agent = np.array([r[2] for r in rows])
            f_agent = np.array([r[3] for r in rows])
            soc = 1.0 - (t * I) / nominal_cap
            soc = np.clip(soc, 0.0, 1.0)
            ref_key = f"{config}_{crate}"
            if ref_key not in ref_data:
                continue
            ref = ref_data[ref_key]
            ref_soc = np.array(ref['soc'])
            ref_v = np.array(ref['voltage_V'])
            ref_s = np.array(ref['swelling_m'])
            ref_f = np.array(ref['jig_force_N'])
            # sort both by soc ascending
            sort_agent = np.argsort(soc)
            soc_agent_sorted = soc[sort_agent]
            v_agent_sorted = v_agent[sort_agent]
            s_agent_sorted = s_agent[sort_agent]
            f_agent_sorted = f_agent[sort_agent]
            sort_ref = np.argsort(ref_soc)
            ref_soc_sorted = ref_soc[sort_ref]
            ref_v_sorted = ref_v[sort_ref]
            ref_s_sorted = ref_s[sort_ref]
            ref_f_sorted = ref_f[sort_ref]
            # interpolate reference to agent soc
            interp_v = interp1d(ref_soc_sorted, ref_v_sorted, kind='linear', fill_value='extrapolate')(soc_agent_sorted)
            interp_s = interp1d(ref_soc_sorted, ref_s_sorted, kind='linear', fill_value='extrapolate')(soc_agent_sorted)
            interp_f = interp1d(ref_soc_sorted, ref_f_sorted, kind='linear', fill_value='extrapolate')(soc_agent_sorted)
            def nrmse(pred, ref):
                rmse = np.sqrt(np.mean((pred - ref)**2))
                range_val = np.max(ref) - np.min(ref)
                if range_val == 0:
                    return 0.0
                return rmse / range_val
            nrmse_v = nrmse(v_agent_sorted, interp_v)
            nrmse_s = nrmse(s_agent_sorted, interp_s)
            nrmse_f = nrmse(f_agent_sorted, interp_f)
            def score_nrmse(err, tol):
                if err <= tol:
                    return 1.0
                else:
                    return max(0.0, 1.0 - (err - tol) / tol)
            cond_score = (score_nrmse(nrmse_v, tol_voltage) + score_nrmse(nrmse_s, tol_swelling) + score_nrmse(nrmse_f, tol_force)) / 3.0
            scores.append(cond_score)
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_1 (check id='step_lithiation_check') ===
def score_1(artifact, step, ctx):
        if not artifact or len(artifact) == 0:
            return 0.0
        ref_pressures = step.get('reference_data', {}).get('pressures', [])
        tol_rel = step.get('tolerance_relative', 0.15)
        nominal_cap = ctx['nominal_capacity_As']
        # Build lookup: pressure -> dict with soc->conc_sep, conc_cc from agent data
        from collections import defaultdict
        data_by_pressure = defaultdict(list)
        for row in artifact:
            try:
                p = float(row['pressure_MPa'])
                t = float(row['time_s'])
                soc = float(row['soc'])
                sep = float(row['anode_conc_sep_mol_m3'])
                cc = float(row['anode_conc_cc_mol_m3'])
                data_by_pressure[p].append((t, soc, sep, cc))
            except (KeyError, ValueError):
                continue
        if not data_by_pressure:
            return 0.0
        # For each pressure, get values at soc 0.5 and 1.0 by linear interpolation
        pressures_list = sorted(data_by_pressure.keys())
        agent_values = {}
        for p in pressures_list:
            rows = data_by_pressure[p]
            rows.sort(key=lambda r: r[1])  # sort by soc
            soc_arr = np.array([r[1] for r in rows])
            sep_arr = np.array([r[2] for r in rows])
            cc_arr = np.array([r[3] for r in rows])
            # Get nearest to soc 0.5 and 1.0
            def get_value_at_soc(soc_arr, val_arr, target_soc):
                idx = np.argmin(np.abs(soc_arr - target_soc))
                return val_arr[idx]
            sep_05 = get_value_at_soc(soc_arr, sep_arr, 0.5)
            sep_10 = get_value_at_soc(soc_arr, sep_arr, 1.0)
            cc_05 = get_value_at_soc(soc_arr, cc_arr, 0.5)
            cc_10 = get_value_at_soc(soc_arr, cc_arr, 1.0)
            agent_values[p] = {'sep_05': sep_05, 'sep_10': sep_10, 'cc_05': cc_05, 'cc_10': cc_10}
        # Check monotonic increase for sep at 0.5 and 1.0: higher pressure should give larger conc
        def monotonic_score(values, psorted):
            # values is dict p->value
            all_inc = True
            for i in range(1, len(psorted)):
                if values[psorted[i]] <= values[psorted[i-1]]:
                    all_inc = False
                    break
            return 1.0 if all_inc else 0.0
        sep_mono_05 = monotonic_score({p: agent_values[p]['sep_05'] for p in pressures_list}, pressures_list)
        sep_mono_10 = monotonic_score({p: agent_values[p]['sep_10'] for p in pressures_list}, pressures_list)
        # Average monotonic score
        mono_score = (sep_mono_05 + sep_mono_10) / 2.0
        # Closeness to reference
        ref_dict = {entry['pressure_MPa']: entry for entry in ref_pressures}
        closeness_scores = []
        for entry in ref_pressures:
            p = entry['pressure_MPa']
            if p not in agent_values:
                continue
            agent = agent_values[p]
            for soc_target, idx in [(0.5, 0), (1.0, 1)]:
                ref_sep = entry['anode_conc_sep_mol_m3'][idx]
                ref_cc = entry['anode_conc_cc_mol_m3'][idx]
                agent_sep = agent['sep_05'] if soc_target == 0.5 else agent['sep_10']
                agent_cc = agent['cc_05'] if soc_target == 0.5 else agent['cc_10']
                if ref_sep > 0:
                    err_sep = abs(agent_sep - ref_sep) / ref_sep
                else:
                    err_sep = 0.0
                if ref_cc > 0:
                    err_cc = abs(agent_cc - ref_cc) / ref_cc
                else:
                    err_cc = 0.0
                # score each error with linear decay beyond tolerance
                def rel_score(err):
                    if err <= tol_rel:
                        return 1.0
                    else:
                        return max(0.0, 1.0 - (err - tol_rel) / tol_rel)
                sep_s = rel_score(err_sep)
                cc_s = rel_score(err_cc)
                closeness_scores.append((sep_s + cc_s) / 2.0)
        if closeness_scores:
            close_score = np.mean(closeness_scores)
        else:
            close_score = 0.0
        overall_score = 0.5 * mono_score + 0.5 * close_score
        return float(overall_score)


_SCORERS = {
    'step_validation_check': score_0,
    'step_lithiation_check': score_1,
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
