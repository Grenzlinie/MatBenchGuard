import os
import json
import csv

# === author imports / helpers ===
import math, itertools


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
    ctx = {'hidden_constants': spec.get('hidden_constants', {})}
    return ctx


# === block: score_0 (check id='structural_check') ===
def score_0(artifact, step, ctx):
    # structural check: required keys and array lengths
    artifact = artifact or {}
    def get(path, obj):
        for k in path.split('.'):
            if isinstance(obj, dict) and k in obj: obj = obj[k]
            else: return None
        return obj
    keys = [
        ("reaction_enthalpies", ["Li2O(s)->Li+LiO", "Li2O(g)->Li+LiO"]),
        ("heat_of_formation", ["LiO_g", "Li2O_g"]),
        ("atomization_energy", ["LiO", "Li2O"])
    ]
    valid = True
    for top, subkeys in keys:
        if top not in artifact or not isinstance(artifact[top], dict):
            valid = False; break
        for sk in subkeys:
            if sk not in artifact[top]: valid=False; break
    if valid:
        reac = artifact['reaction_enthalpies']
        for rk in ['Li2O(s)->Li+LiO', 'Li2O(g)->Li+LiO']:
            vals = get(f'{rk}.values', reac)
            if not isinstance(vals, list) or len(vals) != 16:
                valid = False; break
    return 1.0 if valid else 0.0


# === block: score_1 (check id='reaction_enthalpy_solid') ===
def score_1(artifact, step, ctx):
    # recompute average/std from agent's values array; score per-value and average/std agreement
    config = step.get('recompute_config', {})
    rkey = config['reaction_key']
    sub = artifact.get('reaction_enthalpies', {}).get(rkey, {})
    agent_vals = sub.get('values', [])
    agent_avg = sub.get('average_DeltaH0')
    agent_std = sub.get('standard_deviation')
    if not agent_vals or len(agent_vals) != 16:
        return 0.0
    gold_vals = config.get('gold_values', [])
    gold_avg = config.get('gold_average')
    gold_std = config.get('gold_std')
    ptol = config.get('per_value_tolerance', 5.0)
    atol = config.get('average_tolerance', 2.0)
    stol = config.get('std_tolerance', 1.0)
    # score per-value agreement
    n_ok = sum(1 for a, g in zip(agent_vals, gold_vals) if abs(a - g) <= ptol)
    per_val_score = n_ok / len(agent_vals)
    # compute average from array
    comp_avg = sum(agent_vals) / len(agent_vals)
    # score how close computed average is to gold
    err_avg = abs(comp_avg - gold_avg)
    avg_score = 1.0 if err_avg <= atol else max(0.0, 1.0 - (err_avg - atol) / (gold_avg*0.1))
    # score std
    comp_std = (sum((v - comp_avg)**2 for v in agent_vals) / (len(agent_vals)-1))**0.5 if len(agent_vals)>1 else 0.0
    err_std = abs(comp_std - gold_std)
    std_score = 1.0 if err_std <= stol else max(0.0, 1.0 - (err_std - stol) / (gold_std + 0.5))
    # combined score weighting each component equally
    return (per_val_score + avg_score + std_score) / 3.0


# === block: score_2 (check id='reaction_enthalpy_gas') ===
def score_2(artifact, step, ctx):
    # identical to solid but with gas config
    config = step.get('recompute_config', {})
    rkey = config['reaction_key']
    sub = artifact.get('reaction_enthalpies', {}).get(rkey, {})
    agent_vals = sub.get('values', [])
    agent_avg = sub.get('average_DeltaH0')
    agent_std = sub.get('standard_deviation')
    if not agent_vals or len(agent_vals) != 16:
        return 0.0
    gold_vals = config.get('gold_values', [])
    gold_avg = config.get('gold_average')
    gold_std = config.get('gold_std')
    ptol = config.get('per_value_tolerance', 5.0)
    atol = config.get('average_tolerance', 2.0)
    stol = config.get('std_tolerance', 1.0)
    n_ok = sum(1 for a, g in zip(agent_vals, gold_vals) if abs(a - g) <= ptol)
    per_val_score = n_ok / len(agent_vals)
    comp_avg = sum(agent_vals) / len(agent_vals)
    err_avg = abs(comp_avg - gold_avg)
    avg_score = 1.0 if err_avg <= atol else max(0.0, 1.0 - (err_avg - atol) / (gold_avg*0.1))
    comp_std = (sum((v - comp_avg)**2 for v in agent_vals) / (len(agent_vals)-1))**0.5 if len(agent_vals)>1 else 0.0
    err_std = abs(comp_std - gold_std)
    std_score = 1.0 if err_std <= stol else max(0.0, 1.0 - (err_std - stol) / (gold_std + 0.5))
    return (per_val_score + avg_score + std_score) / 3.0


# === block: score_3 (check id='heat_of_formation_LiO') ===
def score_3(artifact, step, ctx):
    # derive expected δHf(LiO) from solid reaction average and hidden constants
    const = ctx.get('hidden_constants', {})
    if not const:
        return 0.0
    reac = artifact.get('reaction_enthalpies', {})
    solid = reac.get('Li2O(s)->Li+LiO', {})
    agent_avg = solid.get('average_DeltaH0')
    if agent_avg is None:
        return 0.0
    # δHf(LiO) = δH0(7) + δHf(Li2O,s) - δHf(Li,g)  (using δH0(7) from solid reaction)
    expected = agent_avg + const.get('ΔHf(Li2O,s)', -141.6) - const.get('ΔHf(Li,g)', 38.5)
    agent_val = artifact.get('heat_of_formation', {}).get('LiO_g', {}).get('DeltaH0_0')
    if agent_val is None:
        return 0.0
    err = abs(agent_val - expected)
    tol = step.get('tolerance', 2.0)
    if err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (err - tol) / (abs(expected)+1e-5))


# === block: score_4 (check id='heat_of_formation_Li2O') ===
def score_4(artifact, step, ctx):
    # derive expected δHf(Li2O,g) from sublimation enthalpy and solid formation
    const = ctx.get('hidden_constants', {})
    if not const:
        return 0.0
    dHf_solid = const.get('ΔHf(Li2O,s)', -141.6)
    sub_enthalpy = const.get('ΔH_sublim(Li2O)', 99.3)
    expected = dHf_solid + sub_enthalpy
    agent_val = artifact.get('heat_of_formation', {}).get('Li2O_g', {}).get('DeltaH0_0')
    if agent_val is None:
        return 0.0
    err = abs(agent_val - expected)
    tol = step.get('tolerance', 2.0)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - (err - tol) / (abs(expected)+1e-5))


# === block: score_5 (check id='atomization_LiO') ===
def score_5(artifact, step, ctx):
    # D0(LiO) = δHf(Li,g) + δHf(O,g) - δHf(LiO)
    const = ctx.get('hidden_constants', {})
    if not const:
        return 0.0
    dHf_Li = const.get('ΔHf(Li,g)', 38.5)
    dHf_O = const.get('ΔHf(O,g)', 58.989)
    agent_dHf_LiO = artifact.get('heat_of_formation', {}).get('LiO_g', {}).get('DeltaH0_0')
    if agent_dHf_LiO is None:
        return 0.0
    expected = dHf_Li + dHf_O - agent_dHf_LiO
    agent_val = artifact.get('atomization_energy', {}).get('LiO', {}).get('D0_0')
    if agent_val is None:
        return 0.0
    err = abs(agent_val - expected)
    tol = step.get('tolerance', 2.0)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - (err - tol) / (expected+1e-5))


# === block: score_6 (check id='atomization_Li2O') ===
def score_6(artifact, step, ctx):
    # D0(Li2O) = 2*δHf(Li,g) + δHf(O,g) - δHf(Li2O,g)
    const = ctx.get('hidden_constants', {})
    if not const:
        return 0.0
    dHf_Li = const.get('ΔHf(Li,g)', 38.5)
    dHf_O = const.get('ΔHf(O,g)', 58.989)
    agent_dHf_Li2O = artifact.get('heat_of_formation', {}).get('Li2O_g', {}).get('DeltaH0_0')
    if agent_dHf_Li2O is None:
        return 0.0
    expected = 2*dHf_Li + dHf_O - agent_dHf_Li2O
    agent_val = artifact.get('atomization_energy', {}).get('Li2O', {}).get('D0_0')
    if agent_val is None:
        return 0.0
    err = abs(agent_val - expected)
    tol = step.get('tolerance', 2.0)
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - (err - tol) / (expected+1e-5))


_SCORERS = {
    'structural_check': score_0,
    'reaction_enthalpy_solid': score_1,
    'reaction_enthalpy_gas': score_2,
    'heat_of_formation_LiO': score_3,
    'heat_of_formation_Li2O': score_4,
    'atomization_LiO': score_5,
    'atomization_Li2O': score_6,
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
