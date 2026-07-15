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


# === block: score_0 (check id='barrier_step1_NiCuOOH') ===
def score_0(artifact, step, ctx):
    system = step['params']['system']
    step_number = step['params']['step_number']
    target = step['params']['target']
    tol = step['params']['tolerance']
    artifact = [row for row in artifact if row['system'] == system and int(row['step_number']) == step_number]
    if not artifact:
        return 0.0
    agent_val = float(artifact[0]['barrier_ev'])
    diff = abs(agent_val - target)
    if diff <= tol:
        return 1.0
    else:
        # linear decay beyond tolerance, reach 0 at 2*tol
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_1 (check id='barrier_step1_NiCuFeOOH') ===
def score_1(artifact, step, ctx):
    system = step['params']['system']
    step_number = step['params']['step_number']
    target = step['params']['target']
    tol = step['params']['tolerance']
    artifact = [row for row in artifact if row['system'] == system and int(row['step_number']) == step_number]
    if not artifact:
        return 0.0
    agent_val = float(artifact[0]['barrier_ev'])
    diff = abs(agent_val - target)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_2 (check id='rate_limiting') ===
def score_2(artifact, step, ctx):
    systems = ['Ni-Cu-OOH', 'Ni-Cu-Fe-OOH']
    correct = 0
    for sys in systems:
        rows = [row for row in artifact if row['system'] == sys]
        if not rows:
            continue
        barriers = {int(row['step_number']): float(row['barrier_ev']) for row in rows}
        if 1 in barriers:
            max_barrier = max(barriers.values())
            if barriers[1] == max_barrier:
                correct += 1
    return correct / len(systems)


# === block: score_3 (check id='ratio') ===
def score_3(artifact, step, ctx):
    ni_cu = [row for row in artifact if row['system'] == step['params']['system_NiCu'] and int(row['step_number']) == step['params']['step_number']]
    ni_cu_fe = [row for row in artifact if row['system'] == step['params']['system_NiCuFe'] and int(row['step_number']) == step['params']['step_number']]
    if not ni_cu or not ni_cu_fe:
        return 0.0
    v1 = float(ni_cu[0]['barrier_ev'])
    v2 = float(ni_cu_fe[0]['barrier_ev'])
    if v2 <= 0:
        return 0.0
    agent_ratio = v1 / v2
    target = step['params']['target_ratio']
    tol = step['params']['tolerance_ratio']
    diff = abs(agent_ratio - target)
    if diff <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (diff - tol) / tol)


# === block: score_4 (check id='step5_sign') ===
def score_4(artifact, step, ctx):
    ni_cu_fe_row = [row for row in artifact if row['system'] == 'Ni-Cu-Fe-OOH' and int(row['step_number']) == 5]
    ni_cu_row = [row for row in artifact if row['system'] == 'Ni-Cu-OOH' and int(row['step_number']) == 5]
    score = 0.0
    if ni_cu_fe_row:
        score += 0.5 if float(ni_cu_fe_row[0]['barrier_ev']) < 0 else 0.0
    if ni_cu_row:
        score += 0.5 if float(ni_cu_row[0]['barrier_ev']) > 0 else 0.0
    return score


_SCORERS = {
    'barrier_step1_NiCuOOH': score_0,
    'barrier_step1_NiCuFeOOH': score_1,
    'rate_limiting': score_2,
    'ratio': score_3,
    'step5_sign': score_4,
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
