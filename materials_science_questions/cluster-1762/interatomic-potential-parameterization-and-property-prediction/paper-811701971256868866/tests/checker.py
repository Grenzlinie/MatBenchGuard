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
    gold = {
        "LiH": {"y": 2.5199, "lambda": 1.5799, "alpha_calc": 0.2024, "omega_x_calc": 21.01, "Di_calc": 149.1,
                "alpha_error_percent": -5.1, "omega_x_error_percent": -9.4, "Di_error_percent": -9.7},
        "NaH": {"y": 3.0277, "lambda": 1.6045, "alpha_calc": 0.1241, "omega_x_calc": 16.72, "Di_calc": 132.3,
                "alpha_error_percent": -8.3, "omega_x_error_percent": -15.2, "Di_error_percent": -12.0},
        "KH": {"y": 3.5291, "lambda": 1.5727, "alpha_calc": 0.0832, "omega_x_calc": 13.83, "Di_calc": 115.3,
              "alpha_error_percent": 23.6, "omega_x_error_percent": -5.6, "Di_error_percent": -9.4},
        "RbH": {"y": 3.7495, "lambda": 1.5841, "alpha_calc": 0.0730, "omega_x_calc": 13.17, "Di_calc": 110.8,
                "alpha_error_percent": 1.4, "omega_x_error_percent": -6.9, "Di_error_percent": -7.4},
        "CsH": {"y": 3.9407, "lambda": 1.5801, "alpha_calc": 0.0649, "omega_x_calc": 12.53, "Di_calc": 106.2,
                "alpha_error_percent": 13.9, "omega_x_error_percent": -0.6, "Di_error_percent": -8.0}
    }
    mean_lambda = 1.5843
    return {"gold": gold, "mean_lambda": mean_lambda}


# === block: score_0 (check id='step_hellmann_calc') ===
def score_0(artifact, step, ctx):
    gold_dict = ctx["gold"]
    mean_lambda = ctx["mean_lambda"]
    tol = {
        "y": 0.00005,
        "lambda": 0.00005,
        "alpha_calc": 0.00005,
        "omega_x_calc": 0.005,
        "Di_calc": 0.05,
        "alpha_error_percent": 0.2,
        "omega_x_error_percent": 0.2,
        "Di_error_percent": 0.2
    }
    fields = ["y","lambda","alpha_calc","omega_x_calc","Di_calc",
              "alpha_error_percent","omega_x_error_percent","Di_error_percent"]
    total_checks = 0
    passed = 0
    for mol, gold_vals in gold_dict.items():
        total_checks += len(fields)
        row = next((r for r in artifact if r.get("molecule") == mol), None)
        if row is None:
            continue
        for f in fields:
            try:
                agent_val = float(row.get(f))
            except (ValueError, TypeError):
                continue
            if abs(agent_val - gold_vals[f]) <= tol.get(f, 0):
                passed += 1
    mean_row = next((r for r in artifact if r.get("molecule") == "mean"), None)
    if mean_row is not None:
        total_checks += 1
        try:
            agent_mean = float(mean_row.get("lambda"))
        except (ValueError, TypeError):
            agent_mean = None
        if agent_mean is not None and abs(agent_mean - mean_lambda) <= 0.00005:
            passed += 1
    score = passed / total_checks if total_checks > 0 else 0.0
    return score


_SCORERS = {
    'step_hellmann_calc': score_0,
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
