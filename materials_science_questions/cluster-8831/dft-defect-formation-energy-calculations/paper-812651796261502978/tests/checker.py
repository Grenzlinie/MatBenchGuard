import os
import json
import csv

# === author imports / helpers ===
import csv
import io
import json
import os

def find_rows_by_compound(artifact, compound_col="Compound"):
    rows = {}
    if not artifact:
        return rows
    for row in artifact:
        compound = row.get(compound_col, "").strip()
        if compound:
            rows[compound] = row
    return rows

def numeric_score(agent_val, gold_val, tol_abs=None, tol_rel=None):
    if gold_val is None:
        return 0.0
    err = abs(agent_val - gold_val)
    if tol_rel is not None and gold_val != 0.0:
        rel_err = err / abs(gold_val)
        if rel_err <= tol_rel:
            return 1.0
        upper = 3.0 * tol_rel
        if rel_err >= upper:
            return 0.0
        return (upper - rel_err) / (upper - tol_rel)
    if tol_abs is not None:
        if err <= tol_abs:
            return 1.0
        upper = 3.0 * tol_abs
        if err >= upper:
            return 0.0
        return (upper - err) / (upper - tol_abs)
    # no tolerance -> exact match
    return 1.0 if err == 0.0 else 0.0

def eval_trend(artifact, trend_check, rows):
    ttype = trend_check["type"]
    col = trend_check["column"]
    if ttype == "monotonic_decreasing":
        order = trend_check["compounds_order"]
        vals = []
        for comp in order:
            row = rows.get(comp)
            if row is None:
                return 0.0
            try:
                val = float(row[col])
            except (ValueError, KeyError):
                return 0.0
            vals.append(val)
        for i in range(len(vals)-1):
            if vals[i] <= vals[i+1] - 1e-6:
                return 0.0
        return 1.0
    elif ttype == "greater_than_all_others":
        compound = trend_check["compound"]
        other_comps = trend_check["other_compounds"]
        target_val = None
        if rows.get(compound):
            try:
                target_val = float(rows[compound][col])
            except (ValueError, KeyError):
                pass
        if target_val is None:
            return 0.0
        max_other = -float('inf')
        for oc in other_comps:
            other_row = rows.get(oc)
            if other_row:
                try:
                    ov = float(other_row[col])
                except (ValueError, KeyError):
                    continue
                if ov > max_other:
                    max_other = ov
        if target_val > max_other + 1e-6:
            return 1.0
        else:
            return 0.0
    return 0.0


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


# === block: score_0 (check id='step_01_lattice_params') ===
def score_0(artifact, step, ctx):
    rows = find_rows_by_compound(artifact)
    if not rows: return 0.0
    gold_list = step.get("gold", [])
    tolerance = step.get("tolerance", {})
    scores = []
    for gold_row in gold_list:
        comp = gold_row["Compound"]
        if comp not in rows:
            return 0.0
        row = rows[comp]
        for field, tol in tolerance.items():
            gold_val = gold_row[field]
            try:
                agent_val = float(row[field])
            except (ValueError, KeyError):
                return 0.0
            rel = tol.get("rel")
            abs_t = tol.get("abs")
            s = numeric_score(agent_val, gold_val, tol_abs=abs_t, tol_rel=rel)
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_02_band_gaps') ===
def score_1(artifact, step, ctx):
    rows = find_rows_by_compound(artifact)
    if not rows: return 0.0
    gold_list = step.get("gold", [])
    tolerance = step.get("tolerance", {})
    trend_checks = step.get("trend_checks", [])
    scores = []
    for gold_row in gold_list:
        comp = gold_row["Compound"]
        if comp not in rows:
            return 0.0
        row = rows[comp]
        for field, tol in tolerance.items():
            gold_val = gold_row[field]
            try:
                agent_val = float(row[field])
            except (ValueError, KeyError):
                return 0.0
            abs_t = tol.get("abs")
            rel = tol.get("rel")
            s = numeric_score(agent_val, gold_val, tol_abs=abs_t, tol_rel=rel)
            scores.append(s)
    for tc in trend_checks:
        s = eval_trend(artifact, tc, rows)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step_03_apparent_gaps') ===
def score_2(artifact, step, ctx):
    rows = find_rows_by_compound(artifact)
    if not rows: return 0.0
    gold_list = step.get("gold", [])
    tolerance = step.get("tolerance", {})
    trend_checks = step.get("trend_checks", [])
    scores = []
    for gold_row in gold_list:
        comp = gold_row["Compound"]
        if comp not in rows:
            return 0.0
        row = rows[comp]
        for field, tol in tolerance.items():
            gold_val = gold_row[field]
            try:
                agent_val = float(row[field])
            except (ValueError, KeyError):
                return 0.0
            abs_t = tol.get("abs")
            rel = tol.get("rel")
            s = numeric_score(agent_val, gold_val, tol_abs=abs_t, tol_rel=rel)
            scores.append(s)
    for tc in trend_checks:
        s = eval_trend(artifact, tc, rows)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_3 (check id='step_05_band_offsets') ===
def score_3(artifact, step, ctx):
    rows = find_rows_by_compound(artifact)
    if not rows: return 0.0
    gold_list = step.get("gold", [])
    tolerance = step.get("tolerance", {})
    threshold_check = step.get("threshold_check", {})
    trend_checks = step.get("trend_checks", [])
    scores = []
    for gold_row in gold_list:
        comp = gold_row["Compound"]
        if comp not in rows:
            return 0.0
        row = rows[comp]
        for field, tol in tolerance.items():
            if threshold_check and comp == threshold_check.get("compound") and field == threshold_check.get("column"):
                try:
                    agent_val = float(row[field])
                except (ValueError, KeyError):
                    return 0.0
                th = threshold_check["threshold"]
                direction = threshold_check.get("direction", "less_than_or_equal")
                if direction == "less_than_or_equal":
                    full = threshold_check.get("score_full", 1.0)
                    partial = threshold_check.get("score_partial", 0.0)
                    partial_limit = threshold_check.get("partial_limit", th)
                    if agent_val <= th:
                        s = full
                    elif partial_limit is not None and agent_val <= partial_limit:
                        s = partial
                    else:
                        s = 0.0
                else:
                    s = 0.0
                scores.append(s)
            else:
                gold_val = gold_row[field]
                try:
                    agent_val = float(row[field])
                except (ValueError, KeyError):
                    return 0.0
                abs_t = tol.get("abs")
                rel = tol.get("rel")
                s = numeric_score(agent_val, gold_val, tol_abs=abs_t, tol_rel=rel)
                scores.append(s)
    for tc in trend_checks:
        s = eval_trend(artifact, tc, rows)
        scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_01_lattice_params': score_0,
    'step_02_band_gaps': score_1,
    'step_03_apparent_gaps': score_2,
    'step_05_band_offsets': score_3,
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
