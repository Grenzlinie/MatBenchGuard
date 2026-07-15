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


# === block: score_0 (check id='metrics_check') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    ta10 = artifact.get('Ta10', {})
    ta35 = artifact.get('Ta35', {})
    # Validate required fields exist
    required_keys = ['mdot_kg_per_day', 'eta_still_pct', 'eta_system_pct', 'P_output_W']
    if any(key not in ta10 for key in required_keys) or any(key not in ta35 for key in required_keys):
        return 0.0

    ta10_ref = step['ta10_ref']
    ta35_ref = step['ta35_ref']
    tol_mdot_abs = float(step['tolerances']['mdot_abs_tol'])
    tol_rel_other = float(step['tolerances']['other_rel_tol'])

    def metric_score_abs(val, ref, abs_tol):
        if ref == 0:
            return 1.0 if abs(val) <= abs_tol else 0.0
        dev = abs(val - ref)
        if dev <= abs_tol:
            return 1.0
        return max(0.0, 1.0 - (dev - abs_tol) / abs_tol)

    def metric_score_rel(val, ref, rel_tol):
        if ref == 0:
            return 1.0 if val == 0 else 0.0
        rel_err = abs(val - ref) / abs(ref)
        if rel_err <= rel_tol:
            return 1.0
        return max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol)

    def compute_avg(ta_data, ta_ref):
        scores = []
        for key in required_keys:
            val = ta_data[key]
            ref_val = ta_ref[key]
            if key == 'mdot_kg_per_day':
                scores.append(metric_score_abs(val, ref_val, tol_mdot_abs))
            else:
                scores.append(metric_score_rel(val, ref_val, tol_rel_other))
        return sum(scores) / len(scores) if scores else 0.0

    avg_ta35 = compute_avg(ta35, ta35_ref)
    avg_ta10 = compute_avg(ta10, ta10_ref)

    # trend check: relative increase in distillation from Ta10 to Ta35
    mdot10 = ta10['mdot_kg_per_day']
    mdot35 = ta35['mdot_kg_per_day']
    trend_score = 0.0
    if mdot10 > 0:
        increase_pct = (mdot35 - mdot10) / mdot10 * 100.0
        lo, hi = step['trend']['range_pct']
        if lo <= increase_pct <= hi:
            trend_score = 1.0

    # weighted combination
    w35 = step['sub_weights']['ta35_metrics']
    w10 = step['sub_weights']['ta10_metrics']
    wt = step['sub_weights']['trend']
    total = w35 * avg_ta35 + w10 * avg_ta10 + wt * trend_score
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'metrics_check': score_0,
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
