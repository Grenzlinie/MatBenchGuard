import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
        params_base = {"J0":0.8, "D":0.4, "K0":1.0, "zeta":1.2, "eta":0.8, "xi":1.25}

        def solve_mf(theta, h, params):
            J0, D, K0, zeta, xi, eta = params["J0"], params["D"], params["K0"], params["zeta"], params["xi"], params["eta"]
            m = 0.5
            q = 0.2
            for it in range(5000):
                if theta == 0:
                    return 1.0, 1.0/3.0
                A = (h + 2*J0*m) / theta
                B = (6*K0*q - D) / theta
                # clamp to avoid math.exp overflow
                A = max(-700.0, min(700.0, A))
                B = max(-700.0, min(700.0, B))
                if A > 100:
                    sinhA = math.exp(A)/2.0
                    coshA = math.exp(A)/2.0
                elif A < -100:
                    sinhA = -math.exp(-A)/2.0
                    coshA = math.exp(-A)/2.0
                else:
                    sinhA = math.sinh(A)
                    coshA = math.cosh(A)
                if B > 100:
                    expB = math.exp(B)
                elif B < -100:
                    expB = 0.0
                else:
                    expB = math.exp(B)
                denom = 1.0 + 2.0*coshA*expB
                m_new = 2.0*sinhA*expB / denom
                q_new = 1.0/3.0 - 1.0/denom
                change = max(abs(m_new - m), abs(q_new - q))
                m = 0.5*m + 0.5*m_new
                q = 0.5*q + 0.5*q_new
                if change < 1e-12:
                    break
                # Additional guard: if m or q become NaN/inf, break
                if math.isnan(m) or math.isinf(m) or math.isnan(q) or math.isinf(q):
                    m = 1.0
                    q = 1.0/3.0
                    break
            return float(m), float(q)

        def gap1(theta, h, params):
            m, q = solve_mf(theta, h, params)
            return 2*h + 4*m*(params["J0"] - params["zeta"]*params["K0"])

        def gap2(theta, h, params):
            m, q = solve_mf(theta, h, params)
            xi = params["xi"]
            zeta = params["zeta"]
            J0 = params["J0"]
            K0 = params["K0"]
            D = params["D"]
            a = m*m * (xi*J0 - zeta*K0)**2
            b = (D - 6*q*(K0 - xi*J0)) * (D - 6*q*(K0 - zeta*K0))
            rad = math.sqrt(max(0, a + b))
            return h + m*(2*J0 - xi*J0 - zeta*K0) - rad

        def trace_contour(gap_func, theta_min, theta_max, h_min, h_max, ntheta, nh, params):
            thetas = np.linspace(theta_min, theta_max, ntheta)
            hs = np.linspace(h_min, h_max, nh)
            pts = []
            for i in range(ntheta-1):
                for j in range(nh-1):
                    v00 = gap_func(thetas[i], hs[j], params)
                    v10 = gap_func(thetas[i+1], hs[j], params)
                    v01 = gap_func(thetas[i], hs[j+1], params)
                    v11 = gap_func(thetas[i+1], hs[j+1], params)
                    # horizontal edges
                    if v00 * v10 <= 0:
                        t = -v00 / (v10 - v00 + 1e-30)
                        pts.append((thetas[i] + t*(thetas[i+1]-thetas[i]), hs[j]))
                    if v01 * v11 <= 0:
                        t = -v01 / (v11 - v01 + 1e-30)
                        pts.append((thetas[i] + t*(thetas[i+1]-thetas[i]), hs[j+1]))
                    # vertical edges
                    if v00 * v01 <= 0:
                        t = -v00 / (v01 - v00 + 1e-30)
                        pts.append((thetas[i], hs[j] + t*(hs[j+1]-hs[j])))
                    if v10 * v11 <= 0:
                        t = -v10 / (v11 - v10 + 1e-30)
                        pts.append((thetas[i+1], hs[j] + t*(hs[j+1]-hs[j])))
            # clip to domain
            return [(t,h) for t,h in pts if theta_min < t < theta_max and h_min < h < h_max]

        # reference boundaries
        theta_min, theta_max = 0.001, 2.0
        h_min, h_max = -0.5, 2.0
        ref_pts_1 = trace_contour(gap1, theta_min, theta_max, h_min, h_max, 200, 200, params_base)
        ref_pts_2 = trace_contour(gap2, theta_min, theta_max, h_min, h_max, 200, 200, params_base)

        def compute_theta_c(zeta, h, base_params):
            par = base_params.copy()
            par["zeta"] = zeta
            lo, hi = 1e-5, 10.0
            for _ in range(40):
                mid = (lo+hi)/2.0
                g = gap1(mid, h, par)
                if g > 0:
                    hi = mid
                else:
                    lo = mid
                if hi - lo < 1e-8:
                    break
            return (lo+hi)/2.0

        return {"params": params_base, "gap1": gap1, "gap2": gap2, "ref_pts_1": ref_pts_1, "ref_pts_2": ref_pts_2, "compute_theta_c": compute_theta_c}


# === block: score_0 (check id='step_1_stability') ===
def score_0(artifact, step, ctx):
    import math

    artifact_rows = artifact  # list of dicts
    GAP_TOL = step['params']['gap_tol']
    DIST_TOL = step['params']['dist_tol']

    total = 0
    gaps = []
    points_by_type = {1:[], 2:[]}
    for row in artifact_rows:
        try:
            theta = float(row['reduced_temperature'])
            h = float(row['reduced_field'])
            btype = int(row['boundary_type'])
        except:
            continue
        if btype == 1:
            g = ctx['gap1'](theta, h, ctx['params'])
        elif btype == 2:
            g = ctx['gap2'](theta, h, ctx['params'])
        else:
            continue
        gaps.append((btype, theta, h, g))
        total += 1

    if total == 0:
        return 0.0

    # fraction of valid points
    valid_points = {1:[], 2:[]}
    valid_counts = 0
    for btype, theta, h, g in gaps:
        if abs(g) < GAP_TOL:
            valid_points[btype].append((theta, h))
            valid_counts += 1
    f_valid = valid_counts / total

    # coverage score per type
    coverage_scores = []
    for btype, ref_pts in [(1, ctx['ref_pts_1']), (2, ctx['ref_pts_2'])]:
        vpts = valid_points[btype]
        if not ref_pts:
            sc = 1.0
        elif not vpts:
            sc = 0.0
        else:
            max_dist = 0.0
            for rt, rh in ref_pts:
                min_d = min(math.sqrt((rt-t)**2 + (rh-h)**2) for t,h in vpts)
                if min_d > max_dist:
                    max_dist = min_d
            sc = max(0.0, 1.0 - max_dist / DIST_TOL)
        coverage_scores.append(sc)
    coverage = sum(coverage_scores) / len(coverage_scores) if coverage_scores else 0.0

    return float(f_valid * coverage)


# === block: score_1 (check id='step_2_zeta') ===
def score_1(artifact, step, ctx):
    import numpy as np

    ATOL = step['params']['atol']
    errors = []
    for row in artifact:
        try:
            zeta = float(row['zeta'])
            theta_agent = float(row['reduced_temperature'])
            h = float(row['reduced_field'])
        except:
            continue
        theta_ref = ctx['compute_theta_c'](zeta, h, ctx['params'])
        err = abs(theta_agent - theta_ref)
        errors.append(max(0.0, 1.0 - err / ATOL))
    if errors:
        return float(np.mean(errors))
    else:
        return 0.0


_SCORERS = {
    'step_1_stability': score_0,
    'step_2_zeta': score_1,
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
