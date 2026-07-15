import os
import json
import csv

# === author imports / helpers ===
import math, cmath


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


# === block: score_0 (check id='step_1_epis') ===
def score_0(artifact, step, ctx):
    try:
        j1 = float(artifact.get('J2_1', None))
        j2 = float(artifact.get('J2_2', None))
    except (TypeError, ValueError):
        return 0.0
    rel_tol = float(step.get('relative_tolerance', 0.20))
    j1t = float(step.get('J2_1_target', 0.004882))
    j2t = float(step.get('J2_2_target', -0.0001463))
    def rel_err(val, tgt):
        if tgt == 0.0:
            return abs(val - tgt)
        return abs((val - tgt)/tgt)
    s1 = 1.0 if rel_err(j1, j1t) <= rel_tol else 0.0
    s2 = 1.0 if rel_err(j2, j2t) <= rel_tol else 0.0
    return 0.5*s1 + 0.5*s2


# === block: score_1 (check id='step_2_fourier') ===
def score_1(artifact, step, ctx):
    required_keys = {'J000_over_kB', 'J100_over_kB'}
    if not isinstance(artifact, dict) or not required_keys.issubset(artifact.keys()):
        return 0.0
    for k in required_keys:
        v = artifact.get(k)
        if v is None or not isinstance(v, (int, float)):
            return 0.0
    return 1.0


# === block: score_2 (check id='step_3_t_i_minus') ===
def score_2(artifact, step, ctx):
    import json, os
    epis_path = '/app/outputs/step_01_epis.json'
    if not os.path.exists(epis_path):
        return 0.0
    with open(epis_path) as f:
        epis = json.load(f)
    j2_1 = epis.get('J2_1', None)
    j2_2 = epis.get('J2_2', None)
    if j2_1 is None or j2_2 is None:
        return 0.0
    Ry_to_K = 157887.663
    J100 = 4.0 * (-4.0*j2_1 + 6.0*j2_2) * Ry_to_K
    c1 = 0.10
    c2 = 0.25
    def T_i_minus(c):
        return J100 * c * (1.0 - c)
    t1 = T_i_minus(c1)
    t2 = T_i_minus(c2)
    targets = step.get('targets', {})
    target1 = targets.get('c_0.10', 1159.6032)
    target2 = targets.get('c_0.25', 2415.84)
    rel_tol = float(step.get('relative_tolerance', 0.10))
    def score_val(val, tgt):
        if tgt == 0.0:
            return 0.0
        err = abs((val - tgt)/tgt)
        return 1.0 if err <= rel_tol else 0.0
    s1 = score_val(t1, target1)
    s2 = score_val(t2, target2)
    return 0.5*s1 + 0.5*s2


# === block: score_3 (check id='step_4_eta_eq') ===
def score_3(artifact, step, ctx):
    import json, os, math
    epis_path = '/app/outputs/step_01_epis.json'
    if not os.path.exists(epis_path):
        return 0.0
    with open(epis_path) as f:
        epis = json.load(f)
    j2_1 = epis.get('J2_1', None)
    j2_2 = epis.get('J2_2', None)
    if j2_1 is None or j2_2 is None:
        return 0.0
    Ry_to_K = 157887.663
    J000 = 4.0 * (12.0*j2_1 + 6.0*j2_2) * Ry_to_K
    J100 = 4.0 * (-4.0*j2_1 + 6.0*j2_2) * Ry_to_K
    c = float(step.get('c', 0.25))
    T = float(step.get('T', 1000.0))
    kB = 1.0  # in K units, since J are already in K
    # free energy of ordered phase as function of eta (eta_max = 1)
    def F_ord(eta):
        if eta < -1.0 or eta > 1.0:
            return 1e30
        # formula from paper with eta_n = eta
        c2 = c*c
        term1 = 0.5 * (J000 + 3.0 * J100 * eta*eta) * c2
        # entropy term
        t1 = c * (1.0 - eta)
        t2 = c * (1.0 + 3.0*eta)
        # clamp for log
        eps = 1e-12
        if t1 <= 0.0 or t1 >= 1.0: return 1e30
        if t2 <= 0.0 or t2 >= 1.0: return 1e30
        entropy = 0.0
        # term 3*c*(1-eta)*ln(c*(1-eta))
        if t1 > 0:
            entropy += 3.0 * t1 * math.log(t1)
        # term 3*(1-c*(1-eta))*ln(1-c*(1-eta))
        arg = 1.0 - t1
        if arg > 0:
            entropy += 3.0 * arg * math.log(arg)
        # term c*(1+3*eta)*ln(c*(1+3*eta))
        if t2 > 0:
            entropy += t2 * math.log(t2)
        # term (1-c*(1+3*eta))*ln(1-c*(1+3*eta))
        arg2 = 1.0 - t2
        if arg2 > 0:
            entropy += arg2 * math.log(arg2)
        entropy_term = (T / 4.0) * entropy
        return term1 + entropy_term
    # grid search
    best_eta = 0.0
    best_f = float('inf')
    N = 400
    for i in range(N+1):
        eta = i / float(N)
        f = F_ord(eta)
        if f < best_f:
            best_f = f
            best_eta = eta
    target = float(step.get('target_eta_eq', 0.95))
    tol = float(step.get('abs_tolerance', 0.05))
    diff = abs(best_eta - target)
    if diff <= tol:
        return 1.0
    elif diff <= 3*tol:
        return 0.5
    else:
        return 0.0


# === block: score_4 (check id='step_5_phase_boundaries') ===
def score_4(artifact, step, ctx):
    import json, os, math
    epis_path = '/app/outputs/step_01_epis.json'
    if not os.path.exists(epis_path):
        return 0.0
    with open(epis_path) as f:
        epis = json.load(f)
    j2_1 = epis.get('J2_1', None)
    j2_2 = epis.get('J2_2', None)
    if j2_1 is None or j2_2 is None:
        return 0.0
    Ry_to_K = 157887.663
    J000 = 4.0 * (12.0*j2_1 + 6.0*j2_2) * Ry_to_K
    J100 = 4.0 * (-4.0*j2_1 + 6.0*j2_2) * Ry_to_K
    T = float(step.get('T', 1000.0))
    kB = 1.0  # J in K
    def F_dis(c):
        if c <= 0.0 or c >= 1.0:
            return 1e30
        term1 = 0.5 * J000 * c * c
        entropy = c * math.log(c) + (1.0-c) * math.log(1.0-c)
        return term1 + T * entropy
    def F_ord_min(c):
        if c <= 0.0 or c >= 1.0:
            return 1e30
        # minimize over eta
        best = float('inf')
        N = 100
        for i in range(N+1):
            eta = i / float(N)
            # check allowed eta: must satisfy occupation probabilities in [0,1]
            t1 = c * (1.0 - eta)
            t2 = c * (1.0 + 3.0*eta)
            eps = 1e-12
            if t1 <= eps or t1 >= 1.0-eps or t2 <= eps or t2 >= 1.0-eps:
                continue
            term1 = 0.5 * (J000 + 3.0 * J100 * eta*eta) * c * c
            entropy = 0.0
            if t1 > 0:
                entropy += 3.0 * t1 * math.log(t1)
            arg1 = 1.0 - t1
            if arg1 > 0:
                entropy += 3.0 * arg1 * math.log(arg1)
            if t2 > 0:
                entropy += t2 * math.log(t2)
            arg2 = 1.0 - t2
            if arg2 > 0:
                entropy += arg2 * math.log(arg2)
            f = term1 + (T / 4.0) * entropy
            if f < best:
                best = f
        return best
    # common tangent on composition grid
    cmin = 0.01
    cmax = 0.4
    Nc = 150
    cgrid = [cmin + (cmax-cmin)*i/(Nc-1) for i in range(Nc)]
    dis_arr = [F_dis(c) for c in cgrid]
    ord_arr = [F_ord_min(c) for c in cgrid]
    best_pair = None
    best_max_res = float('inf')
    for i in range(Nc):
        for j in range(i+1, Nc):
            m = (ord_arr[j] - dis_arr[i]) / (cgrid[j] - cgrid[i])
            line_i = dis_arr[i]
            max_res = 0.0
            # check all points
            ok = True
            for k in range(Nc):
                c = cgrid[k]
                line_val = line_i + m * (c - cgrid[i])
                res1 = dis_arr[k] - line_val
                res2 = ord_arr[k] - line_val
                if res1 < -1e-12 or res2 < -1e-12:
                    ok = False
                    break
                if res1 > max_res:
                    max_res = res1
                if res2 > max_res:
                    max_res = res2
            if ok and max_res < best_max_res:
                best_max_res = max_res
                best_pair = (i, j)
    if best_pair is None:
        return 0.0
    i, j = best_pair
    c_alpha = cgrid[i]
    c_delta = cgrid[j]
    target_alpha = float(step.get('target_alpha_sol', 0.08))
    target_delta = float(step.get('target_delta_prime', 0.20))
    tol = float(step.get('abs_tolerance', 0.02))
    def score_comp(val, target):
        diff = abs(val - target)
        if diff <= tol:
            return 1.0
        elif diff <= 3*tol:
            return 0.5
        else:
            return 0.0
    s_alpha = score_comp(c_alpha, target_alpha)
    s_delta = score_comp(c_delta, target_delta)
    return 0.5*s_alpha + 0.5*s_delta


_SCORERS = {
    'step_1_epis': score_0,
    'step_2_fourier': score_1,
    'step_3_t_i_minus': score_2,
    'step_4_eta_eq': score_3,
    'step_5_phase_boundaries': score_4,
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
