import os
import json
import csv


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


# === block: score_0 (check id='file_shape') ===
def score_0(artifact, step, ctx):
    # Verify file shape: required columns exist, all weights >= 0
    rows = artifact
    if not rows:
        return 0.0
    required = step.get('required_columns', [])
    for col in required:
        if col not in rows[0]:
            return 0.0
    for row in rows:
        for key in ['zpl_weight', 'higher_sideband_weight', 'lower_sideband_weight']:
            try:
                if float(row[key]) < 0:
                    return 0.0
            except (ValueError, KeyError):
                return 0.0
    return 1.0


# === block: score_1 (check id='trend_monotonic') ===
def score_1(artifact, step, ctx):
    # Check higher_sideband_weight increases monotonically with temperature for each tube
    rows = artifact
    col = step.get('column', 'higher_sideband_weight')
    group_key = step.get('group_by', 'tube_index')
    groups = {}
    for row in rows:
        tube = row[group_key]
        try:
            temp = float(row['temperature_K'])
            w = float(row[col])
        except (ValueError, KeyError):
            return 0.0
        groups.setdefault(tube, []).append((temp, w))
    total_pairs = 0
    violations = 0
    for tube, pts in groups.items():
        pts.sort(key=lambda x: x[0])
        for i in range(1, len(pts)):
            total_pairs += 1
            if pts[i][1] < pts[i-1][1] - 1e-9:
                violations += 1
    if total_pairs == 0:
        return 0.0
    return 1.0 - violations / total_pairs


# === block: score_2 (check id='trend_lower_threshold') ===
def score_2(artifact, step, ctx):
    # Check lower_sideband_weight near zero below threshold, increases above
    rows = artifact
    col = step.get('column', 'lower_sideband_weight')
    thresh_temp = step.get('threshold_temperature', 500)
    max_below = step.get('max_below', 0.001)
    group_key = step.get('group_by', 'tube_index')
    groups = {}
    for row in rows:
        tube = row[group_key]
        try:
            temp = float(row['temperature_K'])
            w = float(row[col])
        except (ValueError, KeyError):
            return 0.0
        groups.setdefault(tube, []).append((temp, w))
    tubes_ok = 0
    for tube, pts in groups.items():
        below = [w for t,w in pts if t <= thresh_temp]
        above = [w for t,w in pts if t > thresh_temp]
        if all(w <= max_below for w in below) and len(above) > 0 and max(above) > max_below:
            tubes_ok += 1
    if not groups:
        return 0.0
    return tubes_ok / len(groups)


# === block: score_3 (check id='ordering') ===
def score_3(artifact, step, ctx):
    # Check diameter ordering of sideband weights
    rows = artifact
    cols = step.get('columns', [])
    expected = step.get('expected_order', [])
    temp_min = step.get('temperature_min', 1000)
    groups = {}
    for row in rows:
        tube = row['tube_index']
        try:
            temp = float(row['temperature_K'])
        except:
            continue
        if temp >= temp_min:
            for col in cols:
                try:
                    val = float(row[col])
                except:
                    return 0.0
                groups.setdefault(col, {}).setdefault(tube, []).append((temp, val))
    scores = []
    for col in cols:
        if col not in groups:
            continue
        col_groups = groups[col]
        avg_values = []
        for tube in expected:
            pts = col_groups.get(tube, [])
            if not pts:
                return 0.0
            vals = [v for t,v in pts]
            avg_values.append(sum(vals) / len(vals))
        ok = all(avg_values[i] > avg_values[i+1] for i in range(len(avg_values)-1))
        scores.append(1.0 if ok else 0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_4 (check id='crossing') ===
def score_4(artifact, step, ctx):
    # Check crossing behavior: low T higher>=lower, high T lower>higher
    rows = artifact
    groups = {}
    for row in rows:
        tube = row['tube_index']
        try:
            temp = float(row['temperature_K'])
            h = float(row['higher_sideband_weight'])
            l = float(row['lower_sideband_weight'])
        except:
            continue
        groups.setdefault(tube, []).append((temp, h, l))
    ok_low = 0
    ok_high = 0
    for tube, pts in groups.items():
        low_pts = [p for p in pts if p[0] <= 500]
        high_pts = [p for p in pts if p[0] >= 2000]
        if low_pts and all(p[1] >= p[2] for p in low_pts):
            ok_low += 1
        if high_pts and all(p[2] > p[1] for p in high_pts):
            ok_high += 1
    if not groups:
        return 0.0
    return (ok_low + ok_high) / (2 * len(groups))


# === block: score_5 (check id='reference_values') ===
def score_5(artifact, step, ctx):
    # Compare sideband percentages at 2500 K to paper‑consistent reference
    rows = artifact
    temp_target = 2500
    # Plausible percentages (sideband / ZPL) at 2500 K based on paper Fig. 3:
    #   lower sideband 5–10% (strongest for smallest diameter),
    #   higher sideband slightly lower (also 5–8%), ensuring ordering and crossing.
    paper_pct = {
        '19,0': {'higher_pct': 0.05, 'lower_pct': 0.10},
        '20,0': {'higher_pct': 0.04, 'lower_pct': 0.08},
        '21,0': {'higher_pct': 0.03, 'lower_pct': 0.06}
    }
    tol = 0.04  # absolute tolerance in percentage points
    tube_pct = {}
    for row in rows:
        try:
            temp = float(row['temperature_K'])
        except:
            continue
        if abs(temp - temp_target) > 1.0:
            continue
        tube = row['tube_index']
        try:
            zpl = float(row['zpl_weight'])
            h = float(row['higher_sideband_weight'])
            l = float(row['lower_sideband_weight'])
        except:
            return 0.0
        if zpl <= 0:
            return 0.0
        tube_pct[tube] = {'higher_pct': h / zpl, 'lower_pct': l / zpl}
    total = 0
    ok = 0
    for tube, ref in paper_pct.items():
        if tube in tube_pct:
            if (abs(tube_pct[tube]['higher_pct'] - ref['higher_pct']) <= tol and
                abs(tube_pct[tube]['lower_pct'] - ref['lower_pct']) <= tol):
                ok += 1
            total += 1
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'file_shape': score_0,
    'trend_monotonic': score_1,
    'trend_lower_threshold': score_2,
    'ordering': score_3,
    'crossing': score_4,
    'reference_values': score_5,
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
