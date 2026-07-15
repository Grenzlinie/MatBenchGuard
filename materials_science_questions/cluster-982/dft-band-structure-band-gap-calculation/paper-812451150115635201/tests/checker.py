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


# === block: score_0 (check id='rutile_TM_props') ===
def score_0(artifact, step, ctx):
    try:
        data = artifact.get('rutile_TM', {})
        gold = step['config']['gold']
        tols = step['config']['tolerances']
        checks = []
        checks.append(abs(data['a'] - gold['a']) <= gold['a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c'] - gold['c']) <= gold['c'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c_over_a'] - gold['c_over_a']) <= gold['c_over_a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['u'] - gold['u']) <= tols['abs_tol_u'])
        checks.append(abs(data['density'] - gold['density']) <= gold['density'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['bulk_modulus'] - gold['bulk_modulus']) <= tols['abs_tol_B'])
        checks.append(abs(data['band_gap'] - gold['band_gap']) <= tols['abs_tol_gap'])
        checks.append(data['gap_direct'] == gold['gap_direct'])
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


# === block: score_1 (check id='rutile_Teter_props') ===
def score_1(artifact, step, ctx):
    try:
        data = artifact.get('rutile_Teter', {})
        gold = step['config']['gold']
        tols = step['config']['tolerances']
        checks = []
        checks.append(abs(data['a'] - gold['a']) <= gold['a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c'] - gold['c']) <= gold['c'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c_over_a'] - gold['c_over_a']) <= gold['c_over_a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['u'] - gold['u']) <= tols['abs_tol_u'])
        checks.append(abs(data['density'] - gold['density']) <= gold['density'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['bulk_modulus'] - gold['bulk_modulus']) <= tols['abs_tol_B'])
        checks.append(abs(data['band_gap'] - gold['band_gap']) <= tols['abs_tol_gap'])
        checks.append(data['gap_direct'] == gold['gap_direct'])
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


# === block: score_2 (check id='anatase_TM_props') ===
def score_2(artifact, step, ctx):
    try:
        data = artifact.get('anatase_TM', {})
        gold = step['config']['gold']
        tols = step['config']['tolerances']
        checks = []
        checks.append(abs(data['a'] - gold['a']) <= gold['a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c'] - gold['c']) <= gold['c'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c_over_a'] - gold['c_over_a']) <= gold['c_over_a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['u'] - gold['u']) <= tols['abs_tol_u'])
        checks.append(abs(data['density'] - gold['density']) <= gold['density'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['bulk_modulus'] - gold['bulk_modulus']) <= tols['abs_tol_B'])
        checks.append(abs(data['band_gap'] - gold['band_gap']) <= tols['abs_tol_gap'])
        checks.append(data['gap_direct'] == gold['gap_direct'])
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


# === block: score_3 (check id='anatase_Teter_props') ===
def score_3(artifact, step, ctx):
    try:
        data = artifact.get('anatase_Teter', {})
        gold = step['config']['gold']
        tols = step['config']['tolerances']
        checks = []
        checks.append(abs(data['a'] - gold['a']) <= gold['a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c'] - gold['c']) <= gold['c'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['c_over_a'] - gold['c_over_a']) <= gold['c_over_a'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['u'] - gold['u']) <= tols['abs_tol_u'])
        checks.append(abs(data['density'] - gold['density']) <= gold['density'] * tols['rel_tol'] + 1e-9)
        checks.append(abs(data['bulk_modulus'] - gold['bulk_modulus']) <= tols['abs_tol_B'])
        checks.append(abs(data['band_gap'] - gold['band_gap']) <= tols['abs_tol_gap'])
        checks.append(data['gap_direct'] == gold['gap_direct'])
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


# === block: score_4 (check id='energy_TM') ===
def score_4(artifact, step, ctx):
    try:
        data = artifact.get('energy_TM', {})
        gold = step['config']['gold']
        tols = step['config']['tolerances']
        checks = []
        # difference within tolerance
        checks.append(abs(data['difference_kcal_per_mol'] - gold['difference_kcal_per_mol']) <= tols['abs_tol_diff_kcal'])
        # sign convention string exact
        checks.append(data.get('difference_sign_convention', '') == gold['sign_convention'])
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


# === block: score_5 (check id='energy_Teter') ===
def score_5(artifact, step, ctx):
    try:
        data = artifact.get('energy_Teter', {})
        gold = step['config']['gold']
        tols = step['config']['tolerances']
        checks = []
        checks.append(abs(data['difference_kcal_per_mol'] - gold['difference_kcal_per_mol']) <= tols['abs_tol_diff_kcal'])
        checks.append(data.get('difference_sign_convention', '') == gold['sign_convention'])
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


# === block: score_6 (check id='directional_checks') ===
def score_6(artifact, step, ctx):
    try:
        checks = []
        # anatase band_gap > rutile band_gap (both pseudopotentials)
        checks.append(artifact['anatase_TM']['band_gap'] > artifact['rutile_TM']['band_gap'])
        checks.append(artifact['anatase_Teter']['band_gap'] > artifact['rutile_Teter']['band_gap'])
        # rutile bulk_modulus > anatase bulk_modulus
        checks.append(artifact['rutile_TM']['bulk_modulus'] > artifact['anatase_TM']['bulk_modulus'])
        checks.append(artifact['rutile_Teter']['bulk_modulus'] > artifact['anatase_Teter']['bulk_modulus'])
        # energy sign: TM diff <= 0, Teter diff >= 0
        checks.append(artifact['energy_TM']['difference_kcal_per_mol'] <= 0)
        checks.append(artifact['energy_Teter']['difference_kcal_per_mol'] >= 0)
        return sum(checks) / len(checks)
    except Exception:
        return 0.0


_SCORERS = {
    'rutile_TM_props': score_0,
    'rutile_Teter_props': score_1,
    'anatase_TM_props': score_2,
    'anatase_Teter_props': score_3,
    'energy_TM': score_4,
    'energy_Teter': score_5,
    'directional_checks': score_6,
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
