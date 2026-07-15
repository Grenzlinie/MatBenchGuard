import os
import json
import csv

# === author imports / helpers ===
import json

# optional imports for scorers that need numeric fitting
np = None
curve_fit = None
try:
    import numpy as np
except ImportError:
    pass
try:
    from scipy.optimize import curve_fit
except ImportError:
    pass


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
    reference = spec.get('reference_values', {})
    tolerance = spec.get('tolerance_abs', 5.0)
    return dict(reference=reference, tolerance=tolerance)


# === block: score_0 (check id='kappa') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    ref = step.get('reference_values', {})
    tol = float(step.get('tolerance_abs', 5.0))
    if not rows:
        return 0.0
    # map temperatures to values
    data = {}
    for r in rows:
        t = int(r['T_K'])
        v = float(r['kappa_W_mK'])
        data[t] = v
    # target temperatures
    targets = [300,400,500,600,700,800]
    # check if all present
    present = all(t in data for t in targets)
    if not present:
        return 0.0
    # compute average distance score
    scores = []
    for t in targets:
        val = data[t]
        gold = ref.get(str(t), None)
        if gold is None:
            continue
        diff = abs(val - gold)
        s = max(0.0, 1.0 - diff/tol)
        scores.append(s)
    avg_score = sum(scores)/len(scores) if scores else 0.0
    # monotonic decrease check: for t1<t2, val(t1) > val(t2)
    vals = [data[t] for t in sorted(targets)]
    monotonic = all(vals[i] >= vals[i+1] for i in range(len(vals)-1))
    if not monotonic:
        avg_score *= 0.5  # penalty
    return avg_score


# === block: score_1 (check id='fit_params') ===
def score_1(artifact, step, ctx):
    import os
    import numpy as np
    # structural checks (weight 0.4)
    struct_score = 0.0
    checks = step.get('structural_checks', {})
    if isinstance(artifact, dict):
        A1 = float(artifact.get('A1', 0))
        A2 = float(artifact.get('A2', 0))
        tau1 = float(artifact.get('tau1_ps', 0))
        tau2 = float(artifact.get('tau2_ps', 0))
        K0 = float(artifact.get('K0', 0))
        struct_pass = 0.0
        total_struct_checks = 0
        if checks.get('all_positive'):
            if all(v>0 for v in [A1,A2,tau1,tau2,K0]):
                struct_pass += 1
            total_struct_checks += 1
        if checks.get('tau1_less_than_tau2'):
            if tau1 < tau2:
                struct_pass += 1
            total_struct_checks += 1
        if 'A1_A2_sum_range' in checks:
            lo, hi = checks['A1_A2_sum_range']
            if lo <= (A1 + A2) <= hi:
                struct_pass += 1
            total_struct_checks += 1
        struct_score = struct_pass / max(1, total_struct_checks) if total_struct_checks else 1.0
    else:
        struct_score = 0.0

    # refit consistency (weight 0.6)
    refit_score = 0.0
    csv_file = step.get('refit_from_csv', '')
    csv_path = os.path.join('/app/outputs', csv_file)
    if os.path.exists(csv_path):
        import csv
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if rows:
            t = np.array([float(r['t_ps']) for r in rows])
            g = np.array([float(r['g_t']) for r in rows])
            # double-exponential model
            def model(t, A1, tau1, A2, tau2):
                return A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)
            # initial guess
            p0 = [0.4, 3.0, 0.6, 30.0]
            try:
                popt, _ = curve_fit(model, t, g, p0=p0, maxfev=10000)
                fit_A1, fit_tau1, fit_A2, fit_tau2 = popt
                # compare relative errors
                rel_err_A1 = abs(A1 - fit_A1) / (abs(fit_A1) + 1e-9)
                rel_err_tau1 = abs(tau1 - fit_tau1) / (abs(fit_tau1) + 1e-9)
                rel_err_A2 = abs(A2 - fit_A2) / (abs(fit_A2) + 1e-9)
                rel_err_tau2 = abs(tau2 - fit_tau2) / (abs(fit_tau2) + 1e-9)
                avg_rel_err = (rel_err_A1 + rel_err_tau1 + rel_err_A2 + rel_err_tau2) / 4.0
                tol_rel = step.get('tolerance_params_rel', 0.3)
                refit_score = max(0.0, 1.0 - avg_rel_err/tol_rel)
            except Exception:
                refit_score = 0.0
    else:
        # csv missing: only structural counts
        refit_score = struct_score  # use struct as fallback

    return 0.4 * struct_score + 0.6 * refit_score


_SCORERS = {
    'kappa': score_0,
    'fit_params': score_1,
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
