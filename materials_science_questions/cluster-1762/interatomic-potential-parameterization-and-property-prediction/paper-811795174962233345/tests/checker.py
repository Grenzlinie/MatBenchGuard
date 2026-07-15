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


# === block: score_0 (check id='step_00') ===
def score_0(artifact, step, ctx):
    d = artifact
    step_def = step
    gold = step_def.get('gold', {})
    tol = step_def.get('tolerances', {})
    keys = ['TO1_frequency_cm-1', 'TO2_frequency_cm-1', 'TO3_frequency_cm-1', 'static_dielectric_constant', 'electronic_dielectric_constant']
    scores = []
    for k in keys:
        v = d.get(k)
        g = gold.get(k)
        if v is None or g is None:
            scores.append(0.0)
            continue
        t = tol.get(k, {})
        a_tol = t.get('abs')
        r_tol = t.get('rel')
        if a_tol is not None:
            if abs(v - g) <= a_tol:
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (abs(v - g) / a_tol)))
        elif r_tol is not None:
            if abs(v - g) <= r_tol * abs(g):
                scores.append(1.0)
            else:
                scores.append(max(0.0, 1.0 - (abs(v - g) / (r_tol * abs(g)))))
        else:
            scores.append(1.0 if v == g else 0.0)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='step_01') ===
def score_1(artifact, step, ctx):
    import math
    artifact = artifact
    step_def = step
    gold = step_def.get('gold', {})
    tols = step_def.get('tolerances', {})
    sub_weights = step_def.get('sub_weights', {})

    def get_tol_for_field(field):
        if 'energy' in field.lower() and 'eV' in field:
            return tols.get('energy_eV', {'abs':0.02,'rel':0.10})
        if 'displacement' in field.lower():
            return tols.get('displacement_A', {'abs':0.05})
        if 'polarization' in field.lower():
            return tols.get('polarization_Cm2', {'rel':0.20})
        if 'dipole' in field.lower():
            return tols.get('dipole_eA', {'rel':0.20})
        if field.startswith('A1'):
            if 'A6' in field:
                return tols.get('coeff_eV_per_A6', {'rel':0.50})
            else:
                return tols.get('coeff_eV_per_A4', {'rel':0.50})
        return {}

    def check_single(val, gold_val, tol_dict):
        if tol_dict.get('abs'):
            a_tol = tol_dict['abs']
            if abs(val - gold_val) <= a_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / a_tol))
        elif tol_dict.get('rel'):
            r_tol = tol_dict['rel']
            if gold_val == 0:
                return 1.0 if val == 0 else 0.0
            if abs(val - gold_val) <= r_tol * abs(gold_val):
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / (r_tol * abs(gold_val))))
        else:
            return 1.0 if val == gold_val else 0.0

    group1_fields = ['Li_energy_[001]_eV', 'Li_displacement_[001]_A', 'Li_energy_[110]_eV', 'Li_displacement_[110]_A', 'Li_energy_[111]_eV', 'Li_displacement_[111]_A']
    score1 = 0.0
    count1 = 0
    for f in group1_fields:
        if f in artifact and f in gold:
            score1 += check_single(artifact[f], gold[f], get_tol_for_field(f))
            count1 += 1
    group1_score = score1 / count1 if count1 else 0.0

    group2_fields = ['total_polarization_Cm2', 'total_dipole_eA', 'Li_dipole_contribution_eA', 'matrix_dipole_contribution_eA']
    score2 = 0.0
    count2 = 0
    for f in group2_fields:
        if f in artifact and f in gold:
            score2 += check_single(artifact[f], gold[f], get_tol_for_field(f))
            count2 += 1
    group2_score = score2 / count2 if count2 else 0.0

    coeff_fields = ['A1_eV_per_A2', 'A11_eV_per_A4', 'A12_eV_per_A4', 'A111_eV_per_A6', 'A112_eV_per_A6', 'A123_eV_per_A6']
    score3 = 0.0
    count3 = 0
    for f in coeff_fields:
        if f in artifact and f in gold:
            score3 += check_single(artifact[f], gold[f], get_tol_for_field(f))
            count3 += 1
    group3_score = score3 / count3 if count3 else 0.0

    struct_score = 0.0
    e001 = artifact.get('Li_energy_[001]_eV')
    e111 = artifact.get('Li_energy_[111]_eV')
    e110 = artifact.get('Li_energy_[110]_eV')
    if e001 is not None and e111 is not None and e110 is not None:
        if e001 < e111 and e111 < e110:
            struct_score += 0.5
    tdip = artifact.get('total_dipole_eA')
    ldip = artifact.get('Li_dipole_contribution_eA')
    mdip = artifact.get('matrix_dipole_contribution_eA')
    if tdip is not None and ldip is not None and mdip is not None:
        if abs(tdip - (ldip + mdip)) < 0.1:
            struct_score += 0.25
    disp001 = artifact.get('Li_displacement_[001]_A')
    if disp001 is not None and disp001 > 0:
        struct_score += 0.25

    w1 = sub_weights.get('energies_displacements', 0.4)
    w2 = sub_weights.get('polarization_dipole', 0.3)
    w3 = sub_weights.get('coefficients', 0.2)
    w4 = sub_weights.get('structural_checks', 0.1)
    total_score = w1*group1_score + w2*group2_score + w3*group3_score + w4*struct_score
    return min(max(total_score, 0.0), 1.0)


# === block: score_2 (check id='step_02') ===
def score_2(artifact, step, ctx):
    import math
    artifact = artifact
    step_def = step
    gold = step_def.get('gold', {})
    tols = step_def.get('tolerances', {}).get('energy_eV', {'abs':0.02,'rel':0.10})
    sub_weights = step_def.get('sub_weights', {})

    def check_single(val, gold_val, tol_dict):
        if tol_dict.get('abs'):
            a_tol = tol_dict['abs']
            if abs(val - gold_val) <= a_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / a_tol))
        elif tol_dict.get('rel'):
            r_tol = tol_dict['rel']
            if gold_val == 0:
                return 1.0 if val == 0 else 0.0
            if abs(val - gold_val) <= r_tol * abs(gold_val):
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / (r_tol * abs(gold_val))))
        else:
            return 1.0 if val == gold_val else 0.0

    energy_fields = ['config_a_energy_relative_to_undisplaced_eV', 'config_b_energy_relative_to_undisplaced_eV', 'config_c_energy_relative_to_undisplaced_eV', 'interaction_energy_config_a_eV', 'interaction_energy_config_b_eV', 'interaction_energy_config_c_eV']
    score_val = 0.0
    count = 0
    for f in energy_fields:
        if f in artifact and f in gold:
            score_val += check_single(artifact[f], gold[f], tols)
            count += 1
    value_score = score_val / count if count else 0.0

    struct = 0.0
    ia = artifact.get('interaction_energy_config_a_eV')
    ib = artifact.get('interaction_energy_config_b_eV')
    ic = artifact.get('interaction_energy_config_c_eV')
    if ia is not None and ib is not None and ic is not None:
        if ic < ib and ib < ia:
            struct += 0.5
        if ia > 0:
            struct += 0.25
        if ic < 0:
            struct += 0.25
    else:
        struct = 0.0

    w_val = sub_weights.get('energies_values', 0.6)
    w_struct = sub_weights.get('interaction_signs_and_ordering', 0.4)
    return min(max(w_val*value_score + w_struct*struct, 0.0), 1.0)


# === block: score_3 (check id='step_03') ===
def score_3(artifact, step, ctx):
    import math
    artifact = artifact
    step_def = step
    gold = step_def.get('gold', {})
    tols = step_def.get('tolerances', {}).get('barrier_eV', {'rel':0.20})
    sub_weights = step_def.get('sub_weights', {})

    def check_single(val, gold_val, tol_dict):
        if tol_dict.get('abs'):
            a_tol = tol_dict['abs']
            if abs(val - gold_val) <= a_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / a_tol))
        elif tol_dict.get('rel'):
            r_tol = tol_dict['rel']
            if gold_val == 0:
                return 1.0 if val == 0 else 0.0
            if abs(val - gold_val) <= r_tol * abs(gold_val):
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / (r_tol * abs(gold_val))))
        else:
            return 1.0 if val == gold_val else 0.0

    b111 = artifact.get('barrier_[111]_path_eV')
    b110 = artifact.get('barrier_[110]_path_eV')
    value_score = 0.0
    if b111 is not None and b110 is not None:
        s1 = check_single(b111, gold['barrier_[111]_path_eV'], tols)
        s2 = check_single(b110, gold['barrier_[110]_path_eV'], tols)
        value_score = (s1 + s2) / 2.0

    struct = 0.0
    if b111 is not None and b110 is not None:
        if b111 <= b110 and b111 > 0:
            struct = 1.0
        elif b111 <= b110:
            struct = 0.5
        elif b111 > 0:
            struct = 0.5
    else:
        struct = 0.0

    w_val = sub_weights.get('values', 0.7)
    w_struct = sub_weights.get('structural', 0.3)
    return min(max(w_val*value_score + w_struct*struct, 0.0), 1.0)


# === block: score_4 (check id='step_04') ===
def score_4(artifact, step, ctx):
    import math
    artifact = artifact
    step_def = step
    gold = step_def.get('gold', {})
    tols = step_def.get('tolerances', {})
    sub_weights = step_def.get('sub_weights', {})

    def check_single(val, gold_val, tol_dict):
        if tol_dict.get('abs'):
            a_tol = tol_dict['abs']
            if abs(val - gold_val) <= a_tol:
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / a_tol))
        elif tol_dict.get('rel'):
            r_tol = tol_dict['rel']
            if gold_val == 0:
                return 1.0 if val == 0 else 0.0
            if abs(val - gold_val) <= r_tol * abs(gold_val):
                return 1.0
            else:
                return max(0.0, 1.0 - (abs(val - gold_val) / (r_tol * abs(gold_val))))
        else:
            return 1.0 if val == gold_val else 0.0

    c1 = artifact.get('chain1_avg_distortion_A')
    c2 = artifact.get('chain2_avg_distortion_A')
    c3 = artifact.get('chain3_avg_distortion_A')
    lt = artifact.get('lateral_thickness_lattice_constants')

    chain_tol = tols.get('chain_distortion_A', {'abs':0.02})
    thick_tol = tols.get('thickness', {'abs':0.5})

    value_score = 0.0
    if c1 is not None and c2 is not None and c3 is not None and lt is not None:
        s1 = check_single(c1, gold['chain1_avg_distortion_A'], chain_tol)
        s2 = check_single(c2, gold['chain2_avg_distortion_A'], chain_tol)
        s3 = check_single(c3, gold['chain3_avg_distortion_A'], chain_tol)
        s4 = check_single(lt, gold['lateral_thickness_lattice_constants'], thick_tol)
        value_score = (s1+s2+s3+s4)/4.0

    struct = 0.0
    if c1 is not None and c2 is not None and c3 is not None:
        if c1 > c2 and c2 > c3:
            struct += 0.5
        if lt is not None and 1.0 <= lt <= 3.0:
            struct += 0.5
    else:
        struct = 0.0

    w_val = sub_weights.get('chain_distortions', 0.7)
    w_struct = sub_weights.get('thickness_and_ordering', 0.3)
    return min(max(w_val*value_score + w_struct*struct, 0.0), 1.0)


_SCORERS = {
    'step_00': score_0,
    'step_01': score_1,
    'step_02': score_2,
    'step_03': score_3,
    'step_04': score_4,
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
