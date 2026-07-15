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
    ref_table = {}
    for step in spec['steps']:
        if step['id'] == 'ssp_values':
            for row in step['reference_table']:
                key = (row['glass'], row['screening'])
                ref_table[key] = {k: float(row[k]) for k in ['lambda','mu_star','Tc','alpha','N0V']}
            return {'ref_table': ref_table, 'tol': step['tolerances']}
    return {}


# === block: score_0 (check id='ssp_values') ===
def score_0(artifact, step, ctx):
    artifact_rows = load_artifact(os.path.join('/app/outputs', step['output_file']))
    if not isinstance(artifact_rows, list) or not artifact_rows:
        return 0.0
    ref_table = ctx['ref_table']
    tol = ctx['tol']
    total_checks = 0
    passed_checks = 0
    for row in artifact_rows:
        glass = row.get('glass', '').strip()
        screening = row.get('screening', '').strip()
        key = (glass, screening)
        if key not in ref_table:
            continue
        ref = ref_table[key]
        for col in ['lambda','mu_star','Tc','alpha','N0V']:
            val_str = row.get(col, None)
            if val_str is None or val_str == '':
                continue
            val = float(val_str)
            ref_val = ref[col]
            if abs(ref_val) < 1e-9:
                if abs(val - ref_val) <= 1e-6:
                    passed_checks += 1
            else:
                if abs(val - ref_val) / abs(ref_val) <= tol[col]:
                    passed_checks += 1
            total_checks += 1
    if total_checks == 0:
        return 0.0
    return passed_checks / total_checks


# === block: score_1 (check id='ssp_ordering') ===
def score_1(artifact, step, ctx):
    artifact_rows = load_artifact(os.path.join('/app/outputs', step['output_file']))
    if not isinstance(artifact_rows, list) or not artifact_rows:
        return 0.0

    # build agent's Tc per glass and screening
    glass_tc_agent = {}
    for row in artifact_rows:
        glass = row.get('glass', '').strip()
        screening = row.get('screening', '').strip()
        if screening not in ('H','T','IU','F','S'):
            continue
        try:
            tc = float(row['Tc'])
        except (ValueError, TypeError):
            continue
        glass_tc_agent.setdefault(glass, {})[screening] = tc

    # get gold Tc ordering from the reference table
    ref_table = ctx.get('ref_table', {})
    gold_order = {}  # glass -> list of screenings sorted by gold Tc
    for (glass, screening), ref in ref_table.items():
        ref_tc = ref.get('Tc')
        if ref_tc is None:
            continue
        gold_order.setdefault(glass, {})[screening] = ref_tc
    # convert to sorted order per glass
    expected_order_map = {}
    for glass, d in gold_order.items():
        if set(d.keys()) == {'H','T','IU','F','S'}:
            expected_order_map[glass] = sorted(d.keys(), key=lambda s: d[s])

    correct = 0
    total = 0
    for glass, order_list in expected_order_map.items():
        if glass not in glass_tc_agent:
            continue
        agent_dict = glass_tc_agent[glass]
        if set(agent_dict.keys()) != {'H','T','IU','F','S'}:
            continue
        agent_vals = [agent_dict[s] for s in order_list]
        # check strictly increasing
        if all(agent_vals[i] < agent_vals[i+1] for i in range(len(agent_vals)-1)):
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'ssp_values': score_0,
    'ssp_ordering': score_1,
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
