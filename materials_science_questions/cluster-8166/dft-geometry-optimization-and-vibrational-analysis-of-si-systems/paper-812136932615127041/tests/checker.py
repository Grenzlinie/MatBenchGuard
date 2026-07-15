import os
import json
import csv

# === author imports / helpers ===
import os
import csv
import json


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


# === block: score_0 (check id='results_csv_shape') ===
def score_0(artifact, step, ctx):
    # Validate CSV shape: existence, required columns, all expected system rows.
    path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(path):
        return 0.0
    try:
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if not rows:
                return 0.0
            required_cols = {'system', 'formation_energy_eV', 'homo_eV', 'lumo_eV', 'effective_work_function_eV'}
            if not required_cols.issubset(rows[0].keys()):
                return 0.0
            systems = {row['system'] for row in rows}
            expected = set(step['expected_systems'])
            if expected.issubset(systems):
                return 1.0
            else:
                return 0.0
    except Exception:
        return 0.0


# === block: score_1 (check id='formation_energy') ===
def score_1(artifact, step, ctx):
    # Compare formation energy values to reference.
    path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(path):
        return 0.0
    try:
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        ref = step['reference']
        tol = step['tolerance_abs']
        total = len(ref)
        if total == 0:
            return 1.0
        correct = 0
        for row in rows:
            sys = row.get('system', '')
            if sys in ref:
                try:
                    val = float(row['formation_energy_eV'])
                    if abs(val - ref[sys]) <= tol:
                        correct += 1
                except (ValueError, KeyError):
                    pass
        return correct / total
    except Exception:
        return 0.0


# === block: score_2 (check id='homo') ===
def score_2(artifact, step, ctx):
    # Compare HOMO values to reference, only for systems for which the paper reported HOMO.
    path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(path):
        return 0.0
    # Define the set of system identifiers for which the paper explicitly reports HOMO.
    VALID_SYSTEMS = {'pure_5_5', 'model_I', 'model_IV', 'pure_9_0', 'model_V', 'model_VI'}
    try:
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        ref = step['reference']
        tol = step['tolerance_abs']
        # Filter reference to only those systems actually reported in the paper.
        filtered_ref = {sys: val for sys, val in ref.items() if sys in VALID_SYSTEMS}
        total = len(filtered_ref)
        if total == 0:
            return 1.0
        correct = 0
        for row in rows:
            sys = row.get('system', '')
            if sys in filtered_ref:
                try:
                    val = float(row['homo_eV'])
                    if abs(val - filtered_ref[sys]) <= tol:
                        correct += 1
                except (ValueError, KeyError):
                    pass
        return correct / total
    except Exception:
        return 0.0


# === block: score_3 (check id='lumo') ===
def score_3(artifact, step, ctx):
    # Compare LUMO values to reference, only for systems for which the paper reported LUMO.
    path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(path):
        return 0.0
    # Define the set of system identifiers for which the paper explicitly reports LUMO.
    VALID_SYSTEMS = {'pure_5_5', 'model_I', 'model_IV', 'pure_9_0', 'model_V', 'model_VI'}
    try:
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        ref = step['reference']
        tol = step['tolerance_abs']
        # Filter reference to only those systems actually reported in the paper.
        filtered_ref = {sys: val for sys, val in ref.items() if sys in VALID_SYSTEMS}
        total = len(filtered_ref)
        if total == 0:
            return 1.0
        correct = 0
        for row in rows:
            sys = row.get('system', '')
            if sys in filtered_ref:
                try:
                    val = float(row['lumo_eV'])
                    if abs(val - filtered_ref[sys]) <= tol:
                        correct += 1
                except (ValueError, KeyError):
                    pass
        return correct / total
    except Exception:
        return 0.0


# === block: score_4 (check id='eeff') ===
def score_4(artifact, step, ctx):
    # Compare effective work function values to reference, only for systems the paper actually reports.
    path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(path):
        return 0.0
    # Define the set of system identifiers for which the paper explicitly reports effective work function.
    VALID_SYSTEMS = {'pure_5_5', 'model_I', 'model_IV', 'pure_9_0', 'model_V', 'model_VI'}
    try:
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        ref = step['reference']
        tol = step['tolerance_abs']
        # Filter reference to only those systems actually reported in the paper.
        filtered_ref = {sys: val for sys, val in ref.items() if sys in VALID_SYSTEMS}
        total = len(filtered_ref)
        if total == 0:
            return 1.0
        correct = 0
        for row in rows:
            sys = row.get('system', '')
            if sys in filtered_ref:
                try:
                    val = float(row['effective_work_function_eV'])
                    if abs(val - filtered_ref[sys]) <= tol:
                        correct += 1
                except (ValueError, KeyError):
                    pass
        return correct / total
    except Exception:
        return 0.0


# === block: score_5 (check id='eeff_trend') ===
def score_5(artifact, step, ctx):
    # Verify monotonic decrease of effective work function with doping concentration.
    path = os.path.join('/app/outputs', step['output_file'])
    if not os.path.exists(path):
        return 0.0
    try:
        with open(path, newline='') as f:
            rows = list(csv.DictReader(f))
        data = {}
        for row in rows:
            sys = row.get('system', '')
            try:
                eeff = float(row['effective_work_function_eV'])
            except (ValueError, KeyError):
                continue
            data[sys] = eeff
        checks = step['trend_checks']
        if not checks:
            return 1.0
        passed = 0
        total = len(checks)
        for check in checks:
            direction = check.get('direction')
            groups = check['systems']  # list of lists
            try:
                # extract all values for each group, ignoring missing systems
                vals = []
                valid = True
                for grp in groups:
                    grp_eeffs = []
                    for sys in grp:
                        if sys in data:
                            grp_eeffs.append(data[sys])
                    if not grp_eeffs:
                        valid = False
                        break
                    # For decreasing: all values in earlier group must be > all values in later group
                    # We'll just compute min of earlier group (or max) based on direction.
                    vals.append(grp_eeffs)
                if not valid:
                    continue
                if direction == 'decreasing':
                    # Check strictly decreasing: for every i, j with i<j, all values in vals[i] > all values in vals[j]
                    ok = True
                    for i in range(len(vals)-1):
                        min_prev = min(vals[i])
                        max_next = max(vals[i+1])
                        if not (min_prev > max_next):
                            ok = False
                            break
                    if ok:
                        passed += 1
                else:
                    # not implemented
                    passed += 1
            except Exception:
                pass
        return passed / total
    except Exception:
        return 0.0


_SCORERS = {
    'results_csv_shape': score_0,
    'formation_energy': score_1,
    'homo': score_2,
    'lumo': score_3,
    'eeff': score_4,
    'eeff_trend': score_5,
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
