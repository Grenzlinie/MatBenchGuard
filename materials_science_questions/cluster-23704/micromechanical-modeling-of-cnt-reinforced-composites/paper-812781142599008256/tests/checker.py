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


# === block: score_0 (check id='step_predictions') ===
def score_0(artifact, step, ctx):
    import math

    # Retrieve model parameters from the hidden grading step
    params = step.get('model_params', {})
    Em   = float(params['Em'])
    E_CNT = float(params['E_CNT'])
    Sm   = float(params['Sm'])
    S_CNT = float(params['S_CNT'])
    L_CNT = float(params['L_CNT'])
    d_CNT = float(params['d_CNT'])
    R = L_CNT / d_CNT
    fR   = float(params['fR'])
    fW   = float(params['fW'])
    alpha = float(params['alpha'])
    beta = float(params['beta'])
    tolerance = float(step.get('mae_tolerance_threshold', 0.1))

    # Convert artifact rows (list of dicts) to numeric values
    V_vals = []
    E_agent = []
    S_agent = []
    for row in artifact:
        try:
            V = float(row['V_CNT'])
            E = float(row['E_modulus (GPa)'])
            S = float(row['Tensile_strength (MPa)'])
            V_vals.append(V)
            E_agent.append(E)
            S_agent.append(S)
        except (ValueError, KeyError):
            return 0.0  # malformed row

    # Compute expected E and S for each V
    E_exp = []
    S_exp = []
    for V in V_vals:
        fA = math.exp(-alpha * (V ** beta))
        # elastic modulus
        term_E = fR * fW * fA * (E_CNT / Em)
        delta_E = (term_E - 1.0) / (term_E + 2.0 * R)
        E_val = Em * (1.0 + 2.0 * R * delta_E * V) / (1.0 - delta_E * V)
        # tensile strength
        term_S = fR * fW * fA * (S_CNT / Em)
        delta_S = (term_S - 1.0) / (term_S + 2.0 * R)
        S_val = Sm * (1.0 + 2.0 * R * delta_S * V) / (1.0 - delta_S * V)
        E_exp.append(E_val)
        S_exp.append(S_val)

    # Compute mean absolute error over all predicted points
    abs_errors = [abs(ea - ee) for ea, ee in zip(E_agent, E_exp)] + [abs(sa - se) for sa, se in zip(S_agent, S_exp)]
    if not abs_errors:
        return 0.0
    mae = sum(abs_errors) / len(abs_errors)

    # Map MAE to score: linear decay, full credit at near-zero error
    if mae >= tolerance:
        return 0.0
    score = max(0.0, 1.0 - mae / tolerance)
    return score


_SCORERS = {
    'step_predictions': score_0,
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
