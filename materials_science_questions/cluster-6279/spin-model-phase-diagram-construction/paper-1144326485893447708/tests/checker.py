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
    vc_gold_data = {
        (23, 'y'): 8.5,
        (23, 'z'): 19.0,
        (36, 'y'): 6.5,
        (36, 'z'): 13.5,
        (199, 'y'): 3.5,
        (199, 'z'): 8.5,
        (223, 'y'): 2.5,
        (223, 'z'): 6.0
    }
    vc_tolerance = 1.0

    tc_gold = {
        'I': {'y': 88, 'y_tol': 28, 'z': 142, 'z_tol': 20},
        'II': {'y': 119, 'y_tol': 20, 'z': 177, 'z_tol': 20},
        'III': {'y': 236, 'y_tol': 20, 'z': 236, 'z_tol': 20},
        'IV': {'y': 151, 'y_tol': 23, 'z': 0, 'z_tol': 1},
        'V': {'y': 0, 'y_tol': 20, 'z': 95, 'z_tol': 23},
        'VI': {'y': 35, 'y_tol': 20, 'z': 35, 'z_tol': 20}
    }

    return {'vc_gold': vc_gold_data, 'vc_tol': vc_tolerance, 'tc_gold': tc_gold}


# === block: score_0 (check id='vc_values') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact: return 0.0
    vc_gold = ctx['vc_gold']
    vc_tol = ctx['vc_tol']

    def row_score(diff, tol):
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)

    scores = []
    for row in artifact:
        temp = float(row.get('temperature_nK'))
        direction = row.get('direction', '').strip()
        vc_val = float(row.get('V_c_Er'))
        key = (temp, direction)
        if key in vc_gold:
            gold_val = vc_gold[key]
            diff = abs(vc_val - gold_val)
            scores.append(row_score(diff, vc_tol))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='vc_trend') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact: return 0.0

    dir_rows = {}
    for row in artifact:
        d = row.get('direction', '').strip()
        temp = float(row.get('temperature_nK'))
        vc = float(row.get('V_c_Er'))
        dir_rows.setdefault(d, []).append((temp, vc))

    correct = 0
    total = 0
    for d in ('y', 'z'):
        if d not in dir_rows:
            continue
        rows = sorted(dir_rows[d])
        if len(rows) < 2:
            continue
        for i in range(len(rows)-1):
            total += 1
            if rows[i+1][1] <= rows[i][1] + 0.1:  # allow tiny increase
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_2 (check id='tc_values') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict): return 0.0
    tc_gold = ctx['tc_gold']

    def score_val(reported, gold, tol):
        # Use a floor tolerance of 20 nK for a zero/negligible gold to avoid
        # penalising honest piecewise fits that yield a small nonzero value.
        if abs(gold) < 1e-9:
            tol = max(tol, 20.0)
        if tol <= 0:
            tol = 0.1
        diff = abs(reported - gold)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)

    scores = []
    for point, gold_entry in tc_gold.items():
        if point not in artifact:
            continue
        entry = artifact[point]
        for dir_key, gold_val, tol_key in [('T_c_y_nK', gold_entry['y'], gold_entry['y_tol']),
                                           ('T_c_z_nK', gold_entry['z'], gold_entry['z_tol'])]:
            if dir_key in entry:
                val = float(entry[dir_key])
                scores.append(score_val(val, gold_val, tol_key))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'vc_values': score_0,
    'vc_trend': score_1,
    'tc_values': score_2,
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
