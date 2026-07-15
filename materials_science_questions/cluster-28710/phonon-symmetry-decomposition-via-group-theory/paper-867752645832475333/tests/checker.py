import os
import json
import csv


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


# === block: score_0 (check id='step_01_space_groups') ===
def score_0(artifact, step, ctx):
    import re

    def _norm(s):
        s = s.strip()
        s = re.sub(r'\([^)]*\)', '', s)
        return s.strip()

    def _norm_gwv(s):
        s = _norm(s)
        s = re.sub(r'\^[0-9]+', '', s)
        return s.strip()

    gold = step['gold']
    if not isinstance(artifact, list):
        return 0.0

    agent_entries = { (e.get('polytype',''), e.get('layer_case','')): e for e in artifact if isinstance(e, dict) }
    matches = 0
    for g in gold:
        key = (g['polytype'], g['layer_case'])
        ae = agent_entries.get(key)
        if ae is None:
            continue

        fields_ok = (
            _norm(ae.get('space_group_HM','')) == _norm(g['space_group_HM']) and
            _norm(ae.get('space_group_Schoenflies','')) == _norm(g['space_group_Schoenflies']) and
            ae.get('space_group_number') == g['space_group_number'] and
            isinstance(ae.get('GWV'), dict)
        )
        if not fields_ok:
            continue

        gwv_ok = True
        for pt in ['Gamma','K','Kprime','M','Sigma','T','Tprime','u']:
            if _norm_gwv(ae['GWV'].get(pt,'')) != _norm_gwv(g['GWV'].get(pt,'')):
                gwv_ok = False
                break
        if gwv_ok:
            matches += 1

    return matches / len(gold) if gold else 0.0


# === block: score_1 (check id='step_02_irreps') ===
def score_1(artifact, step, ctx):
    def _norm(s):
        import re
        s = s.strip()
        s = s.replace('†','+').replace('$','').replace('\n',' ')
        s = re.sub(r'\s+', '', s)
        return s
    gold = step['gold']
    if not isinstance(artifact, dict):
        return 0.0
    total_points = 0
    correct = 0
    for case, pts in gold.items():
        agent_pts = artifact.get(case)
        if not isinstance(agent_pts, dict):
            continue
        for point, formula in pts.items():
            total_points += 1
            agent_formula = agent_pts.get(point, '')
            if _norm(agent_formula) == _norm(formula):
                correct += 1
    return correct / total_points if total_points > 0 else 0.0


# === block: score_2 (check id='step_03_selection_rules') ===
def score_2(artifact, step, ctx):
    def _norm(s):
        import re
        s = s.strip()
        s = s.replace('†','+').replace('$','').replace('\n',' ')
        s = re.sub(r'\s+', '', s)
        return s
    gold = step['gold']
    if not isinstance(artifact, list):
        return 0.0
    agent_entries = { (e.get('polytype',''), e.get('layer_case','')): e for e in artifact if isinstance(e, dict) }
    matches = 0
    field_names = ['Gamma_vib_irrep','Raman_active_irreps','IR_active_irreps','acoustic_irreps','silent_irreps']
    for g in gold:
        key = (g['polytype'], g['layer_case'])
        ae = agent_entries.get(key)
        if ae is None:
            continue
        ok = True
        for fn in field_names:
            if _norm(str(ae.get(fn,''))) != _norm(str(g.get(fn,''))):
                ok = False
                break
        if ok:
            matches += 1
    return matches / len(gold) if gold else 0.0


# === block: score_3 (check id='step_04_raman_tensors') ===
def score_3(artifact, step, ctx):
    def _norm_matrix(m):
        # Convert all elements to strings and flatten for comparison
        if not isinstance(m, list) or len(m) != 3:
            return None
        norm = []
        for row in m:
            if not isinstance(row, list) or len(row) != 3:
                return None
            norm.append([str(elem).strip() for elem in row])
        return norm
    gold = step['gold']
    if not isinstance(artifact, list):
        return 0.0
    matches = 0
    # Build lookup from agent entries
    agent_map = {}
    for ae in artifact:
        if not isinstance(ae, dict):
            continue
        key = (ae.get('space_group',''), ae.get('point_group',''), ae.get('irrep_label',''))
        agent_map[key] = ae.get('tensor')
    for g in gold:
        key = (g['space_group'], g['point_group'], g['irrep_label'])
        agent_tensor = agent_map.get(key)
        agent_norm = _norm_matrix(agent_tensor)
        gold_norm = _norm_matrix(g['tensor'])
        if agent_norm is not None and gold_norm is not None and agent_norm == gold_norm:
            matches += 1
    return matches / len(gold) if gold else 0.0


_SCORERS = {
    'step_01_space_groups': score_0,
    'step_02_irreps': score_1,
    'step_03_selection_rules': score_2,
    'step_04_raman_tensors': score_3,
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
