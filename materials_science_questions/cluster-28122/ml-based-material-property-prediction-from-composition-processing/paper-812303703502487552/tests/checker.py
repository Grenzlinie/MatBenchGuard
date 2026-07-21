import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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
    predictions = []
    p = os.path.join(outputs_dir, "predictions.csv")
    if os.path.exists(p):
        with open(p, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                predictions.append(row)
    return {"predictions": predictions, "outputs_dir": outputs_dir}


# === block: score_0 (check id='fit_regression_models') ===
def score_0(artifact, step, ctx):
    preds = ctx.get("predictions", [])
    if not preds:
        return 0.0
    required = {"melt_id", "tau_exp", "linear_conc_pred", "linear_snir_pred", "exp_conc_pred", "exp_snir_pred"}
    if not required.issubset(set(preds[0].keys())):
        return 0.0
    if len(preds) < 16:
        return 0.0
    return 1.0


# === block: score_1 (check id='compute_deviation_delta') ===
def score_1(artifact, step, ctx):
    predictions = ctx.get("predictions", [])
    if not predictions:
        return 0.0

    # convert columns to float lists
    try:
        tau_exp = [float(r["tau_exp"]) for r in predictions]
        lin_conc = [float(r["linear_conc_pred"]) for r in predictions]
        lin_snir = [float(r["linear_snir_pred"]) for r in predictions]
        exp_conc = [float(r["exp_conc_pred"]) for r in predictions]
        exp_snir = [float(r["exp_snir_pred"]) for r in predictions]
    except (KeyError, ValueError):
        return 0.0

    n = len(tau_exp)
    if n == 0:
        return 0.0

    def mae(a, p):
        return sum(abs(ai - pi) for ai, pi in zip(a, p)) / n

    d_lin_conc = mae(tau_exp, lin_conc)
    d_lin_snir = mae(tau_exp, lin_snir)
    d_exp_conc = mae(tau_exp, exp_conc)
    d_exp_snir = mae(tau_exp, exp_snir)

    # paper reference values
    ref_lin_conc = step.get("reference_delta_linear_concentration", 7.3)
    ref_lin_snir = step.get("reference_delta_linear_snir", 7.7)
    ref_exp_conc = step.get("reference_delta_exponential_concentration", 5.9)
    ref_exp_snir = step.get("reference_delta_exponential_snir", 5.5)
    slack = step.get("delta_tolerance_slack", 0.1)

    def score_delta(recomputed, ref):
        if recomputed <= ref + slack:
            return 1.0
        decay = max(0.0, 1.0 - (recomputed - ref - slack) / (0.3 * ref))
        return decay

    s1 = score_delta(d_lin_conc, ref_lin_conc)
    s2 = score_delta(d_lin_snir, ref_lin_snir)
    s3 = score_delta(d_exp_conc, ref_exp_conc)
    s4 = score_delta(d_exp_snir, ref_exp_snir)

    delta_score = (s1 + s2 + s3 + s4) / 4.0

    # inequalities
    max_diff = step.get("inequality_max_delta_diff", 2.0)
    ineq1 = d_exp_conc < d_lin_conc
    ineq2 = d_exp_snir < d_lin_snir
    ineq3 = abs(d_lin_conc - d_lin_snir) <= max_diff
    ineq4 = abs(d_exp_conc - d_exp_snir) <= max_diff

    satisfied = sum([ineq1, ineq2, ineq3, ineq4])
    inequality_score = satisfied * 0.05   # max 0.2

    # final composite (delta 0.8 + inequalities 0.2)
    total = delta_score * 0.8 + inequality_score
    return min(total, 1.0)


_SCORERS = {
    'fit_regression_models': score_0,
    'compute_deviation_delta': score_1,
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
