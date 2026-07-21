import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='fitted_params') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    targets = params.get('targets', {})
    rel_tol = 0.05
    if not isinstance(artifact, dict):
        return 0.0
    required_keys = {'B_eff','T0','T0i','J_Co_J_Mn'}
    if not required_keys.issubset(artifact.keys()):
        return 0.0
    try:
        B_eff = float(artifact['B_eff'])
        T0 = float(artifact['T0'])
        T0i = float(artifact['T0i'])
        J_Co_J_Mn = float(artifact['J_Co_J_Mn'])
    except (ValueError, TypeError):
        return 0.0
    if B_eff <= 0 or T0 <= 0 or T0i <= 0 or J_Co_J_Mn <= 0:
        return 0.0
    passed = 0
    for key, target in targets.items():
        if key not in artifact:
            continue
        val = artifact[key]
        if abs(target) < 1e-12:
            continue
        if abs(val - target) / abs(target) <= rel_tol:
            passed += 1
    if len(targets) == 0:
        return 0.0
    return float(passed) / len(targets)


# === block: score_1 (check id='coupling_angle') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    rows = []
    for r in artifact:
        try:
            T = float(r.get('Temperature', None))
            phi = float(r.get('Coupling_angle', None))
            if T is None or phi is None:
                return 0.0
            rows.append((T, phi))
        except (ValueError, TypeError):
            return 0.0
    if not rows:
        return 0.0
    rows.sort(key=lambda x: x[0])
    T = [r[0] for r in rows]
    phi = [r[1] for r in rows]
    mono_ok = True
    for i in range(len(T)-1):
        if T[i+1] > T[i]:
            if phi[i+1] > phi[i] + 1e-9:
                mono_ok = False
                break
        # ignore decreasing T steps
    low_T_sample = float(params.get('low_T_sample', 10))
    high_T_sample = float(params.get('high_T_sample', 150))
    phi_low_range = params.get('phi_low_T_range', [50, 90])
    phi_high_bound = float(params.get('phi_high_T_bound', 5.0))
    # find nearest temp for low
    best_idx = min(range(len(T)), key=lambda i: abs(T[i]-low_T_sample))
    phi_low = phi[best_idx]
    low_ok = phi_low_range[0] <= phi_low <= phi_low_range[1]
    # high
    best_idx = min(range(len(T)), key=lambda i: abs(T[i]-high_T_sample))
    phi_high = phi[best_idx]
    high_ok = phi_high <= phi_high_bound
    score = 0.0
    if mono_ok:
        score += 0.5
    if low_ok:
        score += 0.25
    if high_ok:
        score += 0.25
    return score


# === block: score_2 (check id='exchange_energies') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    if not isinstance(artifact, list) or not artifact:
        return 0.0
    rows = []
    for r in artifact:
        try:
            T = float(r.get('Temperature', None))
            J1 = float(r.get('J1', None))
            J2 = float(r.get('J2', None))
            if T is None or J1 is None or J2 is None:
                return 0.0
            rows.append((T, J1, J2))
        except (ValueError, TypeError):
            return 0.0
    if not rows:
        return 0.0
    rows.sort(key=lambda x: x[0])
    T = [r[0] for r in rows]
    J1 = [r[1] for r in rows]
    J2 = [r[2] for r in rows]
    J1_sign_ok = all(v <= 0 for v in J1)
    J2_sign_ok = all(v >= 0 for v in J2)
    J1_mono_ok = True
    for i in range(len(T)-1):
        if T[i+1] > T[i]:
            if J1[i+1] < J1[i] - 1e-9:
                J1_mono_ok = False
                break
    J2_mono_ok = True
    for i in range(len(T)-1):
        if T[i+1] > T[i]:
            if J2[i+1] > J2[i] + 1e-9:
                J2_mono_ok = False
                break
    low_T_sample = float(params.get('low_T_sample', 10))
    J1_low_range = params.get('J1_low_T_range', [-0.0001, 0.0])
    J2_low_range = params.get('J2_low_T_range', [0.0, 0.0001])
    idx = min(range(len(T)), key=lambda i: abs(T[i]-low_T_sample))
    J1_low = J1[idx]
    J2_low = J2[idx]
    J1_range_ok = J1_low_range[0] <= J1_low <= J1_low_range[1]
    J2_range_ok = J2_low_range[0] <= J2_low <= J2_low_range[1]
    score = 0.0
    if J1_sign_ok:
        score += 0.15
    if J2_sign_ok:
        score += 0.15
    if J1_mono_ok:
        score += 0.2
    if J2_mono_ok:
        score += 0.2
    if J1_range_ok:
        score += 0.15
    if J2_range_ok:
        score += 0.15
    return score


_SCORERS = {
    'fitted_params': score_0,
    'coupling_angle': score_1,
    'exchange_energies': score_2,
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
