import os
import json
import csv

# === author imports / helpers ===
import math
import statistics


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


# === block: score_0 (check id='check_plateau_product') ===
def score_0(artifact, step, ctx):
    rows = artifact
    sweep_s0 = step["params"]["s0_sweep"]
    theta_vals = step["params"]["theta0_values"]
    prod_low = step["params"]["product_lower_bound"]
    prod_high = step["params"]["product_upper_bound"]
    threshold = step["params"]["rel_change_threshold"]

    theta_scores = []
    for th in theta_vals:
        sub = [r for r in rows if abs(float(r["s0"]) - sweep_s0) < 1e-9 and abs(float(r["theta0"]) - th) < 1e-9 and float(r["nu"]) > 0]
        if not sub:
            continue
        sub.sort(key=lambda r: float(r["nu"]))
        max_nu = max(float(r["nu"]) for r in sub)
        high = [r for r in sub if float(r["nu"]) >= 0.8 * max_nu]
        if not high:
            high = sub[-3:]
        tau_c_plat = sum(float(r["tau_c"]) for r in high) / len(high)
        n_d_plat = sum(float(r["n_d"]) for r in high) / len(high)
        nu_min = None
        for r in sub:
            tau = float(r["tau_c"])
            nd = float(r["n_d"])
            if abs(tau - tau_c_plat) / max(tau_c_plat, 1e-12) <= threshold and abs(nd - n_d_plat) / max(n_d_plat, 1e-12) <= threshold:
                nu_min = float(r["nu"])
                break
        if nu_min is None:
            continue
        product = nu_min * tau_c_plat
        if prod_low <= product <= prod_high:
            theta_scores.append(1.0)
        else:
            theta_scores.append(0.0)
    if not theta_scores:
        return 0.0
    return sum(theta_scores) / len(theta_scores)


# === block: score_1 (check id='check_scaling_laws') ===
def score_1(artifact, step, ctx):
    rows = artifact
    s0_vals = step["params"]["s0_values"]
    theta_vals = step["params"]["theta0_values"]
    pre_tau = step["params"]["formula_tau_prefactor"]
    coeff_tau = step["params"]["formula_tau_exponent_coeff"]
    pre_n = step["params"]["formula_n_prefactor"]
    coeff_n = step["params"]["formula_n_exponent_coeff"]
    tol = step["params"]["ratio_tolerance_factor"]

    combo_scores = []
    for s0 in s0_vals:
        for th in theta_vals:
            base = [r for r in rows if abs(float(r["s0"]) - s0) < 1e-9 and abs(float(r["theta0"])) < 1e-9 and abs(float(r["nu"])) < 1e-9]
            if not base:
                continue
            tau0 = float(base[0]["tau_c"])
            nd0 = float(base[0]["n_d"])
            plat = [r for r in rows if abs(float(r["s0"]) - s0) < 1e-9 and abs(float(r["theta0"]) - th) < 1e-9 and float(r["nu"]) > 0]
            if not plat:
                continue
            plat.sort(key=lambda r: float(r["nu"]), reverse=True)
            tau_p = float(plat[0]["tau_c"])
            nd_p = float(plat[0]["n_d"])
            if tau_p <= 0 or nd0 <= 0:
                continue
            R_tau = tau0 / tau_p
            R_n = nd_p / nd0
            ln_s0 = math.log(s0)
            R_tau_ref = pre_tau * math.exp(coeff_tau * th / (ln_s0**2))
            R_n_ref = pre_n * math.exp(coeff_n * th / (ln_s0**2))
            if R_tau_ref <= 0 or R_n_ref <= 0:
                continue
            ratio_tau = R_tau / R_tau_ref
            ratio_n = R_n / R_n_ref
            if (1.0/tol <= ratio_tau <= tol) and (1.0/tol <= ratio_n <= tol):
                combo_scores.append(1.0)
            else:
                combo_scores.append(0.0)
    if not combo_scores:
        return 0.0
    return sum(combo_scores) / len(combo_scores)


_SCORERS = {
    'check_plateau_product': score_0,
    'check_scaling_laws': score_1,
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
