import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='NaCl_check') ===
def score_0(artifact, step, ctx):
    import json, math
    compound = step.get("compound", "NaCl")
    gold = step.get("gold", {})
    comps = artifact.get("compounds", [])
    entry = next((c for c in comps if c.get("name") == compound), None)
    if entry is None:
        return 0.0
    def check_field(val, target, tol_rel=None, tol_abs=None):
        if tol_rel is not None:
            return 1.0 if abs(val - target) <= tol_rel * abs(target) else 0.0
        if tol_abs is not None:
            return 1.0 if abs(val - target) <= tol_abs else 0.0
        return 0.0
    total = 0.0
    for field, g in gold.items():
        target = g["target"]
        tol_rel = g.get("tolerance_rel")
        tol_abs = g.get("tolerance_abs")
        val = entry.get(field)
        if val is not None and isinstance(val, (int, float)):
            total += check_field(val, target, tol_rel, tol_abs)
    n = len(gold)
    return total / n if n > 0 else 0.0


# === block: score_1 (check id='KF_check') ===
def score_1(artifact, step, ctx):
    import json, math
    compound = step.get("compound", "KF")
    gold = step.get("gold", {})
    comps = artifact.get("compounds", [])
    entry = next((c for c in comps if c.get("name") == compound), None)
    if entry is None:
        return 0.0
    def check_field(val, target, tol_rel=None, tol_abs=None):
        if tol_rel is not None:
            return 1.0 if abs(val - target) <= tol_rel * abs(target) else 0.0
        if tol_abs is not None:
            return 1.0 if abs(val - target) <= tol_abs else 0.0
        return 0.0
    total = 0.0
    for field, g in gold.items():
        target = g["target"]
        tol_rel = g.get("tolerance_rel")
        tol_abs = g.get("tolerance_abs")
        val = entry.get(field)
        if val is not None and isinstance(val, (int, float)):
            total += check_field(val, target, tol_rel, tol_abs)
    n = len(gold)
    return total / n if n > 0 else 0.0


# === block: score_2 (check id='NaF_check') ===
def score_2(artifact, step, ctx):
    import json, math
    compound = step.get("compound", "NaF")
    gold = step.get("gold", {})
    comps = artifact.get("compounds", [])
    entry = next((c for c in comps if c.get("name") == compound), None)
    if entry is None:
        return 0.0
    def check_field(val, target, tol_rel=None, tol_abs=None):
        if tol_rel is not None:
            return 1.0 if abs(val - target) <= tol_rel * abs(target) else 0.0
        if tol_abs is not None:
            return 1.0 if abs(val - target) <= tol_abs else 0.0
        return 0.0
    total = 0.0
    for field, g in gold.items():
        target = g["target"]
        tol_rel = g.get("tolerance_rel")
        tol_abs = g.get("tolerance_abs")
        val = entry.get(field)
        if val is not None and isinstance(val, (int, float)):
            total += check_field(val, target, tol_rel, tol_abs)
    n = len(gold)
    return total / n if n > 0 else 0.0


# === block: score_3 (check id='KF_transition') ===
def score_3(artifact, step, ctx):
    import json, math
    key = step.get("key", None)
    if key is None:
        return 0.0
    target = step["target"]
    tol = step["tolerance_abs"]
    parts = key.split(".")
    phase = artifact.get("phase_transitions", {})
    if not phase:
        return 0.0
    val = phase.get(parts[-1])
    if val is None:
        return 0.0
    return 1.0 if abs(val - target) <= tol else 0.0


# === block: score_4 (check id='NaF_transition') ===
def score_4(artifact, step, ctx):
    import json, math
    key = step.get("key", None)
    if key is None:
        return 0.0
    target = step["target"]
    tol = step["tolerance_abs"]
    parts = key.split(".")
    phase = artifact.get("phase_transitions", {})
    if not phase:
        return 0.0
    val = phase.get(parts[-1])
    if val is None:
        return 0.0
    return 1.0 if abs(val - target) <= tol else 0.0


# === block: score_5 (check id='pressure_deriv_consistency') ===
def score_5(artifact, step, ctx):
    import json, math
    compounds = step.get("compounds", [])
    r0s = step.get("r0s", {})
    tol_rel = step.get("tolerance_rel", 0.05)
    comp_data = artifact.get("compounds", [])
    e = 4.803e-10
    e2 = e * e
    sqrt2 = math.sqrt(2.0)
    def compute_derivatives(params, r0):
        Z = params["Z"]
        b = params["b"] * 1e-10
        rho = params["rho"] * 1e-8
        rm = params["r_m"] * 1e-8
        eps0 = params["epsilon_0"] * 1e-16
        r0_cm = r0 * 1e-8
        term1_K = -0.77669 * Z*Z*e2 / r0_cm
        term2_K = (2.0/3.0)*b*(r0_cm/rho)*(2.0 + r0_cm/rho) * math.exp(-r0_cm/rho)
        ratio = rm/(sqrt2*r0_cm)
        term3_K = sqrt2 * eps0 * ((r0_cm/rm)**3) * (240.0*ratio**15 - 144.0*ratio**9)
        K_tilde_erg = (term1_K + term2_K + term3_K) / (2.0 * r0_cm**3)
        denom = 6.0 * K_tilde_erg * (r0_cm**3)
        term1_Kp = -3.1068 * Z*Z*e2 / r0_cm
        term2_Kp = (2.0/3.0)*b*(r0_cm/rho)*(4.0 + 3.0*(r0_cm/rho) + (r0_cm/rho)**2) * math.exp(-r0_cm/rho)
        term3_Kp = sqrt2 * eps0 * ((r0_cm/rm)**3) * (3600.0*ratio**15 - 1296.0*ratio**9)
        Kp = (term1_Kp + term2_Kp + term3_Kp) / denom
        term1_C44p = 5.1121 * Z*Z*e2 / r0_cm
        term2_C44p = -2.0 * b*(r0_cm/rho)*(2.0 + r0_cm/rho) * math.exp(-r0_cm/rho)
        term3_C44p = sqrt2 * eps0 * ((r0_cm/rm)**3) * (1800.0*ratio**15 - 432.0*ratio**9)
        C44p = (term1_C44p + term2_C44p + term3_C44p) / denom
        term1_Csp = 4.8861 * Z*Z*e2 / r0_cm
        term2_Csp = b*(r0_cm/rho)*((r0_cm/rho)**2 - 2.0) * math.exp(-r0_cm/rho)
        term3_Csp = sqrt2 * eps0 * ((r0_cm/rm)**3) * (540.0*ratio**15)
        Csp = (term1_Csp + term2_Csp + term3_Csp) / denom
        return Kp, C44p, Csp
    total_fields = 0
    ok = 0
    for comp_name in compounds:
        r0 = r0s.get(comp_name)
        entry = next((c for c in comp_data if c.get("name") == comp_name), None)
        if entry is None or r0 is None:
            continue
        params = {k: entry.get(k) for k in ["Z", "b", "rho", "epsilon_0", "r_m"]}
        if any(v is None for v in params.values()):
            continue
        try:
            Kp, C44p, Csp = compute_derivatives(params, r0)
        except Exception:
            continue
        for field_name, expected in [("K_prime", Kp), ("C44_prime", C44p), ("Cs_prime", Csp)]:
            reported = entry.get(field_name)
            if reported is None:
                continue
            total_fields += 1
            if abs(reported - expected) <= tol_rel * abs(expected):
                ok += 1
    if total_fields == 0:
        return 0.0
    return ok / total_fields


_SCORERS = {
    'NaCl_check': score_0,
    'KF_check': score_1,
    'NaF_check': score_2,
    'KF_transition': score_3,
    'NaF_transition': score_4,
    'pressure_deriv_consistency': score_5,
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
