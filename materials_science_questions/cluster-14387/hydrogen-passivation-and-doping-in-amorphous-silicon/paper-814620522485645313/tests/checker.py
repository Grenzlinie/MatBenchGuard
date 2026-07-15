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


# === block: score_0 (check id='step_bulk_gap') ===
def score_0(artifact, step, ctx):
    # artifact is the string content of bulk_si_gap.txt
    if not artifact.strip():
        return 0.0
    try:
        gap = float(artifact.strip())
    except ValueError:
        return 0.0
    target = step.get('target', 0.55)
    tol = step.get('tolerance_abs', 0.05)
    if abs(gap - target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_qd_correction') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts from qd_gaps.csv
    min_rows = step.get('min_rows', 3)
    tol = step.get('tolerance_abs', 0.01)
    rows = artifact
    if not isinstance(rows, list) or len(rows) < min_rows:
        return 0.0
    correction = 0.58
    total = len(rows)
    passed = 0
    for row in rows:
        try:
            raw = float(row['raw_gap_eV'])
            corrected = float(row['corrected_gap_eV'])
        except (KeyError, ValueError, TypeError):
            continue
        if abs(corrected - raw - correction) <= tol:
            passed += 1
    return passed / total


# === block: score_2 (check id='step_qd_monotonic') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or len(rows) < 2:
        return 0.0
    # extract (diameter, corrected) pairs, ignore bad rows
    pairs = []
    for row in rows:
        try:
            diam = float(row['diameter_nm'])
            corrected = float(row['corrected_gap_eV'])
            pairs.append((diam, corrected))
        except (KeyError, ValueError, TypeError):
            continue
    if len(pairs) < 2:
        return 0.0
    # sort by diameter ascending
    pairs.sort(key=lambda x: x[0])
    for i in range(len(pairs)-1):
        if pairs[i+1][1] > pairs[i][1] + 1e-9:
            return 0.0
    return 1.0


# === block: score_3 (check id='step_qd_reference') ===
def score_3(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0
    ref_points = step.get('reference_points', [])
    if not ref_points:
        return 1.0
    satisfied = 0
    for rp in ref_points:
        diam_target = rp['diameter_nm']
        gap_target = rp['corrected_gap_eV']
        tol_diam = rp.get('tolerance_diameter', 0.02)
        tol_gap = rp.get('tolerance_abs', 0.2)
        found_match = False
        for row in rows:
            try:
                diam = float(row['diameter_nm'])
                gap = float(row['corrected_gap_eV'])
            except (KeyError, ValueError, TypeError):
                continue
            if abs(diam - diam_target) <= tol_diam and abs(gap - gap_target) <= tol_gap:
                found_match = True
                break
        if found_match:
            satisfied += 1
    return satisfied / len(ref_points)


_SCORERS = {
    'step_bulk_gap': score_0,
    'step_qd_correction': score_1,
    'step_qd_monotonic': score_2,
    'step_qd_reference': score_3,
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
