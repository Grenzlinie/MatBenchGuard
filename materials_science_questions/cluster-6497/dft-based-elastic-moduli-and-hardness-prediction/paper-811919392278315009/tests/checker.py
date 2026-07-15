import os
import json
import csv

# === author imports / helpers ===
import csv, math, json, collections


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


# === block: score_0 (check id='bulk_properties') ===
def score_0(artifact, step, ctx):
    gold_rows = step.get('gold', {}).get('rows', [])
    internal_consistency = step.get('gold', {}).get('internal_consistency', {})
    max_diff = internal_consistency.get('max_diff_gpa', 1.0)
    gold_map = {}
    tolerance_map = {}
    for gr in gold_rows:
        gold_map[gr['Property']] = gr['Value']
        tolerance_map[gr['Property']] = gr['tolerance']
    total_rows = len(gold_rows)
    matches = 0
    ye = None
    yv = None
    for row in artifact:
        prop = row.get('Property', '').strip()
        try:
            val = float(row.get('Value', '0'))
        except:
            continue
        if prop in gold_map:
            if abs(val - gold_map[prop]) <= tolerance_map.get(prop, 0):
                matches += 1
        if prop == "Young's modulus energy":
            ye = val
        elif prop == "Young's modulus virial":
            yv = val
    consistency_ok = True
    if ye is not None and yv is not None:
        if abs(ye - yv) > max_diff:
            consistency_ok = False
    score_rows = (matches / total_rows) if total_rows > 0 else 0.0
    total_score = 0.9 * score_rows + 0.1 * (1.0 if consistency_ok else 0.0)
    return total_score


# === block: score_1 (check id='nanowire_moduli') ===
def score_1(artifact, step, ctx):
    structures_gold = step.get('gold', {}).get('structures', [])
    tol_radius = step.get('gold', {}).get('tolerance_radius', 1.0)
    tol_mod_pct = step.get('gold', {}).get('tolerance_modulus_percent', 5.0)
    tol_mod_abs = step.get('gold', {}).get('tolerance_modulus_abs', 10.0)
    trend_check = step.get('gold', {}).get('trend_check', False)
    gold_by_name = {s['Structure']: s for s in structures_gold}
    num_structs = len(structures_gold)
    radius_correct = 0
    modulus_correct = 0
    data_entries = []
    for row in artifact:
        struct_name = row.get('Structure', '').strip()
        if struct_name not in gold_by_name:
            continue
        g = gold_by_name[struct_name]
        r = float(row.get('Radius', 0))
        if abs(r - g['Radius']) <= tol_radius:
            radius_correct += 1
        ye = float(row.get('Young_modulus_energy', 0))
        yv = float(row.get('Young_modulus_virial', 0))
        tol = max(tol_mod_abs, tol_mod_pct / 100.0 * abs(g['Young_modulus']))
        if abs(ye - g['Young_modulus']) <= tol:
            modulus_correct += 1
        if abs(yv - g['Young_modulus']) <= tol:
            modulus_correct += 1
        data_entries.append((r, ye, yv, struct_name))
    total_checks = num_structs * 3
    value_score = (radius_correct + modulus_correct) / total_checks if total_checks > 0 else 0.0
    trend_ok = True
    if trend_check and len(data_entries) >= 2:
        for method_idx in [1, 2]:
            vals = [(r, (ye if method_idx == 1 else yv)) for r, ye, yv, _ in data_entries]
            vals_sorted = sorted(vals, key=lambda x: x[0])
            prev = None
            for _, y in vals_sorted:
                if prev is not None and y > prev + 0.1:
                    trend_ok = False
                    break
                prev = y
            if not trend_ok:
                break
    final_score = 0.8 * value_score + 0.2 * (1.0 if trend_ok else 0.0)
    return final_score


# === block: score_2 (check id='nanotube_moduli') ===
def score_2(artifact, step, ctx):
    structures_gold = step.get('gold', {}).get('structures', [])
    tol_radius = step.get('gold', {}).get('tolerance_radius', 1.0)
    tol_thickness = step.get('gold', {}).get('tolerance_thickness', 1.0)
    tol_mod_pct = step.get('gold', {}).get('tolerance_modulus_percent', 5.0)
    tol_mod_abs = step.get('gold', {}).get('tolerance_modulus_abs', 10.0)
    trend_check = step.get('gold', {}).get('trend_check', False)
    gold_by_name = {s['Structure']: s for s in structures_gold}
    num_structs = len(structures_gold)
    radius_correct = 0
    thickness_correct = 0
    modulus_correct = 0
    data_entries = []
    for row in artifact:
        struct_name = row.get('Structure', '').strip()
        if struct_name not in gold_by_name:
            continue
        g = gold_by_name[struct_name]
        outer_r = float(row.get('Outer_radius', 0))
        inner_r = float(row.get('Inner_radius', 0))
        wt = float(row.get('Wall_thickness', 0))
        if abs(outer_r - g['Outer_radius']) <= tol_radius and abs(inner_r - g['Inner_radius']) <= tol_radius:
            radius_correct += 1
        if abs(wt - g['Wall_thickness']) <= tol_thickness:
            thickness_correct += 1
        ye = float(row.get('Young_modulus_energy', 0))
        yv = float(row.get('Young_modulus_virial', 0))
        tol = max(tol_mod_abs, tol_mod_pct / 100.0 * abs(g['Young_modulus']))
        if abs(ye - g['Young_modulus']) <= tol:
            modulus_correct += 1
        if abs(yv - g['Young_modulus']) <= tol:
            modulus_correct += 1
        data_entries.append((wt, ye, yv, struct_name, row.get('Type', '')))
    radius_frac = radius_correct / num_structs if num_structs > 0 else 0.0
    thickness_frac = thickness_correct / num_structs if num_structs > 0 else 0.0
    modulus_frac = modulus_correct / (2 * num_structs) if num_structs > 0 else 0.0
    value_score = (radius_frac + thickness_frac + modulus_frac) / 3.0
    trend_ok = True
    if trend_check and len(data_entries) >= 2:
        groups = {}
        for entry in data_entries:
            tp = entry[-1]
            groups.setdefault(tp, []).append(entry)
        for tp, entries in groups.items():
            sorted_entries = sorted(entries, key=lambda x: x[0])
            for method_idx in [1, 2]:
                prev = None
                for entry in sorted_entries:
                    y = entry[method_idx]
                    if prev is not None and y > prev + 0.1:
                        trend_ok = False
                        break
                    prev = y
                if not trend_ok:
                    break
            if not trend_ok:
                break
    final_score = 0.8 * value_score + 0.2 * (1.0 if trend_ok else 0.0)
    return final_score


_SCORERS = {
    'bulk_properties': score_0,
    'nanowire_moduli': score_1,
    'nanotube_moduli': score_2,
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
