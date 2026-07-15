import os
import json
import csv

# === author imports / helpers ===
import os, json, csv

# path to agent's output artifacts (hard‑coded by the Harbour sandbox)
output_dir = '/app/outputs'


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
    # extract gold and tolerance from the first step
    param_step = next((s for s in spec['steps'] if s['output_file'] == 'fitted_parameters.json'), None)
    if param_step:
        ctx['gold'] = param_step.get('gold', {})
        ctx['tol'] = param_step.get('tolerance', 0.02)
    else:
        ctx['gold'] = {}
        ctx['tol'] = 0.02
    ctx['freq_checks'] = next((s['structural_checks'] for s in spec['steps'] if s['output_file'] == 'computed_phonon_frequencies.csv'), {})
    return ctx


# === block: score_0 (check id='step_03_fitting') ===
def score_0(artifact, step, ctx):
    artifact = load_artifact(os.path.join(output_dir, 'fitted_parameters.json'))
    gold = ctx.get('gold', {})
    tol = ctx.get('tol', 0.02)
    if not isinstance(artifact, dict):
        return 0.0
    total = 0
    match = 0
    for mat in gold:
        if mat not in artifact:
            continue
        mat_gold = gold[mat]
        mat_agent = artifact[mat]
        for key in mat_gold:
            total += 1
            if key in mat_agent:
                if abs(mat_gold[key] - mat_agent[key]) <= tol:
                    match += 1
    if total == 0:
        return 0.0
    return match / total


# === block: score_1 (check id='step_04_phonon_freqs') ===
def score_1(artifact, step, ctx):
    rows = load_artifact(os.path.join(output_dir, 'computed_phonon_frequencies.csv'))
    if not rows:
        return 0.0
    checks = ctx.get('freq_checks', {})
    required = checks.get('required_columns', ['material','qx','qy','qz','branch','frequency_THz','error_THz'])
    valid_branches = set(checks.get('valid_branches', ['LA','TA','LO','TO']))
    min_rows = checks.get('min_rows', 1)
    if len(rows) < min_rows:
        return 0.0
    # check columns present in first row
    first = rows[0]
    for col in required:
        if col not in first:
            return 0.0
    # audit every row
    for r in rows:
        for col in ['qx','qy','qz']:
            try:
                val = float(r[col])
            except (ValueError, TypeError):
                return 0.0
        try:
            freq = float(r['frequency_THz'])
        except (ValueError, TypeError):
            return 0.0
        if checks.get('require_nonnegative_frequency', True) and freq < 0:
            return 0.0
        try:
            err = float(r['error_THz'])
        except (ValueError, TypeError):
            return 0.0
        if checks.get('require_positive_or_zero_error', True) and err < 0:
            return 0.0
        branch = str(r['branch']).strip()
        if branch not in valid_branches:
            return 0.0
    return 1.0


_SCORERS = {
    'step_03_fitting': score_0,
    'step_04_phonon_freqs': score_1,
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
