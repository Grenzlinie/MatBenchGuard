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


# === block: score_0 (check id='distances') ===
def score_0(artifact, step, ctx):
    # distances scorer
    if not isinstance(artifact, dict):
        return 0.0
    distances = artifact.get('distances', {})
    gold = step.get('gold', {})
    tol = step.get('tolerances', {}).get('default', 0.02)
    total = 0
    passed = 0
    for complex_name, expected in gold.items():
        actual_complex = distances.get(complex_name)
        if not isinstance(actual_complex, dict):
            continue
        for key, exp_val in expected.items():
            total += 1
            actual_val = actual_complex.get(key)
            if actual_val is not None and abs(actual_val - exp_val) <= tol:
                passed += 1
    return passed / max(total, 1)


# === block: score_1 (check id='bond_energies') ===
def score_1(artifact, step, ctx):
    # bond_energies scorer
    if not isinstance(artifact, dict):
        return 0.0
    energies = artifact.get('bond_energies', {})
    gold = step.get('gold', {})
    tol = step.get('tolerance', 10.0)
    total = 0
    passed = 0
    for complex_name, exp_val in gold.items():
        total += 1
        actual_val = energies.get(complex_name)
        if actual_val is not None and abs(actual_val - exp_val) <= tol:
            passed += 1
    return passed / max(total, 1)


# === block: score_2 (check id='charges') ===
def score_2(artifact, step, ctx):
    # charges scorer
    if not isinstance(artifact, dict):
        return 0.0
    charges = artifact.get('charges', {})
    gold = step.get('gold', {})
    tol = step.get('tolerance', 0.02)
    total = 0
    passed = 0
    for complex_name, expected in gold.items():
        actual_complex = charges.get(complex_name)
        if not isinstance(actual_complex, dict):
            continue
        for key, exp_val in expected.items():
            total += 1
            actual_val = actual_complex.get(key)
            if actual_val is not None and abs(actual_val - exp_val) <= tol:
                passed += 1
    return passed / max(total, 1)


# === block: score_3 (check id='structural_trends') ===
def score_3(artifact, step, ctx):
    # structural_trends scorer
    if not isinstance(artifact, dict):
        return 0.0
    distances = artifact.get('distances', {})
    charges = artifact.get('charges', {})
    sub_score = 0.0
    n = 3
    # trend 1: O-O distance ordering Gly > Cys > His
    try:
        d_his = distances['Heme+His+O2']['O1-O2']
        d_cys = distances['Heme+Cys+O2']['O1-O2']
        d_gly = distances['Heme+Gly+O2']['O1-O2']
        if d_gly > d_cys > d_his:
            sub_score += 1
    except:
        pass
    # trend 2: Fe charge more negative for His+O2 than Cys+O2
    try:
        fe_his = charges['Heme+His+O2']['Fe']
        fe_cys = charges['Heme+Cys+O2']['Fe']
        if fe_his < fe_cys:
            sub_score += 1
    except:
        pass
    # trend 3: O2 polarization only His+O2 (opposite signs on O1 and O2)
    try:
        his_o1 = charges['Heme+His+O2']['O1']
        his_o2 = charges['Heme+His+O2']['O2']
        cys_o1 = charges['Heme+Cys+O2']['O1']
        cys_o2 = charges['Heme+Cys+O2']['O2']
        gly_o1 = charges['Heme+Gly+O2']['O1']
        gly_o2 = charges['Heme+Gly+O2']['O2']
        his_polar = (his_o1 > 0 and his_o2 < 0) or (his_o1 < 0 and his_o2 > 0)
        cys_polar = (cys_o1 > 0 and cys_o2 < 0) or (cys_o1 < 0 and cys_o2 > 0)
        gly_polar = (gly_o1 > 0 and gly_o2 < 0) or (gly_o1 < 0 and gly_o2 > 0)
        if his_polar and not cys_polar and not gly_polar:
            sub_score += 1
    except:
        pass
    return sub_score / n


_SCORERS = {
    'distances': score_0,
    'bond_energies': score_1,
    'charges': score_2,
    'structural_trends': score_3,
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
