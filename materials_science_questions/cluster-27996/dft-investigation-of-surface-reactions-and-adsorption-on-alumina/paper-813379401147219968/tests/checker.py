import os
import json
import csv

# === author imports / helpers ===
import json, csv


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


# === block: score_0 (check id='step_02_gamma_surface_relaxation') ===
def score_0(artifact, step, ctx):
    gold_rows = step['gold']['rows']
    tol = step['gold']['tolerances']
    fields = [('delta_z_gas','delta_z'), ('Q_gas','Q'), ('delta_z_liquid','delta_z'), ('Q_liquid','Q')]
    total = len(gold_rows) * len(fields)
    matched = 0
    for row in artifact:
        atom = row.get('atom_label')
        gold = next((g for g in gold_rows if g['atom_label'] == atom), None)
        if gold is None:
            continue
        for fname, tkey in fields:
            try:
                val = float(row[fname])
                if abs(val - gold[fname]) <= tol[tkey]:
                    matched += 1
            except (ValueError, KeyError):
                pass
    return matched / total if total else 0.0


# === block: score_1 (check id='step_03_boehmite_surface_relaxation') ===
def score_1(artifact, step, ctx):
    gold_rows = step['gold']['rows']
    tol = step['gold']['tolerances']
    fields = [('delta_z_gas','delta_z'), ('Q_gas','Q'), ('delta_z_liquid','delta_z'), ('Q_liquid','Q')]
    total = len(gold_rows) * len(fields)
    matched = 0
    for row in artifact:
        atom = row.get('atom_label')
        gold = next((g for g in gold_rows if g['atom_label'] == atom), None)
        if gold is None:
            continue
        for fname, tkey in fields:
            try:
                val = float(row[fname])
                if abs(val - gold[fname]) <= tol[tkey]:
                    matched += 1
            except (ValueError, KeyError):
                pass
    return matched / total if total else 0.0


# === block: score_2 (check id='step_04_gamma_adsorption_energies') ===
def score_2(artifact, step, ctx):
    rows_gold = step['gold']['rows']
    tol = step['gold']['tolerances']['Eads']
    trend_check = step['gold'].get('trend_check', False)
    numeric_total = len(rows_gold) * 2
    numeric_ok = 0
    trend_ok = True
    for row in artifact:
        adsorbate = row.get('adsorbate')
        gold = next((g for g in rows_gold if g['adsorbate'] == adsorbate), None)
        if gold is None:
            continue
        try:
            eg = float(row['Eads_gas'])
            el = float(row['Eads_liquid'])
        except (ValueError, KeyError):
            continue
        if abs(eg - gold['Eads_gas']) <= tol:
            numeric_ok += 1
        if abs(el - gold['Eads_liquid']) <= tol:
            numeric_ok += 1
        if trend_check and el <= eg:
            trend_ok = False
    numeric_score = numeric_ok / numeric_total if numeric_total else 0.0
    trend_score = 1.0 if trend_ok else 0.0
    return numeric_score * 0.8 + trend_score * 0.2


# === block: score_3 (check id='step_05_boehmite_adsorption_energies') ===
def score_3(artifact, step, ctx):
    rows_gold = step['gold']['rows']
    tol = step['gold']['tolerances']['Eads']
    trend_check = step['gold'].get('trend_check', False)
    numeric_total = len(rows_gold) * 2
    numeric_ok = 0
    trend_ok = True
    for row in artifact:
        adsorbate = row.get('adsorbate')
        gold = next((g for g in rows_gold if g['adsorbate'] == adsorbate), None)
        if gold is None:
            continue
        try:
            eg = float(row['Eads_gas'])
            el = float(row['Eads_liquid'])
        except (ValueError, KeyError):
            continue
        if abs(eg - gold['Eads_gas']) <= tol:
            numeric_ok += 1
        if abs(el - gold['Eads_liquid']) <= tol:
            numeric_ok += 1
        if trend_check and el <= eg:
            trend_ok = False
    numeric_score = numeric_ok / numeric_total if numeric_total else 0.0
    trend_score = 1.0 if trend_ok else 0.0
    return numeric_score * 0.8 + trend_score * 0.2


# === block: score_4 (check id='step_06_gamma_reaction_profile') ===
def score_4(artifact, step, ctx):
    gold_vals = step['gold']['values']
    tol = step['gold']['tolerance']
    pref_rules = step['gold']['preferred_rules']
    paths = ['path_I', 'path_II', 'path_III']
    numeric_total = len(paths) * 2
    numeric_ok = 0
    for p in paths:
        if p not in artifact:
            continue
        path_data = artifact[p]
        gold = gold_vals[p]
        for phase in ['Ea_gas', 'Ea_liquid']:
            try:
                val = float(path_data[phase])
                if abs(val - gold[phase]) <= tol:
                    numeric_ok += 1
            except (ValueError, KeyError):
                pass
    numeric_score = numeric_ok / numeric_total if numeric_total else 0.0
    def check_pref(label, required):
        if not isinstance(label, str):
            return False
        lower = label.lower()
        return all(r.lower() in lower for r in required)
    pref_gas = artifact.get('preferred_path_gas', '')
    pref_liq = artifact.get('preferred_path_liquid', '')
    path_match = (1 if check_pref(pref_gas, pref_rules['gas']) else 0) + (1 if check_pref(pref_liq, pref_rules['liquid']) else 0)
    path_score = path_match / 2.0
    return numeric_score * 0.5 + path_score * 0.5


# === block: score_5 (check id='step_07_boehmite_reaction_profile') ===
def score_5(artifact, step, ctx):
    gold_vals = step['gold']['values']
    tol = step['gold']['tolerance']
    pref_rules = step['gold']['preferred_rules']
    paths = ['path_I', 'path_II', 'path_III']
    numeric_total = len(paths) * 2
    numeric_ok = 0
    for p in paths:
        if p not in artifact:
            continue
        path_data = artifact[p]
        gold = gold_vals[p]
        for phase in ['Ea_gas', 'Ea_liquid']:
            try:
                val = float(path_data[phase])
                if abs(val - gold[phase]) <= tol:
                    numeric_ok += 1
            except (ValueError, KeyError):
                pass
    numeric_score = numeric_ok / numeric_total if numeric_total else 0.0
    def check_pref(label, required):
        if not isinstance(label, str):
            return False
        lower = label.lower()
        return all(r.lower() in lower for r in required)
    pref_gas = artifact.get('preferred_path_gas', '')
    pref_liq = artifact.get('preferred_path_liquid', '')
    path_match = (1 if check_pref(pref_gas, pref_rules['gas']) else 0) + (1 if check_pref(pref_liq, pref_rules['liquid']) else 0)
    path_score = path_match / 2.0
    return numeric_score * 0.5 + path_score * 0.5


_SCORERS = {
    'step_02_gamma_surface_relaxation': score_0,
    'step_03_boehmite_surface_relaxation': score_1,
    'step_04_gamma_adsorption_energies': score_2,
    'step_05_boehmite_adsorption_energies': score_3,
    'step_06_gamma_reaction_profile': score_4,
    'step_07_boehmite_reaction_profile': score_5,
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
