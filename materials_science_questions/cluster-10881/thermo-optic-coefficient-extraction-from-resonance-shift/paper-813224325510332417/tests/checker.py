import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
        'a_coeffs': [
            (228.7018,  4.93e-5,  1.10e-7),
            (46.40806, -3.27e-5, -3.78e-8),
            (0.014173, -1.704e-6, -2.14e-9),
        ],
        'b_coeffs': [
            (18.111630,  9.15e-5,  7.478e-5),
            (10.671082, -2.9913e-4, -4.8074e-8),
            (0.125,       1e-5,     1e-8),
        ],
        'temperatures': [20, 40],
        'indices': [1, 2, 3],
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts (CSV rows) as parsed by the loader
    # step dict gives weight, tolerance_relative
    # ctx contains a_coeffs, b_coeffs, etc.
    expected = []
    for T in ctx['temperatures']:
        for idx, i in enumerate(ctx['indices']):
            a0,a1,a2 = ctx['a_coeffs'][idx]
            b0,b1,b2 = ctx['b_coeffs'][idx]
            a_exp = a0 + a1*T + a2*T*T
            b_exp = b0 + b1*T + b2*T*T
            expected.append((T, i, a_exp, b_exp))

    if len(artifact) != 6:
        return 0.0

    # Build mapping from (temperature, i) to submitted values
    submitted = {}
    for row in artifact:
        try:
            T = int(float(row.get('temperature', 0)))
            i = int(float(row.get('i', 0)))
            a_i_val = float(row.get('a_i', 0))
            b_i_val = float(row.get('b_i', 0))
            submitted[(T, i)] = (a_i_val, b_i_val)
        except (ValueError, TypeError):
            return 0.0  # malformed row

    tol = step.get('tolerance_relative', 0.001)
    total_cells = 0
    correct = 0
    for T, i, a_exp, b_exp in expected:
        key = (T, i)
        if key not in submitted:
            continue
        a_sub, b_sub = submitted[key]
        # Relative error with a tiny floor to avoid division by zero
        re_a = abs(a_sub - a_exp) / (abs(a_exp) + 1e-12)
        re_b = abs(b_sub - b_exp) / (abs(b_exp) + 1e-12)
        if re_a <= tol:
            correct += 1
        if re_b <= tol:
            correct += 1
        total_cells += 2

    if total_cells == 0:
        return 0.0
    return correct / total_cells


_SCORERS = {
    'step_01': score_0,
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
