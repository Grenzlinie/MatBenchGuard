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


# === block: score_0 (check id='recompute_young_from_stress_strain') ===
def score_0(artifact, step, ctx):
    data = artifact
    strain_min = float(step.get('strain_min', 0.03))
    strain_max = float(step.get('strain_max', 0.05))
    gold = step['gold_moduli']
    tol_rel = float(step.get('tolerance_rel', 0.10))
    falloff = float(step.get('falloff_multiplier', 2.0))

    groups = {}
    for d in data:
        diam = str(d['diameter_nm'])
        s = float(d['strain'])
        if strain_min <= s <= strain_max:
            groups.setdefault(diam, []).append((s, float(d['stress_GPa'])))

    scores = {}
    slopes = {}
    for diam, points in groups.items():
        if len(points) < 2:
            scores[diam] = 0.0
            continue
        n = len(points)
        sx = sy = sxx = sxy = 0.0
        for x, y in points:
            sx += x
            sy += y
            sxx += x * x
            sxy += x * y
        denom = n * sxx - sx * sx
        if abs(denom) < 1e-30:
            scores[diam] = 0.0
            continue
        slope = (n * sxy - sx * sy) / denom
        slopes[diam] = slope
        gold_val = float(gold.get(diam, 0.0))
        if gold_val == 0.0:
            scores[diam] = 0.0
            continue
        rel_err = abs(slope - gold_val) / gold_val
        if rel_err <= tol_rel:
            scores[diam] = 1.0
        elif rel_err <= falloff * tol_rel:
            scores[diam] = 1.0 - (rel_err - tol_rel) / (falloff * tol_rel - tol_rel)
        else:
            scores[diam] = 0.0

    for diam in gold.keys():
        if diam not in scores:
            scores[diam] = 0.0

    ctx['recomputed_slopes'] = slopes
    if not scores:
        return 0.0
    return sum(scores.values()) / len(scores)


# === block: score_1 (check id='young_moduli_consistency') ===
def score_1(artifact, step, ctx):
    report = artifact
    slopes = ctx.get('recomputed_slopes', {})
    tol_abs = float(step.get('tolerance_abs', 0.01))
    tol_rel = float(step.get('tolerance_rel', 1e-6))

    diams = ['2','3','4','6']
    score_sum = 0.0
    count = 0
    for diam in diams:
        if diam not in report or diam not in slopes:
            continue
        self_val = float(report[diam])
        slope_val = slopes[diam]
        if abs(self_val - slope_val) <= max(tol_rel * max(abs(self_val), abs(slope_val)), tol_abs):
            score_sum += 1.0
        else:
            score_sum += 0.0
        count += 1
    if count == 0:
        return 0.0
    return score_sum / count


_SCORERS = {
    'recompute_young_from_stress_strain': score_0,
    'young_moduli_consistency': score_1,
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
