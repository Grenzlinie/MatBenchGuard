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
    for step in spec.get('steps', []):
        sid = step.get('id')
        ctx[sid] = step.get('config', {})
    return ctx


# === block: score_0 (check id='s02_atomization') ===
def score_0(artifact, step, ctx):
    config = ctx.get(step['id'], {})
    gold = config.get('gold', {})
    tol = config.get('tolerances', {}).get('E_atomization_RPA', 0.02)
    total = 0
    correct = 0
    for item in artifact:
        crystal = item.get('crystal')
        rc = str(item.get('rc', ''))
        value = item.get('E_atomization_RPA')
        expected = gold.get(crystal, {}).get(rc)
        if expected is None:
            continue
        total += 1
        if abs(value - expected) <= tol:
            correct += 1
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='s04_hbn_interlayer') ===
def score_1(artifact, step, ctx):
    config = ctx.get(step['id'], {})
    gold_rows = config.get('gold', [])
    tol_d0 = config.get('tolerances', {}).get('d_0', 0.1)
    tol_C33 = config.get('tolerances', {}).get('C_33', 1.0)
    gold_index = {float(row['r_c']): row for row in gold_rows}
    total_rows = len(gold_rows)
    correct_rows = 0
    for row in artifact:
        r_c = float(row.get('r_c', ''))
        if r_c not in gold_index:
            continue
        gold = gold_index[r_c]
        d_ok = abs(float(row['d_0']) - gold['d_0']) <= tol_d0
        c_ok = abs(float(row['C_33']) - gold['C_33']) <= tol_C33
        if d_ok and c_ok:
            correct_rows += 1
    return correct_rows / total_rows if total_rows > 0 else 0.0


# === block: score_2 (check id='s06_defect_energies') ===
def score_2(artifact, step, ctx):
    config = ctx.get(step['id'], {})
    gold_list = config.get('gold', [])
    tol = config.get('tolerance', 0.1)
    gold_map = {}
    for g in gold_list:
        key = (g['supercell_size'], g['defect'])
        gold_map[key] = g
    checks = 0
    passed = 0
    for item in artifact:
        key = (item.get('supercell_size'), item.get('defect'))
        g = gold_map.get(key)
        if g is None:
            continue
        checks += 1
        if abs(item.get('formation_energy', 0) - g['formation_energy']) <= tol:
            passed += 1
        if 'migration_barrier' in g and g['migration_barrier'] is not None:
            checks += 1
            actual_barrier = item.get('migration_barrier')
            if actual_barrier is not None and abs(actual_barrier - g['migration_barrier']) <= tol:
                passed += 1
    return passed / checks if checks > 0 else 0.0


_SCORERS = {
    's02_atomization': score_0,
    's04_hbn_interlayer': score_1,
    's06_defect_energies': score_2,
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
