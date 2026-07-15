import os
import json
import csv

# === author imports / helpers ===
import json, csv, math


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


# === block: score_0 (check id='step_01_magnetoelastic_params') ===
def score_0(artifact, step, ctx):
    if artifact is None: return 0.0
    dJ = artifact.get('dJ_deta')
    stress = artifact.get('stress_model')
    if not isinstance(dJ, list) or len(dJ) != 6 or not isinstance(stress, list) or len(stress) != 6:
        return 0.0
    gold = step.get('gold', {})
    tols = step.get('tolerances', {})
    gold_dJ = gold['dJ_deta']
    gold_stress = gold['stress_model']
    tol_dJ = tols['dJ_deta_tol']
    tol_stress_nz = tols['stress_nonzero_tol']
    tol_stress_z = tols['stress_zero_tol']

    score_sum = 0.0
    for i in range(6):
        delta = abs(dJ[i] - gold_dJ[i])
        s = max(0.0, 1.0 - delta / tol_dJ)
        score_sum += s
    for i in range(6):
        g = gold_stress[i]
        v = stress[i]
        tol = tol_stress_nz if abs(g) > 1e-9 else tol_stress_z
        s = 1.0 if abs(v - g) < tol else 0.0
        score_sum += s
    return score_sum / 12.0


# === block: score_1 (check id='step_02_polarization_contributions') ===
def score_1(artifact, step, ctx):
    if artifact is None: return 0.0
    keys = ['model_lattice','model_electronic','model_ionic','dft_lattice','dft_electronic','dft_ionic']
    if not all(k in artifact for k in keys):
        return 0.0
    gold = step.get('gold', {})
    tol = step.get('tolerance', 0.2)
    score_sum = 0.0
    for k in keys:
        val = artifact[k]
        g = gold[k]
        delta = abs(val - g)
        s = max(0.0, 1.0 - delta / tol)
        score_sum += s
    return score_sum / 6.0


# === block: score_2 (check id='step_03_field_dependence') ===
def score_2(artifact, step, ctx):
    if artifact is None: return 0.0
    rows = artifact  # list of dicts
    H_vals = step['H_values']
    points = {}
    for r in rows:
        try:
            h = float(r['H_T'])
            dp = float(r['DeltaP_muC_cm2'])
            points[h] = dp
        except (ValueError, KeyError):
            continue
    if not all(h in points for h in H_vals):
        return 0.0

    # score Delta P at 20 T
    gold_20 = step['gold_deltaP_20T']
    tol_20 = step['tolerance_20T']
    dp20 = points[20.0]
    err_20 = abs(dp20 - gold_20)
    score_20 = max(0.0, 1.0 - err_20 / tol_20)

    # quadratic consistency
    k_ref = dp20 / (20.0 ** 2) if dp20 != 0 else 0.0
    rel_tol = step['quadratic_rel_tol']
    quad_scores = []
    for h in [5.0, 10.0, 15.0, 20.0]:
        pred = k_ref * (h ** 2)
        actual = points[h]
        err = abs(actual - pred)
        denom = max(abs(pred), 1e-15)
        s = max(0.0, 1.0 - err / (rel_tol * denom))
        quad_scores.append(s)
    score_quad = sum(quad_scores) / len(quad_scores)

    return 0.5 * score_20 + 0.5 * score_quad


_SCORERS = {
    'step_01_magnetoelastic_params': score_0,
    'step_02_polarization_contributions': score_1,
    'step_03_field_dependence': score_2,
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
