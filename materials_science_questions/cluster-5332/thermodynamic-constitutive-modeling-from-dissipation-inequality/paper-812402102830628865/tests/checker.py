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
    steps = spec.get("steps", [])
    step = next(s for s in steps if s["output_file"] == "computed_quantities.csv")
    constants = step["constants"]
    tol_rel = step["tolerance_rel"]
    tol_sum = step["tolerance_sum"]
    return {"constants": constants, "tol_rel": tol_rel, "tol_sum": tol_sum}


# === block: score_0 (check id='step_01_compute_quantities') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0

    const = ctx["constants"]
    l0_star = const["l0_star"]
    Delta0_l = const["Delta0_l"]
    T_g = const["T_g"]
    T_m = const["T_m"]
    k_B = const["k_B"]
    alpha = 4.0 / (T_m - T_g)
    T0 = (T_g + T_m) / 2.0
    tol_rel = ctx["tol_rel"]
    tol_sum = ctx["tol_sum"]

    def langevin(a):
        return 1.0 / math.tanh(a) - 1.0 / a

    def langevin_deriv(a):
        sinh = math.sinh(a)
        return -1.0 / (sinh * sinh) + 1.0 / (a * a)

    passed = 0
    eps = 1e-15

    for row in rows:
        try:
            T = float(row["temperature_T"])
            f_val = float(row["force_f"])
            U_sub = float(row["U_f"])
            S_sub = float(row["S_f"])
            fS_sub = float(row["f_S"])
            fU_sub = float(row["f_U"])
        except (KeyError, ValueError):
            continue

        if f_val == 0.0:
            U_gold = 0.0
            S_gold = 0.0
            fS_gold = 0.0
            fU_gold = 0.0
        else:
            a_gold = l0_star * f_val / (k_B * T)
            La = langevin(a_gold)
            dLa = langevin_deriv(a_gold)
            Delta_l = Delta0_l * math.exp(alpha * (T - T0))
            log_term = math.log((math.exp(a_gold) - math.exp(-a_gold)) / (2.0 * a_gold))
            U_gold = alpha * Delta_l * (k_B * T * T / l0_star) * log_term
            l_minus_l0 = Delta_l * La
            kappa = l0_star / (k_B * T)
            S_gold = - (l_minus_l0 / (kappa * T)) * (a_gold * La - log_term) + alpha * Delta_l * (k_B * T / l0_star) * log_term
            fS_gold = (1.0 - (alpha * T * La) / (a_gold * dLa)) * f_val
            fU_gold = (alpha * T * La) / (a_gold * dLa) * f_val

        ok = True
        for sub_val, gold_val in [(U_sub, U_gold), (S_sub, S_gold), (fS_sub, fS_gold), (fU_sub, fU_gold)]:
            if abs(gold_val) < 1e-20:
                if abs(sub_val) > eps:
                    ok = False
            else:
                if abs(sub_val - gold_val) > tol_rel * abs(gold_val):
                    ok = False
        if ok and abs(fS_sub + fU_sub - f_val) > tol_sum:
            ok = False
        if ok:
            passed += 1

    return passed / len(rows)


_SCORERS = {
    'step_01_compute_quantities': score_0,
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
