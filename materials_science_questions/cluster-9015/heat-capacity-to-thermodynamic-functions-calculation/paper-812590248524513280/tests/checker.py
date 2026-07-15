import os
import json
import csv

# === author imports / helpers ===
import csv
import json
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
    return {"spec": spec}


# === block: score_0 (check id='step_3_optimization') ===
def score_0(artifact, step, ctx):
    import json
    import math

    artifact_data = artifact
    if not isinstance(artifact_data, dict):
        return 0.0

    # lookup parameters; navigate JSON structure robustly
    def get_nested(d, *keys):
        for k in keys:
            if isinstance(d, dict) and k in d:
                d = d[k]
            else:
                return None
        return d

    alp = get_nested(artifact_data, 'AlP')  # assume key 'AlP'
    if alp is None:
        alp = get_nested(artifact_data, 'phases', 'AlP')
    if not isinstance(alp, dict):
        return 0.0

    liquid = get_nested(artifact_data, 'liquid')
    if liquid is None:
        liquid = get_nested(artifact_data, 'phases', 'liquid')

    ref = step.get('reference_parameters', {})
    checks = []

    # AlP parameters
    try:
        delta_h = float(alp.get('Delta_H_298', alp.get('Delta_H', alp.get('delta_H', alp.get('H298', None)))))
        ref_h = ref['AlP_delta_H']['value']
        tol_h = ref['AlP_delta_H']['tolerance']
        checks.append(1.0 if abs(delta_h - ref_h) <= tol_h else 0.0)
    except Exception:
        checks.append(0.0)

    try:
        s = float(alp.get('S_298', alp.get('S', alp.get('S298', None))))
        ref_s = ref['AlP_S']['value']
        tol_s = ref['AlP_S']['tolerance']
        checks.append(1.0 if abs(s - ref_s) <= tol_s else 0.0)
    except Exception:
        checks.append(0.0)

    # Cp coefficients
    cp = alp.get('Cp', {})
    if isinstance(cp, dict):
        a = float(cp.get('a', cp.get('A', None)))
        b = float(cp.get('b', cp.get('B', None)))
        c = float(cp.get('c', cp.get('C', None)))
    elif isinstance(cp, list) and len(cp) == 3:
        a, b, c = float(cp[0]), float(cp[1]), float(cp[2])
    else:
        a = float(alp.get('Cp_a', None))
        b = float(alp.get('Cp_b', None))
        c = float(alp.get('Cp_c', None))
    try:
        checks.append(1.0 if abs(a - ref['AlP_Cp_a']['value']) <= ref['AlP_Cp_a']['tolerance'] else 0.0)
    except:
        checks.append(0.0)
    try:
        checks.append(1.0 if abs(b - ref['AlP_Cp_b']['value']) <= ref['AlP_Cp_b']['tolerance'] else 0.0)
    except:
        checks.append(0.0)
    try:
        checks.append(1.0 if abs(c - ref['AlP_Cp_c']['value']) <= ref['AlP_Cp_c']['tolerance'] else 0.0)
    except:
        checks.append(0.0)

    # liquid Al-P parameters (Δg_AlP) - from liquid dict
    if isinstance(liquid, dict):
        dg = liquid.get('delta_g_AlP', liquid.get('Delta_g_AlP', None))
        if dg is None:
            # maybe stored as list [constant, T coefficient]
            dg = liquid.get('parameters', {}).get('AlP', None)
        if isinstance(dg, list) and len(dg) == 2:
            dg0, dg1 = float(dg[0]), float(dg[1])
        elif isinstance(dg, dict):
            dg0 = float(dg.get('a', dg.get('A', 0)))
            dg1 = float(dg.get('b', dg.get('B', 0)))
        else:
            dg0 = None
            dg1 = None
        if dg0 is not None:
            try:
                checks.append(1.0 if abs(dg0 - ref['liquid_dg_AlP_const']['value']) <= ref['liquid_dg_AlP_const']['tolerance'] else 0.0)
            except:
                checks.append(0.0)
        else:
            checks.append(0.0)
        if dg1 is not None:
            try:
                checks.append(1.0 if abs(dg1 - ref['liquid_dg_AlP_Tcoeff']['value']) <= ref['liquid_dg_AlP_Tcoeff']['tolerance'] else 0.0)
            except:
                checks.append(0.0)
        else:
            checks.append(0.0)
    else:
        checks.extend([0.0, 0.0])

    if not checks:
        return 0.0
    return sum(checks) / len(checks)


# === block: score_1 (check id='step_4_alp_diagram') ===
def score_1(artifact, step, ctx):
    import csv

    artifact_rows = artifact
    if not isinstance(artifact_rows, list) or not artifact_rows:
        return 0.0

    ref_data = step.get('reference_data', {})
    melting_ref = ref_data.get('melting_point', {})
    liquidus_pts = ref_data.get('liquidus_points', [])
    liq_tol = ref_data.get('liquidus_tolerance', 0.005)
    temp_tol = ref_data.get('temperature_match_tolerance', 1)

    score = 0.0
    total_checks = len(liquidus_pts) + 1  # including melting point

    # Check melting point row: find row with x_P = 0.5 (or near)
    found_melt = False
    for row in artifact_rows:
        try:
            x_p = float(row.get('x_P', 0))
            t_k = float(row.get('T_K', 0))
        except:
            continue
        if abs(x_p - 0.5) < 0.001:
            if abs(t_k - melting_ref.get('T_K', 2805.15)) <= melting_ref.get('tolerance', 50):
                found_melt = True
                break
    if found_melt:
        score += 1.0

    # Check liquidus points
    for q in liquidus_pts:
        target_T = q.get('T_K')
        target_xP = q.get('x_P')
        matched = False
        for row in artifact_rows:
            try:
                t_k = float(row.get('T_K', 0))
                x_p = float(row.get('x_P', 0))
            except:
                continue
            if abs(t_k - target_T) <= temp_tol:
                if abs(x_p - target_xP) <= liq_tol:
                    matched = True
                    break
        if matched:
            score += 1.0

    return score / total_checks if total_checks > 0 else 0.0


# === block: score_2 (check id='step_5_isotherms') ===
def score_2(artifact, step, ctx):
    import csv

    artifact_rows = artifact
    if not isinstance(artifact_rows, list) or not artifact_rows:
        return 0.0

    ref_points = step.get('reference_data', [])
    tolerance = step.get('tolerance', 0.02)
    if not ref_points:
        return 1.0  # no checks? shouldn't happen

    score = 0.0
    for rp in ref_points:
        target_T = rp.get('T_C')
        target_region = rp.get('region_label')
        target_comps = (rp.get('x_Fe'), rp.get('x_Al'), rp.get('x_P'))
        matched = False
        for row in artifact_rows:
            try:
                t = float(row.get('T_C', None))
                region = str(row.get('region_label', ''))
                x_fe = float(row.get('x_Fe'))
                x_al = float(row.get('x_Al'))
                x_p = float(row.get('x_P'))
            except:
                continue
            if t == target_T and region.lower().replace(' ', '') == target_region.lower().replace(' ', ''):
                dist = math.sqrt((x_fe - target_comps[0])**2 + (x_al - target_comps[1])**2 + (x_p - target_comps[2])**2)
                if dist <= tolerance:
                    matched = True
                    break
        if matched:
            score += 1.0

    return score / len(ref_points)


# === block: score_3 (check id='step_6_activity') ===
def score_3(artifact, step, ctx):
    import csv
    import math

    artifact_rows = artifact
    if not isinstance(artifact_rows, list) or not artifact_rows:
        return 0.0

    ref = step.get('reference_data', {})
    ref_points = ref.get('points', [])
    log_tol = ref.get('tolerance_log10', 0.5)
    wt_match_tol = ref.get('wt_Al_match_tolerance', 0.1)

    if not ref_points:
        return 1.0

    score = 0.0
    for rp in ref_points:
        target_T = rp.get('T_C')
        target_wt = rp.get('wt_Al')
        target_log = rp.get('log10_gamma_P')
        matched = False
        for row in artifact_rows:
            try:
                t = float(row.get('T_C'))
                wt_al = float(row.get('wt_Al'))
                log10 = float(row.get('log10_gamma_P'))
            except:
                continue
            if abs(t - target_T) < 1 and abs(wt_al - target_wt) <= wt_match_tol:
                if abs(log10 - target_log) <= log_tol:
                    matched = True
                    break
        if matched:
            score += 1.0

    return score / len(ref_points)


_SCORERS = {
    'step_3_optimization': score_0,
    'step_4_alp_diagram': score_1,
    'step_5_isotherms': score_2,
    'step_6_activity': score_3,
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
