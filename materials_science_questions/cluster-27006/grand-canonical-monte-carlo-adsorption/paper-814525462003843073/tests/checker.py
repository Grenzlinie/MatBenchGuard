import os
import json
import csv

# === author imports / helpers ===
import os, math

def linreg(x, y):
    n = len(x)
    if n < 2:
        return 0.0, 0.0, 0.0
    sx = sum(x)
    sy = sum(y)
    sxx = sum(xi*xi for xi in x)
    sxy = sum(xi*yi for xi, yi in zip(x, y))
    denom = n*sxx - sx*sx
    if abs(denom) < 1e-12:
        return 0.0, 0.0, 0.0
    slope = (n*sxy - sx*sy) / denom
    intercept = (sy - slope*sx) / n
    ymean = sy / n
    ss_res = sum((yi - (slope*xi + intercept))**2 for xi, yi in zip(x, y))
    ss_tot = sum((yi - ymean)**2 for yi in y)
    r2 = 1 - ss_res/ss_tot if ss_tot != 0 else 0.0
    return slope, intercept, r2

def parse_isotherm(rows):
    """Convert list of dicts into a dict mapping temperature to sorted (pressure, loading) list."""
    temps = {}
    for r in rows:
        t = float(r['Temperature_K'])
        p = float(r['Fugacity_bar'])
        n = float(r['Loading_mmol_g'])
        temps.setdefault(t, []).append((p, n))
    for t in temps:
        temps[t].sort(key=lambda x: x[0])
    return temps

def sanity_check_isotherm(temps):
    # monotonic increase with pressure
    for t, pts in temps.items():
        for i in range(1, len(pts)):
            if pts[i][1] < pts[i-1][1] - 1e-6:
                return False
    # temperature ordering at a common low pressure (~0.1 bar)
    pressures = sorted({p for pts in temps.values() for p, _ in pts})
    if pressures:
        ref_p = min(pressures, key=lambda x: abs(x - 0.1))
        loadings = {}
        for t, pts in temps.items():
            best = min(pts, key=lambda x: abs(x[0] - ref_p))
            loadings[t] = best[1]
        if 273 in loadings and 283 in loadings and loadings[273] < loadings[283] - 1e-6:
            return False
        if 283 in loadings and 293 in loadings and loadings[283] < loadings[293] - 1e-6:
            return False
    return True

def compute_qst_from_isotherm(temps):
    henry = {}
    for t, pts in temps.items():
        low = [(p, n) for p, n in pts if p <= 0.1 and n > 0]
        if len(low) < 2:
            return None
        ps = [p for p, _ in low]
        ns = [n for _, n in low]
        slope, intercept, r2 = linreg(ps, ns)
        if slope <= 0:
            return None
        henry[t] = slope
    if len(henry) < 2:
        return None
    T_vals = sorted(henry.keys())
    lnK = [math.log(henry[t]) for t in T_vals]
    invT = [1.0 / t for t in T_vals]
    slope2, intercept2, r2_henry = linreg(invT, lnK)
    R = 8.314e-3  # kJ/(mol·K)
    return -R * slope2


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
    ni_rows = load_artifact(os.path.join(outputs_dir, 'step_01_isotherms_Ni.csv'))
    cu_rows = load_artifact(os.path.join(outputs_dir, 'step_02_isotherms_Cu.csv'))
    ni_temps = parse_isotherm(ni_rows) if ni_rows else {}
    cu_temps = parse_isotherm(cu_rows) if cu_rows else {}
    ni_sanity = sanity_check_isotherm(ni_temps) if ni_temps else False
    cu_sanity = sanity_check_isotherm(cu_temps) if cu_temps else False
    ni_qst = compute_qst_from_isotherm(ni_temps) if ni_temps else None
    cu_qst = compute_qst_from_isotherm(cu_temps) if cu_temps else None
    return {'ni_qst': ni_qst, 'ni_sanity': ni_sanity, 'cu_qst': cu_qst, 'cu_sanity': cu_sanity}


# === block: score_0 (check id='recompute_qst_ni') ===
def score_0(artifact, step, ctx):
    ni_qst = ctx.get('ni_qst')
    if ni_qst is None:
        return 0.0
    target = step.get('target', 32.8)
    tol = step.get('tolerance', 3.0)
    max_err = step.get('max_error', 15.0)
    diff = abs(ni_qst - target)
    if diff <= tol:
        qst_score = 1.0
    elif diff >= max_err:
        qst_score = 0.0
    else:
        qst_score = 1.0 - (diff - tol) / (max_err - tol)
    sanity_factor = 1.0 if ctx.get('ni_sanity', True) else 0.1
    return sanity_factor * qst_score


# === block: score_1 (check id='recompute_qst_cu') ===
def score_1(artifact, step, ctx):
    cu_qst = ctx.get('cu_qst')
    if cu_qst is None:
        return 0.0
    target = step.get('target', 33.5)
    tol = step.get('tolerance', 3.0)
    max_err = step.get('max_error', 15.0)
    diff = abs(cu_qst - target)
    if diff <= tol:
        qst_score = 1.0
    elif diff >= max_err:
        qst_score = 0.0
    else:
        qst_score = 1.0 - (diff - tol) / (max_err - tol)
    sanity_factor = 1.0 if ctx.get('cu_sanity', True) else 0.1
    return sanity_factor * qst_score


# === block: score_2 (check id='cross_check_reported_qst') ===
def score_2(artifact, step, ctx):
    data = artifact  # already loaded dict
    ni_reported = data.get('DICRO-3-Ni-i_zero_loading_Qst_kJmol')
    cu_reported = data.get('DICRO-3-Cu-i_zero_loading_Qst_kJmol')
    if ni_reported is None or cu_reported is None:
        return 0.0
    ni_qst = ctx.get('ni_qst')
    cu_qst = ctx.get('cu_qst')
    if ni_qst is None or cu_qst is None:
        return 0.0
    def sub_score(reported, recomputed):
        diff = abs(reported - recomputed)
        if diff <= 1.0:
            return 1.0
        if diff >= 5.0:
            return 0.0
        return 1.0 - (diff - 1.0) / 4.0
    s_ni = sub_score(ni_reported, ni_qst)
    s_cu = sub_score(cu_reported, cu_qst)
    return (s_ni + s_cu) / 2.0


_SCORERS = {
    'recompute_qst_ni': score_0,
    'recompute_qst_cu': score_1,
    'cross_check_reported_qst': score_2,
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
