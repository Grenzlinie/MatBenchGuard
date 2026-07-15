import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    gold_es = spec['steps'][0]['gold']
    gold_rxn = spec['steps'][1]['gold']
    ctx = dict(
        es_gold=gold_es['es'],
        es_tol=gold_es['tolerance_abs'],
        cluster_n_acid=gold_es['cluster_n_acid'],
        ordering_es=gold_es['ordering_rules'],
        delta_gold=gold_rxn['delta_E'],
        rxn_tol=gold_rxn['tolerance_abs'],
        reaction_specs=gold_rxn['reaction_specs'],
        ordering_rxn=gold_rxn['ordering_rules']
    )
    return ctx


# === block: score_0 (check id='specific_energies') ===
def score_0(artifact, step, ctx):
    def load_total(ods):
        p = os.path.join(ods, 'total_energies.csv')
        if not os.path.exists(p): return None
        rows = csv.DictReader(open(p))
        return {row['id']: float(row['total_energy']) for row in rows}

    def load_es(ods):
        p = os.path.join(ods, 'specific_energies.csv')
        if not os.path.exists(p): return None
        rows = csv.DictReader(open(p))
        return {row['cluster_id']: float(row['E_s']) for row in rows}

    ods = '/app/outputs'
    tot = load_total(ods)
    if tot is not None:
        es_agent = {}
        for cid, n in ctx['cluster_n_acid'].items():
            tid = str(cid)
            if tid in tot:
                es_agent[cid] = tot[tid] / n
            else:
                es_agent[cid] = None
    else:
        es_agent = load_es(ods)
        if es_agent is not None:
            es_agent = {int(k): v for k,v in es_agent.items()}
        else:
            return 0.0

    # score each cluster against gold
    scores = []
    for cid in ctx['cluster_n_acid']:
        gold = ctx['es_gold'].get(cid)
        if gold is None: continue
        val = es_agent.get(cid)
        if val is None:
            scores.append(0.0)
            continue
        diff = abs(val - gold)
        if diff <= ctx['es_tol']:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (diff - ctx['es_tol']) / (0.3))  # linear decay after tolerance
        scores.append(s)

    val_score = sum(scores) / len(scores) if scores else 0.0

    # ordering checks
    ord_ok = 1.0
    if es_agent:
        def get_e(cid):
            v = es_agent.get(cid)
            return v if v is not None else -1e9
        for rule in ctx['ordering_es']:
            parts = rule.split()
            # expect "Es_3 > Es_4"
            if len(parts) == 3 and parts[1] == '>':
                c1 = int(parts[0].split('_')[1])
                c2 = int(parts[2].split('_')[1])
                if get_e(c1) <= get_e(c2):
                    ord_ok *= 0.8  # penalty per failed ordering
        ord_ok = max(0.0, ord_ok)
    else:
        ord_ok = 0.0

    return 0.8 * val_score + 0.2 * ord_ok


# === block: score_1 (check id='reaction_energies') ===
def score_1(artifact, step, ctx):
    def load_total(ods):
        p = os.path.join(ods, 'total_energies.csv')
        if not os.path.exists(p): return None
        rows = csv.DictReader(open(p))
        return {row['id']: float(row['total_energy']) for row in rows}

    def load_rxn(ods):
        p = os.path.join(ods, 'reaction_energies.csv')
        if not os.path.exists(p): return None
        rows = csv.DictReader(open(p))
        return {row['reaction_id']: float(row['delta_E']) for row in rows}

    ods = '/app/outputs'
    tot = load_total(ods)
    if tot is not None:
        def compute_delta(rxn_spec):
            reactants = rxn_spec['reactants']
            products = rxn_spec['products']
            e_total = 0.0
            for r in reactants:
                tid = r['id']
                if tid not in tot: return None
                e_total += tot[tid] * r['coeff']
            for p in products:
                tid = p['id']
                if tid not in tot: return None
                e_total -= tot[p['id']] * p['coeff']
            return -e_total  # delta_E = prod - reac
        delta_agent = {}
        for rid, spec in ctx['reaction_specs'].items():
            val = compute_delta(spec)
            if val is not None:
                delta_agent[rid] = val
    else:
        delta_agent = load_rxn(ods)
        if delta_agent is not None:
            pass
        else:
            return 0.0

    # score each reaction
    scores = []
    for rid, gold in ctx['delta_gold'].items():
        val = delta_agent.get(rid)
        if val is None:
            scores.append(0.0)
            continue
        diff = abs(val - gold)
        if diff <= ctx['rxn_tol']:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (diff - ctx['rxn_tol']) / (0.15))
        scores.append(s)
    val_score = sum(scores) / len(scores) if scores else 0.0

    # ordering
    ord_ok = 1.0
    if delta_agent:
        def get_abs(rid):
            v = delta_agent.get(rid)
            return abs(v) if v is not None else 0.0
        for rule in ctx['ordering_rxn']:
            parts = rule.split()
            if len(parts) == 3 and parts[1] == '>':
                r1 = parts[0].split('_')[1]
                r2 = parts[2].split('_')[1]
                if get_abs(r1) <= get_abs(r2):
                    ord_ok *= 0.8
        ord_ok = max(0.0, ord_ok)
    else:
        ord_ok = 0.0

    return 0.8 * val_score + 0.2 * ord_ok


_SCORERS = {
    'specific_energies': score_0,
    'reaction_energies': score_1,
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
