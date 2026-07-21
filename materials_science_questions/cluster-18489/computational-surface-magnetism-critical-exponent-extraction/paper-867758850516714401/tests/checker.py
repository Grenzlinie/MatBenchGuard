import os
import json
import csv

# === author imports / helpers ===
import math, statistics

try:
    import numpy as np
except ImportError:
    class _NPFallback:
        @staticmethod
        def array(lst, dtype=None):
            return list(lst)
        @staticmethod
        def polyfit(x, y, deg):
            if deg != 1:
                raise ValueError("only deg=1 supported")
            n = len(x)
            sum_x = sum(x)
            sum_y = sum(y)
            sum_xy = sum(xi*yi for xi,yi in zip(x,y))
            sum_x2 = sum(xi*xi for xi in x)
            det = n*sum_x2 - sum_x*sum_x
            if det == 0:
                return [0.0, sum_y/n]
            slope = (n*sum_xy - sum_x*sum_y)/det
            intercept = (sum_y - slope*sum_x)/n
            return [slope, intercept]
        @staticmethod
        def mean(lst):
            if not lst:
                return 0.0
            return sum(lst)/len(lst)
        class errstate:
            def __init__(self, divide='ignore'):
                pass
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
    np = _NPFallback()


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


# === block: score_0 (check id='extrapolation_and_trends') ===
def score_0(artifact, step, ctx):
    import math, statistics

    config = step.get('config', {})
    target = config['target_intercept']
    tol_typ = config['tolerance_typ']
    tol_avg = config['tolerance_avg']
    required_rhos = config['required_rhos']
    min_rows = config.get('min_rows', 3)

    rows = artifact
    rhos_set = set()
    data = {}
    for row in rows:
        r = int(row['rho'])
        rhos_set.add(r)
        l = int(row['l'])
        ratio_typ = float(row['ratio_typ'])
        ratio_avg = float(row['ratio_avg'])
        if r not in data:
            data[r] = {'ls': [], 'ratio_typ': [], 'ratio_avg': []}
        data[r]['ls'].append(l)
        data[r]['ratio_typ'].append(ratio_typ)
        data[r]['ratio_avg'].append(ratio_avg)

    for rr in required_rhos:
        if rr not in rhos_set:
            return 0.0

    def linear_fit(xs, ys):
        n = len(xs)
        if n < 2:
            return 0.0, statistics.mean(ys) if n > 0 else 0.0
        mean_x = sum(xs) / n
        mean_y = sum(ys) / n
        cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
        var = sum((x - mean_x) ** 2 for x in xs)
        if var == 0:
            return 0.0, mean_y
        slope = cov / var
        intercept = mean_y - slope * mean_x
        return slope, intercept

    def fit_and_score_typ(rho):
        d = data[rho]
        if len(d['ls']) < min_rows:
            return 0.0
        lvals = d['ls']
        ratio_typ = d['ratio_typ']
        x = [1.0 / l for l in lvals]
        slope, intercept = linear_fit(x, ratio_typ)
        error = abs(intercept - target)
        if error <= tol_typ:
            return 1.0
        decay = (error - tol_typ) / 0.05
        return max(0.0, 1.0 - decay)

    def fit_and_score_avg(rho):
        d = data[rho]
        if len(d['ls']) < min_rows:
            return 0.0
        lvals = d['ls']
        ratio_avg = d['ratio_avg']
        x = [1.0 / math.log(l) for l in lvals]
        slope, intercept = linear_fit(x, ratio_avg)
        error = abs(intercept - target)
        if error <= tol_avg:
            return 1.0
        decay = (error - tol_avg) / 0.2
        return max(0.0, 1.0 - decay)

    struct_ok = 0
    total_comp = 0
    for row in rows:
        ratio_typ = float(row['ratio_typ'])
        ratio_avg = float(row['ratio_avg'])
        total_comp += 1
        if ratio_avg > ratio_typ:
            struct_ok += 1
    struct_score = struct_ok / total_comp if total_comp else 0.0

    typ_scores = []
    avg_scores = []
    for rr in required_rhos:
        typ_scores.append(fit_and_score_typ(rr))
        avg_scores.append(fit_and_score_avg(rr))

    avg_typ_score = statistics.mean(typ_scores) if typ_scores else 0.0
    avg_avg_score = statistics.mean(avg_scores) if avg_scores else 0.0

    total = 0.4 * avg_typ_score + 0.4 * avg_avg_score + 0.2 * struct_score
    return float(total)


_SCORERS = {
    'extrapolation_and_trends': score_0,
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
