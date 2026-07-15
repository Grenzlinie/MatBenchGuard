import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    return {"steps": spec.get("steps", [])}


# === block: score_0 (check id='bulk_soec') ===
def score_0(artifact, step, ctx):
    if "bulk_soec" not in artifact: return 0.0
    vals = artifact["bulk_soec"]
    target = step.get("target", [183.3, 159.4, 44.3])
    tol_rel = step.get("tolerance_relative", 0.05)
    if len(vals) != len(target): return 0.0
    max_err = 0.0
    for v, t in zip(vals, target):
        if t == 0: return 0.0 if v != 0 else 0.0
        err = abs(v - t) / abs(t)
        if err > max_err: max_err = err
    return 1.0 if max_err <= tol_rel else 0.0


# === block: score_1 (check id='bulk_toec') ===
def score_1(artifact, step, ctx):
    if "bulk_toec" not in artifact: return 0.0
    vals = artifact["bulk_toec"]
    target = step.get("target", [-998.8, -1487.3, 1505.1, -191.4, -5032.2, -200.0])
    tol_rel = step.get("tolerance_relative", 0.10)
    if len(vals) != len(target): return 0.0
    max_err = 0.0
    for v, t in zip(vals, target):
        if t == 0: return 0.0 if v != 0 else 0.0
        err = abs(v - t) / abs(t)
        if err > max_err: max_err = err
    return 1.0 if max_err <= tol_rel else 0.0


# === block: score_2 (check id='core_y_c') ===
def score_2(artifact, step, ctx):
    if "core_young_modulus_x" not in artifact: return 0.0
    val = artifact["core_young_modulus_x"]
    target = step.get("target", 140.80)
    tol_abs = step.get("tolerance_abs", 7.0)
    return 1.0 if abs(val - target) <= tol_abs else 0.0


# === block: score_3 (check id='core_y2_c') ===
def score_3(artifact, step, ctx):
    if "core_young_modulus_2nd_x" not in artifact: return 0.0
    val = artifact["core_young_modulus_2nd_x"]
    target = step.get("target", -827.7)
    tol_abs = step.get("tolerance_abs", 82.77)
    return 1.0 if abs(val - target) <= tol_abs else 0.0


# === block: score_4 (check id='surface_y_s') ===
def score_4(artifact, step, ctx):
    if "surface_young_modulus_x" not in artifact: return 0.0
    val = artifact["surface_young_modulus_x"]
    target = step.get("target", 2.73)
    tol_abs = step.get("tolerance_abs", 0.2)
    return 1.0 if abs(val - target) <= tol_abs else 0.0


# === block: score_5 (check id='surface_y2_s') ===
def score_5(artifact, step, ctx):
    if "surface_young_modulus_2nd_x" not in artifact: return 0.0
    val = artifact["surface_young_modulus_2nd_x"]
    target = step.get("target", 4.11)
    tol_abs = step.get("tolerance_abs", 1.0)
    return 1.0 if abs(val - target) <= tol_abs else 0.0


# === block: score_6 (check id='surface_sigma') ===
def score_6(artifact, step, ctx):
    if "surface_eigenstress_x" not in artifact: return 0.0
    val = artifact["surface_eigenstress_x"]
    target = step.get("target", 1.53)
    tol_abs = step.get("tolerance_abs", 0.2)
    return 1.0 if abs(val - target) <= tol_abs else 0.0


# === block: score_7 (check id='direct_modulus') ===
def score_7(artifact, step, ctx):
    if "Y_n_direct_3nm" not in artifact: return 0.0
    val = artifact["Y_n_direct_3nm"]
    target = step.get("target", 154.0)
    tol_abs = step.get("tolerance_abs", 7.7)
    return 1.0 if abs(val - target) <= tol_abs else 0.0


# === block: score_8 (check id='scaling_selfconsistency') ===
def score_8(artifact, step, ctx):
    h = step.get("thickness_nm", 3.0)
    # required fields
    for k in ["core_young_modulus_x", "core_young_modulus_2nd_x", "surface_young_modulus_x", "surface_young_modulus_2nd_x", "surface_eigenstress_x", "Y_n_scaling_3nm"]:
        if k not in artifact: return 0.0
    Yxc = artifact["core_young_modulus_x"]
    Yx2c = artifact["core_young_modulus_2nd_x"]
    Yxs = artifact["surface_young_modulus_x"]
    Yx2s = artifact["surface_young_modulus_2nd_x"]
    sigmas0 = artifact["surface_eigenstress_x"]
    Y_n_submitted = artifact["Y_n_scaling_3nm"]
    # compute eps_ini via eq. 4b
    a = h * Yx2c + 2.0 * Yx2s
    b = h * Yxc + 2.0 * Yxs
    # ensure denominator not zero
    if a == 0: return 0.0
    disc = b*b - 8.0 * sigmas0 * a
    if disc < 0: return 0.0
    eps_ini = (-b + math.sqrt(disc)) / (2.0 * a)
    # nominal modulus via eq. 4a
    Y_n_computed = Yxc + 2.0 * Yxs / h + 2.0 * (Yx2c + 2.0 * Yx2s / h) * eps_ini
    tol_gpa = step.get("tolerance_gpa", 0.1)
    return 1.0 if abs(Y_n_computed - Y_n_submitted) <= tol_gpa else 0.0


_SCORERS = {
    'bulk_soec': score_0,
    'bulk_toec': score_1,
    'core_y_c': score_2,
    'core_y2_c': score_3,
    'surface_y_s': score_4,
    'surface_y2_s': score_5,
    'surface_sigma': score_6,
    'direct_modulus': score_7,
    'scaling_selfconsistency': score_8,
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
