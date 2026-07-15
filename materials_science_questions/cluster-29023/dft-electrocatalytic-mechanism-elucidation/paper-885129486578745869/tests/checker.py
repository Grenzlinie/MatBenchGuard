import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os
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
    gibbs_path = os.path.join(outputs_dir, 'gibbs_energies.csv')
    gibbs_dict = {}
    if os.path.exists(gibbs_path):
        with open(gibbs_path, newline='') as f:
            for row in csv.DictReader(f):
                gibbs_dict[row['species']] = float(row['G_0V'])
    return {'gibbs_dict': gibbs_dict}


# === block: score_0 (check id='gibbs_energies') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold_species', {})
    tol = step.get('tolerance', 0.2)
    if not gold:
        return 0.0
    gold.pop('H2O(g)', None)
    present = {}
    for row in artifact:
        present[row['species']] = float(row['G_0V'])
    score_sum = 0.0
    for sp, val in gold.items():
        if sp in present:
            diff = abs(present[sp] - val)
            if diff <= tol:
                score_sum += 1.0
    n = len(gold)
    return score_sum / n if n > 0 else 0.0


# === block: score_1 (check id='reaction_free_energies') ===
def score_1(artifact, step, ctx):
    reactions = step.get('reactions', [])
    if not reactions:
        return 0.0
    gibbs = ctx.get('gibbs_dict', {})
    if not gibbs:
        return 0.0
    agent = {}
    for row in artifact:
        agent[row['step']] = float(row['delta_G'])
    n = len(reactions)
    correct = 0.0
    for rxn in reactions:
        lbl = rxn['step']
        prods = rxn.get('products', [])
        reacts = rxn.get('reactants', [])
        delta = sum(gibbs.get(sp, 0.0) for sp in prods) - sum(gibbs.get(sp, 0.0) for sp in reacts)
        if lbl in agent:
            diff = abs(delta - agent[lbl])
            if diff <= 0.2:
                correct += 1.0
    return correct / n if n else 0.0


# === block: score_2 (check id='summary') ===
def score_2(artifact, step, ctx):
    gibbs = ctx.get('gibbs_dict', {})
    if not gibbs:
        return 0.0
    transitions = step.get('transitions', [])
    graph = {}
    for t in transitions:
        src = t['reactant']
        tgt = t.get('product', '')
        lbl = t['step']
        delta = gibbs.get(tgt, 0.0) - gibbs.get(src, 0.0)
        graph.setdefault(src, []).append((tgt, lbl, delta))
    start = 'CO2(g)'
    path = [start]
    current = start
    while current:
        candidates = graph.get(current, [])
        if not candidates:
            break
        best = min(candidates, key=lambda x: x[2])
        next_sp = best[0]
        path.append(next_sp)
        current = next_sp
    steps_in_path = []
    for i in range(len(path)-1):
        src = path[i]
        tgt = path[i+1]
        delta = gibbs.get(tgt, 0.0) - gibbs.get(src, 0.0)
        lbl = None
        for t in transitions:
            if t['reactant'] == src and t.get('product','') == tgt:
                lbl = t['step']
                break
        steps_in_path.append((lbl, delta))
    if steps_in_path:
        limiting_step_label, limiting_delta = max(steps_in_path, key=lambda x: x[1])
        limiting_potential = -limiting_delta
    else:
        limiting_step_label = ''
        limiting_potential = 0.0
    main_product = path[-1] if path else ''
    delta_co_des = gibbs.get('CO(g)', 0.0) - gibbs.get('CO*', 0.0)
    beyond = delta_co_des > 0
    gold_pathway = step.get('gold_pathway', [])
    gold_lp = step.get('gold_limiting_potential', -0.69)
    gold_mp = step.get('gold_main_product', 'CH4')
    gold_bey = step.get('gold_beyond', True)
    lp_tol = step.get('limiting_potential_tolerance', 0.15)
    # derive expected limiting-step label from gold_rate_step string and transitions
    gold_step_label = None
    gold_rds = step.get('gold_rate_step', '')
    if gold_rds and '->' in gold_rds:
        parts = gold_rds.split('->')
        left = parts[0].strip()
        right = parts[1].strip()
        reactant = left.split('+')[0].strip()
        product = right.strip()
        for t in transitions:
            if t.get('reactant','') == reactant and t.get('product','') == product:
                gold_step_label = t['step']
                break
    scores = []
    path_match = (path == gold_pathway)
    scores.append(1.0 if path_match else 0.0)
    lp_diff = abs(limiting_potential - gold_lp)
    scores.append(1.0 if lp_diff <= lp_tol else 0.0)
    rds_match = (limiting_step_label == gold_step_label)
    scores.append(1.0 if rds_match else 0.0)
    mp_match = (main_product == gold_mp)
    scores.append(1.0 if mp_match else 0.0)
    bey_match = (beyond == gold_bey)
    scores.append(1.0 if bey_match else 0.0)
    sub_weights = [0.3, 0.3, 0.2, 0.1, 0.1]
    return sum(s * w for s, w in zip(scores, sub_weights))


_SCORERS = {
    'gibbs_energies': score_0,
    'reaction_free_energies': score_1,
    'summary': score_2,
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
