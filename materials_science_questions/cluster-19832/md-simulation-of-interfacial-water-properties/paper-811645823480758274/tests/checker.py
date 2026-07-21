import os
import json
import csv

# === author imports / helpers ===
def _sort_rows(rows, key):
    return sorted(rows, key=lambda r: float(r[key]))


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


# === block: score_0 (check id='check_file_shape') ===
def score_0(artifact, step, ctx):
    if artifact is None: return 0.0
    required = ['period_lambda_sigma', 'normalized_lambda_over_rB', 'contact_angle_degrees', 'cavity_density_rhocav_sigma3']
    if not artifact or not all(col in artifact[0] for col in required): return 0.0
    if len(artifact) < 5: return 0.0
    # Additional content validation: contact angles must be within a plausible range for water on Si with ε_wf/ε=2.0
    # (derived from paper reports of 63-70° smooth, 75-85° peak, 60-70° trough, with a ±15° margin)
    try:
        for row in artifact:
            angle = float(row['contact_angle_degrees'])
            if not (50.0 <= angle <= 95.0):
                return 0.0
    except (ValueError, KeyError):
        return 0.0
    return 1.0


# === block: score_1 (check id='check_nonmonotonic') ===
def score_1(artifact, step, ctx):
    if not artifact: return 0.0
    try:
        sorted_rows = _sort_rows(artifact, 'normalized_lambda_over_rB')
        angles = [float(r['contact_angle_degrees']) for r in sorted_rows]
    except (ValueError, KeyError):
        return 0.0
    if len(angles) < 3: return 0.0
    max_idx = max(range(len(angles)), key=lambda i: angles[i])
    if max_idx == 0 or max_idx == len(angles)-1:
        return 0.0
    min_after = min(angles[max_idx+1:])
    if min_after >= angles[max_idx]: return 0.0
    min_after_idx = angles.index(min_after, max_idx+1)
    if angles[min_after_idx+1:] and max(angles[min_after_idx+1:]) > min_after:
        return 1.0
    return 0.0


# === block: score_2 (check id='check_cavity_threshold') ===
def score_2(artifact, step, ctx):
    if not artifact: return 0.0
    try:
        sorted_rows = _sort_rows(artifact, 'normalized_lambda_over_rB')
        first_density = float(sorted_rows[0]['cavity_density_rhocav_sigma3'])
        last_density = float(sorted_rows[-1]['cavity_density_rhocav_sigma3'])
    except (ValueError, KeyError, IndexError):
        return 0.0
    if first_density < 0.2 and last_density > 0.2: return 1.0
    return 0.0


# === block: score_3 (check id='check_plausible') ===
def score_3(artifact, step, ctx):
    if not artifact: return 0.0
    try:
        for row in artifact:
            angle = float(row['contact_angle_degrees'])
            density = float(row['cavity_density_rhocav_sigma3'])
            if not (0 < angle < 180) or density < 0:
                return 0.0
    except (ValueError, KeyError):
        return 0.0
    return 1.0


_SCORERS = {
    'check_file_shape': score_0,
    'check_nonmonotonic': score_1,
    'check_cavity_threshold': score_2,
    'check_plausible': score_3,
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
