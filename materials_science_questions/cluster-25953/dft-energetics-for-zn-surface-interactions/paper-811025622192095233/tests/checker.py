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


# === block: score_0 (check id='transition_pressures') ===
def score_0(artifact, step, ctx):
    artifact = artifact  # artifact is a dict loaded from the JSON
    gold = step.get('gold', {})
    tol = step.get('tolerance_abs', 2.0)
    ok = True
    for key in ['B3LYP', 'LDA']:
        val = artifact.get(key)
        ref = gold.get(key)
        if val is None or ref is None or abs(val - ref) > tol:
            ok = False
            break
    return 1.0 if ok else 0.0


# === block: score_1 (check id='B3LYP_activation') ===
def score_1(artifact, step, ctx):
    import csv, io
    rows = artifact  # list of dicts; artifact is already a list if CSV was read
    # Recompute max per pathway
    pmm2_vals = []
    rm3_vals = []
    for r in rows:
        path = r.get('pathway', '').strip().lower()
        try:
            e = float(r.get('enthalpy_diff', 0.0))
        except:
            continue
        if path == 'pmm2':
            pmm2_vals.append(e)
        elif path == 'r3m':
            rm3_vals.append(e)
    if not pmm2_vals or not rm3_vals:
        return 0.0
    pmm2_max = max(pmm2_vals)
    rm3_max = max(rm3_vals)
    gold = step.get('gold', {})
    tol = step.get('tolerance_abs', 0.1)
    check_trend = step.get('check_trend', True)
    score = 0.0
    # trend
    if check_trend and pmm2_max < rm3_max:
        score += 0.5
    # Pmm2 tolerance
    ref_p = gold.get('Pmm2')
    if ref_p is not None and abs(pmm2_max - ref_p) <= tol:
        score += 0.25
    # R3m tolerance
    ref_r = gold.get('R3m')
    if ref_r is not None and abs(rm3_max - ref_r) <= tol:
        score += 0.25
    return min(score, 1.0)


# === block: score_2 (check id='LDA_activation') ===
def score_2(artifact, step, ctx):
    import csv, io
    rows = artifact  # list of dicts; artifact is already a list if CSV was read
    # Recompute max per pathway
    pmm2_vals = []
    rm3_vals = []
    for r in rows:
        path = r.get('pathway', '').strip().lower()
        try:
            e = float(r.get('enthalpy_diff', 0.0))
        except:
            continue
        if path == 'pmm2':
            pmm2_vals.append(e)
        elif path == 'r3m':
            rm3_vals.append(e)
    if not pmm2_vals or not rm3_vals:
        return 0.0
    pmm2_max = max(pmm2_vals)
    rm3_max = max(rm3_vals)
    gold = step.get('gold', {})
    tol = step.get('tolerance_abs', 0.1)
    score = 0.0
    # trend
    if step.get('check_trend', True) and pmm2_max < rm3_max:
        score += 0.5
    # Pmm2 tolerance
    ref_p = gold.get('Pmm2')
    if ref_p is not None and abs(pmm2_max - ref_p) <= tol:
        score += 0.25
    # R3m tolerance
    ref_r = gold.get('R3m')
    if ref_r is not None and abs(rm3_max - ref_r) <= tol:
        score += 0.25
    return min(score, 1.0)


# === block: score_3 (check id='band_gaps_B3LYP') ===
def score_3(artifact, step, ctx):
    artifact = artifact
    gold = step.get('gold', {})
    tol = step.get('tolerance_abs', 0.5)
    ok = True
    for key, ref in gold.items():
        val = artifact.get(key)
        if val is None or abs(val - ref) > tol:
            ok = False
            break
    return 1.0 if ok else 0.0


_SCORERS = {
    'transition_pressures': score_0,
    'B3LYP_activation': score_1,
    'LDA_activation': score_2,
    'band_gaps_B3LYP': score_3,
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
