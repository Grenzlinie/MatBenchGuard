import os
import json
import csv

# === author imports / helpers ===
import math
import json
import csv


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
    # Compute expected values from the analytical model
    n1 = 3.473
    n2 = 1.444
    lam0 = 1550e-9
    w = 600e-9
    d = 250e-9
    r = 136.13e-9
    t = 136.13e-9
    neff0 = 3.32
    neff1 = 2.83
    neff2 = 1.9
    neff_single = 2.93

    beta0 = 2 * math.pi * neff0 / lam0
    beta1 = 2 * math.pi * neff1 / lam0
    beta2 = 2 * math.pi * neff2 / lam0
    beta_s = 2 * math.pi * neff_single / lam0

    def rho_val(n): return (2 * math.pi / lam0) * math.sqrt(n1 ** 2 - n ** 2)
    def gamma_val(n): return (2 * math.pi / lam0) * math.sqrt(n ** 2 - n2 ** 2)

    rho0 = rho_val(neff0)
    gamma0 = gamma_val(neff0)
    rho1 = rho_val(neff1)
    gamma1 = gamma_val(neff1)
    rho2 = rho_val(neff2)
    gamma2 = gamma_val(neff2)
    rho_s = rho_val(neff_single)
    gamma_s = gamma_val(neff_single)

    def sinc(x):
        if abs(x) < 1e-12:
            return 1.0
        return math.sin(math.pi * x) / (math.pi * x)

    # zeta_2^0
    term_zeta = (rho2 ** 2 * sinc(0)) / (2 * beta2 * (w + 2 / gamma2))
    zeta2_0 = term_zeta * (math.sinh(gamma2 * t) / gamma2) * math.exp(-gamma2 * r)

    # iota^0
    term_iota = (rho_s ** 2 * sinc(0)) / (2 * beta_s * (d + 2 / gamma_s))
    iota_0 = term_iota * (math.sinh(gamma_s * t) / gamma_s) * math.exp(-gamma_s * r)

    # Grating period Lambda (in nm)
    Lambda = (2 * math.pi / (beta2 + beta_s + zeta2_0 + iota_0)) * 1e9

    # Lambda_min using Eq.33
    const_term = 1.0 / 328e-9
    prod_term = (rho2 ** 2 / (4 * beta2 * gamma2 * (w + 2 / gamma2))) * \
                (rho_s ** 2 / (4 * beta_s * gamma_s * (d + 2 / gamma_s)))
    Lambda_min = 1.0 / (const_term + (1.0 / (2 * math.pi)) * prod_term)   # meters
    L = 34 * Lambda_min   # coupling length

    # Kappa for mode 2, harmonic 1 (contra-directional)
    kappa2_1 = (rho2 * rho_s * sinc(0.5) / math.sqrt(beta2 * beta_s * (w + 2 / gamma2) * (d + 2 / gamma_s))) * \
               (math.sinh((gamma_s - gamma2) * t / 2) / (gamma_s - gamma2)) * \
               math.exp(-(gamma_s + gamma2) * r / 2)

    # Kappa for mode 1, harmonic 0 (co-directional)
    kappa1_0 = (rho1 * rho_s * sinc(0) / math.sqrt(beta1 * beta_s * (w + 2 / gamma1) * (d + 2 / gamma_s))) * \
               (math.sinh((gamma_s - gamma1) * t / 2) / (gamma_s - gamma1)) * \
               math.exp(-(gamma_s + gamma1) * r / 2)

    # varsigma_1
    varsigma1 = (rho1 * rho_s * (gamma1 + gamma_s) * math.exp(-gamma_s * r)) / \
                ((rho1 ** 2 + gamma_s ** 2) * math.sqrt(beta1 * beta_s * (w + 2 / gamma1) * (d + 2 / gamma_s)))

    kappa1_prime = kappa1_0 + varsigma1

    s1_co = abs(kappa1_prime)
    IL1_dB = 10 * math.log10(math.sin(s1_co * L) ** 2)

    s2_contra = abs(kappa2_1)
    IL2_dB = 10 * math.log10(math.tanh(s2_contra * L) ** 2)

    ctx = {
        'expected_Lambda_nm': Lambda,
        'expected_IL1_dB': IL1_dB,
        'expected_IL2_dB': IL2_dB
    }
    return ctx


# === block: score_0 (check id='grating_period') ===
def score_0(artifact, step, ctx):
    # Scorer for grating_period.txt
    import math
    val_str = artifact.strip()
    try:
        val = float(val_str)
    except (ValueError, TypeError):
        return 0.0
    expected = ctx['expected_Lambda_nm']
    tol = step.get('tolerance_abs', 1.0)
    diff = abs(val - expected)
    if diff <= tol:
        return 1.0
    # partial credit outside tolerance
    score = max(0.0, 1.0 - (diff - tol) / tol)
    return score


# === block: score_1 (check id='insertion_losses') ===
def score_1(artifact, step, ctx):
    # Scorer for insertion_losses.csv
    import csv
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    row = artifact[0]
    try:
        il1 = float(row.get('IL1_dB', ''))
        il2 = float(row.get('IL2_dB', ''))
    except (ValueError, TypeError):
        return 0.0
    tol = step.get('tolerance_abs', 0.5)
    def score_value(actual, expected):
        diff = abs(actual - expected)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / tol)
    s1 = score_value(il1, ctx['expected_IL1_dB'])
    s2 = score_value(il2, ctx['expected_IL2_dB'])
    return min(s1, s2)


_SCORERS = {
    'grating_period': score_0,
    'insertion_losses': score_1,
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
