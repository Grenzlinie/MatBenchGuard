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


# === block: score_0 (check id='lifetime_curve') ===
def score_0(artifact, step, ctx):
    import math

    # artifact is list of dicts with temperature_K, pressure_MPa, lifetime_s
    # step is the grading step dict; ctx is {} (unused)

    def groupby_temp(rows):
        d = {}
        for r in rows:
            t = float(r["temperature_K"])
            p = float(r["pressure_MPa"])
            l = float(r["lifetime_s"])
            d.setdefault(t, []).append((p, l))
        for t in d:
            d[t].sort(key=lambda x: x[0])
        return d

    data = groupby_temp(artifact)
    all_temps = [500.0, 1000.0, 1500.0, 2000.0, 2500.0]
    present_temps = []
    completeness = 0.0
    for T in all_temps:
        if T in data and len(data[T]) >= 2:
            completeness += 1.0
            present_temps.append(T)
    completeness /= len(all_temps)

    min_scores = []
    plateau_scores = []
    for T in present_temps:
        row = data[T]
        lifetimes = [l for (p, l) in row]
        min_val = min(lifetimes)
        min_idx = lifetimes.index(min_val)
        if min_idx == 0 or min_idx == len(lifetimes) - 1:
            min_ok = 0.0
        else:
            left_ok = all(l > min_val + 0.001 for l in lifetimes[:min_idx])
            right_ok = all(l >= min_val - 0.001 for l in lifetimes[min_idx+1:])
            min_ok = 1.0 if left_ok and right_ok else 0.0
        min_scores.append(min_ok)

        high_p = [(p, l) for (p, l) in row if p >= 10.0]
        if len(high_p) < 2:
            plateau_scores.append(0.0)
        else:
            vals = [l for (p, l) in high_p]
            mean = sum(vals) / len(vals)
            if mean == 0:
                plateau_scores.append(0.0)
            else:
                std = math.sqrt(sum((v - mean) ** 2 for v in vals) / len(vals))
                rsd = std / mean
                if rsd <= 0.15:
                    plateau_scores.append(1.0)
                elif rsd >= 0.25:
                    plateau_scores.append(0.0)
                else:
                    plateau_scores.append(1.0 - (rsd - 0.15) / 0.1)

    min_score = sum(min_scores) / len(min_scores) if min_scores else 0.0
    plateau_score = sum(plateau_scores) / len(plateau_scores) if plateau_scores else 0.0

    scaling_score = 0.0
    if present_temps:
        means = []
        for T in present_temps:
            high_p = [(p, l) for (p, l) in data[T] if p >= 10.0]
            vals = [l for (p, l) in high_p]
            means.append((T, sum(vals) / len(vals)) if vals else (T, None))
        valid = [(T, m) for T, m in means if m is not None]
        if len(valid) >= 2:
            logTs = [math.log(T) for T, _ in valid]
            logts = [math.log(m) for _, m in valid]
            n = len(logTs)
            sum_x = sum(logTs)
            sum_y = sum(logts)
            sum_xy = sum(x * y for x, y in zip(logTs, logts))
            sum_xx = sum(x * x for x in logTs)
            denom = n * sum_xx - sum_x * sum_x
            if denom > 0:
                b = (n * sum_xy - sum_x * sum_y) / denom
                if -0.9 <= b <= -0.6:
                    scaling_score = 1.0
                elif b < -0.9:
                    scaling_score = max(0.0, 1.0 - (abs(b) - 0.9) / 0.2)
                else:
                    scaling_score = max(0.0, 1.0 - (b + 0.6) / 0.2)

    score = 0.1 * completeness + 0.3 * min_score + 0.3 * plateau_score + 0.3 * scaling_score
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='critical_boundary') ===
def score_1(artifact, step, ctx):
    import math

    # artifact is list of dicts with temperature_K, pressure_MPa
    temp_points = [(float(r["temperature_K"]), float(r["pressure_MPa"])) for r in artifact]
    if not temp_points:
        return 0.0
    temp_points.sort(key=lambda x: x[0])
    monotonic = True
    for i in range(len(temp_points) - 1):
        if temp_points[i][1] <= temp_points[i + 1][1]:
            monotonic = False
            break
    range_ok = all(3.0 <= p <= 20.0 for _, p in temp_points)
    score = 0.6 * (1.0 if monotonic else 0.0) + 0.4 * (1.0 if range_ok else 0.0)
    return score


_SCORERS = {
    'lifetime_curve': score_0,
    'critical_boundary': score_1,
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
