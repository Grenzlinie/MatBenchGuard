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
    def prepare(outputs_dir, spec):
        steps = spec.get("steps", [])
        ref_neutral = None
        ref_doping = None
        for step in steps:
            if step["id"] == "step_03_poisson_neutral":
                ref_neutral = step.get("reference", {})
            elif step["id"] == "step_05_poisson_doping":
                ref_doping = step.get("reference", {})
        return {"ref_neutral": ref_neutral, "ref_doping": ref_doping}


# === block: score_0 (check id='step_03_poisson_neutral') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    ref = ctx["ref_neutral"]
    if not ref:
        return 0.0
    tol = step.get("tolerance_abs", 0.02)
    mat_expected = list(ref.keys())
    n_expected = len(mat_expected)
    if n_expected == 0:
        return 0.0
    rows_by_mat = {}
    for row in artifact:
        mat = row.get("material", "").strip()
        rows_by_mat[mat] = row
    correct_fields = 0
    total_fields = 4 * n_expected
    for mat in mat_expected:
        expected = ref[mat]
        row = rows_by_mat.get(mat)
        if not row:
            continue
        for field in ["v_zx", "v_zy", "v_yx", "v_xy"]:
            try:
                val = float(row.get(field, "NaN"))
                target = float(expected[field])
                if abs(val - target) <= tol:
                    correct_fields += 1
            except (ValueError, TypeError):
                pass
    return correct_fields / total_fields if total_fields > 0 else 0.0


# === block: score_1 (check id='step_05_poisson_doping') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        ref = ctx["ref_doping"]
        doses = ref.get("doping_electrons_per_atom", [])
        expected_v = ref.get("v_zy", [])
        tol = step.get("tolerance_abs", 0.05)
        mapping = {}
        for row in artifact:
            try:
                d = float(row.get("doping_electrons_per_atom", "NaN"))
                v = float(row.get("v_zy", "NaN"))
                mapping[d] = v
            except (ValueError, TypeError):
                continue
        correct = 0
        for d_target, v_target in zip(doses, expected_v):
            closest = None
            min_diff = float('inf')
            for d in mapping:
                diff = abs(d - d_target)
                if diff < min_diff:
                    min_diff = diff
                    closest = d
            if closest is not None and min_diff <= 0.005:
                if abs(mapping[closest] - v_target) <= tol:
                    correct += 1
        return correct / len(doses) if doses else 0.0


# === block: score_2 (check id='step_07_poisson_strain') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        tol = step.get("tolerance_abs", 0.05)
        low_ref = step.get("expected_low", {})
        high_ref = step.get("expected_high", {})
        sign_eps = step.get("sign_change_eps", 0.06)
        eps_vals = []
        vzx_vals = []
        for row in artifact:
            try:
                e = float(row.get("strain_eps_x", "NaN"))
                v = float(row.get("v_zx", "NaN"))
                eps_vals.append(e)
                vzx_vals.append(v)
            except (ValueError, TypeError):
                continue
        if len(eps_vals) == 0:
            return 0.0
        def closest_val(target, xs, ys):
            idx = min(range(len(xs)), key=lambda i: abs(xs[i] - target))
            return xs[idx], ys[idx]
        low_eps, low_v = closest_val(low_ref["eps_x"], eps_vals, vzx_vals)
        high_eps, high_v = closest_val(high_ref["eps_x"], eps_vals, vzx_vals)
        score = 0.0
        if abs(low_v - low_ref["v_zx"]) <= tol:
            score += 0.3
        if abs(high_v - high_ref["v_zx"]) <= tol:
            score += 0.3
        pos_before = any(v > 0.0 for e, v in zip(eps_vals, vzx_vals) if e <= sign_eps + 0.01)
        neg_after = any(v < 0.0 for e, v in zip(eps_vals, vzx_vals) if e >= sign_eps - 0.01)
        if pos_before and neg_after:
            score += 0.4
        return score


_SCORERS = {
    'step_03_poisson_neutral': score_0,
    'step_05_poisson_doping': score_1,
    'step_07_poisson_strain': score_2,
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
