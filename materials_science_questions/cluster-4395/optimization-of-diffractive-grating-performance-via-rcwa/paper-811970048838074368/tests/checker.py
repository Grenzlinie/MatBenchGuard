import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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
    return {'output_dir': '/app/outputs'}


# === block: score_0 (check id='amplitude_ratio_map') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    zeroth_max = float(step.get('config',{}).get('zeroth_max',0.2))
    h_min, h_max = step.get('config',{}).get('h_min',55), step.get('config',{}).get('h_max',75)
    alpha_min, alpha_max = step.get('config',{}).get('alpha_min',20), step.get('config',{}).get('alpha_max',30)

    valid_rows = [r for r in rows if float(r.get('zeroth_amplitude',1e9)) < zeroth_max]
    if not valid_rows:
        return 0.0

    max_ratio = -1.0
    best_row = None
    for r in valid_rows:
        ratio = float(r.get('ratio',-1))
        if ratio > max_ratio:
            max_ratio = ratio
            best_row = r
    if best_row is None:
        return 0.0

    best_h = float(best_row['h_nm'])
    best_alpha = float(best_row['alpha_deg'])
    h_ok = (h_min <= best_h <= h_max)
    a_ok = (alpha_min <= best_alpha <= alpha_max)
    if h_ok and a_ok:
        return 1.0
    elif h_ok or a_ok:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='optimal_parameters') ===
def score_1(artifact, step, ctx):
    json_data = artifact  # dict
    map_file = os.path.join(ctx['output_dir'], 'amplitude_ratio_map.csv')
    if not os.path.exists(map_file):
        return 0.0
    rows = []
    with open(map_file, newline='') as f:
        for r in csv.DictReader(f):
            rows.append(r)

    zeroth_max = float(step.get('config',{}).get('zeroth_max',0.2))
    h_tol = float(step.get('config',{}).get('h_tol',5))
    alpha_tol = float(step.get('config',{}).get('alpha_tol',2))
    period_tol = float(step.get('config',{}).get('period_tol',0.1))

    valid_rows = [r for r in rows if float(r.get('zeroth_amplitude',1e9)) < zeroth_max]
    if not valid_rows:
        return 0.0

    max_ratio = -1.0
    best_row = None
    for r in valid_rows:
        ratio = float(r.get('ratio',-1))
        if ratio > max_ratio:
            max_ratio = ratio
            best_row = r
    if best_row is None:
        return 0.0

    rec_h = float(best_row['h_nm'])
    rec_alpha = float(best_row['alpha_deg'])

    rep_h = float(json_data.get('optimal_h_nm', -999))
    rep_alpha = float(json_data.get('optimal_alpha_deg', -999))
    rep_period = float(json_data.get('period_nm', -999))

    period_ok = abs(rep_period - 600) <= period_tol
    h_match = abs(rep_h - rec_h) <= h_tol
    alpha_match = abs(rep_alpha - rec_alpha) <= alpha_tol

    if h_match and alpha_match and period_ok:
        return 1.0
    elif h_match and alpha_match:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'amplitude_ratio_map': score_0,
    'optimal_parameters': score_1,
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
