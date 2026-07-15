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
    ctx = {}
    for step in (spec.get('steps') or spec.get('checks') or []):
        sid = step.get('id', '')
        if sid == 'transition_levels_check':
            ctx['gold_transition'] = step['parameters']['gold']
        elif sid == 'optical_transitions_check':
            ctx['gold_optical'] = step['parameters']['gold']
        elif sid == 'valence_summary_check':
            ctx['gold_valence'] = step['parameters']['gold']
    return ctx


# === block: score_0 (check id='transition_levels_check') ===
def score_0(artifact, step, ctx):
    agent_tl = artifact.get('transition_levels', {})
    gold = ctx.get('gold_transition', {})
    tol = step['parameters'].get('tolerance_abs_eV', 0.2)
    scores = []
    for ln in ['La','Ce','Eu','Yb','Lu']:
        gold_val = gold.get(ln, {})
        agent_val = agent_tl.get(ln, {})
        if not isinstance(agent_val, dict):
            scores.append(0.0)
            continue
        for key in ['epsilon_plus_over_0','epsilon_0_over_minus']:
            gold_eps = gold_val.get(key)
            agent_eps = agent_val.get(key)
            if gold_eps is None:
                if agent_eps is None:
                    scores.append(1.0)
                else:
                    scores.append(0.0)
            else:
                if agent_eps is None:
                    scores.append(0.0)
                else:
                    err = abs(agent_eps - gold_eps)
                    scores.append(1.0 if err <= tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='optical_transitions_check') ===
def score_1(artifact, step, ctx):
    agent_opt = artifact.get('optical_transitions', {})
    gold_opt = ctx.get('gold_optical', {})
    tol = step['parameters'].get('tolerance_abs_eV', 0.3)
    scores = []
    for ln in ['Ce','Eu']:
        gold_v = gold_opt.get(ln)
        agent_v = agent_opt.get(ln)
        if not isinstance(agent_v, dict):
            scores.extend([0.0]*2)
            continue
        for key in ['absorption_eV','emission_eV']:
            gold_val = gold_v.get(key)
            agent_val = agent_v.get(key)
            if gold_val is None or agent_val is None:
                scores.append(0.0)
            else:
                err = abs(agent_val - gold_val)
                scores.append(1.0 if err <= tol else 0.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='valence_summary_check') ===
def score_2(artifact, step, ctx):
    agent_valence = artifact.get('valence_summary', {})
    gold_valence = ctx.get('gold_valence', {})
    scores = []
    for ln in ['La','Ce','Eu','Yb','Lu']:
        gold = gold_valence.get(ln)
        agent = agent_valence.get(ln)
        if isinstance(agent, str) and agent == gold:
            scores.append(1.0)
        else:
            scores.append(0.0)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'transition_levels_check': score_0,
    'optical_transitions_check': score_1,
    'valence_summary_check': score_2,
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
