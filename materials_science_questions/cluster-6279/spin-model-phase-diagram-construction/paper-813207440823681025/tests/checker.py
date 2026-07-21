import os
import json
import csv

# === author imports / helpers ===
import json, csv, os, math

def gamma_hh(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1 or abs(1-u) < 1e-12:
        return 0.0
    denom = k*k * (1.0 - u)
    if abs(denom) < 1e-15:
        return 0.0
    b = - (rho - rho * u - 1.0) / denom
    c = - u * rho_x * rho_y / (k**4 * (1.0 - u))
    disc = b*b - 4.0*c
    if disc < 0:
        return 0.0
    sqrt_disc = math.sqrt(disc)
    g1 = (-b + sqrt_disc) / 2.0
    g2 = (-b - sqrt_disc) / 2.0
    g = max(g1, g2)
    max_possible = min(rho_x, rho_y) / (k*k)
    if g < 0:
        g = 0.0
    elif g > max_possible:
        g = max_possible
    return g

def free_energy(rho_x, rho_y, u, k):
    rho = rho_x + rho_y
    if rho <= 0 or u >= 1:
        return 0.0
    g = gamma_hh(rho_x, rho_y, u, k)
    gkk = g * k * k
    term1 = 0.0
    if rho_x > 0:
        term1 += rho_x * math.log(rho_x)
    if rho_y > 0:
        term1 += rho_y * math.log(rho_y)
    term1 *= -(k-1)/k
    term2 = 0.0
    for ri in [rho_x, rho_y]:
        arg = 1.0 - (k-1)*ri/k
        if arg <= 0:
            return 1e12
        term2 += arg * math.log(arg)
    term3 = 0.0
    for ri in [rho_x, rho_y]:
        arg = ri - gkk
        if arg <= 0:
            return 1e12
        term3 += arg * math.log(arg)
    term4 = 1.0 - rho + gkk
    if term4 <= 0:
        return 1e12
    term4 = term4 * math.log(term4)
    term5 = - rho/k * math.log(k)
    term6 = 0.0
    if gkk > 0 and u > 0:
        term6 = gkk * math.log(gkk / u)
    return term1 + term2 + term3 + term4 + term5 + term6

def compute_critical_densities(k, u):
    # scan rho and find sign change of A2
    if u <= 0 or u >= 1:
        return (None, None)
    rho_min = 0.01
    rho_max = 0.99
    step = 0.0005
    delta = 1e-6
    prev_A2 = None
    transitions = []
    rho = rho_min
    while rho <= rho_max:
        if rho <= 0 or rho >= 1:
            rho += step
            continue
        # compute A2 by perturbation
        f0 = free_energy(rho/2.0, rho/2.0, u, k)
        if f0 >= 1e11:
            rho += step
            continue
        # small perturbation
        dx = delta
        if rho/2.0 + dx > rho or rho/2.0 - dx < 0:
            rho += step
            continue
        f_pert = free_energy(rho/2.0+dx, rho/2.0-dx, u, k)
        if f_pert >= 1e11:
            rho += step
            continue
        psi = 2*dx/rho
        if psi == 0:
            rho += step
            continue
        A2 = (f_pert - f0) / (psi*psi)
        if prev_A2 is not None:
            if (prev_A2 < 0 and A2 > 0) or (prev_A2 > 0 and A2 < 0):
                transitions.append(rho - step/2.0)  # approximate root position
        prev_A2 = A2
        rho += step
    if len(transitions) == 2:
        return (transitions[0], transitions[1])
    elif len(transitions) == 1:
        # only one transition (maybe only rho_c1)
        return (transitions[0], None)
    else:
        return (None, None)

def extract_critical_from_order_curve(rows):
    # rows: list of dicts with "density" and "order_parameter"
    try:
        densities = [float(r["density"]) for r in rows]
        psis = [float(r["order_parameter"]) for r in rows]
    except (KeyError, ValueError):
        return (None, None)
    threshold = 1e-5
    # find first index where psi > threshold
    idx_start = None
    for idx, psi in enumerate(psis):
        if psi > threshold:
            idx_start = idx
            break
    if idx_start is None or idx_start == 0:
        return (None, None)
    # interpolate to find rho_c1
    rho_prev = densities[idx_start-1]
    rho_curr = densities[idx_start]
    psi_prev = psis[idx_start-1]
    psi_curr = psis[idx_start]
    if psi_curr - psi_prev > 1e-15:
        frac = (0.0 - psi_prev) / (psi_curr - psi_prev)
        rho_c1 = rho_prev + frac * (rho_curr - rho_prev)
    else:
        rho_c1 = rho_prev
    # find last index where psi > threshold
    idx_end = None
    for idx in range(len(psis)-1, -1, -1):
        if psis[idx] > threshold:
            idx_end = idx
            break
    if idx_end is None or idx_end == len(psis)-1:
        return (rho_c1, None)
    rho_curr = densities[idx_end]
    rho_next = densities[idx_end+1]
    psi_curr = psis[idx_end]
    psi_next = psis[idx_end+1]
    if psi_curr - psi_next > 1e-15:
        rho_c2 = rho_curr + (0.0 - psi_next) / (psi_curr - psi_next) * (rho_next - rho_curr)
    else:
        rho_c2 = rho_curr
    return (rho_c1, rho_c2)


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


# === block: score_0 (check id='shape_order') ===
def score_0(artifact, step, ctx):
    try:
        if not isinstance(artifact, list) or len(artifact) < step.get('min_rows', 100):
            return 0.0
        req_cols = step.get('required_columns', ['density','order_parameter'])
        cols = set(artifact[0].keys()) if artifact else set()
        for col in req_cols:
            if col not in cols:
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_1 (check id='shape_phase') ===
def score_1(artifact, step, ctx):
    try:
        if not isinstance(artifact, list) or len(artifact) < step.get('min_rows', 2):
            return 0.0
        req_cols = step.get('required_columns', ['u','rho_c1','rho_c2'])
        cols = set(artifact[0].keys()) if artifact else set()
        for col in req_cols:
            if col not in cols:
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_2 (check id='crit_order') ===
def score_2(artifact, step, ctx):
    k = step.get('k', 6)
    u = step.get('u', 0.15)
    tol_full = step.get('tolerance_relative_full', 0.02)
    tol_zero = step.get('tolerance_relative_zero', 0.10)
    extracted = extract_critical_from_order_curve(artifact)
    rho_c1_agent, rho_c2_agent = extracted
    if rho_c1_agent is None:
        return 0.0
    gold = compute_critical_densities(k, u)
    rho_c1_gold, rho_c2_gold = gold
    if rho_c1_gold is None or rho_c2_gold is None:
        # no nematic phase expected (should not happen for u=0.15,k=6)
        return 0.0
    # compute relative errors
    rel1 = abs(rho_c1_agent - rho_c1_gold) / rho_c1_gold if rho_c1_gold != 0 else 1.0
    rel2 = abs(rho_c2_agent - rho_c2_gold) / rho_c2_gold if rho_c2_gold != 0 else 1.0
    score1 = 1.0 if rel1 <= tol_full else max(0.0, 1.0 - (rel1-tol_full)/(tol_zero-tol_full))
    score2 = 1.0 if rel2 <= tol_full else max(0.0, 1.0 - (rel2-tol_full)/(tol_zero-tol_full))
    return (score1 + score2) / 2.0


# === block: score_3 (check id='crit_phase') ===
def score_3(artifact, step, ctx):
    k = step.get('k', 6)
    tol_full = step.get('tolerance_relative_full', 0.02)
    tol_zero = step.get('tolerance_relative_zero', 0.10)
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    total_errors = []
    for row in artifact:
        try:
            u_val = float(row['u'])
            rho_c1_agent = float(row['rho_c1'])
            rho_c2_agent = float(row['rho_c2'])
        except (KeyError, ValueError):
            return 0.0
        gold = compute_critical_densities(k, u_val)
        rho_c1_gold, rho_c2_gold = gold
        if rho_c1_gold is None or rho_c2_gold is None:
            # if no nematic phase expected but agent reports one
            if rho_c1_agent > 0 or rho_c2_agent > 0:
                # agent should have stopped at u_c
                return 0.0
            continue
        rel1 = abs(rho_c1_agent - rho_c1_gold) / rho_c1_gold if rho_c1_gold != 0 else 1.0
        rel2 = abs(rho_c2_agent - rho_c2_gold) / rho_c2_gold if rho_c2_gold != 0 else 1.0
        total_errors.append((rel1, rel2))
    if not total_errors:
        return 0.0
    avg_rel = sum((r1+r2)/2.0 for r1,r2 in total_errors) / len(total_errors)
    if avg_rel <= tol_full:
        return 1.0
    else:
        return max(0.0, 1.0 - (avg_rel-tol_full)/(tol_zero-tol_full))


_SCORERS = {
    'shape_order': score_0,
    'shape_phase': score_1,
    'crit_order': score_2,
    'crit_phase': score_3,
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
