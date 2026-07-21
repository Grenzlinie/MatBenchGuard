import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from collections import defaultdict
import math
import os

def _bisect(f, a, b, tol=1e-12, max_iter=200):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    if abs(fa) < tol:
        return a
    if abs(fb) < tol:
        return b
    for _ in range(max_iter):
        m = (a + b) / 2.0
        fm = f(m)
        if abs(fm) < tol or (b - a) < tol:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2.0

# ---------- decorated dimer mapping ----------
def _Z(beta, h, Delta, D):
    sqrt2 = math.sqrt(2)
    Sp = np.array([[0, sqrt2, 0],
                   [0, 0, sqrt2],
                   [0, 0, 0]], dtype=float)
    Sm = Sp.T
    I2 = np.eye(3)
    S1p = np.kron(Sp, I2)
    S1m = np.kron(Sm, I2)
    S2p = np.kron(I2, Sp)
    S2m = np.kron(I2, Sm)
    Sz1 = np.kron(np.diag([1, 0, -1]), I2)
    Sz2 = np.kron(I2, np.diag([1, 0, -1]))
    H_heis = -((Delta/2) * (S1p @ S2m + S1m @ S2p) + Sz1 @ Sz2)
    H_field = -h * (Sz1 + Sz2)
    H_ani = -D * (Sz1 @ Sz1 + Sz2 @ Sz2)
    H = H_heis + H_field + H_ani
    eigvals = np.linalg.eigvalsh(H)
    return np.sum(np.exp(-beta * eigvals))

def _solve_Tc(Delta, D_JI):
    D = D_JI
    def objective(beta):
        Z1 = _Z(beta, 1.0, Delta, D)
        Z0 = _Z(beta, 0.0, Delta, D)
        return Z1 - math.sqrt(3) * Z0
    try:
        beta_c = _bisect(objective, 1e-3, 100.0)
    except ValueError:
        return 0.0
    return 1.0 / beta_c


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
    tolerance = 0.01
    sweeps_A = []
    for D_JI in [-0.5, 0.0, 0.5, 1.0, 2.0]:
        for Delta in np.arange(0.0, 3.01, 0.25):
            sweeps_A.append(('Delta', round(Delta, 10), D_JI, round(Delta, 10)))
    sweeps_B = []
    for Delta in [0.5, 1.0, 1.5, 2.0, 3.0]:
        for D_JI in np.arange(-0.5, 2.01, 0.25):
            sweeps_B.append(('D_J_I', round(D_JI, 10), D_JI, Delta))
    expected_groups = defaultdict(list)
    for param_type, pval, D_JI, Delta in sweeps_A:
        Tc = _solve_Tc(Delta, D_JI)
        expected_groups[(param_type, str(round(pval, 10)))].append(Tc)
    for param_type, pval, D_JI, Delta in sweeps_B:
        Tc = _solve_Tc(Delta, D_JI)
        expected_groups[(param_type, str(round(pval, 10)))].append(Tc)
    return {'expected_groups': dict(expected_groups), 'tolerance': tolerance}


# === block: score_0 (check id='tc_check') ===
def score_0(artifact, step, ctx):
    expected_groups = ctx['expected_groups']
    tolerance = ctx['tolerance']
    agent_groups = defaultdict(list)
    for row in artifact:
        param = str(row.get('param', '')).strip()
        param_value = str(row.get('param_value', '')).strip()
        Tc_str = str(row.get('T_c', '')).strip()
        try:
            Tc = float(Tc_str)
        except:
            continue
        agent_groups[(param, param_value)].append(Tc)
    total = len(expected_groups)
    correct = 0
    for key, expected_list in expected_groups.items():
        agent_list = agent_groups.get(key, [])
        if len(agent_list) != len(expected_list):
            continue
        exp_sorted = sorted(expected_list)
        agt_sorted = sorted(agent_list)
        if all(abs(a - e) <= tolerance for a, e in zip(agt_sorted, exp_sorted)):
            correct += 1
    score = (correct / total) if total > 0 else 1.0
    return score


_SCORERS = {
    'tc_check': score_0,
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
