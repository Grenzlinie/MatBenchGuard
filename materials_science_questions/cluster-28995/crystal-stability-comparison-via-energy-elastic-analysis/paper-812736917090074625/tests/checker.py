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
    return {}


# === block: score_0 (check id='step_main') ===
def score_0(artifact, step, ctx):
    # read CSV artifact, match required conditions, compare z/w with tolerances, check trends
    rows = artifact  # loaded as list of dicts
    # Build lookup keyed by (eta, t) rounded to 6 decimals
    lookup = {}
    for r in rows:
        try:
            eta = float(r['eta'])
            t = float(r['t'])
            key = (round(eta, 6), round(t, 6))
            if key not in lookup:
                lookup[key] = r
        except:
            continue

    tol_z = step.get('tolerance_fraction', 0.2)
    tol_w = step.get('tolerance_fraction', 0.2)
    conditions = step['conditions']

    passed = 0
    total = 0
    rows_t05 = []  # for trend check

    for cond_group, cond in conditions.items():
        t_cond = cond['t']
        for eta_s in cond['etas']:
            eta_cond = float(eta_s)
            total += 1
            key = (round(eta_cond, 6), round(t_cond, 6))
            if key in lookup:
                row = lookup[key]
                gold = cond['gold'][eta_s]
                z_ok = abs(float(row['z']) - gold['z']) <= tol_z
                w_ok = abs(float(row['w']) - gold['w']) <= tol_w
                if z_ok and w_ok:
                    passed += 1
                if t_cond == 0.05:
                    rows_t05.append((eta_cond, float(row['z']), float(row['w'])))
            # else missing row: count as failed

    value_score = passed / total if total > 0 else 0.0

    # Trend checks
    trend_score = 1.0
    if step.get('trend_check', {}).get('t0.05_monotonic_z', False):
        rows_sorted = sorted(rows_t05, key=lambda x: x[0])
        z_vals = [z for _, z, _ in rows_sorted]
        for i in range(1, len(z_vals)):
            if z_vals[i] < z_vals[i-1] - 0.1:
                trend_score = 0.0
                break

    w_zero_thresh = step.get('trend_check', {}).get('t0.05_w_zero_below_thresh', None)
    if w_zero_thresh is not None:
        for eta, _, w in rows_t05:
            if eta <= w_zero_thresh and abs(w) > 0.001:
                trend_score = 0.0
                break

    final_score = 0.7 * value_score + 0.3 * trend_score
    return min(1.0, max(0.0, final_score))


_SCORERS = {
    'step_main': score_0,
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
