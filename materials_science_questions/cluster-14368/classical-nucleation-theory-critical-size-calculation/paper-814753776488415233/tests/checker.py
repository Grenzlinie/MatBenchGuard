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
    import math

    # parameters in cgs Gaussian (energy in erg, length in cm, time in s)
    sigma_erg_cm2 = 500.0
    d0_cm = 1e-7
    E0_V_cm = 1e6
    E0_statV_cm = E0_V_cm / 299.792458
    Lambda = 2.0
    L_cm = 3e-4
    D_cm2_s = 1e-18
    T_K = 300.0
    k_B_erg_K = 1.380649e-16
    epsilon = 1.0
    Angstrom_per_cm = 1e8
    eV_to_erg = 1.602176634e-12

    def g_max_over_L():
        beta = 1.0
        gamma = 0.15
        def f(x):
            if x <= 0:
                return float('-inf')
            term = x * math.log(((1 + math.sqrt(1 + x*x))**2) / (4 * math.sqrt(1 + x*x)))
            return beta * x * math.exp(-gamma * term * term)
        lo, hi = 0.001, 20.0
        for _ in range(60):
            m1 = lo + 0.382 * (hi - lo)
            m2 = lo + 0.618 * (hi - lo)
            if f(m1) < f(m2):
                lo = m1
            else:
                hi = m2
        return (lo + hi) / 2.0

    ref = {}
    h0_cm = math.sqrt((math.pi * sigma_erg_cm2 * Lambda * d0_cm) / (epsilon * E0_statV_cm**2))
    ref['h0_nm'] = h0_cm * 1e7
    ref['W_eV'] = ((2.0/3.0) * math.pi * sigma_erg_cm2 * d0_cm * h0_cm) / eV_to_erg

    b_cm2_s_per_erg = D_cm2_s / (k_B_erg_K * T_K)
    ref['t0_s'] = (3.0 * Lambda) / (b_cm2_s_per_erg * epsilon * E0_statV_cm**2 * h0_cm)
    ref['tL_s'] = (3.0 * Lambda) / (b_cm2_s_per_erg * epsilon * E0_statV_cm**2 * L_cm)
    ref['growth_rate_Angstrom_per_s'] = (L_cm / ref['tL_s']) * Angstrom_per_cm
    ref['distribution_peak_h_over_L'] = g_max_over_L()

    return {'ref': ref}


# === block: score_0 (check id='step_01') ===
def score_0(artifact, step, ctx):
    import math

    tolerances = step.get('tolerances', {})
    ref = ctx.get('ref', {})
    if not isinstance(artifact, dict) or not ref:
        return 0.0

    score = 0.0
    n = 0
    for field, tol in tolerances.items():
        if field not in artifact or field not in ref:
            continue
        n += 1
        try:
            val = float(artifact[field])
        except (ValueError, TypeError):
            continue
        ref_val = float(ref[field])
        tol_type = tol.get('type', '')
        if tol_type == 'factor':
            factor = float(tol.get('factor', 1.0))
            if ref_val != 0 and factor > 0:
                ratio = val / ref_val
                if 1.0/factor <= ratio <= factor:
                    score += 1.0
        elif tol_type == 'absolute':
            abs_tol = float(tol.get('abs', 0.0))
            if abs(val - ref_val) <= abs_tol:
                score += 1.0

    if n > 0:
        score = score / n
    return score


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
