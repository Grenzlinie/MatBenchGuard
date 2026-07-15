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


# === block: score_0 (check id='coverage_density') ===
def score_0(artifact, step, ctx):
    refs = step.get('reference_densities', {})
    tol = step.get('tolerance_abs', 0.0005)
    cov_scan = artifact.get('coverage_scan', [])
    if not cov_scan:
        return 0.0
    total = 0
    passed = 0
    for entry in cov_scan:
        tube = entry.get('tube')
        cov = entry.get('coverage')
        den = entry.get('density')
        if tube in refs and str(cov) in refs[tube]:
            ref_val = refs[tube][str(cov)]
            if abs(den - ref_val) <= tol:
                passed += 1
            total += 1
    if total == 0:
        return 0.0
    return passed / total


# === block: score_1 (check id='coverage_monotonic') ===
def score_1(artifact, step, ctx):
    cov_scan = artifact.get('coverage_scan', [])
    from collections import defaultdict
    groups = defaultdict(list)
    for e in cov_scan:
        groups[e['tube']].append((e['coverage'], e['density']))
    score = 0.0
    for tube, pts in groups.items():
        if len(pts) < 2:
            continue
        pts.sort(key=lambda x: x[0])
        mono = True
        for i in range(1, len(pts)):
            if pts[i][1] > pts[i-1][1] + 1e-5:
                mono = False
                break
        if mono and (pts[0][1] - pts[-1][1]) > 1e-4:
            score += 1.0
    if len(groups) > 0:
        score /= len(groups)
    return score


# === block: score_2 (check id='isotherms_hydrogenated_below') ===
def score_2(artifact, step, ctx):
    clean = artifact.get('isotherms_clean', [])
    hyd = artifact.get('isotherms_hydrogenated', [])
    temps = step.get('comparison_temperatures', [])
    target_ps = step.get('target_pressures', [])
    p_tol = step.get('pressure_tolerance', 0.5)
    def match_p(clist):
        out = {}
        for p in target_ps:
            best = None
            min_diff = float('inf')
            for entry in clist:
                diff = abs(entry['pressure'] - p)
                if diff < p_tol and diff < min_diff:
                    best = entry
                    min_diff = diff
            if best is not None:
                out[p] = best
        return out
    score = 0.0
    count = 0
    for T in temps:
        clean_T = [e for e in clean if e['temperature'] == T]
        hyd_T = [e for e in hyd if e['temperature'] == T]
        clean_map = match_p(clean_T)
        hyd_map = match_p(hyd_T)
        for p in target_ps:
            c = clean_map.get(p)
            h = hyd_map.get(p)
            if c is not None and h is not None:
                count += 1
                if h['gravimetric_capacity'] <= c['gravimetric_capacity'] and h['volumetric_capacity'] <= c['volumetric_capacity']:
                    score += 1.0
    if count == 0:
        return 0.0
    return score / count


# === block: score_3 (check id='oxidized_capacity_77K_20MPa') ===
def score_3(artifact, step, ctx):
    ox = artifact.get('isotherms_oxidized', [])
    target_temp = step.get('target_temperature', 77)
    target_p = step.get('target_pressure', 20.0)
    p_tol = step.get('pressure_tolerance', 0.5)
    target_grav = step.get('target_gravimetric', 4.10)
    grav_tol = step.get('gravimetric_tolerance', 0.50)
    best = None
    min_diff = float('inf')
    for entry in ox:
        if entry['temperature'] == target_temp:
            diff = abs(entry['pressure'] - target_p)
            if diff < p_tol and diff < min_diff:
                best = entry
                min_diff = diff
    if best is None:
        return 0.0
    grav = best['gravimetric_capacity']
    if abs(grav - target_grav) <= grav_tol:
        return 1.0
    return 0.0


# === block: score_4 (check id='clean_10MPa_293K_gravimetric') ===
def score_4(artifact, step, ctx):
    clean = artifact.get('isotherms_clean', [])
    target_temp = step.get('target_temperature', 293)
    target_p = step.get('target_pressure', 10.0)
    p_tol = step.get('pressure_tolerance', 0.5)
    target_grav = step.get('target_gravimetric', 3.4)
    grav_tol = step.get('gravimetric_tolerance', 0.5)
    best = None
    min_diff = float('inf')
    for entry in clean:
        if entry['temperature'] == target_temp:
            diff = abs(entry['pressure'] - target_p)
            if diff < p_tol and diff < min_diff:
                best = entry
                min_diff = diff
    if best is None:
        return 0.0
    grav = best['gravimetric_capacity']
    if abs(grav - target_grav) <= grav_tol:
        return 1.0
    return 0.0


_SCORERS = {
    'coverage_density': score_0,
    'coverage_monotonic': score_1,
    'isotherms_hydrogenated_below': score_2,
    'oxidized_capacity_77K_20MPa': score_3,
    'clean_10MPa_293K_gravimetric': score_4,
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
