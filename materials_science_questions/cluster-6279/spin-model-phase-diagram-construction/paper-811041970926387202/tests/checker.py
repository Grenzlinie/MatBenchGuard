import os
import json
import csv

# === author imports / helpers ===
import numpy as np
from scipy.optimize import minimize_scalar, minimize

def nematic_phase_positive(delta1, delta2, delta=0.5, j0=0.8, k0=1.0):
    # Free energy for nematic (alpha=-pi/4), independent of Delta and J0
    def f(theta):
        s = np.sin(theta)
        s2 = s * s
        a = k0 * (1 + delta2 - 2 * delta1)
        b = k0 / 2.0 * (4 * delta1 - 3 - delta2)
        return a * s2 + b * s2 * s2
    res = minimize_scalar(f, bounds=(0, np.pi/2), method='bounded')
    theta_opt = res.x
    s_opt = np.sin(theta_opt)
    if s_opt < 1e-6:
        return 'N1'
    if s_opt > 1 - 1e-6:
        return 'N2'
    # angular phase
    if (4 * delta1 - 3 - delta2) > 0:
        return 'N_angle'
    # fallback
    return 'N1' if theta_opt < 1e-3 else 'N2'

def ferromagnetic_phase_positive(J0, K0, Delta, Delta1, Delta2):
    def free_energy(params):
        alpha, theta = params
        sin2a = np.sin(2 * alpha)
        cos2a = np.cos(2 * alpha)
        term1 = 0.5 * J0 * (1 - Delta) * cos2a ** 2
        term2 = 0.5 * K0 * (1 - Delta1 + (Delta1 - Delta2) * sin2a) * (1 - sin2a)
        factor = term1 + term2
        F = (factor * np.sin(theta) ** 2
             + (K0 / 8.0) * (4 * Delta1 - 3 - Delta2) * (1 - sin2a) ** 2 * np.sin(theta) ** 4
             - 0.5 * (J0 - K0 * Delta2) * cos2a ** 2)
        return F
    bounds = [(-np.pi/2, np.pi/2), (0, np.pi/2)]
    x0 = [0.0, 0.0]
    res = minimize(free_energy, x0, bounds=bounds, method='L-BFGS-B')
    alpha_opt, theta_opt = res.x
    m = np.cos(2 * alpha_opt)
    if abs(m) < 1e-6:
        return nematic_phase_positive(Delta1, Delta2)
    # ferromagnetic classification
    if theta_opt < 0.1:
        return 'FM_parallel'
    if theta_opt > np.pi/2 - 0.1:
        return 'QFM_perp'
    return 'QFM_angle'

def phase_negative(J0, K0):
    return 'FM_parallel' if J0 > K0 else 'N2'


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


# === block: score_0 (check id='nematic_phase_map') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    matched = 0
    total = 0
    for row in artifact:
        try:
            delta1 = float(row['delta1'])
            delta2 = float(row['delta2'])
            agent_phase = row['phase'].strip()
            expected = nematic_phase_positive(delta1, delta2)
            if agent_phase == expected:
                matched += 1
            total += 1
        except (KeyError, ValueError):
            continue
    return matched / total if total else 0.0


# === block: score_1 (check id='ferro_phase_check') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    pos_tests = artifact.get('positive_tests', [])
    neg_tests = artifact.get('negative_tests', [])
    all_tests = []
    for lst, is_neg in [(pos_tests, False), (neg_tests, True)]:
        for item in lst:
            try:
                J0 = float(item['J0'])
                K0 = float(item['K0'])
                Delta = float(item['Delta'])
                Delta1 = float(item['Delta1'])
                Delta2 = float(item['Delta2'])
                agent_phase = item['computed_phase'].strip()
                if is_neg:
                    expected = phase_negative(J0, K0)
                else:
                    expected = ferromagnetic_phase_positive(J0, K0, Delta, Delta1, Delta2)
                all_tests.append((agent_phase, expected))
            except (KeyError, ValueError):
                continue
    if not all_tests:
        return 0.0
    correct = sum(1 for a, e in all_tests if a == e)
    return correct / len(all_tests)


# === block: score_2 (check id='magnon_gap_check') ===
def score_2(artifact, step, ctx):
    tol = step.get('tolerance', 1e-6)
    test_points = artifact.get('test_points', [])
    if not test_points:
        return 0.0
    ok = 0
    for tp in test_points:
        try:
            e1 = abs(float(tp['epsilon1_gap']))
            e2 = abs(float(tp['epsilon2_gap']))
            if e1 <= tol and e2 <= tol:
                ok += 1
        except (KeyError, ValueError):
            continue
    return ok / len(test_points)


_SCORERS = {
    'nematic_phase_map': score_0,
    'ferro_phase_check': score_1,
    'magnon_gap_check': score_2,
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
