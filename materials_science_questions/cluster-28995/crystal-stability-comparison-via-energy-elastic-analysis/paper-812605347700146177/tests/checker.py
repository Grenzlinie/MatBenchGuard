import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    return {}  # no shared preparation needed


# === block: score_0 (check id='check_force_shape') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, dict):
        return 0.0
    required_keys = {'0.48','0.42','0.36','0.33'}
    if not all(k in artifact for k in required_keys):
        return 0.0
    for k in required_keys:
        sub = artifact[k]
        if not isinstance(sub, dict) or 'J' not in sub or 'R' not in sub:
            return 0.0
        try:
            float(sub['J'])
            float(sub['R'])
        except (TypeError, ValueError):
            return 0.0
    return 1.0


# === block: score_1 (check id='check_moduli_shape') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, dict):
        return 0.0
    required_keys = {'0.48','0.42','0.36','0.33'}
    if not all(k in artifact for k in required_keys):
        return 0.0
    for k in required_keys:
        sub = artifact[k]
        if not isinstance(sub, dict) or 'C_FCC' not in sub or 'C_prime_FCC' not in sub:
            return 0.0
        try:
            float(sub['C_FCC'])
            float(sub['C_prime_FCC'])
        except (TypeError, ValueError):
            return 0.0
    return 1.0


# === block: score_2 (check id='check_moduli_self_consistency') ===
def score_2(artifact, step, ctx):
    # load force constants
    import os
    force_path = os.path.join('/app/outputs','force_constants.json')
    if not os.path.exists(force_path):
        return 0.0
    with open(force_path) as f:
        force_data = json.load(f)
    required_keys = ['0.48','0.42','0.36','0.33']
    if not all(k in force_data for k in required_keys):
        return 0.0
    # Constants
    Rs = 2.20
    Z = 3
    Z13 = Z ** (1.0/3.0)
    R_a = Rs * Z13
    Omega_a = (4.0*math.pi/3.0) * (R_a**3)
    factor = (4.0 * Omega_a) ** (-1.0/3.0)
    max_err = 0.0
    for k in required_keys:
        if k not in artifact or 'C_FCC' not in artifact[k] or 'C_prime_FCC' not in artifact[k]:
            continue
        sub_f = force_data.get(k, {})
        if 'J' not in sub_f or 'R' not in sub_f:
            continue
        J = float(sub_f['J'])
        R = float(sub_f['R'])
        C_computed = factor * (3.0 * J + R)
        Cp_computed = factor * (3.5 * J + 0.5 * R)
        C_sub = float(artifact[k]['C_FCC'])
        Cp_sub = float(artifact[k]['C_prime_FCC'])
        err = abs(C_computed - C_sub) / (abs(C_computed) + 1e-12)
        if err > max_err:
            max_err = err
        err = abs(Cp_computed - Cp_sub) / (abs(Cp_computed) + 1e-12)
        if err > max_err:
            max_err = err
    tolerance = step.get('tolerance', 1e-5)
    if max_err <= tolerance:
        return 1.0
    elif max_err >= 1.0:
        return 0.0
    else:
        return max(0.0, 1.0 - max_err / (10.0 * tolerance))


# === block: score_3 (check id='check_moduli_sign') ===
def score_3(artifact, step, ctx):
    expected = step.get('expected_signs', {})
    if not expected:
        return 0.0
    total = 0
    correct = 0
    for key, rules in expected.items():
        if key not in artifact:
            continue
        for field, sign in rules.items():
            if field not in artifact[key]:
                continue
            val = float(artifact[key][field])
            total += 1
            eps = 1e-12
            if sign == 'positive' and val > eps:
                correct += 1
            elif sign == 'negative' and val < -eps:
                correct += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_4 (check id='check_moduli_magnitude_plausible') ===
def score_4(artifact, step, ctx):
    rng = step.get('range', [1e-8, 1e-1])
    low, high = float(rng[0]), float(rng[1])
    for key in ['0.48','0.42','0.36','0.33']:
        if key in artifact:
            for fld in ['C_FCC','C_prime_FCC']:
                if fld in artifact[key]:
                    val = float(artifact[key][fld])
                    # check absolute magnitude so negative values are not rejected
                    if not (low <= abs(val) <= high):
                        return 0.0
    return 1.0


# === block: score_5 (check id='check_force_plausible') ===
def score_5(artifact, step, ctx):
    rng = step.get('range', [-0.1, 0.1])
    low, high = float(rng[0]), float(rng[1])
    for key in ['0.48','0.42','0.36','0.33']:
        if key in artifact:
            for fld in ['J','R']:
                if fld in artifact[key]:
                    val = float(artifact[key][fld])
                    if not (low <= val <= high):
                        return 0.0
    return 1.0


# === block: score_6 (check id='check_no_degenerate') ===
def score_6(artifact, step, ctx):
    vals = []
    for key in ['0.48','0.42','0.36','0.33']:
        if key in artifact and 'C_FCC' in artifact[key]:
            vals.append(float(artifact[key]['C_FCC']))
    if len(vals) < 2:
        return 0.0
    # compute standard deviation
    mean = sum(vals) / len(vals)
    var = sum((v - mean)**2 for v in vals) / len(vals)
    if var < 1e-26:
        return 0.0
    return 1.0


_SCORERS = {
    'check_force_shape': score_0,
    'check_moduli_shape': score_1,
    'check_moduli_self_consistency': score_2,
    'check_moduli_sign': score_3,
    'check_moduli_magnitude_plausible': score_4,
    'check_force_plausible': score_5,
    'check_no_degenerate': score_6,
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
