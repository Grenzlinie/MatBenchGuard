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


# === block: score_0 (check id='elastic_and_moduli') ===
def score_0(artifact, step, ctx):
    artifact = load_artifact(os.path.join('/app/outputs', step['output_file']))
    config = step['config']
    gold = config['gold']
    tols = config['tolerances']

    # Correct gold densities derived from the paper's VASP-optimised cell volumes
    # (LaNi2P2: V=153.66 Å³, LaNi2Ge2: V=175.43 Å³, Z=2) and molar masses.
    gold['LaNi2P2']['density_gcm3'] = 6.88
    gold['LaNi2Ge2']['density_gcm3'] = 7.60

    accuracy_score = 0.0
    total_fields = 0
    missing_fields = 0

    for comp in ['LaNi2P2', 'LaNi2Ge2']:
        if comp not in artifact:
            continue
        comp_data = artifact[comp]
        gold_comp = gold[comp]
        for key, gval in gold_comp.items():
            total_fields += 1
            val = comp_data.get(key)
            if val is None:
                missing_fields += 1
                continue
            if key.startswith('C'):
                tol = tols['Cij_rel'] * abs(gval)
            elif key in ('B_V','B_R','B_VRH','G_V','G_R','G_VRH','Y'):
                tol = tols['moduli_rel'] * abs(gval)
            elif key == 'density_gcm3':
                tol = tols['density_rel'] * abs(gval)
            elif key == 'molar_mass_gmol':
                tol = tols['molar_mass_rel'] * abs(gval)
            elif key == 'G_over_B':
                tol = tols['G_over_B_abs']
            elif key == 'nu':
                tol = tols['nu_abs']
            else:
                tol = 0.01
            if abs(val - gval) <= tol:
                accuracy_score += 1

    if total_fields > 0:
        accuracy_score = accuracy_score / total_fields
    else:
        accuracy_score = 0.0

    # structural checks: mechanical stability + G/B>0.5
    struct_score = 0.0
    struct_count = 0
    for comp in ['LaNi2P2', 'LaNi2Ge2']:
        if comp not in artifact:
            continue
        cdata = artifact[comp]
        try:
            C11 = cdata.get('C11')
            C12 = cdata.get('C12')
            C13 = cdata.get('C13')
            C33 = cdata.get('C33')
            C44 = cdata.get('C44')
            C66 = cdata.get('C66')
            if None in (C11,C12,C13,C33,C44,C66):
                continue
            stable1 = C11>0 and C33>0 and C44>0 and C66>0 and (C11-C12)>0 and (C11+C33-2*C13)>0 and (2*(C11+C12)+C33+4*C13)>0
            gb = cdata.get('G_over_B')
            if stable1 and gb is not None and gb > 0.5:
                struct_score += 1
        except:
            pass
        struct_count += 1

    if struct_count > 0:
        struct_score = struct_score / struct_count
    else:
        struct_score = 0.0

    step_score = 0.9 * accuracy_score + 0.1 * struct_score
    return step_score


# === block: score_1 (check id='thermophysical') ===
def score_1(artifact, step, ctx):
    artifact = load_artifact(os.path.join('/app/outputs', step['output_file']))
    config = step['config']
    gold = config['gold']
    tols = config['tolerances']

    vel_theta_keys = ['v_l','v_t','v_m','theta_D']
    vel_theta_ok = 0
    total_vel_theta = 0
    for comp in ['LaNi2P2', 'LaNi2Ge2']:
        if comp not in artifact:
            continue
        comp_data = artifact[comp]
        gold_comp = gold[comp]
        for key in vel_theta_keys:
            total_vel_theta += 1
            val = comp_data.get(key)
            gval = gold_comp[key]
            if key != 'theta_D':
                tol = tols['velocity_rel'] * abs(gval)
            else:
                tol = tols['theta_D_rel'] * abs(gval)
            if val is not None and abs(val-gval) <= tol:
                vel_theta_ok += 1

    vel_theta_score = vel_theta_ok / total_vel_theta if total_vel_theta > 0 else 0

    # heat capacity accuracy
    heat_ok = 0
    total_heat = 0
    for comp in ['LaNi2P2', 'LaNi2Ge2']:
        if comp not in artifact:
            continue
        comp_data = artifact[comp]
        hc = comp_data.get('heat_capacity')
        if not hc or not isinstance(hc, list):
            continue
        gold_hc = {item['T']: item['Cp'] for item in gold[comp]['heat_capacity']}
        for item in hc:
            T = item.get('T')
            Cp_val = item.get('Cp')
            if T is None or Cp_val is None:
                continue
            g_Cp = gold_hc.get(T)
            if g_Cp is None:
                continue
            tol = tols['Cp_rel'] * abs(g_Cp)
            total_heat += 1
            if abs(Cp_val - g_Cp) <= tol:
                heat_ok += 1

    heat_accuracy = heat_ok / total_heat if total_heat > 0 else 0

    # structural checks
    struct_score = 0.0
    struct_count = 0
    for comp in ['LaNi2P2', 'LaNi2Ge2']:
        if comp not in artifact:
            continue
        hc = artifact[comp].get('heat_capacity')
        if not hc or len(hc) < 2:
            continue
        try:
            temps = [item['T'] for item in hc]
            cps = [item['Cp'] for item in hc]
            pos = all(c > 0 for c in cps)
            inc = all(temps[i] < temps[i+1] for i in range(len(temps)-1)) and all(cps[i] < cps[i+1] for i in range(len(cps)-1))
            if pos and inc:
                struct_score += 1
        except:
            pass
        struct_count += 1

    # Cp(Ge) > Cp(P) at each common T
    if 'LaNi2P2' in artifact and 'LaNi2Ge2' in artifact:
        hc1 = artifact['LaNi2P2'].get('heat_capacity')
        hc2 = artifact['LaNi2Ge2'].get('heat_capacity')
        if hc1 and hc2:
            try:
                map1 = {item['T']: item['Cp'] for item in hc1 if 'T' in item and 'Cp' in item}
                map2 = {item['T']: item['Cp'] for item in hc2 if 'T' in item and 'Cp' in item}
                common = set(map1.keys()) & set(map2.keys())
                if common:
                    if all(map2[t] > map1[t] for t in common):
                        struct_score += 1
                struct_count += 1
            except:
                pass

    struct_score = struct_score / struct_count if struct_count > 0 else 0

    step_score = 0.5 * vel_theta_score + 0.3 * heat_accuracy + 0.2 * struct_score
    return step_score


_SCORERS = {
    'elastic_and_moduli': score_0,
    'thermophysical': score_1,
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
