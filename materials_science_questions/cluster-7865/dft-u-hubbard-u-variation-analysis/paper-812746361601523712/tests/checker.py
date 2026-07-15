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


# === block: score_0 (check id='yb_structural') ===
def score_0(artifact, step, ctx):
    data = artifact.get('Yb3Pd2Sn2')
    if not data:
        return 0.0
    gold = step['gold']
    tolerances = step['tolerances']
    def rel_err(val, ref, tol):
        if ref == 0:
            return abs(val) <= tol
        return abs((val - ref) / ref) <= tol
    def abs_err(val, ref, tol):
        return abs(val - ref) <= tol
    checks = [
        ('V', 'relative'),
        ('a', 'relative'),
        ('b', 'relative'),
        ('c', 'relative'),
        ('c_over_a', 'absolute'),
        ('b_over_a', 'absolute'),
        ('B', 'relative'),
        ('B_prime', 'relative')
    ]
    passed = 0
    for key, tol_type in checks:
        val = data.get(key)
        ref = gold.get(key)
        if val is not None and ref is not None:
            tol = tolerances[key]['value']
            if tol_type == 'relative':
                if rel_err(val, ref, tol):
                    passed += 1
            else:
                if abs_err(val, ref, tol):
                    passed += 1
    return passed / len(checks)


# === block: score_1 (check id='eu_structural') ===
def score_1(artifact, step, ctx):
    data = artifact.get('Eu3Pd2Sn2')
    if not data:
        return 0.0
    gold = step['gold']
    tolerances = step['tolerances']
    def rel_err(val, ref, tol):
        if ref == 0:
            return abs(val) <= tol
        return abs((val - ref) / ref) <= tol
    def abs_err(val, ref, tol):
        return abs(val - ref) <= tol
    checks = [
        ('V', 'relative'),
        ('a', 'relative'),
        ('b', 'relative'),
        ('c', 'relative'),
        ('c_over_a', 'absolute'),
        ('b_over_a', 'absolute'),
        ('B', 'relative'),
        ('B_prime', 'relative')
    ]
    passed = 0
    for key, tol_type in checks:
        val = data.get(key)
        ref = gold.get(key)
        if val is not None and ref is not None:
            tol = tolerances[key]['value']
            if tol_type == 'relative':
                if rel_err(val, ref, tol):
                    passed += 1
            else:
                if abs_err(val, ref, tol):
                    passed += 1
    return passed / len(checks)


# === block: score_2 (check id='yb_mag') ===
def score_2(artifact, step, ctx):
    data = artifact.get('Yb3Pd2Sn2')
    if not data:
        return 0.0
    total = data.get('total_magnetic_moment')
    atom = data.get('atomic_magnetic_moments')
    gold_total = step['gold_total']
    gold_atom = step['gold_atomic']
    tol = step['tolerance']
    passed = 0
    if total is not None and abs(total - gold_total) <= tol:
        passed += 1
    if isinstance(atom, list) and len(atom) == len(gold_atom):
        for a, b in zip(atom, gold_atom):
            if abs(a - b) <= tol:
                passed += 1
    return passed / (1 + len(gold_atom))


# === block: score_3 (check id='eu_mag') ===
def score_3(artifact, step, ctx):
    data = artifact.get('Eu3Pd2Sn2')
    if not data:
        return 0.0
    total = data.get('total_magnetic_moment')
    atom = data.get('atomic_magnetic_moments')
    gold_total = step['gold_total']
    gold_atom = step['gold_atomic']
    tol = step['tolerance']
    passed = 0
    if total is not None and abs(total - gold_total) <= tol:
        passed += 1
    if isinstance(atom, list) and len(atom) == len(gold_atom):
        for a, b in zip(atom, gold_atom):
            if abs(a - b) <= tol:
                passed += 1
    return passed / (1 + len(gold_atom))


# === block: score_4 (check id='eu_ground_state') ===
def score_4(artifact, step, ctx):
    data = artifact.get('Eu3Pd2Sn2')
    if not data:
        return 0.0
    gs = data.get('magnetic_ground_state')
    fm = data.get('FM_energy')
    afm1 = data.get('AFM1_energy')
    afm2 = data.get('AFM2_energy')
    if gs == 'FM' and fm is not None and afm1 is not None and afm2 is not None:
        if fm < afm1 and fm < afm2:
            return 1.0
    return 0.0


# === block: score_5 (check id='consistency') ===
def score_5(artifact, step, ctx):
    data_yb = artifact.get('Yb3Pd2Sn2')
    data_eu = artifact.get('Eu3Pd2Sn2')
    tol = step.get('tolerance', 0.001)
    score = 0.0
    for data in [data_yb, data_eu]:
        if not data:
            continue
        V = data.get('V')
        a = data.get('a')
        ca = data.get('c_over_a')
        ba = data.get('b_over_a')
        if V is not None and a is not None and ca is not None and ba is not None and a != 0:
            V_check = ca * ba * a**3
            if abs(V_check - V) / V <= tol:
                score += 0.5
    return score


_SCORERS = {
    'yb_structural': score_0,
    'eu_structural': score_1,
    'yb_mag': score_2,
    'eu_mag': score_3,
    'eu_ground_state': score_4,
    'consistency': score_5,
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
