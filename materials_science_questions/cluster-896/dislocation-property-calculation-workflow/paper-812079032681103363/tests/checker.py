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


# === block: score_0 (check id='elastic_constants') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tolerances = step.get('tolerances', {})
    total = len(gold)
    passed = 0
    for key, gval in gold.items():
        aval = artifact.get(key)
        if aval is None:
            continue
        try:
            aval = float(aval)
        except:
            continue
        tol_spec = tolerances.get(key, {})
        if 'abs' in tol_spec:
            if abs(aval - gval) <= tol_spec['abs']:
                passed += 1
        elif 'rel' in tol_spec:
            if abs(gval) < 1e-12:
                if abs(aval) <= 1e-12:
                    passed += 1
            else:
                if abs(aval - gval) / abs(gval) <= tol_spec['rel']:
                    passed += 1
    return passed / max(total, 1)


# === block: score_1 (check id='gsfe_fit_params') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tol_gamma = step['tolerances']['gamma_abs']
    tol_d1 = step['tolerances']['Delta1_abs']
    tol_d2 = step['tolerances']['Delta2_abs']
    total = 6
    passed = 0
    for case in ('relaxed', 'nonrelaxed'):
        gcase = gold.get(case, {})
        acase = artifact.get(case, {})
        for field_tol in [('gamma', tol_gamma), ('Delta1', tol_d1), ('Delta2', tol_d2)]:
            field, tol = field_tol
            gval = gcase.get(field)
            aval = acase.get(field)
            if aval is None:
                continue
            try:
                aval = float(aval)
            except:
                continue
            if abs(aval - gval) <= tol:
                passed += 1
    return passed / total


# === block: score_2 (check id='dislocation_properties') ===
def score_2(artifact, step, ctx):
    gold = step.get('gold', {})
    tol_hw = step['tolerances']['half_width_abs']
    tol_ps = step['tolerances']['peierls_stress_abs']
    fields = [
        ('relaxed_xi0', 'half_width', gold['relaxed_xi0']),
        ('relaxed_xi', 'half_width', gold['relaxed_xi']),
        ('nonrelaxed_xi', 'half_width', gold['nonrelaxed_xi']),
        ('relaxed_sigmaP0', 'stress', gold['relaxed_sigmaP0']),
        ('relaxed_sigmaP', 'stress', gold['relaxed_sigmaP']),
        ('nonrelaxed_sigmaP', 'stress', gold['nonrelaxed_sigmaP'])
    ]
    passed = 0
    for key, typ, gval in fields:
        aval = artifact.get(key)
        if aval is None:
            continue
        try:
            aval = float(aval)
        except:
            continue
        if typ == 'half_width':
            if abs(aval - gval) <= tol_hw:
                passed += 1
        else:
            if abs(aval - gval) <= tol_ps:
                passed += 1
    numeric_score = passed / float(len(fields))
    # structural trends
    trends = 0
    if artifact.get('relaxed_xi') is not None and artifact.get('nonrelaxed_xi') is not None:
        if float(artifact['relaxed_xi']) > float(artifact['nonrelaxed_xi']):
            trends += 1
    if artifact.get('relaxed_sigmaP') is not None and artifact.get('nonrelaxed_sigmaP') is not None:
        if float(artifact['relaxed_sigmaP']) < float(artifact['nonrelaxed_sigmaP']):
            trends += 1
    if (artifact.get('relaxed_xi') is not None and artifact.get('relaxed_xi0') is not None and
        artifact.get('relaxed_sigmaP') is not None and artifact.get('relaxed_sigmaP0') is not None):
        if float(artifact['relaxed_xi']) > float(artifact['relaxed_xi0']) and float(artifact['relaxed_sigmaP']) < float(artifact['relaxed_sigmaP0']):
            trends += 1
    combined = 0.7 * numeric_score + 0.3 * (trends / 3.0)
    return combined


_SCORERS = {
    'elastic_constants': score_0,
    'gsfe_fit_params': score_1,
    'dislocation_properties': score_2,
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
