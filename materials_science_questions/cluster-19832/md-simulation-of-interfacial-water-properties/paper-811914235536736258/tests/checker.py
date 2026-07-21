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
    import json, os
    with open(os.path.join(outputs_dir, "results.json")) as f:
        data = json.load(f)
    return {"data": data}


# === block: score_0 (check id='water_secondary_structure') ===
def score_0(artifact, step, ctx):
    import math
    data = ctx["data"]
    water = data.get("water")
    if not water:
        return 0.0
    ss = sorted(water.get("secondary_structure", []), key=lambda x: x.get("residue", 0))
    gold = step.get("gold_secondary_structure", [])
    thres_low = step["threshold_low"]
    tol_low = step["tolerance_low"]
    tol_high = step["tolerance_high"]
    props = ["beta_sheet", "turn", "bend", "coil"]
    N = min(len(gold), len(ss))
    if N == 0:
        return 0.0
    good = 0
    total = N * len(props)
    for i in range(N):
        g = gold[i]
        r = ss[i]
        for p in props:
            gp = g.get(p, 0.0)
            ap = r.get(p, 0.0)
            if isinstance(gp, (int, float)) and isinstance(ap, (int, float)):
                tol = tol_low if gp <= thres_low else tol_high
                if abs(ap - gp) <= tol:
                    good += 1
    return good / total if total else 0.0


# === block: score_1 (check id='interface_secondary_structure') ===
def score_1(artifact, step, ctx):
    import math
    data = ctx["data"]
    iface = data.get("interface")
    if not iface:
        return 0.0
    ss = sorted(iface.get("secondary_structure", []), key=lambda x: x.get("residue", 0))
    gold = step.get("gold_secondary_structure", [])
    thres_low = step["threshold_low"]
    tol_low = step["tolerance_low"]
    tol_high = step["tolerance_high"]
    props = ["beta_sheet", "turn", "bend", "coil"]
    N = min(len(gold), len(ss))
    if N == 0:
        return 0.0
    good = 0
    total = N * len(props)
    for i in range(N):
        g = gold[i]
        r = ss[i]
        for p in props:
            gp = g.get(p, 0.0)
            ap = r.get(p, 0.0)
            if isinstance(gp, (int, float)) and isinstance(ap, (int, float)):
                tol = tol_low if gp <= thres_low else tol_high
                if abs(ap - gp) <= tol:
                    good += 1
    return good / total if total else 0.0


# === block: score_2 (check id='water_largest_cluster') ===
def score_2(artifact, step, ctx):
    data = ctx["data"]
    water = data.get("water")
    if not water:
        return 0.0
    val = water.get("largest_cluster_percentage")
    if not isinstance(val, (int, float)):
        return 0.0
    gold = step["gold_value"]
    tol = step["tolerance"]
    return 1.0 if abs(val - gold) <= tol else 0.0


# === block: score_3 (check id='interface_largest_cluster') ===
def score_3(artifact, step, ctx):
    data = ctx["data"]
    iface = data.get("interface")
    if not iface:
        return 0.0
    val = iface.get("largest_cluster_percentage")
    if not isinstance(val, (int, float)):
        return 0.0
    gold = step["gold_value"]
    tol = step["tolerance"]
    return 1.0 if abs(val - gold) <= tol else 0.0


# === block: score_4 (check id='water_sum_check') ===
def score_4(artifact, step, ctx):
    data = ctx["data"]
    water = data.get("water")
    if not water:
        return 0.0
    ss = water.get("secondary_structure", [])
    if not ss:
        return 0.0
    tol = step["tolerance"]
    lower = 100.0 - tol
    upper = 100.0 + tol
    good = 0
    for r in ss:
        total = r.get("beta_sheet", 0) + r.get("turn", 0) + r.get("bend", 0) + r.get("coil", 0)
        if lower <= total <= upper:
            good += 1
    return good / len(ss)


# === block: score_5 (check id='interface_sum_check') ===
def score_5(artifact, step, ctx):
    data = ctx["data"]
    iface = data.get("interface")
    if not iface:
        return 0.0
    ss = iface.get("secondary_structure", [])
    if not ss:
        return 0.0
    tol = step["tolerance"]
    lower = 100.0 - tol
    upper = 100.0 + tol
    good = 0
    for r in ss:
        total = r.get("beta_sheet", 0) + r.get("turn", 0) + r.get("bend", 0) + r.get("coil", 0)
        if lower <= total <= upper:
            good += 1
    return good / len(ss)


_SCORERS = {
    'water_secondary_structure': score_0,
    'interface_secondary_structure': score_1,
    'water_largest_cluster': score_2,
    'interface_largest_cluster': score_3,
    'water_sum_check': score_4,
    'interface_sum_check': score_5,
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
