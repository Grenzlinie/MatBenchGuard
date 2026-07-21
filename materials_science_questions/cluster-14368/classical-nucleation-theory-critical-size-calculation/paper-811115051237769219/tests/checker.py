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
    # Gold values extracted from the paper's Fig.2 (growth rates at σ∞=0.6) and Fig.5 (critical supersaturations).
    # widths are in units of a0; growth_rate is dimensionless; critical_supersaturation is dimensionless.
    gold_growth = {
        6.0: 1e-07,
        8.0: 3e-07,
        10.0: 1e-06,
        15.0: 8e-06,
        20.0: 1.5e-05,
        40.0: 2.8e-05,
        160.0: 4e-05,
    }
    gold_crit = {
        8.0: 0.45,
        15.0: 0.24,
    }
    return {"growth_gold": gold_growth, "crit_gold": gold_crit}


# === block: score_0 (check id='growth_rate_values') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = ctx.get("growth_gold", {})
    if not gold:
        return 0.0
    rel_tol = step.get("params", {}).get("rel_tol", 0.2)
    row_by_width = {}
    for row in artifact:
        try:
            w = float(row.get("width"))
            r = float(row.get("growth_rate"))
            row_by_width[w] = r
        except (ValueError, TypeError):
            continue
    scores = 0.0
    count = 0
    for width, gold_val in gold.items():
        count += 1
        val = row_by_width.get(width)
        if val is None:
            continue
        denom = abs(gold_val) if abs(gold_val) > 1e-15 else 1e-15
        if abs(val - gold_val) / denom <= rel_tol:
            scores += 1.0
    return scores / count if count > 0 else 0.0


# === block: score_1 (check id='growth_rate_trend') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) < 2:
        return 0.0
    try:
        pairs = []
        for row in artifact:
            w = float(row.get("width"))
            r = float(row.get("growth_rate"))
            pairs.append((w, r))
        pairs.sort(key=lambda x: x[0])
        for i in range(len(pairs) - 1):
            if pairs[i+1][1] < pairs[i][1] - 1e-15:
                return 0.0
        return 1.0
    except (ValueError, TypeError):
        return 0.0


# === block: score_2 (check id='crit_sup_values') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = ctx.get("crit_gold", {})
    if not gold:
        return 0.0
    abs_tol = step.get("params", {}).get("abs_tol", 0.1)
    row_by_width = {}
    for row in artifact:
        try:
            w = float(row.get("width"))
            s = float(row.get("critical_supersaturation"))
            row_by_width[w] = s
        except (ValueError, TypeError):
            continue
    scores = 0.0
    count = 0
    for width, gold_val in gold.items():
        count += 1
        val = row_by_width.get(width)
        if val is None:
            continue
        if abs(val - gold_val) <= abs_tol:
            scores += 1.0
    return scores / count if count > 0 else 0.0


# === block: score_3 (check id='crit_sup_trend') ===
def score_3(artifact, step, ctx):
    if not artifact or len(artifact) < 2:
        return 0.0
    try:
        pairs = []
        for row in artifact:
            w = float(row.get("width"))
            s = float(row.get("critical_supersaturation"))
            pairs.append((w, s))
        pairs.sort(key=lambda x: x[0])
        for i in range(len(pairs) - 1):
            if pairs[i+1][1] > pairs[i][1] + 1e-15:
                return 0.0
        return 1.0
    except (ValueError, TypeError):
        return 0.0


_SCORERS = {
    'growth_rate_values': score_0,
    'growth_rate_trend': score_1,
    'crit_sup_values': score_2,
    'crit_sup_trend': score_3,
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