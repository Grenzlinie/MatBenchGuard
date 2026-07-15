import os
import json
import csv

# === author imports / helpers ===
import os, math, statistics


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


# === block: score_0 (check id='step_01_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    min_rows = step["require_min_rows"]
    if len(rows) < min_rows:
        return 0.0
    time_col = step["time_column"]
    value_col = step["value_column"]
    dd0_col = "d_d0"
    data = []
    for r in rows:
        try:
            t = float(r[time_col])
            v = float(r[value_col])
            d = float(r[dd0_col]) if dd0_col in r else None
            data.append((t, v, d))
        except (ValueError, KeyError):
            continue
    if not data:
        return 0.0
    t_start = step["time_start"]; t_end = step["time_end"]
    masked = [(t, v) for t, v, _ in data if t_start <= t <= t_end]
    if not masked:
        return 0.0
    recomputed_mean = statistics.mean(v for _, v in masked)
    ref = step["reference_value"]
    tol = step["tolerance"]
    max_dev = step.get("max_allowed_dev", tol*3)
    diff = abs(recomputed_mean - ref)
    if diff <= tol:
        energy_score = 1.0
    else:
        energy_score = max(0.0, 1.0 - (diff - tol) / (max_dev - tol))

    trend_time_start = step.get("trend_time_start", 20.0)
    trend_time_end = step.get("trend_time_end", 27.5)
    threshold_dd0 = step.get("trend_threshold", 0.6)
    required_fraction = step.get("trend_required_fraction", 0.8)
    trend_data = [(d) for t, _, d in data if trend_time_start <= t <= trend_time_end and d is not None]
    if not trend_data:
        trend_score = 0.0
    else:
        fraction_below = sum(1 for d in trend_data if d < threshold_dd0) / len(trend_data)
        trend_score = min(1.0, fraction_below / required_fraction)
    return 0.8 * energy_score + 0.2 * trend_score


# === block: score_1 (check id='step_02_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold_means = step["gold_means"]
    tol = step["tolerance"]
    max_dev = step.get("max_allowed_dev", tol*3)

    # Convert gold_means string keys to int for comparison with agent's integer cnt_index
    gold_means = {int(k): v for k, v in gold_means.items()}

    reported = {}
    for r in rows:
        idx = int(r["cnt_index"])
        mean_val = float(r["mean_Evdw_int_kcal_mol"])
        reported[idx] = mean_val

    expected_idxs = set(gold_means.keys())
    if set(reported.keys()) != expected_idxs:
        return 0.0

    scores = []
    for idx in sorted(expected_idxs):
        rep = reported[idx]
        gold = gold_means[idx]
        diff = abs(rep - gold)
        if diff <= tol:
            si = 1.0
        else:
            si = max(0.0, 1.0 - (diff - tol) / (max_dev - tol))
        scores.append(si)
    mean_comp_score = sum(scores)/len(scores)

    cross_file = step.get("cross_check_file")
    if cross_file:
        step01_artifact = load_artifact(os.path.join("/app/outputs", cross_file))
        if step01_artifact is None:
            cross_score = 0.0
        else:
            time_col = "time_ns"
            val_col = "Evdw_int_kcal_mol"
            t_start = 15.0
            t_end = 27.5
            vals = []
            for r in step01_artifact:
                try:
                    t = float(r[time_col])
                    v = float(r[val_col])
                    if t_start <= t <= t_end:
                        vals.append(v)
                except:
                    continue
            if not vals:
                cross_score = 0.0
            else:
                recomputed_mean = statistics.mean(vals)
                rep17 = reported.get(17)
                if rep17 is None:
                    cross_score = 0.0
                else:
                    diff = abs(recomputed_mean - rep17)
                    cross_tol = step.get("cross_check_tolerance", tol)
                    if diff <= cross_tol:
                        cross_score = 1.0
                    else:
                        cross_score = max(0.0, 1.0 - (diff - cross_tol)/((max_dev or cross_tol*3) - cross_tol))
        weight_cross = 0.2
        return (1 - weight_cross) * mean_comp_score + weight_cross * cross_score
    else:
        return mean_comp_score


# === block: score_2 (check id='step_03_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    gold_means = step["gold_means"]
    tol = step["tolerance"]
    max_dev = step.get("max_allowed_dev", tol*3)

    # Convert gold_means keys to integers for comparison with agent's integer cnt_index
    gold_means = {int(k): v for k, v in gold_means.items()}

    reported = {}
    for r in rows:
        idx = int(r["cnt_index"])
        mean_val = float(r["mean_Rg_A"])
        reported[idx] = mean_val

    expected_idxs = set(gold_means.keys())
    if set(reported.keys()) != expected_idxs:
        return 0.0

    scores = []
    for idx in sorted(expected_idxs):
        rep = reported[idx]
        gold = gold_means[idx]
        diff = abs(rep - gold)
        if diff <= tol:
            si = 1.0
        else:
            si = max(0.0, 1.0 - (diff - tol) / (max_dev - tol))
        scores.append(si)
    return sum(scores)/len(scores)


_SCORERS = {
    'step_01_check': score_0,
    'step_02_check': score_1,
    'step_03_check': score_2,
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
