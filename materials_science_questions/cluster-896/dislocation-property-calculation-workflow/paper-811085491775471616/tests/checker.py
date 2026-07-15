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
        gold = {}
        for step in spec.get('steps', []):
            if 'gold' in step:
                gold = step['gold']
        return gold


# === block: score_0 (check id='analyze_results') ===
def score_0(artifact, step, ctx):
        gold = ctx
        if not isinstance(artifact, dict):
            return 0.0
        scores = {}
        # junction_formed (weight 0.1)
        if 'junction_formed' in artifact and isinstance(artifact['junction_formed'], bool):
            scores['junction_formed'] = 1.0 if artifact['junction_formed'] == gold.get('junction_formed', True) else 0.0
        else:
            scores['junction_formed'] = 0.0

        # junction_length_r0 (weight 0.2)
        try:
            length = float(artifact.get('junction_length_r0', 0))
            ref = float(gold.get('junction_length_r0', 10.0))
            lower, upper = ref - 2.0, ref + 2.0   # 8–12 full credit
            if lower <= length <= upper:
                scores['junction_length'] = 1.0
            elif length < lower:
                scores['junction_length'] = max(0.0, 1.0 - (lower - length) / 4.0)
            else:
                scores['junction_length'] = max(0.0, 1.0 - (length - upper) / 4.0)
        except Exception:
            scores['junction_length'] = 0.0

        # jog_direction (weight 0.15)
        jog = str(artifact.get('jog_direction', '')).strip().replace('[', '').replace(']', '').replace(' ', '')
        gold_jog = str(gold.get('jog_direction', '[0-1-1]')).strip().replace('[', '').replace(']', '').replace(' ', '')
        scores['jog_direction'] = 1.0 if jog == gold_jog else 0.0

        # critical_breaking_angle_degrees (weight 0.25)
        try:
            angle = float(artifact.get('critical_breaking_angle_degrees', 0))
            ref_angle = float(gold.get('critical_breaking_angle_degrees', 70.0))
            lower_a, upper_a = ref_angle - 5.0, ref_angle + 5.0   # 65–75 full credit
            if lower_a <= angle <= upper_a:
                scores['critical_angle'] = 1.0
            elif angle < lower_a:
                scores['critical_angle'] = max(0.0, 1.0 - (lower_a - angle) / 5.0)
            else:
                scores['critical_angle'] = max(0.0, 1.0 - (angle - upper_a) / 5.0)
        except Exception:
            scores['critical_angle'] = 0.0

        # b2_analysis (weight 0.3) — exact string match for fractions
        b2_gold = gold.get('partial_reaction_b2_analysis', {})
        b2_agent = artifact.get('partial_reaction_b2_analysis', {})
        b2_score = 0.0
        if isinstance(b2_agent, dict):
            sub_scores = []
            for key in ['alphaB_deltaA', 'alphaB_Bdelta']:
                gold_rxn = b2_gold.get(key, {})
                agent_rxn = b2_agent.get(key, {})
                if not isinstance(agent_rxn, dict):
                    sub_scores.append(0.0)
                    continue
                # check reactants list (exact order ignored, but set comparison)
                ok_react = set(gold_rxn.get('reactants', [])) == set(agent_rxn.get('reactants', []))
                # check product string
                ok_prod = str(gold_rxn.get('product', '')) == str(agent_rxn.get('product', ''))
                # check sums
                ok_sum1 = str(gold_rxn.get('reactant_b2_sum', '')).replace(' ', '') == str(agent_rxn.get('reactant_b2_sum', '')).replace(' ', '')
                ok_sum2 = str(gold_rxn.get('product_b2', '')).replace(' ', '') == str(agent_rxn.get('product_b2', '')).replace(' ', '')
                sub = (ok_react + ok_prod + ok_sum1 + ok_sum2) / 4.0
                sub_scores.append(sub)
            b2_score = sum(sub_scores) / len(sub_scores) if sub_scores else 0.0
        scores['b2'] = b2_score

        weights = {'junction_formed': 0.1, 'junction_length': 0.2, 'jog_direction': 0.15,
                   'critical_angle': 0.25, 'b2': 0.3}
        total = sum(weights[k] * scores.get(k, 0.0) for k in weights)
        return min(1.0, max(0.0, total))


_SCORERS = {
    'analyze_results': score_0,
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
