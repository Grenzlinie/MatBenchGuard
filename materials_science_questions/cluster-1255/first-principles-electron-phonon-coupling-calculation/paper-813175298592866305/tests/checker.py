import os
import json
import csv

# === author imports / helpers ===
import json, math, os


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
    steps = spec.get('steps', [])
    step = next(s for s in steps if s['id'] == 'results')
    rubric = step['rubric']
    return {'golds': rubric}


# === block: score_0 (check id='results') ===
def score_0(artifact, step, ctx):
    artifact_path = os.path.join('/app/outputs', 'results.json')
    if not os.path.exists(artifact_path):
        return 0.0
    with open(artifact_path) as f:
        data = json.load(f)
    suspended = data.get('suspended')
    supported = data.get('supported')
    if not suspended or not supported:
        return 0.0

    def trapz(y, x):
        n = len(x)
        if n < 2:
            return 0.0
        total = 0.0
        for i in range(n-1):
            total += (y[i] + y[i+1]) * (x[i+1] - x[i]) / 2.0
        return total

    def compute_lambda(omega, alpha2F):
        n = len(omega)
        integrand = [a / w for a, w in zip(alpha2F, omega)]
        lam = 2.0 * trapz(integrand, omega)
        return lam

    def compute_log_avg(omega, alpha2F, lam):
        if lam == 0:
            return 0.0
        integrand = [a * math.log(w) / w for a, w in zip(alpha2F, omega)]
        integral = trapz(integrand, omega)
        log_avg = math.exp(2.0 / lam * integral)
        return log_avg

    def score_system(sys_data, golds, cons_lam_tol, cons_log_tol):
        required = ('omega','alpha2F','lambda','log_avg_freq','Tc','delta_sc')
        if not all(k in sys_data for k in required):
            return 0.0
        omega = sys_data['omega']
        alpha = sys_data['alpha2F']
        reported_lam = sys_data['lambda']
        reported_log = sys_data['log_avg_freq']
        reported_Tc = sys_data['Tc']
        reported_delta = sys_data['delta_sc']

        rec_lam = compute_lambda(omega, alpha)
        rec_log = compute_log_avg(omega, alpha, rec_lam)

        lam_cons = abs(reported_lam - rec_lam) <= cons_lam_tol
        log_cons = abs(reported_log - rec_log) <= cons_log_tol
        consistency_score = 1.0 if (lam_cons and log_cons) else 0.0

        g_lam, g_lam_tol = golds['lambda'], golds['lambda_tol']
        g_log, g_log_tol = golds['log_avg_freq'], golds['log_avg_freq_tol']
        g_Tc, g_Tc_tol = golds['Tc'], golds['Tc_tol']
        g_delta, g_delta_tol = golds['delta_sc'], golds['delta_sc_tol']

        lam_match = 1.0 if abs(reported_lam - g_lam) <= g_lam_tol else 0.0
        log_match = 1.0 if abs(reported_log - g_log) <= g_log_tol else 0.0
        Tc_match = 1.0 if abs(reported_Tc - g_Tc) <= g_Tc_tol else 0.0
        delta_match = 1.0 if abs(reported_delta - g_delta) <= g_delta_tol else 0.0

        score = (lam_match * 0.3 +
                 log_match * 0.2 +
                 Tc_match * 0.3 +
                 delta_match * 0.1 +
                 consistency_score * 0.1)
        return score

    golds = ctx['golds']
    cons_lam_tol = golds['consistency_tol_lambda']
    cons_log_tol = golds['consistency_tol_log_avg']

    susp_score = score_system(suspended, golds['suspended'], cons_lam_tol, cons_log_tol)
    supp_score = score_system(supported, golds['supported'], cons_lam_tol, cons_log_tol)
    overall = (susp_score + supp_score) / 2.0
    return overall


_SCORERS = {
    'results': score_0,
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
