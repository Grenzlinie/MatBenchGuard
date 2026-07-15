import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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


# === block: score_0 (check id='step_01_geometry') ===
def score_0(artifact, step, ctx):
    def safe_float(v):
        try:
            return float(v)
        except (ValueError, TypeError):
            return None
    items = step['gold']['items']
    scores = []
    for row in artifact:
        label = row.get('label', '').strip()
        if label in items:
            expected = items[label]['expected_value']
            tol = items[label]['tolerance']
            val = safe_float(row.get('value'))
            if val is None:
                scores.append(0.0)
            else:
                scores.append(1.0 if abs(val - expected) <= tol else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02_formation_energy') ===
def score_1(artifact, step, ctx):
    def safe_float(v):
        try:
            return float(v)
        except (ValueError, TypeError):
            return None
    items = step['gold']['items']
    scores = []
    for row in artifact:
        rxn = row.get('reaction', '').strip()
        if rxn in items:
            expected = items[rxn]['expected_value']
            tol = items[rxn]['tolerance']
            val = safe_float(row.get('delta_E_eV'))
            if val is None:
                scores.append(0.0)
            else:
                scores.append(1.0 if abs(val - expected) <= tol else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_03_excited_states') ===
def score_2(artifact, step, ctx):
    def safe_float(v):
        if v is None:
            return None
        v = str(v).strip()
        if v == '' or v.lower() == '–' or v.lower() == '-':
            return None
        try:
            return float(v)
        except (ValueError, TypeError):
            return None
    gold_states = step['gold']['states']
    tols = step['gold']['tolerances']
    state_scores = []
    for gs in gold_states:
        state_name = gs['state']
        agent_row = None
        for row in artifact:
            if row.get('state', '').strip() == state_name:
                agent_row = row
                break
        if agent_row is None:
            state_scores.append(0.0)
            continue
        local_scores = []
        # delta_E
        de_gold = gs['delta_E']
        de_val = safe_float(agent_row.get('delta_E_eV'))
        if de_val is None:
            local_scores.append(0.0)
        else:
            local_scores.append(1.0 if abs(de_val - de_gold) <= tols['delta_E'] else 0.0)
        # oscillator strengths
        if gs['forbidden']:
            # must be absent or non-numeric
            f_l_val = safe_float(agent_row.get('f_L'))
            f_v_val = safe_float(agent_row.get('f_v'))
            local_scores.append(1.0 if f_l_val is None else 0.0)
            local_scores.append(1.0 if f_v_val is None else 0.0)
        else:
            f_l_val = safe_float(agent_row.get('f_L'))
            f_v_val = safe_float(agent_row.get('f_v'))
            f_l_gold = gs['f_L']
            f_v_gold = gs['f_v']
            local_scores.append(1.0 if (f_l_val is not None and abs(f_l_val - f_l_gold) <= tols['f_L']) else 0.0)
            local_scores.append(1.0 if (f_v_val is not None and abs(f_v_val - f_v_gold) <= tols['f_v']) else 0.0)
        state_scores.append(sum(local_scores) / len(local_scores))
    if not state_scores:
        return 0.0
    return sum(state_scores) / len(state_scores)


_SCORERS = {
    'step_01_geometry': score_0,
    'step_02_formation_energy': score_1,
    'step_03_excited_states': score_2,
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
