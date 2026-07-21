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
    return {}


# === block: score_0 (check id='strain_series') ===
def score_0(artifact, step, ctx):
    strains = [0,1,2,3,4,5]
    reported = {}
    for row in artifact:
        try:
            s = float(row['strain_percent'])
            k = float(row['conductivity_W_mK'])
            reported[s] = k
        except (KeyError, ValueError):
            pass

    # check zero‑strain anchor against the paper‑reported value
    base_val = reported.get(0)
    if base_val is None:
        return 0.0
    ref_zero = 629.0
    tol_rel = 0.30   # generous tolerance to absorb toolchain spread
    zero_ok = 1.0 if abs(base_val - ref_zero) <= tol_rel * ref_zero else 0.0

    # monotonic decrease trend
    vals = [reported.get(s) for s in strains]
    trend_ok = False
    if all(v is not None for v in vals):
        trend_ok = True
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1]:
                trend_ok = False
                break
    trend_score = 1.0 if trend_ok else 0.0

    return 0.3 * zero_ok + 0.7 * trend_score


# === block: score_1 (check id='temperature_series') ===
def score_1(artifact, step, ctx):
    strains = [0,1,2,3,4,5]
    temps = [100,200,300,400,500,600]
    reported = {}
    for row in artifact:
        try:
            s = int(float(row['strain_percent']))
            t = int(float(row['temperature_K']))
            k = float(row['conductivity_W_mK'])
            reported[(s, t)] = k
        except (KeyError, ValueError):
            pass
    trend_strains_ok = 0
    for s in strains:
        vals = [reported.get((s, t)) for t in temps]
        if any(v is None for v in vals):
            continue
        ok_trend = True
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1]:
                ok_trend = False
                break
        if ok_trend:
            trend_strains_ok += 1
    return trend_strains_ok / len(strains)


# === block: score_2 (check id='width_series') ===
def score_2(artifact, step, ctx):
    strains = [0,1,2,3,4,5]
    widths = [1,2,3,4,5]
    reported = {}
    for row in artifact:
        try:
            s = int(float(row['strain_percent']))
            w = int(float(row['width_nm']))
            k = float(row['conductivity_W_mK'])
            reported[(s, w)] = k
        except (KeyError, ValueError):
            pass
    trend_strains_ok = 0
    total_strains_checked = 0
    for s in strains:
        vals = [reported.get((s, w)) for w in widths]
        if any(v is None for v in vals):
            continue
        total_strains_checked += 1
        ok_trend = True
        for i in range(1, len(vals)):
            if vals[i] < vals[i-1]:
                ok_trend = False
                break
        if ok_trend:
            trend_strains_ok += 1
    if total_strains_checked == 0:
        return 0.0
    return trend_strains_ok / total_strains_checked


_SCORERS = {
    'strain_series': score_0,
    'temperature_series': score_1,
    'width_series': score_2,
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
