import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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
    import os, json
    summary_path = os.path.join(outputs_dir, "summary.json")
    ctx = {"solver": None}
    if os.path.exists(summary_path):
        try:
            with open(summary_path) as f:
                summary = json.load(f)
            solver = str(summary.get("solver", "")).strip()
            ctx["solver"] = solver
        except Exception:
            pass
    return ctx


# === block: score_0 (check id='scored_1_profile_varkappa_0_01') ===
def score_0(artifact, step, ctx):
    config = step.get("config", {})
    solver = ctx.get("solver")
    if solver is None:
        return 0.0
    gold = config.get("solver_gold", {}).get(solver, None)
    if gold is None:
        return 0.0

    # Analytical parameters
    kappa = config["kappa_atpct"]
    c0 = config["c0_atpct"]
    R_nm = config["R_nm"]
    G_m = config["G_m"]
    V_m = config["V_m"]
    T = config["T"]
    R_gas = config["R_gas"]
    C11_p = config["C11_p"]
    C12_p = config["C12_p"]
    eps_p = config["eps_p"]
    tol = config["tolerance_abs"]
    max_pen = config["max_deviation_penalty"]

    B_p = (C11_p + 2 * C12_p) / 3.0
    b = -3.0 * eps_p * B_p / (3.0 * B_p + 4.0 * G_m)
    g0 = 6.0 * G_m * V_m * b * b / (R_gas * T)
    k_eff = 100.0 * kappa
    A_atpct = 100.0 * g0 * k_eff

    sq_diff = 0.0
    sq_ref = 0.0
    for row in artifact:
        try:
            r = float(row["r"])
            c_num = float(row["c"])
        except (KeyError, ValueError):
            continue
        if r < R_nm * 0.99:
            continue
        c_ref = c0 - A_atpct * (R_nm / r) ** 6
        sq_diff += (c_num - c_ref) ** 2
        sq_ref += c_ref * c_ref

    if sq_ref == 0.0:
        return 1.0

    L2 = math.sqrt(sq_diff / sq_ref)
    threshold = gold + tol
    if L2 <= threshold:
        return 1.0
    score = max(0.0, 1.0 - (L2 - threshold) / max_pen)
    return score


# === block: score_1 (check id='scored_2_profile_varkappa_0_04') ===
def score_1(artifact, step, ctx):
    config = step.get("config", {})
    solver = ctx.get("solver")
    if solver is None:
        return 0.0
    gold = config.get("solver_gold", {}).get(solver, None)
    if gold is None:
        return 0.0

    kappa = config["kappa_atpct"]
    c0 = config["c0_atpct"]
    R_nm = config["R_nm"]
    G_m = config["G_m"]
    V_m = config["V_m"]
    T = config["T"]
    R_gas = config["R_gas"]
    C11_p = config["C11_p"]
    C12_p = config["C12_p"]
    eps_p = config["eps_p"]
    tol = config["tolerance_abs"]
    max_pen = config["max_deviation_penalty"]

    B_p = (C11_p + 2 * C12_p) / 3.0
    b = -3.0 * eps_p * B_p / (3.0 * B_p + 4.0 * G_m)
    g0 = 6.0 * G_m * V_m * b * b / (R_gas * T)
    k_eff = 100.0 * kappa
    A_atpct = 100.0 * g0 * k_eff

    sq_diff = 0.0
    sq_ref = 0.0
    for row in artifact:
        try:
            r = float(row["r"])
            c_num = float(row["c"])
        except (KeyError, ValueError):
            continue
        if r < R_nm * 0.99:
            continue
        c_ref = c0 - A_atpct * (R_nm / r) ** 6
        sq_diff += (c_num - c_ref) ** 2
        sq_ref += c_ref * c_ref

    if sq_ref == 0.0:
        return 1.0

    L2 = math.sqrt(sq_diff / sq_ref)
    threshold = gold + tol
    if L2 <= threshold:
        return 1.0
    score = max(0.0, 1.0 - (L2 - threshold) / max_pen)
    return score


# === block: score_2 (check id='scored_3_summary_solver_check') ===
def score_2(artifact, step, ctx):
    allowed = step.get("config", {}).get("allowed_solvers", [])
    if not isinstance(artifact, dict):
        return 0.0
    solver = str(artifact.get("solver", "")).strip()
    if solver in allowed:
        return 1.0
    return 0.0


_SCORERS = {
    'scored_1_profile_varkappa_0_01': score_0,
    'scored_2_profile_varkappa_0_04': score_1,
    'scored_3_summary_solver_check': score_2,
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
