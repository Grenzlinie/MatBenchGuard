import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    return {
        "T_N_gold": 0.052,
        "Delta": 0.2,
        "I": 1.0
    }


# === block: score_0 (check id='zero_temp_energies') ===
def score_0(artifact, step, ctx):
    # find row with T closest to zero
    rows = artifact
    t_vals = np.array([float(r["T"]) for r in rows])
    idx = np.argmin(np.abs(t_vals))
    row = rows[idx]
    def get_float(key):
        v = row.get(key)
        if v is None or v == "":
            return None
        return float(v)
    vals = {k: get_float(k) for k in ["E_SDW","E_F","E_P","mu_SDW","mu_F"]}
    if any(v is None for v in vals.values()):
        return 0.0
    cfg = step.get("config", {})
    exp = cfg["expected"]
    tols = cfg.get("tolerances", {})
    sub_scores = []
    for key in ["E_SDW","E_P"]:
        target = exp[key]
        val = vals[key]
        relerr = abs(val - target) / (abs(target) + 1e-12) if abs(target) > 1e-12 else 0.0
        tol_rel = tols.get(f"{key}_rel", 0.01)
        sub_scores.append(max(0.0, 1.0 - relerr / tol_rel))
    # E_F 
    target = exp["E_F"]
    val = vals["E_F"]
    tol_abs = tols.get("E_F_abs", 0.001)
    sub_scores.append(max(0.0, 1.0 - abs(val - target) / (tol_abs + 1e-12)))
    # mu_SDW and mu_F with relative tolerance
    for key in ["mu_SDW","mu_F"]:
        target = exp[key]
        val = vals[key]
        relerr = abs(val - target) / (abs(target) + 1e-12)
        tol_rel = tols.get(f"{key}_rel", 0.01)
        sub_scores.append(max(0.0, 1.0 - relerr / tol_rel))
    score = float(np.mean(sub_scores))
    return score


# === block: score_1 (check id='critical_temperature') ===
def score_1(artifact, step, ctx):
    rows = artifact
    t_vals = np.array([float(r["T"]) for r in rows])
    mu = np.array([float(r["mu_SDW"]) for r in rows])
    cfg = step.get("config", {})
    mu_thr = cfg.get("mu_threshold", 1e-4)
    # find first index where mu <= threshold
    nz_idx = np.where(mu <= mu_thr)[0]
    if len(nz_idx) == 0:
        return 0.0
    idx = nz_idx[0]
    T_N_found = t_vals[idx]

    # Compute expected T_N from model parameters (Delta, I) in ctx.
    # Self-consistency equation for lambda=1: I/(2*Delta) * tanh( (1/T_N) * Delta/2 ) = 1
    Delta = ctx["Delta"]
    I = ctx["I"]
    rhs = 2 * Delta / I
    if rhs >= 1.0:
        T_N_expected = 0.0
    else:
        beta_N = (2.0 / Delta) * np.arctanh(rhs)
        T_N_expected = 1.0 / beta_N

    tol_rel = cfg.get("T_N_tol_rel", 0.05)
    err = abs(T_N_found - T_N_expected) / (T_N_expected + 1e-12)
    score = max(0.0, 1.0 - err / tol_rel)
    return score


# === block: score_2 (check id='energy_ordering_and_specific_heat') ===
def score_2(artifact, step, ctx):
    rows = artifact
    t_vals = np.array([float(r["T"]) for r in rows])
    mu_SDW = np.array([float(r["mu_SDW"]) for r in rows])
    E_SDW = np.array([float(r["E_SDW"]) for r in rows])
    E_F   = np.array([float(r["E_F"])   for r in rows])
    E_P   = np.array([float(r["E_P"])   for r in rows])
    C_SDW = np.array([float(r["C_SDW"]) for r in rows])
    cfg = step.get("config", {})
    mu_thr = cfg.get("mu_threshold", 1e-4)
    # find T_N index
    nz = np.where(mu_SDW <= mu_thr)[0]
    if len(nz) == 0:
        T_N_idx = len(t_vals) - 1
    else:
        T_N_idx = nz[0]
    # Energy ordering for T <= T_N
    if T_N_idx > 0:
        cond = (E_SDW[:T_N_idx+1] < E_F[:T_N_idx+1]) & (E_F[:T_N_idx+1] < E_P[:T_N_idx+1])
        ordering_score = float(np.mean(cond))
    else:
        ordering_score = 0.0
    # Specific heat jump: find maximum absolute difference in C_SDW near T_N
    window_frac = cfg.get("window_frac", 0.02)
    T_N_val = t_vals[T_N_idx] if T_N_idx < len(t_vals) else t_vals[-1]
    mask = np.abs(t_vals - T_N_val) <= window_frac * T_N_val if T_N_val > 0 else np.zeros_like(t_vals, dtype=bool)
    if np.sum(mask) >= 2:
        region = C_SDW[mask]
        jumps = np.abs(np.diff(region))
        max_jump = np.max(jumps) if len(jumps) > 0 else 0.0
        jump_thr = cfg.get("specific_heat_jump_threshold", 0.3)
        jump_score = min(1.0, max_jump / jump_thr) if jump_thr > 0 else 1.0
    else:
        jump_score = 0.0
    score = 0.6 * ordering_score + 0.4 * jump_score
    return score


# === block: score_3 (check id='temperature_range') ===
def score_3(artifact, step, ctx):
    rows = artifact
    t_vals = np.array([float(r["T"]) for r in rows])
    cfg = step.get("config", {})
    T_N_gold = cfg.get("T_N_gold", 0.052)
    factor = cfg.get("factor", 1.5)
    zero_thr = cfg.get("zero_t_threshold", 1e-6)
    # check max T
    max_T = np.max(t_vals)
    required = factor * T_N_gold
    if max_T < required:
        return 0.0
    # check T=0 row exists
    has_zero = np.any(np.abs(t_vals) <= zero_thr)
    return 1.0 if has_zero else 0.0


_SCORERS = {
    'zero_temp_energies': score_0,
    'critical_temperature': score_1,
    'energy_ordering_and_specific_heat': score_2,
    'temperature_range': score_3,
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
