import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.special import lambertw
import os as _ff_os
import json as _ff_json

# helper to compute nucleus side m(t) from Eq.(3) of the paper
def _m_t(t, a, b, m0):
    if a == 0.0:
        return 1.0 + (m0 - 1.0) * np.exp(t / b)
    else:
        z = (a * (m0 - 1) / b) * np.exp((1.0 / b) * (t + a * (m0 - 1)))
        w = lambertw(z).real
        return 1.0 + (b / a) * w

def _X_ext(t_arr, a, b, m0, J_st, t0, rho_seed):
    X = np.zeros_like(t_arr, dtype=float)
    if rho_seed > 0:
        X += rho_seed * (_m_t(t_arr, a, b, m0) ** 2)
    if J_st > 0:
        for i in range(len(t_arr)):
            t = t_arr[i]
            if t <= t0:
                continue
            tau = t - t0
            n_points = min(10000, max(100, int(tau * 10)))
            td = np.linspace(0.0, tau, n_points)
            md2 = _m_t(td, a, b, m0) ** 2
            integ = np.trapz(md2, td)
            X[i] += J_st * integ
    return X

def _M_KA(t_arr, ka):
    a, b, m0, J_st, t0, rho_seed = ka['a'], ka['b'], ka['m0'], ka['J_st'], ka['t0'], ka['rho_seed']
    X_ext = _X_ext(t_arr, a, b, m0, J_st, t0, rho_seed)
    X = 1.0 - np.exp(-X_ext)
    return 2.0 * X - 1.0

def _ff_validate_output_contract():
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
            except Exception as exc:
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
            if not schema.get("header", True):
                # no header was declared; skip column-name validation
                continue
            try:
                with open(path, newline="") as _f:
                    cols = set((_ff_csv.reader(_f, delimiter=delim).__next__() or []))
            except StopIteration:
                cols = set()
            except Exception as exc:
                violations.append(base + ": cannot read table (" + str(exc) + ")")
                continue
            required_cols = schema.get("required_columns", []) or []
            for col in required_cols:
                name = col.get("name") if isinstance(col, dict) else col
                if name and name not in cols:
                    violations.append(base + ": missing table column '" + str(name) + "'")
    return violations

def _ff_contract_gate():
    violations = _ff_validate_output_contract()
    if not violations:
        return
    _ff_os.makedirs("/logs/verifier", exist_ok=True)
    with open("/logs/verifier/reward.txt", "w") as _f:
        _f.write("0.0")
    with open("/logs/verifier/breakdown.json", "w") as _f:
        _ff_json.dump({"output_contract_violations": violations}, _f, indent=2)
    raise SystemExit(0)


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
    ctx = {}
    ctx['ka_params'] = spec['ka_params']
    ctx['percolation_gold'] = spec['percolation_gold']
    ctx['percolation_tolerances'] = spec['percolation_tolerances']
    ctx['outputs_dir'] = outputs_dir
    return ctx


# === block: score_0 (check id='homogeneous_mae') ===
def score_0(artifact, step, ctx):
    import os
    path = os.path.join(ctx['outputs_dir'], step['output_file'])
    try:
        data = np.loadtxt(path, delimiter=',', skiprows=0)  # no header
        if data.ndim != 2 or data.shape[1] < 2:
            return 0.0
        t_sim = data[:, 0]
        M_sim = data[:, 1]
    except Exception:
        return 0.0
    if len(t_sim) < 2:
        return 0.0
    # compute KA prediction
    try:
        M_ka = _M_KA(t_sim, ctx['ka_params']['homogeneous'])
        mae = np.mean(np.abs(M_sim - M_ka))
    except Exception:
        return 0.0
    threshold = step.get('threshold_mae', 0.05)
    if mae <= threshold:
        return 1.0
    else:
        # linear decay: score = 1 at threshold, 0 at 2*threshold
        score = max(0.0, 1.0 - (mae - threshold) / threshold)
        return float(score)


# === block: score_1 (check id='breakdown_mae') ===
def score_1(artifact, step, ctx):
    import os
    path = os.path.join(ctx['outputs_dir'], step['output_file'])
    try:
        data = np.loadtxt(path, delimiter=',', skiprows=0)
        if data.ndim != 2 or data.shape[1] < 2:
            return 0.0
        t_sim = data[:, 0]
        M_sim = data[:, 1]
    except Exception:
        return 0.0
    if len(t_sim) < 2:
        return 0.0
    try:
        M_ka = _M_KA(t_sim, ctx['ka_params']['breakdown'])
        mae = np.mean(np.abs(M_sim - M_ka))
    except Exception:
        return 0.0
    min_mae = step.get('min_mae', 0.2)
    if mae >= min_mae:
        return 1.0
    else:
        # linear partial credit: score = mae / min_mae
        return float(mae / min_mae)


# === block: score_2 (check id='percolation_check') ===
def score_2(artifact, step, ctx):
    import os
    path = os.path.join(ctx['outputs_dir'], step['output_file'])
    try:
        art = json.load(open(path))
    except Exception:
        return 0.0
    if not isinstance(art, dict):
        return 0.0
    gold = ctx['percolation_gold']
    tols = ctx['percolation_tolerances']
    passed = 0
    total = 0
    for k, g in gold.items():
        val = art.get(k)
        if val is None:
            continue
        total += 1
        tol = tols.get(k, 0.05)
        if abs(val - g) <= tol:
            passed += 1
    if total == 0:
        return 0.0
    return float(passed) / total


_SCORERS = {
    'homogeneous_mae': score_0,
    'breakdown_mae': score_1,
    'percolation_check': score_2,
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
