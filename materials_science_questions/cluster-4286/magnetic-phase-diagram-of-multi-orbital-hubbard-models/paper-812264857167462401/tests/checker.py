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


# === block: score_0 (check id='quasiparticle_weight') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = []
    for row in artifact:
        try:
            v = float(row['V'])
            u = float(row['U'])
            z = float(row['Z'])
            rows.append((v, u, z))
        except Exception:
            continue
    if not rows:
        return 0.0
    # Condition 1: For V>0, all Z > 1e-3
    c1 = all(z > 1e-3 for v, u, z in rows if v > 0)
    # Condition 2: For each V, Z is monotonic non-increasing with U
    c2 = True
    for v in set(v for v, _, _ in rows):
        zv = [(u, z) for vv, u, z in rows if vv == v]
        zv.sort(key=lambda x: x[0])
        prev = 1.0
        for _, z in zv:
            if z > prev + 1e-9:
                c2 = False
                break
            prev = z
    # Condition 3: For V=0, Z close to zero at U>=3.0
    c3 = True
    v0_rows = [(u, z) for vv, u, z in rows if vv == 0.0]
    if v0_rows:
        for u, z in v0_rows:
            if u >= 3.0 and z > 1e-6:
                c3 = False
                break
    else:
        c3 = False
    score = 0.0
    if c1:
        score += 1.0/3.0
    if c2:
        score += 1.0/3.0
    if c3:
        score += 1.0/3.0
    return score


# === block: score_1 (check id='critical_temperatures') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    gold = step.get('hidden', {}).get('gold', {})
    tol = step.get('hidden', {}).get('tolerance', 0.02)
    data = {}
    for row in artifact:
        try:
            v = float(row['V'])
            upper = float(row['upper_Tc'])
            lower = float(row['lower_Tc'])
            data[v] = {'upper_Tc': upper, 'lower_Tc': lower}
        except Exception:
            continue
    total_pairs = len(gold) * 2
    matched = 0
    for v_str, expected in gold.items():
        v_key = float(v_str)
        if v_key not in data:
            continue
        row = data[v_key]
        if abs(row['upper_Tc'] - expected['upper_Tc']) <= tol:
            matched += 1
        if abs(row['lower_Tc'] - expected['lower_Tc']) <= tol:
            matched += 1
    if total_pairs == 0:
        return 0.0
    return matched / total_pairs


_SCORERS = {
    'quasiparticle_weight': score_0,
    'critical_temperatures': score_1,
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
