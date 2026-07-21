import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='polarization_profile') ===
def score_0(artifact, step, ctx):
    checks = step.get('checks', [])
    total_weight = sum(ch['weight'] for ch in checks)
    score = 0.0
    for ch in checks:
        params = ch.get('params', {})
        rc_list = params.get('rc_list', [5,10,15,20])
        if ch['id'] == 'p3_far_field':
            x_thresh = params['x_thresh']
            target = params['target']
            tol = params['tolerance']
            pass_count = 0
            for rc in rc_list:
                rows = [r for r in artifact if float(r['rc']) == rc and abs(float(r['x'])) >= x_thresh]
                if not rows:
                    continue
                mean_abs = sum(abs(float(r['P3'])) for r in rows) / len(rows)
                if abs(mean_abs - target) <= tol:
                    pass_count += 1
            ch_score = pass_count / len(rc_list) if rc_list else 1.0
        elif ch['id'] == 'p3_center_zero':
            max_abs = params['max_abs']
            pass_count = 0
            for rc in rc_list:
                rows_rc = [r for r in artifact if float(r['rc']) == rc]
                if not rows_rc:
                    continue
                closest = min(rows_rc, key=lambda r: abs(float(r['x'])))
                if abs(float(closest['P3'])) <= max_abs:
                    pass_count += 1
            ch_score = pass_count / len(rc_list) if rc_list else 1.0
        else:
            ch_score = 1.0
        score += ch_score * ch['weight']
    return score / total_weight if total_weight > 0 else 0.0


# === block: score_1 (check id='refractive_index_profile') ===
def score_1(artifact, step, ctx):
    checks = step.get('checks', [])
    total_weight = sum(ch['weight'] for ch in checks)
    score = 0.0
    for ch in checks:
        params = ch.get('params', {})
        rc_list = params.get('rc_list', [5,10,15,20])
        if ch['id'] == 'n_far_field':
            x_thresh = params['x_thresh']
            targets = params['targets']
            tol = params['tolerance']
            pass_count = 0
            total_checks = 0
            for rc in rc_list:
                rows = [r for r in artifact if float(r['rc']) == rc and abs(float(r['x'])) >= x_thresh]
                if not rows:
                    continue
                avg = {}
                for comp in ['n1','n2','n3']:
                    vals = [float(r[comp]) for r in rows]
                    avg[comp] = sum(vals) / len(vals) if vals else None
                for comp in ['n1','n2','n3']:
                    if avg[comp] is not None and comp in targets:
                        total_checks += 1
                        if abs(avg[comp] - targets[comp]) <= tol:
                            pass_count += 1
            ch_score = pass_count / total_checks if total_checks else 0.0
        elif ch['id'] == 'n_peak':
            min_excess = params['min_excess']
            far_avg = params['far_field_avg']
            pass_count = 0
            total_checks = 0
            for rc in rc_list:
                rows_rc = [r for r in artifact if float(r['rc']) == rc]
                if not rows_rc:
                    continue
                # find center row closest to x=0
                center_row = min(rows_rc, key=lambda r: abs(float(r['x'])))
                for comp in ['n2','n3']:
                    if comp in far_avg:
                        total_checks += 1
                        if float(center_row[comp]) - far_avg[comp] >= min_excess:
                            pass_count += 1
            ch_score = pass_count / total_checks if total_checks else 0.0
        else:
            ch_score = 1.0
        score += ch_score * ch['weight']
    return score / total_weight if total_weight > 0 else 0.0


_SCORERS = {
    'polarization_profile': score_0,
    'refractive_index_profile': score_1,
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
