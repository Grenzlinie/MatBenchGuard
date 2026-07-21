import os
import json
import csv

# === author imports / helpers ===
import math

class _BoolList:
    def __init__(self, arr):
        self.arr = arr
    def any(self):
        return any(self.arr)

class _NumpyShim:
    @staticmethod
    def log10(values):
        return [math.log10(v) for v in values]

    @staticmethod
    def polyfit(x, y, deg):
        if deg != 1:
            raise NotImplementedError
        n = len(x)
        if n < 2:
            raise _LinAlgError("not enough data points")
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_x2 = sum(xi * xi for xi in x)
        denom = n * sum_x2 - sum_x * sum_x
        if denom == 0:
            raise _LinAlgError("singular matrix")
        slope = (n * sum_xy - sum_x * sum_y) / denom
        intercept = (sum_y * sum_x2 - sum_x * sum_xy) / denom
        return [slope, intercept]

    @staticmethod
    def isnan(values):
        if isinstance(values, (list, tuple)):
            return _BoolList([math.isnan(v) for v in values])
        return _BoolList([math.isnan(values)])

    @staticmethod
    def isinf(values):
        if isinstance(values, (list, tuple)):
            return _BoolList([math.isinf(v) for v in values])
        return _BoolList([math.isinf(values)])

class _LinAlgError(Exception):
    pass

np = _NumpyShim()
np.linalg = type('linalg', (), {'LinAlgError': _LinAlgError})()


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


# === block: score_0 (check id='cluster_size_scaling') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    if len(rows) < 3:
        return 0.0
    pe_gammas = []
    mean_sizes = []
    for r in rows:
        try:
            pe = float(r['Pe'])
            gamma = float(r['gamma'])
            sz = float(r['mean_cluster_size'])
        except (ValueError, KeyError):
            return 0.0
        if pe > 0 and gamma > 0 and sz > 0:
            pe_gammas.append(pe / gamma)
            mean_sizes.append(sz)
    if len(pe_gammas) < 3:
        return 0.0
    x = np.log10(pe_gammas)
    y = np.log10(mean_sizes)
    # linear regression y = slope * x + intercept
    if np.isnan(x).any() or np.isnan(y).any() or np.isinf(x).any() or np.isinf(y).any():
        return 0.0
    try:
        slope, _ = np.polyfit(x, y, 1)
    except np.linalg.LinAlgError:
        return 0.0
    target = step.get('target', -1.0)
    tol = step.get('tolerance', 0.3)
    dev = abs(slope - target)
    if dev <= tol:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (dev - tol) / (2 * tol))
    return float(score)


# === block: score_1 (check id='polarity_autocorrelation_scaling') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if len(rows) < 3:
        return 0.0
    Ns = []
    tau_ps = []
    for r in rows:
        try:
            n = float(r['N'])
            tp = float(r['tau_p'])
        except (ValueError, KeyError):
            return 0.0
        if n > 0 and tp > 0:
            Ns.append(n)
            tau_ps.append(tp)
    if len(Ns) < 3:
        return 0.0
    x = np.log10(Ns)
    y = np.log10(tau_ps)
    if np.isnan(x).any() or np.isnan(y).any() or np.isinf(x).any() or np.isinf(y).any():
        return 0.0
    try:
        slope, _ = np.polyfit(x, y, 1)
    except np.linalg.LinAlgError:
        return 0.0
    target = step.get('target', 2.0)
    tol = step.get('tolerance', 0.5)
    dev = abs(slope - target)
    if dev <= tol:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (dev - tol) / (2 * tol))
    return float(score)


# === block: score_2 (check id='phase_diagram_simulation') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    # group by ratio, check re-entrant pattern for high ratios
    try:
        data = []
        for r in rows:
            ratio = float(r['alpha_beta_ratio'])
            pe_g = float(r['Pe_gamma'])
            reg = r['regime'].strip().lower()
            data.append((ratio, pe_g, reg))
    except (ValueError, KeyError):
        return 0.0
    # find unique ratios
    ratios = sorted(set(r[0] for r in data))
    if not ratios:
        return 0.0
    max_ratio = max(ratios)
    # check all ratios >= 2 or just max? we'll check all ratios >= 2
    valid_ratios = [r for r in ratios if r >= 2.0]
    if not valid_ratios:
        return 0.0
    def has_reentrant(rows_sorted):
        # rows_sorted: list of (pe_g, reg) sorted by pe_g
        # define desired state machine: 0=clustered, 1=microphase, 2=dispersed, 3=clustered (re-entrant)
        # simplified: find first clustered, then microphase, then dispersed, then clustered again.
        state = 0
        for _, reg in rows_sorted:
            if state == 0 and reg == 'clustered':
                state = 1  # saw first clustered, now looking for microphase
            elif state == 1 and reg == 'microphase':
                state = 2  # saw microphase, now looking for dispersed
            elif state == 2 and reg == 'dispersed':
                state = 3  # saw dispersed, now looking for re-entrant clustered
            elif state == 3 and reg == 'clustered':
                return True
        return False
    passed = 0
    for ratio in valid_ratios:
        subset = [(pe_g, reg) for r, pe_g, reg in data if r == ratio]
        subset.sort(key=lambda x: x[0])  # sort by Pe_gamma
        if has_reentrant(subset):
            passed += 1
    score = passed / len(valid_ratios)
    return float(score)


_SCORERS = {
    'cluster_size_scaling': score_0,
    'polarity_autocorrelation_scaling': score_1,
    'phase_diagram_simulation': score_2,
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
