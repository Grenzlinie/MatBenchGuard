import os
import json
import csv

# === author imports / helpers ===
import numpy as np
import json
from itertools import combinations


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
    step = None
    for s in spec['steps']:
        if s['id'] == 'step_01_cluster_details':
            step = s
            break
    if step is None:
        return {}
    return {
        'gold_binding_energy': step['gold_binding_energy'],
        'gold_symmetries': step['gold_symmetries'],
        'tolerance_energy': step['tolerance_energy']
    }


# === block: score_0 (check id='step_01_cluster_details') ===
def score_0(artifact, step, ctx):
    if artifact is None:
        return 0.0
    gold_eb = ctx['gold_binding_energy']
    gold_sym = ctx['gold_symmetries']
    tol = ctx['tolerance_energy']

    D = 2.918
    a2 = 6.50
    a3 = 6.50
    re = 2.389
    c = [3.598, -11.609, 13.486, -18.174, -5.570, 79.210, -6.458, 23.383, -111.809, 9.705, 38.297]

    sqrt13 = np.sqrt(1/3)
    sqrt12 = np.sqrt(1/2)
    sqrt23 = np.sqrt(2/3)
    sqrt16 = np.sqrt(1/6)
    U = np.array([[sqrt13, sqrt13, sqrt13],
                  [0.0, sqrt12, -sqrt12],
                  [sqrt23, -sqrt16, -sqrt16]])

    def compute_V(positions):
        N = positions.shape[0]
        V2 = 0.0
        for i in range(N):
            for j in range(i+1, N):
                rij = np.linalg.norm(positions[i] - positions[j])
                rho = (rij - re)/re
                V2 += -D * (1 + a2*rho) * np.exp(-a2*rho)
        V3 = 0.0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    r1 = np.linalg.norm(positions[i] - positions[j])
                    r2 = np.linalg.norm(positions[i] - positions[k])
                    r3 = np.linalg.norm(positions[j] - positions[k])
                    rho1 = (r1 - re)/re
                    rho2 = (r2 - re)/re
                    rho3 = (r3 - re)/re
                    rhos = np.array([rho1, rho2, rho3])
                    Q = U @ rhos
                    Q1, Q2, Q3 = Q[0], Q[1], Q[2]
                    P = (c[0] + c[1]*Q1 + c[2]*Q1**2 + c[3]*(Q2**2 + Q3**2)
                         + c[4]*Q1**3 + c[5]*Q1*(Q2**2 + Q3**2)
                         + c[6]*(Q3**3 - 3*Q3*Q2**2)
                         + c[7]*Q1**4 + c[8]*Q1**2*(Q2**2 + Q3**2)
                         + c[9]*(Q2**2 + Q3**2)**2
                         + c[10]*Q1*(Q3**3 - 3*Q3*Q2**2))
                    V3 += D * P * np.exp(-a3 * Q1)
        return V2 + V3

    def numerical_gradient(positions):
        N = positions.shape[0]
        grad = np.zeros_like(positions)
        eps = 1e-5
        for i in range(N):
            for d in range(3):
                pos_plus = positions.copy()
                pos_plus[i, d] += eps
                pos_minus = positions.copy()
                pos_minus[i, d] -= eps
                E_plus = compute_V(pos_plus)
                E_minus = compute_V(pos_minus)
                grad[i, d] = (E_plus - E_minus) / (2*eps)
        return grad

    def numerical_hessian_eigenvalues(positions):
        N = positions.shape[0]
        M = 3*N
        eps = 1e-4
        hess = np.zeros((M, M))
        pos_flat = positions.flatten()
        base_grad = numerical_gradient(positions).flatten()
        for j in range(M):
            pos_pert = pos_flat.copy()
            pos_pert[j] += eps
            grad_plus = numerical_gradient(pos_pert.reshape(N,3)).flatten()
            pos_pert[j] -= 2*eps
            grad_minus = numerical_gradient(pos_pert.reshape(N,3)).flatten()
            hess[:, j] = (grad_plus - grad_minus) / (2*eps)
        hess = (hess + hess.T) / 2
        eigvals = np.linalg.eigvalsh(hess)
        return eigvals

    def score_cluster(n, entry):
        if entry.get('n_atoms') != n:
            return 0.0
        coord_data = entry['coordinates']
        positions = np.array([[x, y, z] for (el, x, y, z) in coord_data], dtype=float)
        V = compute_V(positions)
        binding_energy = -V / n
        ref_eb = gold_eb[str(n)]
        diff = abs(binding_energy - ref_eb)
        if diff <= tol:
            energy_score = 1.0
        else:
            energy_score = max(0.0, 1.0 - (diff - tol)/0.2)
        sym = entry.get('symmetry', '').strip().lower()
        allowed = [s.lower() for s in gold_sym[str(n)]]
        sym_score = 1.0 if sym in allowed else 0.0
        grad = numerical_gradient(positions)
        max_force = np.max(np.abs(grad))
        if max_force < 1.1e-4:
            force_score = 1.0
        else:
            force_score = max(0.0, 1.0 - (max_force - 1.1e-4)/1e-3)
        eigvals = numerical_hessian_eigenvalues(positions)
        min_eig = np.min(eigvals)
        hess_score = 1.0 if min_eig > -1e-3 else 0.0
        w_energy, w_sym, w_force, w_hess = 0.5, 0.2, 0.15, 0.15
        return w_energy*energy_score + w_sym*sym_score + w_force*force_score + w_hess*hess_score

    if not isinstance(artifact, list):
        return 0.0
    score_sum = 0.0
    count = 0
    for n in range(2, 9):
        found = [e for e in artifact if e.get('n_atoms') == n]
        if not found:
            score_sum += 0.0
            count += 1
        else:
            score_sum += score_cluster(n, found[0])
            count += 1
    return score_sum / count if count > 0 else 0.0


_SCORERS = {
    'step_01_cluster_details': score_0,
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
