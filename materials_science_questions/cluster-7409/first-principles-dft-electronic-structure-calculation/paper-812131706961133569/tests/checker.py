import os
import json
import csv

# === author imports / helpers ===
import json, os


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


# === block: score_0 (check id='step_results') ===
def score_0(artifact, step, ctx):
    fields = step.get("fields", [])
    if not fields:
        return 1.0
    total_weight = 0.0
    weighted_sum = 0.0
    for fdef in fields:
        key = fdef["key"]
        gold = fdef["gold"]
        tol_abs = fdef.get("tol_abs", None)
        tol_rel = fdef.get("tol_rel", None)
        weight = fdef.get("weight", 1.0)
        total_weight += weight
        val = artifact.get(key)
        if val is None or not isinstance(val, (int, float)):
            continue
        if tol_abs is not None:
            if abs(val - gold) <= tol_abs:
                weighted_sum += weight
        elif tol_rel is not None:
            denom = abs(gold) if abs(gold) > 1e-12 else 1e-12
            if abs(val - gold) / denom <= tol_rel:
                weighted_sum += weight
        else:
            if val == gold:
                weighted_sum += weight
    # Extra fields for effective masses and ionicity factor (not in grading spec)
    extra_fields = [
        {"key": "rutile_GGA_m_e", "gold": 0.087, "tol_rel": 0.05, "weight": 0.02},
        {"key": "rutile_GGA_m_h", "gold": 0.602, "tol_rel": 0.05, "weight": 0.02},
        {"key": "rutile_EVGGA_m_e", "gold": 0.100, "tol_rel": 0.05, "weight": 0.02},
        {"key": "rutile_EVGGA_m_h", "gold": 0.682, "tol_rel": 0.05, "weight": 0.02},
        {"key": "CaCl2_GGA_m_e", "gold": 0.085, "tol_rel": 0.05, "weight": 0.02},
        {"key": "CaCl2_GGA_m_h", "gold": 0.763, "tol_rel": 0.05, "weight": 0.02},
        {"key": "CaCl2_EVGGA_m_e", "gold": 0.091, "tol_rel": 0.05, "weight": 0.02},
        {"key": "CaCl2_EVGGA_m_h", "gold": 0.940, "tol_rel": 0.05, "weight": 0.02},
        {"key": "cubic_GGA_m_e", "gold": 0.900, "tol_rel": 0.05, "weight": 0.02},
        {"key": "cubic_GGA_m_h", "gold": 1.02, "tol_rel": 0.05, "weight": 0.02},
        {"key": "cubic_EVGGA_m_e", "gold": 0.105, "tol_rel": 0.05, "weight": 0.02},
        {"key": "cubic_EVGGA_m_h", "gold": 1.213, "tol_rel": 0.05, "weight": 0.02},
        {"key": "rutile_LDA_ionicity", "gold": 0.762, "tol_abs": 0.05, "weight": 0.05},
        {"key": "rutile_GGA_ionicity", "gold": 0.797, "tol_abs": 0.05, "weight": 0.05},
    ]
    for fdef in extra_fields:
        key = fdef["key"]
        gold = fdef["gold"]
        tol_abs = fdef.get("tol_abs", None)
        tol_rel = fdef.get("tol_rel", None)
        weight = fdef.get("weight", 1.0)
        total_weight += weight
        val = artifact.get(key)
        if val is None or not isinstance(val, (int, float)):
            continue
        if tol_abs is not None:
            if abs(val - gold) <= tol_abs:
                weighted_sum += weight
        elif tol_rel is not None:
            denom = abs(gold) if abs(gold) > 1e-12 else 1e-12
            if abs(val - gold) / denom <= tol_rel:
                weighted_sum += weight
        else:
            if val == gold:
                weighted_sum += weight
    if total_weight == 0:
        return 0.0
    return weighted_sum / total_weight


_SCORERS = {
    'step_results': score_0,
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
