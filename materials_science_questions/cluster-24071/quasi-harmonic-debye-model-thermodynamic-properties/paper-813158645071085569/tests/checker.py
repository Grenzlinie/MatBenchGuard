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


# === block: score_0 (check id='step_02_elastic') ===
def score_0(artifact, step, ctx):
    gold_phases = step['gold']
    phases = artifact.get('phases', [])
    if not phases:
        return 0.0
    tols = step.get('tolerances', {})
    tol_C = tols.get('C', 0.05)
    tol_moduli = tols.get('moduli', 0.10)
    tol_lattice = tols.get('lattice', 0.01)
    total_score = 0.0
    count = 0
    for name, gp in gold_phases.items():
        match = None
        for p in phases:
            if p.get('name') == name:
                match = p
                break
        if match is None:
            # missing phase: add zero contributions for all fields
            n_fields = sum(1 for f in gp if f != 'name')
            count += n_fields
            continue
        for field, gold_val in gp.items():
            if field == 'name':
                continue
            if field == 'C66' and field not in match:
                continue  # ok missing for α-Zr
            actual = match.get(field)
            if actual is None:
                return 0.0
            if field.startswith('C'):
                tol = tol_C
            elif field in ('E','B','G'):
                tol = tol_moduli
            else:
                tol = tol_lattice
            if gold_val == 0.0:
                score_val = 1.0 if abs(actual) < 1e-6 else 0.0
            else:
                rel_err = abs(actual - gold_val) / abs(gold_val)
                score_val = max(0.0, 1.0 - rel_err / tol)
            total_score += score_val
            count += 1
    if count == 0:
        return 1.0
    return total_score / count


# === block: score_1 (check id='step_03_thermo') ===
def score_1(artifact, step, ctx):
    gold_phases = step['gold']
    phases = artifact.get('phases', [])
    if not phases:
        return 0.0
    tols = step.get('tolerances', {})
    tol_arr = tols.get('entropy', {'rel':0.10, 'abs':5.0})
    tol_cp = tols.get('heat_capacity', {'rel':0.10, 'abs':5.0})
    tol_h = tols.get('enthalpy', {'rel':0.10, 'abs':5.0})
    tol_single = tols.get('single', {'rel':0.10})
    total_score = 0.0
    count = 0
    for name, gp in gold_phases.items():
        match = None
        for p in phases:
            if p.get('name') == name:
                match = p
                break
        if match is None:
            return 0.0
        # arrays: compare at indices 3,5,10 (300K,500K,1000K)
        for arr_key, tol_info in [('entropy', tol_arr), ('heat_capacity', tol_cp), ('enthalpy', tol_h)]:
            arr = match.get(arr_key)
            gold_arr = gp[arr_key]
            if not arr or len(arr) < 11 or not gold_arr:
                return 0.0
            for idx in (3,5,10):
                actual = arr[idx]
                gold_val = gold_arr[idx]
                if gold_val == 0.0:
                    s = 1.0 if abs(actual) < 1e-6 else 0.0
                else:
                    allowed = max(abs(gold_val) * tol_info['rel'], tol_info['abs'])
                    err = abs(actual - gold_val)
                    s = max(0.0, 1.0 - err / allowed)
                total_score += s
                count += 1
        # singles
        for key in ('enthalpy_of_formation', 'Debye_temperature', 'electronic_heat_constant'):
            actual = match.get(key)
            gold_val = gp[key]
            if actual is None or gold_val is None:
                return 0.0
            if gold_val == 0.0:
                s = 1.0 if abs(actual) < 1e-6 else 0.0
            else:
                allowed = abs(gold_val) * tol_single['rel']
                err = abs(actual - gold_val)
                s = max(0.0, 1.0 - err / allowed)
            total_score += s
            count += 1
    if count == 0:
        return 1.0
    return total_score / count


_SCORERS = {
    'step_02_elastic': score_0,
    'step_03_thermo': score_1,
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
