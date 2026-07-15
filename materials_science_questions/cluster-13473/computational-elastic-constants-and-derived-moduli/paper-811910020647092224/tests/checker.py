import os
import json
import csv

# === author imports / helpers ===
import math

# Physical constants (SI)
a0_nm = 0.135775
a0 = a0_nm * 1e-9
kb0 = 6.187e20
ktheta0 = 1.813e20
delta_nm = 0.05197
delta = delta_nm * 1e-9
a_T_nm = {0:0.135775, 100:0.135830, 500:0.136200, 1000:0.136800}

def a_T_m(T):
    return a_T_nm[T] * 1e-9

def keating_force_constants(T):
    aT_m = a_T_m(T)
    ratio = a0 / aT_m
    kb = kb0 * (ratio ** 4)
    ktheta = ktheta0 * (ratio ** 7)
    return kb, ktheta

def E_unreconstructed(N, a, kb, ktheta):
    # Eq. (12)
    return (4.0 * N * a / (4.0 * N + 1.0)) * (kb + 1.5 * ktheta)

def E_reconstructed(N, a, kb, ktheta, delta):
    # Eq. (16)
    term1 = 4.0 * (N - 1) * a**4 * (kb + 1.5 * ktheta)
    term2 = kb * (
        8.0 * (a - delta)**4
        + ((a + delta)**2 - delta**2 / 2.0)**2
        + ((a - delta)**2 - delta**2 / 2.0)**2
        + 2.0 * (a**2 + delta**2 / 2.0)**2
    )
    term3 = 0.5 * ktheta * (
        (2.0 * a**2 - delta**2)**2
        + 4.0 * a**2 * (a + delta)**2
        + 4.0 * a**2 * (a - delta)**2
    )
    numerator = term1 + term2 + term3
    denominator = (4.0 * N + 1.0) * a**3
    return numerator / denominator

def Pa_to_GPa(val):
    return val / 1e9


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
    return {"required": spec["steps"][0]["required_combinations"], "tolerance_abs": spec["steps"][0]["tolerance_abs"]}


# === block: score_0 (check id='scored_youngs_modulus') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts with N, condition, temperature_K, E_GPa
    required = ctx["required"]
    tol = ctx["tolerance_abs"]

    # Build lookup from agent CSV (first occurrence wins)
    lookup = {}
    for row in rows:
        key = (int(row["N"]), row["condition"], float(row["temperature_K"]))
        if key not in lookup:
            lookup[key] = float(row["E_GPa"])

    correct = 0
    total = len(required)
    for req in required:
        key = (int(req["N"]), req["condition"], float(req["temperature_K"]))
        if key not in lookup:
            continue
        submitted = lookup[key]
        N = int(req["N"])
        condition = req["condition"]
        T = float(req["temperature_K"])
        aT_m = a_T_m(T)
        kb, kt = keating_force_constants(T)
        if condition == "unreconstructed":
            exp = E_unreconstructed(N, aT_m, kb, kt)
        else:
            exp = E_reconstructed(N, aT_m, kb, kt, delta)
        exp_gpa = Pa_to_GPa(exp)
        if abs(submitted - exp_gpa) <= tol:
            correct += 1

    return correct / total


_SCORERS = {
    'scored_youngs_modulus': score_0,
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
