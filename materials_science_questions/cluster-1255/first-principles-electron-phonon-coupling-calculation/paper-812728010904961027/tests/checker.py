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
    spec = spec  # the grading_spec dict passed in, not a ctx object
    resistivity_step = None
    distribution_step = None
    for step in spec.get("steps", []):
        if step["id"] == "resistivity":
            resistivity_step = step
        elif step["id"] == "distribution":
            distribution_step = step
    return {
        "resistivity": resistivity_step,
        "distribution": distribution_step
    }


# === block: score_0 (check id='resistivity') ===
def score_0(artifact, step, ctx):
    params = step.get("params", {})
    rho0 = params["rho0"]
    targets = params["targets"]
    tol = params["tolerance_relative"]
    per_point = params.get("score_per_point", 0.2)
    Ts = []
    rhos = []
    for row in artifact:
        try:
            Ts.append(float(row["T"]))
            rhos.append(float(row["rho"]))
        except (KeyError, ValueError):
            return 0.0
    if len(Ts) < 2:
        return 0.0
    def interp(T_val):
        if T_val <= Ts[0]:
            return rhos[0]
        if T_val >= Ts[-1]:
            return rhos[-1]
        for i in range(len(Ts)-1):
            if Ts[i] <= T_val <= Ts[i+1]:
                frac = (T_val - Ts[i]) / (Ts[i+1] - Ts[i])
                return rhos[i] + frac * (rhos[i+1] - rhos[i])
        return rhos[0]
    scores = []
    for tgt in targets:
        T_tgt = tgt["T"]
        delta_exp = tgt["delta_rho"]
        rho_agent = interp(T_tgt)
        delta_agent = rho_agent - rho0
        rel_err = abs(delta_agent - delta_exp) / abs(delta_exp) if abs(delta_exp) > 1e-20 else abs(delta_agent)
        if rel_err <= tol:
            scores.append(1.0)
        else:
            scores.append(0.0)
    return sum(scores) / len(scores)


# === block: score_1 (check id='distribution') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    dip_center_exp = params["dip_center_expected"]
    center_tol = params["dip_center_tolerance"]
    dip_range = params["dip_min_expected_range"]
    dip_depth_min = params["dip_depth_min"]
    monotonic_ranges = params["monotonic_increase_expected"]
    weights = params["score_weights"]
    y_vals = []
    phi_vals = []
    for row in artifact:
        try:
            y = float(row["y"])
            phi = float(row["phi_norm"])
            y_vals.append(y)
            phi_vals.append(phi)
        except (KeyError, ValueError):
            continue
    if len(y_vals) < 10:
        return 0.0
    min_phi = float('inf')
    min_y = None
    for y, phi in zip(y_vals, phi_vals):
        if dip_range[0] <= y <= dip_range[1]:
            if phi < min_phi:
                min_phi = phi
                min_y = y
    dip_exists = (min_y is not None)
    center_score = 1.0 if dip_exists and abs(min_y - dip_center_exp) <= center_tol else 0.0
    mono_scores = []
    for rng in monotonic_ranges:
        lo, hi = rng
        valid = [(y, phi) for y, phi in zip(y_vals, phi_vals) if lo <= y <= hi]
        if len(valid) < 2:
            mono_scores.append(1.0)
            continue
        sorted_valid = sorted(valid, key=lambda x: x[0])
        is_mono = True
        for i in range(1, len(sorted_valid)):
            if sorted_valid[i][1] < sorted_valid[i-1][1] - 1e-9:
                is_mono = False
                break
        mono_scores.append(1.0 if is_mono else 0.0)
    mono_score = sum(mono_scores) / len(mono_scores) if mono_scores else 0.0
    total = (weights["dip_exists"] * (1.0 if dip_exists else 0.0) +
             weights["dip_center"] * center_score +
             weights["monotonic"] * mono_score)
    return min(1.0, total)


_SCORERS = {
    'resistivity': score_0,
    'distribution': score_1,
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
