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


# === block: score_0 (check id='step_2') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0

    # monotonicity
    pairs = len(artifact) - 1
    mono_count = 0.0
    for i in range(pairs):
        try:
            t_cur = float(artifact[i]['temperature_K'])
            t_next = float(artifact[i+1]['temperature_K'])
            if t_next <= t_cur + 1e-6:
                mono_count += 1.0
        except:
            pass
    mono_score = mono_count / pairs if pairs else 0.0

    # endpoint checks (tight tolerances because boundary conditions are fixed)
    try:
        first_temp = float(artifact[0]['temperature_K'])
        last_temp = float(artifact[-1]['temperature_K'])
        first_ok = 1.0 if abs(first_temp - 300.0) <= 1.0 else 0.0
        last_ok = 1.0 if abs(last_temp - 78.0) <= 1.0 else 0.0
    except:
        first_ok = 0.0
        last_ok = 0.0

    def _temp_at(rows, x_target):
        xs, ts = [], []
        for r in rows:
            try:
                xs.append(float(r['length_m']))
                ts.append(float(r['temperature_K']))
            except:
                continue
        if not xs:
            return None
        order = sorted(range(len(xs)), key=lambda i: xs[i])
        xs_sorted = [xs[i] for i in order]
        ts_sorted = [ts[i] for i in order]
        if x_target <= xs_sorted[0]:
            return ts_sorted[0]
        if x_target >= xs_sorted[-1]:
            return ts_sorted[-1]
        for i in range(len(xs_sorted)-1):
            if xs_sorted[i] <= x_target <= xs_sorted[i+1]:
                x0, x1 = xs_sorted[i], xs_sorted[i+1]
                t0, t1 = ts_sorted[i], ts_sorted[i+1]
                if x1 - x0 == 0:
                    return t0
                return t0 + (t1 - t0) * (x_target - x0) / (x1 - x0)
        return None

    # check temperature at Peltier junction (x ≈ 0.007 m) – upper bound 250 K
    check1_score = 0.0
    t1 = _temp_at(artifact, 0.007)
    if t1 is not None:
        if t1 <= 250.0:
            check1_score = 1.0
        else:
            check1_score = max(0.0, 1.0 - (t1 - 250.0) / 50.0)

    # check temperature at mid CuI (x ≈ 0.20 m) – upper bound 210 K
    check2_score = 0.0
    t2 = _temp_at(artifact, 0.20)
    if t2 is not None:
        if t2 <= 210.0:
            check2_score = 1.0
        else:
            check2_score = max(0.0, 1.0 - (t2 - 210.0) / 50.0)

    # check temperature at CuI-CuII junction (x ≈ 0.587 m) – upper bound 140 K
    check3_score = 0.0
    t3 = _temp_at(artifact, 0.587)
    if t3 is not None:
        if t3 <= 140.0:
            check3_score = 1.0
        else:
            check3_score = max(0.0, 1.0 - (t3 - 140.0) / 50.0)

    # check temperature at mid CuII (x ≈ 0.80 m) – upper bound 105 K
    check4_score = 0.0
    t4 = _temp_at(artifact, 0.80)
    if t4 is not None:
        if t4 <= 105.0:
            check4_score = 1.0
        else:
            check4_score = max(0.0, 1.0 - (t4 - 105.0) / 50.0)

    score = (0.15 * mono_score +
             0.05 * first_ok +
             0.05 * last_ok +
             0.20 * check1_score +
             0.20 * check2_score +
             0.20 * check3_score +
             0.15 * check4_score)
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step_3') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    val = artifact.get(step.get('field', 'cold_end_heat_load_W'))
    if val is None:
        return 0.0
    try:
        val = float(val)
    except:
        return 0.0
    threshold = float(step.get('threshold', 215))
    if val <= threshold:
        return 1.0
    decay = float(step.get('decay_range', 50))
    score = max(0.0, 1.0 - (val - threshold) / decay)
    return score


# === block: score_2 (check id='step_4') ===
def score_2(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    val = artifact.get(step.get('field', 'cold_end_heat_load_W'))
    if val is None:
        return 0.0
    try:
        val = float(val)
    except:
        return 0.0
    threshold = float(step.get('threshold', 150))
    if val <= threshold:
        return 1.0
    decay = float(step.get('decay_range', 50))
    score = max(0.0, 1.0 - (val - threshold) / decay)
    return score


_SCORERS = {
    'step_2': score_0,
    'step_3': score_1,
    'step_4': score_2,
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
