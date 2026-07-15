import os
import json
import csv

# === author imports / helpers ===
import math

def eval_poly(coeffs, x):
    res = 0.0
    for c in reversed(coeffs):
        res = res * x + c
    return res


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
    gold_coeffs = spec["gold_coefficients"]
    x_points = spec["x_points"]
    gold_values = {}
    for key in gold_coeffs:
        coeffs = gold_coeffs[key]
        pts = x_points[key]
        gold_values[key] = [(x, eval_poly(coeffs, x)) for x in pts]
    return {"gold_values": gold_values, "expected_bU": spec["expected_bU"], "expected_cU": spec["expected_cU"], "tolerance": spec.get("tolerance", 0.01)}


# === block: score_0 (check id='fit_polynomials') ===
def score_0(artifact, step, ctx):
    gold_values = ctx["gold_values"]
    expected_bU = ctx["expected_bU"]
    expected_cU = ctx["expected_cU"]
    tolerance = ctx["tolerance"]
    if not isinstance(artifact, dict):
        return 0.0

    # check bU and cU exactness (0.1 weight)
    bU = artifact.get("bU")
    cU = artifact.get("cU")
    const_ok = 0.0
    if isinstance(bU, list) and len(bU) == 5 and all(abs(a-b) < 1e-9 for a,b in zip(bU, expected_bU)):
        const_ok += 0.5
    if isinstance(cU, list) and len(cU) == 5 and all(abs(a-b) < 1e-9 for a,b in zip(cU, expected_cU)):
        const_ok += 0.5
    const_score = const_ok

    # polynomial evaluation accuracy (0.9 weight)
    keys = ["M1_left", "M1_right", "M2", "M3", "M4", "M5"]
    total_points = 0
    passed_points = 0
    for key in keys:
        arr = artifact.get(key)
        if not isinstance(arr, list) or len(arr) != 8:
            total_points += len(gold_values[key])
            continue
        for x, gold_P in gold_values[key]:
            try:
                agent_P = eval_poly(arr, x)
            except:
                total_points += 1
                continue
            if abs(gold_P) < 1e-12:
                if abs(agent_P - gold_P) < 1e-12:
                    passed_points += 1
            else:
                rel_err = abs(agent_P - gold_P) / max(abs(gold_P), 1e-12)
                if rel_err < tolerance:
                    passed_points += 1
            total_points += 1
    poly_score = passed_points / max(total_points, 1)

    overall = 0.1 * const_score + 0.9 * poly_score
    return overall


_SCORERS = {
    'fit_polynomials': score_0,
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
