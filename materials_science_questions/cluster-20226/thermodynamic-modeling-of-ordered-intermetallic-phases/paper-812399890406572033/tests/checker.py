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
    return {
        'ref_DG_bp_ap': lambda T: 19.6 - 1.4940*T + 8.1215e-3*T**2 - 8.1925e-6*T**3,
        'ref_DG_b_a': lambda T: -1098.8 + 1.3516*T,
        'ref_DG_bp_b1p': lambda T: 6.3 - 1.71e-2*T - 3.99e-5*T**2 + 5.71e-8*T**3,
        'ref_DG_a_ap': lambda T: -520.4 + 1.1931*T,
        'poly_ref': {
            'constant': 19.6,
            'T': -1.4940,
            'T2': 8.1215e-3,
            'T3': -8.1925e-6
        }
    }


# === block: score_0 (check id='step_02_driving_forces') ===
def score_0(artifact, step, ctx):
    rows = artifact  # CSV as list of dicts
    if not rows:
        return 0.0
    refs = ctx['ref_DG_bp_ap'], ctx['ref_DG_b_a'], ctx['ref_DG_bp_b1p'], ctx['ref_DG_a_ap']
    cols = ["DG_beta'_to_alpha'", 'DG_beta_to_alpha', "DG_beta'_to_beta1'_plus_alpha", 'DG_alpha_to_alpha']
    tol = step.get('tolerance_abs', 5.0)
    ok = 0
    total = 0
    for row in rows:
        T = float(row['T'])
        for col, func in zip(cols, refs):
            try:
                val = float(row[col])
                ref = func(T)
                if abs(val - ref) <= tol:
                    ok += 1
            except (ValueError, KeyError):
                pass
            total += 1
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='step_03_fit_polynomial') ===
def score_1(artifact, step, ctx):
    import json
    coeffs = artifact
    if not isinstance(coeffs, dict):
        return 0.0
    ref = ctx['poly_ref']
    tols = step.get('tolerances', {})
    keys = ['constant', 'T', 'T2', 'T3']
    if all(k in coeffs for k in keys):
        ok = 0
        for k in keys:
            try:
                v = float(coeffs[k])
                r = float(ref[k])
                t = float(tols.get(k, 0.0))
                if abs(v - r) <= t:
                    ok += 1
            except (ValueError, KeyError):
                pass
        return ok / 4 if ok > 0 else 0.0
    return 0.0


_SCORERS = {
    'step_02_driving_forces': score_0,
    'step_03_fit_polynomial': score_1,
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
