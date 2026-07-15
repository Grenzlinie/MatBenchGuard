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


# === block: score_0 (check id='step_02_extract_x') ===
def score_0(artifact, step, ctx):
    try:
        val = float(str(artifact).strip())
    except:
        return 0.0
    target = step.get("target", 0.1284)
    tolerance = step.get("tolerance", 0.01)
    if abs(val - target) <= tolerance:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_05_band_analysis') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    bw = artifact.get("optimized_bandwidth_dx2y2")
    if bw is None:
        return 0.0
    try:
        bw = float(bw)
    except:
        return 0.0
    threshold = step.get("bandwidth_threshold", 0.1)
    score = 0.0
    if bw <= threshold:
        score += 0.5
    half_met = artifact.get("optimized_half_metallic")
    if half_met == step.get("half_metallic_expected", True):
        score += 0.25
    x1450_met = artifact.get("x1450_metallic")
    if x1450_met == step.get("x1450_metallic_expected", True):
        score += 0.25
    return score


# === block: score_2 (check id='step_06_diff_charge') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    opt = artifact.get("optimized_peak_density")
    x1450 = artifact.get("x1450_peak_density")
    if opt is None or x1450 is None:
        return 0.0
    try:
        opt_val = float(opt); x1450_val = float(x1450)
    except:
        return 0.0
    target_opt = step.get("optimized_target", 2.2)
    target_x1450 = step.get("x1450_target", 1.3)
    rel_tol = step.get("relative_tolerance", 0.15)
    def in_tol(val, target, rel_tol):
        if target == 0:
            return False
        return abs(val - target) / abs(target) <= rel_tol
    score = 0.0
    if in_tol(opt_val, target_opt, rel_tol):
        score += 0.5
    if in_tol(x1450_val, target_x1450, rel_tol):
        score += 0.5
    return score


_SCORERS = {
    'step_02_extract_x': score_0,
    'step_05_band_analysis': score_1,
    'step_06_diff_charge': score_2,
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
