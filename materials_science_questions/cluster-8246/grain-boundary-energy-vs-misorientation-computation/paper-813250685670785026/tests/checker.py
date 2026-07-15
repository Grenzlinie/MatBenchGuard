import os
import json
import csv

# === author imports / helpers ===
import csv
import os

def _extract_references(spec):
    refs = {}
    for step in spec.get('steps', []):
        refs[step['id']] = {
            'ref_values': step.get('reference_values', []),
            'tolerances': step.get('tolerances', {}),
            'trend_required': step.get('trend_required', [])
        }
    return refs


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
    refs = _extract_references(spec)
    return {'refs': refs}


# === block: score_0 (check id='tblg_results') ===
def score_0(artifact, step, ctx):
    ref_info = ctx['refs'].get(step['id'], {})
    tolerances = ref_info.get('tolerances', {})
    ref_values = ref_info.get('ref_values', [])
    trend_required = ref_info.get('trend_required', [])
    if not ref_values:
        return 0.0
    try:
        rows = {float(r['twist_angle_deg']): r for r in artifact}
    except Exception:
        return 0.0
    if len(rows) < len(ref_values):
        return 0.0
    total_points = len(ref_values) * 3
    matched_points = 0
    sorted_angles = sorted(ref_values, key=lambda x: x['twist_angle_deg'])
    strength_seq = []
    strain_seq = []
    agent_angles = []
    for ref in sorted_angles:
        ang = ref['twist_angle_deg']
        if ang not in rows:
            continue
        row = rows[ang]
        try:
            s_val = float(row['intrinsic_strength_GPa'])
            st_val = float(row['critical_failure_strain_percent'])
            m_val = float(row['Youngs_modulus_GPa'])
        except Exception:
            continue
        agent_angles.append(ang)
        strength_seq.append(s_val)
        strain_seq.append(st_val)
        if abs(s_val - ref['intrinsic_strength_GPa']) <= tolerances.get('strength_GPa', 5.0):
            matched_points += 1
        if abs(st_val - ref['critical_failure_strain_percent']) <= tolerances.get('strain_percent', 2.0):
            matched_points += 1
        if abs(m_val - ref['Youngs_modulus_GPa']) <= tolerances.get('modulus_GPa', 10.0):
            matched_points += 1
    value_score = matched_points / total_points if total_points > 0 else 0
    trend_ok = True
    for trend in trend_required:
        field = trend['field']
        direction = trend['direction']
        tol = trend.get('tolerance_for_small_violations', 0.5)
        if field == 'intrinsic_strength_GPa':
            seq = strength_seq
        elif field == 'critical_failure_strain_percent':
            seq = strain_seq
        else:
            continue
        if len(seq) < 2:
            trend_ok = False
            break
        if direction == 'decreasing':
            for i in range(1, len(seq)):
                if seq[i] > seq[i-1] + tol:
                    trend_ok = False
                    break
        elif direction == 'increasing':
            for i in range(1, len(seq)):
                if seq[i] < seq[i-1] - tol:
                    trend_ok = False
                    break
        if not trend_ok:
            break
    # Additional slope check: the decreasing trend must have a meaningful magnitude,
    # otherwise a flat constant guess passes the monotonicity check.
    if trend_ok and len(strength_seq) >= 2 and len(strain_seq) >= 2:
        angles_ref = [r['twist_angle_deg'] for r in sorted_angles]
        if angles_ref[-1] != angles_ref[0]:
            ref_slope_strength = (sorted_angles[-1]['intrinsic_strength_GPa'] - sorted_angles[0]['intrinsic_strength_GPa']) / (angles_ref[-1] - angles_ref[0])
            ref_slope_strain = (sorted_angles[-1]['critical_failure_strain_percent'] - sorted_angles[0]['critical_failure_strain_percent']) / (angles_ref[-1] - angles_ref[0])
        else:
            trend_ok = False
        if trend_ok:
            slope_strength = (strength_seq[-1] - strength_seq[0]) / (agent_angles[-1] - agent_angles[0])
            slope_strain = (strain_seq[-1] - strain_seq[0]) / (agent_angles[-1] - agent_angles[0])
            # The reference slope is negative; we require the agent's slope to be
            # negative and not too flat: at least 30% of the reference magnitude.
            min_frac = 0.3
            if slope_strength >= 0 or slope_strength > ref_slope_strength * min_frac:
                trend_ok = False
            if slope_strain >= 0 or slope_strain > ref_slope_strain * min_frac:
                trend_ok = False
    elif trend_ok:
        trend_ok = False  # insufficient data points
    trend_factor = 1.0 if trend_ok else 0.5
    final_score = 0.7 * value_score + 0.3 * trend_factor
    return final_score


# === block: score_1 (check id='blggb_results') ===
def score_1(artifact, step, ctx):
    ref_info = ctx['refs'].get(step['id'], {})
    tolerances = ref_info.get('tolerances', {})
    ref_values = ref_info.get('ref_values', [])
    trend_required = ref_info.get('trend_required', [])
    if not ref_values:
        return 0.0
    try:
        configs = {}
        for r in artifact:
            ang = float(r['misorientation_angle_deg'])
            orient = r.get('orientation_type', '').strip().lower()
            configs[(ang, orient)] = r
    except Exception:
        return 0.0
    if len(configs) < len(ref_values):
        return 0.0
    total_points = len(ref_values) * 3
    matched_points = 0
    zigzag_seq = []
    armchair_seq = []
    strain_zigzag = []
    strain_armchair = []
    for ref in ref_values:
        ang = ref['misorientation_angle_deg']
        orient = ref['orientation_type'].strip().lower()
        key = (ang, orient)
        if key not in configs:
            continue
        row = configs[key]
        try:
            s_val = float(row['intrinsic_strength_GPa'])
            st_val = float(row['critical_failure_strain_percent'])
            m_val = float(row['Youngs_modulus_GPa'])
        except Exception:
            continue
        if orient == 'zigzag':
            zigzag_seq.append((ang, s_val))
            strain_zigzag.append((ang, st_val))
        else:
            armchair_seq.append((ang, s_val))
            strain_armchair.append((ang, st_val))
        if abs(s_val - ref['intrinsic_strength_GPa']) <= tolerances.get('strength_GPa', 5.0):
            matched_points += 1
        if abs(st_val - ref['critical_failure_strain_percent']) <= tolerances.get('strain_percent', 2.0):
            matched_points += 1
        if abs(m_val - ref['Youngs_modulus_GPa']) <= tolerances.get('modulus_GPa', 10.0):
            matched_points += 1
    value_score = matched_points / total_points if total_points > 0 else 0
    def check_trend(seq, direction, tol=0.5):
        if len(seq) < 2:
            return False
        seq_sorted = sorted(seq, key=lambda x: x[0])
        vals = [x[1] for x in seq_sorted]
        if direction == 'increasing':
            for i in range(1, len(vals)):
                if vals[i] < vals[i-1] - tol:
                    return False
        elif direction == 'decreasing':
            for i in range(1, len(vals)):
                if vals[i] > vals[i-1] + tol:
                    return False
        return True
    trend_ok = True
    for trend in trend_required:
        field = trend['field']
        direction = trend['direction']
        groups = trend.get('group_by', None)
        tol = trend.get('tolerance_for_small_violations', 0.5)
        if field == 'intrinsic_strength_GPa':
            if groups == 'orientation_type':
                if not (check_trend(zigzag_seq, direction, tol) and check_trend(armchair_seq, direction, tol)):
                    trend_ok = False
                    break
            else:
                seq = zigzag_seq + armchair_seq
                if not check_trend(seq, direction, tol):
                    trend_ok = False
                    break
        elif field == 'critical_failure_strain_percent':
            if groups == 'orientation_type':
                if not (check_trend(strain_zigzag, direction, tol) and check_trend(strain_armchair, direction, tol)):
                    trend_ok = False
                    break
            else:
                seq = strain_zigzag + strain_armchair
                if not check_trend(seq, direction, tol):
                    trend_ok = False
                    break
    trend_factor = 1.0 if trend_ok else 0.5
    final_score = 0.7 * value_score + 0.3 * trend_factor
    return final_score


_SCORERS = {
    'tblg_results': score_0,
    'blggb_results': score_1,
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
