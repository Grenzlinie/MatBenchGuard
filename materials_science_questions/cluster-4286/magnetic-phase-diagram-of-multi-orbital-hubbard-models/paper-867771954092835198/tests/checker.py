import os
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
    return {}


# === block: score_0 (check id='phase_diagram') ===
def score_0(artifact, step, ctx):
    import math
    expected_rows = step['expected_rows']
    tol = step['tolerances']
    tol_m = tol['m_Os']
    tol_d = tol['Delta_D']
    tol_c = tol['Delta_C']
    exp_dict = {r['Ueff']: r for r in expected_rows}
    rows = artifact
    if not rows:
        return 0.0
    scores = []
    for row in rows:
        u = float(row['Ueff'])
        if u not in exp_dict:
            continue
        exp = exp_dict[u]
        # phase match
        phase_match = 1 if row['phase'].strip() == exp['phase'].strip() else 0
        # m_Os
        m = float(row['m_Os'])
        delta_m = abs(m - float(exp['m_Os']))
        score_m = max(0.0, 1.0 - delta_m / tol_m)
        # Delta_D
        dd = float(row['Delta_D'])
        delta_d = abs(dd - float(exp['Delta_D']))
        score_d = max(0.0, 1.0 - delta_d / tol_d)
        # Delta_C
        dc = float(row['Delta_C'])
        delta_c = abs(dc - float(exp['Delta_C']))
        score_c = max(0.0, 1.0 - delta_c / tol_c)
        row_score = (phase_match + score_m + score_d + score_c) / 4.0
        scores.append(row_score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='energy_comparison') ===
def score_1(artifact, step, ctx):
    rows = artifact
    diff_expected = step['expected_diff_ev']
    tol_rel = step['tol_rel']
    energies = {}
    for row in rows:
        key = row['magnetic_order'].strip()
        energies[key] = float(row['total_energy_per_Os'])
    if 'AIAO' not in energies or '3in1out' not in energies:
        return 0.0
    diff = energies['3in1out'] - energies['AIAO']
    if diff <= 0:
        return 0.0
    rel_err = abs(diff - diff_expected) / diff_expected
    if rel_err > 1.0:
        rel_err = 1.0
    return max(0.0, 1.0 - rel_err)


# === block: score_2 (check id='anisotropy_curve') ===
def score_2(artifact, step, ctx):
    import math
    import numpy as np
    rows = artifact
    gold_A_sia = step['gold_A_sia']
    gold_A_DM = step['gold_A_DM']
    tol_frac = step['tol_frac']
    theta_vals = []
    ediff_vals = []
    for r in rows:
        theta = float(r['theta'])
        if theta == 0.0:
            continue
        ed = float(r['energy_diff'])
        theta_vals.append(theta)
        ediff_vals.append(ed)
    if len(theta_vals) < 2:
        return 0.0
    theta_rad = np.radians(theta_vals)
    cos_th = np.cos(theta_rad)
    f = 1.0 - ((2.0 * cos_th + 1.0) ** 2) / 9.0
    coeff = 4.0 * math.sqrt(2.0) / 3.0
    g = coeff * (1.0 - cos_th)
    X = np.column_stack([f, g])
    y = np.array(ediff_vals)
    try:
        A_fit, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
        A_sia_fit = max(float(A_fit[0]), 0.0)
        A_DM_fit = max(float(A_fit[1]), 0.0)
    except Exception:
        return 0.0
    def param_score(fit, gold, tol):
        if gold == 0:
            return 1.0 if abs(fit) <= 1e-3 else 0.0
        rel = abs(fit - gold) / (tol * gold)
        return max(0.0, 1.0 - rel)
    score_sia = param_score(A_sia_fit, gold_A_sia, tol_frac)
    score_dm = param_score(A_DM_fit, gold_A_DM, tol_frac)
    return 0.5 * score_sia + 0.5 * score_dm


# === block: score_3 (check id='dos_near_MIT') ===
def score_3(artifact, step, ctx):
    import numpy as np
    rows = artifact
    energies = []
    dos_vals = []
    for row in rows:
        energies.append(float(row['energy']))
        dos_vals.append(float(row['DOS']))
    if not energies:
        return 0.0
    idx_zero = np.argmin(np.abs(np.array(energies) - 0.0))
    dos_EF = dos_vals[idx_zero]
    indices = [i for i, e in enumerate(energies) if -0.5 <= e <= 0.5]
    if not indices:
        return 0.0
    avg_dos = np.mean([dos_vals[i] for i in indices])
    if avg_dos == 0.0:
        return 1.0
    ratio = dos_EF / avg_dos
    if ratio <= 0.5:
        return 1.0
    else:
        return 0.0


_SCORERS = {
    'phase_diagram': score_0,
    'energy_comparison': score_1,
    'anisotropy_curve': score_2,
    'dos_near_MIT': score_3,
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
