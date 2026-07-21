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
    spec = spec  # grading_spec_json already parsed
    ctx = {}
    return ctx


# === block: score_0 (check id='beams_ab_numerics') ===
def score_0(artifact, step, ctx):
    step_conf = step.get('config', {})
    gold = step_conf.get('gold', {})
    tol = step_conf.get('tolerances', {})

    data = artifact  # artifact is loaded from the JSON file

    def get_val(obj, path):
        keys = path.split('.')
        v = obj
        for k in keys:
            v = v.get(k)
            if v is None:
                return None
        return v

    def score_field(agent_val, target, field_name):
        if agent_val is None:
            return 0.0
        if not isinstance(agent_val, (int, float)):
            return 0.0
        # Determine tolerance type: for phi and D_z absolute, others relative
        if field_name in ('phi', 'D_z'):
            abs_tol = tol.get(field_name, 1.0)
            err = abs(agent_val - target)
            if err <= abs_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (err - abs_tol) / (abs_tol * 3))
        else:
            rel_tol = tol.get(field_name, 0.05)
            denom = max(abs(target), 1e-3)
            rel_err = abs(agent_val - target) / denom
            if rel_err <= rel_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (rel_err - rel_tol) / (rel_tol * 3))

    scores = []
    for beam_key, beam_gold in gold.items():
        beam_agent = data.get(f'beam_{beam_key}')
        if not beam_agent:
            continue
        for lc_key, lc_gold in beam_gold.items():
            lc_agent = beam_agent.get(lc_key)
            if not lc_agent:
                continue
            for s_key, s_gold in lc_gold.items():
                s_agent = lc_agent.get(s_key)
                if not s_agent:
                    continue
                for field, target in s_gold.items():
                    agent_val = s_agent.get(field)
                    sc = score_field(agent_val, target, field)
                    scores.append(sc)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='beam_c_structural') ===
def score_1(artifact, step, ctx):
    step_conf = step.get('config', {})
    top_bottom_tol = step_conf.get('top_bottom_potential_tol', 0.1)
    min_points = step_conf.get('min_profile_points', 10)

    data = artifact
    beam_c = data.get('beam_c')
    if not beam_c:
        return 0.0

    sub_scores = []
    for lc_key in ('load_case_1', 'load_case_2'):
        lc = beam_c.get(lc_key)
        if not lc:
            sub_scores.append(0.0)
            continue
        s5 = lc.get('S=5')
        if not s5:
            sub_scores.append(0.0)
            continue
        # w_center existence check
        w = s5.get('w_center')
        if w is None or not isinstance(w, (int, float)):
            sub_scores.append(0.0)
        else:
            sub_scores.append(0.3)
        # phi_profile structural checks
        profile = s5.get('phi_profile')
        if not isinstance(profile, list) or len(profile) < min_points:
            sub_scores.append(0.0)
            continue
        # check top and bottom points near zero
        try:
            top_val = None
            bot_val = None
            for p in profile:
                z = float(p.get('z/h'))
                phi_val = float(p.get('phi_nondim'))
                if abs(z - 0.5) < 1e-3:
                    top_val = phi_val
                if abs(z + 0.5) < 1e-3:
                    bot_val = phi_val
            top_ok = (top_val is not None) and (abs(top_val) <= top_bottom_tol)
            bot_ok = (bot_val is not None) and (abs(bot_val) <= top_bottom_tol)
            if top_ok and bot_ok:
                sub_scores.append(0.7)
            else:
                sub_scores.append(0.0)
        except Exception:
            sub_scores.append(0.0)
    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


_SCORERS = {
    'beams_ab_numerics': score_0,
    'beam_c_structural': score_1,
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
