import os
import json
import csv

# === author imports / helpers ===
import math
try:
    import numpy as np
except ImportError:
    np = None


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


# === block: score_0 (check id='band_dispersion') ===
def score_0(artifact, step, ctx):
    import math

    def _ls_fit(xs, ys):
        n = len(xs)
        sx = sum(xs)
        sy = sum(ys)
        sxx = sum(x*x for x in xs)
        sxy = sum(x*y for x,y in zip(xs, ys))
        det = n * sxx - sx * sx
        if abs(det) < 1e-12:
            return 0.0, 0.0
        slope = (n * sxy - sx * sy) / det
        intercept = (sxx * sy - sx * sxy) / det
        return slope, intercept

    def _r2(xs, ys, slope, intercept):
        mean_y = sum(ys) / len(ys)
        ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
        ss_tot = sum((y - mean_y) ** 2 for y in ys)
        if ss_tot < 1e-12:
            return 0.0
        return 1.0 - ss_res / ss_tot

    kappas = []
    upper = []
    lower = []
    for row in artifact:
        try:
            kappas.append(float(row["kappa"]))
            upper.append(float(row["beta_upper"]))
            lower.append(float(row["beta_lower"]))
        except Exception:
            continue
    if not kappas:
        return 0.0

    # index of kappa closest to 0
    idx0 = 0
    min_abs = abs(kappas[0])
    for i, k in enumerate(kappas):
        a = abs(k)
        if a < min_abs:
            min_abs = a
            idx0 = i

    gap = abs(upper[idx0] - lower[idx0])
    if gap < 0.01:
        gap_score = 1.0
    else:
        gap_score = max(0.0, 1.0 - (gap - 0.01) / 0.04)

    # linearity near kappa = 0: points with kappa <= 0.2
    k_lin = [k for k in kappas if k <= 0.2]
    u_lin = [u for k, u in zip(kappas, upper) if k <= 0.2]
    l_lin = [l for k, l in zip(kappas, lower) if k <= 0.2]

    if len(k_lin) >= 3:
        slope_u, intercept_u = _ls_fit(k_lin, u_lin)
        slope_l, intercept_l = _ls_fit(k_lin, l_lin)
        r2_u = _r2(k_lin, u_lin, slope_u, intercept_u)
        r2_l = _r2(k_lin, l_lin, slope_l, intercept_l)
        opposite = (slope_u * slope_l) < 0
        intercept_diff = abs(intercept_u - intercept_l)
        linear_ok = opposite and intercept_diff < 0.01 and r2_u > 0.9 and r2_l > 0.9
        linearity_score = 1.0 if linear_ok else 0.0
    else:
        linearity_score = 0.0

    return 0.4 * gap_score + 0.6 * linearity_score


# === block: score_1 (check id='surface_existence') ===
def score_1(artifact, step, ctx):
    def compute_r(eta, Z):
        if Z == 0:
            if eta < -1:
                r = -1.0 / eta
                return [r], [abs(r)]
            else:
                return [], []
        term = (eta**3) / (Z**2) - eta
        disc = term**2 + 4.0 * (eta / Z)**2
        sqrt_disc = math.sqrt(disc)
        r_plus = 0.5 * (term + sqrt_disc)
        r_minus = 0.5 * (term - sqrt_disc)
        return [r_plus, r_minus], [abs(r_plus), abs(r_minus)]

    # generate expected grid points
    eta_start, eta_end, eta_step = -2.0, -0.5, 0.1
    Z_start, Z_end, Z_step = -2.0, 2.0, 0.1
    eta_vals = []
    e = eta_start
    while e <= eta_end + 1e-9:
        eta_vals.append(round(e, 10))
        e += eta_step
    Z_vals = []
    z = Z_start
    while z <= Z_end + 1e-9:
        Z_vals.append(round(z, 10))
        z += Z_step

    expected = {}
    for e in eta_vals:
        for z in Z_vals:
            r_vals, r_abs = compute_r(e, z)
            if r_vals:
                valid = [a for a in r_abs if a < 1.0]
                if valid:
                    exists = 1
                    r_mag = min(valid)
                else:
                    exists = 0
                    r_mag = max(r_abs)
            else:
                exists = 0
                r_mag = 1.0
            expected[(round(e,6), round(z,6))] = exists

    total = len(expected)
    if total == 0:
        return 0.0
    artifact_dict = {}
    for row in artifact:
        try:
            eta = float(row['eta'])
            Z = float(row['Z'])
            exists = int(row['exists'])
            artifact_dict[(round(eta,6), round(Z,6))] = exists
        except:
            continue
    matched = 0
    for key, e_exists in expected.items():
        if key in artifact_dict and artifact_dict[key] == e_exists:
            matched += 1
    return matched / total


_SCORERS = {
    'band_dispersion': score_0,
    'surface_existence': score_1,
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
