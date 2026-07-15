import os
import json
import csv

# === author imports / helpers ===
import math


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


# === block: score_0 (check id='transition_temperature') ===
def score_0(artifact, step, ctx):
    rows = sorted(artifact, key=lambda r: float(r['temperature_normalized']))
    target = float(step['target_tc'])
    tol = float(step['tol_abs'])
    tc = None
    for r in rows:
        lro = float(r['LRO'])
        T = float(r['temperature_normalized'])
        if lro < 0.01:
            tc = T
            break
    if tc is None:
        return 0.0
    diff = abs(tc - target)
    if diff <= tol:
        return 1.0
    extra = diff - tol
    score = max(0.0, 1.0 - extra / (2*tol))
    return score


# === block: score_1 (check id='lro_at_t0.1') ===
def score_1(artifact, step, ctx):
    check_temp = float(step['check_temp'])
    min_lro = float(step['min_lro'])
    rows = artifact
    temps = [float(r['temperature_normalized']) for r in rows]
    lros = [float(r['LRO']) for r in rows]
    pairs = sorted(zip(temps, lros))
    temps_sorted, lros_sorted = zip(*pairs) if pairs else ([], [])
    if len(temps_sorted) == 0:
        return 0.0
    lro_est = None
    if check_temp <= temps_sorted[0]:
        lro_est = lros_sorted[0]
    elif check_temp >= temps_sorted[-1]:
        lro_est = lros_sorted[-1]
    else:
        for i in range(len(temps_sorted)-1):
            if temps_sorted[i] <= check_temp <= temps_sorted[i+1]:
                w = (check_temp - temps_sorted[i]) / (temps_sorted[i+1] - temps_sorted[i])
                lro_est = lros_sorted[i] + w * (lros_sorted[i+1] - lros_sorted[i])
                break
    if lro_est is None:
        return 0.0
    if lro_est >= min_lro:
        return 1.0
    score = max(0.0, (lro_est - 0.9) / (min_lro - 0.9))
    return score


# === block: score_2 (check id='lro_at_t2.0') ===
def score_2(artifact, step, ctx):
    check_temp = float(step['check_temp'])
    lro_min = float(step['lro_min'])
    lro_max = float(step['lro_max'])
    rows = artifact
    temps = [float(r['temperature_normalized']) for r in rows]
    lros = [float(r['LRO']) for r in rows]
    pairs = sorted(zip(temps, lros))
    temps_sorted, lros_sorted = zip(*pairs) if pairs else ([], [])
    if len(temps_sorted) == 0:
        return 0.0
    lro_est = None
    if check_temp <= temps_sorted[0]:
        lro_est = lros_sorted[0]
    elif check_temp >= temps_sorted[-1]:
        lro_est = lros_sorted[-1]
    else:
        for i in range(len(temps_sorted)-1):
            if temps_sorted[i] <= check_temp <= temps_sorted[i+1]:
                w = (check_temp - temps_sorted[i]) / (temps_sorted[i+1] - temps_sorted[i])
                lro_est = lros_sorted[i] + w * (lros_sorted[i+1] - lros_sorted[i])
                break
    if lro_est is None:
        return 0.0
    if lro_min <= lro_est <= lro_max:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='lro_at_t2.5') ===
def score_3(artifact, step, ctx):
    check_temp = float(step['check_temp'])
    max_lro = float(step['max_lro'])
    rows = artifact
    temps = [float(r['temperature_normalized']) for r in rows]
    lros = [float(r['LRO']) for r in rows]
    pairs = sorted(zip(temps, lros))
    temps_sorted, lros_sorted = zip(*pairs) if pairs else ([], [])
    if len(temps_sorted) == 0:
        return 0.0
    lro_est = None
    if check_temp <= temps_sorted[0]:
        lro_est = lros_sorted[0]
    elif check_temp >= temps_sorted[-1]:
        lro_est = lros_sorted[-1]
    else:
        for i in range(len(temps_sorted)-1):
            if temps_sorted[i] <= check_temp <= temps_sorted[i+1]:
                w = (check_temp - temps_sorted[i]) / (temps_sorted[i+1] - temps_sorted[i])
                lro_est = lros_sorted[i] + w * (lros_sorted[i+1] - lros_sorted[i])
                break
    if lro_est is None:
        return 0.0
    if lro_est <= max_lro:
        return 1.0
    score = max(0.0, 1.0 - (lro_est - max_lro) / 0.05)
    return score


_SCORERS = {
    'transition_temperature': score_0,
    'lro_at_t0.1': score_1,
    'lro_at_t2.0': score_2,
    'lro_at_t2.5': score_3,
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
