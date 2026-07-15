import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    import os
    def prepare(outputs_dir, spec):
        return {'output_dir': outputs_dir}


# === block: score_0 (check id='mc_A') ===
def score_0(artifact, step, ctx):
    artifact = artifact
    step = step
    ctx = ctx
    if artifact is None:
        return 0.0
    required = ['F_c', 'p_flaws', 'trials', 'failures']
    if not all(k in artifact for k in required):
        return 0.0
    trials = artifact['trials']
    failures = artifact['failures']
    Fc = artifact['F_c']
    p_flaws = artifact['p_flaws']
    shape_ok = 1.0 if (int(trials) == 1000000 and int(failures) >= 0 and int(failures) <= int(trials)) else 0.0
    gold = step['gold']
    gold_Fc = gold['F_c']
    gold_p = gold['p_flaws']
    rel_tol = gold['rel_tol_Fc']
    abs_tol = gold['abs_tol_p_flaws']
    # Closeness scoring for F_c (symmetric)
    Fc_err = abs(Fc - gold_Fc)
    max_Fc_err = gold_Fc * rel_tol
    if Fc_err <= max_Fc_err:
        score_Fc = 1.0
    else:
        score_Fc = max(0.0, 1.0 - (Fc_err - max_Fc_err) / (gold_Fc * rel_tol * 2.0))
    # Closeness scoring for p_flaws (symmetric)
    p_err = abs(p_flaws - gold_p)
    if p_err <= abs_tol:
        score_p = 1.0
    else:
        score_p = max(0.0, 1.0 - (p_err - abs_tol) / (abs_tol * 2.0))
    return 0.1 * shape_ok + 0.45 * score_Fc + 0.45 * score_p


# === block: score_1 (check id='mc_B') ===
def score_1(artifact, step, ctx):
    artifact = artifact
    step = step
    ctx = ctx
    if artifact is None:
        return 0.0
    required = ['F_c', 'p_flaws', 'trials', 'failures']
    if not all(k in artifact for k in required):
        return 0.0
    trials = artifact['trials']
    failures = artifact['failures']
    Fc = artifact['F_c']
    p_flaws = artifact['p_flaws']
    shape_ok = 1.0 if (int(trials) == 1000000 and int(failures) >= 0 and int(failures) <= int(trials)) else 0.0
    gold = step['gold']
    gold_Fc = gold['F_c']
    gold_p = gold['p_flaws']
    rel_tol = gold['rel_tol_Fc']
    abs_tol = gold['abs_tol_p_flaws']
    Fc_limit = gold_Fc * (1.0 + rel_tol)
    if Fc <= Fc_limit:
        score_Fc = 1.0
    else:
        excess = Fc - Fc_limit
        max_excess = gold_Fc * rel_tol * 2
        score_Fc = max(0.0, 1.0 - excess / max_excess)
    p_limit = gold_p + abs_tol
    if p_flaws <= p_limit:
        score_p = 1.0
    else:
        excess_p = p_flaws - p_limit
        max_excess_p = abs_tol * 2
        score_p = max(0.0, 1.0 - excess_p / max_excess_p)
    return 0.1*shape_ok + 0.45*score_Fc + 0.45*score_p


# === block: score_2 (check id='trend') ===
def score_2(artifact, step, ctx):
    output_dir = ctx['output_dir']
    import json, os
    pathA = os.path.join(output_dir, 'design_A_MC_results.json')
    pathB = os.path.join(output_dir, 'design_B_MC_results.json')
    if not os.path.exists(pathA) or not os.path.exists(pathB):
        return 0.0
    with open(pathA) as f: A = json.load(f)
    with open(pathB) as f: B = json.load(f)
    pA = A.get('p_flaws')
    pB = B.get('p_flaws')
    if pA is None or pB is None:
        return 0.0
    if pB < pA:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='consistency') ===
def score_3(artifact, step, ctx):
    output_dir = ctx['output_dir']
    import json, os, math
    pathA = os.path.join(output_dir, 'design_A_MC_results.json')
    pathB = os.path.join(output_dir, 'design_B_MC_results.json')
    if not os.path.exists(pathA) or not os.path.exists(pathB):
        return 0.0
    with open(pathA) as f: A = json.load(f)
    with open(pathB) as f: B = json.load(f)
    gold = step['gold']
    lambda_A = gold['lambda_A']
    V_A = gold['V_A']
    lambda_B = gold['lambda_B']
    V_B = gold['V_B']
    tol_p = gold['tolerance_p']
    tol_fail = gold['tolerance_failures']
    def check(data, lam, V, tol_p, tol_fail):
        Fc = data.get('F_c')
        p_flaws = data.get('p_flaws')
        trials = data.get('trials')
        failures = data.get('failures')
        if None in (Fc, p_flaws, trials, failures):
            return 0.0
        expected_p = 1.0 - math.exp(-lam * V * Fc)
        if abs(p_flaws - expected_p) > tol_p:
            return 0.0
        expected_failures = int(round(Fc * trials))
        if abs(failures - expected_failures) > tol_fail:
            return 0.0
        return 1.0
    score_A = check(A, lambda_A, V_A, tol_p, tol_fail)
    score_B = check(B, lambda_B, V_B, tol_p, tol_fail)
    return (score_A + score_B) / 2.0


_SCORERS = {
    'mc_A': score_0,
    'mc_B': score_1,
    'trend': score_2,
    'consistency': score_3,
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
