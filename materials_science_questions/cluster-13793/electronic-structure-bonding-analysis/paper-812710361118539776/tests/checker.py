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


# === block: score_0 (check id='adsorption_energies') ===
def score_0(artifact, step, ctx):
    import math
    ref = step.get('reference', {})
    tol = step.get('tolerance', {})
    abs_tol = float(tol.get('absolute', 200.0))
    rel_tol = float(tol.get('relative', 0.15))
    expected_keys = ['Glycine', 'Serine', 'Glutamate', 'Arginine']
    if not isinstance(artifact, dict):
        return 0.0
    correct = 0
    total = len(expected_keys)
    for key in expected_keys:
        val = artifact.get(key)
        if val is None:
            continue
        ref_val = ref.get(key)
        if ref_val is None:
            continue
        try:
            val_f = float(val)
            ref_f = float(ref_val)
        except (TypeError, ValueError):
            continue
        if abs(val_f - ref_f) <= abs_tol:
            correct += 1
        elif ref_f != 0.0 and abs(val_f - ref_f) / abs(ref_f) <= rel_tol:
            correct += 1
    score = correct / total if total > 0 else 0.0
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='mulliken_charges') ===
def score_1(artifact, step, ctx):
    ref_list = step.get('reference', [])
    tol_abs = float(step.get('tolerance_abs', 0.1))
    ref_map = {}
    for item in ref_list:
        aa = item.get('amino_acid')
        if aa:
            ref_map[aa] = (item.get('COO_charge'), item.get('NH3_charge'))
    if not isinstance(artifact, list):
        return 0.0
    total_charges = len(ref_map) * 2
    correct = 0
    for item in artifact:
        if not isinstance(item, dict):
            continue
        aa = item.get('amino_acid')
        if aa is None or aa not in ref_map:
            continue
        coo_val = item.get('COO_charge')
        nh3_val = item.get('NH3_charge')
        ref_coo, ref_nh3 = ref_map[aa]
        try:
            coo_f = float(coo_val) if coo_val is not None else None
            nh3_f = float(nh3_val) if nh3_val is not None else None
        except (TypeError, ValueError):
            continue
        if coo_f is not None and ref_coo is not None and abs(coo_f - ref_coo) <= tol_abs:
            correct += 1
        if nh3_f is not None and ref_nh3 is not None and abs(nh3_f - ref_nh3) <= tol_abs:
            correct += 1
    if total_charges == 0:
        return 0.0
    return round(correct / total_charges, 6)


# === block: score_2 (check id='vb_dominance') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, str):
        return 0.0
    text = artifact.lower()
    has_o2p = 'o-2p' in text
    has_vb = 'valence band' in text
    has_driver = ('principal adsorption driver' in text) or ('main interaction' in text) or ('primary driver' in text)
    if has_o2p and has_driver:
        return 1.0
    elif has_o2p:
        return 0.5
    else:
        return 0.0


_SCORERS = {
    'adsorption_energies': score_0,
    'mulliken_charges': score_1,
    'vb_dominance': score_2,
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
