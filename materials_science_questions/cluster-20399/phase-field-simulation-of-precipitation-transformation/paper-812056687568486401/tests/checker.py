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


# === block: score_0 (check id='step_01_gibbs_thomson') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    data = []
    for row in rows:
        try:
            r = float(row.get('radius_nm', ''))
            x = float(row.get('X_B_matrix', ''))
            data.append((r, x))
        except (ValueError, TypeError):
            return 0.0

    if len(data) < 2:
        return 0.0

    data.sort(key=lambda tup: tup[0])
    radii = [t[0] for t in data]
    xs = [t[1] for t in data]

    sw = step.get('sub_weights', {})
    w_mono = sw.get('monotonic', 0.2)
    w_points = sw.get('point_checks', 0.6)
    w_flat = sw.get('flat_check', 0.2)

    mono = all(xs[i] >= xs[i+1] - 1e-12 for i in range(len(xs)-1))
    mono_score = 1.0 if mono else 0.0

    target_radii = step.get('target_radii', [])
    gold_concs = step.get('gold_concentrations', [])
    tol_rel = step.get('tolerance_relative', 0.2)
    if len(target_radii) != len(gold_concs) or len(target_radii) == 0:
        point_scores = [0.0]
    else:
        point_scores = []
        for tr, gc in zip(target_radii, gold_concs):
            idx = min(range(len(radii)), key=lambda i: abs(radii[i] - tr))
            mx = xs[idx]
            if gc == 0:
                score = 1.0 if mx == 0 else 0.0
            else:
                rel_err = abs(mx - gc) / abs(gc)
                score = 1.0 if rel_err <= tol_rel else 0.0
            point_scores.append(score)
    avg_point = sum(point_scores) / len(point_scores) if point_scores else 0.0

    flat_conc = step.get('flat_conc', 0.0)
    flat_tol_rel = step.get('flat_tolerance_relative', 0.10)
    threshold_r = step.get('large_radius_threshold_nm', 900.0)
    large_idx = None
    for i, r in enumerate(radii):
        if r >= threshold_r:
            large_idx = i
            break
    if large_idx is None:
        large_idx = len(radii)-1
    mx_large = xs[large_idx]
    if flat_conc == 0:
        flat_score = 1.0 if mx_large == 0 else 0.0
    else:
        rel_err = abs(mx_large - flat_conc) / abs(flat_conc)
        flat_score = 1.0 if rel_err <= flat_tol_rel else 0.0

    score = w_mono * mono_score + w_points * avg_point + w_flat * flat_score
    return score


_SCORERS = {
    'step_01_gibbs_thomson': score_0,
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
