import os
import json
import csv

# === author imports / helpers ===
import json, re, collections


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


# === block: score_0 (check id='step_02_free_energy') ===
def score_0(artifact, step, ctx):
    def normalize(s):
        return re.sub(r'\s+', ' ', str(s).strip())

    target = step.get('target', {})
    if not isinstance(artifact, dict):
        return 0.0
    materials = ['TaX2', 'TiSe2']
    passed = 0
    for mat in materials:
        if mat not in artifact or mat not in target:
            continue
        art_mat = artifact[mat]
        tgt_mat = target[mat]
        # check order_parameter_dim
        if art_mat.get('order_parameter_dim') != tgt_mat.get('order_parameter_dim'):
            continue
        # compare transformation_rules (dict of normalized strings)
        art_rules = {k: normalize(v) for k, v in art_mat.get('transformation_rules', {}).items()}
        tgt_rules = {k: normalize(v) for k, v in tgt_mat.get('transformation_rules', {}).items()}
        if art_rules != tgt_rules:
            continue
        # compare polynomial_terms as sorted normalized lists
        art_terms = sorted([normalize(t) for t in art_mat.get('polynomial_terms', [])])
        tgt_terms = sorted([normalize(t) for t in tgt_mat.get('polynomial_terms', [])])
        if art_terms != tgt_terms:
            continue
        # compare invariant_constraints as sorted normalized lists
        art_constr = sorted([normalize(c) for c in art_mat.get('invariant_constraints', [])])
        tgt_constr = sorted([normalize(c) for c in tgt_mat.get('invariant_constraints', [])])
        if art_constr != tgt_constr:
            continue
        passed += 1
    return 1.0 if passed == len(materials) else (passed / len(materials) * 0.5)


# === block: score_1 (check id='step_03_mean_field') ===
def score_1(artifact, step, ctx):
    def normalize(s):
        return re.sub(r'\s+', ' ', str(s).strip())

    target = step.get('target', {})
    if not isinstance(artifact, dict):
        return 0.0
    materials = ['TaX2', 'TiSe2']
    passed = 0
    for mat in materials:
        if mat not in artifact or mat not in target:
            continue
        art_mat = artifact[mat]
        tgt_mat = target[mat]
        # compare condition strings
        if (normalize(art_mat.get('single_Q_condition','')) != normalize(tgt_mat.get('single_Q_condition','')) or
            normalize(art_mat.get('triple_Q_condition','')) != normalize(tgt_mat.get('triple_Q_condition',''))):
            continue
        # compare order_parameter_components as sets of normalized dict items
        art_comps = art_mat.get('order_parameter_components', [])
        tgt_comps = tgt_mat.get('order_parameter_components', [])
        if not isinstance(art_comps, list) or not isinstance(tgt_comps, list):
            continue
        def comp_to_tuple(comp):
            return tuple(sorted((k, normalize(v)) for k, v in comp.items()))
        art_set = set(comp_to_tuple(c) for c in art_comps)
        tgt_set = set(comp_to_tuple(c) for c in tgt_comps)
        if art_set != tgt_set:
            continue
        passed += 1
    return 1.0 if passed == len(materials) else (passed / len(materials) * 0.5)


# === block: score_2 (check id='step_04_rg') ===
def score_2(artifact, step, ctx):
    constraints = step.get('constraints', {})
    if not isinstance(artifact, dict):
        return 0.0
    tise2_score = 0.0
    tax2_score = 0.0
    # TiSe2 check
    if 'TiSe2' in artifact:
        ts = artifact['TiSe2']
        c = constraints.get('TiSe2', {})
        req_keys = c.get('required_keys', [])
        if all(k in ts for k in req_keys):
            fps = ts.get('fixed_points', [])
            if isinstance(fps, list) and len(fps) >= c.get('fixed_points_min_count', 0):
                # check for stable Heisenberg fixed point
                heis_stable = False
                for fp in fps:
                    if isinstance(fp, dict) and 'name' in fp and 'stability' in fp:
                        if str(fp['name']).lower() == 'heisenberg' and str(fp['stability']).lower() in ('stable', 'true'):
                            heis_stable = True
                            break
                if c.get('heisenberg_present_stable', False):
                    if heis_stable and ts.get('heisenberg_is_stable', False) == True:
                        tise2_score = 1.0
                    else:
                        tise2_score = 0.5  # partial: structure okay but flag mismatch
                else:
                    tise2_score = 1.0  # no strict requirement
            else:
                tise2_score = 0.3
        else:
            tise2_score = 0.1
    else:
        tise2_score = 0.0

    # TaX2 check (modest)
    if 'TaX2' in artifact:
        ta = artifact['TaX2']
        c2 = constraints.get('TaX2', {})
        req_keys2 = c2.get('required_keys', [])
        if all(k in ta for k in req_keys2):
            fps2 = ta.get('fixed_points', [])
            if isinstance(fps2, list) and len(fps2) >= c2.get('fixed_points_min_count', 0):
                tax2_score = 0.2
            else:
                tax2_score = 0.1
        else:
            tax2_score = 0.05
    else:
        tax2_score = 0.0

    # combined weight: TiSe2 0.8, TaX2 0.2
    return tise2_score * 0.8 + tax2_score


_SCORERS = {
    'step_02_free_energy': score_0,
    'step_03_mean_field': score_1,
    'step_04_rg': score_2,
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
