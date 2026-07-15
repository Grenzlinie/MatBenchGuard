import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, io


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
        "lambda_target": 7.0,
        "omega_target": 1406.0,
        "Tc_target": 327.0,
        "mu_star": 0.089,
        "energy_flat_threshold": 0.002,
        "energy_local_max_tol": 1e-8
    }
    return gold


# === block: score_0 (check id='energy_curve_shape') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, list) or len(data) < 3:
        return 0.0
    points = {}
    for row in data:
        try:
            t = float(row.get("theta_deg"))
            e = float(row.get("total_energy_Ry"))
            points[t] = e
        except (ValueError, TypeError):
            continue
    if not points:
        return 0.0
    def get_nearest(target, pts):
        return pts[min(pts.keys(), key=lambda x: abs(x-target))]
    try:
        e88 = get_nearest(88.0, points)
        e90 = get_nearest(90.0, points)
        e92 = get_nearest(92.0, points)
        local_max = (e90 > e88 - ctx.get("energy_local_max_tol", 1e-8)) and \
                    (e90 > e92 - ctx.get("energy_local_max_tol", 1e-8))
    except (KeyError, ValueError):
        local_max = False
    basin_pts = {t: e for t, e in points.items() if 87.0 <= t <= 93.0}
    if basin_pts:
        rng = max(basin_pts.values()) - min(basin_pts.values())
        thr = ctx.get("energy_flat_threshold", 0.002)
        if rng <= thr:
            flat_score = 1.0
        elif rng <= 3 * thr:
            flat_score = 0.5
        else:
            flat_score = 0.0
    else:
        flat_score = 0.0
    score = 0.6 * (1.0 if local_max else 0.0) + 0.4 * flat_score
    return score


# === block: score_1 (check id='superconductivity_params') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    required = ["lambda", "omega_log_K", "Tc_K", "pressure_GPa"]
    if not all(k in artifact for k in required):
        return 0.0
    l = float(artifact["lambda"])
    w = float(artifact["omega_log_K"])
    tc_sub = float(artifact["Tc_K"])
    mu = ctx.get("mu_star", 0.089)
    try:
        denom = l - mu * (1.0 + 0.62 * l)
        exp_arg = -1.04 * (1.0 + l) / denom
        exp_val = math.exp(exp_arg) if exp_arg <= 700.0 else float('inf')
        tc_ad = (w / 1.2) * exp_val
    except (ZeroDivisionError, ValueError):
        tc_ad = -1.0
    consistency = 1.0 if abs(tc_ad - tc_sub) <= max(1e-3, 1e-3 * abs(tc_sub)) else 0.0
    gold_l = ctx.get("lambda_target", 7.0)
    gold_w = ctx.get("omega_target", 1406.0)
    gold_tc = ctx.get("Tc_target", 327.0)
    rel_tol = 0.2
    lambda_ok = 1.0 if abs(l - gold_l) <= rel_tol * gold_l else 0.0
    omega_ok = 1.0 if abs(w - gold_w) <= rel_tol * gold_w else 0.0
    tc_ok = 1.0 if abs(tc_sub - gold_tc) <= 50.0 else 0.0
    score = 0.3 * consistency + 0.3 * lambda_ok + 0.2 * omega_ok + 0.2 * tc_ok
    return score


_SCORERS = {
    'energy_curve_shape': score_0,
    'superconductivity_params': score_1,
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
