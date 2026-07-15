import os
import json
import csv

# === author imports / helpers ===
import numpy as np

def _compute_mu_eff(k_val, v_val, kt_over_lambda):
    lam = -1.0
    Delta = v_val * lam
    ax = np.array([Delta/3, Delta/3, -2*Delta/3])
    S_z = np.diag([2,1,0,-1,-2])
    S_p = np.zeros((5,5))
    S_m = np.zeros((5,5))
    for m in range(5):
        ms = 2 - m
        if ms < 2:
            S_p[m-1, m] = np.sqrt(6 - ms*(ms+1))
        if ms > -2:
            S_m[m+1, m] = np.sqrt(6 - ms*(ms-1))
    S_x = (S_p + S_m) / 2
    S_y = (S_p - S_m) / (2j)
    L_z_c = np.diag([2,1,0,-1,-2])
    L_p_c = np.zeros((5,5))
    L_m_c = np.zeros((5,5))
    for m in range(5):
        ml = 2 - m
        if ml < 2:
            L_p_c[m-1, m] = np.sqrt(6 - ml*(ml+1))
        if ml > -2:
            L_m_c[m+1, m] = np.sqrt(6 - ml*(ml-1))
    L_x_c = (L_p_c + L_m_c) / 2
    L_y_c = (L_p_c - L_m_c) / (2j)
    U = np.zeros((5,3), dtype=complex)
    U[1,0] = 1/np.sqrt(2)
    U[3,0] = -1/np.sqrt(2)
    U[1,1] = -1j/np.sqrt(2)
    U[3,1] = -1j/np.sqrt(2)
    U[0,2] = 1/np.sqrt(2)
    U[4,2] = -1/np.sqrt(2)
    L_x = U.conj().T @ L_x_c @ U
    L_y = U.conj().T @ L_y_c @ U
    L_z = U.conj().T @ L_z_c @ U
    L_p = L_x + 1j*L_y
    L_m = L_x - 1j*L_y
    H_axial = np.diag(ax)
    H_axial_full = np.kron(H_axial, np.eye(5))
    LS = np.kron(L_z, S_z) + 0.5*(np.kron(L_p, S_m) + np.kron(L_m, S_p))
    H = H_axial_full + lam * LS
    evals, evecs = np.linalg.eigh(H)
    mu_z = k_val * np.kron(L_z, np.eye(5)) + 2 * np.kron(np.eye(3), S_z)
    mu_z_sq = mu_z @ mu_z
    mu2_diag = np.diag(evecs.conj().T @ mu_z_sq @ evecs)
    if kt_over_lambda == 0:
        return 0.0
    exp_vals = np.exp(evals / kt_over_lambda)
    Z = np.sum(exp_vals)
    if Z == 0:
        return 0.0
    mu2_avg = np.sum(mu2_diag * exp_vals) / Z
    return np.sqrt(np.abs(mu2_avg))


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


# === block: score_0 (check id='calc_moments') ===
def score_0(artifact, step, ctx):
    tolerance = step.get('tolerance', 1e-8)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    correct = 0
    total = 0
    for row in artifact:
        try:
            k = float(row['k'])
            v = float(row['v'])
            kt = float(row['kT_over_lambda'])
        except (ValueError, KeyError, TypeError):
            return 0.0
        if kt == 0:
            continue
        expected = _compute_mu_eff(k, v, kt)
        actual = float(row['mu_eff'])
        if abs(expected - actual) <= tolerance:
            correct += 1
        total += 1
    if total == 0:
        return 0.0
    return correct / total


_SCORERS = {
    'calc_moments': score_0,
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
