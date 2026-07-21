import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os

def get_gap_values(rows, col):
    data = []
    for r in rows:
        d = float(r['diameter_nm'])
        g = float(r[col])
        data.append((d, g))
    data.sort(key=lambda x: x[0])
    return data

def find_transition_diameter(data):
    # data sorted ascending by diameter
    prev_d, prev_g = data[0]
    for d, g in data[1:]:
        if prev_g <= 0 and g > 0:
            if g - prev_g != 0:
                t = prev_d + (0 - prev_g) * (d - prev_d) / (g - prev_g)
            else:
                t = prev_d
            return t
        prev_d, prev_g = d, g
    return None

def interpolate_zt(data, target_d):
    # data sorted ascending by diameter
    if not data:
        return None
    if target_d <= data[0][0]:
        return data[0][1]
    if target_d >= data[-1][0]:
        return data[-1][1]
    for i in range(len(data)-1):
        d0, z0 = data[i]
        d1, z1 = data[i+1]
        if d0 <= target_d <= d1:
            if d1 == d0:
                return (z0+z1)/2
            frac = (target_d - d0) / (d1 - d0)
            return z0 + frac * (z1 - z0)
    return None


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


# === block: score_0 (check id='step_02_band_gap') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows or not isinstance(rows, list) or not rows:
        return 0.0
    first = rows[0]
    if not all(k in first for k in ['diameter_nm','binary_gap_meV','trigonal_gap_meV','bisectrix_gap_meV']):
        return 0.0
    conf = step.get('config', {})
    targets = conf.get('transition_targets', {'binary': 30, 'trigonal': 45, 'bisectrix': 81})
    tol_nm = conf.get('trans_tol_nm', 10)
    binary_data = get_gap_values(rows, 'binary_gap_meV')
    trigonal_data = get_gap_values(rows, 'trigonal_gap_meV')
    bisectrix_data = get_gap_values(rows, 'bisectrix_gap_meV')
    transition_diams = {}
    for orient, data in [('binary', binary_data), ('trigonal', trigonal_data), ('bisectrix', bisectrix_data)]:
        td = find_transition_diameter(data)
        transition_diams[orient] = td
    transition_pass = all(
        abs(transition_diams.get(orient, 999) - targets[orient]) <= tol_nm
        for orient in targets
    )
    monotonic_pass = True
    for orient, data in [('binary', binary_data), ('trigonal', trigonal_data), ('bisectrix', bisectrix_data)]:
        td = transition_diams[orient]
        if td is None:
            continue
        subset = [(d,g) for d,g in data if d <= td + 1e-9]
        if len(subset) < 2:
            continue
        prev_g = subset[0][1]
        for d,g in subset[1:]:
            if g > prev_g + 1e-9:
                monotonic_pass = False
                break
            prev_g = g
        if not monotonic_pass:
            break
    return (transition_pass * 0.5) + (monotonic_pass * 0.5)


# === block: score_1 (check id='step_03_ZT') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows or not isinstance(rows, list) or not rows:
        return 0.0
    first = rows[0]
    if not all(k in first for k in ['diameter_nm','ZT']):
        return 0.0
    data = [(float(r['diameter_nm']), float(r['ZT'])) for r in rows]
    data.sort(key=lambda x: x[0])
    conf = step.get('config', {})
    max_d = conf.get('max_diameter_monotonic', 50.0)
    monotonic = True
    subset = [(d,zt) for d,zt in data if d <= max_d]
    if len(subset) >= 2:
        prev_zt = subset[0][1]
        for d,zt in subset[1:]:
            if zt > prev_zt + 1e-9:
                monotonic = False
                break
            prev_zt = zt
    gold_zt = conf.get('gold_zt', {})
    tol_rel = conf.get('zt_tol_rel', 0.25)
    pass_count = 0
    for d_str, gold in gold_zt.items():
        d_target = float(d_str)
        zt_agent = interpolate_zt(data, d_target)
        if zt_agent is not None and abs(zt_agent - gold) <= tol_rel * gold:
            pass_count += 1
    zt_value_pass = 1.0 if pass_count >= 3 else 0.0
    score = 0.1 + monotonic * 0.3 + zt_value_pass * 0.6
    return min(score, 1.0)


_SCORERS = {
    'step_02_band_gap': score_0,
    'step_03_ZT': score_1,
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
