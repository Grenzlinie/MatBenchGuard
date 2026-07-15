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
    epsilon_eV = 0.00239
    sigma_nm = 0.3415
    l0_nm = 0.142
    epsilon_J = epsilon_eV * 1.602176634e-19
    sigma_m = sigma_nm * 1e-9
    l0_m = l0_nm * 1e-9
    rho_c_m2 = 4.0 / (3.0 * math.sqrt(3.0) * l0_m**2)
    v_nm = [i * 0.01 for i in range(51)]
    v_m = [vn * 1e-9 for vn in v_nm]
    L_u_m = 10e-9
    sigma_Pa = [8.0 * math.pi * rho_c_m2**2 * epsilon_J * sigma_m * (
        (sigma_m**5 / (sigma_m + v)**5) - (sigma_m**11 / (sigma_m + v)**11)
    ) for v in v_m]
    ref_sigma = [s * 1e-9 for s in sigma_Pa]
    tau_Pa = [2.0 * math.pi * rho_c_m2**2 * epsilon_J * sigma_m**2 / L_u_m * (
        (sigma_m**4 / (sigma_m + v)**4) - (2.0/5.0) * (sigma_m**10 / (sigma_m + v)**10)
    ) for v in v_m]
    ref_tau = [t * 1e-9 for t in tau_Pa]
    return {"ref_sigma": ref_sigma, "ref_tau": ref_tau}


# === block: score_0 (check id='cohesive_parameters') ===
def score_0(artifact, step, ctx):
    data = artifact
    targets = step.get("targets", {})
    tols = step.get("tolerances_relative", {})
    score = 0.0
    count = 0
    for field in ["Phi_total", "sigma_max", "delta_0"]:
        val = data.get(field)
        target = targets.get(field)
        tol = tols.get(field, 0.02)
        if val is None or target is None:
            continue
        err = abs(val - target) / target
        if err <= tol:
            s = 1.0
        else:
            s = max(0.0, 1.0 - (err - tol) / tol)
        score += s
        count += 1
    if count == 0:
        return 0.0
    return score / count


# === block: score_1 (check id='stress_displacement') ===
def score_1(artifact, step, ctx):
    csv_data = artifact
    ref_sigma = ctx["ref_sigma"]
    ref_tau = ctx["ref_tau"]
    n = len(ref_sigma)
    if len(csv_data) != n:
        return 0.0
    sigma_scores = []
    tau_scores = []
    tau_vals = []
    for i, row in enumerate(csv_data):
        s_val = row.get("sigma_cohesive_GPa")
        t_val = row.get("tau_cohesive_GPa")
        if s_val is None or t_val is None:
            continue
        s = float(s_val)
        t = float(t_val)
        # sigma: absolute tolerance
        abs_diff_s = abs(s - ref_sigma[i])
        ok_s = 1.0 if abs_diff_s <= 0.05 else max(0.0, 1.0 - (abs_diff_s - 0.05)/0.05)
        # tau: relative tolerance
        rt = ref_tau[i]
        abs_diff_t = abs(t - rt)
        tol_t = 0.1 * max(abs(rt), 1e-6)
        ok_t = 1.0 if abs_diff_t <= tol_t else max(0.0, 1.0 - (abs_diff_t - tol_t) / tol_t)
        sigma_scores.append(ok_s)
        tau_scores.append(ok_t)
        tau_vals.append(t)
    avg_sigma = sum(sigma_scores)/len(sigma_scores) if sigma_scores else 0.0
    avg_tau = sum(tau_scores)/len(tau_scores) if tau_scores else 0.0
    row_score = 0.5 * avg_sigma + 0.5 * avg_tau
    # monotonicity of tau (decreasing)
    mono = all(tau_vals[i] >= tau_vals[i+1] - 1e-6 for i in range(len(tau_vals)-1))
    mono_score = 1.0 if mono else 0.0
    final = 0.8 * row_score + 0.2 * mono_score
    return final


# === block: score_2 (check id='expressions') ===
def score_2(artifact, step, ctx):
    text = artifact
    required = ["Phi_total", "sigma_cohesive", "tau_cohesive", "rho_c", "epsilon", "sigma"]
    text_l = text.lower()
    present = [t.lower() in text_l for t in required]
    score = sum(present) / len(required)
    return score


_SCORERS = {
    'cohesive_parameters': score_0,
    'stress_displacement': score_1,
    'expressions': score_2,
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
