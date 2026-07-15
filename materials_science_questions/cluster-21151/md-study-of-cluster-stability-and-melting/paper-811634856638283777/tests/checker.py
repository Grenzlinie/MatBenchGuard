import os
import json
import csv

# === author imports / helpers ===
import csv, math, statistics


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
    gold_raw = spec.get('hidden_reference', {}).get('rows', [])
    gold = {}
    for row in gold_raw:
        gold[row['oxygen_number']] = row
    return {
        'gold': gold,
        'hl_tol': 0.1,
        'opt_tol': 0.1,
        'be_tol': 0.2,
        'hl_std_max': 0.15,
        'opt_range_min': 0.1
    }


# === block: score_0 (check id='results_table') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    gold = ctx['gold']
    hl_tol = ctx['hl_tol']
    opt_tol = ctx['opt_tol']
    be_tol = ctx['be_tol']
    hl_std_max = ctx['hl_std_max']
    opt_range_min = ctx['opt_range_min']

    hl_vals = []
    opt_vals = []
    be_vals = []

    hl_scores = []
    opt_scores = []
    be_scores = []

    for row in artifact:
        try:
            ox = int(row.get('oxygen_number', None))
            hl = float(row.get('homolumo_gap_ev', None))
            opt = float(row.get('optical_gap_ev', None))
            be = float(row.get('binding_energy_ev_atom', None))
        except (TypeError, ValueError):
            continue
        ref = gold.get(ox)
        if ref is None:
            continue
        hl_vals.append(hl)
        opt_vals.append(opt)
        be_vals.append(be)

        error_hl = abs(hl - ref['homolumo_gap_ev'])
        error_opt = abs(opt - ref['optical_gap_ev'])
        error_be = abs(be - ref['binding_energy_ev_atom'])

        def linear_score(error, tol):
            if error <= tol:
                return 1.0
            if error >= 2 * tol:
                return 0.0
            return 1.0 - (error - tol) / tol

        hl_scores.append(linear_score(error_hl, hl_tol))
        opt_scores.append(linear_score(error_opt, opt_tol))
        be_scores.append(linear_score(error_be, be_tol))

    if not hl_vals:
        return 0.0

    avg_hl = sum(hl_scores) / len(hl_scores)
    avg_opt = sum(opt_scores) / len(opt_scores)
    avg_be = sum(be_scores) / len(be_scores)

    # trend HOMO-LUMO: low std
    std_hl = statistics.stdev(hl_vals) if len(hl_vals) > 1 else 0.0
    if std_hl <= 0.08:
        trend_hl = 1.0
    elif std_hl >= hl_std_max:
        trend_hl = 0.0
    else:
        trend_hl = 1.0 - (std_hl - 0.08) / (hl_std_max - 0.08)

    # trend optical: range
    opt_range = max(opt_vals) - min(opt_vals) if opt_vals else 0.0
    if opt_range >= 0.4:
        trend_opt = 1.0
    elif opt_range < 0.05:
        trend_opt = 0.0
    else:
        trend_opt = (opt_range - 0.05) / (0.4 - 0.05)

    score = 0.25 * avg_hl + 0.25 * avg_opt + 0.3 * avg_be + 0.1 * trend_hl + 0.1 * trend_opt
    return min(1.0, score)


_SCORERS = {
    'results_table': score_0,
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
