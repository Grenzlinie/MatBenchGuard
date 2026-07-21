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


# === block: score_0 (check id='e_ad_h2') ===
def score_0(artifact, step, ctx):
    te = artifact.get('total_energies', {})
    if not all(k in te for k in ['h2_ti2n','h2','ti2n']):
        return 0.0
    e_ad = te['h2_ti2n'] - te['h2'] - te['ti2n']
    target = step.get('target', -2.964)
    tol = step.get('tolerance', 0.1)
    return 1.0 if abs(e_ad - target) <= tol else 0.0


# === block: score_1 (check id='e_ad_ch4') ===
def score_1(artifact, step, ctx):
    te = artifact.get('total_energies', {})
    if not all(k in te for k in ['ch4_ti2n','ch4','ti2n']):
        return 0.0
    e_ad = te['ch4_ti2n'] - te['ch4'] - te['ti2n']
    target = step.get('target', -0.214)
    tol = step.get('tolerance', 0.1)
    return 1.0 if abs(e_ad - target) <= tol else 0.0


# === block: score_2 (check id='e_ad_c2h2') ===
def score_2(artifact, step, ctx):
    te = artifact.get('total_energies', {})
    if not all(k in te for k in ['c2h2_ti2n','c2h2','ti2n']):
        return 0.0
    e_ad = te['c2h2_ti2n'] - te['c2h2'] - te['ti2n']
    target = step.get('target', -5.527)
    tol = step.get('tolerance', 0.1)
    return 1.0 if abs(e_ad - target) <= tol else 0.0


# === block: score_3 (check id='structural_checks') ===
def score_3(artifact, step, ctx):
    te = artifact.get('total_energies', {})
    if not all(k in te for k in ['h2_ti2n','h2','ti2n','ch4_ti2n','ch4','c2h2_ti2n','c2h2']):
        return 0.0
    e_ad_h2 = te['h2_ti2n'] - te['h2'] - te['ti2n']
    e_ad_ch4 = te['ch4_ti2n'] - te['ch4'] - te['ti2n']
    e_ad_c2h2 = te['c2h2_ti2n'] - te['c2h2'] - te['ti2n']
    bl = artifact.get('bond_lengths', {})
    thr = step.get('thresholds', {})
    passed = 0
    total = 5
    if abs(e_ad_h2) > thr.get('h2_abs_gt', 2.0):
        passed += 1
    if abs(e_ad_c2h2) > thr.get('c2h2_abs_gt', 4.0):
        passed += 1
    if abs(e_ad_ch4) < thr.get('ch4_abs_lt', 0.5):
        passed += 1
    if 'H2_HH' in bl and bl['H2_HH'] > thr.get('h2_hh_gt', 2.5):
        passed += 1
    if 'C2H2_CC' in bl and bl['C2H2_CC'] > thr.get('c2h2_cc_gt', 1.2):
        passed += 1
    return passed / total


# === block: score_4 (check id='charge_transfers') ===
def score_4(artifact, step, ctx):
    ct = artifact.get('charge_transfers', {})
    required = ['H2','CH4','C2H2']
    if not all(k in ct for k in required):
        return 0.0
    targets = step.get('targets', {})
    tol = step.get('tolerance', 0.03)
    passed = sum(1 for k in required if abs(ct[k] - targets.get(k, 0.0)) <= tol)
    return passed / len(required)


_SCORERS = {
    'e_ad_h2': score_0,
    'e_ad_ch4': score_1,
    'e_ad_c2h2': score_2,
    'structural_checks': score_3,
    'charge_transfers': score_4,
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
