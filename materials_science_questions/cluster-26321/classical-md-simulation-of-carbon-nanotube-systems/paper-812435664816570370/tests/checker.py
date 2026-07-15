import os
import json
import csv

# === author imports / helpers ===
import statistics, math
from collections import defaultdict


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


# === block: score_0 (check id='step_01_free_energy') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    g = {}
    for r in rows:
        try:
            n = int(r['N'])
            g[n] = float(r['free_energy_kT'])
        except Exception:
            return 0.0
    required = [0,1,2,3,4,5]
    if not all(k in g for k in required):
        return 0.0
    score = 0.0
    if abs(g[0]) < 0.1:
        score += 0.25
    mono = all(g[i] < g[i+1] for i in range(0,4))
    if mono:
        score += 0.25
    if g[5] < g[4]:
        score += 0.25
    if 2.0 <= g[4] <= 6.0:
        score += 0.125
    if 1.0 <= g[5] <= 4.0:
        score += 0.125
    return score


# === block: score_1 (check id='step_02_commitment') ===
def score_1(artifact, step, ctx):
    p_vals = []
    for row in artifact:
        try:
            p = float(row['p_fill'])
            p_vals.append(p)
        except Exception:
            continue
    if len(p_vals) < 10:
        return 0.0
    mean_val = statistics.mean(p_vals)
    var_val = statistics.variance(p_vals) if len(p_vals) > 1 else 0.0
    ref = step['mean_target']
    tol = step['mean_tolerance']
    var_max = step['var_max']
    score = 0.0
    if abs(mean_val - ref) <= tol:
        score += 0.5
    if var_val <= var_max:
        score += 0.5
    return score


# === block: score_2 (check id='step_03_lifetimes') ===
def score_2(artifact, step, ctx):
    refs = step.get('ref_values', {})
    expected = len(refs)
    found = 0
    for row in artifact:
        tt = row.get('tube_type', '').strip().lower()
        st = row.get('state', '').strip().lower()
        try:
            mean_val = float(row['mean_lifetime_ps'])
        except Exception:
            continue
        if tt == 'short' and st == 'filled':
            key = 'short_filled'
        elif tt == 'short' and st == 'empty':
            key = 'short_empty'
        elif tt == 'long' and st == 'filled':
            key = 'long_filled'
        elif tt == 'long' and st == 'empty':
            key = 'long_empty'
        else:
            continue
        if key in refs:
            target = refs[key]['mean']
            tol = refs[key]['tol']
            if abs(mean_val - target) <= tol:
                found += 1
    return found / expected if expected else 0.0


# === block: score_3 (check id='step_04_lambda_dependence') ===
def score_3(artifact, step, ctx):
    refs = step.get('ref_slopes', {})
    lam_map = {0.75:'0.75', 0.785:'0.785', 1.0:'1.0'}
    found = 0
    total = len(refs)
    for row in artifact:
        try:
            lam = float(row['lambda'])
            slope = float(row['slope'])
        except Exception:
            continue
        matched = None
        for lkey, lref in lam_map.items():
            if abs(lam - lkey) < 0.01:
                matched = lref
                break
        if matched and matched in refs:
            target = refs[matched]['slope']
            tol = refs[matched]['tol']
            if abs(slope - target) <= tol:
                found += 1
    return found / total if total else 0.0


_SCORERS = {
    'step_01_free_energy': score_0,
    'step_02_commitment': score_1,
    'step_03_lifetimes': score_2,
    'step_04_lambda_dependence': score_3,
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
