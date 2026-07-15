import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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
    gold_rows = {}
    for step in spec.get('steps', []):
        gdata = step.get('gold_data', {})
        if gdata:
            gold_rows.update(gdata.get('rows', {}))
    ctx['gold_rows'] = gold_rows
    return ctx


# === block: score_0 (check id='s02_simulation') ===
def score_0(artifact, step, ctx):
    import csv, json, math
    # artifact is list of dicts; step is the grading step dict; ctx from prepare
    rows = artifact
    gold_rows = ctx['gold_rows']
    tolerance = step.get('tolerance', 0.10)
    trend_checks = step.get('trend_checks', [])

    # build lookup from submitted rows by configuration and T_h
    submitted = {}
    for r in rows:
        conf = r.get('configuration', '').strip()
        th_str = str(float(r.get('T_h', 0)))
        key = f"{conf},{th_str}"
        submitted[key] = r

    # Scores for applicable metrics
    applicable_count = 0
    total_metric_score = 0.0
    for key, gold in gold_rows.items():
        if not gold.get('applicable', True):
            continue
        applicable_count += 1
        if key not in submitted:
            continue  # missing row scores 0
        row = submitted[key]
        scores_row = []
        for mcol, gkey in [('output_power', 'P'), ('conversion_efficiency', 'eta'), ('exergy_efficiency', 'eta_e')]:
            val = float(row.get(mcol, 0))
            gval = gold[gkey]
            threshold = gval * (1 - tolerance)
            if val >= threshold:
                scores_row.append(1.0)
            else:
                scores_row.append(max(0.0, val / gval))  # partial credit
        total_metric_score += sum(scores_row) / len(scores_row)

    avg_metric = total_metric_score / applicable_count if applicable_count else 0.0

    # Trend checks
    trend_score = 0.0
    if trend_checks:
        passed = 0
        # Extract values for trends
        rows_500 = [r for r in rows if float(r.get('T_h',0)) == 500.0]
        rows_800 = [r for r in rows if float(r.get('T_h',0)) == 800.0]
        def get_power(config, th):
            lst = rows_500 if th == 500 else rows_800
            for r in lst:
                if r.get('configuration','').strip() == config:
                    return float(r.get('output_power', 0))
            return None
        # Trend 1
        p1_500 = get_power('single_bi2te3', 500)
        p2_500 = get_power('serial_two_stage', 500)
        if p1_500 is not None and p2_500 is not None and p1_500 > p2_500:
            passed += 1
        # Trend 2
        p_ser_800 = get_power('serial_two_stage', 800)
        p_sku_800 = get_power('single_skutterudite', 800)
        if p_ser_800 is not None and p_sku_800 is not None and p_ser_800 > p_sku_800:
            passed += 1
        # Trend 3
        p_par_800 = get_power('parallel_two_stage', 800)
        if p_par_800 is not None and p_ser_800 is not None and p_par_800 > p_ser_800:
            passed += 1
        trend_score = passed / len(trend_checks)

    # Combine: 70% metric, 30% trends
    final_score = 0.7 * avg_metric + 0.3 * trend_score
    return round(final_score, 4)


_SCORERS = {
    's02_simulation': score_0,
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
