import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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
    return {}


# === block: score_0 (check id='step_01_sfa_phase_diagram') ===
def score_0(artifact, step, ctx):
    import csv
    import math

    # artifact is a list of dicts, e.g. [{'U': '2.0', 'V1': '0.28', 'V2': '0.5', 'S_over_L': '0.0'}, ...]
    try:
        rows = artifact
    except:
        return 0.0

    if not rows or len(rows) < 5:
        return 0.0

    # Convert to floats
    U_vals = []
    V1_vals = []
    V2_vals = []
    S_vals = []
    for row in rows:
        try:
            u = float(row['U'])
            v1 = float(row['V1'])
            v2 = float(row['V2'])
            s = float(row['S_over_L'])
            U_vals.append(u)
            V1_vals.append(v1)
            V2_vals.append(v2)
            S_vals.append(s)
        except:
            continue

    if not U_vals:
        return 0.0

    # Sort by U
    zipped = sorted(zip(U_vals, V1_vals, V2_vals, S_vals))
    U_vals, V1_vals, V2_vals, S_vals = zip(*zipped)

    threshold = step.get('recompute', {}).get('V_zero_threshold', 0.01)
    U_c1_gold = step['recompute']['U_c1_gold']
    U_c1_tol = step['recompute']['U_c1_tol']
    U_c2_gold = step['recompute']['U_c2_gold']
    U_c2_tol = step['recompute']['U_c2_tol']
    S_OSM_gold = step['recompute']['S_OSM_gold']
    S_OSM_tol = step['recompute']['S_OSM_tol']
    S_MI_gold = step['recompute']['S_MI_gold']
    S_MI_tol = step['recompute']['S_MI_tol']

    # Find U_c1: first U where V1 < threshold
    U_c1 = None
    for u, v1 in zip(U_vals, V1_vals):
        if v1 < threshold:
            U_c1 = u
            break

    # Find U_c2: first U where V2 < threshold (and V1 already zero)
    U_c2 = None
    for u, v2 in zip(U_vals, V2_vals):
        if v2 < threshold:
            U_c2 = u
            break

    # Compute OSM mean entropy: U between U_c1 and U_c2, exclude endpoints if necessary
    # Only consider if both V1 < threshold and V2 >= threshold (or positive)
    OSM_S = []
    MI_S = []
    for u, v1, v2, s in zip(U_vals, V1_vals, V2_vals, S_vals):
        if U_c1 is not None and u >= U_c1:
            if U_c2 is None or u < U_c2:
                # OSM region: V1 should be near zero, V2 > threshold
                if v2 >= threshold:
                    OSM_S.append(s)
            else:
                # MI region: both near zero
                if v2 < threshold:
                    MI_S.append(s)

    S_OSM = sum(OSM_S)/len(OSM_S) if OSM_S else None
    S_MI = sum(MI_S)/len(MI_S) if MI_S else None

    sub_scores = {}
    if U_c1 is not None:
        sub_scores['U_c1'] = 1.0 if abs(U_c1 - U_c1_gold) <= U_c1_tol else 0.0
    else:
        sub_scores['U_c1'] = 0.0
    if U_c2 is not None:
        sub_scores['U_c2'] = 1.0 if abs(U_c2 - U_c2_gold) <= U_c2_tol else 0.0
    else:
        sub_scores['U_c2'] = 0.0
    if S_OSM is not None:
        sub_scores['S_OSM'] = 1.0 if abs(S_OSM - S_OSM_gold) <= S_OSM_tol else 0.0
    else:
        sub_scores['S_OSM'] = 0.0
    if S_MI is not None:
        sub_scores['S_MI'] = 1.0 if abs(S_MI - S_MI_gold) <= S_MI_tol else 0.0
    else:
        sub_scores['S_MI'] = 0.0

    # Weight sub-scores equally
    score = (sub_scores['U_c1'] + sub_scores['U_c2'] + sub_scores['S_OSM'] + sub_scores['S_MI']) / 4.0
    return score


# === block: score_1 (check id='step_02_transition_report') ===
def score_1(artifact, step, ctx):
    txt = artifact
    if not isinstance(txt, str):
        return 0.0
    lines = txt.strip().split('\n')
    data = {}
    for line in lines:
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip()
    targets = step.get('targets', {})
    fields = ['U_c1', 'U_c2', 'S_OSM', 'S_MI']
    U_tol = targets.get('U_tol', 0.2)
    S_tol = targets.get('S_tol', 0.05)
    score_parts = []
    for f in fields:
        gold = targets.get(f)
        if gold is None:
            continue
        val_str = data.get(f)
        if val_str is None:
            score_parts.append(0.0)
            continue
        try:
            val = float(val_str)
        except:
            score_parts.append(0.0)
            continue
        tol = U_tol if 'U_' in f else S_tol
        score_parts.append(1.0 if abs(val - gold) <= tol else 0.0)
    if not score_parts:
        return 0.0
    return sum(score_parts) / len(score_parts)


_SCORERS = {
    'step_01_sfa_phase_diagram': score_0,
    'step_02_transition_report': score_1,
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
