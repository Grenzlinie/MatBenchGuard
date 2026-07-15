import os
import json
import csv

# === author imports / helpers ===
import os, csv, json, math

def score_mae(artifact, step, ctx):
    if not artifact:
        return 0.0
    true_col = step['true_column']
    pred_col = step['pred_column']
    ref = step['paper_reported_mae']
    fp = step.get('fp_floor', 0.001)
    decay = step.get('decay_factor', 0.2)
    total = 0.0
    n = 0
    for row in artifact:
        try:
            t = float(row[true_col])
            p = float(row[pred_col])
            total += abs(t - p)
            n += 1
        except (ValueError, KeyError):
            continue
    if n == 0:
        return 0.0
    mae = total / n
    if math.isnan(mae) or math.isinf(mae):
        return 0.0
    if mae <= ref + fp:
        return 1.0
    return max(0.0, 1.0 - (mae - ref) / (decay * ref))

def score_consistency(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    prop_map = step.get('properties', {})
    tol = step.get('tolerance_abs', 0.01)
    fallback_tol = step.get('fallback_tolerance_abs', 0.1)
    per_prop = []
    for prop, info in prop_map.items():
        key = info['mae_key']
        if key not in artifact:
            per_prop.append(0.0)
            continue
        reported = float(artifact[key])
        recomputed = ctx.get(f'mae_{prop}')
        if recomputed is not None:
            diff = abs(reported - recomputed)
            if diff <= tol:
                per_prop.append(1.0)
            else:
                per_prop.append(max(0.0, 1.0 - (diff - tol) / tol))
        else:
            # fallback: compare reported to paper gold
            gold = info['gold_mae']
            if reported <= gold:
                per_prop.append(1.0)
            else:
                diff_abs = abs(reported - gold)
                if diff_abs <= fallback_tol:
                    per_prop.append(1.0 - diff_abs / fallback_tol)
                else:
                    per_prop.append(0.0)
    if not per_prop:
        return 0.0
    return sum(per_prop) / len(per_prop)


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
    import os, csv, json

    def compute_mae(rows, true_col, pred_col):
        total = 0.0
        n = 0
        for row in rows:
            try:
                t = float(row[true_col])
                p = float(row[pred_col])
                total += abs(t - p)
                n += 1
            except (ValueError, KeyError):
                continue
        return (total / n) if n > 0 else None

    ctx = {}
    fmap = [
        ("predictions_total_energy.csv", "mae_total_energy"),
        ("predictions_bandgap.csv", "mae_bandgap"),
        ("predictions_shear_modulus.csv", "mae_shear_modulus"),
        ("predictions_bulk_modulus.csv", "mae_bulk_modulus"),
    ]
    for fname, key in fmap:
        path = os.path.join(outputs_dir, fname)
        if os.path.exists(path):
            with open(path, newline='') as f:
                rows = list(csv.DictReader(f))
            mae = compute_mae(rows, "true_value", "predicted_value")
            ctx[key] = mae
        else:
            ctx[key] = None
    return ctx


# === block: score_0 (check id='step_04') ===
def score_0(artifact, step, ctx):
    import copy
    step_new = copy.deepcopy(step)
    step_new['fp_floor'] = 0.05
    step_new['decay_factor'] = 0.5
    return score_mae(artifact, step_new, ctx)


# === block: score_1 (check id='step_05') ===
def score_1(artifact, step, ctx):
    return score_mae(artifact, step, ctx)


# === block: score_2 (check id='step_06') ===
def score_2(artifact, step, ctx):
    return score_mae(artifact, step, ctx)


# === block: score_3 (check id='step_07') ===
def score_3(artifact, step, ctx):
    return score_mae(artifact, step, ctx)


# === block: score_4 (check id='step_08') ===
def score_4(artifact, step, ctx):
    return score_consistency(artifact, step, ctx)


_SCORERS = {
    'step_04': score_0,
    'step_05': score_1,
    'step_06': score_2,
    'step_07': score_3,
    'step_08': score_4,
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
