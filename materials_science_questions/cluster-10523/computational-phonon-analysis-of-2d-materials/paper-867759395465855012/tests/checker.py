import os
import json
import csv

# === author imports / helpers ===
import csv, math


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
    return {"spec": spec}


# === block: score_0 (check id='equilibrium_gap_check') ===
def score_0(artifact, step, ctx):
    try:
        gap = float(artifact.strip())
    except:
        return 0.0
    if abs(gap - 0.012) <= 0.003:
        return 1.0
    else:
        return 0.0


# === block: score_1 (check id='gap_vs_Q_check') ===
def score_1(artifact, step, ctx):
    try:
        reader = csv.DictReader(artifact.splitlines())
        rows = list(reader)
    except:
        return 0.0
    criteria = step.get('criteria', {})
    sub_weights = step.get('sub_weights', {})
    expected_modes = criteria.get('expected_modes')
    closing_modes = criteria.get('closing_modes')
    non_closing = criteria.get('non_closing_mode')

    # Check columns
    if sorted(rows[0].keys()) != sorted(['mode_name','Q','gap_meV','topological_phase']):
        return 0.0
    seen_modes = set()
    Q_vals = {}
    gaps = {}
    phases = {}
    for r in rows:
        mode = r['mode_name']
        seen_modes.add(mode)
        q = float(r['Q'])
        g = float(r['gap_meV'])
        ph = r['topological_phase']
        Q_vals.setdefault(mode, []).append(q)
        gaps.setdefault(mode, []).append(g)
        phases.setdefault(mode, []).append(ph)

    score = 0.0
    # Mode identification
    if set(expected_modes) == seen_modes:
        score += sub_weights.get('mode_identification', 0.1)

    # Data completeness: Q range coverage and step
    q_range = criteria.get('Q_range_min'), criteria.get('Q_range_max')
    max_step = criteria.get('max_step', 0.1)
    complete = True
    for mode in expected_modes:
        qs = sorted(Q_vals.get(mode, []))
        if len(qs) < 2:
            complete = False
            break
        if qs[0] > q_range[0] + 0.05 or qs[-1] < q_range[1] - 0.05:
            complete = False
            break
        steps = [qs[i+1]-qs[i] for i in range(len(qs)-1)]
        if max(steps) > max_step + 0.02:
            complete = False
            break
    if complete:
        score += sub_weights.get('data_completeness', 0.15)

    # Closing detection: for each closing mode, min gap < threshold
    thresh_close = criteria.get('closing_threshold_meV', 2.0)
    all_close_ok = True
    for mode in closing_modes:
        g = gaps.get(mode, [])
        if not g or min(g) > thresh_close:
            all_close_ok = False
            break
    if all_close_ok:
        score += sub_weights.get('closing_detection', 0.3)

    # Non-closing detection: min gap > threshold
    thresh_non = criteria.get('non_closing_min_gap_meV', 5.0)
    g_non = gaps.get(non_closing, [])
    if g_non and min(g_non) > thresh_non:
        score += sub_weights.get('non_closing_detection', 0.15)

    # Phase flip: each closing mode must have both STI and WTI phases
    flip_ok = True
    for mode in closing_modes:
        ph = phases.get(mode, [])
        if not ('STI' in ph and 'WTI' in ph):
            flip_ok = False
            break
    if flip_ok:
        score += sub_weights.get('phase_flip_present', 0.2)

    # Ag27 critical Q near -0.25
    q27 = Q_vals.get('Ag27', [])
    g27 = gaps.get('Ag27', [])
    target_q = criteria.get('critical_Q_Ag27', -0.25)
    tol_q = criteria.get('critical_Q_tolerance', 0.1)
    if q27 and g27:
        # find Q where gap is minimal (within closing threshold)
        min_gap = min(g27)
        if min_gap <= thresh_close:
            q_min = q27[g27.index(min_gap)]
            if abs(q_min - target_q) <= tol_q:
                score += sub_weights.get('Ag27_critical_Q', 0.1)

    return min(1.0, score)


# === block: score_2 (check id='phase_diagram_2D_check') ===
def score_2(artifact, step, ctx):
    try:
        reader = csv.DictReader(artifact.splitlines())
        rows = list(reader)
    except:
        return 0.0
    criteria = step.get('criteria', {})
    sub_weights = step.get('sub_weights', {})

    # Check columns
    if sorted(rows[0].keys()) != sorted(['Q27','Q31','gap_meV','topological_phase']):
        return 0.0

    score = 0.0
    # Grid completeness: at least grid_points distinct points
    grid_points = len(rows)
    expected = criteria.get('grid_points', 49)
    if grid_points >= expected:
        score += sub_weights.get('grid_completeness', 0.2)

    # Phase labels valid
    valid_phases = {'STI', 'WTI'}
    phases_set = set(r['topological_phase'] for r in rows)
    if phases_set.issubset(valid_phases) and len(phases_set) > 0:
        score += sub_weights.get('phase_labels_valid', 0.1)

    # Line fitting: find points with small gap (close to Dirac line) and fit a line
    points = []
    for r in rows:
        gap = float(r['gap_meV'])
        if gap < 5.0:  # near gap closure
            points.append((float(r['Q27']), float(r['Q31'])))

    if len(points) >= 3:
        # Fit line a*Q31 + b*Q27 + c = 0 using least squares
        # minimize sum (a*i31 + b*i27 + c)^2 with constraint a^2+b^2=1
        # Solve by linear algebra, but we can approximate by normalizing
        A = []
        b = []
        for (x, y) in points:
            A.append([y, x, 1])
        # Use pseudo-inverse to get [a, b, c]
        import numpy as np
        try:
            sol, _, _, _ = np.linalg.lstsq(A, np.zeros(len(A)), rcond=None)
            a_fit, b_fit, c_fit = sol[0], sol[1], sol[2]
            # normalize
            norm = math.sqrt(a_fit**2 + b_fit**2)
            if norm > 1e-6:
                a_fit /= norm
                b_fit /= norm
                c_fit /= norm
            ref = criteria.get('reference_line', {})
            coeffs_ref = ref.get('coefficients', [10.0, 2.5, 0.75])
            tol = ref.get('tolerance', {'a':2.0,'b':1.0,'c':0.2})
            a_ref, b_ref, c_ref = coeffs_ref
            norm_ref = math.sqrt(a_ref**2 + b_ref**2)
            a_ref_n = a_ref / norm_ref
            b_ref_n = b_ref / norm_ref
            c_ref_n = c_ref / norm_ref
            # score based on closeness
            score_a = 1.0 if abs(a_fit - a_ref_n) <= tol['a'] else max(0, 1 - abs(a_fit-a_ref_n)/tol['a'])
            score_b = 1.0 if abs(b_fit - b_ref_n) <= tol['b'] else max(0, 1 - abs(b_fit-b_ref_n)/tol['b'])
            score_c = 1.0 if abs(c_fit - c_ref_n) <= tol['c'] else max(0, 1 - abs(c_fit-c_ref_n)/tol['c'])
            line_score = 0.4*score_a + 0.4*score_b + 0.2*score_c
        except:
            line_score = 0.0
    else:
        line_score = 0.0

    score += sub_weights.get('line_fitting', 0.7) * line_score
    return min(1.0, score)


_SCORERS = {
    'equilibrium_gap_check': score_0,
    'gap_vs_Q_check': score_1,
    'phase_diagram_2D_check': score_2,
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
