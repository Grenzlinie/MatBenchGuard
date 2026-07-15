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


# === block: score_0 (check id='bulk_surface') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict): return 0.0
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    fields = ['bulk_lattice_constant', 'surface_energy', 'vacancy_formation_energy']
    ok = 0
    total = len(fields)
    for key in fields:
        if key in data and key in gold:
            try:
                diff = abs(float(data[key]) - float(gold[key]))
                if diff <= tols.get(key, 0):
                    ok += 1
            except (ValueError, TypeError):
                pass
    return ok / max(total, 1)


# === block: score_1 (check id='adsorption_perfect') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list): return 0.0
    gold_rows = step.get('gold', {}).get('rows', [])
    tols = step.get('tolerances', {})
    gold_by_cfg = {r['config']: r for r in gold_rows}
    numeric_keys = ['E_ads', 'C_Oa', 'C_Ob', 'O_C_O_angle', 'Bader_charge']
    ok = 0
    total = len(gold_rows) * len(numeric_keys)
    for row in rows:
        cfg = row.get('config', '').strip()
        gold_row = gold_by_cfg.get(cfg)
        if gold_row is None:
            continue
        for key in numeric_keys:
            if key in row and key in gold_row:
                try:
                    diff = abs(float(row[key]) - float(gold_row[key]))
                    if diff <= tols.get(key, 0):
                        ok += 1
                except (ValueError, TypeError):
                    pass
    return ok / max(total, 1)


# === block: score_2 (check id='adsorption_defective') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list): return 0.0
    gold_rows = step.get('gold', {}).get('rows', [])
    tols = step.get('tolerances', {})
    gold_by_cfg = {r['config']: r for r in gold_rows}
    numeric_keys = ['E_ads', 'C_Oa', 'C_Ob', 'O_C_O_angle', 'Bader_charge']
    ok = 0
    total = len(gold_rows) * len(numeric_keys)
    for row in rows:
        cfg = row.get('config', '').strip()
        gold_row = gold_by_cfg.get(cfg)
        if gold_row is None:
            continue
        for key in numeric_keys:
            if key in row and key in gold_row:
                try:
                    diff = abs(float(row[key]) - float(gold_row[key]))
                    if diff <= tols.get(key, 0):
                        ok += 1
                except (ValueError, TypeError):
                    pass
    return ok / max(total, 1)


# === block: score_3 (check id='reaction_pathways') ===
def score_3(artifact, step, ctx):
    pathways = artifact
    if not isinstance(pathways, list): return 0.0
    gold_pws = step.get('gold', {}).get('pathways', [])
    tols = step.get('tolerances', {})
    gold_by_label = {p['pathway_label']: p for p in gold_pws}
    numeric_keys = ['reaction_energy', 'barrier']
    ok = 0
    total = len(gold_pws) * len(numeric_keys)
    for pw in pathways:
        lbl = pw.get('pathway_label', '').strip()
        gold_pw = gold_by_label.get(lbl)
        if gold_pw is None:
            continue
        for key in numeric_keys:
            if key in pw and key in gold_pw:
                try:
                    diff = abs(float(pw[key]) - float(gold_pw[key]))
                    if diff <= tols.get(key, 0):
                        ok += 1
                except (ValueError, TypeError):
                    pass
    return ok / max(total, 1)


_SCORERS = {
    'bulk_surface': score_0,
    'adsorption_perfect': score_1,
    'adsorption_defective': score_2,
    'reaction_pathways': score_3,
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
