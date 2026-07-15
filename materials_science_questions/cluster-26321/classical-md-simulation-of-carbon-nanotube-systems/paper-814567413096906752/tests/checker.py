import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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


# === block: score_0 (check id='check_zcoord') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    lines = artifact.strip().split('\n')
    if len(lines) < 2:
        return 0.0
    time_vals = []
    z_vals = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            t = float(parts[0])
            z = float(parts[1])
        except (ValueError, TypeError):
            continue
        time_vals.append(t)
        z_vals.append(z)
    if not time_vals:
        return 0.0
    total_time = time_vals[-1] - time_vals[0]
    if total_time < 5000:
        return 0.0
    threshold_time = time_vals[-1] - 5000
    last_z = [z for t, z in zip(time_vals, z_vals) if t >= threshold_time]
    if not last_z:
        return 0.0
    avg_z = sum(last_z) / len(last_z)
    return 1.0 if avg_z > 6.0 else 0.0


# === block: score_1 (check id='check_water_energy') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 10:
            return 0.0
        region_sums = [0.0, 0.0, 0.0, 0.0]
        region_counts = [0, 0, 0, 0]
        for row in artifact:
            try:
                z = float(row['z'])
                e = float(row['water_energy_per_molecule'])
            except (KeyError, ValueError):
                continue
            if z < 0 or z > 24:
                continue
            idx = min(3, int(z // 6))
            region_sums[idx] += e
            region_counts[idx] += 1
        if any(count == 0 for count in region_counts):
            return 0.0
        means = [s/c for s, c in zip(region_sums, region_counts)]
        if means[0] < means[1] and means[1] < means[2] and means[2] < means[3]:
            return 1.0
        else:
            return 0.0


# === block: score_2 (check id='check_U_NP_volume') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        if not artifact or len(artifact) < 10:
            return 0.0
        val3 = None
        val21 = None
        prev_z3 = None
        prev_z21 = None
        for row in artifact:
            try:
                z = float(row['z'])
                u = float(row['U_NP_volume'])
            except (KeyError, ValueError):
                continue
            if abs(z - 3.0) <= 0.2:
                if val3 is None or abs(z - 3.0) < abs(prev_z3 - 3.0):
                    val3 = u
                    prev_z3 = z
            if abs(z - 21.0) <= 0.2:
                if val21 is None or abs(z - 21.0) < abs(prev_z21 - 21.0):
                    val21 = u
                    prev_z21 = z
        if val3 is None or val21 is None:
            return 0.0
        diff = abs(val3) - abs(val21)
        if diff >= 5.0:
            return 1.0
        elif abs(val3) > abs(val21):
            return 0.5
        else:
            return 0.0


_SCORERS = {
    'check_zcoord': score_0,
    'check_water_energy': score_1,
    'check_U_NP_volume': score_2,
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
