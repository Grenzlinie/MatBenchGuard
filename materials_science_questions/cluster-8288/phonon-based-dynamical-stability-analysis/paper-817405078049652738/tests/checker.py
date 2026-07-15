import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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


# === block: score_0 (check id='step03_thermo_functions') ===
def score_0(artifact, step, ctx):
    if artifact is None: return 0.0

    # --- basic shape validation ---
    required = {"Temperature (K)", "C_V (J/mol/K)", "S (J/mol/K)", "H (J/mol)", "F (J/mol)"}
    cols = set(artifact[0].keys()) if artifact else set()
    if not required.issubset(cols):
        return 0.0

    temps = []
    cv = []
    S = []
    H = []
    F = []
    try:
        for row in artifact:
            t = float(row["Temperature (K)"])
            c = float(row["C_V (J/mol/K)"])
            s = float(row["S (J/mol/K)"])
            h = float(row["H (J/mol)"])
            f = float(row["F (J/mol)"])
            temps.append(t)
            cv.append(c)
            S.append(s)
            H.append(h)
            F.append(f)
    except (ValueError, KeyError, TypeError):
        return 0.0

    n = len(temps)
    if n < 100:
        return 0.0

    # ------------------------------------------------------------
    # Sub‑scores (weights sum to 1.0)
    # ------------------------------------------------------------
    w_shape   = 0.05   # basic format already passed → 1.0
    w_cv_ref  = 0.50   # hidden reference points from paper Fig. 6a
    w_cv_mono = 0.10   # monotonic non‑decreasing (sanity)
    w_S       = 0.10   # S ≥ 0, monotonic, S(0) ≈ 0
    w_H       = 0.10   # H ≥ 0, monotonic
    w_F_cons  = 0.15   # F = H − T·S consistency

    score_shape = 1.0

    # ----- C_V monotonicity (low‑weight sanity) -----
    tol = 1e-6
    nondec = all((cv[i+1] - cv[i]) >= -tol for i in range(n-1))
    score_cv_mono = 1.0 if nondec else 0.0

    # ----- C_V reference comparison (hidden gold) -----
    # Digitised from paper Figure 6a (phonon heat capacity for Na3ClO supercell).
    # Temperatures in K, C_V in J/(mol·K).
    hidden_ref = [
        (  0.0,   0.0),
        (100.0,  21.0),
        (200.0,  92.0),
        (300.0, 116.0),
        (400.0, 123.0),
        (500.0, 125.0),
        (600.0, 125.0),
    ]

    def _interp_cv(t):
        """Linear interpolation of agent's C_V at temperature t."""
        if t <= temps[0]:
            return cv[0]
        if t >= temps[-1]:
            return cv[-1]
        for i in range(n-1):
            if temps[i] <= t <= temps[i+1]:
                frac = (t - temps[i]) / (temps[i+1] - temps[i])
                return cv[i] + frac * (cv[i+1] - cv[i])
        return 0.0  # fallback

    rel_errs = []
    for t_ref, c_ref in hidden_ref:
        c_agent = _interp_cv(t_ref)
        if abs(c_ref) < 0.001:
            # avoid division by zero; treat zero reference points separately
            if abs(c_agent) < 0.5:
                rel_errs.append(0.0)
            else:
                rel_errs.append(1.0)
        else:
            rel_err = abs(c_agent - c_ref) / abs(c_ref)
            rel_errs.append(rel_err)

    mean_rel_err = sum(rel_errs) / len(rel_errs)
    tol_ref = 0.60   # generous tolerance to accommodate synthetic Debye approximations and DFT toolchain spread
    score_cv_ref = max(0.0, 1.0 - mean_rel_err / tol_ref)

    # ----- S constraints -----
    if any(v < -tol for v in S):
        score_S = 0.0
    else:
        nondec_S = all((S[i+1] - S[i]) >= -tol for i in range(n-1))
        if not nondec_S:
            score_S = 0.0
        else:
            idx_0 = min(range(n), key=lambda i: abs(temps[i] - 0.0))
            score_S = 1.0 if abs(S[idx_0]) <= 5.0 else 0.0

    # ----- H constraints -----
    score_H = 0.0
    if all(v >= -tol for v in H):
        score_H = 1.0 if all((H[i+1] - H[i]) >= -tol for i in range(n-1)) else 0.0

    # ----- Internal consistency F = H - T·S -----
    consist = sum(
        1 for i in range(n)
        if abs(H[i] - temps[i]*S[i] - F[i]) / (max(abs(F[i]), 1e-6)) < 0.02
    )
    score_F_cons = consist / n

    # ---- aggregate ----
    score_total = (w_shape  * score_shape +
                   w_cv_ref * score_cv_ref +
                   w_cv_mono* score_cv_mono +
                   w_S      * score_S +
                   w_H      * score_H +
                   w_F_cons * score_F_cons)
    return min(max(score_total, 0.0), 1.0)


_SCORERS = {
    'step03_thermo_functions': score_0,
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
