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
    return {}


# === block: score_0 (check id='rgs_properties_check') ===
def score_0(artifact, step, ctx):
    import math
    config = step['config']
    solids = config['solids']
    tol = config['tolerance_relative']
    K_B = config['K_B']
    fields = ['K_T','C_S','C_44','dK_T_dP','dC_S_dP','dC44_prime_dP','d2K_T_dP2','d2C_S_dP2','d2C44_prime_dP2']
    total = 0.0
    n = 0
    for elem, param in solids.items():
        a = param['a']
        gamma = param['gamma']
        theta_D = param['theta_D']
        alpha = param['alpha_prime_a8']
        A = param['A']
        ldf = param['lambda_df_a7']
        ld2 = param['lambda_d2f_a6']
        ld3 = param['lambda_d3f_a5']
        C = param['C']
        D_val = param['D']
        U = K_B * theta_D * gamma / (a*a)
        U_gamma = U * gamma
        P = 0.0
        KT_raw = (1.0/(6.0*a)) * (12.6448*alpha -61.2992*ldf + 4.0*A + 1.1248*U + 3.374*U_gamma - 4.0*a*P)
        CS_raw = (1.0/(4.0*a)) * (1.928*alpha + 0.5*ldf + 0.984375*U + 1.75*a*P)
        C44_raw = (1.0/(2.0*a)) * (2.9292*alpha + A - 0.10546*U + 0.1875*a*P)
        dK_dP_expr = -139.1084*alpha -12.0*A +4.0*C +827.721*ldf -130.052*ld2 +7.875*U +3.375*U_gamma -8.0*a*P
        dK_dP = -1.0/(18.0*a*KT_raw) * dK_dP_expr
        dCS_dP_expr = -12.5748*alpha +6.0*A +C -41.832*ldf -10.838*ld2 -5.625*U +9.0*a*P
        dCS_dP = -1.0/(12.0*a*KT_raw) * dCS_dP_expr
        dC44_dP_expr = -27.5532*alpha -1.375*A +C +55.4582*ldf -10.8394*ld2 +0.2109*U -0.375*a*P
        dC44_dP = -1.0/(6.0*a*KT_raw) * dC44_dP_expr
        term1 = dK_dP * (-139.108*alpha -12.0*A +4.0*C -827.721*ldf -130.059*ld2 +7.875*U +3.375*U_gamma -8.0*a*P)
        term2 = 442.612*alpha -3116.646*ldf +12.0*A -4.0*C + (4.0/3.0)*D_val +736.957*ld2 -81.759*ld3 -7.5937*U -6.4687*U_gamma -3.375*U*gamma*gamma +8.0*a*P
        d2K_raw = (1.0/(18.0*a*KT_raw*KT_raw)) * (term1 + term2)
        term1s = dK_dP * (-12.5748*alpha +6.0*A +C -41.832*ldf -10.838*ld2 -5.0625*U +9.0*a*P)
        term2s = 18.7572*alpha -8.0*A -2.0*C + D_val/3.0 +132.378*ldf -16.106*ld2 -10.223*ld3 +3.375*U*gamma*gamma +6.0*a*P
        d2CS_raw = (1.0/(12.0*a*KT_raw*KT_raw)) * (term1s + term2s)
        term1c = dK_dP * (-27.5533*alpha -1.375*A +C +55.4582*ldf -10.8394*ld2 +0.21093*U -0.375*a*P)
        term2c = 83.499*alpha -0.715*A +0.625*C + D_val/3.0 +307.559*ldf +41.9464*ld2 -5.1089*ld3 -0.140625*U +0.375*a*P
        d2C44_raw = (1.0/(6.0*a*KT_raw*KT_raw)) * (term1c + term2c)
        expected = {
            'K_T': KT_raw * 0.01,
            'C_S': CS_raw * 0.01,
            'C_44': C44_raw * 0.01,
            'dK_T_dP': dK_dP,
            'dC_S_dP': dCS_dP,
            'dC44_prime_dP': dC44_dP,
            'd2K_T_dP2': d2K_raw * 100.0,
            'd2C_S_dP2': d2CS_raw * 100.0,
            'd2C44_prime_dP2': d2C44_raw * 100.0
        }
        agent_vals = artifact.get(elem, {})
        for f in fields:
            exp = expected[f]
            got = agent_vals.get(f)
            if got is None:
                continue
            denom = abs(exp) if abs(exp) > 1e-12 else 1e-12
            rel = abs(got - exp) / denom
            if rel <= tol:
                total += 1.0
            n += 1
    score = total / n if n > 0 else 0.0
    return score


_SCORERS = {
    'rgs_properties_check': score_0,
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
