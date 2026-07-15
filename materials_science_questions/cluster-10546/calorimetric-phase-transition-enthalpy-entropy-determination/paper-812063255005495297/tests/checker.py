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


# === block: score_0 (check id='phase_diagram_check') ===
def score_0(artifact, step, ctx):
    import math

    artifact_rows = artifact  # list of dicts
    gold = step['gold']
    points = gold['points']
    n_checks = len(points) + 2  # plus two structural checks
    passed = 0

    # 1. Compare at fixed compositions
    for pt in points:
        comp = pt['composition']
        ptype = pt['phase_type']
        match_lower = None
        match_upper = None
        for row in artifact_rows:
            try:
                row_c = float(row['composition_c_A'])
                row_pt = row['phase_type'].strip()
            except (ValueError, KeyError):
                continue
            if abs(row_c - comp) < 1e-5 and row_pt == ptype:
                match_lower = float(row['T_c_lower'])
                match_upper = float(row['T_c_upper'])
                break
        if match_lower is None or match_upper is None:
            continue
        ok_lower = False
        ok_upper = False
        gold_lower = pt['T_c_lower']
        gold_upper = pt['T_c_upper']
        if abs(match_lower - gold_lower) <= 1e-12:
            ok_lower = True
        elif abs(gold_lower) > 1e-12:
            rel = abs(match_lower - gold_lower) / abs(gold_lower)
            if rel <= pt['tol_rel']:
                ok_lower = True
        if abs(match_upper - gold_upper) <= 1e-12:
            ok_upper = True
        elif abs(gold_upper) > 1e-12:
            rel = abs(match_upper - gold_upper) / abs(gold_upper)
            if rel <= pt['tol_rel']:
                ok_upper = True
        if ok_lower and ok_upper:
            passed += 1

    # 2. Structural: L12 maximum composition range
    l12_rows = [r for r in artifact_rows if r['phase_type'].strip() == 'L12']
    if l12_rows:
        best = max(l12_rows, key=lambda r: float(r['T_c_upper']))
        max_comp = float(best['composition_c_A'])
        lo, hi = gold['max_L12_composition_range']
        if lo <= max_comp <= hi:
            passed += 1

    # 3. Structural: L10 maximum composition range
    l10_rows = [r for r in artifact_rows if r['phase_type'].strip() == 'L10']
    if l10_rows:
        best = max(l10_rows, key=lambda r: float(r['T_c_upper']))
        max_comp = float(best['composition_c_A'])
        lo, hi = gold['max_L10_composition_range']
        if lo <= max_comp <= hi:
            passed += 1

    return passed / float(n_checks) if n_checks > 0 else 0.0


# === block: score_1 (check id='transition_properties_check') ===
def score_1(artifact, step, ctx):
    gold_dict = step['gold']
    artifact_dict = artifact  # dict
    fields = list(gold_dict.keys())
    if not fields:
        return 1.0
    passed = 0
    for field, spec in gold_dict.items():
        if field not in artifact_dict:
            continue
        val = float(artifact_dict[field])  # ensure numeric
        ref = spec['value']
        if 'tol_rel' in spec:
            if abs(val - ref) <= 1e-12:
                passed += 1
            elif abs(ref) > 1e-12:
                rel = abs(val - ref) / abs(ref)
                if rel <= spec['tol_rel']:
                    passed += 1
        elif 'tol_abs' in spec:
            if abs(val - ref) <= spec['tol_abs']:
                passed += 1
    return passed / float(len(fields))


# === block: score_2 (check id='heat_capacity_structural') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    compositions = gold['compositions']
    window = gold['peak_window']
    transition_temps = gold['transition_temperatures']
    artifact_rows = artifact  # list of dicts
    score = 0.0
    for comp_tag in compositions:
        comp_str = str(comp_tag)
        # find target transition temp
        target_t = transition_temps.get(comp_str)
        if target_t is None:
            continue
        # collect rows for this composition (allow small floating difference)
        rows_c = []
        for r in artifact_rows:
            try:
                c = float(r['composition_c_A'])
            except (ValueError, KeyError):
                continue
            if abs(c - comp_tag) < 0.002:
                rows_c.append(r)
        if not rows_c:
            continue
        # find maximum Cv
        try:
            max_row = max(rows_c, key=lambda r: float(r['C_v_per_Nk']))
            max_t = float(max_row['reduced_temperature_t'])
        except (KeyError, ValueError):
            continue
        if abs(max_t - target_t) <= window:
            score += 0.5
    return min(score, 1.0)


_SCORERS = {
    'phase_diagram_check': score_0,
    'transition_properties_check': score_1,
    'heat_capacity_structural': score_2,
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
