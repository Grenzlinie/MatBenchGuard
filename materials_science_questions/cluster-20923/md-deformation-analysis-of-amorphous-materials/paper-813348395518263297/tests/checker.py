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
    # Parameters for Ni (homogeneous)
    ni_params = {
        "a": 0.35e-9,
        "b": 0.14e-9,
        "gamma_m": 0.17,
        "gamma_0": 0.12,
        "gamma_s": 0.12,
        "lam": 0.6,
        "G": 76e9,
        "W_A": 76e9 / 65.0,
        "model": "homogeneous"
    }
    # Parameters for Si (band-like)
    si_params = {
        "a": 0.54e-9,
        "b": 0.22e-9,
        "gamma_m": 1.67,
        "gamma_0": 0.075,
        "gamma_s": 1.5,
        "lam": 0.1,
        "W_A": 8.13e8,
        "W_cr_glass": 0.23,
        "n": 5,
        "model": "band"
    }
    return {"ni_params": ni_params, "si_params": si_params}


# === block: score_0 (check id='step_02_compute_ni_tau_c') ===
def score_0(artifact, step, ctx):
    import math
    params = ctx["ni_params"]
    a = params["a"]
    b = params["b"]
    gamma_m = params["gamma_m"]
    gamma_0 = params["gamma_0"]
    gamma_s = params["gamma_s"]
    lam = params["lam"]
    W_A = params["W_A"]
    p = a / math.sqrt(3)
    C = (p * W_A - lam * gamma_0) / b
    tau_base = lam * math.pi * gamma_m / b + C

    # expected L' values
    Lprime_expected = step.get("Lprime_values", [5,10,15,20,25])
    tol_rel = step.get("tolerance_rel", 0.05)
    tol_abs = step.get("tolerance_abs_GPa", 0.2)

    rows = []
    for row in artifact:
        try:
            L_nm = float(row["L_nm"])
            tau_agent = float(row["tau_c_GPa"])
        except (ValueError, KeyError):
            continue
        rows.append((L_nm, tau_agent))

    # must have exactly the expected L' values
    if len(rows) != len(Lprime_expected):
        return 0.0

    scores = []
    for L_nm, tau_agent in rows:
        if L_nm not in Lprime_expected:
            return 0.0
        L_m = L_nm * 1e-9 * math.sqrt(2)
        tau_expected_gpa = (tau_base + gamma_s / L_m) * 1e-9
        err = abs(tau_agent - tau_expected_gpa)
        tol = max(tol_rel * abs(tau_expected_gpa), tol_abs)
        if err <= tol:
            s = 1.0
        else:
            excess = err - tol
            # linear fall-off: reaches 0 at 0.5 * expected value
            s = max(0.0, 1.0 - excess / (max(abs(tau_expected_gpa), 1e-12) * 0.5))
        scores.append(s)

    return sum(scores) / len(scores)


# === block: score_1 (check id='step_03_compute_si_tau_c') ===
def score_1(artifact, step, ctx):
    import math
    params = ctx["si_params"]
    a = params["a"]
    b = params["b"]
    gamma_m = params["gamma_m"]
    gamma_0 = params["gamma_0"]
    gamma_s = params["gamma_s"]
    lam = params["lam"]
    W_A = params["W_A"]
    W_cr_glass = params["W_cr_glass"]
    n = params["n"]
    p = a / math.sqrt(3)
    C = ( ((n - 2) / n) * (p * W_A - lam * gamma_0) + (2.0 / n) * W_cr_glass ) / b
    tau_base = lam * math.pi * gamma_m / b + C

    Lprime_expected = step.get("Lprime_values", [5,10,15,20,25])
    tol_rel = step.get("tolerance_rel", 0.05)
    tol_abs = step.get("tolerance_abs_GPa", 0.2)

    rows = []
    for row in artifact:
        try:
            L_nm = float(row["L_nm"])
            tau_agent = float(row["tau_c_GPa"])
        except (ValueError, KeyError):
            continue
        rows.append((L_nm, tau_agent))

    if len(rows) != len(Lprime_expected):
        return 0.0

    scores = []
    for L_nm, tau_agent in rows:
        if L_nm not in Lprime_expected:
            return 0.0
        L_m = L_nm * 1e-9 * math.sqrt(2)
        tau_expected_gpa = (tau_base + gamma_s / L_m) * 1e-9
        err = abs(tau_agent - tau_expected_gpa)
        tol = max(tol_rel * abs(tau_expected_gpa), tol_abs)
        if err <= tol:
            s = 1.0
        else:
            excess = err - tol
            s = max(0.0, 1.0 - excess / (max(abs(tau_expected_gpa), 1e-12) * 0.5))
        scores.append(s)

    return sum(scores) / len(scores)


_SCORERS = {
    'step_02_compute_ni_tau_c': score_0,
    'step_03_compute_si_tau_c': score_1,
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
