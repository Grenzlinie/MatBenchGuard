import os
import json
import csv

# === author imports / helpers ===
import math, csv, json
from collections import defaultdict


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


# === block: score_0 (check id='mulliken_pairs') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    expected = gold.get('pairs', {})
    tolerance = gold.get('tolerance', 1)
    charge_threshold = gold.get('charge_threshold', 0.0)
    dist_threshold = gold.get('distance_threshold', 3.0)

    time_data = defaultdict(list)
    for row in artifact:
        try:
            t = float(row['time_ps'])
        except:
            continue
        time_data[t].append(row)

    total = 0
    valid_times = 0
    for t_str, exp_count in expected.items():
        t = float(t_str)
        if t not in time_data:
            continue
        rows = time_data[t]
        oxygens = []
        for r in rows:
            if r.get('element', '').strip() == 'O':
                try:
                    charge = float(r['mulliken_charge'])
                    if charge > charge_threshold:
                        x = float(r['x'])
                        y = float(r['y'])
                        z = float(r['z'])
                        oxygens.append((x, y, z))
                except:
                    pass
        n = len(oxygens)
        pairs = 0
        for i in range(n):
            xi, yi, zi = oxygens[i]
            for j in range(i+1, n):
                xj, yj, zj = oxygens[j]
                dist = math.sqrt((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)
                if dist < dist_threshold:
                    pairs += 1
        diff = abs(pairs - exp_count)
        if diff <= tolerance:
            total += 1
        valid_times += 1

    if valid_times == 0:
        return 0.0
    return total / float(valid_times)


# === block: score_1 (check id='mulliken_bonds') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    check_times = gold.get('check_times', [2.0, 3.0])
    dist_range = gold.get('distance_range', [2.5, 3.2])
    align_thresh = gold.get('alignment_threshold', 0.8)

    time_data = defaultdict(list)
    for row in artifact:
        try:
            t = float(row['time_ps'])
        except:
            continue
        time_data[t].append(row)

    total = 0
    for t in check_times:
        if t not in time_data:
            continue
        rows = time_data[t]
        ti_atoms = []
        for r in rows:
            if r.get('element', '').strip() == 'Ti':
                try:
                    x = float(r['x'])
                    y = float(r['y'])
                    z = float(r['z'])
                    ti_atoms.append((x, y, z))
                except:
                    pass
        found = False
        n = len(ti_atoms)
        for i in range(n):
            if found:
                break
            xi, yi, zi = ti_atoms[i]
            for j in range(i+1, n):
                xj, yj, zj = ti_atoms[j]
                dx = xj - xi
                dy = yj - yi
                dz = zj - zi
                dist = math.sqrt(dx*dx + dy*dy + dz*dz)
                if dist_range[0] <= dist <= dist_range[1]:
                    proj = abs(dy)
                    if proj >= align_thresh * dist:
                        found = True
                        break
        if found:
            total += 1

    if len(check_times) == 0:
        return 0.0
    return total / float(len(check_times))


# === block: score_2 (check id='band_gaps') ===
def score_2(artifact, step, ctx):
    gold = step.get('gold', {})
    req_times = set(gold.get('times', []))
    max_gap = gold.get('max_gap_eV', 0.15)

    data = {}
    for line in artifact.strip().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 2:
            try:
                t = float(parts[0])
                gap = float(parts[1])
                data[t] = gap
            except:
                pass

    total = 0
    for t in req_times:
        if t in data and data[t] <= max_gap:
            total += 1

    if len(req_times) == 0:
        return 0.0
    return total / len(req_times)


_SCORERS = {
    'mulliken_pairs': score_0,
    'mulliken_bonds': score_1,
    'band_gaps': score_2,
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
