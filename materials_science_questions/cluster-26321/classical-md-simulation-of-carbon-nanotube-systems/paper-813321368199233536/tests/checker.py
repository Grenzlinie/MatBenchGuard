import os
import json
import csv

# === author imports / helpers ===
import csv, math, collections


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


# === block: score_0 (check id='permeation_rates') ===
def score_0(artifact, step, ctx):
    gold_rows = step['targets']['rows']
    cols = step['tolerance']['columns']
    tol = step['tolerance']['relative']
    # build lookup by (system, field)
    lookup = {}
    for r in gold_rows:
        key = (r['system'].strip().lower(), r['field'].strip().lower())
        lookup[key] = r
    scores = []
    for row in artifact:
        key = (row['system'].strip().lower(), row['field'].strip().lower())
        if key not in lookup:
            continue
        expected = lookup[key]
        cell_scores = []
        for c in cols:
            try:
                a = float(row[c])
                e = float(expected[c])
                if e == 0:
                    # skip or treat as perfect if agent also zero
                    cell_scores.append(1.0 if a == 0 else 0.0)
                    continue
                rel_err = abs(a - e) / abs(e)
                if rel_err <= tol:
                    cs = 1.0
                else:
                    cs = max(0.0, 1.0 - (rel_err - tol) / tol)
                cell_scores.append(cs)
            except (ValueError, TypeError):
                cell_scores.append(0.0)
        if cell_scores:
            scores.append(sum(cell_scores)/len(cell_scores))
    if not scores:
        return 0.0
    return sum(scores)/len(scores)


# === block: score_1 (check id='dipole_distribution') ===
def score_1(artifact, step, ctx):
    gold_bins = step['targets']['bins']
    tol = step['tolerance']['max_mean_abs_diff']
    # group gold by (system, field)
    gold_group = collections.defaultdict(list)
    for b in gold_bins:
        key = (b['system'].strip().lower(), b['field'].strip().lower())
        gold_group[key].append(b)
    # sort each group by cos_alpha_low
    for k in gold_group:
        gold_group[k].sort(key=lambda x: float(x['cos_alpha_low']))
    # group agent rows
    agent_group = collections.defaultdict(list)
    for row in artifact:
        key = (row['system'].strip().lower(), row['field'].strip().lower())
        agent_group[key].append(row)
    for k in agent_group:
        agent_group[k].sort(key=lambda x: float(x['cos_alpha_low']))
    # evaluate pairs
    mads = []
    for key in gold_group:
        if key not in agent_group:
            return 0.0
        gold_list = gold_group[key]
        agent_list = agent_group[key]
        if len(gold_list) != len(agent_list):
            return 0.0
        diffs = []
        for g, a in zip(gold_list, agent_list):
            try:
                g_prob = float(g['probability'])
                a_prob = float(a['probability'])
                diffs.append(abs(a_prob - g_prob))
            except (ValueError, TypeError):
                diffs.append(1.0)  # penalize
        if diffs:
            mads.append(sum(diffs)/len(diffs))
    if not mads:
        return 0.0
    avg_mad = sum(mads)/len(mads)
    if avg_mad <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (avg_mad - tol) / tol)


# === block: score_2 (check id='effective_viscosity') ===
def score_2(artifact, step, ctx):
    gold_rows = step['targets']['rows']
    col = step['tolerance']['column']
    tol = step['tolerance']['relative']
    # find agent row matching array_separation='15'
    agent_row = None
    for row in artifact:
        if str(row.get('array_separation', '')).strip() == '15':
            agent_row = row
            break
    if agent_row is None:
        return 0.0
    try:
        a = float(agent_row[col])
        e = float(gold_rows[0][col])
        if e == 0:
            return 1.0 if a == 0 else 0.0
        rel_err = abs(a - e) / abs(e)
        if rel_err <= tol:
            return 1.0
        else:
            return max(0.0, 1.0 - (rel_err - tol) / tol)
    except (ValueError, TypeError, KeyError):
        return 0.0


_SCORERS = {
    'permeation_rates': score_0,
    'dipole_distribution': score_1,
    'effective_viscosity': score_2,
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
