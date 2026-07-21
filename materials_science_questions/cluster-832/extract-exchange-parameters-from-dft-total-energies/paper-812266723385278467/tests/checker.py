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
    step = spec['steps'][0]
    gold = step.get('gold', {})
    tol = step.get('abs_tolerance', 0.005)
    ordering = step.get('ordering_rules', {})
    return {'gold': gold, 'tolerance': tol, 'ordering': ordering}


# === block: score_0 (check id='step_02_compute_couplings') ===
def score_0(artifact, step, ctx):
    import os, json
    artifact_path = os.path.join('/app/outputs', step['output_file'])
    artifact = load_artifact(artifact_path)
    if not isinstance(artifact, dict):
        return 0.0
    compound_si = artifact.get('BaCu2Si2O7', {})
    compound_ge = artifact.get('BaCu2Ge2O7', {})
    if not isinstance(compound_si, dict) or not isinstance(compound_ge, dict):
        return 0.0

    gold_map = ctx['gold']
    order = ctx['ordering']

    # Expected signs from gold values (positive = FM, negative = AF)
    signs = {}
    for compound in gold_map:
        for key, val in gold_map[compound].items():
            if val > 0:
                signs[(compound, key)] = 1
            elif val < 0:
                signs[(compound, key)] = -1
            else:
                signs[(compound, key)] = 0
    # Manually add J2 Ge sign (FM, as stated in paper)
    signs[('BaCu2Ge2O7', 'J2')] = 1

    si_keys = ['J1','J2','J4','J7','J8']
    ge_keys = ['J1','J2','J4']
    all_couplings = [('BaCu2Si2O7', k) for k in si_keys] + [('BaCu2Ge2O7', k) for k in ge_keys]

    total = len(all_couplings)
    correct = 0
    for comp, key in all_couplings:
        val = compound_si.get(key) if comp == 'BaCu2Si2O7' else compound_ge.get(key)
        if val is None or not isinstance(val, (int, float)):
            continue
        expected_sign = signs.get((comp, key))
        if expected_sign is None:
            continue
        if expected_sign > 0 and val > 0:
            correct += 1
        elif expected_sign < 0 and val < 0:
            correct += 1
        elif expected_sign == 0 and val == 0:
            correct += 1
        # otherwise sign wrong, don't count

    # Ordering checks
    ordering_ok_si = True
    j_vals_si = {}
    for k in si_keys:
        v = compound_si.get(k)
        if v is None or not isinstance(v, (int, float)):
            ordering_ok_si = False
            break
        j_vals_si[k] = abs(v)
    if ordering_ok_si:
        ordering_ok_si = (j_vals_si['J1'] > j_vals_si['J8'] > j_vals_si['J2'] > j_vals_si['J7'] > j_vals_si['J4'])

    ordering_ok_ge = True
    j_vals_ge = {}
    for k in ge_keys:
        v = compound_ge.get(k)
        if v is None or not isinstance(v, (int, float)):
            ordering_ok_ge = False
            break
        j_vals_ge[k] = abs(v)
    if ordering_ok_ge:
        ordering_ok_ge = (j_vals_ge['J1'] > j_vals_ge['J2'] > j_vals_ge['J4'])

    mult = 1.0 if (ordering_ok_si and ordering_ok_ge) else 0.5

    if total == 0:
        return 0.0
    score = (correct / total) * mult
    return score


_SCORERS = {
    'step_02_compute_couplings': score_0,
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
