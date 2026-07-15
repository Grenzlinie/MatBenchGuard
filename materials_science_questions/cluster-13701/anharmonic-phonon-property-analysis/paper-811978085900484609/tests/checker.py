import os
import json
import csv

# === author imports / helpers ===
import math

def compute_cv(temps, deltas):
    n = len(temps)
    cv = [0.0] * n
    if n == 0:
        return cv
    if temps[0] == 0.0:
        cv[0] = 0.0
        start = 1
    else:
        start = 0
    d_dT = [0.0] * n
    for i in range(n - 1):
        if temps[i + 1] > temps[i]:
            d_dT[i] = (deltas[i + 1] - deltas[i]) / (temps[i + 1] - temps[i])
    d_dT[-1] = d_dT[-2] if n >= 2 else 0.0
    for i in range(start, n):
        T = temps[i]
        if T <= 0.0:
            cv[i] = 0.0
            continue
        beta = 1.0 / T
        delta = deltas[i]
        ddelta_dbeta = -T * T * d_dT[i]
        arg = beta * delta / 2.0
        sinh_arg = math.sinh(arg)
        denom = sinh_arg * sinh_arg
        if denom == 0.0:
            cv[i] = 0.0
        else:
            term1 = 0.5 * (beta * delta) ** 2 / denom
            term2 = 1.0 + (beta / delta) * ddelta_dbeta
            cv[i] = term1 * term2
    return cv


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


# === block: score_0 (check id='step_solve_thermo') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    gold = step.get("gold", {})
    tol = step.get("tolerances", {})
    rel_tol = tol.get("rel", 0.02)
    abs_eta = tol.get("abs_eta", 0.01)
    abs_delta = tol.get("abs_delta", 1.0)
    abs_cv = tol.get("abs_cv", 0.01)
    abs_tlambda = tol.get("abs_T_lambda", 2.0)

    crystals = ["N2", "CO", "N2O", "CO2"]
    total_passes = 0
    total_entries = 0

    def within(a, b, abs_tol):
        ref = max(abs(a), abs(b), 1e-9)
        tol_val = max(rel_tol * ref, abs_tol)
        return abs(a - b) <= tol_val

    for material in crystals:
        if material not in artifact:
            if material in gold:
                g = gold[material]
                nT = len(g["T"])
                total_entries += nT * 3 + 1
            continue
        g = gold.get(material)
        if not g:
            continue
        a = artifact[material]
        T_agent = a.get("T")
        T_gold = g["T"]
        lengths_ok = True
        if not isinstance(T_agent, list) or len(T_agent) != len(T_gold):
            lengths_ok = False
        else:
            for i in range(len(T_gold)):
                if T_agent[i] != T_gold[i]:
                    lengths_ok = False
                    break
        if not lengths_ok:
            total_entries += len(T_gold) * 3 + 1
            continue

        eta_agent = a.get("eta", [])
        eta_gold = g["eta"]
        n_eta = len(eta_gold)
        total_entries += n_eta
        if len(eta_agent) == n_eta:
            for i in range(n_eta):
                if within(eta_agent[i], eta_gold[i], abs_eta):
                    total_passes += 1

        delta_agent = a.get("delta", [])
        delta_gold = g["delta"]
        n_delta = len(delta_gold)
        total_entries += n_delta
        if len(delta_agent) == n_delta:
            for i in range(n_delta):
                if within(delta_agent[i], delta_gold[i], abs_delta):
                    total_passes += 1

        cv_gold = compute_cv(T_gold, delta_gold)
        cv_agent = a.get("C_v_R", [])
        n_cv = len(cv_gold)
        total_entries += n_cv
        if len(cv_agent) == n_cv:
            for i in range(n_cv):
                if within(cv_agent[i], cv_gold[i], abs_cv):
                    total_passes += 1

        T_lambda_agent = a.get("T_lambda")
        T_lambda_gold = g["T_lambda"]
        total_entries += 1
        if T_lambda_agent is not None:
            if within(float(T_lambda_agent), float(T_lambda_gold), abs_tlambda):
                total_passes += 1

    if total_entries == 0:
        return 0.0
    return total_passes / total_entries


_SCORERS = {
    'step_solve_thermo': score_0,
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
