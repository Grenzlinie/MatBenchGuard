import os
import json
import csv

# === author imports / helpers ===
import csv
import math
import re


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


# === block: score_0 (check id='step_3_structure_and_stability') ===
def score_0(artifact, step, ctx):
    cfg = step.get('checks', {})
    props = cfg.get('properties', [])
    if not props or not isinstance(artifact, list):
        return 0.0
    data = {}
    for row in artifact:
        prop = row.get('property', '').strip()
        val_str = row.get('value', '').strip()
        unit = row.get('unit', '').strip()
        data[prop] = (val_str, unit)
    total = len(props)
    correct = 0.0
    for p in props:
        name = p['property']
        if name not in data:
            continue
        val_str, _ = data[name]
        if p.get('unit') == 'boolean':
            expected = p['expected']
            if str(val_str).lower() in ('true', '1', 'yes'):
                actual_bool = True
            else:
                actual_bool = False
            if actual_bool == expected:
                correct += 1.0
        else:
            try:
                val = float(val_str)
            except (ValueError, TypeError):
                continue
            target = p['target']
            tol = p.get('tolerance_abs', 0.0)
            if abs(val - target) <= tol:
                correct += 1.0
    return correct / total if total > 0 else 0.0


# === block: score_1 (check id='step_4_electronic_properties') ===
def score_1(artifact, step, ctx):
    cfg = step.get('checks', {})
    props = cfg.get('properties', [])
    if not props or not isinstance(artifact, list):
        return 0.0
    data = {}
    for row in artifact:
        prop = row.get('property', '').strip()
        unit = row.get('unit', '').strip()
        val_str = row.get('value', '').strip()
        data[prop] = (val_str, unit)
    total = len(props)
    correct = 0.0
    for p in props:
        name = p['property']
        if name not in data:
            continue
        val_str, _ = data[name]
        try:
            val = float(val_str)
        except (ValueError, TypeError):
            continue
        target = p['target']
        tol = p.get('tolerance_abs', 0.0)
        if abs(val - target) <= tol:
            correct += 1.0
    return correct / total if total > 0 else 0.0


# === block: score_2 (check id='step_5_mae_vs_strain') ===
def score_2(artifact, step, ctx):
    cfg = step.get('checks', {})
    strains_ref = cfg.get('strains', [])
    gold_mae = cfg.get('gold_mae', [])
    tol = cfg.get('tolerance_abs', 0.0)
    check_mono = cfg.get('check_monotonic', False)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    agent_map = {}
    for row in artifact:
        try:
            s = float(row['strain'])
            m = float(row['MAE'])
            agent_map[s] = m
        except (ValueError, KeyError, TypeError):
            continue
    total = len(strains_ref)
    if total == 0:
        return 0.0
    point_score = 0.0
    for s, g in zip(strains_ref, gold_mae):
        if s in agent_map:
            if abs(agent_map[s] - g) <= tol:
                point_score += 1.0
    points_frac = point_score / total
    mono_score = 0.0
    if check_mono:
        sorted_strains = sorted(agent_map.keys())
        if len(sorted_strains) >= 2:
            mono = True
            for i in range(len(sorted_strains)-1):
                if agent_map[sorted_strains[i]] >= agent_map[sorted_strains[i+1]]:
                    mono = False
                    break
            if mono:
                mono_score = 1.0
    return 0.8 * points_frac + 0.2 * mono_score


# === block: score_3 (check id='step_6_valley_polarization_vs_strain') ===
def score_3(artifact, step, ctx):
    cfg = step.get('checks', {})
    strains_ref = cfg.get('strains', [])
    gold_vp = cfg.get('gold_vp', [])
    tol = cfg.get('tolerance_abs', 0.0)
    check_mono = cfg.get('check_monotonic', False)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    agent_map = {}
    for row in artifact:
        try:
            s = float(row['strain'])
            v = float(row['valley_polarization'])
            agent_map[s] = v
        except (ValueError, KeyError, TypeError):
            continue
    total = len(strains_ref)
    if total == 0:
        return 0.0
    point_score = 0.0
    for s, g in zip(strains_ref, gold_vp):
        if s in agent_map:
            if abs(agent_map[s] - g) <= tol:
                point_score += 1.0
    points_frac = point_score / total
    mono_score = 0.0
    if check_mono:
        sorted_strains = sorted(agent_map.keys())
        if len(sorted_strains) >= 2:
            mono = True
            for i in range(len(sorted_strains)-1):
                if agent_map[sorted_strains[i]] >= agent_map[sorted_strains[i+1]]:
                    mono = False
                    break
            if mono:
                mono_score = 1.0
    return 0.8 * points_frac + 0.2 * mono_score


# === block: score_4 (check id='step_8_curie_temperature') ===
def score_4(artifact, step, ctx):
    cfg = step.get('checks', {})
    target = cfg.get('target', 0.0)
    tol = cfg.get('tolerance_abs', 0.0)
    if not isinstance(artifact, str):
        return 0.0
    import re
    match = re.search(r'([\d.]+)', artifact)
    if not match:
        return 0.0
    try:
        val = float(match.group(1))
    except ValueError:
        return 0.0
    if abs(val - target) <= tol:
        return 1.0
    # partial credit: linear decay outside tolerance, zero when deviation > tol*2
    if tol <= 0:
        return 0.0
    dev = abs(val - target)
    if dev >= 2*tol:
        return 0.0
    return max(0.0, 1.0 - (dev - tol) / tol)


# === block: score_5 (check id='step_9_curie_temperature_modulation') ===
def score_5(artifact, step, ctx):
    cfg = step.get('checks', {})
    rows_gold = cfg.get('rows', [])
    tol = cfg.get('tolerance_abs', 20.0)
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    agent_data = {}
    for row in artifact:
        try:
            s = float(row['strain'])
            d = float(row['doping'])
            tc = float(row['Tc'])
        except (ValueError, KeyError, TypeError):
            continue
        agent_data[(s, d)] = tc
    total = len(rows_gold)
    if total == 0:
        return 0.0
    correct = 0.0
    for gold_row in rows_gold:
        strain = gold_row['strain']
        doping = gold_row['doping']
        target = gold_row['Tc']
        key = (strain, doping)
        if key in agent_data:
            if abs(agent_data[key] - target) <= tol:
                correct += 1.0
    return correct / total


# === block: score_6 (check id='step_11_berry_and_ahc') ===
def score_6(artifact, step, ctx):
    cfg = step.get('checks', {})
    kpts = cfg.get('kpoints', [])
    if not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    agent = {}
    for row in artifact:
        kp = row.get('kpoint', '').strip()
        try:
            bc = float(row['berry_curvature'])
            ahc = float(row['anomalous_hall_conductivity'])
        except (ValueError, KeyError, TypeError):
            continue
        agent[kp] = (bc, ahc)

    total_checks = 0.0
    passed = 0.0

    # Per-kpoint berry checks (magnitude + sign)
    for ref in kpts:
        kp = ref['kpoint']
        if kp not in agent:
            total_checks += 2
            continue
        bc, _ = agent[kp]
        # berry curvature magnitude
        BC_target = ref['berry_target']
        bc_tol = ref['berry_tol_abs']
        if abs(bc - BC_target) <= bc_tol:
            passed += 1.0
        total_checks += 1.0
        # berry sign check
        sign_ok = False
        if ref.get('berry_sign_positive') and bc > 0:
            sign_ok = True
        elif ref.get('berry_sign_negative') and bc < 0:
            sign_ok = True
        if sign_ok:
            passed += 1.0
        total_checks += 1.0

    # Global maximum AHC check
    ahc_values = []
    for row in artifact:
        try:
            ahc = float(row.get('anomalous_hall_conductivity', 'nan'))
            if not math.isnan(ahc):
                ahc_values.append(ahc)
        except (ValueError, TypeError):
            continue

    if kpts:
        ahc_target = kpts[0].get('ahc_target', 0.0)
        ahc_tol = kpts[0].get('ahc_tol_abs', 5.0)
    else:
        ahc_target = 9.5
        ahc_tol = 5.0

    if ahc_values:
        max_ahc = max(ahc_values)
        if abs(max_ahc - ahc_target) <= ahc_tol:
            passed += 1.0
    else:
        # If no AHC value found, add check without pass
        pass
    total_checks += 1.0

    return passed / total_checks if total_checks > 0 else 0.0


_SCORERS = {
    'step_3_structure_and_stability': score_0,
    'step_4_electronic_properties': score_1,
    'step_5_mae_vs_strain': score_2,
    'step_6_valley_polarization_vs_strain': score_3,
    'step_8_curie_temperature': score_4,
    'step_9_curie_temperature_modulation': score_5,
    'step_11_berry_and_ahc': score_6,
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
