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


# === block: score_0 (check id='eq_lattice_param') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, str):
        return 0.0
    try:
        val = float(artifact.strip())
    except Exception:
        return 0.0
    target = step.get('target')
    tol = step.get('tolerance')
    if target is None or tol is None:
        return 0.0
    if abs(val - target) <= tol:
        return 1.0
    return 0.0


# === block: score_1 (check id='electronic_structure') ===
def score_1(artifact, step, ctx):
    import csv
    import io
    expected = step['expected_rows']
    tolerances = step['tolerances']
    reader = csv.DictReader(io.StringIO(artifact))
    rows = list(reader)
    score_sum = 0.0
    count = 0.0
    exp_by_p = {e['pressure']: e for e in expected}
    for p, exp_row in exp_by_p.items():
        found_row = None
        for r in rows:
            if abs(float(r['pressure (GPa)']) - float(p)) < 1e-6:
                found_row = r
                break
        if found_row is None:
            for col_name in ['N(EF) (states/Ryd atom)', 's_electrons', 'p_electrons', 'd_electrons']:
                count += 1
            continue
        for col_name in ['N(EF) (states/Ryd atom)', 's_electrons', 'p_electrons', 'd_electrons']:
            try:
                val = float(found_row[col_name])
            except (ValueError, KeyError):
                count += 1
                continue
            exp_val = exp_row[col_name]
            tol_info = tolerances[col_name]
            if 'abs' in tol_info:
                if abs(val - exp_val) <= tol_info['abs']:
                    score_sum += 1
            elif 'rel' in tol_info:
                if abs(exp_val) < 1e-12:
                    if abs(val) <= 1e-6:
                        score_sum += 1
                else:
                    if abs(val - exp_val) / abs(exp_val) <= tol_info['rel']:
                        score_sum += 1
            count += 1
    if count == 0:
        return 0.0
    return score_sum / count


# === block: score_2 (check id='tc_pressure') ===
def score_2(artifact, step, ctx):
    import csv
    import io
    expected = step['expected_rows']
    tol_rel = step['tolerance_rel']
    monotonic_req = step.get('monotonicity_required', False)
    reader = csv.DictReader(io.StringIO(artifact))
    rows = list(reader)
    exp_by_p = {e['pressure']: e for e in expected}
    tc_values = []
    point_scores = []
    for p, exp_row in exp_by_p.items():
        found_row = None
        for r in rows:
            if abs(float(r['Pressure (GPa)']) - float(p)) < 1e-6:
                found_row = r
                break
        if found_row is None:
            point_scores.append(0.0)
            tc_values.append(None)
            continue
        try:
            val = float(found_row['Tc (K)'])
        except:
            point_scores.append(0.0)
            tc_values.append(None)
            continue
        tc_values.append(val)
        exp_val = exp_row['Tc']
        if abs(exp_val) < 1e-12:
            if abs(val) <= 1e-6:
                point_scores.append(1.0)
            else:
                point_scores.append(0.0)
        else:
            rel_err = abs(val - exp_val) / abs(exp_val)
            if rel_err <= tol_rel:
                point_scores.append(1.0)
            else:
                point_scores.append(0.0)
    avg_point = sum(point_scores) / len(point_scores) if point_scores else 0.0
    score = avg_point
    if monotonic_req:
        monoton = 1.0
        for i in range(1, len(tc_values)):
            if tc_values[i-1] is not None and tc_values[i] is not None:
                if tc_values[i] < tc_values[i-1] - 1e-9:
                    monoton = 0.0
                    break
        score = 0.8 * avg_point + 0.2 * monoton
    return score


_SCORERS = {
    'eq_lattice_param': score_0,
    'electronic_structure': score_1,
    'tc_pressure': score_2,
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
