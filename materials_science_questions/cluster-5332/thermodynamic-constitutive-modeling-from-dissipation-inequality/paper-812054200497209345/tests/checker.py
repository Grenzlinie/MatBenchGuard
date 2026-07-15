import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os
from typing import Dict, Any, List


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
    gold = spec.get("gold", {})
    step_config = {}
    if spec.get("steps"):
        first_step = spec["steps"][0]
        step_config = first_step.get("config", {})
    return {
        "E1": gold.get("E1", 200e9),
        "M1": gold.get("M1", 1e-6),
        "H1": gold.get("H1", 20e9),
        "J1": gold.get("J1", 1e-6),
        "E2": gold.get("E2", 100e9),
        "M2": gold.get("M2", 5e-7),
        "H2": gold.get("H2", 10e9),
        "J2": gold.get("J2", 5e-7),
        "sigma": gold.get("sigma", 300e6),
        "sigma_y": gold.get("sigma_y", 250e6),
        "rel_tol": step_config.get("relative_tolerance", 1e-4),
        "bc_tol": step_config.get("boundary_tolerance", 1e-4),
        "bc_weight": step_config.get("boundary_weight", 0.1)
    }


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    # Extract parameters from ctx
    E1 = ctx["E1"]
    M1 = ctx["M1"]
    H1 = ctx["H1"]
    J1 = ctx["J1"]
    E2 = ctx["E2"]
    M2 = ctx["M2"]
    H2 = ctx["H2"]
    J2 = ctx["J2"]
    sigma = ctx["sigma"]
    sigma_y = ctx["sigma_y"]
    rel_tol = ctx["rel_tol"]
    bc_tol = ctx["bc_tol"]
    bc_weight = ctx["bc_weight"]

    # Internal length scales
    l1 = math.sqrt(M1 / E1)
    l2 = math.sqrt(M2 / E2)
    l1p = math.sqrt(J1 / H1)
    l2p = math.sqrt(J2 / H2)

    # Omega factors for general case
    Omega_e = (E2 - E1) / (E1 * l1 + E2 * l2)
    Omega_p = (H2 - H1) / (H1 * l1p + H2 * l2p)

    # Helper: reference strains for a single x point
    def general_ref(x, sign_val):
        if sign_val >= 0:
            eps_e = (sigma / E1) * (1.0 - Omega_e * l2 * math.exp(-x / l1))
            eps_p = ((sigma - sigma_y) / H1) * (1.0 - Omega_p * l2p * math.exp(-x / l1p))
        else:
            eps_e = (sigma / E2) * (1.0 + Omega_e * l1 * math.exp(x / l2))
            eps_p = ((sigma - sigma_y) / H2) * (1.0 + Omega_p * l1p * math.exp(x / l2p))
        return eps_e, eps_p

    def case1_ref(x):
        if x >= 0:
            eps_e = (sigma / E1) * (1.0 - math.exp(-x / l1))
            eps_p = ((sigma - sigma_y) / H1) * (1.0 - math.exp(-x / l1p))
        else:
            eps_e = 0.0
            eps_p = 0.0
        return eps_e, eps_p

    def case2_ref(x):
        if x > 0:
            eps_e = sigma / E1
            eps_p = (sigma - sigma_y) / H1
        else:
            eps_e = 0.0
            eps_p = 0.0
        return eps_e, eps_p

    def case3_ref(x):
        if x > 0:
            eps_e = sigma / E1
            eps_p = ((sigma - sigma_y) / H1) * (1.0 - math.exp(-x / l1p))
        else:
            eps_e = 0.0
            eps_p = 0.0
        return eps_e, eps_p

    def relative_ok(val, ref):
        return abs(val - ref) <= rel_tol * max(abs(ref), 1e-20)

    # Parse artifact: list of dicts expected
    rows = artifact
    # Validate presence of required columns in at least one row
    if not rows or not all(k in rows[0] for k in ('case', 'x', 'epsilon_e', 'epsilon_p')):
        return 0.0

    # Group rows by case
    cases_data = {}
    for r in rows:
        c = r['case']
        if c not in ('general', 'case1', 'case2', 'case3'):
            continue
        x_val = float(r['x'])
        ee = float(r['epsilon_e'])
        ep = float(r['epsilon_p'])
        cases_data.setdefault(c, []).append((x_val, ee, ep))

    # Ensure all expected cases are present
    expected_cases = ('general', 'case1', 'case2', 'case3')
    if any(c not in cases_data for c in expected_cases):
        return 0.0

    # Compute element‑wise match score for a case
    def element_score(case_name, data):
        n = len(data)
        if n == 0:
            return 0.0
        matches = 0
        for x_val, ee_agent, ep_agent in data:
            if case_name == 'general':
                sign_val = 1 if x_val >= 0 else -1
                ref_e, ref_p = general_ref(x_val, sign_val)
            elif case_name == 'case1':
                ref_e, ref_p = case1_ref(x_val)
            elif case_name == 'case2':
                ref_e, ref_p = case2_ref(x_val)
            else:  # case3
                ref_e, ref_p = case3_ref(x_val)
            if relative_ok(ee_agent, ref_e) and relative_ok(ep_agent, ref_p):
                matches += 1
        return matches / n

    # Compute boundary‑condition score for a case (revised to avoid false penalty at x=0)
    def boundary_score(case_name, data):
        if len(data) < 2:
            return 0.0
        if case_name == 'case1':
            # case1: strains must be zero at x=0 (continuous solution)
            xs = [t[0] for t in data]
            idx0 = min(range(len(xs)), key=lambda i: abs(xs[i]))
            e0 = data[idx0][1]
            p0 = data[idx0][2]
            err = max(abs(e0), abs(p0))
            return max(0.0, 1.0 - min(1.0, err / bc_tol))

        # For case2 and case3, the solution has a jump at x=0.
        # Check derivatives / values only on the positive side (x>0).
        pos_pts = [(x, ee, ep) for (x, ee, ep) in data if x > 0]
        if len(pos_pts) < 2:
            return 0.0
        # Sort positive points by x
        pos_pts.sort(key=lambda t: t[0])
        xs_pos = [t[0] for t in pos_pts]
        ee_pos = [t[1] for t in pos_pts]
        ep_pos = [t[2] for t in pos_pts]

        # Forward difference between the first two positive points
        dx = xs_pos[1] - xs_pos[0]
        if abs(dx) > 1e-30:
            de = (ee_pos[1] - ee_pos[0]) / dx
            dp = (ep_pos[1] - ep_pos[0]) / dx
        else:
            de = dp = 0.0

        if case_name == 'case2':
            # static HO constraints: both derivatives must be zero
            err = max(abs(de), abs(dp))
            return max(0.0, 1.0 - min(1.0, err / bc_tol))
        else:  # case3: e'=0 and p(0)=0
            # plastic strain at the first positive point
            p0 = ep_pos[0]
            err = max(abs(de), abs(p0))
            return max(0.0, 1.0 - min(1.0, err / bc_tol))

    # Collect scores per case
    elem_scores = []
    bc_scores = []
    for c in expected_cases:
        data = cases_data.get(c, [])
        if not data:
            return 0.0
        elem_scores.append(element_score(c, data))
        bc_scores.append(boundary_score(c, data))

    avg_elem = sum(elem_scores) / len(elem_scores)
    avg_bc = sum(bc_scores) / len(bc_scores)
    overall = avg_elem * (1.0 - bc_weight) + avg_bc * bc_weight
    return max(0.0, min(1.0, overall))


_SCORERS = {
    'step_01': score_0,
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
