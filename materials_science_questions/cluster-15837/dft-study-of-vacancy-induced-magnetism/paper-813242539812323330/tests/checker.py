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


# === block: score_0 (check id='magnetic_moments') ===
def score_0(artifact, step, ctx):
    # Read artifact JSON, step has 'systems' dict and 'fields' list.
    artifact_dict = artifact   # already loaded JSON object
    systems = step.get('systems', {})
    fields = step.get('fields', [])
    tol = step.get('tolerance', 0.2)
    correct = 0
    total = 0
    for sys_name, gold_vals in systems.items():
        if sys_name not in artifact_dict:
            continue
        sys_data = artifact_dict[sys_name]
        for field in fields:
            total += 1
            if field in sys_data and isinstance(sys_data[field], (int, float)):
                val = sys_data[field]
                gold = gold_vals.get(field)
                if gold is not None and abs(val - gold) <= tol:
                    correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='off_center') ===
def score_1(artifact, step, ctx):
    # Read artifact JSON, step has 'target' and 'tolerance'.
    disp = artifact.get('displacement_A')
    if not isinstance(disp, (int, float)):
        return 0.0
    target = step.get('target', 0.9)
    tol = step.get('tolerance', 0.1)
    return 1.0 if abs(disp - target) <= tol else 0.0


# === block: score_2 (check id='polarizability') ===
def score_2(artifact, step, ctx):
    # Read artifact JSON, step has 'fields' dict with per-field target and tolerance.
    fields_info = step.get('fields', {})
    total_checks = len(fields_info)
    passed = 0
    for field_name, spec in fields_info.items():
        value = artifact.get(field_name)
        if not isinstance(value, (int, float)):
            continue
        if 'tolerance_rel' in spec:
            target = spec['target']
            tol = spec['tolerance_rel'] * abs(target)
            if abs(value - target) <= tol:
                passed += 1
        elif 'tolerance_abs' in spec:
            target = spec['target']
            tol = spec['tolerance_abs']
            if abs(value - target) <= tol:
                passed += 1
    if total_checks == 0:
        return 0.0
    return passed / total_checks


# === block: score_3 (check id='transmission') ===
def score_3(artifact, step, ctx):
    # Read CSV rows, step has criteria dict.
    criteria = step.get('criteria', {})
    score = 0.0
    # shape check: columns present
    required_cols = ['energy_eV', 'transmission_up', 'transmission_down']
    if not artifact or not isinstance(artifact, list):
        return 0.0
    first_row = artifact[0] if artifact else {}
    cols_ok = all(c in first_row for c in required_cols)
    if not cols_ok:
        return 0.0
    score += 0.2
    # row count
    min_rows = criteria.get('min_rows', 100)
    if len(artifact) < min_rows:
        return score  # 0.2 only
    score += 0.2
    # energy range
    energies = []
    for row in artifact:
        try:
            e = float(row['energy_eV'])
        except (ValueError, TypeError):
            continue
        energies.append(e)
    if energies:
        emin = min(energies)
        emax = max(energies)
        if emin <= criteria.get('energy_min', -1.0) and emax >= criteria.get('energy_max', 1.0):
            score += 0.2
    else:
        return score
    # non-negative transmission
    neg_found = False
    for row in artifact:
        try:
            tup = float(row['transmission_up'])
            tdown = float(row['transmission_down'])
        except (ValueError, TypeError):
            neg_found = True
            break
        if tup < -1e-9 or tdown < -1e-9:
            neg_found = True
            break
    if not neg_found:
        score += 0.2
    # spin-polarization absence (mean absolute difference)
    spin_diffs = []
    for row in artifact:
        try:
            tup = float(row['transmission_up'])
            tdown = float(row['transmission_down'])
        except (ValueError, TypeError):
            continue
        spin_diffs.append(abs(tup - tdown))
    if spin_diffs:
        mean_diff = sum(spin_diffs) / len(spin_diffs)
        if mean_diff <= criteria.get('spin_diff_threshold', 0.01):
            score += 0.2
    return score


_SCORERS = {
    'magnetic_moments': score_0,
    'off_center': score_1,
    'polarizability': score_2,
    'transmission': score_3,
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
