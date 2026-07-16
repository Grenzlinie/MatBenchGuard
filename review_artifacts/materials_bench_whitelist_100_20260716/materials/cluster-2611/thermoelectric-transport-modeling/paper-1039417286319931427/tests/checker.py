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
    steps = spec.get('steps', spec.get('checks', []))
    ctx = {}
    for step in steps:
        ctx[step['id']] = step.get('params', {})
    return ctx


# === block: score_0 (check id='step_2_transmission') ===
def score_0(artifact, step, ctx):
    params = ctx['step_2_transmission']
    energy_col = params['energy_column']
    system_col = params['system_column']
    trans_col = params['transmission_column']
    peak_thresh = params['peak_threshold']
    systems_cfg = params['systems']

    # helper: find peaks (local maxima) within window, above threshold
    def find_peaks(rows, energy_col, trans_col, window, threshold):
        points = []
        for row in rows:
            try:
                e = float(row.get(energy_col, 0))
                t = float(row.get(trans_col, 0))
            except (ValueError, TypeError):
                continue
            if window[0] <= e <= window[1]:
                points.append((e, t))
        if not points:
            return []
        points.sort(key=lambda x: x[0])
        peaks = []
        n = len(points)
        for i in range(1, n-1):
            if points[i][1] > points[i-1][1] and points[i][1] > points[i+1][1] and points[i][1] >= threshold:
                peaks.append(points[i][0])
        return peaks

    # greedy matching: each found peak assigned to closest expected within tolerance, no double assignment
    def match_peaks(found, expected, tol):
        expected = sorted(expected)
        used = [False]*len(expected)
        matches = 0
        for fp in found:
            best_idx = -1
            best_dist = float('inf')
            for i, ep in enumerate(expected):
                if used[i]:
                    continue
                dist = abs(fp - ep)
                if dist < best_dist:
                    best_dist = dist
                    best_idx = i
            if best_idx != -1 and best_dist <= tol:
                matches += 1
                used[best_idx] = True
        return matches

    # Separate rows by system
    system_rows = {}
    for row in artifact:
        sys = row.get(system_col, '').strip()
        if sys not in system_rows:
            system_rows[sys] = []
        system_rows[sys].append(row)

    sub_scores = []
    for sys_name, cfg in systems_cfg.items():
        rows = system_rows.get(sys_name, [])
        if not rows:
            sub_scores.append(0.0)
            continue
        window = cfg['window']
        if 'expected_peak_count' in cfg:  # C60 case
            peaks = find_peaks(rows, energy_col, trans_col, window, peak_thresh)
            score = 1.0 if len(peaks) <= cfg['expected_peak_count'] else 0.0
        else:
            expected = cfg['expected_peaks']
            tol = cfg['tolerance']
            peaks = find_peaks(rows, energy_col, trans_col, window, peak_thresh)
            matches = match_peaks(peaks, expected, tol)
            score = min(1.0, matches / float(len(expected)))
        sub_scores.append(score)

    if not sub_scores:
        return 0.0
    return sum(sub_scores) / len(sub_scores)


# === block: score_1 (check id='step_3_seebeck') ===
def score_1(artifact, step, ctx):
    params = ctx['step_3_seebeck']
    energy_col = params['energy_column']
    system_col = params['system_column']
    see_col = params['seebeck_column']
    target_system = params['target_system']
    window = params['energy_window']
    spread_target = params['spread_target']
    spread_thresh = params['spread_threshold']

    values = []
    for row in artifact:
        sys = row.get(system_col, '').strip()
        if sys != target_system:
            continue
        try:
            e = float(row.get(energy_col, 0))
            s = float(row.get(see_col, 0))
        except (ValueError, TypeError):
            continue
        if window[0] <= e <= window[1]:
            values.append(s)

    if not values:
        return 0.0
    max_s = max(values)
    min_s = min(values)
    spread = max_s - min_s

    if spread >= spread_target:
        return 1.0
    if spread <= spread_thresh:
        return 0.0
    return (spread - spread_thresh) / (spread_target - spread_thresh)


# === block: score_2 (check id='step_4_zt') ===
def score_2(artifact, step, ctx):
    params = ctx['step_4_zt']
    energy_col = params['energy_column']
    system_col = params['system_column']
    zt_col = params['zt_column']
    target_system = params['target_system']
    window = params['energy_window']
    zt_target = params['zt_target']
    zt_thresh = params['zt_threshold']

    zt_vals = []
    for row in artifact:
        sys = row.get(system_col, '').strip()
        if sys != target_system:
            continue
        try:
            e = float(row.get(energy_col, 0))
            z = float(row.get(zt_col, 0))
        except (ValueError, TypeError):
            continue
        if window[0] <= e <= window[1]:
            zt_vals.append(z)

    if not zt_vals:
        return 0.0
    max_zt = max(zt_vals)

    if max_zt >= zt_target:
        return 1.0
    if max_zt <= zt_thresh:
        return 0.0
    return (max_zt - zt_thresh) / (zt_target - zt_thresh)


_SCORERS = {
    'step_2_transmission': score_0,
    'step_3_seebeck': score_1,
    'step_4_zt': score_2,
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
