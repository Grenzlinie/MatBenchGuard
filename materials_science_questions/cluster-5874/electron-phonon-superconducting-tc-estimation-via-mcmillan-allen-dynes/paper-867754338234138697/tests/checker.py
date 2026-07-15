import os
import json
import csv

# === author imports / helpers ===
import math, json


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


# === block: score_0 (check id='s1') ===
def score_0(artifact, step, ctx):
    import math
    R = 8.314
    N_A = 6.02214076e23
    kB = 1.380649e-23
    eV = 1.602176634e-19
    mu_star = 0.1
    N_atoms = 3
    inputs = {
        "MoTe2": {"gamma": 3.06, "beta": 0.758, "Tc": 0.1},
        "MoTe1.8S0.2": {"gamma": 2.07, "beta": 0.635, "Tc": 1.3}
    }
    tol_theta = step.get("tolerance_theta_d", 1.0)
    tol_nef = step.get("tolerance_N_EF", 0.01)
    tol_lam = step.get("tolerance_lambda_ep", 0.01)
    expected = {}
    for comp, vals in inputs.items():
        beta_J = vals["beta"] * 1e-3
        Theta_D = (N_atoms * (12/5) * math.pi**4 * R / beta_J) ** (1/3)
        gamma_J = vals["gamma"] * 1e-3
        N_EF = (gamma_J / ((math.pi**2/3) * kB**2 * N_A)) * eV
        arg = 1.45 * vals["Tc"] / Theta_D
        if arg > 0:
            lam = (mu_star * math.log(arg) - 1.04) / (1.04 + math.log(arg) * (1.0 - 0.62 * mu_star))
        else:
            lam = 0.0
        expected[comp] = {"Theta_D": Theta_D, "N_EF": N_EF, "lambda_ep": lam}
    if not isinstance(artifact, dict):
        return 0.0
    total = 0
    correct = 0
    for comp in ["MoTe2", "MoTe1.8S0.2"]:
        if comp not in artifact:
            continue
        obj = artifact[comp]
        if not isinstance(obj, dict):
            continue
        exp = expected[comp]
        for key, tol in [("Theta_D", tol_theta), ("N_EF", tol_nef), ("lambda_ep", tol_lam)]:
            total += 1
            agent_val = obj.get(key)
            if agent_val is None:
                continue
            if isinstance(agent_val, (int, float)) and abs(agent_val - exp[key]) <= tol:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    's1': score_0,
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
