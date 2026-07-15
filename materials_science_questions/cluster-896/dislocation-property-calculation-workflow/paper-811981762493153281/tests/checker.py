import os
import json
import csv

# === author imports / helpers ===
import math

# Fake numpy to support np.arange used in the scorer without requiring numpy
class _FakeNp:
    @staticmethod
    def arange(start, stop, step):
        vals = []
        cur = start
        while cur < stop + 1e-12:
            vals.append(cur)
            cur += step
        return vals

np = _FakeNp()


def compute_Rc_and_Uc(b, sigma, gamma, G):
    if sigma <= gamma / b:
        return None
    b0 = b / 2.0
    const = (G * b) / (4.0 * math.pi * (sigma - gamma / b))
    # Newton's method to solve R = const * (log(R/b0) + 1)
    R = max(const, b0 * 1.01)
    for _ in range(100):
        logratio = math.log(R / b0)
        f_val = R - const * (logratio + 1.0)
        df = 1.0 - const / R
        if df == 0:
            break
        R_new = R - f_val / df
        if R_new <= b0:
            R_new = b0 * 1.01
        if abs(R_new - R) < 1e-12 * abs(R):
            R = R_new
            break
        R = R_new
    Rc = R
    if Rc <= b0:
        return None
    Uc = 0.25 * G * b * b * Rc * (math.log(Rc / b0) - 1)
    return Rc, Uc


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
    G = 21.3e11  # dyn/cm^2
    eV_to_erg = 1.602176634e-12
    G_bt3_eV = 25.0
    G_bt3_erg = G_bt3_eV * eV_to_erg
    b_t = (G_bt3_erg / G) ** (1.0 / 3.0)
    b_p = b_t / (3.0 ** 0.5)
    return {
        "G": G,
        "eV_to_erg": eV_to_erg,
        "G_bt3_erg": G_bt3_erg,
        "b_t": b_t,
        "b_p": b_p,
    }


# === block: score_0 (check id='results_csv') ===
def score_0(artifact, step, ctx):
    tol = step.get("tolerances", {})
    expected_sigma_vals = [round(v, 2) for v in np.arange(0.05, 0.151, 0.01)]
    expected_f_vals = [0.0, 0.01, 0.02, 0.03]
    expected_set = set()
    for f in expected_f_vals:
        for s in expected_sigma_vals:
            expected_set.add((f, round(s, 2)))

    rows = artifact
    if len(rows) != 44:
        return 0.0
    correct = 0
    for row in rows:
        f = float(row["f"])
        s = float(row["sigma_over_G"])
        if (f, round(s, 2)) not in expected_set:
            return 0.0
        expected_loop = "perfect" if f == 0.0 else "faulted"
        if row["loop_type"].strip().lower() != expected_loop:
            return 0.0
        sigma = s * ctx["G"]
        if f == 0.0:
            b = ctx["b_t"]
            gamma = 0.0
        else:
            b = ctx["b_p"]
            gamma = f * ctx["G"] * ctx["b_p"]
        out = compute_Rc_and_Uc(b, sigma, gamma, ctx["G"])
        if out is None:
            return 0.0
        Rc_cm, Uc_erg = out
        Rc_ang_expected = Rc_cm * 1e8
        Uc_eV_expected = Uc_erg / ctx["eV_to_erg"]
        Uc_norm_expected = Uc_erg / ctx["G_bt3_erg"]
        dRc = abs(float(row["R_c_angstrom"]) - Rc_ang_expected)
        dUc_eV = abs(float(row["U_c_eV"]) - Uc_eV_expected)
        dUc_norm = abs(float(row["U_c_normalized"]) - Uc_norm_expected)
        if dRc <= tol.get("Rc_abs", 0.1) and dUc_eV <= tol.get("Uc_eV_abs", 0.005) and dUc_norm <= tol.get("Uc_norm_abs", 0.001):
            correct += 1
    return correct / 44.0


# === block: score_1 (check id='critical_stress') ===
def score_1(artifact, step, ctx):
    import re
    text = artifact
    match = re.search(r"sigma_over_G\s*=\s*([\d.]+)", text)
    if not match:
        return 0.0
    reported = float(match.group(1))
    sigma_vals = np.arange(0.05, 0.151, 0.01)
    threshold = None
    for s in sigma_vals:
        sigma = s * ctx["G"]
        out_perf = compute_Rc_and_Uc(ctx["b_t"], sigma, 0.0, ctx["G"])
        if out_perf is None:
            continue
        _, Uc_perf = out_perf
        f = 0.01
        gamma = f * ctx["G"] * ctx["b_p"]
        out_fault = compute_Rc_and_Uc(ctx["b_p"], sigma, gamma, ctx["G"])
        if out_fault is None:
            continue
        _, Uc_fault = out_fault
        if Uc_fault < Uc_perf:
            threshold = s
            break
    if threshold is None:
        return 0.0
    tol = step.get("tolerances", {}).get("sigma_abs", 0.005)
    if abs(reported - threshold) <= tol:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'results_csv': score_0,
    'critical_stress': score_1,
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
