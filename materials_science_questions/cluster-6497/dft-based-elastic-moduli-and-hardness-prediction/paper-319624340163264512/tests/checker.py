import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    gold_list = spec["gold_table"]
    double_weight_cols = {"chi1", "epsilon_inf", "epsilon_0", "B"}
    # Build lookup dict keyed by (compound.lower(), source.lower()) for case‑insensitive matching
    gold_rows = {}
    for g in gold_list:
        key = (str(g["compound"]).strip().lower(), str(g["source"]).strip().lower())
        gold_rows[key] = {k: v for k, v in g.items() if k not in ("compound", "source")}
    return {"gold_rows": gold_rows, "double_weight_cols": double_weight_cols, "gold_count": len(gold_list)}


# === block: score_0 (check id='properties_check') ===
def score_0(artifact, step, ctx):
    agent_rows = artifact
    if not isinstance(agent_rows, list) or len(agent_rows) == 0:
        return 0.0
    gold_rows = ctx["gold_rows"]
    double_weight_cols = ctx["double_weight_cols"]
    gold_count = ctx["gold_count"]
    # Column names from gold (any gold row)
    sample_gold = next(iter(gold_rows.values()))
    num_cols = [col for col in sample_gold.keys()]
    row_scores = []
    for gold_key, gold_vals in gold_rows.items():
        # find matching agent row
        agent_row = None
        for ar in agent_rows:
            if str(ar.get("compound", "")).strip().lower() == gold_key[0] and str(ar.get("source", "")).strip().lower() == gold_key[1]:
                agent_row = ar
                break
        if agent_row is None:
            row_scores.append(0.0)
            continue
        correct_w = 0.0
        total_w = 0.0
        for col in num_cols:
            w = 2.0 if col in double_weight_cols else 1.0
            total_w += w
            if col not in agent_row:
                continue
            try:
                gold_val = float(gold_vals[col])
                agent_val = float(agent_row[col])
            except (TypeError, ValueError):
                continue
            if abs(gold_val) < 0.05:
                passed = abs(agent_val - gold_val) <= 0.005
            else:
                passed = abs((agent_val - gold_val) / gold_val) <= 0.10
            if passed:
                correct_w += w
        row_score = (correct_w / total_w) if total_w > 0 else 0.0
        row_scores.append(row_score)
    if gold_count == 0:
        return 0.0
    return sum(row_scores) / gold_count


_SCORERS = {
    'properties_check': score_0,
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
