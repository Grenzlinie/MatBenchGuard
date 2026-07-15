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
    return {
        'step': spec['steps'][0]
    }


# === block: score_0 (check id='lattice_and_formation_check') ===
def score_0(artifact, step, ctx):
    # artifact is already the parsed JSON object, passed by checker.py
    data = artifact
    if not isinstance(data, dict) or 'compositions' not in data:
        return 0.0
    comps = data['compositions']
    if not isinstance(comps, list) or len(comps) < 4:
        return 0.0

    # Build lookup by label
    label_to_entry = {}
    for c in comps:
        if isinstance(c, dict) and 'label' in c:
            label_to_entry[c['label']] = c

    expected = step['expected_compositions']
    lattice_tol = step['lattice_tol']
    form_rel_tol = step['formation_rel_tol']

    # Score each composition
    lattice_score = 0.0
    formation_score = 0.0
    n_expected = len(expected)
    if n_expected == 0:
        return 0.0

    missing_count = 0
    for exp in expected:
        label = exp['label']
        if label not in label_to_entry:
            missing_count += 1
            continue
        entry = label_to_entry[label]
        # Check lattice
        try:
            latt = float(entry['lattice_parameter_angstrom'])
        except (KeyError, ValueError):
            lattice_score += 0.0
            formation_score += 0.0
            continue
        if abs(latt - exp['lattice']) <= lattice_tol:
            lattice_score += 1.0
        # Check formation energy
        try:
            form = float(entry['formation_energy_eV_per_atom'])
        except (KeyError, ValueError):
            formation_score += 0.0
            continue
        ref = exp['formation']
        if abs(ref) < 1e-9:
            form_err = abs(form - ref)
        else:
            form_err = abs(form - ref) / abs(ref)
        if form_err <= form_rel_tol:
            formation_score += 1.0

    # Average per composition
    lattice_score /= n_expected
    formation_score /= n_expected

    # Trend: lattice parameter must strictly increase with y
    # Sort by y, ensure strict monotonic increase
    valid_y_pairs = []
    for exp in expected:
        label = exp['label']
        if label in label_to_entry:
            entry = label_to_entry[label]
            try:
                y_val = float(entry['y'])
                latt_val = float(entry['lattice_parameter_angstrom'])
            except (KeyError, ValueError):
                continue
            valid_y_pairs.append((y_val, latt_val))
    valid_y_pairs.sort(key=lambda x: x[0])
    trend_ok = True
    for i in range(1, len(valid_y_pairs)):
        if valid_y_pairs[i][1] <= valid_y_pairs[i-1][1]:
            trend_ok = False
            break
    trend_score = 1.0 if trend_ok and len(valid_y_pairs) >= 2 else 0.0

    # Combine: equal weights on lattice, formation, trend
    final_score = (lattice_score + formation_score + trend_score) / 3.0
    return min(max(final_score, 0.0), 1.0)


_SCORERS = {
    'lattice_and_formation_check': score_0,
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
