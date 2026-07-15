import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='csv_shape_gate') ===
def score_0(artifact, step, ctx):
    required = step.get('params', {}).get('required_columns', [])
    exp_compounds = set(step.get('params', {}).get('expected_compounds', []))
    if not isinstance(artifact, list) or len(artifact) < max(len(exp_compounds), 1):
        return 0.0
    cols = set(artifact[0].keys()) if artifact else set()
    col_ok = all(c in cols for c in required)
    compounds_found = set(row.get('compound', '') for row in artifact)
    comp_ok = exp_compounds.issubset(compounds_found) if exp_compounds else True
    return 1.0 if (col_ok and comp_ok) else 0.0


# === block: score_1 (check id='lattice_accuracy') ===
def score_1(artifact, step, ctx):
    expected = step.get('params', {}).get('expected', [])
    tol = float(step.get('params', {}).get('tolerance_relative', 0.02))
    if not expected:
        return 0.0
    exp_map = {}
    for e in expected:
        key = (e.get('compound', ''), e.get('arrangement', ''))
        exp_map[key] = float(e['optimized_a'])
    correct = 0
    total = 0
    for row in artifact:
        key = (row.get('compound', ''), row.get('arrangement', ''))
        exp = exp_map.get(key)
        if exp is not None:
            try:
                a_val = float(row['optimized_a'])
            except (ValueError, KeyError):
                continue
            rel_err = abs(a_val - exp) / exp if exp != 0 else abs(a_val - exp)
            if rel_err <= tol:
                correct += 1
            total += 1
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='lialsi_energy_ordering') ===
def score_2(artifact, step, ctx):
    compound = step.get('params', {}).get('compound', 'LiAlSi')
    order = step.get('params', {}).get('arrangement_order', ['I', 'II', 'III'])
    energy_col = step.get('params', {}).get('energy_column', 'total_energy_ev')
    rel = step.get('params', {}).get('relation', 'increasing')
    rows = [r for r in artifact if r.get('compound', '') == compound]
    if len(rows) < len(order):
        return 0.0
    arr_map = {}
    for r in rows:
        arr = r.get('arrangement', '')
        try:
            e = float(r[energy_col])
        except (ValueError, KeyError):
            continue
        arr_map[arr] = e
    for o in order:
        if o not in arr_map:
            return 0.0
    vals = [arr_map[o] for o in order]
    if rel == 'increasing':
        if all(vals[i] < vals[i+1] for i in range(len(vals)-1)):
            return 1.0
        else:
            return 0.0
    return 0.0


# === block: score_3 (check id='li2alsi_energy_equality') ===
def score_3(artifact, step, ctx):
    compound = step.get('params', {}).get('compound', 'Li2AlSi')
    keys = step.get('params', {}).get('arrangement_keys', ['non-centrosymmetric', 'centrosymmetric'])
    col = step.get('params', {}).get('energy_column', 'total_energy_ev')
    max_diff = float(step.get('params', {}).get('max_abs_diff', 0.1))
    rows = [r for r in artifact if r.get('compound', '') == compound]
    if len(rows) < 2:
        return 0.0
    vals = {}
    for r in rows:
        arr = r.get('arrangement', '')
        try:
            e = float(r[col])
        except (ValueError, KeyError):
            continue
        vals[arr] = e
    found = []
    for k in keys:
        # allow partial matching for variations like 'centrosymmetric' vs 'centrosymmetric' etc.
        matched = None
        for a, e in vals.items():
            if k.lower() in a.lower():
                matched = e
                break
        if matched is not None:
            found.append(matched)
    if len(found) != 2:
        return 0.0
    if abs(found[0] - found[1]) <= max_diff:
        return 1.0
    return 0.0


# === block: score_4 (check id='metallic_flags') ===
def score_4(artifact, step, ctx):
    expected = step.get('params', {}).get('expected', [])
    exp_map = {}
    for e in expected:
        key = (e.get('compound', ''), e.get('arrangement', ''))
        exp_map[key] = bool(e['is_metallic'])
    correct = 0
    total = 0
    for row in artifact:
        key = (row.get('compound', ''), row.get('arrangement', ''))
        exp = exp_map.get(key)
        if exp is not None:
            try:
                flag = row.get('is_metallic', False)
                if isinstance(flag, str):
                    flag = flag.strip().lower() in ('true', '1', 'yes')
                else:
                    flag = bool(flag)
            except Exception:
                continue
            if flag == exp:
                correct += 1
            total += 1
    return correct / total if total > 0 else 0.0


_SCORERS = {
    'csv_shape_gate': score_0,
    'lattice_accuracy': score_1,
    'lialsi_energy_ordering': score_2,
    'li2alsi_energy_equality': score_3,
    'metallic_flags': score_4,
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
