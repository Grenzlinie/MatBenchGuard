import os
import json
import csv

# === author imports / helpers ===
import os
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
    return {"outputs_dir": outputs_dir}


# === block: score_0 (check id='peak_time_recompute') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0:
        return 0.0
    times = [float(row.get('time_fs',0)) for row in artifact]
    rms = [float(row.get('rms_displacement_AA',0)) for row in artifact]
    if len(times) == 0:
        return 0.0
    max_rms = max(rms)
    peak_idx = rms.index(max_rms)
    peak_time = times[peak_idx]
    if abs(peak_time - 146.0) <= 40.0:
        return 1.0
    return 0.0


# === block: score_1 (check id='oscillation_structural') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    times = [float(row['time_fs']) for row in artifact]
    rms = [float(row['rms_displacement_AA']) for row in artifact]
    n = len(rms)
    first_n = min(5, n)
    last_n = min(5, n)
    avg_first = sum(rms[:first_n]) / first_n if first_n > 0 else 0.0
    avg_last = sum(rms[-last_n:]) / last_n if last_n > 0 else 0.0
    max_rms = max(rms)
    if max_rms > avg_first and max_rms > avg_last and rms[-1] < max_rms:
        return 1.0
    return 0.0


# === block: score_2 (check id='variance_consistency') ===
def score_2(artifact, step, ctx):
    if artifact is None:
        return 0.0
    json_data = artifact
    csv_path = os.path.join(ctx['outputs_dir'], 'rms_displacement_50mH.csv')
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            csv_rows = list(reader)
    except Exception:
        return 0.0
    if not csv_rows:
        return 0.0
    sq_vals = [float(row['rms_displacement_AA'])**2 for row in csv_rows]
    max_sq = max(sq_vals)
    min_sq = min(sq_vals)
    zpv_csv = float(csv_rows[0].get('zero_point_variance_AA2', 0))
    if zpv_csv == 0:
        return 0.0
    recomputed_min = min_sq / zpv_csv
    recomputed_max = max_sq / zpv_csv
    score = 0.0
    reported_min = json_data.get('variance_min_ratio_50mH', None)
    reported_max = json_data.get('variance_max_ratio_50mH', None)
    reported_zpv = json_data.get('zero_point_variance_AA2', None)
    if reported_min is not None and abs(reported_min - recomputed_min) < 0.01:
        score += 0.3
    if reported_max is not None and abs(reported_max - recomputed_max) < 0.01:
        score += 0.3
    if reported_zpv is not None and abs(reported_zpv - zpv_csv) < 1e-6:
        score += 0.4
    return score


_SCORERS = {
    'peak_time_recompute': score_0,
    'oscillation_structural': score_1,
    'variance_consistency': score_2,
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
