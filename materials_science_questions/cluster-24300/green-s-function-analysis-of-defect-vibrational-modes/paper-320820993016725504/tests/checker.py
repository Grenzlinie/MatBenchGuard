import os
import json
import csv

# === author imports / helpers ===
import json
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
    artifact_path = os.path.join(outputs_dir, "dispersion_results.json")
    with open(artifact_path, 'r') as f:
        artifact = json.load(f)
    return {"artifact": artifact}


# === block: score_0 (check id='step_dispersion_points') ===
def score_0(artifact, step, ctx):
    params = ctx["artifact"]["parameters"]
    points = ctx["artifact"]["points"]
    J_S = float(params["J_S"])
    xi = float(params["xi"])
    beta = float(params["beta"])
    # H is assumed 0 per task example; if non-zero, further constants would be needed, but we verify consistency anyway
    H = float(params.get("H", 0.0))
    g_prime_over_g = float(params.get("g_prime_over_g", 1.0))
    gamma = float(params.get("gamma", 0.0))
    tol = float(step.get("tolerance_rel", 1e-6))

    ok = 0
    total = 0
    for pt in points:
        kx = float(pt["kappa_x"])
        kz = float(pt["kappa_z"])
        ek = J_S * (4.0 - 2.0*math.cos(kx) - 2.0*math.cos(kz))
        # gamma' = gamma - xi
        gamma_prime = gamma - xi
        # epsilon formula; with H=0 the g*mu0*H term vanishes
        epsilon = - (xi * ek) / J_S
        # compute expected values
        if abs(epsilon - 1.0) < 1e-12:
            # degenerate; avoid division by zero
            continue
        E_plus_exp = ek + (2.0 * J_S * epsilon**2) / (2.0 * (epsilon - 1.0))
        denom_am = epsilon + 1.0 - 2.0*beta
        if abs(denom_am) < 1e-12:
            continue
        E_minus_exp = ek + (2.0 * J_S * (epsilon + 2.0*(1.0 - beta))**2) / (2.0 * denom_am)
        E_plus_ag = float(pt["E_plus"])
        E_minus_ag = float(pt["E_minus"])
        rel_plus = abs(E_plus_exp - E_plus_ag) / max(abs(E_plus_exp), 1e-12)
        rel_minus = abs(E_minus_exp - E_minus_ag) / max(abs(E_minus_exp), 1e-12)
        total += 2
        if rel_plus <= tol:
            ok += 1
        if rel_minus <= tol:
            ok += 1
    if total == 0:
        return 0.0
    return min(1.0, ok / total)


# === block: score_1 (check id='step_localization_condition') ===
def score_1(artifact, step, ctx):
    params = ctx["artifact"]["parameters"]
    points = ctx["artifact"]["points"]
    cond = ctx["artifact"]["condition_check"]
    J_S = float(params["J_S"])
    xi = float(params["xi"])
    beta = float(params["beta"])

    sm_true_all = True
    am_true_all = True
    for pt in points:
        kx = float(pt["kappa_x"])
        kz = float(pt["kappa_z"])
        ek = J_S * (4.0 - 2.0*math.cos(kx) - 2.0*math.cos(kz))
        epsilon = - (xi * ek) / J_S
        sm_ok = (epsilon <= 0.0 or epsilon >= 2.0)
        am_ok = (epsilon <= 2.0*(beta - 1.0) or epsilon >= 2.0*beta)
        if not sm_ok:
            sm_true_all = False
        if not am_ok:
            am_true_all = False

    agent_sm = bool(cond.get("SM_localization_condition", False))
    agent_am = bool(cond.get("AM_localization_condition", False))
    score = 0.0
    if agent_sm == sm_true_all:
        score += 0.5
    if agent_am == am_true_all:
        score += 0.5
    return score


# === block: score_2 (check id='step_beta_independence') ===
def score_2(artifact, step, ctx):
    params = ctx["artifact"]["parameters"]
    beta_check = ctx["artifact"]["beta_independence_check"]
    J_S = float(params["J_S"])
    xi = float(params["xi"])
    kx = float(beta_check["kappa_x"])
    kz = float(beta_check["kappa_z"])
    ek = J_S * (4.0 - 2.0*math.cos(kx) - 2.0*math.cos(kz))
    epsilon = - (xi * ek) / J_S
    if abs(epsilon - 1.0) < 1e-12:
        return 0.0  # degenerate
    E_plus_const = ek + (2.0 * J_S * epsilon**2) / (2.0 * (epsilon - 1.0))

    tol = 1e-6
    agent_vals = [float(v) for v in beta_check["E_plus_values"]]
    agent_constant = bool(beta_check.get("constant_confirmed", False))

    # check constancy of agent values among themselves
    max_diff = max(agent_vals) - min(agent_vals) if agent_vals else 0.0
    constant_ok = (max_diff <= tol)

    # check each agent value against recomputed constant
    match_frac = 0.0
    if agent_vals:
        match_count = sum(1.0 for v in agent_vals if abs(v - E_plus_const) / max(abs(E_plus_const), 1e-12) <= tol)
        match_frac = match_count / len(agent_vals)

    score = 0.5 * match_frac
    if constant_ok == agent_constant:
        score += 0.5
    return min(1.0, score)


_SCORERS = {
    'step_dispersion_points': score_0,
    'step_localization_condition': score_1,
    'step_beta_independence': score_2,
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
