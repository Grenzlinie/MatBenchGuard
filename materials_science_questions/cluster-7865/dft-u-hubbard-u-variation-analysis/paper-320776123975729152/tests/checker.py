import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    NA = 6.02214076e23
    muB = 9.274009994e-21
    kB = 1.380649e-16
    g = 2.0
    S = 1.5
    theta = -4.0
    conc = 200.0e-6
    mu_eff = g * math.sqrt(S*(S+1)) * muB
    C_Fe = NA * mu_eff**2 / (3 * kB)
    C_imp = conc * C_Fe
    def chi_imp(T):
        return C_imp / (T - theta)
    imp_temps = [30, 100, 200]
    expected_imp = {T: chi_imp(T) for T in imp_temps}
    ctx = {
        "chi_s_target": 3.3e-5,
        "chi_orb_target": 4.77e-4,
        "susc_tol": 0.10,
        "plateau_min_temp": 100,
        "plateau_max_var": 0.05,
        "imp_temps": imp_temps,
        "imp_expected": expected_imp,
        "imp_tol": 0.05
    }
    return ctx


# === block: score_0 (check id='chi_s_check') ===
def score_0(artifact, step, ctx):
    val = artifact.get("chi_s")
    if val is None: return 0.0
    # Use target and tolerance from the grading-spec step, falling back to ctx if missing
    target = step.get("target_value", ctx.get("chi_s_target", 0.0))
    tol = step.get("tolerance", ctx.get("susc_tol", 0.1))
    if target == 0: return 1.0 if val == 0 else 0.0
    if abs(val - target) / abs(target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='chi_orb_check') ===
def score_1(artifact, step, ctx):
    val = artifact.get("chi_orb")
    if val is None: return 0.0
    target = ctx["chi_orb_target"]
    tol = ctx["susc_tol"]
    if target == 0: return 1.0 if val == 0 else 0.0
    if abs(val - target) / abs(target) <= tol:
        return 1.0
    else:
        return 0.0


# === block: score_2 (check id='csv_plateau_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    vals = [float(r["chi_total(emu/mol)"]) for r in rows if float(r["T(K)"]) >= ctx["plateau_min_temp"]]
    if len(vals) < 2:
        return 0.0
    mean_val = sum(vals) / len(vals)
    if mean_val == 0:
        return 0.0
    dev = max(abs(v - mean_val) for v in vals)
    ratio = dev / mean_val
    if ratio <= ctx["plateau_max_var"]:
        return 1.0
    else:
        return max(0.0, 1.0 - (ratio - ctx["plateau_max_var"]) / 0.1)


# === block: score_3 (check id='csv_impurity_check') ===
def score_3(artifact, step, ctx):
    rows = artifact
    agent_imp = {}
    for r in rows:
        T = int(float(r["T(K)"]))
        if T in ctx["imp_temps"]:
            agent_imp[T] = float(r["chi_imp(emu/mol)"])
    if len(agent_imp) != len(ctx["imp_temps"]):
        return 0.0
    matches = 0
    for T, exp in ctx["imp_expected"].items():
        val = agent_imp.get(T)
        if val is not None and exp != 0:
            if abs(val - exp) / abs(exp) <= ctx["imp_tol"]:
                matches += 1
    return matches / len(ctx["imp_temps"])


_SCORERS = {
    'chi_s_check': score_0,
    'chi_orb_check': score_1,
    'csv_plateau_check': score_2,
    'csv_impurity_check': score_3,
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
