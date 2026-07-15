import os
import json
import csv

# === author imports / helpers ===
import math
import numpy as np
from scipy.special import k0, k1


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
    G = 5e10
    nu = 0.3
    omega = 0.01
    R = 2e-6
    b = 2.5e-10
    rho0 = 1e14
    T_ext = 1.6e-9

    D = G / (2 * math.pi * (1 - nu))
    r_d = 1.0 / math.sqrt(math.pi * rho0 * b**2 * D / T_ext)
    I_c = omega / (math.pi * b * r_d)

    ctx = {
        "G": G,
        "nu": nu,
        "omega": omega,
        "R": R,
        "b": b,
        "rho0": rho0,
        "T_ext": T_ext,
        "D": D,
        "r_d": r_d,
        "I_c": I_c,
    }
    return ctx


# === block: score_0 (check id='step_01_fields') ===
def score_0(artifact, step, ctx):
    x = np.asarray(artifact["x"], dtype=float)
    y = np.asarray(artifact["y"], dtype=float)
    I_agent = np.asarray(artifact["I"], dtype=float)
    sigma_xx_agent = np.asarray(artifact["sigma_xx"], dtype=float)
    sigma_yy_agent = np.asarray(artifact["sigma_yy"], dtype=float)
    sigma_xy_agent = np.asarray(artifact["sigma_xy"], dtype=float)
    r_d_agent = float(artifact["r_d"])
    I_c_agent = float(artifact["I_c"])
    D_agent = float(artifact["D"])

    # Parameter consistency
    if not (np.isclose(r_d_agent, ctx["r_d"], rtol=1e-12) and
            np.isclose(I_c_agent, ctx["I_c"], rtol=1e-12) and
            np.isclose(D_agent, ctx["D"], rtol=1e-12)):
        return 0.0

    # Use reference parameters for field recomputation
    rd = ctx["r_d"]
    Ic = ctx["I_c"]
    D = ctx["D"]
    omega = ctx["omega"]

    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    rd_eps = 1e-15 * rd
    mask_valid = R > rd_eps

    # Expected fields
    I_exp = Ic * np.sinh(Y / rd) * k0(R / rd)
    sigma_yy_exp = -D * omega * (np.cosh(Y/rd)*k0(R/rd) + np.sinh(Y/rd)*(Y/R)*k1(R/rd))
    sigma_xx_exp = -D * omega * (np.cosh(Y/rd)*k0(R/rd) - np.sinh(Y/rd)*(Y/R)*k1(R/rd))
    sigma_xy_exp = -D * omega * np.sinh(Y/rd)*(X/R)*k1(R/rd)

    # Compare on valid points
    def close_enough(a, e):
        return np.isclose(a, e, rtol=step.get("tolerance_rtol", 1e-8), atol=step.get("tolerance_atol", 1e-12))

    if (np.all(close_enough(I_exp[mask_valid], I_agent[mask_valid])) and
        np.all(close_enough(sigma_xx_exp[mask_valid], sigma_xx_agent[mask_valid])) and
        np.all(close_enough(sigma_yy_exp[mask_valid], sigma_yy_agent[mask_valid])) and
        np.all(close_enough(sigma_xy_exp[mask_valid], sigma_xy_agent[mask_valid]))):
        return 1.0

    # Partial credit based on maximum relative error
    def max_rel_error(a, e):
        diff = np.abs(a - e)
        denom = np.maximum(np.abs(a), np.abs(e))
        with np.errstate(divide='ignore', invalid='ignore'):
            rel = np.where(denom > 0, diff / denom, 0.0)
        return np.max(rel)

    tol = step.get("tolerance_rtol", 1e-8)
    max_err = max(
        max_rel_error(I_exp[mask_valid], I_agent[mask_valid]),
        max_rel_error(sigma_xx_exp[mask_valid], sigma_xx_agent[mask_valid]),
        max_rel_error(sigma_yy_exp[mask_valid], sigma_yy_agent[mask_valid]),
        max_rel_error(sigma_xy_exp[mask_valid], sigma_xy_agent[mask_valid])
    )
    if max_err <= tol:
        return 1.0
    else:
        return max(0.0, 1.0 - (max_err - tol) / (9 * tol))


# === block: score_1 (check id='step_02_energy') ===
def score_1(artifact, step, ctx):
    W_unscreened_agent = float(artifact["W_unscreened"])
    W_screened_agent = float(artifact["W_screened"])
    ratio_agent = float(artifact["ratio"])

    D = ctx["D"]
    omega = ctx["omega"]
    R = ctx["R"]
    r_d = ctx["r_d"]

    W_unscreened_exp = D * omega**2 * R**2 / 8.0
    W_screened_exp = (math.sqrt(math.pi) / 4.0) * D * omega**2 * r_d**2 * math.sqrt(R / r_d)
    ratio_exp = W_screened_exp / W_unscreened_exp

    tol_rtol = step.get("tolerance_rtol", 1e-12)
    tol_atol = step.get("tolerance_atol", 1e-15)

    if (np.isclose(W_unscreened_agent, W_unscreened_exp, rtol=tol_rtol, atol=tol_atol) and
        np.isclose(W_screened_agent, W_screened_exp, rtol=tol_rtol, atol=tol_atol) and
        np.isclose(ratio_agent, ratio_exp, rtol=tol_rtol, atol=tol_atol)):
        return 1.0

    def rel_err(a, e):
        return abs(a - e) / max(abs(e), 1e-100)

    max_err = max(rel_err(W_unscreened_agent, W_unscreened_exp),
                  rel_err(W_screened_agent, W_screened_exp),
                  rel_err(ratio_agent, ratio_exp))
    if max_err <= tol_rtol:
        return 1.0
    else:
        return max(0.0, 1.0 - (max_err - tol_rtol) / (9 * tol_rtol))


_SCORERS = {
    'step_01_fields': score_0,
    'step_02_energy': score_1,
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
