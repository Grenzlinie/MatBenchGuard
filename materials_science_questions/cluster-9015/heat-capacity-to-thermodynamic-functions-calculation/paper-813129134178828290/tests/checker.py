import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    for step in spec.get('steps', []):
        if step['id'] == 'thermodynamic_functions':
            return {'config': step.get('parameters', {})}
    return {}


# === block: score_0 (check id='thermodynamic_functions') ===
def score_0(artifact, step, ctx):
    config = ctx.get('config', {})
    if not config:
        return 0.0

    coeffs = config['polynomial_coefficients']
    S0 = float(config['standard_entropy_298_15'])
    T0 = float(config['reference_temperature'])
    step = float(config['integration_step'])
    T_start = int(config['temperature_grid']['start'])
    T_end = int(config['temperature_grid']['end'])
    T_step = int(config['temperature_grid']['step'])
    tol_Cp = float(config['tolerances']['Cp_rel'])
    tol_H = float(config['tolerances']['H_rel'])
    tol_S = float(config['tolerances']['S_rel'])

    # piecewise Cp function using paper's coefficients
    a = coeffs['range1_200_500']
    b = coeffs['range2_500_573']
    c = coeffs['range3_573_700']

    def cp(T):
        if T <= 500.0:
            return a[0] + a[1]*T + a[2]*T*T + a[3]*T*T*T
        elif T <= 573.0:
            return b[0] + b[1]*T + b[2]*T*T + b[3]/(T*T)
        else:
            return c[0] + c[1]*T + c[2]*T*T

    # generate fine grid and integrate
    T_fine = []
    cp_fine = []
    T = T_start
    while T <= T_end + 1e-12:
        T_fine.append(T)
        cp_fine.append(cp(T))
        T += step

    n = len(T_fine)
    cum_H = [0.0]
    cum_S_over_T = [0.0]
    for i in range(1, n):
        dT = T_fine[i] - T_fine[i-1]
        dH = 0.5 * (cp_fine[i-1] + cp_fine[i]) * dT
        dS = 0.5 * (cp_fine[i-1]/T_fine[i-1] + cp_fine[i]/T_fine[i]) * dT
        cum_H.append(cum_H[-1] + dH)
        cum_S_over_T.append(cum_S_over_T[-1] + dS)

    # find index nearest to a given T
    def nearest_index(T):
        idx = int(round((T - T_start) / step))
        if idx < 0:
            idx = 0
        if idx >= n:
            idx = n - 1
        return idx

    idx0 = nearest_index(T0)
    H0 = cum_H[idx0]
    S0_int = cum_S_over_T[idx0]

    def expected_values(T):
        idx = nearest_index(T)
        cp_val = cp_fine[idx]
        H_val = cum_H[idx] - H0
        S_val = S0 + (cum_S_over_T[idx] - S0_int)
        return cp_val, H_val, S_val

    # expected rows
    required = list(range(T_start, T_end+1, T_step))
    expected = []
    for t in required:
        expected.append(expected_values(t))

    # read agent artifact rows into dict T->values
    data = {}
    for row in artifact:
        try:
            t = float(row['T'])
            cp_a = float(row['Cp'])
            h_a = float(row['H_T_minus_H298'])
            s_a = float(row['S_T'])
            data[t] = (cp_a, h_a, s_a)
        except (ValueError, KeyError):
            continue

    # score: count rows within tolerance
    passed = 0
    for i, t in enumerate(required):
        if t not in data:
            continue
        v_agent = data[t]
        v_exp = expected[i]
        # relative errors
        rel_Cp = abs(v_agent[0] - v_exp[0]) / (abs(v_exp[0]) + 1e-12)
        rel_H  = abs(v_agent[1] - v_exp[1]) / (abs(v_exp[1]) + 1e-12)
        rel_S  = abs(v_agent[2] - v_exp[2]) / (abs(v_exp[2]) + 1e-12)
        if rel_Cp <= tol_Cp and rel_H <= tol_H and rel_S <= tol_S:
            passed += 1

    score = passed / len(required) if required else 0.0
    return score


_SCORERS = {
    'thermodynamic_functions': score_0,
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
