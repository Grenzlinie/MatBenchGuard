import os
import json
import csv

# === author imports / helpers ===
import csv
import io
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


# === block: score_0 (check id='step_03_bandgap') ===
def score_0(artifact, step, ctx):
    try:
        gap = float(artifact.strip())
    except:
        return 0.0
    if abs(gap - step['target']) <= step['tolerance']:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step_04_thermopower') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list):
        return 0.0
    rows = artifact
    req_cols = step['config']['required_columns']
    if not all(c in rows[0] for c in req_cols):
        return 0.0
    valid_d = step['config']['valid_doping']
    groups = {}
    for r in rows:
        try:
            d = float(r.get('doping'))
            T = float(r.get('T'))
            S = float(r.get('S_xx'))
        except:
            continue
        if d not in valid_d:
            continue
        groups.setdefault(d, []).append((T, S))
    if len(groups) != len(valid_d):
        return 0.0
    sub = step['config']['sub_weights']
    # monotonicity
    mono_score = 0.0
    for d in valid_d:
        pts = sorted(groups.get(d, []), key=lambda x: x[0])
        if len(pts) < 2:
            continue
        S_vals = [p[1] for p in pts]
        if all(S_vals[i] < S_vals[i+1] for i in range(len(S_vals)-1)):
            mono_score += 1.0 / len(valid_d)
    # ordering at T_ref
    T_ref = step['config']['magnitude_check']['T_ref']
    def get_S_at_T(pts, T):
        best = min(pts, key=lambda p: abs(p[0]-T))
        return best[1]
    ord_score = 0.0
    try:
        S_01 = get_S_at_T(groups[0.1], T_ref)
        S_02 = get_S_at_T(groups[0.2], T_ref)
        S_03 = get_S_at_T(groups[0.3], T_ref)
        if S_01 > S_02 > S_03:
            ord_score = 1.0
    except:
        ord_score = 0.0
    # magnitude
    ranges = step['config']['magnitude_check']['ranges']
    mag_score = 0.0
    n_mag = 0
    for d_str, (low, high) in ranges.items():
        d = float(d_str)
        if d in groups:
            S_val = get_S_at_T(groups[d], T_ref)
            if low <= S_val <= high:
                mag_score += 1.0
            n_mag += 1
    if n_mag > 0:
        mag_score /= n_mag
    else:
        mag_score = 0.0
    return sub['monotonic'] * mono_score + sub['ordering'] * ord_score + sub['magnitude'] * mag_score


_SCORERS = {
    'step_03_bandgap': score_0,
    'step_04_thermopower': score_1,
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
