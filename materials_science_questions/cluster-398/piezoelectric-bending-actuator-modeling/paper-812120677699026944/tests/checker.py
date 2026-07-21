import os
import json
import csv

# === author imports / helpers ===
"""Checker imports."""
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
    spec_steps = spec.get('steps', [])
    refs = {}
    for s in spec_steps:
        if s.get('kind') == 'numeric' and 'reference' in s:
            refs[s['id']] = s['reference']
        if s['id'] == 'step_02_actuator':
            ref = s['reference']
            refs['step_02_actuator_ex_range'] = max(ref['Ex_field']) - min(ref['Ex_field'])
            refs['step_02_actuator_sig_range'] = max(ref['sigma_yy']) - min(ref['sigma_yy'])
    return refs


# === block: score_0 (check id='step_01_hole') ===
def score_0(artifact, step, ctx):
    import math
    ref = ctx.get('step_01_hole')
    if not ref:
        return 0.0
    agent_sigma = [float(r['sigma_normalized']) for r in artifact]
    agent_D = [float(r['D_normalized']) for r in artifact]
    if len(agent_sigma) != len(ref['sigma_normalized']) or len(agent_D) != len(ref['D_normalized']):
        return 0.0
    rmse_s = math.sqrt(sum((a - b)**2 for a,b in zip(agent_sigma, ref['sigma_normalized'])) / len(agent_sigma))
    rmse_d = math.sqrt(sum((a - b)**2 for a,b in zip(agent_D, ref['D_normalized'])) / len(agent_D))
    rmse_avg = 0.5*(rmse_s + rmse_d)
    tol = step.get('tolerance', 0.08)
    if rmse_avg <= tol:
        return 1.0
    else:
        score = 1.0 - (rmse_avg - tol) / 0.12
        return max(0.0, min(1.0, score))


# === block: score_1 (check id='step_02_actuator') ===
def score_1(artifact, step, ctx):
    ref = ctx.get('step_02_actuator')
    ex_range = ctx.get('step_02_actuator_ex_range', 1.0)
    sig_range = ctx.get('step_02_actuator_sig_range', 1.0)
    if not ref or not artifact:
        return 0.0
    agent_x = [float(r['x_over_H']) for r in artifact]
    agent_ex = [float(r['Ex_field']) for r in artifact]
    agent_sig = [float(r['sigma_yy']) for r in artifact]
    ref_x = ref['x_over_H']
    ref_ex = ref['Ex_field']
    ref_sig = ref['sigma_yy']
    if len(agent_ex) != len(ref_ex) or len(agent_sig) != len(ref_sig):
        return 0.0
    max_dev_ex = max(abs(a - b) for a,b in zip(agent_ex, ref_ex))
    max_dev_sig = max(abs(a - b) for a,b in zip(agent_sig, ref_sig))
    norm_ex = max_dev_ex / (ex_range + 1e-9)
    norm_sig = max_dev_sig / (sig_range + 1e-9)
    norm_err = max(norm_ex, norm_sig)
    tol = 0.15
    if norm_err <= tol:
        return 1.0
    else:
        score = 1.0 - (norm_err - tol) / 0.35
        return max(0.0, min(1.0, score))


_SCORERS = {
    'step_01_hole': score_0,
    'step_02_actuator': score_1,
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
