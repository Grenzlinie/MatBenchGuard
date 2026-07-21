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
    steps = spec.get('steps', [])
    eol_step = next((s for s in steps if s['id'] == 'step_ilal_stress_eol'), None)
    trend_step = next((s for s in steps if s['id'] == 'step_ilal_stress_trend'), None)
    cases = eol_step.get('cases', []) if eol_step else []
    trend = {}
    if trend_step:
        trend = {
            'plate': trend_step['trend_plate'],
            'location': trend_step['trend_location'],
            'fd_low': trend_step['fd_low'],
            'fd_high': trend_step['fd_high']
        }
    return {'cases': cases, 'trend': trend}


# === block: score_0 (check id='step_ilal_stress_eol') ===
def score_0(artifact, step, ctx):
    cases = ctx['cases']
    if not artifact or not cases:
        return 0.0
    # build index: (plate, location) -> rows
    rows_by_key = {}
    for row in artifact:
        if not all(k in row for k in ('plate', 'location', 'fission_density_1e21', 'radial_stress_MPa')):
            continue
        key = (row['plate'].strip(), row['location'].strip())
        rows_by_key.setdefault(key, []).append(row)
    scores = []
    for case in cases:
        key = (case['plate'], case['location'])
        cand = rows_by_key.get(key, [])
        if not cand:
            scores.append(0.0)
            continue
        # choose row with maximum fission_density_1e21
        best_row = max(cand, key=lambda r: float(r['fission_density_1e21']))
        try:
            stress = float(best_row['radial_stress_MPa'])
        except (ValueError, TypeError):
            scores.append(0.0)
            continue
        gold = float(case['stress_gold'])
        tol_rel = float(case.get('tolerance_rel', 0.15))
        tol_abs = float(case.get('tolerance_abs', 10.0))
        max_tol = max(tol_rel * abs(gold), tol_abs)
        error = abs(stress - gold)
        scores.append(1.0 if error <= max_tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='step_ilal_stress_trend') ===
def score_1(artifact, step, ctx):
    trend = ctx['trend']
    if not artifact or not trend:
        return 0.0
    plate = trend['plate']
    location = trend['location']
    lo = float(trend['fd_low'])
    hi = float(trend['fd_high'])
    found_transition = False
    for row in artifact:
        if not all(k in row for k in ('plate', 'location', 'fission_density_1e21', 'radial_stress_MPa')):
            continue
        if row['plate'].strip() != plate or row['location'].strip() != location:
            continue
        try:
            fd = float(row['fission_density_1e21'])
            stress = float(row['radial_stress_MPa'])
        except (ValueError, TypeError):
            continue
        if lo <= fd <= hi and stress >= 0.0:
            found_transition = True
            break
    return 1.0 if found_transition else 0.0


_SCORERS = {
    'step_ilal_stress_eol': score_0,
    'step_ilal_stress_trend': score_1,
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
