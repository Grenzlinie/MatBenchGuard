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
    ctx = {}
    for step in spec['steps']:
        if step['id'] == 'struct_opt':
            ctx['struct_opt_gold'] = {row['compound']: row for row in step['gold_rows']}
            ctx['struct_tol_len'] = step['tolerance_details']['length_Å']
            ctx['struct_tol_z'] = step['tolerance_details']['z']
            ctx['struct_tol_bond'] = step['tolerance_details']['bond_Å']
        elif step['id'] == 'mag_moments':
            ctx['mag_gold'] = {(row['compound'], row['method']): row for row in step['gold_rows']}
            ctx['mag_tol'] = step['tolerance']
        elif step['id'] == 'dos_gap':
            ctx['dos_expected'] = step['expected_gap']
            ctx['gap_threshold'] = step['gap_threshold']
    return ctx


# === block: score_0 (check id='struct_opt') ===
def score_0(artifact, step, ctx):
    gold_map = ctx['struct_opt_gold']
    tol_len = ctx['struct_tol_len']
    tol_z = ctx['struct_tol_z']
    tol_bond = ctx['struct_tol_bond']
    total_checks = 0
    passed = 0
    for row in artifact:
        compound = row.get('compound')
        if compound not in gold_map:
            continue
        g = gold_map[compound]
        for field, gold_val in g.items():
            if field == 'compound':
                continue
            if field in ('a (Å)', 'b (Å)', 'c (Å)'):
                tol = tol_len
            elif field in ('Fe_As_1 (Å)', 'Fe_As_2 (Å)'):
                tol = tol_bond
            else:
                tol = tol_z
            actual = row.get(field)
            if actual is None:
                continue
            try:
                actual_val = float(actual)
            except (ValueError, TypeError):
                continue
            if abs(actual_val - float(gold_val)) <= tol:
                passed += 1
            total_checks += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_1 (check id='mag_moments') ===
def score_1(artifact, step, ctx):
    gold_map = ctx['mag_gold']
    tol = ctx['mag_tol']
    row_scores = []
    for row in artifact:
        compound = row.get('compound')
        method = row.get('method')
        if compound is None or method is None:
            continue
        key = (compound.strip(), method.strip())
        if key not in gold_map:
            continue
        g = gold_map[key]
        R_actual = row.get('R_moment (μ_B)')
        Fe_actual = row.get('Fe_moment (μ_B)')
        if R_actual is None or Fe_actual is None:
            continue
        try:
            R_val = float(R_actual)
            Fe_val = float(Fe_actual)
        except (ValueError, TypeError):
            continue
        R_gold = float(g['R_moment (μ_B)'])
        Fe_gold = float(g['Fe_moment (μ_B)'])
        R_ok = abs(R_val - R_gold) <= tol
        Fe_ok = abs(Fe_val - Fe_gold) <= tol
        if R_ok and Fe_ok:
            row_scores.append(1.0)
        elif R_ok or Fe_ok:
            row_scores.append(0.5)
        else:
            row_scores.append(0.0)
    if not row_scores:
        return 0.0
    return sum(row_scores) / len(row_scores)


# === block: score_2 (check id='dos_gap') ===
def score_2(artifact, step, ctx):
    expected = ctx['dos_expected']
    gap_thresh = ctx['gap_threshold']
    scores = []
    for row in artifact:
        compound = row.get('compound')
        if compound not in expected:
            continue
        expected_gap = expected[compound]
        agent_gap = row.get('gap')
        if agent_gap is None:
            continue
        if compound == 'Sm':
            if str(agent_gap).strip().lower() == 'metallic':
                scores.append(1.0)
            else:
                scores.append(0.0)
        else:
            try:
                gap_val = float(agent_gap)
            except (ValueError, TypeError):
                scores.append(0.0)
                continue
            if gap_val >= gap_thresh:
                scores.append(1.0)
            else:
                scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'struct_opt': score_0,
    'mag_moments': score_1,
    'dos_gap': score_2,
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
