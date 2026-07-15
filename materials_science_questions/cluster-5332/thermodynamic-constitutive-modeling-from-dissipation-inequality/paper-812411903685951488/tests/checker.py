import os
import json
import csv

# === author imports / helpers ===
import scipy.integrate
import scipy.optimize
import numpy as np


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
    def prepare(outputs_dir, spec):
        import scipy.integrate
        import scipy.optimize
        import numpy as np
        alphas = [1e-6,5e-6,1e-5,5e-5,1e-4,5e-4,1e-3,5e-3,1e-2,2e-2]
        def tau_in(T):
            U = 1.0/(825.0-T)
            return 10.0**(0.16095 + 70.2299*U + 10.0144*U*U)
        def temperature(t,alpha):
            return 20.0 + 780.0*np.exp(-alpha*t)
        def integrand_trad(t,alpha):
            T = temperature(t,alpha)
            return 1.0/tau_in(T)
        def integrand_gen(t,alpha):
            T = temperature(t,alpha)
            S = 1.083 - 0.00106*T
            return S * t**(S-1) / (tau_in(T)**S)
        def G(t, alpha, mode):
            if mode=='traditional':
                return scipy.integrate.quad(integrand_trad, 0, t, args=(alpha,), limit=200)[0]
            else:
                return scipy.integrate.quad(integrand_gen, 0, t, args=(alpha,), limit=200)[0]
        expected = {}
        for alpha in alphas:
            try:
                t_f = scipy.optimize.brentq(lambda t: G(t,alpha,'generalized')-1.0, 1e-6, 1e12, xtol=1e-12, rtol=1e-8, maxiter=1000)
                T_gen = temperature(t_f,alpha)
                expected[alpha] = T_gen
            except Exception:
                expected[alpha] = None
        return {'expected': expected}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        tol = step.get('tolerance_temperature', 2.0)
        sanity_tol = step.get('tolerance_traditional_plausibility', 50.0)
        expected = ctx.get('expected', {})
        if not isinstance(artifact, list) or len(artifact) != 10:
            return 0.0
        row_scores = []
        for row in artifact:
            if not isinstance(row, dict):
                row_scores.append(0.0)
                continue
            try:
                alpha = float(row['alpha'])
                T_trad = float(row['T_start_traditional'])
                T_gen = float(row['T_start_generalized'])
            except (KeyError, ValueError, TypeError):
                row_scores.append(0.0)
                continue
            exp = expected.get(alpha)
            if exp is None:
                row_scores.append(0.0)
                continue
            diff = abs(T_gen - exp)
            plaus = abs(T_trad - T_gen) <= sanity_tol
            if diff <= tol and plaus:
                row_scores.append(1.0)
            else:
                row_scores.append(0.0)
        return sum(row_scores) / 10.0


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
