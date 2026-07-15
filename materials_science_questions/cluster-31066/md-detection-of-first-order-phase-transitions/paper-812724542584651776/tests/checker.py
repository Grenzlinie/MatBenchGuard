import os
import json
import csv

# === author imports / helpers ===
import csv
import json
import os


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
    spec = json.load(open('/tests/grading_spec.json'))
    step02 = next(s for s in spec['steps'] if s['id'] == 'step_02_recompute')
    return {'gold_slopes': step02['params']['gold_slopes'], 'tolerance_frac': step02['params']['tolerance_frac']}


# === block: score_0 (check id='step_01_audit') ===
def score_0(artifact, step, ctx):
    import csv
    import os

    def scorer(artifact, step, ctx):
        # artifact is a list of dicts (loaded CSV)
        # step.params contains required_columns, pzz_drop_threshold, transition_ranges
        params = step.get('params', {})
        required = params.get('required_columns', [])
        if not required:
            return 0.0
        # check all required columns present in header
        if not artifact:
            return 0.0
        header = list(artifact[0].keys())
        if not all(col in header for col in required):
            return 0.0
        # extract H and Pzz, sorted by H descending (compression direction)
        rows = []
        for r in artifact:
            try:
                H_val = r.get('H')
                Pzz_val = r.get('Pzz')
                if H_val is None or Pzz_val is None:
                    continue
                H = float(H_val)
                Pzz = float(Pzz_val)
                rows.append((H, Pzz))
            except (ValueError, TypeError):
                continue
        if len(rows) < 2:
            return 0.0
        rows.sort(key=lambda x: x[0], reverse=True)  # descending H
        # detect drops > threshold
        thr = float(params.get('pzz_drop_threshold', 50.0))
        ranges = params.get('transition_ranges', [])
        detections = [False] * len(ranges)
        for i in range(1, len(rows)):
            H_prev, Pzz_prev = rows[i-1]
            H_curr, Pzz_curr = rows[i]
            drop = Pzz_curr - Pzz_prev
            if drop < -thr:
                mean_H = (H_prev + H_curr) / 2
                for j, (lo, hi) in enumerate(ranges):
                    if lo <= mean_H <= hi:
                        detections[j] = True
        score = sum(1 for d in detections if d) * 0.5
        return min(score, 1.0)


# === block: score_1 (check id='step_02_recompute') ===
def score_1(artifact, step, ctx):
    import json
    import os

    def scorer(artifact, step, ctx):
        # artifact is the loaded JSON object (the agent's step_02 output)
        # artifact should have keys 'alpha_beta' and 'beta_gamma'
        if not isinstance(artifact, dict):
            return 0.0
        required_keys = ['alpha_beta', 'beta_gamma']
        if not all(k in artifact for k in required_keys):
            return 0.0
        gold = ctx.get('gold_slopes', {})
        tol = ctx.get('tolerance_frac', 0.5)
        sub_slope_keys = ['dT_dPxx', 'dPxx_dH', 'dH_dT']
        matches = []
        for phase_key in required_keys:
            if phase_key not in gold:
                return 0.0
            agent_phase = artifact[phase_key]
            gold_phase = gold[phase_key]
            if not isinstance(agent_phase, dict):
                return 0.0
            for sk in sub_slope_keys:
                if sk not in agent_phase or sk not in gold_phase:
                    return 0.0
                val = float(agent_phase[sk])
                ref = float(gold_phase[sk])
                # check sign match
                if (val >= 0) != (ref >= 0):
                    matches.append(0.0)
                    continue
                if abs(ref) < 1e-12:
                    matches.append(1.0 if abs(val) < 1e-12 else 0.0)
                else:
                    rel_err = abs(val - ref) / abs(ref)
                    matches.append(1.0 if rel_err <= tol else 0.0)
        if not matches:
            return 0.0
        return sum(matches) / len(matches)


_SCORERS = {
    'step_01_audit': score_0,
    'step_02_recompute': score_1,
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
