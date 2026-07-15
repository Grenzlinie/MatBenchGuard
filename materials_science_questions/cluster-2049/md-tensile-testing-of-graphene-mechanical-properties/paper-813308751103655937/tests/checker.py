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


# === block: score_0 (check id='step_02_compute_bavg') ===
def score_0(artifact, step, ctx):
    import os
    evidence_path = "/app/outputs/md_configurations.txt"
    if not os.path.isfile(evidence_path) or os.path.getsize(evidence_path) < 1000:
        return 0.0
    # artifact is list of dicts with keys 'x (nm)' and 'B_avg (T)'
    x_vals = []
    b_vals = []
    for row in artifact:
        try:
            x = float(row['x (nm)'])
            b = float(row['B_avg (T)'])
            x_vals.append(x)
            b_vals.append(b)
        except (ValueError, KeyError):
            return 0.0
    n = len(b_vals)
    if n < 50:
        return 0.0
    b_max = max(b_vals)
    b_min = min(b_vals)
    if b_max == b_min:
        return 0.0
    abs_max = max(abs(b_max), abs(b_min))
    if abs_max < 1.0:
        return 0.0
    # 1. Plausible magnitude
    if 10.0 <= abs_max <= 2000.0:
        mag_score = 0.3
    elif abs_max > 2000.0:
        mag_score = 0.15
    else:
        mag_score = 0.0
    # 2. Opposite signs
    sign_score = 0.2 if (b_max > 0 and b_min < 0) or (b_max < 0 and b_min > 0) else 0.0
    # 3. Zero net average
    avg_b = sum(b_vals) / n
    rel_avg = abs(avg_b) / (abs_max + 1e-12)
    if rel_avg < 0.15:
        zero_score = 0.2
    elif rel_avg < 0.3:
        zero_score = 0.1
    else:
        zero_score = 0.0
    # 4. Peak locations near step (x=0)
    idx_max = b_vals.index(b_max)
    idx_min = b_vals.index(b_min)
    x_max = x_vals[idx_max]
    x_min = x_vals[idx_min]
    loc_max_ok = -2.0 <= x_max <= 2.0
    loc_min_ok = -2.0 <= x_min <= 2.0
    if loc_max_ok and loc_min_ok:
        loc_score = 0.3
    elif -3.0 <= x_max <= 3.0 and -3.0 <= x_min <= 3.0:
        loc_score = 0.2
    else:
        loc_score = 0.0
    total = mag_score + sign_score + zero_score + loc_score
    return min(max(total, 0.0), 1.0)


_SCORERS = {
    'step_02_compute_bavg': score_0,
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
