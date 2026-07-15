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
    step = next(s for s in spec.get('steps', []) if s.get('id') == 'output_c_values')
    params = step['recompute_params']
    return params


# === block: score_0 (check id='output_c_values') ===
def score_0(artifact, step, ctx):
    # Load artifact and validate shape
    C_dict = None
    if isinstance(artifact, dict) and 'C_values' in artifact:
        C_dict = artifact['C_values']
    required_keys = ['1','2','3','4','6','24']
    if not C_dict or not all(k in C_dict for k in required_keys):
        return 0.0
    try:
        C_vals = {int(k): float(C_dict[k]) for k in required_keys}
    except (ValueError, TypeError):
        return 0.0

    # Unpack hidden reference parameters
    N1p0_V = float(ctx['N1p0_V_cm3'])
    V_over_A = float(ctx['V_over_A_cm'])
    d = float(ctx['d_cm'])
    D_s = float(ctx['D_s_cm2_s'])
    rho_s = float(ctx['rho_s_cm2_s'])

    # Compute monomer areal concentration (S=1)
    N1s_A = N1p0_V * V_over_A * math.exp(C_vals[1])

    # Compute attachment rate prefactor: Gamma_n = gamma_0 * sqrt(n) * N1s_A
    a0 = 1.0 / math.sqrt(math.pi * rho_s)
    beta = D_s / (4.0 * d)
    gamma_0 = 2.0 * math.pi * beta * a0

    # Build N_n^s/A for the given n using ideal-gas-mixture formalism
    n_list = sorted(C_vals.keys())
    Nn_A = {}
    sum_C = 0.0
    for n in n_list:
        if n == 1:
            Nn_A[1] = N1s_A
            sum_C = 0.0  # will be updated for n>1 below
        else:
            # accumulate sum of C(2..n)
            sum_C += C_vals[n]
            # Nn^s/A = (N1s/A)^n * (V_over_A)^{n-1} * exp(sum_{i=2}^n C(i)) / n!
            Nn_A[n] = (N1s_A ** n) * (V_over_A ** (n - 1)) * math.exp(sum_C) / math.factorial(n)

    # Determine critical cluster size n* via incremental free energy
    # n* is the largest n where C(n-1) - C(n) >= 0 (for n >= 2)
    n_star = 1
    diffs = [C_vals[n - 1] - C_vals[n] for n in n_list if n >= 2]
    last = 1
    for n in n_list:
        if n == 1:
            continue
        delta = C_vals[n - 1] - C_vals[n]
        if delta >= 0:
            last = n
        else:
            break
    n_star = last

    # Recompute nucleation rate J = 1 / Σ [1/(Γ_n * N_n/A)]
    J_inv = 0.0
    for n in n_list:
        Gamma_n = gamma_0 * math.sqrt(n) * N1s_A
        term = 1.0 / (Gamma_n * Nn_A[n])
        J_inv += term
    J = 1.0 / J_inv if J_inv > 0 else 0.0

    # Score n*: 1 if exactly 3, else 0
    n_star_score = 1.0 if n_star == 3 else 0.0

    # Score J: factor-of-5 band around paper value 1e23 cm^{-2}s^{-1}
    log10_J = math.log10(J) if J > 0 else -1e9
    # Acceptable log10 range: 22.3 .. 23.7 (factor 5)
    if 22.3 <= log10_J <= 23.7:
        J_score = 1.0
    elif 22.0 <= log10_J < 22.3 or 23.7 < log10_J <= 24.0:
        J_score = 0.5   # within factor 10
    else:
        J_score = 0.0

    # Combined score (weights: n* 0.4, J 0.6)
    score = n_star_score * 0.4 + J_score * 0.6
    return score


_SCORERS = {
    'output_c_values': score_0,
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
