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
    ctx = {}
    for step in spec.get("steps", []):
        sid = step.get("id", "")
        if "gold_points" in step:
            ctx[sid + "_gold"] = step["gold_points"]
            ctx[sid + "_rel_tol"] = step.get("rel_tol", 1.0)
            ctx[sid + "_abs_floor"] = step.get("abs_floor", 1e-8)
    return ctx


# === block: score_0 (check id='step_04_kappa_NaCl') ===
def score_0(artifact, step, ctx):
    gold_points = ctx.get(step.get("id") + "_gold", [])
    rel_tol = ctx.get(step.get("id") + "_rel_tol", 1.0)
    abs_floor = ctx.get(step.get("id") + "_abs_floor", 1e-8)
    if not gold_points:
        return 0.0

    agent_lookup = {}
    for row in (artifact or []):
        try:
            b = float(row.get("magnetic_field_T", 0))
            t = float(row.get("temperature_K", 0))
            k = float(row.get("kappa_xy_W_mK", 0))
            agent_lookup[(b, t)] = k
        except (ValueError, TypeError, KeyError):
            continue

    scores = []
    for gp in gold_points:
        b_g, t_g, k_g = gp[0], gp[1], gp[2]
        best_key = None
        best_dist = float('inf')
        for (b_a, t_a) in agent_lookup:
            dist = abs(b_a - b_g) + abs(t_a - t_g)
            if dist < best_dist:
                best_dist = dist
                best_key = (b_a, t_a)
        if best_key is None or best_dist > 1.0:
            scores.append(0.0)
            continue
        k_agent = agent_lookup[best_key]
        gold_abs = max(abs(k_g), abs_floor)
        if gold_abs < abs_floor * 10:
            point_score = 1.0 if abs(k_agent) < abs_floor * 10 else 0.0
        else:
            rel_err = abs(k_agent - k_g) / gold_abs
            point_score = max(0.0, 1.0 - rel_err / rel_tol)
            if k_agent * k_g < 0:
                point_score = 0.0
        scores.append(point_score)
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_05_kappa_BTO') ===
def score_1(artifact, step, ctx):
    gold_points = ctx.get(step.get("id") + "_gold", [])
    rel_tol = ctx.get(step.get("id") + "_rel_tol", 1.0)
    abs_floor = ctx.get(step.get("id") + "_abs_floor", 1e-8)
    if not gold_points:
        return 0.0

    agent_lookup = {}
    for row in (artifact or []):
        try:
            b = float(row.get("magnetic_field_T", 0))
            t = float(row.get("temperature_K", 0))
            k = float(row.get("kappa_xy_W_mK", 0))
            agent_lookup[(b, t)] = k
        except (ValueError, TypeError, KeyError):
            continue

    scores = []
    for gp in gold_points:
        b_g, t_g, k_g = gp[0], gp[1], gp[2]
        best_key = None
        best_dist = float('inf')
        for (b_a, t_a) in agent_lookup:
            dist = abs(b_a - b_g) + abs(t_a - t_g)
            if dist < best_dist:
                best_dist = dist
                best_key = (b_a, t_a)
        if best_key is None or best_dist > 1.0:
            scores.append(0.0)
            continue
        k_agent = agent_lookup[best_key]
        gold_abs = max(abs(k_g), abs_floor)
        if gold_abs < abs_floor * 10:
            point_score = 1.0 if abs(k_agent) < abs_floor * 10 else 0.0
        else:
            rel_err = abs(k_agent - k_g) / gold_abs
            point_score = max(0.0, 1.0 - rel_err / rel_tol)
            if k_agent * k_g < 0:
                point_score = 0.0
        scores.append(point_score)
    return sum(scores) / len(scores)


_SCORERS = {
    'step_04_kappa_NaCl': score_0,
    'step_05_kappa_BTO': score_1,
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
