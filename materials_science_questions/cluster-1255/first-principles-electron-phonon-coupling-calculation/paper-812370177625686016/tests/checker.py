import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='step_results') ===
def score_0(artifact, step, ctx):
    cases_params = [
        {"case_id": "n2_generic", "lam": [0.30, 0.15], "omega": [50.0, 200.0], "alpha0": [0.5, 0.5]},
        {"case_id": "n2_coulomb", "lam": [0.45, -0.12], "omega": [60.0, 5000.0], "alpha0": [0.5, 0.0]},
        {"case_id": "n3_coulomb", "lam": [0.20, 0.10, -0.08], "omega": [30.0, 100.0, 1000.0], "alpha0": [0.5, 0.0, 0.0]},
        {"case_id": "case_a", "lam": [0.25, 0.35, -0.10], "omega": [40.0, 120.0, 600.0], "alpha0": [0.5, 0.5, 0.0]},
        {"case_id": "case_b", "lam": [0.35, 0.20, -0.10], "omega": [100.0, 250.0, 800.0], "alpha0": [0.5, 0.0, 0.0]},
    ]

    euler_gamma = 0.5772156649015328606
    factor = 2 * math.exp(euler_gamma) / math.pi

    def compute_tc_alpha(lam, omega, alpha0):
        n = len(lam)
        lam_star = [0.0] * (n + 1)
        for k in range(n, 1, -1):
            l_k = math.log(omega[k-1] / omega[k-2])
            lam_k1 = lam_star[k+1] if k < n else 0.0
            denom = 1.0 - (lam[k-1] + lam_k1) * l_k
            lam_star[k] = (lam[k-1] + lam_k1) / denom
        lam_tilde = lam[0] + lam_star[2]
        Tc = factor * omega[0] * math.exp(-1.0 / lam_tilde)
        Lambdas = [0.0] * (n + 2)
        Lambdas[1] = 1.0
        for k in range(2, n+1):
            prod = 1.0
            for l in range(1, k):
                ratio = lam_star[l+1] / (lam[l-1] + lam_star[l+1])
                prod *= ratio * ratio
            Lambdas[k] = prod
        Lambdas[n+1] = 0.0
        alpha = 0.0
        for k in range(1, n+1):
            C_k = Lambdas[k] - Lambdas[k+1]
            alpha += C_k * alpha0[k-1]
        return Tc, alpha

    if not isinstance(artifact, list) or len(artifact) != len(cases_params):
        return 0.0

    score_per_case = 0.0
    rel_tol = 1e-8
    abs_tol_alpha = 1e-8

    for case_param in cases_params:
        cid = case_param["case_id"]
        agent_entry = None
        for entry in artifact:
            if isinstance(entry, dict) and entry.get("case_id") == cid:
                agent_entry = entry
                break
        if agent_entry is None:
            continue
        Tc_a = agent_entry.get("Tc")
        alpha_a = agent_entry.get("alpha")
        if Tc_a is None or alpha_a is None:
            continue
        Tc_exp, alpha_exp = compute_tc_alpha(case_param["lam"], case_param["omega"], case_param["alpha0"])
        if abs(Tc_exp) > 1e-12:
            tc_pass = abs(Tc_a - Tc_exp) / abs(Tc_exp) <= rel_tol
        else:
            tc_pass = abs(Tc_a - Tc_exp) <= rel_tol * 1e-12
        alpha_pass = abs(alpha_a - alpha_exp) <= abs_tol_alpha
        if tc_pass and alpha_pass:
            score_per_case += 1.0

    return score_per_case / len(cases_params)


_SCORERS = {
    'step_results': score_0,
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
