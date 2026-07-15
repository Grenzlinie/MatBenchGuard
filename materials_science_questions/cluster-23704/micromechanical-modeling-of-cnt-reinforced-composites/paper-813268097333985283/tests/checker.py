import os
import json
import csv

# === author imports / helpers ===
import csv, math, os

def read_csv(path):
    rows = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


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


# === block: score_0 (check id='step_06') ===
def score_0(artifact, step, ctx):
    artifact = read_csv(os.path.join('/app/outputs', 'shear_properties.csv'))
    if not artifact or len(artifact) < 3:
        return 0.0
    try:
        rho = [float(r['rho']) for r in artifact]
        G = [float(r['G']) for r in artifact]
        tau_yield = [float(r['tau_yield']) for r in artifact]
        tau_sliding = [float(r['tau_sliding']) for r in artifact]
    except (KeyError, ValueError):
        return 0.0
    ref = step.get('ref_slopes', {})
    tol_rel = step.get('tolerance_relative', 0.25)
    def slope_zero_intercept(x, y):
        xy = sum(xi*yi for xi,yi in zip(x,y))
        xx = sum(xi*xi for xi in x)
        if xx == 0:
            return None
        return xy/xx
    def score_slope(computed, target):
        if computed is None:
            return 0.0
        rel_err = abs(computed - target) / target
        return max(0.0, 1.0 - rel_err / tol_rel)
    scores = []
    for prop, target in ref.items():
        y = {'G': G, 'tau_yield': tau_yield, 'tau_sliding': tau_sliding}[prop]
        comp = slope_zero_intercept(rho, y)
        scores.append(score_slope(comp, target))
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_07') ===
def score_1(artifact, step, ctx):
    artifact = read_csv(os.path.join('/app/outputs', 'tensile_properties.csv'))
    if not artifact or len(artifact) < 3:
        return 0.0
    try:
        uts = [float(r['UTS_GPa']) for r in artifact]
        c = [float(r['largest_hole_size_nm']) for r in artifact]
    except (KeyError, ValueError):
        return 0.0
    pairs = [(ci, ui) for ci, ui in zip(c, uts) if ci > 0 and ui > 0]
    if len(pairs) < 3:
        return 0.0
    log_c = [math.log(ci) for ci, ui in pairs]
    log_uts = [math.log(ui) for ci, ui in pairs]
    n = len(log_c)
    mean_x = sum(log_c)/n
    mean_y = sum(log_uts)/n
    cov = sum((x - mean_x)*(y - mean_y) for x,y in zip(log_c, log_uts))
    var = sum((x - mean_x)**2 for x in log_c)
    if var == 0:
        return 0.0
    b = cov / var
    m = -b
    ref_exp = step.get('ref_exponent', 0.35)
    tol_exp = step.get('tolerance_exponent', 0.1)
    score = max(0.0, 1.0 - abs(m - ref_exp) / tol_exp)
    return score


_SCORERS = {
    'step_06': score_0,
    'step_07': score_1,
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
