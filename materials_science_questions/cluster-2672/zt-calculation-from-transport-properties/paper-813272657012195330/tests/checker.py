import os
import json
import csv

# === author imports / helpers ===
class _fake_ndarray:
    def __init__(self, data):
        self._data = list(data)
    def __getitem__(self, idx):
        if isinstance(idx, list):
            return [self._data[i] for i in idx]
        return self._data[idx]
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)

class _FakeNumpy:
    @staticmethod
    def array(x):
        return _fake_ndarray(x)
    @staticmethod
    def min(x):
        return min(x)
    @staticmethod
    def max(x):
        return max(x)
    @staticmethod
    def argsort(x):
        return sorted(range(len(x)), key=lambda i: x[i])
    @staticmethod
    def interp(x, xp, fp):
        xp = list(xp)
        fp = list(fp)
        if x <= xp[0]:
            return fp[0]
        if x >= xp[-1]:
            return fp[-1]
        for i in range(len(xp)-1):
            if xp[i] <= x <= xp[i+1]:
                if xp[i+1] == xp[i]:
                    return fp[i]
                t = (x - xp[i]) / (xp[i+1] - xp[i])
                return fp[i] + t * (fp[i+1] - fp[i])
        return fp[-1]

np = _FakeNumpy()


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
    return {}


# === block: score_0 (check id='check_pf_ratio') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        import numpy as np
        data = artifact
        groups = {}
        for row in data:
            depth = row['impurity_band_depth'].strip()
            try:
                s = float(row['seebeck_muV_per_K'])
                pf = float(row['power_factor_arb_units'])
            except:
                continue
            if depth not in groups:
                groups[depth] = {'s': [], 'pf': []}
            groups[depth]['s'].append(s)
            groups[depth]['pf'].append(pf)
        for d in groups:
            idx = np.argsort(groups[d]['s'])
            groups[d]['s'] = np.array(groups[d]['s'])[idx]
            groups[d]['pf'] = np.array(groups[d]['pf'])[idx]
        target_s = 200.0
        def interp_pf(depth):
            if depth not in groups:
                return None
            s_arr = groups[depth]['s']
            pf_arr = groups[depth]['pf']
            if np.min(s_arr) > target_s or np.max(s_arr) < target_s:
                return None
            return np.interp(target_s, s_arr, pf_arr)
        pf_none = interp_pf('none')
        pf_0 = interp_pf('0')
        if pf_none is None or pf_0 is None or pf_none == 0:
            return 0.0
        ratio = pf_0 / pf_none
        if 0.65 <= ratio <= 0.75:
            return 1.0
        elif 0.60 <= ratio < 0.65 or 0.75 < ratio <= 0.80:
            return 0.5
        else:
            return 0.0


# === block: score_1 (check id='check_pf_ordering') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        import numpy as np
        data = artifact
        groups = {}
        for row in data:
            depth = row['impurity_band_depth'].strip()
            try:
                s = float(row['seebeck_muV_per_K'])
                pf = float(row['power_factor_arb_units'])
            except:
                continue
            if depth not in groups:
                groups[depth] = {'s': [], 'pf': []}
            groups[depth]['s'].append(s)
            groups[depth]['pf'].append(pf)
        for d in groups:
            idx = np.argsort(groups[d]['s'])
            groups[d]['s'] = np.array(groups[d]['s'])[idx]
            groups[d]['pf'] = np.array(groups[d]['pf'])[idx]
        target_s = 200.0
        pf_vals = {}
        depths = ['none', '0', 'kT', '4kT']
        for d in depths:
            if d in groups:
                s_arr = groups[d]['s']
                pf_arr = groups[d]['pf']
                if np.min(s_arr) <= target_s <= np.max(s_arr):
                    pf_vals[d] = np.interp(target_s, s_arr, pf_arr)
                else:
                    pf_vals[d] = None
            else:
                pf_vals[d] = None
        if any(pf_vals[d] is None for d in depths):
            return 0.0
        c1 = pf_vals['4kT'] > pf_vals['none']
        c2 = pf_vals['none'] > pf_vals['kT']
        c3 = pf_vals['kT'] > pf_vals['0']
        count = sum([c1, c2, c3])
        return count / 3.0


_SCORERS = {
    'check_pf_ratio': score_0,
    'check_pf_ordering': score_1,
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
