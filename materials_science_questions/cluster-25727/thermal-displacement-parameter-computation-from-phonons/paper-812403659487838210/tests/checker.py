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


# === block: score_0 (check id='csv_recompute') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    if not artifact_rows:
        return 0.0

    # constants
    delta_meV = 3.5
    kB_meV_K = 8.617333262e-2
    a_RT = 4.0682
    alpha = 1.4e-5
    T_room = 298.0
    a0 = a_RT / (1.0 + alpha * T_room)
    N_e = 10
    g = 2
    levels = [i*delta_meV for i in range(10)]

    def fermi(E, mu, kBT):
        if kBT <= 0.0:
            return 1.0 if E < mu else 0.0
        return 1.0 / (1.0 + math.exp((E - mu) / kBT))

    def total_electrons(mu, kBT):
        return sum(g * fermi(E, mu, kBT) for E in levels)

    def find_mu(T):
        kBT = kB_meV_K * T
        if T < 1e-3:
            return 4.5 * delta_meV
        lo = -10.0
        hi = 10.0 * delta_meV + 10.0
        for _ in range(100):
            mid = (lo + hi) * 0.5
            ne = total_electrons(mid, kBT)
            if ne < N_e:
                lo = mid
            else:
                hi = mid
        return (lo + hi) * 0.5

    def dU_dR(T):
        kBT = kB_meV_K * T
        if T < 1e-3:
            return 0.0
        mu = find_mu(T)
        sum_S = 0.0
        for E in levels:
            fv = fermi(E, mu, kBT)
            term = E * fv - (E**2 * fv * (1.0 - fv)) / kBT
            sum_S += g * term
        return (3.0 * N_e / a0) * sum_S

    # scaling constant C such that da*/dT = 0 at 125 K
    dU124 = dU_dR(124.0)
    dU126 = dU_dR(126.0)
    d_neg_dT = ((-dU126) - (-dU124)) / 2.0
    C = - a0 * alpha / d_neg_dT

    # build reference map
    ref = {}
    for row in artifact_rows:
        T = float(row['temperature_K'])
        dU = dU_dR(T)
        neg_dU = -dU
        a_ref = a0 * (1.0 + alpha * T) + C * neg_dU
        ref[T] = a_ref

    # relative errors
    rel_errs = []
    a_vals = []
    for row in artifact_rows:
        T = float(row['temperature_K'])
        a = float(row['a_star_Angstrom'])
        a_ref = ref[T]
        err = abs(a - a_ref) / a_ref if a_ref != 0 else abs(a - a_ref)
        rel_errs.append(err)
        a_vals.append((T, a))

    max_re = max(rel_errs) if rel_errs else 1.0
    rel_tol = float(step.get('rel_error_tol', 0.10))
    if max_re <= rel_tol:
        rel_score = 1.0
    else:
        rel_score = max(0.0, 1.0 - (max_re - rel_tol) / 0.20)

    # minimum location: find T where a_star is maximal
    max_a = None
    T_max = None
    for T, a in a_vals:
        if max_a is None or a > max_a:
            max_a = a
            T_max = T
    if T_max is None:
        min_score = 0.0
    else:
        lo = float(step.get('min_temp_tolerance_low', 110))
        hi = float(step.get('min_temp_tolerance_high', 140))
        if lo <= T_max <= hi:
            min_score = 1.0
        else:
            dist = min(abs(T_max - lo), abs(T_max - hi))
            min_score = max(0.0, 1.0 - dist / 20.0)

    # trend signs
    def fit_slope(ts, vs):
        n = len(ts)
        if n < 2:
            return 0.0
        sx = sum(ts)
        sy = sum(vs)
        sxx = sum(t*t for t in ts)
        sxy = sum(t*v for t,v in zip(ts, vs))
        denom = n*sxx - sx*sx
        if denom == 0:
            return 0.0
        return (n*sxy - sx*sy) / denom

    low_range = step.get('low_temp_range', [0, 100])
    high_range = step.get('high_temp_range', [150, 390])
    low_pts = [(T,a) for T,a in a_vals if low_range[0] <= T <= low_range[1]]
    high_pts = [(T,a) for T,a in a_vals if high_range[0] <= T <= high_range[1]]
    low_slope = fit_slope([T for T,a in low_pts], [a for T,a in low_pts])
    high_slope = fit_slope([T for T,a in high_pts], [a for T,a in high_pts])
    exp_low = step.get('trend_sign_low', 'positive_expansion')
    trend = 0.0
    if exp_low == 'positive_expansion':
        if low_slope > 0:
            trend += 1.0
    else:
        if low_slope < 0:
            trend += 1.0
    if high_slope < 0:
        trend += 1.0
    trend_score = trend / 2.0

    final_score = 0.5 * rel_score + 0.3 * min_score + 0.2 * trend_score
    return final_score


_SCORERS = {
    'csv_recompute': score_0,
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
