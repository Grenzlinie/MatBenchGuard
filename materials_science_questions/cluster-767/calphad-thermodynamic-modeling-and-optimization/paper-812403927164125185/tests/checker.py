import os
import json
import csv

# === author imports / helpers ===
import re


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
        if step.get('id') == 'invariant_reactions':
            ctx['gold_reactions'] = step.get('gold_reactions', [])
            ctx['tolerance_K'] = step.get('tolerance_K', 15)
        elif step.get('id') == 'formation_enthalpies':
            ctx['gold_compounds'] = step.get('gold_compounds', [])
            ctx['tolerance_kJ'] = step.get('tolerance_kJ_per_mol_atom', 5.0)
    return ctx


# === block: score_0 (check id='invariant_reactions') ===
def score_0(artifact, step, ctx):
    gold_reactions = ctx.get('gold_reactions', [])
    if not gold_reactions:
        return 0.0
    tolerance = ctx.get('tolerance_K', 15)
    if not artifact:
        return 0.0

    rows_with_temp = []
    for idx, row in enumerate(artifact):
        try:
            temp = float(row.get('temperature_K', 0))
            rtype = row.get('reaction_type', '').strip().lower()
            rows_with_temp.append((rtype, temp, idx))
        except (ValueError, TypeError):
            pass

    used_rows = set()
    matched = 0
    for gold in gold_reactions:
        gold_type = gold['reaction_type'].strip().lower()
        gold_temp = gold['temperature_K']
        best_idx = None
        best_diff = float('inf')
        for rtype, temp, idx in rows_with_temp:
            if idx in used_rows:
                continue
            if rtype == gold_type:
                diff = abs(temp - gold_temp)
                if diff <= tolerance and diff < best_diff:
                    best_diff = diff
                    best_idx = idx
        if best_idx is not None:
            matched += 1
            used_rows.add(best_idx)

    return matched / len(gold_reactions)


# === block: score_1 (check id='formation_enthalpies') ===
def score_1(artifact, step, ctx):
    gold_compounds = ctx.get('gold_compounds', [])
    if not gold_compounds:
        return 0.0
    tolerance = ctx.get('tolerance_kJ', 5.0)
    matched = 0
    for gold in gold_compounds:
        gold_comp = gold['compound'].strip().lower()
        gold_enthalpy = gold['enthalpy_kJ_per_mol_atom']
        for row in artifact:
            if row.get('compound', '').strip().lower() == gold_comp:
                try:
                    calc_enthalpy = float(row.get('enthalpy_kJ_per_mol_atom', 0))
                    if abs(calc_enthalpy - gold_enthalpy) <= tolerance:
                        matched += 1
                except (ValueError, TypeError):
                    pass
                break
    return matched / len(gold_compounds)


_SCORERS = {
    'invariant_reactions': score_0,
    'formation_enthalpies': score_1,
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
