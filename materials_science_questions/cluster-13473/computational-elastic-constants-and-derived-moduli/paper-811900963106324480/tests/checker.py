import os
import json
import csv

# === author imports / helpers ===
import math
from statistics import mean


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


# === block: score_0 (check id='elastic_moduli_trends') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    def pearson(x, y):
        n = len(x)
        if n < 2:
            return 0
        mx = mean(x)
        my = mean(y)
        cov = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n - 1)
        sx = math.sqrt(sum((xi - mx) ** 2 for xi in x) / (n - 1))
        sy = math.sqrt(sum((yi - my) ** 2 for yi in y) / (n - 1))
        if sx == 0 or sy == 0:
            return 0
        return cov / (sx * sy)

    # sort by d_nm
    rows_sorted = sorted(rows, key=lambda r: float(r['d_nm']))
    d_vals = [float(r['d_nm']) for r in rows_sorted]
    E_vals = [float(r['E_GPa']) for r in rows_sorted]
    nu_vals = [float(r['nu']) for r in rows_sorted]

    r_E = pearson(d_vals, E_vals)
    r_nu = pearson(d_vals, nu_vals)

    # trend score for E (should be negative)
    if r_E <= -0.9:
        trend_E_score = 1.0
    elif r_E >= -0.5:
        trend_E_score = 0.0
    else:
        trend_E_score = (abs(r_E) - 0.5) / 0.4

    # trend score for nu (should be positive)
    if r_nu >= 0.9:
        trend_nu_score = 1.0
    elif r_nu <= 0.5:
        trend_nu_score = 0.0
    else:
        trend_nu_score = (r_nu - 0.5) / 0.4

    # asymptote E
    large_E_rows = [r for r in rows_sorted if float(r['d_nm']) >= 6.0]
    if large_E_rows:
        mean_E = mean(float(r['E_GPa']) for r in large_E_rows)
        err_E = abs(mean_E - step['target_E'])
        asym_E_score = max(0.0, 1.0 - err_E / step['tol_E'])
    else:
        asym_E_score = 0.0

    # asymptote nu
    large_nu_rows = [r for r in rows_sorted if float(r['d_nm']) >= 5.0]
    if large_nu_rows:
        mean_nu = mean(float(r['nu']) for r in large_nu_rows)
        err_nu = abs(mean_nu - step['target_nu'])
        asym_nu_score = max(0.0, 1.0 - err_nu / step['tol_nu'])
    else:
        asym_nu_score = 0.0

    score = 0.3 * trend_E_score + 0.3 * asym_E_score + 0.2 * trend_nu_score + 0.2 * asym_nu_score
    return min(max(score, 0.0), 1.0)


# === block: score_1 (check id='stress_profile_qualitative') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    rows_sorted = sorted(rows, key=lambda r: float(r['position_nm']))
    center_row = rows_sorted[0]
    surface_row = rows_sorted[-1]
    sigma_center = float(center_row['sigma_zz_GPa'])
    sigma_surface = float(surface_row['sigma_zz_GPa'])

    score_center = 1.0 if sigma_center <= 0 else 0.0
    score_surface = 1.0 if sigma_surface > 0 else 0.0

    # trend: correlation between position and sigma
    pos_vals = [float(r['position_nm']) for r in rows_sorted]
    sig_vals = [float(r['sigma_zz_GPa']) for r in rows_sorted]
    def pearson(x, y):
        n = len(x)
        if n < 2:
            return 0
        mx = mean(x)
        my = mean(y)
        cov = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n - 1)
        sx = math.sqrt(sum((xi - mx) ** 2 for xi in x) / (n - 1))
        sy = math.sqrt(sum((yi - my) ** 2 for yi in y) / (n - 1))
        if sx == 0 or sy == 0:
            return 0
        return cov / (sx * sy)

    r = pearson(pos_vals, sig_vals)
    if r >= 0.7:
        trend_score = 1.0
    elif r > 0:
        trend_score = r / 0.7
    else:
        trend_score = 0.0

    # magnitude sanity
    max_abs = max(abs(s) for s in sig_vals)
    if max_abs < 5.0:
        mag_score = 1.0
    elif max_abs < 15.0:
        mag_score = 0.5
    else:
        mag_score = 0.0

    score = 0.3 * score_surface + 0.3 * score_center + 0.3 * trend_score + 0.1 * mag_score
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'elastic_moduli_trends': score_0,
    'stress_profile_qualitative': score_1,
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
