import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import math

# ----------------------------------------------------------------------
# Minimal numpy‑like helpers so the checker works without the real numpy
# ----------------------------------------------------------------------
class _Arr(list):
    """list subclass that supports element‑wise comparison and advanced indexing."""
    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return _Arr([x < other for x in self])
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, (int, float)):
            return _Arr([x <= other for x in self])
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return _Arr([x > other for x in self])
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return _Arr([x >= other for x in self])
        return NotImplemented

    def __getitem__(self, idx):
        if isinstance(idx, (list, tuple, _Arr)):
            return _Arr([super(_Arr, self).__getitem__(int(i)) for i in idx])
        return super(_Arr, self).__getitem__(idx)


class np:
    @staticmethod
    def array(iterable):
        return _Arr(iterable)

    @staticmethod
    def argsort(arr):
        return sorted(range(len(arr)), key=lambda i: arr[i])

    @staticmethod
    def concatenate(arrays):
        res = _Arr()
        for a in arrays:
            res.extend(a)
        return res

    @staticmethod
    def any(iterable):
        return any(iterable)

    @staticmethod
    def all(iterable):
        return all(iterable)

    @staticmethod
    def argmin(arr):
        return min(range(len(arr)), key=lambda i: arr[i])

    @staticmethod
    def max(arr):
        return max(arr)

    @staticmethod
    def mean(arr):
        if len(arr) == 0:
            return 0.0
        return sum(arr) / len(arr)


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
    def load_csv_cols(path, t_col, cp_col):
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        Ts = []
        Cps = []
        for r in rows:
            try:
                t = float(r[t_col])
                cp = float(r[cp_col])
                Ts.append(t)
                Cps.append(cp)
            except (ValueError, KeyError):
                continue
        if not Ts:
            return np.array([]), np.array([])
        order = np.argsort(Ts)
        T = np.array(Ts)[order]
        Cp = np.array(Cps)[order]
        return T, Cp

    outputs_dir = os.path.join('/app/outputs')  # prepare receives outputs_dir
    smoothed_path = os.path.join(outputs_dir, 'smoothed_heat_capacity.csv')
    if not os.path.exists(smoothed_path):
        return {'smoothed_cp': None}
    T, Cp = load_csv_cols(smoothed_path, 'T_K', 'Cp_cal_per_K_mol')
    if len(T) == 0:
        return {'smoothed_cp': None}
    # Ensure starting point near zero; prepend (0,0) if needed
    if T[0] > 1.0:
        T = np.concatenate(([0.0], T))
        Cp = np.concatenate(([0.0], Cp))
    return {'smoothed_cp': {'T': T, 'Cp': Cp}}


# === block: score_0 (check id='smoothed_cp_structure') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        # artifact is the loaded CSV as list of dicts, but we already have ctx.smoothed_cp
        data = ctx.get('smoothed_cp')
        if data is None:
            return 0.0
        T = data['T']
        Cp = data['Cp']
        # check positivity
        if np.any(Cp < 0):
            return 0.0
        # check temperature range covers at least up to 298.15 and starts low
        if T[-1] < 298.15 or T[0] > 15:
            return 0.5
        # all good
        return 1.0


# === block: score_1 (check id='smoothed_cp_curve_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = ctx.get('smoothed_cp')
        if data is None:
            return 0.0
        T = data['T']
        Cp = data['Cp']
        params = step.get('params', {})
        tol_Cp = params.get('tol_Cp', 0.8)
        def nearest_idx(tv):
            return np.argmin(np.abs(T - tv))
        # get indices
        i200 = nearest_idx(200.0)
        i220 = nearest_idx(220.0)
        i270 = nearest_idx(270.0)
        i298 = nearest_idx(298.15)
        # conditions
        cond1 = Cp[i220] > Cp[i200]  # monotonic increase before hump
        cond2 = Cp[i270] > Cp[i220]   # hump higher
        cond3 = Cp[i270] > Cp[i298]   # hump decreasing after peak
        # check bounds
        cond4 = np.all(Cp > 0) and np.max(Cp) < 40.0
        score = 0.0
        if cond1:
            score += 0.25
        if cond2:
            score += 0.25
        if cond3:
            score += 0.25
        if cond4:
            score += 0.25
        return score


# === block: score_2 (check id='recompute_entropy_enthalpy') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = ctx.get('smoothed_cp')
        if data is None:
            return 0.0
        T = data['T']
        Cp = data['Cp']
        params = step.get('params', {})
        gold_S = params['gold_entropy']
        gold_H = params['gold_enthalpy']
        tol_rel = params['tol_relative']
        dead_extra = params['dead_zone_extra']
        # trapezoidal integration to 298.15 K, assuming (0,0) is already prepended
        def integrate(target, integrand_func):
            i = 0
            val = 0.0
            N = len(T)
            while i < N-1:
                if T[i+1] > target:
                    # interpolate to target
                    t_interp = target
                    frac = (t_interp - T[i]) / (T[i+1] - T[i])
                    cp_interp = Cp[i] + frac * (Cp[i+1] - Cp[i])
                    # integrate from T[i] to t_interp
                    dt = t_interp - T[i]
                    val += 0.5 * (integrand_func(T[i], Cp[i]) + integrand_func(t_interp, cp_interp)) * dt
                    break
                else:
                    dt = T[i+1] - T[i]
                    val += 0.5 * (integrand_func(T[i], Cp[i]) + integrand_func(T[i+1], Cp[i+1])) * dt
                    i += 1
            return val
        S = integrate(298.15, lambda t, cp: cp / t if t > 0 else 0.0)
        H = integrate(298.15, lambda t, cp: cp)
        err_S = abs(S - gold_S) / max(gold_S, 1.0)
        err_H = abs(H - gold_H) / max(gold_H, 1.0)
        def partial(err):
            if err <= tol_rel:
                return 1.0
            excess = err - tol_rel
            return max(0.0, 1.0 - excess / dead_extra)
        score_S = partial(err_S)
        score_H = partial(err_H)
        return (score_S + score_H) / 2.0


# === block: score_3 (check id='final_values_consistency') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = ctx.get('smoothed_cp')
        if data is None or artifact is None:
            return 0.0
        T = data['T']
        Cp = data['Cp']
        params = step.get('params', {})
        tol_rel = params.get('tol_relative', 0.005)
        # recompute S and H as above
        def integrate(target, integrand):
            val = 0.0
            i = 0
            N = len(T)
            while i < N-1:
                if T[i+1] > target:
                    if T[i+1] > target:
                        frac = (target - T[i]) / (T[i+1] - T[i])
                        cp_interp = Cp[i] + frac * (Cp[i+1] - Cp[i])
                        dt = target - T[i]
                        val += 0.5 * (integrand(T[i], Cp[i]) + integrand(target, cp_interp)) * dt
                    break
                dt = T[i+1] - T[i]
                val += 0.5 * (integrand(T[i], Cp[i]) + integrand(T[i+1], Cp[i+1])) * dt
                i += 1
            return val
        S_comp = integrate(298.15, lambda t, cp: cp / t if t > 0 else 0.0)
        H_comp = integrate(298.15, lambda t, cp: cp)
        # read artifact
        try:
            S_art = float(artifact.get('S_298_15_cal_per_K_mol', None))
            H_art = float(artifact.get('H_298_15_minus_H0_cal_per_mol', None))
        except (TypeError, ValueError):
            return 0.0
        if S_art is None or H_art is None:
            return 0.0
        err_S = abs(S_comp - S_art) / max(abs(S_comp), 1.0)
        err_H = abs(H_comp - H_art) / max(abs(H_comp), 1.0)
        return 1.0 if (err_S <= tol_rel and err_H <= tol_rel) else 0.0


# === block: score_4 (check id='thermodynamic_table_consistency') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = ctx.get('smoothed_cp')
        if data is None or artifact is None or not artifact:
            return 0.0
        T_cp = data['T']
        Cp_cp = data['Cp']
        params = step.get('params', {})
        check_temps = params.get('check_temps', [298.15])
        tol_rel = params.get('tol_relative', 0.05)
        # Build S and H interpolation from smoothed Cp
        def integrate_up_to(target):
            val = 0.0
            i = 0
            N = len(T_cp)
            while i < N-1:
                if T_cp[i+1] > target:
                    frac = (target - T_cp[i]) / (T_cp[i+1] - T_cp[i])
                    cp_interp = Cp_cp[i] + frac * (Cp_cp[i+1] - Cp_cp[i])
                    dt = target - T_cp[i]
                    val += 0.5 * (Cp_cp[i] + cp_interp) * dt
                    break
                dt = T_cp[i+1] - T_cp[i]
                val += 0.5 * (Cp_cp[i] + Cp_cp[i+1]) * dt
                i += 1
            return val
        # Precompute S and H for each T_cp point (not efficient but fine)
        # We'll just compute on demand
        def compute_S_H(target):
            S_val = 0.0
            H_val = 0.0
            i = 0
            N = len(T_cp)
            while i < N-1:
                t1 = T_cp[i]
                t2 = T_cp[i+1]
                if t2 > target:
                    if t2 > target:
                        # interp
                        frac = (target - t1) / (t2 - t1)
                        cp_interp = Cp_cp[i] + frac * (Cp_cp[i+1] - Cp_cp[i])
                        dt = target - t1
                        # integrate Cp/T for S
                        S_part = 0.5 * ( (Cp_cp[i] / t1 if t1>0 else 0.0) + (cp_interp / target if target>0 else 0.0) ) * dt
                        H_part = 0.5 * (Cp_cp[i] + cp_interp) * dt
                        S_val += S_part
                        H_val += H_part
                    break
                dt = t2 - t1
                S_part = 0.5 * ( (Cp_cp[i] / t1 if t1>0 else 0.0) + (Cp_cp[i+1] / t2 if t2>0 else 0.0) ) * dt
                H_part = 0.5 * (Cp_cp[i] + Cp_cp[i+1]) * dt
                S_val += S_part
                H_val += H_part
                i += 1
            return S_val, H_val
        # For each check temperature, find the corresponding row in artifact
        # artifact is list of dicts with T_K, S_cal_per_K_mol, H_minus_H0_cal_per_mol
        def find_row(target, rows):
            for r in rows:
                try:
                    t = float(r['T_K'])
                    if abs(t - target) < 0.5:  # only exact match or very close
                        return r
                except (KeyError, ValueError):
                    continue
            return None
        scores = []
        for temp in check_temps:
            row = find_row(temp, artifact)
            if row is None:
                scores.append(0.0)
                continue
            try:
                S_table = float(row['S_cal_per_K_mol'])
                H_table = float(row['H_minus_H0_cal_per_mol'])
            except (KeyError, ValueError):
                scores.append(0.0)
                continue
            S_comp, H_comp = compute_S_H(temp)
            if abs(S_comp) < 1e-6 or abs(H_comp) < 1e-6:
                scores.append(0.0)
                continue
            err_S = abs(S_table - S_comp) / max(abs(S_comp), 1.0)
            err_H = abs(H_table - H_comp) / max(abs(H_comp), 1.0)
            ok = 1.0 if err_S <= tol_rel and err_H <= tol_rel else 0.0
            scores.append(ok)
        if not scores:
            return 0.0
        return np.mean(scores)


_SCORERS = {
    'smoothed_cp_structure': score_0,
    'smoothed_cp_curve_check': score_1,
    'recompute_entropy_enthalpy': score_2,
    'final_values_consistency': score_3,
    'thermodynamic_table_consistency': score_4,
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
