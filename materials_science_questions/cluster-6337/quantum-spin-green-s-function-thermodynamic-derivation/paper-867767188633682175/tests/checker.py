import os
import json
import csv

# === author imports / helpers ===
import os
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import erf, exp1


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
    output_dir = outputs_dir
    filepath = os.path.join(output_dir, "bloch_vector_results.json")
    with open(filepath) as f:
        artifact = json.load(f)

    g = 1.0
    beta = 5.0
    mu = 0.4
    Delta = 0.5
    gbeta = g * beta
    lam3_0 = 0.5
    lam1_0 = 0.375
    lam2_0 = 0.375
    t_arr = np.array(artifact["t"])

    # Compute Z_bar
    Z_bar = 2 * np.sqrt(2) / ((2 + gbeta) * np.sqrt(2 + gbeta * Delta))
    prefactor_eta = 8.0 / Z_bar

    def eta_integrand(r, t):
        return np.exp(-(2 + gbeta) * r**2) * (r**2 / (mu**2 + r**2)) * (np.sin(t * np.sqrt(mu**2 + r**2)) ** 2)

    eta_vals = []
    for t in t_arr:
        I, _ = quad(eta_integrand, 0, np.inf, args=(t,), limit=200)
        eta = prefactor_eta * I
        eta_vals.append(eta)
    eta_vals = np.array(eta_vals)
    expected_lambda3 = lam3_0 * (1 - eta_vals)

    # zeta, xi analytic
    sg = np.sqrt(2 + gbeta)
    arg = mu * (2 + gbeta)
    def zeta_xi(t):
        z1 = (arg + 1j * t) / sg
        z2 = (arg - 1j * t) / sg
        exp_factor = np.exp((2 + gbeta) * mu**2 - t**2 / (2 + gbeta))
        zeta = np.cos(2 * mu * t) + (1j * t / 2) * np.sqrt(np.pi / (2 + gbeta)) * exp_factor * (erf(z1) - erf(z2))
        if np.iscomplexobj(zeta):
            zeta = zeta.real
        xi = (1j * mu / 2) * np.sqrt(np.pi * (2 + gbeta)) * exp_factor * (erf(z1) - erf(z2))
        if np.iscomplexobj(xi):
            xi = xi.real
        return float(zeta.real), float(xi.real)

    expected_lambda1 = np.zeros(len(t_arr))
    for i, t in enumerate(t_arr):
        zeta_t, xi_t = zeta_xi(t)
        eta_t = eta_vals[i]
        lam1 = lam1_0 * (zeta_t + 0.5 * eta_t) + lam2_0 * xi_t
        expected_lambda1[i] = lam1

    expected_eta_inf = mu**2 * (2 + gbeta) * np.exp(mu**2 * (2 + gbeta)) * exp1(mu**2 * (2 + gbeta))
    expected_tau = np.sqrt((2 + gbeta) / 1.0)
    gaussian_ratio = np.exp(-2 * 0.5**2 / (2 + gbeta))

    ctx = {
        "expected_lambda3": expected_lambda3,
        "expected_lambda1": expected_lambda1,
        "expected_eta_inf": expected_eta_inf,
        "expected_tau": expected_tau,
        "gaussian_ratio": gaussian_ratio
    }
    return ctx


# === block: score_0 (check id='lambda3_check') ===
def score_0(artifact, step, ctx):
    submitted = np.array(artifact['lambda3'])
    expected = ctx['expected_lambda3']
    tolerance = step.get('tolerance', 0.05)
    diffs = np.abs(submitted - expected)
    score = np.mean(diffs <= tolerance)
    return float(score)


# === block: score_1 (check id='lambda1_check') ===
def score_1(artifact, step, ctx):
    submitted = np.array(artifact['lambda1'])
    expected = ctx['expected_lambda1']
    diffs = np.abs(submitted - expected)
    score = np.mean(diffs <= 0.05)
    return float(score)


# === block: score_2 (check id='eta_inf_check') ===
def score_2(artifact, step, ctx):
    val = artifact['eta_inf']
    if abs(val - ctx['expected_eta_inf']) <= 0.1:
        return 1.0
    else:
        return 0.0


# === block: score_3 (check id='tau_check') ===
def score_3(artifact, step, ctx):
    val = artifact['tau']
    if abs(val - ctx['expected_tau']) <= 0.1:
        return 1.0
    else:
        return 0.0


# === block: score_4 (check id='short_time_consistency_check') ===
def score_4(artifact, step, ctx):
    t = artifact['t']
    lam3 = artifact['lambda3']
    if len(t) >= 2 and t[0] == 0.0 and t[1] == 0.5:
        ratio = lam3[1] / lam3[0] if lam3[0] != 0 else 0.0
        if abs(ratio - ctx['gaussian_ratio']) <= 0.05:
            return 1.0
    return 0.0


_SCORERS = {
    'lambda3_check': score_0,
    'lambda1_check': score_1,
    'eta_inf_check': score_2,
    'tau_check': score_3,
    'short_time_consistency_check': score_4,
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
