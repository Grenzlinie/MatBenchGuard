import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math

def compute_mechanical_properties(rows):
    R_lengths, R_energies = [], []
    C_lengths, C_energies = [], []
    for r in rows:
        phase = r['phase'].strip()
        L = float(r['length'])
        E = float(r['energy'])
        if phase == 'R':
            R_lengths.append(L)
            R_energies.append(E)
        elif phase == 'C':
            C_lengths.append(L)
            C_energies.append(E)
    if not R_lengths or not C_lengths:
        raise ValueError('Missing data for one phase')
    idx_Rmin = min(range(len(R_energies)), key=lambda i: R_energies[i])
    idx_Cmin = min(range(len(C_energies)), key=lambda i: C_energies[i])
    L0_R = R_lengths[idx_Rmin]
    E0_R = R_energies[idx_Rmin]
    L0_C = C_lengths[idx_Cmin]
    E0_C = C_energies[idx_Cmin]
    deltaE = E0_C - E0_R

    def fit_local(lengths, energies, L0):
        mask = [abs(l - L0) < 0.1 for l in lengths]
        if sum(mask) < 3:
            mask = [abs(l - L0) < 0.2 for l in lengths]
        if sum(mask) < 3:
            mask = [True] * len(lengths)
        x = [l for l, m in zip(lengths, mask) if m]
        y = [e for e, m in zip(energies, mask) if m]
        n = len(x)
        s0 = n
        s1 = sum(x)
        s2 = sum(xi*xi for xi in x)
        s3 = sum(xi**3 for xi in x)
        s4 = sum(xi**4 for xi in x)
        t0 = sum(y)
        t1 = sum(xi*yi for xi, yi in zip(x, y))
        t2 = sum(xi*xi*yi for xi, yi in zip(x, y))
        det = s0*(s2*s4 - s3*s3) - s1*(s1*s4 - s2*s3) + s2*(s1*s3 - s2*s2)
        if abs(det) < 1e-12:
            if n < 2:
                return (0.0, 0.0, y[0] if n > 0 else 0.0)
            sxx = s2 - s1*s1/s0
            sxy = t1 - s1*t0/s0
            b = sxy / sxx if sxx != 0 else 0.0
            a = 0.0
            c = t0/s0 - b*s1/s0
            return a, b, c
        det_a = t2*(s1*s3 - s2*s2) - t1*(s2*s3 - s1*s4) + t0*(s2*s2 - s1*s3)
        det_b = s0*(t2*s3 - s1*s4) - t2*(s1*s3 - s2*s2) + t1*(s1*s2 - s0*s3)
        det_c = s0*(s2*t2 - s3*t1) - s1*(s1*t2 - s2*t1) + t0*(s1*s3 - s2*s2)
        a = det_a / det
        b = det_b / det
        c = det_c / det
        return a, b, c

    fit_R_abc = fit_local(R_lengths, R_energies, L0_R)
    a_R, b_R, c_R = fit_R_abc
    stiffness_R = 2 * a_R * L0_R
    fit_C_abc = fit_local(C_lengths, C_energies, L0_C)
    a_C, b_C, c_C = fit_C_abc
    stiffness_C = 2 * a_C * L0_C

    t = b_R - b_C
    A = 4 * a_R * (a_R - a_C)
    B = 4 * a_R * t
    C_eq = t*t + 4 * a_C * (c_R - c_C)
    disc = B*B - 4 * A * C_eq
    if disc < 0 or A == 0:
        raise ValueError('No real common tangent')
    L_R_tan = (-B + math.sqrt(disc)) / (2*A)
    alt = (-B - math.sqrt(disc)) / (2*A)
    if abs(alt - L0_R) < abs(L_R_tan - L0_R):
        L_R_tan = alt
    F_eV_per_A = 2 * a_R * L_R_tan + b_R
    tension_nN = F_eV_per_A * 1.602176634

    return {
        'deltaE': deltaE,
        'stiffness_R': stiffness_R,
        'stiffness_C': stiffness_C,
        'tension': tension_nN,
        'L0_R': L0_R,
        'L0_C': L0_C,
        'E0_R': E0_R,
        'E0_C': E0_C
    }


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
    return {'output_dir': '/app/outputs'}


# === block: score_0 (check id='step01_csv_shape') ===
def score_0(artifact, step, ctx):
    required_cols = {'phase', 'length', 'energy'}
    if not artifact or not all(col in artifact[0] for col in required_cols):
        return 0.0

    min_rows = step.get('min_rows', 5)
    tol = step.get('tolerance', 0)
    effective_min = max(0, min_rows - tol)

    phase_counts = {}
    for row in artifact:
        phase = row.get('phase', '').strip()
        phase_counts[phase] = phase_counts.get(phase, 0) + 1

    count_R = phase_counts.get('R', 0)
    count_C = phase_counts.get('C', 0)
    if count_R >= effective_min and count_C >= effective_min:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='step01_recompute_mechanical') ===
def score_1(artifact, step, ctx):
    try:
        props = compute_mechanical_properties(artifact)
        deltaE_target = step['deltaE_target']
        deltaE_tol = step['deltaE_tol']
        stiffness_R_target = step['stiffness_R_target']
        stiffness_R_tol_rel = step['stiffness_R_tol_rel']
        stiffness_C_target = step['stiffness_C_target']
        stiffness_C_tol_rel = step['stiffness_C_tol_rel']
        tension_target = step['tension_target']
        tension_tol = step['tension_tol']
        scores = []
        scores.append(1.0 if abs(props['deltaE'] - deltaE_target) <= deltaE_tol else 0.0)
        scores.append(1.0 if abs(props['stiffness_R'] - stiffness_R_target) / stiffness_R_target <= stiffness_R_tol_rel else 0.0)
        scores.append(1.0 if abs(props['stiffness_C'] - stiffness_C_target) / stiffness_C_target <= stiffness_C_tol_rel else 0.0)
        scores.append(1.0 if abs(props['tension'] - tension_target) <= tension_tol else 0.0)
        return sum(scores) / len(scores)
    except Exception:
        return 0.0


# === block: score_2 (check id='step02_consistency') ===
def score_2(artifact, step, ctx):
    csv_path = os.path.join(ctx['output_dir'], 'step01_energy_strain.csv')
    if not os.path.exists(csv_path):
        return 0.0
    with open(csv_path) as f:
        csv_reader = csv.DictReader(f)
        csv_rows = list(csv_reader)
    try:
        props = compute_mechanical_properties(csv_rows)
        json_deltaE = artifact.get('cohesive_energy_difference')
        json_kR = artifact.get('tensile_stiffness_R')
        json_kC = artifact.get('tensile_stiffness_C')
        json_tension = artifact.get('equilibrium_tension')
        if any(v is None for v in [json_deltaE, json_kR, json_kC, json_tension]):
            return 0.0
        if abs(json_deltaE - props['deltaE']) > 0.01:
            return 0.0
        if abs(json_kR - props['stiffness_R']) / abs(props['stiffness_R']) > 0.01:
            return 0.0
        if abs(json_kC - props['stiffness_C']) / abs(props['stiffness_C']) > 0.01:
            return 0.0
        if abs(json_tension - props['tension']) > 0.01:
            return 0.0
        return 1.0
    except Exception:
        return 0.0


# === block: score_3 (check id='step03_band_gap') ===
def score_3(artifact, step, ctx):
    try:
        gap = float(artifact.strip())
        target = step['target']
        tol = step['tol']
        if abs(gap - target) <= tol:
            return 1.0
        else:
            return 0.0
    except Exception:
        return 0.0


_SCORERS = {
    'step01_csv_shape': score_0,
    'step01_recompute_mechanical': score_1,
    'step02_consistency': score_2,
    'step03_band_gap': score_3,
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
