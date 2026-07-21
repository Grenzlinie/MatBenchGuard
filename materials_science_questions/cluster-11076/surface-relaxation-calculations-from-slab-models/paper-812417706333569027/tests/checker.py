import os
import json
import csv

# === author imports / helpers ===
import json
import math

def score_rel_tolerance(value, target, tol_rel):
    """Return score in [0,1] based on relative error, monotonically decreasing after tolerance."""
    if value is None:
        return 0.0
    denom = max(abs(target), 1e-12)
    rel_err = abs(value - target) / denom
    if rel_err <= tol_rel:
        return 1.0
    # Decay to zero at 5*tol_rel
    decay = (rel_err - tol_rel) / (4.0 * tol_rel)  # 5*tol_rel total range
    return max(0.0, 1.0 - decay)

def get_nested(d, path_str):
    keys = path_str.split('.')
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k)
        else:
            return None
    return d


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


# === block: score_0 (check id='check_Fb_minus_Fa') ===
def score_0(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_1 (check id='check_Fc_minus_Fb') ===
def score_1(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_2 (check id='check_Fd_minus_Fc') ===
def score_2(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_3 (check id='check_Fe_minus_Fd') ===
def score_3(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_4 (check id='check_Ff_minus_Fe') ===
def score_4(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_5 (check id='check_total_free_energy') ===
def score_5(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', 'total_free_energy'))
    return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_6 (check id='check_surface_tension') ===
def score_6(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    # Use absolute tolerance if provided, else fall back to relative
    abs_tol = step.get('tolerance_abs', None)
    if abs_tol is not None and value is not None:
        err = abs(value - step['target'])
        if err <= abs_tol:
            return 1.0
        # Decay: zero credit at 5*abs_tol
        decay = (err - abs_tol) / (4.0 * abs_tol)
        return max(0.0, 1.0 - decay)
    else:
        return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


# === block: score_7 (check id='check_excess_internal_energy') ===
def score_7(artifact, step, ctx):
    value = get_nested(artifact, step.get('json_path', ''))
    abs_tol = step.get('tolerance_abs', None)
    if abs_tol is not None and value is not None:
        err = abs(value - step['target'])
        if err <= abs_tol:
            return 1.0
        decay = (err - abs_tol) / (4.0 * abs_tol)
        return max(0.0, 1.0 - decay)
    else:
        return score_rel_tolerance(value, step['target'], step.get('tolerance_rel', 0.0))


_SCORERS = {
    'check_Fb_minus_Fa': score_0,
    'check_Fc_minus_Fb': score_1,
    'check_Fd_minus_Fc': score_2,
    'check_Fe_minus_Fd': score_3,
    'check_Ff_minus_Fe': score_4,
    'check_total_free_energy': score_5,
    'check_surface_tension': score_6,
    'check_excess_internal_energy': score_7,
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