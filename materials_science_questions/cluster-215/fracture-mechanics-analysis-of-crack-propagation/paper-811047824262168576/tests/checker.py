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
    import os, csv
    velocities = {}
    vel_file = os.path.join(outputs_dir, "steady_state_velocities.csv")
    try:
        with open(vel_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ov = row.get("overload", "").strip()
                tv = row.get("terminal_velocity", "").strip()
                if ov and tv:
                    try:
                        velocities[float(ov)] = float(tv)
                    except:
                        pass
    except:
        pass
    return {"steady_velocities": velocities}


# === block: score_0 (check id='step04a') ===
def score_0(artifact, step, ctx):
    gold = step.get("gold", {})
    tol = step.get("tolerance", 0.05)
    rows_by_overload = {}
    for r in artifact:
        ov = r.get("overload", "").strip()
        if ov:
            rows_by_overload[ov] = r
    score_sum = 0.0
    count = 0
    for ov_key, gv in gold.items():
        count += 1
        row = rows_by_overload.get(str(ov_key))
        if row is None:
            continue
        try:
            val = float(row["terminal_velocity"])
        except:
            continue
        diff = abs(val - gv)
        if diff <= tol:
            score_sum += 1.0
        else:
            s = max(0.0, 1.0 - (diff - tol) / tol)
            score_sum += s
    if count == 0:
        return 0.0
    return score_sum / count


# === block: score_1 (check id='step04b') ===
def score_1(artifact, step, ctx):
    gold = step.get("gold", {})
    rows_by_overload = {}
    for r in artifact:
        ov = r.get("overload", "").strip()
        state = r.get("state", "").strip().lower()
        if ov:
            rows_by_overload[ov] = state
    match_count = 0
    for ov_key, expected in gold.items():
        actual = rows_by_overload.get(str(ov_key))
        if actual == expected.lower():
            match_count += 1
    if len(gold) == 0:
        return 0.0
    return 1.0 if match_count == len(gold) else 0.0


# === block: score_2 (check id='step04c') ===
def score_2(artifact, step, ctx):
    overload = step.get("overload")
    term_vel = None
    if ctx and "steady_velocities" in ctx:
        term_vel = ctx["steady_velocities"].get(overload)
    times = []
    v_tips = []
    for r in artifact:
        try:
            t = float(r["time"])
            v = float(r["v_tip"])
            times.append(t)
            v_tips.append(v)
        except:
            continue
    if len(times) < 10:
        return 0.0
    split_idx = max(1, int(len(times) * 0.2))
    early_avg = sum(v_tips[:split_idx]) / split_idx
    late_idx = max(split_idx, int(len(times) * 0.8))
    late_avg = sum(v_tips[late_idx:]) / max(1, len(times) - late_idx)
    increasing = late_avg > early_avg + 0.02
    plateau_len = max(10, int(len(times) * 0.2))
    plateau_avg = sum(v_tips[-plateau_len:]) / plateau_len
    plateau_ok = False
    if term_vel is not None:
        plateau_ok = abs(plateau_avg - term_vel) <= 0.06
    score_shape = 0.5 if increasing else 0.0
    score_plateau = 0.5 if plateau_ok else 0.0
    if term_vel is None:
        return 1.0 if increasing else 0.0
    return score_shape + score_plateau


# === block: score_3 (check id='step04d') ===
def score_3(artifact, step, ctx):
    overload = step.get("overload")
    term_vel = None
    if ctx and "steady_velocities" in ctx:
        term_vel = ctx["steady_velocities"].get(overload)
    times = []
    v_tips = []
    for r in artifact:
        try:
            t = float(r["time"])
            v = float(r["v_tip"])
            times.append(t)
            v_tips.append(v)
        except:
            continue
    if len(times) < 10:
        return 0.0
    split_idx = max(1, int(len(times) * 0.2))
    early_avg = sum(v_tips[:split_idx]) / split_idx
    late_idx = max(split_idx, int(len(times) * 0.8))
    late_avg = sum(v_tips[late_idx:]) / max(1, len(times) - late_idx)
    increasing = late_avg > early_avg + 0.02
    plateau_len = max(10, int(len(times) * 0.2))
    plateau_avg = sum(v_tips[-plateau_len:]) / plateau_len
    plateau_ok = False
    if term_vel is not None:
        plateau_ok = abs(plateau_avg - term_vel) <= 0.06
    score_shape = 0.5 if increasing else 0.0
    score_plateau = 0.5 if plateau_ok else 0.0
    if term_vel is None:
        return 1.0 if increasing else 0.0
    return score_shape + score_plateau


_SCORERS = {
    'step04a': score_0,
    'step04b': score_1,
    'step04c': score_2,
    'step04d': score_3,
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
