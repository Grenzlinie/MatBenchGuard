import os
import json
import csv

# === author imports / helpers ===
import math, csv, os


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


# === block: score_0 (check id='step_mode_csv') ===
def score_0(artifact, step, ctx):
    # structural audit for mode_gruneisen.csv
    required_cols = step['params']['required_columns']
    if not artifact or not all(all(c in row for c in required_cols) for row in artifact):
        return 0.0
    if len(artifact) < step['params']['min_rows']:
        return 0.0
    neg_count = sum(1 for row in artifact if float(row['gamma']) < 0.0)
    if neg_count < step['params']['min_negative_gamma']:
        return 0.0
    max_freq = step['params'].get('max_frequency', 10000)
    if any(float(row['frequency_cm1']) <= 0.0 or float(row['frequency_cm1']) > max_freq for row in artifact):
        return 0.0
    if any(int(row['degeneracy']) < 1 for row in artifact):
        return 0.0
    return 1.0


# === block: score_1 (check id='step_thermal_expansion') ===
def score_1(artifact, step, ctx):
    # recompute thermal expansion coefficient
    csv_path = os.path.join('/app/outputs', 'mode_gruneisen.csv')
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path, newline='') as f:
        modes = list(csv.DictReader(f))
    if not modes or not all(c in modes[0] for c in ['mode_index','frequency_cm1','gamma','degeneracy']):
        return 0.0
    try:
        freqs = [float(r['frequency_cm1']) for r in modes]
        gammas = [float(r['gamma']) for r in modes]
        degs = [int(r['degeneracy']) for r in modes]
    except (ValueError, KeyError):
        return 0.0
    if len(modes) < 30:
        return 0.0
    lat = artifact.get('relaxed_lattice_parameters')
    if not lat:
        return 0.0
    a = float(lat['a'])
    c = float(lat['c'])
    B0 = float(artifact.get('bulk_modulus_B0'))
    p = step['params']
    T = p['temperature_K']
    R = p['R']
    h = p['h']
    c_light = p['c_light']
    kB = p['kB']
    N_A = p['N_A']
    V_cell_A3 = a * a * c * math.sqrt(3.0) / 2.0
    V_m = V_cell_A3 * 1e-30 * N_A
    B0_Pa = B0 * 1e9
    C_total = 0.0
    gamma_weighted_sum = 0.0
    for freq, gamma, deg in zip(freqs, gammas, degs):
        x = h * c_light * 100.0 * freq / (kB * T)
        exp_x = math.exp(x)
        C_i = R * (x*x * exp_x) / ((exp_x - 1.0)**2)
        C_total += deg * C_i
        gamma_weighted_sum += deg * C_i * gamma
    if C_total == 0.0:
        return 0.0
    gamma_av = gamma_weighted_sum / C_total
    alpha = gamma_av * C_total / (3.0 * V_m * B0_Pa)
    target = p['target_alpha']
    rel_tol = p['rel_tol']
    relative_error = abs(alpha - target) / target
    if relative_error <= rel_tol:
        return 1.0
    score = max(0.0, 1.0 - (relative_error - rel_tol) / rel_tol)
    return score


_SCORERS = {
    'step_mode_csv': score_0,
    'step_thermal_expansion': score_1,
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
