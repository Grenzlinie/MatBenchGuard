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
    import math

    # Hardcoded parameters from paper Table I
    params = [
        {"x": 0, "E5d1Ex": 34542, "SS": 2896},
        {"x": 1, "E5d1Ex": 34843, "SS": 2689},
        {"x": 2, "E5d1Ex": 35335, "SS": 2735},
        {"x": 3, "E5d1Ex": 35747, "SS": 2798},
        {"x": 4, "E5d1Ex": 35939, "SS": 2744},
        {"x": 5, "E5d1Ex": 36331, "SS": 2947},
    ]
    # Paper reported ΔE values (hidden gold for deriving E³P₂Ex)
    delta_paper = [17388, 18487, 19839, 20713, 22097, 20857]

    ref_params = []
    for i, p in enumerate(params):
        A = p["SS"] / 2.0
        E_zpl = p["E5d1Ex"] - A
        dp = delta_paper[i]
        # Derive E³P₂Ex that makes the harmonic model reproduce the paper's ΔE exactly
        sqrt_term = math.sqrt(A * dp)
        E3P2Ex = E_zpl - A - 2 * sqrt_term
        ref_params.append({
            "x": p["x"],
            "A": A,
            "E_zpl": E_zpl,
            "E3P2Ex": E3P2Ex
        })

    return {"ref_params": ref_params}


# === block: score_0 (check id='barrier_check') ===
def score_0(artifact, step, ctx):
    import math

    data = artifact
    tolerance = 1.0

    # Input parameters from instruction (same as agent receives)
    params = [
        {"x": 0, "E5d1Ex": 34542, "SS": 2896, "E3P2Ex": 21618},
        {"x": 1, "E5d1Ex": 34843, "SS": 2689, "E3P2Ex": 22186},
        {"x": 2, "E5d1Ex": 35335, "SS": 2735, "E3P2Ex": 22185},
        {"x": 3, "E5d1Ex": 35747, "SS": 2798, "E3P2Ex": 22181},
        {"x": 4, "E5d1Ex": 35939, "SS": 2744, "E3P2Ex": 22183},
        {"x": 5, "E5d1Ex": 36331, "SS": 2947, "E3P2Ex": 22295},
    ]

    # Compute reference barriers using harmonic model with equal force constants
    ref_computed = {}
    for p in params:
        A = p["SS"] / 2.0
        E_zpl = p["E5d1Ex"] - A
        E3P2Ex = p["E3P2Ex"]
        # crossing point: u = (E_zpl + A - E3P2Ex) / (2 A)
        u = (E_zpl + A - E3P2Ex) / (2.0 * A)
        delta = A * (u - 1.0) ** 2
        ref_computed[p["x"]] = delta

    # per‑composition accuracy
    keys = ["x0", "x1", "x2", "x3", "x4", "x5"]
    per_x_score = 0.0
    for x_idx, key in enumerate(keys):
        if key not in data:
            per_x_score = 0.0
            break
        val = float(data[key])
        ref = ref_computed[x_idx]
        if abs(val - ref) <= tolerance:
            per_x_score += 1.0
    per_x_score /= 6.0

    # monotonic trend check for x0..x4
    vals = []
    for key in ["x0", "x1", "x2", "x3", "x4"]:
        if key not in data:
            mono = False
            break
        vals.append(float(data[key]))
    else:
        mono = all(vals[i] < vals[i+1] for i in range(4))
    mono_score = 1.0 if mono else 0.0

    score = 0.7 * per_x_score + 0.3 * mono_score
    return score


_SCORERS = {
    'barrier_check': score_0,
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
