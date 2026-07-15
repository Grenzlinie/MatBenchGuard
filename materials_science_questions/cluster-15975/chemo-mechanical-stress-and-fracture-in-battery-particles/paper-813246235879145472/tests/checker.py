import os
import json
import csv


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


# === block: score_0 (check id='data_quality') ===
def score_0(artifact, step, ctx):
    expected = step.get("expected_conditions", [])
    if not expected:
        return 0.0
    header = artifact[0] if artifact else {}
    if set(["condition_id","time_h","damage"]) - set(header.keys()):
        return 0.0
    cond_data = {}
    for row in artifact:
        cid = row["condition_id"]
        cond_data.setdefault(cid, []).append((float(row["time_h"]), float(row["damage"])))
    present = set(cond_data.keys())
    expected_ids = [c["id"] for c in expected]
    completeness = len(present & set(expected_ids)) / float(len(expected_ids)) if expected_ids else 0.0
    eps = step.get("monotonic_epsilon", 1e-9)
    monotonic_count = 0
    for cid in expected_ids:
        if cid in present:
            vals = sorted(cond_data[cid], key=lambda x: x[0])
            damage_vals = [v[1] for v in vals]
            ok = all(damage_vals[i] >= damage_vals[i-1] - eps for i in range(1, len(damage_vals)))
            if ok:
                monotonic_count += 1
    monotonicity = monotonic_count / float(len(expected_ids)) if expected_ids else 0.0
    return 0.5 * completeness + 0.5 * monotonicity


# === block: score_1 (check id='exponent_accuracy') ===
def score_1(artifact, step, ctx):
    import math

    rows = artifact
    gold = step.get("gold", {})
    tol_abs = step.get("tolerance_abs", 0.2)
    tol_rel = step.get("tolerance_rel", 0.2)
    fit_th = step.get("fit_time_threshold_h", 6.0)
    sweep_params = step.get("sweep_params", {})
    cond_mapping = step.get("conditions_mapping", {})

    cond_dict = {}
    for r in rows:
        cid = r["condition_id"]
        t = float(r["time_h"])
        d = float(r["damage"])
        cond_dict.setdefault(cid, []).append((t, d))

    def linreg(x, y):
        n = len(x)
        if n < 2:
            return None
        sx = sum(x)
        sy = sum(y)
        sxy = sum(xi*yi for xi,yi in zip(x,y))
        sxx = sum(xi*xi for xi in x)
        denom = n*sxx - sx*sx
        if denom == 0:
            return None
        slope = (n*sxy - sx*sy) / denom
        return slope

    b_vals = {}
    for cid, data in cond_dict.items():
        filt = [(t,d) for t,d in data if t >= fit_th]
        if len(filt) < 2:
            continue
        t_use = [d[0] for d in filt]
        d_use = [d[1] for d in filt]
        positive = [(ti,di) for ti,di in zip(t_use, d_use) if di > 0]
        if len(positive) < 2:
            continue
        t_pos = [p[0] for p in positive]
        logd = [math.log(p[1]) for p in positive]
        b = linreg(t_pos, logd)
        if b is not None:
            b_vals[cid] = b

    def fit_exponent(sweep_name, param_vals):
        cids = cond_mapping.get(sweep_name, [])
        b_list = [b_vals[cid] for cid in cids if cid in b_vals]
        if len(b_list) != len(cids):
            return None
        logx = [math.log(v) for v in param_vals]
        logy = [math.log(v) for v in b_list]
        expo = linreg(logx, logy)
        return expo

    m = fit_exponent("duty_sweep", sweep_params["duty_sweep"]["values"])
    p = fit_exponent("freq_sweep", sweep_params["freq_sweep"]["values"])
    n = fit_exponent("j_sweep", sweep_params["j_sweep"]["values"])

    if None in (m, p, n):
        return 0.0

    passed = 0
    for comp, gold_val in [(m, gold["m"]), (p, gold["p"]), (n, gold["n"])]:
        allowed = max(tol_abs, tol_rel * abs(gold_val))
        if abs(comp - gold_val) <= allowed:
            passed += 1
    return passed / 3.0


# === block: score_2 (check id='reported_exponents_check') ===
def score_2(artifact, step, ctx):
    import math
    gold = step.get("gold", {})
    tol_abs = step.get("tolerance_abs", 0.2)
    tol_rel = step.get("tolerance_rel", 0.2)
    m = artifact.get("m")
    p = artifact.get("p")
    n = artifact.get("n")
    if None in [m,p,n]:
        return 0.0
    passed = 0
    for comp, gold_val in [(m, gold["m"]), (p, gold["p"]), (n, gold["n"])]:
        allowed = max(tol_abs, tol_rel * abs(gold_val))
        if abs(comp - gold_val) <= allowed:
            passed += 1
    return passed / 3.0


_SCORERS = {
    'data_quality': score_0,
    'exponent_accuracy': score_1,
    'reported_exponents_check': score_2,
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
