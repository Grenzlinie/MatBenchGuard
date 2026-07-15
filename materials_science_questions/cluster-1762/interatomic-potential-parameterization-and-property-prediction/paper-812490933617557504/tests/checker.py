import os
import json
import csv

# === author imports / helpers ===
import csv
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
    gold = spec.get('gold_parameters', {})
    return {
        'gold_rows': gold.get('gold_rows', []),
        'trend1_pairs': gold.get('trend1_pairs', []),
        'trend2_compounds': gold.get('trend2_compounds', []),
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold_rows = ctx['gold_rows']
    trend1_pairs = ctx['trend1_pairs']
    trend2_compounds = ctx['trend2_compounds']

    # Build index from agent CSV keyed by (compound, structure_type, lattice)
    agent_dict = {}
    for row in artifact:
        try:
            compound = str(row['compound']).strip()
            stype = str(row['structure_type']).strip()
            lattice = float(row['lattice_param_A'])
            energy = float(row['Madelung_energy_eV'])
        except (KeyError, ValueError):
            continue
        key = (compound, stype, lattice)
        # keep first occurrence; later duplicates ignored
        if key not in agent_dict:
            agent_dict[key] = energy

    # 1. Energy match score
    matched = 0
    for g in gold_rows:
        key = (g['compound'], g['structure_type'], g['lattice_param_A'])
        if key in agent_dict:
            agent_energy = agent_dict[key]
            if abs(agent_energy - g['Madelung_energy_eV']) <= 0.2:
                matched += 1
    energy_score = matched / len(gold_rows) if gold_rows else 0.0

    # 2. Trend1: mixed_ordered energy < simple energy (the two specific pairs)
    t1_correct = 0
    # Build a lookup from gold_rows to get lattice for a compound+structure_type
    gold_lut = {}
    for g in gold_rows:
        gold_lut[(g['compound'], g['structure_type'])] = g['lattice_param_A']
    for mixed_comp, mixed_st, ref_comp, ref_st in trend1_pairs:
        # For the mixed ordered compound, we need the lattice.
        mix_key = (mixed_comp, mixed_st)
        if mix_key not in gold_lut:
            continue
        lattice = gold_lut[mix_key]
        key_mix = (mixed_comp, mixed_st, lattice)
        # For the reference simple ABO3, we need the same lattice.
        key_ref = (ref_comp, ref_st, lattice)
        if key_mix in agent_dict and key_ref in agent_dict:
            if agent_dict[key_mix] < agent_dict[key_ref]:
                t1_correct += 1
    t1_score = t1_correct / len(trend1_pairs) if trend1_pairs else 1.0

    # 3. Trend2: ordered < disordered for each compound that has both
    t2_correct = 0
    for comp in trend2_compounds:
        # find lattice from gold (ordered row)
        ord_key = (comp, 'mixed_ordered')
        if ord_key not in gold_lut:
            continue
        lattice = gold_lut[ord_key]
        key_ord = (comp, 'mixed_ordered', lattice)
        key_dis = (comp, 'mixed_disordered', lattice)
        if key_ord in agent_dict and key_dis in agent_dict:
            if agent_dict[key_ord] < agent_dict[key_dis]:
                t2_correct += 1
    t2_score = t2_correct / len(trend2_compounds) if trend2_compounds else 1.0

    w_e, w_t1, w_t2 = 0.7, 0.15, 0.15
    return w_e * energy_score + w_t1 * t1_score + w_t2 * t2_score


_SCORERS = {
    'step_01': score_0,
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
