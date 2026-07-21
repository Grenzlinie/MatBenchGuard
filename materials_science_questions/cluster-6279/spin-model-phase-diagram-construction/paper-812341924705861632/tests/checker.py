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


# === block: score_0 (check id='step0-phase-diagram') ===
def score_0(artifact, step, ctx):
    score = 0.0
    rows = artifact
    mu_key = 'beta_mu'
    om_key = 'beta_omega3'
    phase_key = 'phase_type'
    found_types = set()
    tricrit = None
    for r in rows:
        try:
            mu = float(r[mu_key])
            omega = float(r[om_key])
            pt = str(r.get(phase_key, '')).strip()
            found_types.add(pt)
            if pt.lower() == 'tricritical':
                tricrit = (mu, omega)
        except (ValueError, KeyError):
            continue
    target = step.get('target', {})
    missing_types = set(target.get('required_phase_types', [])) - found_types
    if missing_types:
        score += max(0.0, 1.0 - len(missing_types) * 0.25)
    else:
        score += 0.5
    if tricrit is not None:
        ref_mu = target.get('tricritical_mu', 5.1)
        ref_om = target.get('tricritical_omega3', 0.2)
        tol = target.get('tricritical_euclidean_tol', 0.3)
        dist = math.hypot(tricrit[0] - ref_mu, tricrit[1] - ref_om)
        if dist <= tol:
            score += 0.5
        else:
            score += 0.5 * max(0.0, 1.0 - (dist - tol) / (2 * tol))
    else:
        score += 0.0
    return min(score, 1.0)


# === block: score_1 (check id='step1-heat-adsorption') ===
def score_1(artifact, step, ctx):
    score = 0.0
    rows = artifact
    cov_key = 'coverage'
    est_key = 'Est_eV'
    floats = []
    for r in rows:
        try:
            cov = float(r[cov_key])
            est = float(r[est_key])
            floats.append((cov, est))
        except (ValueError, KeyError):
            continue
    if not floats:
        return 0.0
    floats.sort(key=lambda x: x[0])
    target = step.get('target', {})
    target_cov_low = target['coverage_low']
    target_cov_high = target['coverage_high']
    est_low_min = target['est_low_min']
    est_high_max = target['est_high_max']
    drop_min = target['drop_min']
    # find nearest points
    def nearest(arr, val):
        best = None
        best_dist = float('inf')
        for cov, est in arr:
            d = abs(cov - val)
            if d < best_dist:
                best_dist = d
                best = (cov, est)
        return best
    low = nearest(floats, target_cov_low)
    high = nearest(floats, target_cov_high)
    below_half = nearest(floats, 0.48)
    above_half = nearest(floats, 0.52)
    checks = 0
    total = 0
    if low is not None and low[1] >= est_low_min:
        score += 0.2
    if high is not None and high[1] <= est_high_max:
        score += 0.2
    if below_half is not None and above_half is not None:
        if (below_half[1] - above_half[1]) >= drop_min:
            score += 0.3
    # monotonic decrease check after 0.5 ML
    sub = [(cov, est) for cov, est in floats if cov > 0.5]
    monotonic = True
    for i in range(1, len(sub)):
        if sub[i][1] > sub[i-1][1] + 1e-6:
            monotonic = False
            break
    if monotonic and sub:
        score += 0.3
    return min(score, 1.0)


# === block: score_2 (check id='step2-adsorption-isobars') ===
def score_2(artifact, step, ctx):
    score = 0.0
    rows = artifact
    t_key = 'temperature_K'
    cov_key = 'coverage'
    p_key = 'pressure_Torr'
    # filter for target pressure
    target_p = step['target']['target_pressure']
    filtered = []
    for r in rows:
        try:
            tmp = float(r[t_key])
            cov = float(r[cov_key])
            pres = float(r[p_key])
            if abs(pres - target_p) / max(1e-12, target_p) < 0.1:
                filtered.append((tmp, cov))
        except (ValueError, KeyError):
            continue
    if not filtered:
        return 0.0
    filtered.sort(key=lambda x: x[0])
    def nearest_temp(arr, t):
        best = None
        best_dist = float('inf')
        for tmp, cov in arr:
            d = abs(tmp - t)
            if d < best_dist:
                best_dist = d
                best = (tmp, cov)
        return best
    target = step.get('target', {})
    p_center = target['plateau_coverage_center']
    p_tol = target['plateau_coverage_tol']
    plateau_temps = target['plateau_temps']
    plateau_ok = 0
    for t in plateau_temps:
        pt = nearest_temp(filtered, t)
        if pt is not None and abs(pt[1] - p_center) <= p_tol:
            plateau_ok += 1
    if plateau_ok == len(plateau_temps):
        score += 0.4
    else:
        score += 0.4 * (plateau_ok / len(plateau_temps))
    low_t = target['low_temp']
    low_min = target['low_temp_coverage_min']
    low_pt = nearest_temp(filtered, low_t)
    if low_pt is not None and low_pt[1] >= low_min:
        score += 0.3
    high_t = target['high_temp']
    high_max = target['high_temp_coverage_max']
    high_pt = nearest_temp(filtered, high_t)
    if high_pt is not None and high_pt[1] <= high_max:
        score += 0.3
    return min(score, 1.0)


_SCORERS = {
    'step0-phase-diagram': score_0,
    'step1-heat-adsorption': score_1,
    'step2-adsorption-isobars': score_2,
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
