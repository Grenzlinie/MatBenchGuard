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


# === block: score_0 (check id='check_lattice_constants') ===
def score_0(artifact, step, ctx):
    ref = step['config']['reference']
    tol = step['config']['tolerance']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        art = artifact[sys]
        if 'lattice_constants' not in art:
            continue
        lc = art['lattice_constants']
        ref_sys = ref[sys]
        for key in ['a','b','c']:
            if key not in lc or ref_sys[key] is None:
                continue
            val = lc[key]
            target = ref_sys[key]
            if not isinstance(val, (int, float)) or not isinstance(target, (int, float)):
                continue
            if abs(val - target) <= tol[key]:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (abs(val-target)-tol[key])/(0.5*tol[key]+1e-12))
            total += score_i
            count += 1
    score = total / count if count > 0 else 0.0
    return score


# === block: score_1 (check id='check_bulk_modulus') ===
def score_1(artifact, step, ctx):
    ref = step['config']['reference']
    tol_rel = step['config']['tolerance_relative']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        art = artifact[sys]
        if 'bulk_modulus' not in art:
            continue
        bm = art['bulk_modulus']
        ref_sys = ref[sys]
        for key in ['a','b','c']:
            ref_val = ref_sys[key]
            if ref_val is None:
                continue
            if key not in bm:
                continue
            val = bm[key]
            if val is None or not isinstance(val, (int, float)):
                continue
            target = ref_val
            if target == 0:
                score_i = 1.0 if abs(val) < 0.1 else 0.0
            else:
                rel_diff = abs(val - target) / abs(target)
                if rel_diff <= tol_rel:
                    score_i = 1.0
                else:
                    score_i = max(0.0, 1.0 - (rel_diff - tol_rel)/(2*tol_rel))
            total += score_i
            count += 1
    score = total / count if count > 0 else 0.0
    return score


# === block: score_2 (check id='check_diameter_buckling') ===
def score_2(artifact, step, ctx):
    ref = step['config']['reference']
    tol = step['config']['tolerance']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        art = artifact[sys]
        ref_sys = ref[sys]
        for prop in ['tubular_diameter', 'radial_buckling']:
            if prop not in art:
                continue
            val = art[prop]
            target = ref_sys[prop]
            if not isinstance(val, (int, float)) or not isinstance(target, (int, float)):
                continue
            if abs(val - target) <= tol[prop]:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (abs(val-target)-tol[prop])/(0.5*tol[prop]+1e-12))
            total += score_i
            count += 1
    score = total / count if count > 0 else 0.0
    return score


# === block: score_3 (check id='check_band_gap') ===
def score_3(artifact, step, ctx):
    ref = step['config']['reference']
    tol = step['config']['tolerance']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        art = artifact[sys]
        if 'band_gap' not in art:
            continue
        bg = art['band_gap']
        if sys == 'ISW_NTSi':
            if bg.get('value') is None and bg.get('transition') is None:
                score_i = 1.0
            else:
                score_i = 0.0
        else:
            val = bg.get('value')
            if val is None or not isinstance(val, (int, float)):
                score_val = 0.0
            else:
                target = ref[sys]['value']
                diff = abs(val - target)
                if diff <= tol['value']:
                    score_val = 1.0
                else:
                    score_val = max(0.0, 1.0 - (diff - tol['value'])/(2*tol['value']))
            trans = bg.get('transition')
            if trans is not None and isinstance(trans, str) and len(trans.strip()) > 0:
                score_trans = 1.0
            else:
                score_trans = 0.0
            score_i = 0.7 * score_val + 0.3 * score_trans
        total += score_i
        count += 1
    score = total / count if count > 0 else 0.0
    return score


# === block: score_4 (check id='check_effective_mass_velocity') ===
def score_4(artifact, step, ctx):
    ref_mass = step['config']['reference_effective_mass']
    ref_vel = step['config']['reference_velocity']
    tol_rel = step['config']['tolerance_relative']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        art = artifact[sys]
        mass_ok = True
        if 'effective_mass' in art:
            em = art['effective_mass']
            for band in ['CB','VB']:
                ref_val = ref_mass[sys][band]
                if ref_val is None:
                    expected = None
                else:
                    expected = ref_val
                actual = em.get(band)
                if actual is None and expected is None:
                    score_i = 1.0
                elif actual is None or expected is None or not isinstance(actual, (int, float)):
                    score_i = 0.0
                else:
                    if expected == 0:
                        score_i = 1.0 if abs(actual) < 1e-6 else 0.0
                    else:
                        rel_diff = abs(actual - expected) / abs(expected)
                        if rel_diff <= tol_rel:
                            score_i = 1.0
                        else:
                            score_i = max(0.0, 1.0 - (rel_diff - tol_rel)/(2*tol_rel))
                total += score_i
                count += 1
        if 'velocity_z' in art:
            vz = art['velocity_z']
            for band in ['CB','VB']:
                ref_val = ref_vel[sys][band]
                if ref_val is None:
                    expected = None
                else:
                    expected = ref_val
                actual = vz.get(band)
                if actual is None and expected is None:
                    score_i = 1.0
                elif actual is None or expected is None or not isinstance(actual, (int, float)):
                    score_i = 0.0
                else:
                    if expected == 0:
                        score_i = 1.0 if abs(actual) < 1e-6 else 0.0
                    else:
                        rel_diff = abs(actual - expected) / abs(expected)
                        if rel_diff <= tol_rel:
                            score_i = 1.0
                        else:
                            score_i = max(0.0, 1.0 - (rel_diff - tol_rel)/(2*tol_rel))
                total += score_i
                count += 1
    score = total / count if count > 0 else 0.0
    return score


# === block: score_5 (check id='check_charge_density') ===
def score_5(artifact, step, ctx):
    ref = step['config']['reference']
    tol = step['config']['tolerance']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    fields = ['s_C', 's_Si', 'p_C', 'p_Si', 'total']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        art = artifact[sys]
        if 'charge_density' not in art:
            continue
        cd = art['charge_density']
        ref_sys = ref[sys]
        for f in fields:
            if f not in cd:
                continue
            val = cd[f]
            target = ref_sys[f]
            if not isinstance(val, (int, float)) or not isinstance(target, (int, float)):
                continue
            if abs(val - target) <= tol:
                score_i = 1.0
            else:
                score_i = max(0.0, 1.0 - (abs(val-target)-tol)/(0.5*tol+1e-12))
            total += score_i
            count += 1
    score = total / count if count > 0 else 0.0
    return score


# === block: score_6 (check id='check_magnetization_trends') ===
def score_6(artifact, step, ctx):
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    mag_scores = []
    for sys in systems:
        if sys not in artifact:
            continue
        mag = artifact[sys].get('total_magnetization')
        if mag is not None and isinstance(mag, (int, float)) and abs(mag) < 0.001:
            mag_scores.append(1.0)
        else:
            mag_scores.append(0.0)
    mag_score = sum(mag_scores) / len(mag_scores) if mag_scores else 0.0
    order_score = 0.0
    try:
        c_values = []
        for sys in ['ISW_NT', 'ISW_NTC', 'ISW_NTSi']:
            lc = artifact.get(sys, {}).get('lattice_constants', {})
            c = lc.get('c')
            if isinstance(c, (int, float)):
                c_values.append(float(c))
        if len(c_values) == 3:
            if c_values[0] > c_values[1] - 0.01 and c_values[1] > c_values[2] - 0.01:
                order_score = 1.0
    except Exception:
        pass
    score = 0.6 * mag_score + 0.4 * order_score
    return score


# === block: score_7 (check id='check_symmetry') ===
def score_7(artifact, step, ctx):
    expected = step['config']['expected_symmetry_number']
    systems = ['ISW_NT', 'BSW_NT', 'ISW_NTC', 'ISW_NTSi']
    total = 0.0
    count = 0
    for sys in systems:
        if sys not in artifact:
            continue
        sn = artifact[sys].get('symmetry_number')
        if isinstance(sn, int) and sn == expected:
            score_i = 1.0
        else:
            score_i = 0.0
        total += score_i
        count += 1
    score = total / count if count > 0 else 0.0
    return score


_SCORERS = {
    'check_lattice_constants': score_0,
    'check_bulk_modulus': score_1,
    'check_diameter_buckling': score_2,
    'check_band_gap': score_3,
    'check_effective_mass_velocity': score_4,
    'check_charge_density': score_5,
    'check_magnetization_trends': score_6,
    'check_symmetry': score_7,
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
