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


# === block: score_0 (check id='reaction_energies_curvatures') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get('gold_rows', [])
    tolerances = step.get('tolerances', {})
    total_checks = 0
    passed = 0
    for gold in gold_rows:
        spec = gold['species']
        row = None
        for r in artifact:
            if r.get('species', '').strip().lower() == spec.lower():
                row = r
                break
        if row is None:
            num_fields = len(gold) - 1
            total_checks += num_fields
            continue
        for field in gold:
            if field == 'species':
                continue
            if field not in row:
                total_checks += 1
                continue
            try:
                agent_val = float(row[field])
                gold_val = float(gold[field])
            except (ValueError, TypeError):
                total_checks += 1
                continue
            tol = tolerances.get(field, 0.0)
            if abs(agent_val - gold_val) <= tol:
                passed += 1
            total_checks += 1
    score = passed / max(total_checks, 1)
    return score


# === block: score_1 (check id='band_gaps') ===
def score_1(artifact, step, ctx):
    gold_rows = step.get('gold_rows', [])
    tolerances = step.get('tolerances', {})
    total_checks = 0
    passed = 0
    for gold in gold_rows:
        spec = gold['species']
        hyd = gold.get('hydrogenated', '').strip().lower()
        row = None
        for r in artifact:
            r_spec = r.get('species', '').strip().lower()
            r_hyd = r.get('hydrogenated', '').strip().lower()
            if r_spec == spec.lower() and r_hyd == hyd:
                row = r
                break
        if row is None:
            total_checks += 1
            continue
        for field in gold:
            if field in ('species', 'hydrogenated'):
                continue
            if field not in row:
                total_checks += 1
                continue
            try:
                agent_val = float(row[field])
                gold_val = float(gold[field])
            except (ValueError, TypeError):
                total_checks += 1
                continue
            tol = tolerances.get(field, 0.0)
            if abs(agent_val - gold_val) <= tol:
                passed += 1
            total_checks += 1
    score = passed / max(total_checks, 1)
    return score


# === block: score_2 (check id='curvature_energy_linear_fit') ===
def score_2(artifact, step, ctx):
    checks = step.get('checks', {})
    score_parts = []
    slope = None
    intercept = None
    r_squared = None
    try:
        slope = float(artifact.get('slope'))
    except (ValueError, TypeError):
        pass
    try:
        intercept = float(artifact.get('intercept'))
    except (ValueError, TypeError):
        pass
    try:
        r_squared = float(artifact.get('r_squared'))
    except (ValueError, TypeError):
        pass

    # 1. slope negative
    if slope is not None and slope < 0:
        score_parts.append(1.0)
    else:
        score_parts.append(0.0)

    # 2. R² threshold
    if r_squared is not None and r_squared >= checks.get('r_squared_min', 0.9):
        score_parts.append(1.0)
    else:
        score_parts.append(0.0)

    # 3. predicted Er consistency
    if slope is not None and intercept is not None:
        pred_curv = checks.get('predicted_at_avg_curvature', 0.197)
        pred_er = slope * pred_curv + intercept
        target_er = checks.get('predicted_er_target', -0.17)
        tol = checks.get('predicted_er_tol', 0.2)
        if abs(pred_er - target_er) <= tol:
            score_parts.append(1.0)
        else:
            # partial credit based on relative error
            rel_err = abs(pred_er - target_er) / max(abs(target_er) + 1e-6, tol)
            partial = max(0.0, 1.0 - rel_err)
            score_parts.append(partial)
    else:
        score_parts.append(0.0)

    if len(score_parts) == 0:
        return 0.0
    return sum(score_parts) / len(score_parts)


_SCORERS = {
    'reaction_energies_curvatures': score_0,
    'band_gaps': score_1,
    'curvature_energy_linear_fit': score_2,
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
