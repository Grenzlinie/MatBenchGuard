import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='water_outlet_temp') ===
def score_0(artifact, step, ctx):
    nodes = artifact.get('nodes', [])
    if not nodes:
        return 0.0
    last = nodes[-1]
    val = last.get('T_water')
    if val is None:
        return 0.0
    err = abs(val - step['target'])
    tol = step['tolerance_abs']
    if err <= tol:
        return 1.0
    return max(0.0, 1.0 - (err - tol) / tol)


# === block: score_1 (check id='total_qout_te') ===
def score_1(artifact, step, ctx):
    nodes = artifact.get('nodes', [])
    qout = sum(n.get('Q_out_TE', 0.0) for n in nodes)
    target = step['target']
    if target == 0:
        return 0.0
    rel_err = abs(qout - target) / target
    tol = step['tolerance_rel']
    if rel_err <= tol:
        return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_2 (check id='total_power') ===
def score_2(artifact, step, ctx):
    nodes = artifact.get('nodes', [])
    power = sum(n.get('P_TEG', 0.0) for n in nodes)
    target = step['target']
    if target == 0:
        return 0.0
    rel_err = abs(power - target) / target
    tol = step['tolerance_rel']
    if rel_err <= tol:
        return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_3 (check id='total_efficiency') ===
def score_3(artifact, step, ctx):
    nodes = artifact.get('nodes', [])
    p_total = sum(n.get('P_TEG', 0.0) for n in nodes)
    qin = sum(n.get('Q_in_TE', 0.0) for n in nodes)
    if qin == 0:
        return 0.0
    eta = p_total / qin
    target = step['target']
    rel_err = abs(eta - target) / target
    tol = step['tolerance_rel']
    if rel_err <= tol:
        return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_4 (check id='delta_eta_sofc') ===
def score_4(artifact, step, ctx):
    nodes = artifact.get('nodes', [])
    p_total = sum(n.get('P_TEG', 0.0) for n in nodes)
    delta = p_total / 700.0 * 46.0
    target = step['target']
    rel_err = abs(delta - target) / target
    tol = step['tolerance_rel']
    if rel_err <= tol:
        return 1.0
    return max(0.0, 1.0 - (rel_err - tol) / tol)


# === block: score_5 (check id='temperature_monotonicity') ===
def score_5(artifact, step, ctx):
    nodes = artifact.get('nodes', [])
    if len(nodes) < 2:
        return 0.0
    ex_v, w_v = 0, 0
    for i in range(len(nodes)-1):
        if nodes[i+1].get('T_ex', 0.0) > nodes[i].get('T_ex', 0.0):
            ex_v += 1
        if nodes[i+1].get('T_water', 0.0) < nodes[i].get('T_water', 0.0):
            w_v += 1
    ex_score = max(0.0, 1.0 - ex_v / (len(nodes)-1))
    water_score = max(0.0, 1.0 - w_v / (len(nodes)-1))
    return (ex_score + water_score) / 2.0


_SCORERS = {
    'water_outlet_temp': score_0,
    'total_qout_te': score_1,
    'total_power': score_2,
    'total_efficiency': score_3,
    'delta_eta_sofc': score_4,
    'temperature_monotonicity': score_5,
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
