import os
import json
import csv

# === author imports / helpers ===
import subprocess, sys
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy"])
    import numpy as np


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


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    # The artifact is a list of dicts with keys Q1, Q2, energy_mev_per_fu
    if len(artifact) != 49:
        return 0.0
    Q1 = np.array([float(r['Q1']) for r in artifact])
    Q2 = np.array([float(r['Q2']) for r in artifact])
    E = np.array([float(r['energy_mev_per_fu']) for r in artifact])

    # Build design matrix: columns [Q2^2, Q2^4, Q2^6, Q2^8, Q1*Q2^2, Q1*Q2^4, Q1^2]
    A = np.column_stack([
        Q2**2, Q2**4, Q2**6, Q2**8,
        Q1 * Q2**2, Q1 * Q2**4,
        Q1**2
    ])
    coeffs, residuals, rank, s = np.linalg.lstsq(A, E, rcond=None)
    b02_fit, b04_fit, b06_fit, b08_fit, c12_fit, c14_fit, a20_fit = coeffs

    hidden = step.get('hidden', {})
    gold = hidden.get('coefficients', {})
    tol_rel = hidden.get('tolerance_rel', 0.2)
    tol_abs = hidden.get('tolerance_abs', 10.0)
    tol_abs_thresh = hidden.get('tolerance_abs_threshold', 10.0)

    # Ordered gold coefficients matching the design matrix columns
    keys = ['b02', 'b04', 'b06', 'b08', 'c12', 'c14', 'a20']
    fitted_vals = [b02_fit, b04_fit, b06_fit, b08_fit, c12_fit, c14_fit, a20_fit]

    all_ok = True
    for key, fit_val in zip(keys, fitted_vals):
        gold_val = gold.get(key)
        if gold_val is None:
            all_ok = False
            break
        delta = abs(fit_val - gold_val)
        if abs(gold_val) > tol_abs_thresh:
            tol = tol_rel * abs(gold_val)
        else:
            tol = tol_abs
        if delta > tol:
            all_ok = False
            break

    # Structural checks
    structural = hidden.get('structural', {})
    if structural.get('check_c12_sign', False) and c12_fit >= 0:
        all_ok = False
    if structural.get('check_c12_magnitude_gt_b02_magnitude', False) and abs(c12_fit) <= abs(b02_fit):
        all_ok = False

    return 1.0 if all_ok else 0.0


_SCORERS = {
    'step2': score_0,
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
