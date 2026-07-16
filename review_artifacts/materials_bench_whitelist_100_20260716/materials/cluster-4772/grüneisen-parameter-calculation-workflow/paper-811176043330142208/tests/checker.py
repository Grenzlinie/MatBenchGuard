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


# === block: score_0 (check id='lattice_param_check') ===
def score_0(artifact, step, ctx):
    target = step.get("target_values", {})
    tol = step.get("tolerance_relative", 0.01)
    agent_dict = {}
    for row in artifact:
        try:
            T = int(float(row["temperature_K"]))
            a = float(row["lattice_parameter_A"])
            agent_dict[str(T)] = a
        except:
            pass
    max_rel_err = 0.0
    count = 0
    for T, a_gold in target.items():
        if T in agent_dict:
            a_agent = agent_dict[T]
            rel_err = abs(a_agent - float(a_gold)) / float(a_gold)
            if rel_err > max_rel_err:
                max_rel_err = rel_err
            count += 1
    if count == 0:
        return 0.0
    if max_rel_err <= tol:
        return 1.0
    excess = max_rel_err - tol
    score_val = max(0.0, 1.0 - excess / 0.04)
    return score_val


# === block: score_1 (check id='thermal_cond_check') ===
def score_1(artifact, step, ctx):
    data = []
    for row in artifact:
        try:
            T = int(float(row["temperature_K"]))
            k = float(row["thermal_conductivity_W_mK"])
            data.append((T, k))
        except:
            pass
    if not data:
        return 0.0
    data.sort(key=lambda x: x[0])
    pos = all(k > 0 for _, k in data)
    dec = all(data[i][1] >= data[i+1][1] for i in range(len(data)-1))
    logT = [math.log(T) for T, _ in data]
    logK = [math.log(k) for _, k in data]
    n = len(logT)
    sum_x = sum(logT)
    sum_y = sum(logK)
    sum_xy = sum(x*y for x, y in zip(logT, logK))
    sum_xx = sum(x*x for x in logT)
    try:
        slope = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)
    except ZeroDivisionError:
        slope = 0
    alpha = -slope
    exp_ok = 0.5 <= alpha <= 0.7
    ref = step.get("reference_values", {})
    mag_ok = 0
    total = 0
    for row in artifact:
        T_str = str(int(float(row.get("temperature_K", 0))))
        if T_str in ref:
            try:
                k_agent = float(row.get("thermal_conductivity_W_mK", 0))
                k_gold = float(ref[T_str])
                ratio = k_agent / k_gold
                if 0.5 <= ratio <= 2.0:
                    mag_ok += 1
                total += 1
            except:
                pass
    mag_score = mag_ok / total if total > 0 else 0.0
    trend_score = 0.0
    if pos:
        trend_score += 0.1
    if dec:
        trend_score += 0.1
    exp_score = 1.0 if exp_ok else 0.0
    score_val = trend_score + 0.3*exp_score + 0.5*mag_score
    return max(0.0, min(1.0, score_val))


# === block: score_2 (check id='gruneisen_check') ===
def score_2(artifact, step, ctx):
    data = {}
    for row in artifact:
        try:
            T = int(float(row["temperature_K"]))
            g = float(row["weighted_gruneisen_parameter"])
            data[T] = g
        except:
            pass
    low_neg = data.get(0) is not None and data[0] < 0
    high_nonneg = data.get(1500) is not None and data[1500] >= 0
    crossing = False
    if 600 in data and 1200 in data:
        if data[600] <= 0 and data[1200] >= 0:
            crossing = True
    elif 900 in data and 1200 in data:
        if data[900] <= 0 and data[1200] >= 0:
            crossing = True
    score_val = (0.3 if low_neg else 0.0) + (0.3 if high_nonneg else 0.0) + (0.4 if crossing else 0.0)
    return score_val


_SCORERS = {
    'lattice_param_check': score_0,
    'thermal_cond_check': score_1,
    'gruneisen_check': score_2,
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
