import os
import json
import csv

# === author imports / helpers ===
import numpy as np


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


# === block: score_0 (check id='precip_ordering') ===
def score_0(artifact, step, ctx):
    # artifact is a list of dicts with keys: t_over_tAS, phi_p_const, phi_p_var, xi_const, xi_var
    params = step.get('params', {})
    target_times = params.get('times', [0.05, 0.1, 0.15, 0.2])
    tolerance = params.get('tolerance', 0.01)

    if not artifact:
        return 0.0

    t_over = np.array([float(r['t_over_tAS']) for r in artifact])
    phi_p_const = np.array([float(r['phi_p_const']) for r in artifact])
    phi_p_var = np.array([float(r['phi_p_var']) for r in artifact])
    xi_const = np.array([float(r['xi_const']) for r in artifact])
    xi_var = np.array([float(r['xi_var']) for r in artifact])

    successes = 0
    total = 0
    for t in target_times:
        idx = np.argmin(np.abs(t_over - t))
        if abs(t_over[idx] - t) > tolerance:
            continue
        total += 2
        if phi_p_const[idx] > phi_p_var[idx]:
            successes += 1
        if xi_const[idx] > xi_var[idx]:
            successes += 1
    if total == 0:
        return 0.0
    return successes / total


# === block: score_1 (check id='precip_range') ===
def score_1(artifact, step, ctx):
    # Sanity check: values in [0,1] and roughly increasing
    if not artifact:
        return 0.0

    t_over = np.array([float(r['t_over_tAS']) for r in artifact])
    phi_p_const = np.array([float(r['phi_p_const']) for r in artifact])
    phi_p_var = np.array([float(r['phi_p_var']) for r in artifact])
    xi_const = np.array([float(r['xi_const']) for r in artifact])
    xi_var = np.array([float(r['xi_var']) for r in artifact])

    if np.any(phi_p_const < 0) or np.any(phi_p_const > 1) or np.any(phi_p_var < 0) or np.any(phi_p_var > 1):
        return 0.0
    if np.any(xi_const < 0) or np.any(xi_const > 1) or np.any(xi_var < 0) or np.any(xi_var > 1):
        return 0.0
    # Optional: check that phi_p_const is non-decreasing
    if np.any(np.diff(phi_p_const) < -1e-9):
        return 0.5
    return 1.0


# === block: score_2 (check id='sauter_ordering') ===
def score_2(artifact, step, ctx):
    # artifact: list of dicts with SMD_norm_const, SMD_norm_var, sigma_over_SMD_const, sigma_over_SMD_var
    params = step.get('params', {})
    target_times = params.get('times', [0.05, 0.1, 0.15, 0.2])
    tolerance = params.get('tolerance', 0.01)

    if not artifact:
        return 0.0

    t_over = np.array([float(r['t_over_tAS']) for r in artifact])
    SMD_const = np.array([float(r['SMD_norm_const']) for r in artifact])
    SMD_var = np.array([float(r['SMD_norm_var']) for r in artifact])
    sigma_const = np.array([float(r['sigma_over_SMD_const']) for r in artifact])
    sigma_var = np.array([float(r['sigma_over_SMD_var']) for r in artifact])

    successes = 0
    total = 0
    for t in target_times:
        idx = np.argmin(np.abs(t_over - t))
        if abs(t_over[idx] - t) > tolerance:
            continue
        total += 2
        if SMD_const[idx] > SMD_var[idx]:
            successes += 1
        if sigma_const[idx] < sigma_var[idx]:
            successes += 1
    if total == 0:
        return 0.0
    return successes / total


# === block: score_3 (check id='sauter_range') ===
def score_3(artifact, step, ctx):
    # Sanity: SMD in reasonable range, sigma/SMD positive
    if not artifact:
        return 0.0

    SMD_const = np.array([float(r['SMD_norm_const']) for r in artifact])
    SMD_var = np.array([float(r['SMD_norm_var']) for r in artifact])
    sigma_const = np.array([float(r['sigma_over_SMD_const']) for r in artifact])
    sigma_var = np.array([float(r['sigma_over_SMD_var']) for r in artifact])

    if np.any(SMD_const <= 0) or np.any(SMD_var <= 0) or np.any(SMD_const > 20) or np.any(SMD_var > 20):
        return 0.0
    if np.any(sigma_const < 0) or np.any(sigma_var < 0) or np.any(sigma_const > 1) or np.any(sigma_var > 1):
        return 0.0
    return 1.0


# === block: score_4 (check id='csd_peak') ===
def score_4(artifact, step, ctx):
    # Check CSD snapshots at t=0.1: variable peak near w=1.5, constant peak at larger w (5-9)
    if not artifact:
        return 0.0

    w = np.array([float(r['w']) for r in artifact])
    wf_const = np.array([float(r['wf_const_t01']) for r in artifact])
    wf_var   = np.array([float(r['wf_var_t01']) for r in artifact])

    # Variable case: peak location between 1.0 and 2.5
    idx_peak_var = np.argmax(wf_var)
    peak_w_var = w[idx_peak_var]
    peak_val_var = wf_var[idx_peak_var]

    score = 0.0
    if peak_val_var > 1e-6 and 1.0 <= peak_w_var <= 2.5:
        score += 0.5
    elif peak_val_var > 1e-6 and 0.5 <= peak_w_var <= 4.0:
        score += 0.25

    # Constant case: peak location > 5 (plateau near 6-7 expected)
    idx_peak_const = np.argmax(wf_const)
    peak_w_const = w[idx_peak_const]
    peak_val_const = wf_const[idx_peak_const]

    if peak_val_const > 1e-6 and peak_w_const > 5.0:
        score += 0.5
    elif peak_val_const > 1e-6 and peak_w_const > 3.0:
        score += 0.25

    return min(1.0, score)


_SCORERS = {
    'precip_ordering': score_0,
    'precip_range': score_1,
    'sauter_ordering': score_2,
    'sauter_range': score_3,
    'csd_peak': score_4,
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
