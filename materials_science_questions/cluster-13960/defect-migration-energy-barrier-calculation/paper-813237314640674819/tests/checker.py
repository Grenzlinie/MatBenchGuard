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


# === block: score_0 (check id='lattice') ===
def score_0(artifact, step, ctx):
    val = artifact.get('lattice_parameter_A')
    if val is None: return 0.0
    diff = abs(val - step['target_value'])
    return 1.0 if diff <= step['tolerance'] else 0.0


# === block: score_1 (check id='vacancy_N') ===
def score_1(artifact, step, ctx):
    val = artifact.get('vacancy_formation_N_eV')
    if val is None: return 0.0
    diff = abs(val - step['target_value'])
    return 1.0 if diff <= step['tolerance'] else 0.0


# === block: score_2 (check id='vacancy_Zr') ===
def score_2(artifact, step, ctx):
    val = artifact.get('vacancy_formation_Zr_eV')
    if val is None: return 0.0
    diff = abs(val - step['target_value'])
    return 1.0 if diff <= step['tolerance'] else 0.0


# === block: score_3 (check id='bind_N') ===
def score_3(artifact, step, ctx):
    field = step['field']
    targets = step['targets']
    tol = step['tolerance']
    obj = artifact.get(field)
    if not isinstance(obj, dict):
        return 0.0
    scores = []
    for key, target in targets.items():
        if key not in obj:
            scores.append(0.0)
        else:
            diff = abs(obj[key] - target)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff/(3*tol))))
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_4 (check id='bind_Zr') ===
def score_4(artifact, step, ctx):
    field = step['field']
    targets = step['targets']
    tol = step['tolerance']
    obj = artifact.get(field)
    if not isinstance(obj, dict):
        return 0.0
    scores = []
    for key, target in targets.items():
        if key not in obj:
            scores.append(0.0)
        else:
            diff = abs(obj[key] - target)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff/(3*tol))))
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_5 (check id='inter_em') ===
def score_5(artifact, step, ctx):
    field = step['field']
    targets = step['targets']
    tol = step['tolerance']
    obj = artifact.get(field)
    if not isinstance(obj, dict):
        return 0.0
    scores = []
    for key, target in targets.items():
        if key not in obj:
            scores.append(0.0)
        else:
            diff = abs(obj[key] - target)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff/(3*tol))))
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_6 (check id='vac_aid_em') ===
def score_6(artifact, step, ctx):
    field = step['field']
    targets = step['targets']
    tol = step['tolerance']
    obj = artifact.get(field)
    if not isinstance(obj, dict):
        return 0.0
    scores = []
    for key, target in targets.items():
        if key not in obj:
            scores.append(0.0)
        else:
            diff = abs(obj[key] - target)
            if diff <= tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (diff/(3*tol))))
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_7 (check id='trends') ===
def score_7(artifact, step, ctx):
    t = artifact
    checks = step.get('checks', [])
    if not checks:
        return 1.0
    results = []
    for check in checks:
        if check == 'interstitial_order':
            inter = t.get('interstitial_migration_barriers_eV', {})
            if all(k in inter for k in ['He','Kr','Xe']):
                results.append(1.0 if inter['He'] < inter['Kr'] and inter['He'] < inter['Xe'] else 0.0)
            else:
                results.append(0.0)
        elif check == 'vacancy_aided_order':
            va = t.get('vacancy_aided_migration_barriers_eV', {})
            if all(k in va for k in ['He','Kr','Xe']):
                results.append(1.0 if va['He'] < va['Kr'] and va['He'] < va['Xe'] else 0.0)
            else:
                results.append(0.0)
        elif check == 'binding_order_N':
            be = t.get('binding_energies_to_N_vac_eV', {})
            if all(k in be for k in ['He','Kr','Xe']):
                results.append(1.0 if be['He'] > be['Kr'] and be['He'] > be['Xe'] else 0.0)
            else:
                results.append(0.0)
        elif check == 'binding_order_Zr':
            be = t.get('binding_energies_to_Zr_vac_eV', {})
            if all(k in be for k in ['He','Kr','Xe']):
                results.append(1.0 if be['He'] > be['Kr'] and be['He'] > be['Xe'] else 0.0)
            else:
                results.append(0.0)
        else:
            results.append(1.0)
    return sum(results)/len(results) if results else 1.0


_SCORERS = {
    'lattice': score_0,
    'vacancy_N': score_1,
    'vacancy_Zr': score_2,
    'bind_N': score_3,
    'bind_Zr': score_4,
    'inter_em': score_5,
    'vac_aid_em': score_6,
    'trends': score_7,
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
