import os
import json
import csv

# === author imports / helpers ===
import csv
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


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    artifact_csv = artifact
    if not artifact_csv or len(artifact_csv) == 0:
        return 0.0
    total = len(artifact_csv)
    correct = 0
    for row in artifact_csv:
        try:
            x = float(row['K24_over_K2'])
            y = float(row['K3_over_K2'])
            beta_reported = float(row['beta1_rad'])
            free_reported = float(row['free_energy_per_piL'])
        except (KeyError, ValueError):
            continue
        # Expected beta1
        if x < 2.0:
            expected_beta = 0.0
        else:
            arg = math.sqrt(2.0 * x * (x - 2.0) / y)
            expected_beta = math.atan(arg)
        # Expected free energy per piL (K2=1)
        if x < 2.0:
            expected_free = 0.0
        else:
            if y == 1.0:
                expected_free = -(x - 2.0) + (x - 2.0) / (x - 1.0)  # limit y->1
            else:
                expected_free = -(x - 2.0) + (y / math.sqrt(y - 1.0)) * math.atan(
                    math.sqrt(y - 1.0) * (x - 2.0) / (y + x - 2.0)
                )
        if abs(beta_reported - expected_beta) <= 0.001 and abs(free_reported - expected_free) <= 0.001:
            correct += 1
    return correct / total


# === block: score_1 (check id='step_02') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or len(rows) < 10:
        return 0.0
    # Sort by K24_over_K
    sorted_rows = sorted(rows, key=lambda r: float(r['K24_over_K']))
    k = [float(r['K24_over_K']) for r in sorted_rows]
    ep = [float(r['energy_point']) for r in sorted_rows]
    ew = [float(r['energy_wall']) for r in sorted_rows]
    # Monotonicity with epsilon for floating noise
    ep_mono = all(ep[i+1] <= ep[i] + 1e-6 for i in range(len(ep)-1))
    ew_mono = all(ew[i+1] >= ew[i] - 1e-6 for i in range(len(ew)-1))
    # Crossover detection
    cross_idx = None
    for i in range(1, len(ep)):
        if ep[i] <= ew[i] and ep[i-1] > ew[i-1]:
            cross_idx = i
            break
    crossover_exists = cross_idx is not None
    cross_in_range = False
    if crossover_exists:
        cross_k = k[cross_idx]
        cross_in_range = 3.5 <= cross_k <= 4.5
    # Ordering at extremes
    ep_high = ep[-1] < ew[-1]  # point defect lower
    ep_low = ep[0] > ew[0]     # point defect higher
    score = 0.0
    if ep_mono:
        score += 0.2
    if ew_mono:
        score += 0.2
    if crossover_exists and cross_in_range:
        score += 0.3
    if ep_high:
        score += 0.15
    if ep_low:
        score += 0.15
    return score


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
