import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='rate_constants_check') ===
def score_0(artifact, step, ctx):
    data = artifact
    # data must be a list of exactly three objects with required keys
    required = {"MOF", "barrier_kJ_per_mol", "reaction_energy_kJ_per_mol", "rate_constant"}
    if not isinstance(data, list) or len(data) != 3:
        return 0.0
    for d in data:
        if not isinstance(d, dict) or not required.issubset(d.keys()):
            return 0.0
    # Build lookup by MOF name
    mof_map = {}
    valid_names = {"MIL-53(Al)-BDC", "MIL-53(Al)-FA", "MIL-53(Al)-TDC"}
    for d in data:
        name = d["MOF"].strip()
        if name not in valid_names:
            return 0.0
        mof_map[name] = d
    # All three must be present exactly once
    if set(mof_map.keys()) != valid_names:
        return 0.0

    # Extract values
    k_bdc = mof_map["MIL-53(Al)-BDC"]["rate_constant"]
    k_fa  = mof_map["MIL-53(Al)-FA"]["rate_constant"]
    k_tdc = mof_map["MIL-53(Al)-TDC"]["rate_constant"]
    bar_bdc = mof_map["MIL-53(Al)-BDC"]["barrier_kJ_per_mol"]
    bar_fa  = mof_map["MIL-53(Al)-FA"]["barrier_kJ_per_mol"]
    bar_tdc = mof_map["MIL-53(Al)-TDC"]["barrier_kJ_per_mol"]

    score = 0.0

    # ---- rate constant trend (0.7 total) ----
    if k_bdc < 0 and k_fa < 0 and k_tdc < 0:
        # TDC must be at least 10 times more negative (i.e., larger absolute value)
        if abs(k_tdc) > 10.0 * max(abs(k_bdc), abs(k_fa)):
            score += 0.4
        # BDC and FA must be within an order of magnitude of each other
        if abs(k_bdc) > 0 and abs(k_fa) > 0:
            log10_diff = abs(math.log10(abs(k_bdc)) - math.log10(abs(k_fa)))
            if log10_diff < 1.0:
                score += 0.3
        # (if TDC ordering fails, still might get similarity credit)

    # ---- barrier trend (0.3) ----
    if bar_tdc + 10.0 <= bar_bdc and bar_tdc + 10.0 <= bar_fa:
        score += 0.3

    return min(score, 1.0)


_SCORERS = {
    'rate_constants_check': score_0,
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
