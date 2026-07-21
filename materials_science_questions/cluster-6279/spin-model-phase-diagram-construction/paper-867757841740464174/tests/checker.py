import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='first_order_Tc') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    agent_list = artifact.get('first_order_transitions', [])
    matched = 0
    for g in gold:
        j = g['J_over_Jprime']
        tc_gold = g['Tc']
        tol = g['Tc_tol']
        found = next((a for a in agent_list if a.get('J_over_Jprime') == j), None)
        if found is not None and abs(found.get('Tc', 0) - tc_gold) <= tol:
            matched += 1
    return matched / len(gold) if gold else 0.0


# === block: score_1 (check id='DLRO_transitions') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    tnu = step.get('tolerances', {})
    nu_tol = tnu.get('nu_tol', 0.05)
    gamma_tol = tnu.get('gamma_tol', 0.10)
    agent_list = artifact.get('DLRO_transitions', [])
    matched = 0
    for g in gold:
        j = g['J_over_Jprime']
        tc_gold = g['Tc']
        tc_tol = g['Tc_tol']
        nu_gold = g['nu']
        gamma_gold = g['gamma']
        found = None
        for a in agent_list:
            a_j = a.get('J_over_Jprime')
            # accept numeric 0.8 vs string 'inf' but treat 'inf' specially
            if j == 'inf' and a_j == 'inf':
                found = a
                break
            elif isinstance(j, (int,float)) and isinstance(a_j, (int,float)) and abs(a_j - j) < 1e-9:
                found = a
                break
        if found is not None:
            if abs(found.get('Tc', 0) - tc_gold) <= tc_tol and abs(found.get('nu', 0) - nu_gold) <= nu_tol and abs(found.get('gamma', 0) - gamma_gold) <= gamma_tol:
                matched += 1
    return matched / len(gold) if gold else 0.0


# === block: score_2 (check id='QLRO_transitions') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tnu = step.get('tolerances', {})
    nu_tol = tnu.get('nu_tol', 0.05)
    gamma_tol = tnu.get('gamma_tol', 0.10)
    agent_list = artifact.get('QLRO_transitions', [])
    matched = 0
    for g in gold:
        j = g['J_over_Jprime']
        tc_gold = g['Tc']
        tc_tol = g['Tc_tol']
        nu_gold = g['nu']
        gamma_gold = g['gamma']
        found = next((a for a in agent_list if a.get('J_over_Jprime') == j), None)
        if found is not None:
            if abs(found.get('Tc', 0) - tc_gold) <= tc_tol and abs(found.get('nu', 0) - nu_gold) <= nu_tol and abs(found.get('gamma', 0) - gamma_gold) <= gamma_tol:
                matched += 1
    return matched / len(gold) if gold else 0.0


_SCORERS = {
    'first_order_Tc': score_0,
    'DLRO_transitions': score_1,
    'QLRO_transitions': score_2,
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
