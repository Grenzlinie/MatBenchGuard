import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='step_cyclic') ===
def score_0(artifact, step, ctx):
    def _toleranced_score(value, target, rel_tol):
        if abs(target) < 1e-12:
            return 1.0 if abs(value) < 1e-12 else 0.0
        rel_err = abs(value - target) / abs(target)
        if rel_err <= rel_tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol)

    target_stress = float(step.get('target_peak_stress_mbar', 0.0093))
    tol_stress = float(step.get('tolerance_peak_stress_relative', 0.05))
    plastic_thresh = float(step.get('plastic_strain_threshold', 1e-8))

    peak_stress = max(float(r['axial_stress_Mbar']) for r in artifact)
    stress_score = _toleranced_score(peak_stress, target_stress, tol_stress)

    plastic_vals = [float(r['axial_plastic_strain']) for r in artifact]
    plastic_ok = all(abs(v) < plastic_thresh for v in plastic_vals)
    plastic_score = 1.0 if plastic_ok else 0.0

    return 0.9 * stress_score + 0.1 * plastic_score


# === block: score_1 (check id='step_compressive') ===
def score_1(artifact, step, ctx):
    def _toleranced_score(value, target, rel_tol):
        if abs(target) < 1e-12:
            return 1.0 if abs(value) < 1e-12 else 0.0
        rel_err = abs(value - target) / abs(target)
        if rel_err <= rel_tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (rel_err - rel_tol) / rel_tol)

    target_stress = float(step.get('target_stress_mbar', -0.51))
    tol_stress = float(step.get('tolerance_stress_relative', 0.05))
    target_c_ratio = float(step.get('target_c_over_c0', 5.9))
    c0 = float(step.get('c0_cm', 0.0014))
    tol_c = float(step.get('tolerance_c_relative', 0.10))

    target_strain = -0.2
    closest_row = None
    min_diff = float('inf')
    for row in artifact:
        diff = abs(float(row['strain']) - target_strain)
        if diff < min_diff:
            min_diff = diff
            closest_row = row

    if closest_row is None or min_diff > 1e-6:
        return 0.0

    stress_val = float(closest_row['axial_stress_Mbar'])
    radius_val = float(closest_row['mean_crack_radius_cm'])
    c_ratio = radius_val / c0

    stress_score = _toleranced_score(stress_val, target_stress, tol_stress)
    crack_score = _toleranced_score(c_ratio, target_c_ratio, tol_c)

    return 0.5 * stress_score + 0.5 * crack_score


_SCORERS = {
    'step_cyclic': score_0,
    'step_compressive': score_1,
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
