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


# === block: score_0 (check id='step_1_lattice') ===
def score_0(artifact, step, ctx):
    ref = step['reference_points']
    tol = step.get('tolerance_absolute', 0.05)
    points = {}
    for row in artifact:
        try:
            x_val = float(row['x'])
            lc_val = float(row['lattice_constant'])
            points[x_val] = lc_val
        except:
            pass
    total = len(ref)
    if total == 0:
        return 0.0
    within = 0
    for x_str, expected in ref.items():
        x = float(x_str)
        if x in points and abs(points[x] - expected) <= tol:
            within += 1
    frac = within / total
    sorted_x = sorted(points.keys())
    monotonic = True
    if len(sorted_x) > 1:
        for i in range(len(sorted_x)-1):
            if points[sorted_x[i+1]] <= points[sorted_x[i]]:
                monotonic = False
                break
    else:
        monotonic = False
    score = frac * 0.6 + (1.0 if monotonic else 0.0) * 0.4
    return score


# === block: score_1 (check id='step_2_phonon') ===
def score_1(artifact, step, ctx):
    ref = step['reference']
    tol = step.get('tolerance_absolute', 20.0)
    check_trend = step.get('check_trend', True)
    data = {}
    for row in artifact:
        try:
            x_val = float(row['x'])
            freq = float(row['highest_optical_frequency'])
            data[x_val] = freq
        except:
            pass
    if 0.0 not in data or 1.0 not in data:
        return 0.0
    within0 = 1 if abs(data[0.0] - ref['0']) <= tol else 0
    within1 = 1 if abs(data[1.0] - ref['1']) <= tol else 0
    frac_within = (within0 + within1) / 2.0
    trend_ok = data[0.0] > data[1.0]
    score = frac_within * 0.7 + (1.0 if trend_ok else 0.0) * 0.3
    return score


# === block: score_2 (check id='step_3_heat') ===
def score_2(artifact, step, ctx):
    ref = step['reference']
    points = []
    for row in artifact:
        try:
            t = float(row['T'])
            cv = float(row['C_v'])
            points.append((t, cv))
        except:
            pass
    if not points:
        return 0.0
    score_total = 0.0
    for ref_pt in ref:
        T_target = ref_pt['T']
        C_target = ref_pt['C_v']
        tol = ref_pt.get('tolerance', 5.0)
        cv_agent = None
        for t, cv in points:
            if abs(t - T_target) < 1e-6:
                cv_agent = cv
                break
        if cv_agent is not None and abs(cv_agent - C_target) <= tol:
            score_total += 1.0
    return score_total / len(ref) if ref else 0.0


_SCORERS = {
    'step_1_lattice': score_0,
    'step_2_phonon': score_1,
    'step_3_heat': score_2,
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
