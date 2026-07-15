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


# === block: score_0 (check id='dft_energies') ===
def score_0(artifact, step, ctx):
    import math
    _DFT_REF = {
        ("GaAsSe4", "MoS2"): 0.12,
        ("GaAsSe4", "CdI2"): -0.06,
        ("AlAsTe4", "MoS2"): 0.13,
        ("AlAsTe4", "CdI2"): -0.03,
    }

    try:
        compounds = artifact.get('compounds', [])
    except Exception:
        return 0.0

    # Increased tolerance to accommodate open-source DFT code differences (e.g. QE/GPAW vs VASP)
    tol = 0.08  # eV/atom

    score_per = []
    for (name, proto), ref_val in _DFT_REF.items():
        dft_val = None
        for c in compounds:
            if c.get('name') == name and c.get('prototype') == proto:
                dft_val = c.get('dft_formation_energy')
                break
        if dft_val is None:
            score_per.append(0.0)
            continue
        a, e = dft_val, ref_val
        if abs(a - e) <= tol:
            score_per.append(1.0)
        else:
            score_per.append(max(0.0, 1.0 - (abs(a - e) - tol) / tol))

    return sum(score_per) / len(score_per) if score_per else 0.0


# === block: score_1 (check id='predicted_classes') ===
def score_1(artifact, step, ctx):
    try:
        compounds = artifact.get('compounds', [])
    except Exception:
        return 0.0

    _EXPECTED_CLASS = {
        ("GaAsSe4", "MoS2"): "low",
        ("GaAsSe4", "CdI2"): "high",
        ("AlAsTe4", "MoS2"): "low",
        ("AlAsTe4", "CdI2"): "high",
    }

    scores = []
    for (name, proto), exp_cls in _EXPECTED_CLASS.items():
        found = None
        for c in compounds:
            if c.get('name') == name and c.get('prototype') == proto:
                found = c
                break
        if found is None:
            scores.append(0.0)
            continue
        actual = found.get('predicted_class', '')
        scores.append(1.0 if actual == exp_cls else 0.0)

    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='regression_rmse') ===
def score_2(artifact, step, ctx):
    import math
    try:
        rmse = artifact.get('regression_model_rmse', None)
        if rmse is None:
            return 0.0
    except Exception:
        return 0.0
    ref = step.get('reference', 0.205)
    slack = step.get('slack', 0.05)
    if rmse <= ref + slack:
        return 1.0
    else:
        over = rmse - (ref + slack)
        return max(0.0, 1.0 - over / (2*slack))


# === block: score_3 (check id='classification_auc') ===
def score_3(artifact, step, ctx):
    try:
        perf = artifact.get('classification_performance', {})
        auc_vals = perf.get('test_auc', {})
        thresholds = step.get('thresholds', {})
        scores = []
        for cls in ['low', 'medium', 'high']:
            val = auc_vals.get(cls, None)
            th = thresholds.get(cls, 0.85)
            if val is not None and val >= th:
                scores.append(1.0)
            else:
                scores.append(max(0.0, min(1.0, (val or 0.0) / th)))
        return sum(scores) / len(scores) if scores else 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'dft_energies': score_0,
    'predicted_classes': score_1,
    'regression_rmse': score_2,
    'classification_auc': score_3,
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
