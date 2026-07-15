import os
import json
import csv

# === author imports / helpers ===
import csv, math

q = 3
sigma = 5
theta_c_val = ((q - 1)**((sigma - 1)/(sigma + 1)) - 1) / (q - 2)

def potts_probs(theta):
    if theta <= 0.0:
        return 1.0, 1.0
    if theta >= theta_c_val:
        p1 = 1.0 / q
        p11 = 1.0 / (1.0 + (q - 1) * theta)
        return p1, p11
    a = 1.0 / theta
    def g(r):
        return r - ((a * r + q - 1) / (r + a + q - 2))**sigma
    low = 1.000001
    high = max(2.0, a**sigma * 2)
    while g(high) <= 0:
        high *= 2.0
    for _ in range(200):
        mid = (low + high) / 2.0
        if g(mid) <= 0:
            low = mid
        else:
            high = mid
    r = (low + high) / 2.0
    p1 = r / (r + q - 1)
    p11 = a * r / (a * r + q - 1)
    return p1, p11

def percolation_full(theta):
    p1, p11 = potts_probs(theta)
    p_b = 1.0 - theta
    c = p_b * p11
    sigma_c = sigma * c
    if sigma_c <= 1.0:
        Q = 1.0
    else:
        def h(Q_val):
            return Q_val - (1.0 - c) - c * (Q_val**sigma)
        lo = 0.0
        hi = 1.0
        while h(lo) * h(hi) > 0:
            lo = hi
            hi = 2.0 * hi
        for _ in range(200):
            mid = (lo + hi) / 2.0
            if h(mid) * h(lo) > 0:
                lo = mid
            else:
                hi = mid
        Q = (lo + hi) / 2.0
    N = p1 * Q**(sigma + 1) - (sigma + 1)/2 * p1 * p_b * p11 * Q**(2*sigma)
    P = 1.0 - Q**(sigma + 1)
    denom = 1.0 - sigma * p_b * p11 * Q**(sigma - 1)
    if abs(denom) < 1e-15:
        S = float('inf')
    else:
        S = (1.0 + p_b * p11 * Q**(sigma - 1)) / denom
    return p1, p11, p_b, Q, N, P, S


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
    test_thetas = [0.0, 0.2, 0.4, 0.58, round(theta_c_val, 12), 0.59, 0.7, 1.0]
    reference = {}
    for t in test_thetas:
        _, _, _, _, _, P, _ = percolation_full(t)
        reference[t] = {'P': P}
    return {'test_thetas': test_thetas, 'reference': reference}


# === block: score_0 (check id='shape_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if rows is None or not isinstance(rows, list) or len(rows) == 0:
        return 0.0
    required = {'theta', 'p1', 'p11', 'p_b', 'Q', 'N', 'P', 'S', 'threshold_flag'}
    if not required.issubset(rows[0].keys()):
        return 0.0
    if len(rows) < 20:
        return 0.0
    return 1.0


# === block: score_1 (check id='internal_consistency') ===
def score_1(artifact, step, ctx):
    rows = artifact
    tol = 1e-10
    passed = 0
    total = 0
    for row in rows:
        try:
            p1 = float(row['p1'])
            p11 = float(row['p11'])
            p_b = float(row['p_b'])
            Q = float(row['Q'])
            N_rep = float(row['N'])
            P_rep = float(row['P'])
            S_rep = float(row['S'])
        except (KeyError, ValueError):
            continue
        total += 1
        N_calc = p1 * Q**(sigma + 1) - (sigma + 1)/2 * p1 * p_b * p11 * Q**(2*sigma)
        P_calc = 1.0 - Q**(sigma + 1)
        denom = 1.0 - sigma * p_b * p11 * Q**(sigma - 1)
        if abs(denom) < 1e-15:
            S_calc = float('inf')
        else:
            S_calc = (1.0 + p_b * p11 * Q**(sigma - 1)) / denom
        if abs(N_rep - N_calc) <= tol and abs(P_rep - P_calc) <= tol and abs(S_rep - S_calc) <= tol:
            passed += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_2 (check id='percolation_structure') ===
def score_2(artifact, step, ctx):
    rows = artifact
    has_sub = False
    has_super = False
    all_sub_Q_one = True
    no_inf_S = True
    for row in rows:
        try:
            flag = row['threshold_flag'].strip().lower()
            P = float(row['P'])
            Q = float(row['Q'])
            S_str = row['S'].strip().lower()
            if S_str in ('inf', '-inf', 'nan', ''):
                S_val = float('inf')
            else:
                S_val = float(row['S'])
        except (KeyError, ValueError):
            continue
        if 'sub' in flag:
            if not has_sub and P < 1e-12:
                has_sub = True
            if abs(Q - 1.0) > 1e-10:
                all_sub_Q_one = False
        if 'super' in flag:
            if not has_super and P > 0.01:
                has_super = True
        if S_val == float('inf') or S_val != S_val:
            no_inf_S = False
    score = 0.0
    if has_sub:
        score += 0.25
    if has_super:
        score += 0.25
    if all_sub_Q_one:
        score += 0.25
    if no_inf_S:
        score += 0.25
    return score


# === block: score_3 (check id='reference_P') ===
def score_3(artifact, step, ctx):
    rows = artifact
    test_thetas = ctx['test_thetas']
    reference = ctx['reference']
    tol = 1e-8
    points = 0
    for t in test_thetas:
        best = None
        for row in rows:
            try:
                theta = float(row['theta'])
            except (KeyError, ValueError):
                continue
            if abs(theta - t) < 1e-6:
                best = row
                break
        if best is None:
            continue
        try:
            P_agent = float(best['P'])
        except (KeyError, ValueError):
            continue
        if abs(P_agent - reference[t]['P']) <= tol:
            points += 1
    return points / len(test_thetas)


_SCORERS = {
    'shape_check': score_0,
    'internal_consistency': score_1,
    'percolation_structure': score_2,
    'reference_P': score_3,
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
