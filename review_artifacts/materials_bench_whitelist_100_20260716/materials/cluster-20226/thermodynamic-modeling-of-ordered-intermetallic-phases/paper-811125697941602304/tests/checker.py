import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os


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


# === block: score_0 (check id='step_1_vacancy_vs_r') ===
def score_0(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list):
        return 0.0
    if not artifact:
        return 0.0
    ok = 0
    tol = 0.02
    for row in artifact:
        try:
            r = float(row.get('r', ''))
            y = float(row.get('y_square_alpha', ''))
            if r < 1.0:
                ref = 0.0
            else:
                ref = 1.0 - 1.0 / r
                if ref < 0:
                    ref = 0.0
            if abs(y - ref) <= tol:
                ok += 1
        except:
            pass
    total = len(artifact)
    if total == 0:
        return 0.0
    return ok / total


# === block: score_1 (check id='step_2_pressure_vs_vacancy') ===
def score_1(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    score = 0.0
    # check sufficient points
    if len(artifact) >= 15:
        score += 0.1
    else:
        score += 0.0
    # monotonicity: p should increase with y
    try:
        prev_y = -1.0
        monotonic = True
        for row in artifact:
            y = float(row.get('y_square_alpha', ''))
            p = float(row.get('p_H2_GPa', ''))
            if y < prev_y:
                monotonic = False
                break
            prev_y = y
        if monotonic:
            score += 0.3
    except:
        pass
    # landmark at y ~ 0.17
    try:
        landmark_ok = False
        for row in artifact:
            y = float(row.get('y_square_alpha', ''))
            p = float(row.get('p_H2_GPa', ''))
            if 0.16 <= y <= 0.18:
                if 5.0 <= p <= 15.0:
                    landmark_ok = True
                    break
        if landmark_ok:
            score += 0.4
    except:
        pass
    # coverage: y range should span at least 0.01 to 0.17
    try:
        ys = [float(r.get('y_square_alpha','')) for r in artifact]
        min_y = min(ys) if ys else 0
        max_y = max(ys) if ys else 0
        if min_y <= 0.02 and max_y >= 0.16:
            score += 0.2
    except:
        pass
    return min(score, 1.0)


# === block: score_2 (check id='step_3_order_vs_temperature') ===
def score_2(artifact, step, ctx):
    if artifact is None or not isinstance(artifact, list) or len(artifact) < 5:
        return 0.0
    score = 0.0
    # monotonic decrease of order with T? but may be noisy; relax
    try:
        temps = [float(r.get('temperature_K','')) for r in artifact]
        orders = [float(r.get('long_range_order_parameter','')) for r in artifact]
        # check low-T order >= 0.8
        low_T_rows = [o for t,o in zip(temps,orders) if t <= 600]
        if low_T_rows:
            if all(o >= 0.8 for o in low_T_rows):
                score += 0.2
        else:
            # if no points below 600, check min T
            min_idx = temps.index(min(temps))
            if orders[min_idx] >= 0.8:
                score += 0.2
        # check high-T order <= 0.2
        high_T_rows = [o for t,o in zip(temps,orders) if t >= 1000]
        if high_T_rows:
            if all(o <= 0.2 for o in high_T_rows):
                score += 0.2
        else:
            max_idx = temps.index(max(temps))
            if orders[max_idx] <= 0.2:
                score += 0.2
        # check ordering temperature: find temp where order crosses 0.5
        # approximate by interpolation
        pairs = sorted(zip(temps, orders), key=lambda x: x[0])
        t_half = None
        for i in range(len(pairs)-1):
            t1, o1 = pairs[i]
            t2, o2 = pairs[i+1]
            if (o1 - 0.5) * (o2 - 0.5) <= 0:
                # linear interpolation
                if o2 != o1:
                    t_half = t1 + (0.5 - o1) * (t2 - t1) / (o2 - o1)
                else:
                    t_half = (t1+t2)/2
                break
        if t_half is not None:
            if 850 <= t_half <= 950:
                score += 0.3
            elif 800 <= t_half <= 1000:
                score += 0.2
            else:
                score += 0.0
        # overall monotonic trend: order should generally decrease
        # compute correlation
        if len(temps) > 1:
            inv_t = [1/t for t in temps]
            # simple test: check if order at lowest T >= order at highest T
            if orders[temps.index(min(temps))] >= orders[temps.index(max(temps))] * 0.95:
                score += 0.2
            else:
                score += 0.1
    except:
        pass
    return min(score, 1.0)


_SCORERS = {
    'step_1_vacancy_vs_r': score_0,
    'step_2_pressure_vs_vacancy': score_1,
    'step_3_order_vs_temperature': score_2,
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
