import os
import json
import csv

# === author imports / helpers ===
import csv, json, os, math


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


# === block: score_0 (check id='metrics_summary') ===
def score_0(artifact, step, ctx):
    rows = artifact
    config = step.get("config", {})
    elements = config.get("elements", [])
    metrics_defs = config.get("metrics", {})

    by_element = {}
    for row in rows:
        e = row.get("element", "")
        by_element[e] = row

    # ---- compute aggregate scores for P90 / P80 (paper only gives overall averages) ----
    AGGREGATE_GOLD = {"P90": 93.6, "P80": 97.7}
    AGGREGATE_TOL = {"P90": 5.0, "P80": 5.0}

    aggregate_score = {}
    for metric in ("P90", "P80"):
        vals = []
        for elem in elements:
            row = by_element.get(elem)
            if row is None:
                continue
            v = row.get(metric, "")
            if v == "":
                continue
            try:
                vals.append(float(v))
            except ValueError:
                continue
        if not vals:
            aggregate_score[metric] = 0.0
            continue
        avg = sum(vals) / len(vals)
        gold = AGGREGATE_GOLD[metric]
        tol = AGGREGATE_TOL[metric]
        threshold = gold - tol   # higher_is_better
        if threshold <= 0:
            threshold = 1e-9
        if avg >= threshold:
            aggregate_score[metric] = 1.0
        else:
            aggregate_score[metric] = max(0.0, avg / threshold)

    score_total = 0.0
    count = 0
    for elem in elements:
        row = by_element.get(elem)
        if row is None:
            continue
        for metric_name, mdef in metrics_defs.items():
            val_str = row.get(metric_name, "")
            if val_str == "":
                continue
            try:
                val = float(val_str)
            except ValueError:
                continue

            # For P90 and P80, use the aggregate score
            if metric_name in ("P90", "P80"):
                score_cell = aggregate_score.get(metric_name, 0.0)
            else:
                gold = mdef.get("gold", {}).get(elem)
                if gold is None:
                    continue
                tol = float(mdef.get("tolerance", 0.0))
                direction = mdef.get("direction", "")
                if direction == "higher_is_better":
                    threshold = gold - tol
                    if threshold <= 0:
                        threshold = 1e-9
                    if val >= threshold:
                        score_cell = 1.0
                    else:
                        score_cell = max(0.0, val / threshold)
                elif direction == "lower_is_better":
                    threshold = gold + tol
                    if threshold <= 0:
                        threshold = 1e-9
                    if val <= threshold:
                        score_cell = 1.0
                    else:
                        if val > 0:
                            score_cell = max(0.0, threshold / val)
                        else:
                            score_cell = 1.0
                else:
                    score_cell = 0.0

            score_total += score_cell
            count += 1

    if count == 0:
        return 0.0
    avg_score = score_total / count
    return min(1.0, max(0.0, avg_score))


_SCORERS = {
    'metrics_summary': score_0,
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
