import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    gold_list = step.get("gold", [])
    if not gold_list or not artifact:
        return 0.0
    tol = step.get("tolerance", 0.1)
    tight_tol = step.get("tight_tolerance", 0.01)

    gold_by_key = {}
    for g in gold_list:
        key = (round(float(g["x"]),3), round(float(g["z"]),3))
        gold_by_key[key] = float(g["w"])

    agent_by_key = {}
    for row in artifact:
        try:
            x = float(row.get("x"))
            z = float(row.get("z"))
            w = float(row.get("w"))
            key = (round(x,3), round(z,3))
            agent_by_key[key] = w
        except:
            continue

    total_points = len(gold_by_key)
    correct_points = 0
    for key, gw in gold_by_key.items():
        aw = agent_by_key.get(key)
        if aw is not None and abs(aw - gw) <= tol:
            correct_points += 1
    pointwise_score = correct_points / total_points if total_points>0 else 0.0

    z_values = sorted(set(k[1] for k in agent_by_key.keys()))
    monotonic = True
    for z in z_values:
        points = [(k[0], agent_by_key[k]) for k in agent_by_key if k[1] == z]
        points.sort()
        for i in range(1, len(points)):
            if points[i][1] < points[i-1][1] - 1e-9:
                monotonic = False
                break
        if not monotonic:
            break
    monotonic_score = 1.0 if monotonic else 0.0

    boundary_checks = { (0.0,0.0):0.0, (0.0,0.5):0.5, (0.0,1.0):1.0 }
    boundary_ok = True
    for (bx,bz), bw in boundary_checks.items():
        key = (round(bx,3), round(bz,3))
        aw = agent_by_key.get(key)
        if aw is None or abs(aw - bw) > tight_tol:
            boundary_ok = False
            break
    boundary_score = 1.0 if boundary_ok else 0.0

    return pointwise_score * 0.5 + monotonic_score * 0.3 + boundary_score * 0.2


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    gold_list = step.get("gold", [])
    if not gold_list or not artifact:
        return 0.0
    tol = step.get("tolerance", 0.005)

    gold_by_voltage = {}
    for g in gold_list:
        v = float(g["voltage"])
        d = float(g["tip_displacement"])
        gold_by_voltage[round(v,2)] = d

    agent_by_voltage = {}
    for row in artifact:
        try:
            v = float(row.get("voltage"))
            d = float(row.get("tip_displacement"))
            agent_by_voltage[round(v,2)] = d
        except:
            continue

    total_points = len(gold_by_voltage)
    correct = 0
    for v, gd in gold_by_voltage.items():
        ad = agent_by_voltage.get(v)
        if ad is not None and abs(ad - gd) <= tol:
            correct += 1
    pointwise_score = correct / total_points if total_points>0 else 0.0

    voltages = sorted(agent_by_voltage.keys())
    monotonic = True
    for i in range(1, len(voltages)):
        if agent_by_voltage[voltages[i]] < agent_by_voltage[voltages[i-1]] - 1e-9:
            monotonic = False
            break
    monotonic_score = 1.0 if monotonic else 0.0

    return pointwise_score * 0.6 + monotonic_score * 0.4


_SCORERS = {
    'step_01': score_0,
    'step_02': score_1,
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
