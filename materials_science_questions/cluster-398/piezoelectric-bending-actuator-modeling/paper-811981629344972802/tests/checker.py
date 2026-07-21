import os
import json
import csv

# === author imports / helpers ===
import re

def normalize_material(m):
    m = m.strip().lower()
    m = m.replace('α', 'alpha').replace('β', 'beta')
    if 'adp' in m:
        return 'adp'
    if 'kdp' in m:
        return 'kdp'
    if 'quartz' in m or 'sio2' in m:
        return 'alpha-quartz'
    return m

def normalize_disloc(s):
    s = s.strip().lower()
    s = s.replace(' ', '')
    s = s.replace('√', 'sqrt').replace('−', '-')
    s = s.replace('*', '*')
    return s

def check_tol(val, gold, rel, abs_min):
    if gold == 0:
        return abs(val - gold) <= abs_min
    else:
        allowed = max(rel * abs(gold), abs_min)
        return abs(val - gold) <= allowed


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
    steps = spec.get('steps', [])
    ctx = {}
    for step in steps:
        if step.get('id') == 'step_02_table2_reproduction':
            hg = step.get('hidden_gold', {})
            ctx['gold_rows'] = hg.get('expected_rows', [])
            tol = hg.get('tolerances', {})
            delta_tol = tol.get('delta_n_max', {})
            r_tol = tol.get('r_max', {})
            ctx['tol_delta_rel'] = delta_tol.get('relative', 0.20)
            ctx['tol_delta_abs_min'] = delta_tol.get('absolute_min', 1e-6)
            ctx['tol_r_rel'] = r_tol.get('relative', 0.20)
            ctx['tol_r_abs_min'] = r_tol.get('absolute_min', 1e-3)
            break
    return ctx


# === block: score_0 (check id='step_02_table2_reproduction') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list):
        return 0.0

    # build agent lookup
    agent_lookup = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        mat_norm = normalize_material(row.get('material', ''))
        xi_norm = normalize_disloc(row.get('dislocation_type_xi', ''))
        b_norm = normalize_disloc(row.get('dislocation_type_b', ''))
        key = (mat_norm, xi_norm, b_norm)
        agent_lookup[key] = row

    gold_rows = ctx.get('gold_rows', [])
    if not gold_rows:
        return 0.0

    matched = 0
    for exp in gold_rows:
        mat_norm = normalize_material(exp['material'])
        xi_norm = normalize_disloc(exp['dislocation_type_xi'])
        b_norm = normalize_disloc(exp['dislocation_type_b'])
        key = (mat_norm, xi_norm, b_norm)
        if key not in agent_lookup:
            continue
        agent_row = agent_lookup[key]
        delta_agent = agent_row.get('delta_n_max', None)
        r_agent = agent_row.get('r_max', None)
        if delta_agent is None or r_agent is None:
            continue
        if check_tol(delta_agent, exp['delta_n_max'], ctx['tol_delta_rel'], ctx['tol_delta_abs_min']) and check_tol(r_agent, exp['r_max'], ctx['tol_r_rel'], ctx['tol_r_abs_min']):
            matched += 1

    return matched / len(gold_rows)


_SCORERS = {
    'step_02_table2_reproduction': score_0,
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
