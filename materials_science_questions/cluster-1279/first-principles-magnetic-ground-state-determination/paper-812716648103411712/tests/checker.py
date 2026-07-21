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


# === block: score_0 (check id='struct_thermo') ===
def score_0(artifact, step, ctx):
    # struct_thermo: compare a, E_f, E_c, T_C
    import math

    def score_value(val, gold, tol_abs=None, tol_rel=None):
        if val is None:
            return 0.0
        if tol_abs is not None:
            diff = abs(val - gold)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / (2 * tol_abs))
        if tol_rel is not None:
            denom = max(abs(gold), 1e-9)
            rel_diff = abs(val - gold) / denom
            if rel_diff <= tol_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_diff - tol_rel) / (2 * tol_rel))
        return 0.0

    config = step['config']
    compounds = config['compounds']
    fields = config['fields']
    artifact = artifact  # dict from JSON

    scores = []
    for c in compounds:
        comp_data = artifact.get(c, {})
        for fld in fields:
            name = fld['name']
            gold_val = fld['gold_per_compound'].get(c)
            agent_val = comp_data.get(name)
            if gold_val is None or agent_val is None:
                scores.append(0.0)
                continue
            tol_abs = fld.get('tol_abs')
            tol_rel = fld.get('tol_rel')
            s = score_value(agent_val, gold_val, tol_abs=tol_abs, tol_rel=tol_rel)
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='half_metallicity') ===
def score_1(artifact, step, ctx):
    # half_metallicity: compare VBM, CBM, E_g_up, E_g_HM; self-consistency, half-metallic condition, ordering
    import math

    def score_value(val, gold, tol_abs=None, tol_rel=None):
        if val is None:
            return 0.0
        if tol_abs is not None:
            diff = abs(val - gold)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / (2 * tol_abs))
        if tol_rel is not None:
            denom = max(abs(gold), 1e-9)
            rel_diff = abs(val - gold) / denom
            if rel_diff <= tol_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_diff - tol_rel) / (2 * tol_rel))
        return 0.0

    config = step['config']
    compounds = config['compounds']
    fields = config['fields']
    artifact = artifact

    # field scores
    field_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        for fld in fields:
            name = fld['name']
            gold_val = fld['gold_per_compound'].get(c)
            agent_val = data.get(name)
            if gold_val is None or agent_val is None:
                field_scores.append(0.0)
                continue
            tol_abs = fld.get('tol_abs')
            s = score_value(agent_val, gold_val, tol_abs=tol_abs)
            field_scores.append(s)

    field_mean = sum(field_scores) / len(field_scores) if field_scores else 0.0

    # self-consistency: E_g_up should equal CBM - VBM, E_g_HM = min(|VBM|,|CBM|)
    consistency_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        vbm = data.get('VBM')
        cbm = data.get('CBM')
        e_g_up = data.get('E_g_up')
        e_g_hm = data.get('E_g_HM')
        if None in (vbm, cbm, e_g_up, e_g_hm):
            consistency_scores.append(0.0)
            continue
        eg_up_calc = cbm - vbm
        diff_up = abs(e_g_up - eg_up_calc)
        s_up = 1.0 if diff_up <= 0.01 else max(0.0, 1.0 - diff_up/0.05)
        eg_hm_calc = min(abs(vbm), abs(cbm))
        diff_hm = abs(e_g_hm - eg_hm_calc)
        s_hm = 1.0 if diff_hm <= 0.01 else max(0.0, 1.0 - diff_hm/0.05)
        consistency_scores.append((s_up + s_hm) / 2.0)
    consistency_mean = sum(consistency_scores) / len(consistency_scores) if consistency_scores else 0.0

    # half-metallic condition: VBM < 0, CBM > 0, E_g_up > 0, E_g_HM > 0
    cond_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        vbm = data.get('VBM')
        cbm = data.get('CBM')
        egu = data.get('E_g_up')
        egh = data.get('E_g_HM')
        if None in (vbm, cbm, egu, egh):
            cond_scores.append(0.0)
            continue
        ok = (vbm < 0) and (cbm > 0) and (egu > 0) and (egh > 0)
        cond_scores.append(1.0 if ok else 0.0)
    cond_mean = sum(cond_scores) / len(cond_scores) if cond_scores else 0.0

    # ordering trends (paper: E_g_up increasing? Actually BeF3<MgF3<CaF3 then SrF3,BaF3 slightly lower but the trend is increasing then plateau. We'll check monotonic non-decreasing from Be to Ba for E_g_up, and decreasing for E_g_HM (paper says decreasing). If violated, give partial credit.
    order_score = 1.0
    egu_vals = []
    egh_vals = []
    for c in compounds:
        data = artifact.get(c, {})
        egu_vals.append(data.get('E_g_up', None))
        egh_vals.append(data.get('E_g_HM', None))
    if None not in egu_vals:
        for i in range(len(egu_vals)-1):
            if egu_vals[i] > egu_vals[i+1] + 0.5:  # allow slight decrease
                # check if the decrease is beyond tolerance; the paper has CaF3>SrF3 slightly; so allow some decrease but penalize large.
                diff = egu_vals[i] - egu_vals[i+1]
                if diff > 1.0:
                    order_score *= 0.8
    if None not in egh_vals:
        for i in range(len(egh_vals)-1):
            if egh_vals[i] < egh_vals[i+1] + 0.1:
                pass  # supposed decreasing; but allow small increase?
                # Actually should be decreasing: BeF3=0.599, MgF3=0.568, CaF3=0.566, SrF3=0.495, BaF3=0.411. So check if any later is larger by more than 0.05.
                if egh_vals[i+1] > egh_vals[i] + 0.05:
                    order_score *= 0.8

    # weights
    w_field = 0.85  # main numeric comparison
    w_cons = config.get('self_consistency_weight', 0.05)
    w_cond = config.get('half_metallic_condition_weight', 0.05)
    w_order = config.get('ordering_weight', 0.05)
    total_weight = w_field + w_cons + w_cond + w_order
    score = (w_field * field_mean + w_cons * consistency_mean + w_cond * cond_mean + w_order * order_score) / total_weight if total_weight > 0 else 0.0
    return score


# === block: score_2 (check id='magnetic_moments') ===
def score_2(artifact, step, ctx):
    # magnetic_moments: compare M_t, atomic moments, interstitial; integer moment and sum consistency
    import math

    def score_value(val, gold, tol_abs=None, tol_rel=None):
        if val is None:
            return 0.0
        if tol_abs is not None:
            diff = abs(val - gold)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / (2 * tol_abs))
        if tol_rel is not None:
            denom = max(abs(gold), 1e-9)
            rel_diff = abs(val - gold) / denom
            if rel_diff <= tol_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_diff - tol_rel) / (2 * tol_rel))
        return 0.0

    config = step['config']
    compounds = config['compounds']
    fields = config['fields']
    artifact = artifact

    field_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        for fld in fields:
            name = fld['name']
            gold_val = fld['gold_per_compound'].get(c)
            agent_val = data.get(name)
            if gold_val is None or agent_val is None:
                field_scores.append(0.0)
                continue
            tol_abs = fld.get('tol_abs')
            s = score_value(agent_val, gold_val, tol_abs=tol_abs)
            field_scores.append(s)
    field_mean = sum(field_scores) / len(field_scores) if field_scores else 0.0

    # integer magnetic moment: M_t should be 1.0 within 0.05
    int_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        mt = data.get('M_t')
        if mt is None:
            int_scores.append(0.0)
            continue
        s = 1.0 if abs(mt - 1.0) <= 0.05 else max(0.0, 1.0 - abs(mt - 1.0) / 0.2)
        int_scores.append(s)
    int_mean = sum(int_scores) / len(int_scores) if int_scores else 0.0

    # sum consistency: M_F_A + M_F_B + M_F_C + M_X + M_int should equal M_t (within 0.1)
    sum_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        mfa = data.get('M_F_A')
        mfb = data.get('M_F_B')
        mfc = data.get('M_F_C')
        mx = data.get('M_X')
        mint = data.get('M_int')
        mt = data.get('M_t')
        if None in (mfa, mfb, mfc, mx, mint, mt):
            sum_scores.append(0.0)
            continue
        calc_sum = mfa + mfb + mfc + mx + mint
        diff = abs(calc_sum - mt)
        s = 1.0 if diff <= 0.1 else max(0.0, 1.0 - diff / 0.3)
        sum_scores.append(s)
    sum_mean = sum(sum_scores) / len(sum_scores) if sum_scores else 0.0

    w_fields = 0.8
    w_int = 0.1
    w_sum = config.get('sum_consistency_weight', 0.1)
    total_w = w_fields + w_int + w_sum
    score = (w_fields * field_mean + w_int * int_mean + w_sum * sum_mean) / total_w
    return score


# === block: score_3 (check id='elastic_mechanical') ===
def score_3(artifact, step, ctx):
    # elastic_mechanical: compare elastic constants and moduli, mechanical stability conditions
    import math

    def score_value(val, gold, tol_abs=None, tol_rel=None):
        if val is None:
            return 0.0
        if tol_abs is not None:
            diff = abs(val - gold)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / (2 * tol_abs))
        if tol_rel is not None:
            denom = max(abs(gold), 1e-9)
            rel_diff = abs(val - gold) / denom
            if rel_diff <= tol_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_diff - tol_rel) / (2 * tol_rel))
        return 0.0

    config = step['config']
    compounds = config['compounds']
    fields = config['fields']
    artifact = artifact

    field_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        for fld in fields:
            name = fld['name']
            gold_val = fld['gold_per_compound'].get(c)
            agent_val = data.get(name)
            if gold_val is None or agent_val is None:
                field_scores.append(0.0)
                continue
            tol_abs = fld.get('tol_abs')
            tol_rel = fld.get('tol_rel')
            s = score_value(agent_val, gold_val, tol_abs=tol_abs, tol_rel=tol_rel)
            field_scores.append(s)
    field_mean = sum(field_scores) / len(field_scores) if field_scores else 0.0

    # mechanical stability: C44>0, C11>abs(C12), C11+2*C12>0
    stab_scores = []
    for c in compounds:
        data = artifact.get(c, {})
        c11 = data.get('C11')
        c12 = data.get('C12')
        c44 = data.get('C44')
        if None in (c11, c12, c44):
            stab_scores.append(0.0)
            continue
        cond1 = c44 > 0
        cond2 = c11 > abs(c12)
        cond3 = c11 + 2*c12 > 0
        s = 1.0 if (cond1 and cond2 and cond3) else 0.0
        stab_scores.append(s)
    stab_mean = sum(stab_scores) / len(stab_scores) if stab_scores else 0.0

    w_fields = 0.9
    w_stab = config.get('stability_weight', 0.1)
    total_w = w_fields + w_stab
    score = (w_fields * field_mean + w_stab * stab_mean) / total_w
    return score


# === block: score_4 (check id='strain_ranges') ===
def score_4(artifact, step, ctx):
    # strain_ranges: compare hydrostatic and tetragonal strain limits with relative tolerance
    import math

    def score_value(val, gold, tol_abs=None, tol_rel=None):
        if val is None:
            return 0.0
        if tol_abs is not None:
            diff = abs(val - gold)
            if diff <= tol_abs:
                return 1.0
            return max(0.0, 1.0 - (diff - tol_abs) / (2 * tol_abs))
        if tol_rel is not None:
            denom = max(abs(gold), 1e-9)
            rel_diff = abs(val - gold) / denom
            if rel_diff <= tol_rel:
                return 1.0
            return max(0.0, 1.0 - (rel_diff - tol_rel) / (2 * tol_rel))
        return 0.0

    config = step['config']
    compounds = config['compounds']
    fields = config['fields']
    artifact = artifact

    scores = []
    for c in compounds:
        data = artifact.get(c, {})
        hydro_range = data.get('hydrostatic_HM_range', {})
        tet_range = data.get('tetragonal_HM_range', {})
        # flatten to expected field names
        vals = {
            'hydrostatic_HM_min': hydro_range.get('min_strain') if isinstance(hydro_range, dict) else None,
            'hydrostatic_HM_max': hydro_range.get('max_strain') if isinstance(hydro_range, dict) else None,
            'tetragonal_HM_min_c_over_a': tet_range.get('min_c_over_a') if isinstance(tet_range, dict) else None,
            'tetragonal_HM_max_c_over_a': tet_range.get('max_c_over_a') if isinstance(tet_range, dict) else None
        }
        for fld in fields:
            name = fld['name']
            gold_val = fld['gold_per_compound'].get(c)
            agent_val = vals.get(name)
            if gold_val is None or agent_val is None:
                scores.append(0.0)
                continue
            tol_rel = fld.get('tol_rel')
            s = score_value(agent_val, gold_val, tol_rel=tol_rel)
            scores.append(s)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'struct_thermo': score_0,
    'half_metallicity': score_1,
    'magnetic_moments': score_2,
    'elastic_mechanical': score_3,
    'strain_ranges': score_4,
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
