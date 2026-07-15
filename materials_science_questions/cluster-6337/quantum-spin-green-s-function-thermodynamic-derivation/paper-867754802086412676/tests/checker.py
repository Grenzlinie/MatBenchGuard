import os
import json
import csv

# === author imports / helpers ===
import math
import cmath

def compute_epsilon(coeffs, q, xi):
    kappa = math.pi * q + 1j / xi
    d = sum(a * cmath.cos(n * kappa) for n, a in enumerate(coeffs))
    return cmath.sqrt(d)

def model_score(artifact, step):
    model_name = step['model_name']
    ref_xi = step['reference_xi']
    tol_rel = step['tolerance_relation']
    tol_xi_rel = step['tolerance_xi_rel']
    decay_rel = step['decay_relation_scale']
    decay_xi = step['decay_xi_rel_scale']
    w_rel = step['weight_relation']
    w_xi = step['weight_xi']

    models = artifact.get('models', [])
    match = None
    for m in models:
        if m.get('model') == model_name:
            match = m
            break
    if match is None:
        return 0.0

    xi = float(match['xi'])
    q = float(match['q_in_units_of_pi'])
    coeffs = match['fourier_coefficients_A_n']
    if not coeffs:
        return 0.0

    eps = compute_epsilon(coeffs, q, xi)
    abs_eps = abs(eps)
    if abs_eps <= tol_rel:
        rel_score = 1.0
    else:
        rel_score = max(0.0, 1.0 - (abs_eps - tol_rel) / decay_rel)

    xi_err = abs(xi - ref_xi) / ref_xi
    if xi_err <= tol_xi_rel:
        xi_score = 1.0
    else:
        xi_score = max(0.0, 1.0 - (xi_err - tol_xi_rel) / decay_xi)

    return w_rel * rel_score + w_xi * xi_score


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


# === block: score_0 (check id='model_BLBQ_beta_0') ===
def score_0(artifact, step, ctx):
    return model_score(artifact, step)


# === block: score_1 (check id='model_BLBQ_beta_1_3') ===
def score_1(artifact, step, ctx):
    return model_score(artifact, step)


# === block: score_2 (check id='model_BLBQ_beta_0.6') ===
def score_2(artifact, step, ctx):
    return model_score(artifact, step)


# === block: score_3 (check id='model_zigzag_alpha_0.48') ===
def score_3(artifact, step, ctx):
    return model_score(artifact, step)


# === block: score_4 (check id='model_zigzag_alpha_0.6') ===
def score_4(artifact, step, ctx):
    return model_score(artifact, step)


_SCORERS = {
    'model_BLBQ_beta_0': score_0,
    'model_BLBQ_beta_1_3': score_1,
    'model_BLBQ_beta_0.6': score_2,
    'model_zigzag_alpha_0.48': score_3,
    'model_zigzag_alpha_0.6': score_4,
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
