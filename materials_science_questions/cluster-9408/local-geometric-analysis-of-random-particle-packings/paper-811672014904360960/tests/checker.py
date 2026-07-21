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


# === block: score_0 (check id='shape_factor_fraction_monotonic') ===
def score_0(artifact, step, ctx):
    taps_order = [2,8,15,30,50,70]
    fractions = []
    for t in taps_order:
        key = str(t)
        if key not in artifact:
            return 0.0
        vals = artifact[key]
        if not isinstance(vals, list):
            return 0.0
        n = len(vals)
        if n == 0:
            return 0.0
        count = sum(1 for v in vals if v < 1.108)
        fractions.append(count / n)
    non_decreasing = all(fractions[i] >= fractions[i-1] for i in range(1, len(fractions)))
    strict_increase = fractions[-1] > fractions[0]
    return 1.0 if (non_decreasing and strict_increase) else 0.0


# === block: score_1 (check id='shape_factor_mean_monotonic') ===
def score_1(artifact, step, ctx):
    taps_order = [2,8,15,30,50,70]
    means = []
    for t in taps_order:
        key = str(t)
        if key not in artifact:
            return 0.0
        vals = artifact[key]
        if not isinstance(vals, list) or len(vals) == 0:
            return 0.0
        mean_val = sum(vals) / len(vals)
        means.append(mean_val)
    monotonic_decrease = all(means[i] <= means[i-1] for i in range(1, len(means)))
    strict_decrease = means[-1] < means[0]
    return 1.0 if (monotonic_decrease and strict_decrease) else 0.0


# === block: score_2 (check id='memory_effect_scenario0_anomaly') ===
def score_2(artifact, step, ctx):
    rows0 = [row for row in artifact if int(row.get('scenario','')) == 0]
    dm = {}
    for row in rows0:
        try:
            t = int(row['tap'])
            d = float(row['density'])
        except (KeyError, ValueError):
            return 0.0
        dm[t] = d
    if 30 not in dm or 31 not in dm or 32 not in dm:
        return 0.0
    d30 = dm[30]
    d31 = dm[31]
    d32 = dm[32]
    return 1.0 if (d31 < d30 and d32 > d31) else 0.0


# === block: score_3 (check id='memory_effect_scenario1_anomaly') ===
def score_3(artifact, step, ctx):
    rows1 = [row for row in artifact if int(row.get('scenario','')) == 1]
    dm = {}
    for row in rows1:
        try:
            t = int(row['tap'])
            d = float(row['density'])
        except (KeyError, ValueError):
            return 0.0
        dm[t] = d
    if 30 not in dm or 31 not in dm or 32 not in dm:
        return 0.0
    d30 = dm[30]
    d31 = dm[31]
    d32 = dm[32]
    return 1.0 if (d31 > d30 and d32 < d31) else 0.0


_SCORERS = {
    'shape_factor_fraction_monotonic': score_0,
    'shape_factor_mean_monotonic': score_1,
    'memory_effect_scenario0_anomaly': score_2,
    'memory_effect_scenario1_anomaly': score_3,
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
