import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import json
import csv


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
    gold = spec.get('gold', {})
    return dict(gold=gold)


# === block: score_0 (check id='step_01_csv') ===
def score_0(artifact, step, ctx):
    try:
        rows = artifact  # list of dicts
        if len(rows) < 5:
            return 0.0
        N_p = np.array([int(r['N_p']) for r in rows])
        energies = np.array([float(r['total_energy']) for r in rows])
        variances = np.array([float(r['var_local_energy']) for r in rows])
    except Exception:
        return 0.0

    # Variance-energy linear fit E = k*V + E_SE
    slope_v, intercept_v = np.polyfit(variances, energies, 1)
    e_se = intercept_v

    # Power-law fit E - E_SE = alpha * N_p^{-beta}
    residuals = energies - e_se
    if np.any(residuals <= 0):
        return 0.0
    log_res = np.log10(residuals)
    log_Np = np.log10(N_p)
    coeffs = np.polyfit(log_Np, log_res, 1)
    beta = -coeffs[0]

    # Gold
    G = ctx['gold']
    target_e_se = G['e_se']
    target_beta = G['beta']
    beta_tol = G.get('beta_tolerance', 0.05)
    e_se_thresh = G.get('e_se_full_credit_threshold', target_e_se)
    e_se_decay = G.get('e_se_decay_width', 0.001)

    # Score E_SE (monotonic: lower/more negative is better)
    if e_se <= e_se_thresh:
        s1 = 1.0
    else:
        diff = e_se - e_se_thresh
        s1 = max(0.0, 1.0 - diff / e_se_decay)

    # Score beta (exact match within tolerance)
    if abs(beta - target_beta) <= beta_tol:
        s2 = 1.0
    else:
        s2 = 0.0

    # Monotonicity: energies should be non-increasing (i.e., more negative)
    if all(energies[i+1] <= energies[i] for i in range(len(energies)-1)):
        s3 = 1.0
    else:
        s3 = 0.0

    return 0.5*s1 + 0.3*s2 + 0.2*s3


# === block: score_1 (check id='step_02_json') ===
def score_1(artifact, step, ctx):
    try:
        data = artifact
        if not isinstance(data, dict):
            return 0.0
        if 'power_law' not in data or 'variance_energy' not in data:
            return 0.0
        pl = data['power_law']
        ve = data['variance_energy']
        for k in ['alpha','beta','E_SE']:
            if k not in pl:
                return 0.0
            float(pl[k])
        for k in ['slope','intercept']:
            if k not in ve:
                return 0.0
            float(ve[k])
        return 1.0
    except Exception:
        return 0.0


_SCORERS = {
    'step_01_csv': score_0,
    'step_02_json': score_1,
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
