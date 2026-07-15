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


# === block: score_0 (check id='base_case_e11') ===
def score_0(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.15)
    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_1 (check id='base_case_e22') ===
def score_1(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.2)
    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_2 (check id='base_case_e33') ===
def score_2(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.2)
    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_3 (check id='base_case_g12') ===
def score_3(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict):
                return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None:
        return 0.0

    # Correct effective shear modulus G12 for fractures normal to x
    E_matrix = 100e9
    nu_matrix = 0.3
    ks = 10e9  # kn/2, in Pa/m
    spacing = 1.0 / 3.0

    G_matrix = E_matrix / (2.0 * (1.0 + nu_matrix))
    G12_eff = 1.0 / (1.0 / G_matrix + 1.0 / (ks * spacing))

    target = G12_eff
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.2)

    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_4 (check id='base_case_g13') ===
def score_4(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict):
                return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None:
        return 0.0

    # Correct effective shear modulus G13 for fractures normal to x
    E_matrix = 100e9
    nu_matrix = 0.3
    ks = 10e9  # kn/2, in Pa/m
    spacing = 1.0 / 3.0

    G_matrix = E_matrix / (2.0 * (1.0 + nu_matrix))
    G13_eff = 1.0 / (1.0 / G_matrix + 1.0 / (ks * spacing))

    target = G13_eff
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.2)

    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_5 (check id='base_case_g23') ===
def score_5(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.2)
    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_6 (check id='nonzero_nu_case_e11') ===
def score_6(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    full_tol = step.get('full_tol_rel', 0.05)
    max_tol = step.get('max_tol_rel', 0.15)
    rel_err = abs(val - target) / target if target else 0.0
    if rel_err <= full_tol:
        return 1.0
    if rel_err >= max_tol:
        return 0.0
    return (max_tol - rel_err) / (max_tol - full_tol)


# === block: score_7 (check id='nonzero_e11_increase') ===
def score_7(artifact, step, ctx):
    base = artifact.get('base_case', {})
    nonzero = artifact.get('nonzero_nu_case', {})
    val_base = base.get('E11')
    val_nonzero = nonzero.get('E11')
    if val_base is None or val_nonzero is None:
        return 0.0
    if val_base <= 0:
        return 0.0
    inc_rel = (val_nonzero - val_base) / val_base
    if inc_rel >= step.get('min_increase_rel', 0.20):
        return 1.0
    return 0.0


# === block: score_8 (check id='percent_change_consistency') ===
def score_8(artifact, step, ctx):
    reported = artifact.get('percent_change_E11')
    base = artifact.get('base_case', {})
    nonzero = artifact.get('nonzero_nu_case', {})
    val_base = base.get('E11')
    val_nonzero = nonzero.get('E11')
    if reported is None or val_base is None or val_nonzero is None:
        return 0.0
    computed = 100.0 * (val_nonzero - val_base) / val_base
    if abs(reported - computed) <= 0.005 * abs(computed):
        return 1.0
    return 0.0


# === block: score_9 (check id='base_case_fracture_nu') ===
def score_9(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    return 1.0 if abs(val - target) < 1e-12 else 0.0


# === block: score_10 (check id='nonzero_nu_case_fracture_nu') ===
def score_10(artifact, step, ctx):
    def get_path(obj, path):
        parts = path.split('.')
        for p in parts:
            if not isinstance(obj, dict): return None
            obj = obj.get(p)
        return obj

    val = get_path(artifact, step['json_path'])
    if val is None: return 0.0
    target = step['target']
    return 1.0 if abs(val - target) < 1e-12 else 0.0


_SCORERS = {
    'base_case_e11': score_0,
    'base_case_e22': score_1,
    'base_case_e33': score_2,
    'base_case_g12': score_3,
    'base_case_g13': score_4,
    'base_case_g23': score_5,
    'nonzero_nu_case_e11': score_6,
    'nonzero_e11_increase': score_7,
    'percent_change_consistency': score_8,
    'base_case_fracture_nu': score_9,
    'nonzero_nu_case_fracture_nu': score_10,
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
