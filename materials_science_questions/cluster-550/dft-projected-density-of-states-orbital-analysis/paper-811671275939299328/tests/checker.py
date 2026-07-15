import os
import json
import csv

# === author imports / helpers ===
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
    ref_rows = None
    for s in spec.get('steps', []):
        if s.get('output_file') == 'table_ii_results.csv':
            ref_rows = s.get('reference_rows', [])
            break
    return {'reference_rows': ref_rows}


# === block: score_0 (check id='table_ii_result') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    agent_rows = artifact
    if not agent_rows:
        return 0.0

    ref_rows = ctx.get('reference_rows', [])
    if not ref_rows:
        return 0.0

    tol_gap = step.get('tolerance_gap', 0.1)
    tol_te = step.get('tolerance_transition_energy', 0.1)
    tol_osc_rel = step.get('tolerance_oscillator_strength_relative', 0.2)
    tol_osc_abs = step.get('tolerance_oscillator_strength_absolute', 0.02)

    def safe_float(s):
        try:
            return float(s) if s else None
        except:
            return None

    def match_ref(row_ref):
        for arow in agent_rows:
            if (arow.get('Silicide', '').strip() == row_ref['Silicide'].strip() and
                (arow.get('kpoint', '') or '').strip() == (row_ref['kpoint'] or '').strip()):
                return arow
        return None

    def field_ok(ref_val, agent_val, field_name):
        if ref_val == '':
            return (agent_val or '').strip() == ''
        agent_str = (agent_val or '').strip()
        if field_name in ('Gap', 'Transition_energy', 'Oscillator_strength'):
            ref_num = safe_float(ref_val)
            agent_num = safe_float(agent_str)
            if ref_num is None or agent_num is None:
                return False
            if field_name in ('Gap', 'Transition_energy'):
                return abs(agent_num - ref_num) <= (tol_gap if field_name == 'Gap' else tol_te)
            else:
                ref_abs = abs(ref_num)
                allowed = max(tol_osc_rel * ref_abs, tol_osc_abs)
                return abs(agent_num - ref_num) <= allowed
        else:
            return agent_str == ref_val.strip()

    matched = 0
    for rr in ref_rows:
        arow = match_ref(rr)
        if arow is None:
            continue
        ok = True
        for field in ['Gap', 'Type', 'VBM', 'CBM', 'kpoint', 'Transition_energy', 'Oscillator_strength']:
            ref_val = rr.get(field, '')
            agent_val = arow.get(field, '')
            if not field_ok(ref_val, agent_val, field):
                ok = False
                break
        if ok:
            matched += 1
    return matched / len(ref_rows)


_SCORERS = {
    'table_ii_result': score_0,
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
