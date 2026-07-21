import os
import json
import csv

# === author imports / helpers ===
import math, statistics


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


# === block: score_0 (check id='trends_audit') ===
def score_0(artifact, step, ctx):
    data = artifact
    params = step.get('params', {})
    low_T_target = params.get('low_temperature', 0.5)
    open_m = params.get('open_bc_m', 6)
    helicity_open_max = params.get('helicity_open_max', 0.1)
    closed_orders = params.get('closed_bc_orders', [4,5,6,7])
    ratio_min = params.get('decrease_ratio_min', 1.0)
    heat_capacity_std_max = params.get('heat_capacity_std_max', 0.2)
    heat_capacity_ref_T = params.get('heat_capacity_ref_T', 0.8)

    def find_closest_T(rows, target):
        return min(rows, key=lambda r: abs(float(r['temperature']) - target))

    groups = {}
    for row in data:
        m = int(row['m'])
        bc = row['boundary_condition']
        groups.setdefault((m, bc), []).append(row)

    # Helicity closed BC check
    closed_vals = {}
    for m in closed_orders:
        key = (m, 'closed')
        if key not in groups:
            return 0.0
        row = find_closest_T(groups[key], low_T_target)
        closed_vals[m] = float(row['helicity_modulus'])

    decreasing = True
    for i in range(len(closed_orders)-1):
        if closed_vals[closed_orders[i]] <= closed_vals[closed_orders[i+1]] * ratio_min:
            decreasing = False
            break
    score_closed = 1.0 if decreasing else 0.0

    # Open BC check
    key_open = (open_m, 'open')
    if key_open in groups:
        row = find_closest_T(groups[key_open], low_T_target)
        val_open = float(row['helicity_modulus'])
        score_open = 1.0 if val_open < helicity_open_max else 0.0
    else:
        score_open = 0.0

    # Heat capacity size independence
    cap_vals = []
    for m in closed_orders:
        key = (m, 'closed')
        if key not in groups:
            return 0.0
        row = find_closest_T(groups[key], heat_capacity_ref_T)
        cap_vals.append(float(row['heat_capacity']))
    if len(cap_vals) > 1:
        std_cap = statistics.stdev(cap_vals)
        score_cap = 1.0 if std_cap <= heat_capacity_std_max else 0.0
    else:
        score_cap = 0.0

    overall = 0.6 * score_closed + 0.2 * score_open + 0.2 * score_cap
    return overall


_SCORERS = {
    'trends_audit': score_0,
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
