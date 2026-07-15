import os
import json
import csv

# === author imports / helpers ===
import math
import csv
import os
import json


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
    ctx = {
        'sigma': 20.0,            # erg/cm^2
        'rho': 1.0,               # g/cm^3
        'delta_H_f': 3.34e9,      # erg/g
        'T_m': 273.0,             # K
        'k_B': 1.380649e-16,      # erg/K
        'K_prefactor': 1e20,      # cm^{-2} s^{-1}
        'm': 0.5,
        'beta': 0.001,
        'gamma': 0.8,
        'A0': 2.0e-15,            # cm^2
    }
    return ctx


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    import math

    def f_m_x(m, x):
        g = math.sqrt(1.0 + x*x - 2.0*m*x)
        if g == 0.0:
            return 0.0
        term1 = ((1.0 - m*x) / g)**3
        term2 = x**3 * (2.0 - 3.0*(x - m)/g + ((x - m)/g)**3)
        term3 = 3.0*m*x*x * ((x - m)/g - 1.0)
        return 0.5 * (1.0 + term1 + term2 + term3)

    def delta_G0_star(delta_T, sigma, rho, delta_H_f, T_m):
        # delta_T in K
        if delta_T <= 0:
            return float('inf')
        return (16.0*math.pi/3.0) * sigma**3 * T_m**2 / (delta_H_f**2 * delta_T**2 * rho**2)

    def r_star(delta_T, sigma, T_m, delta_H_f, rho):
        if delta_T <= 0:
            return float('inf')
        return 2.0 * sigma * T_m / (delta_H_f * delta_T * rho)   # cm

    def alpha_crit_from_T(T_K, R_cm, m, sigma, rho, delta_H_f, T_m, k_B, K_prefactor):
        delta_T = T_m - T_K
        if delta_T <= 0:
            return 0.0
        dG0 = delta_G0_star(delta_T, sigma, rho, delta_H_f, T_m)
        r_crit = r_star(delta_T, sigma, T_m, delta_H_f, rho)
        x = R_cm / r_crit
        f_val = f_m_x(m, x)
        dG_hetero_flat = dG0 * f_val
        dG_threshold = k_B * T_K * math.log(4.0 * math.pi * R_cm**2 * K_prefactor)
        if dG_threshold >= dG_hetero_flat:
            return 0.0   # particle active even without pit
        denom = R_cm**2 * (1.0 - m) * sigma
        if denom <= 0:
            return 0.0
        alpha = (dG_hetero_flat - dG_threshold) / denom
        return max(0.0, alpha)

    def N_pits(area, A0, beta, gamma):
        if area <= 0:
            return float('inf')
        x_pit = gamma * math.log(area / A0) - 1.0/(2.0*gamma)
        # exact erfc formula
        from math import erfc
        coeff = (beta / A0) * (math.sqrt(math.pi) / (2.0*gamma)) * math.exp(1.0/(2.0*gamma**2))
        return coeff * erfc(x_pit)

    def P_active(alpha, R_cm, A0, beta, gamma):
        area = alpha * R_cm**2
        N = N_pits(area, A0, beta, gamma)
        return 1.0 - math.exp(-4.0 * math.pi * R_cm**2 * N)

    def F_of_T(T_K, R_cm, m, sigma, rho, delta_H_f, T_m, k_B, K_prefactor, A0, beta, gamma):
        alpha_c = alpha_crit_from_T(T_K, R_cm, m, sigma, rho, delta_H_f, T_m, k_B, K_prefactor)
        return P_active(alpha_c, R_cm, A0, beta, gamma)

    def expected_T(R_angstrom, F_target, params):
        R_cm = R_angstrom * 1.0e-8
        # binary search for T in Kelvin
        T_lo = 230.0  # K
        T_hi = 273.0
        for _ in range(50):
            T_mid = (T_lo + T_hi) / 2.0
            F_mid = F_of_T(T_mid, R_cm, params['m'], params['sigma'], params['rho'],
                           params['delta_H_f'], params['T_m'], params['k_B'],
                           params['K_prefactor'], params['A0'], params['beta'], params['gamma'])
            if F_mid < F_target:
                T_hi = T_mid
            else:
                T_lo = T_mid
        return T_lo - 273.15   # convert to °C

    # artifact is list of dicts
    rows = artifact
    tolerance = 2.0
    correct = 0
    total = 0
    for row in rows:
        try:
            R = float(row['R_Angstrom'])
            F = float(row['F_fraction'])
            T_agent = float(row['T_Celsius'])
        except (ValueError, KeyError):
            continue
        expected = expected_T(R, F, ctx)
        if abs(T_agent - expected) <= tolerance:
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'step1': score_0,
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
