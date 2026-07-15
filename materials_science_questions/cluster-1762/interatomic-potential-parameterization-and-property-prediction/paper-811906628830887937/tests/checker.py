import os
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
    import math
    import numpy as np

    hidden = spec.get("hidden_data", {})
    metals = hidden["metals"]
    fcc_w = hidden["fcc_w"]
    conv = hidden["conv_GPa_to_eV_A3"]

    # compute Möbius coefficients m(n) from w(n)
    nmax = len(fcc_w) - 1
    w = fcc_w
    m = [0.0] * (nmax + 1)
    m[1] = 1.0 / w[1]
    for k in range(2, nmax + 1):
        s = 0.0
        for d in range(1, k):
            if k % d == 0:
                s += m[d] * w[k // d]
        m[k] = -s / w[1]

    # precompute conversion factors and derived parameters per metal
    metal_params = {}
    for name, p in metals.items():
        a0 = p["a0"]
        C12 = p["C12"]
        C44 = p["C44"]
        Es = p["Es"]
        Ev = p["Ev"]
        B_GPa = p["B"]
        Omega = a0**3 / 4.0
        R1e = a0 / math.sqrt(2.0)
        dC = C12 - C44
        Es_minus_Ev = Es - Ev
        alpha = math.sqrt(18.0 * Omega * dC * conv / Es_minus_Ev) if Es_minus_Ev > 0 else 0.0
        n_e = 4.0 * (Es_minus_Ev)**2
        B_conv = B_GPa * conv
        sqrt_term = math.sqrt(9.0 * B_conv * Omega / Es) if Es > 0 else 0.0
        metal_params[name] = {
            "R1e": R1e,
            "alpha": alpha,
            "n_e": n_e,
            "Es": Es,
            "Es_minus_Ev": Es_minus_Ev,
            "sqrt_term": sqrt_term
        }

    # functions to evaluate lattice sums at a given R1 (nearest-neighbour distance)
    def S_rho(R1, params):
        return params["n_e"] * math.exp(-params["alpha"] * (R1 / params["R1e"] - 1.0))

    def E_TB(R1, params):
        return -2.0 * params["Es_minus_Ev"] * math.exp(-0.5 * params["alpha"] * (R1 / params["R1e"] - 1.0))

    def E_coh(R1, params):
        x = params["sqrt_term"] * (R1 / params["R1e"] - 1.0)
        return -params["Es"] * (1.0 + x) * math.exp(-x)

    def SigmaPhi(R1, params):
        return 2.0 * (E_coh(R1, params) - E_TB(R1, params))

    # inversion: compute f(r) = sum_n m(n) * F(sqrt(n)*r)
    def invert_rho(r, params):
        total = 0.0
        for n in range(1, nmax + 1):
            R = math.sqrt(n) * r
            total += m[n] * S_rho(R, params)
        return total

    def invert_phi(r, params):
        total = 0.0
        for n in range(1, nmax + 1):
            R = math.sqrt(n) * r
            total += m[n] * SigmaPhi(R, params)
        return total

    ctx = {
        "metals": metal_params,
        "m_array": m,
        "nmax": nmax,
        "invert_rho": invert_rho,
        "invert_phi": invert_phi
    }
    return ctx


# === block: score_0 (check id='step_csv_score') ===
def score_0(artifact, step, ctx):
    import math
    import csv
    from io import StringIO

    # artifact is a list of dicts loaded from the CSV; each dict has keys: metal, distance_R1, hopping_integral, pair_potential
    if not artifact or len(artifact) != 300:
        return 0.0

    metals_params = ctx["metals"]
    invert_rho = ctx["invert_rho"]
    invert_phi = ctx["invert_phi"]

    tolerance = step.get("params", {}).get("tolerance", 1e-5)

    rel_errors = []
    for row in artifact:
        metal = row["metal"].strip()
        if metal not in metals_params:
            return 0.0  # unknown metal
        params = metals_params[metal]
        try:
            r = float(row["distance_R1"])
            h_agent = float(row["hopping_integral"])
            phi_agent = float(row["pair_potential"])
        except (ValueError, KeyError):
            return 0.0
    
        rho_val = invert_rho(r, params)
        h_gold = math.sqrt(max(0.0, rho_val))
        phi_gold = invert_phi(r, params)
    
        # relative error with a floor to avoid division by zero
        denom_h = max(abs(h_gold), 1e-12)
        denom_phi = max(abs(phi_gold), 1e-12)
        err_h = abs(h_agent - h_gold) / denom_h
        err_phi = abs(phi_agent - phi_gold) / denom_phi
        rel_errors.append(max(err_h, err_phi))

    if not rel_errors:
        return 0.0

    mean_err = sum(rel_errors) / len(rel_errors)
    # score: 1.0 if mean_err <= tolerance, linearly decays to 0 at 5*tolerance
    if mean_err <= tolerance:
        score = 1.0
    else:
        score = max(0.0, 1.0 - (mean_err - tolerance) / (4.0 * tolerance))
    return score


_SCORERS = {
    'step_csv_score': score_0,
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
