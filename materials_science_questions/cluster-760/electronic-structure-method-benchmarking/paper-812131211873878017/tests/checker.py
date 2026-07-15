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


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    # Validate the JSON array structure
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    schema = step.get("schema", {})
    expected_methods = schema.get("expected_methods", [])
    required_keys = schema.get("required_keys", [])
    if not required_keys or not expected_methods:
        return 0.0
    # Must have exactly the expected number of methods (all of them present)
    if len(artifact) != len(expected_methods):
        return 0.0
    for item in artifact:
        if not isinstance(item, dict):
            return 0.0
        for key in required_keys:
            if key not in item:
                return 0.0
        # Check that method is one of expected
        if item.get("method") not in expected_methods:
            return 0.0
        # Check numeric types roughly
        if not isinstance(item.get("E_abs_eV"), (int, float)):
            return 0.0
        if not isinstance(item.get("E_LC_eV"), (int, float)):
            return 0.0
        if not isinstance(item.get("E_EC_eV"), (int, float)):
            return 0.0
        if not isinstance(item.get("E_H2_eV"), (int, float)):
            return 0.0
    return 1.0


# === block: score_1 (check id='internal_consistency') ===
def score_1(artifact, step, ctx):
    # Check that E_abs = E_LC - E_EC - E_H2 within numerical tolerance
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    tolerance = step.get("tolerance", 1e-6)
    expected_methods = ["LDA", "PW91", "PBE", "BLYP", "FF_Buck"]
    # Build a dict from artifact
    art_dict = {}
    for item in artifact:
        if isinstance(item, dict) and "method" in item:
            art_dict[item["method"]] = item
    score = 0.0
    total = len(expected_methods)
    if total == 0:
        return 0.0
    for m in expected_methods:
        entry = art_dict.get(m)
        if entry is None:
            continue
        e_abs = entry.get("E_abs_eV")
        e_lc = entry.get("E_LC_eV")
        e_ec = entry.get("E_EC_eV")
        e_h2 = entry.get("E_H2_eV")
        if None in (e_abs, e_lc, e_ec, e_h2):
            continue
        computed = e_lc - e_ec - e_h2
        if abs(e_abs - computed) <= tolerance:
            score += 1.0
    return score / total


# === block: score_2 (check id='eabs_accuracy') ===
def score_2(artifact, step, ctx):
    # Compare E_abs per method against paper gold with tolerance
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    method_configs = step.get("methods", [])
    if not method_configs:
        return 0.0
    art_dict = {}
    for item in artifact:
        if isinstance(item, dict) and "method" in item:
            art_dict[item["method"]] = item
    total = len(method_configs)
    score = 0.0
    for cfg in method_configs:
        name = cfg.get("name")
        gold = cfg.get("gold")
        tol = cfg.get("tolerance", 0.01)
        if name is None or gold is None:
            continue
        entry = art_dict.get(name)
        if entry is None:
            continue
        e_abs = entry.get("E_abs_eV")
        if e_abs is None or not isinstance(e_abs, (int, float)):
            continue
        diff = abs(e_abs - gold)
        if diff <= tol:
            this_score = 1.0
        else:
            # Linear decay beyond tolerance, zero at 2*tol
            decay = (diff - tol) / tol  # non-negative
            this_score = max(0.0, 1.0 - decay)
        score += this_score
    return score / total if total > 0 else 0.0


_SCORERS = {
    'shape_check': score_0,
    'internal_consistency': score_1,
    'eabs_accuracy': score_2,
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
