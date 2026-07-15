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
    reference = {}
    steps = spec.get('steps', [])
    for s in steps:
        if s.get('id') == 'step01':
            reference['step01'] = s.get('reference_curve', [])
        elif s.get('id') == 'step02':
            reference['step02'] = s.get('reference_rows', [])
    return reference


# === block: score_0 (check id='step01') ===
def score_0(artifact, step, ctx):
    # score step01: time series comparison
    ref_curve = ctx['step01']
    if not ref_curve:
        return 0.0
    # sort reference by time
    ref_curve = sorted(ref_curve, key=lambda p: p[0])
    def ref_val(t):
        if t <= ref_curve[0][0]:
            return ref_curve[0][1]
        if t >= ref_curve[-1][0]:
            return ref_curve[-1][1]
        for i in range(len(ref_curve)-1):
            t0, v0 = ref_curve[i]
            t1, v1 = ref_curve[i+1]
            if t0 <= t <= t1:
                frac = (t - t0) / (t1 - t0)
                return v0 + frac * (v1 - v0)
        return ref_curve[-1][1]
    errors = []
    for row in artifact:
        try:
            t = float(row['time_hr'])
            v = float(row['precipitated_oxygen_atoms_per_precipitate'])
        except (ValueError, KeyError):
            continue
        if t < 0 or t > 12.0:
            continue
        v_ref = ref_val(t)
        if v_ref > 0:
            err = abs(v - v_ref) / v_ref
        else:
            err = abs(v - v_ref)
        errors.append(min(err, 1.0))
    if not errors:
        return 0.0
    avg_err = sum(errors) / len(errors)
    tol = step.get('tolerance', 0.20)
    score = max(0.0, 1.0 - avg_err / tol)
    return score


# === block: score_1 (check id='step02') ===
def score_1(artifact, step, ctx):
    # score step02: three rows of sticking coefficient results
    ref_rows = ctx['step02']
    if not ref_rows:
        return 0.0
    # build reference dict keyed by sticking_coefficient as string (but we'll compare as float)
    ref_dict = {}
    for r in ref_rows:
        try:
            alpha = float(r['sticking_coefficient'])
        except (KeyError, ValueError):
            continue
        ref_dict[alpha] = (float(r['denuded_zone_depth_um']), float(r['final_precipitate_radius_um']))
    if len(ref_dict) == 0:
        return 0.0
    tol = step.get('tolerance', 0.20)
    scores = []
    for row in artifact:
        try:
            alpha = float(row['sticking_coefficient'])
            depth = float(row['denuded_zone_depth_um'])
            radius = float(row['final_precipitate_radius_um'])
        except (KeyError, ValueError):
            continue
        if alpha not in ref_dict:
            continue
        ref_depth, ref_rad = ref_dict[alpha]
        err_depth = abs(depth - ref_depth) / (abs(ref_depth) + 1e-9)
        err_rad = abs(radius - ref_rad) / (abs(ref_rad) + 1e-9)
        score_depth = max(0.0, 1.0 - err_depth / tol)
        score_rad = max(0.0, 1.0 - err_rad / tol)
        scores.append((score_depth + score_rad) / 2.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step01': score_0,
    'step02': score_1,
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
