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


# === block: score_0 (check id='step_03_emission_curve') ===
def score_0(artifact, step, ctx):
    details = step.get('details', {})
    if not details:
        return 0.0

    try:
        plateau_range = details['plateau_field_range']
        plateau_low, plateau_high = plateau_range[0], plateau_range[1]
        avalanche_min = details['avalanche_field_min']
        ratio_low = details['ratio_threshold_low']
        ratio_full = details['ratio_threshold_full']
    except (KeyError, ValueError, TypeError):
        return 0.0

    # Read optional tolerance from grading_spec step and relax thresholds
    tolerance = step.get('tolerance')
    if tolerance is not None:
        try:
            tol = float(tolerance)
        except (ValueError, TypeError):
            tol = 0.0
        ratio_full = max(0.0, ratio_full - tol)
        ratio_low = max(0.0, ratio_low - tol)

    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    try:
        fields = [float(row['electric_field_strength']) for row in artifact]
        counts = [float(row['emitted_electron_count']) for row in artifact]
    except (KeyError, ValueError, TypeError):
        return 0.0

    pairs = sorted(zip(fields, counts))

    plateau_vals = [c for f, c in pairs if plateau_low <= f <= plateau_high]
    if not plateau_vals:
        return 0.0
    median_plateau = sorted(plateau_vals)[len(plateau_vals) // 2]

    avalanche_vals = [c for f, c in pairs if f >= avalanche_min]
    if not avalanche_vals:
        return 0.0
    max_avalanche = max(avalanche_vals)

    if median_plateau <= 0:
        return 0.0

    ratio = max_avalanche / median_plateau
    if ratio >= ratio_full:
        return 1.0
    elif ratio >= ratio_low:
        return 0.5
    else:
        return 0.0


# === block: score_1 (check id='step_04_determine_breakdown') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, dict):
        return 0.0
    rng = artifact.get('breakdown_range_MV_per_cm')
    if not isinstance(rng, list) or len(rng) != 2:
        return 0.0
    try:
        low, high = float(rng[0]), float(rng[1])
    except (ValueError, TypeError):
        return 0.0
    gold_low, gold_high = 11.5, 12.5
    tol = 0.5
    def score_bound(val, gold):
        err = abs(val - gold)
        if err <= tol:
            return 1.0
        elif err <= 0.8:
            return 0.5
        else:
            return 0.0
    s = (score_bound(low, gold_low) + score_bound(high, gold_high)) / 2.0
    return s


_SCORERS = {
    'step_03_emission_curve': score_0,
    'step_04_determine_breakdown': score_1,
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
