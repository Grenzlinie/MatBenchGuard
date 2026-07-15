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


# === block: score_0 (check id='fit_params') ===
def score_0(artifact, step, ctx):
    gold = {
        "Ne": {"alpha1": 0.7053, "beta1": 1.0432, "alpha2": 0.7092, "beta2": 0.116,
               "a_exp": 4.464, "E_exp": 165},
        "Ar": {"alpha1": 0.8208, "beta1": 1.0214, "alpha2": 0.8293, "beta2": 0.074,
               "a_exp": 5.311, "E_exp": 646},
        "Kr": {"alpha1": 0.8565, "beta1": 1.0211, "alpha2": 0.8602, "beta2": 0.080,
               "a_exp": 5.67, "E_exp": 936},
        "Xe": {"alpha1": 0.8715, "beta1": 1.0138, "alpha2": 0.876, "beta2": 0.06,
               "a_exp": 6.132, "E_exp": 1328},
    }
    tol_alpha = 0.001
    tol_beta  = 0.01
    tol_a     = 0.1
    tol_E     = 50

    total = 0
    passed = 0

    # Index artifact by RG
    data_by_rg = {}
    for entry in artifact:
        rg = entry.get("RG")
        if rg in gold:
            data_by_rg[rg] = entry

    for rg, g in gold.items():
        d = data_by_rg.get(rg)
        if d is None:
            total += 8
            continue
        # Fitted parameters
        checks = [
            (d.get("alpha1"), g["alpha1"], tol_alpha),
            (d.get("beta1"),  g["beta1"],  tol_beta),
            (d.get("alpha2"), g["alpha2"], tol_alpha),
            (d.get("beta2"),  g["beta2"],  tol_beta),
            # Computed properties against experiment
            (d.get("computed_a1"),      g["a_exp"], tol_a),
            (d.get("computed_E_inf1"),  g["E_exp"], tol_E),
            (d.get("computed_a2"),      g["a_exp"], tol_a),
            (d.get("computed_E_inf2"),  g["E_exp"], tol_E),
        ]
        for val, ref, tol in checks:
            total += 1
            if val is not None and isinstance(val, (int, float)) and abs(val - ref) <= tol:
                passed += 1

    if total == 0:
        return 0.0
    return passed / total


_SCORERS = {
    'fit_params': score_0,
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
