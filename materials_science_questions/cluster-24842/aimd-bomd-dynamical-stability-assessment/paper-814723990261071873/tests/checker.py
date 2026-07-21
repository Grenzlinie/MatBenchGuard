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
    gold_table = spec.get('gold_table', {})
    tolerances = spec.get('tolerances', {})
    return {'gold_table': gold_table, 'tolerances': tolerances}


# === block: score_0 (check id='numeric_accuracy') ===
def score_0(artifact, step, ctx):
    gold = ctx['gold_table']
    tolerances = ctx['tolerances']
    total = 0
    correct = 0
    for row in artifact:
        sys = row.get('System')
        if sys not in gold:
            continue
        try:
            temp = int(row.get('Temperature_K'))
        except:
            continue
        sys_gold = gold[sys]
        temp_gold = sys_gold.get(str(temp), {})
        if not temp_gold:
            continue
        for field in ['L_ave_A','L_max_A','CED_kJ_cm3','vdW_kJ_cm3','Electrostatic_kJ_cm3','E_bind_kJ_mol','E_modulus_GPa','bulk_modulus_K_GPa','shear_modulus_G_GPa','K_G_ratio']:
            gold_val = temp_gold.get(field)
            if gold_val is None:
                continue
            agent_str = row.get(field)
            if agent_str is None or agent_str == '':
                continue
            try:
                agent_val = float(agent_str)
            except:
                continue
            tol = tolerances.get(field, 0.0)
            if abs(agent_val - gold_val) <= tol + 1e-9:
                correct += 1
            total += 1
    if total == 0:
        return 0.0
    return correct / total


# === block: score_1 (check id='trend_Lmax_ordering') ===
def score_1(artifact, step, ctx):
    # Check L_max(cocrystal) < L_max(composite) < L_max(epsilon-CL-20) at each temperature
    systems = ['cocrystal', 'composite', 'epsilon-CL-20']
    by_temp = {}
    for row in artifact:
        sys = row.get('System')
        if sys not in systems:
            continue
        try:
            temp = int(row.get('Temperature_K'))
            lmax_str = row.get('L_max_A')
            if lmax_str is None or lmax_str == '':
                continue
            lmax = float(lmax_str)
        except:
            continue
        by_temp.setdefault(temp, {})[sys] = lmax
    for temp in [245, 295, 345, 395, 445]:
        vals = by_temp.get(temp)
        if vals is None:
            return 0.0
        if vals.get('cocrystal') is None or vals.get('composite') is None or vals.get('epsilon-CL-20') is None:
            return 0.0
        if not (vals['cocrystal'] < vals['composite'] < vals['epsilon-CL-20']):
            return 0.0
    return 1.0


# === block: score_2 (check id='trend_Lmax_monotonic') ===
def score_2(artifact, step, ctx):
    # Check L_max increases monotonically with temperature for epsilon-CL-20, composite, cocrystal
    systems = ['epsilon-CL-20', 'composite', 'cocrystal']
    by_sys = {}
    for row in artifact:
        sys = row.get('System')
        if sys not in systems:
            continue
        try:
            temp = int(row.get('Temperature_K'))
            lmax_str = row.get('L_max_A')
            if lmax_str is None or lmax_str == '':
                continue
            lmax = float(lmax_str)
        except:
            continue
        if sys not in by_sys:
            by_sys[sys] = []
        by_sys[sys].append((temp, lmax))
    for sys in systems:
        pts = sorted(by_sys.get(sys, []), key=lambda x: x[0])
        if len(pts) < 2:
            return 0.0
        for i in range(1, len(pts)):
            if pts[i][1] <= pts[i-1][1] + 1e-9:
                return 0.0
    return 1.0


# === block: score_3 (check id='trend_CED_Ebind_decrease') ===
def score_3(artifact, step, ctx):
    # Check CED and E_bind decrease with temperature for composite and cocrystal
    systems = ['composite', 'cocrystal']
    fields = ['CED_kJ_cm3', 'E_bind_kJ_mol']
    by_sys_field = {}
    for row in artifact:
        sys = row.get('System')
        if sys not in systems:
            continue
        try:
            temp = int(row.get('Temperature_K'))
        except:
            continue
        for field in fields:
            val_str = row.get(field)
            if val_str is None or val_str == '':
                continue
            try:
                val = float(val_str)
            except:
                continue
            key = (sys, field)
            if key not in by_sys_field:
                by_sys_field[key] = []
            by_sys_field[key].append((temp, val))
    for (sys, field), pts in by_sys_field.items():
        pts.sort(key=lambda x: x[0])
        if len(pts) < 2:
            return 0.0
        for i in range(1, len(pts)):
            if pts[i][1] >= pts[i-1][1] - 1e-9:
                return 0.0
    return 1.0


# === block: score_4 (check id='trend_elastic_moduli_decrease') ===
def score_4(artifact, step, ctx):
    # Check E, K, G decrease with temperature for all four systems
    systems = ['epsilon-CL-20', 'composite', 'cocrystal', 'beta-HMX']
    fields = ['E_modulus_GPa', 'bulk_modulus_K_GPa', 'shear_modulus_G_GPa']
    by_sys_field = {}
    for row in artifact:
        sys = row.get('System')
        if sys not in systems:
            continue
        try:
            temp = int(row.get('Temperature_K'))
        except:
            continue
        for field in fields:
            val_str = row.get(field)
            if val_str is None or val_str == '':
                continue
            try:
                val = float(val_str)
            except:
                continue
            key = (sys, field)
            if key not in by_sys_field:
                by_sys_field[key] = []
            by_sys_field[key].append((temp, val))
    for (sys, field), pts in by_sys_field.items():
        pts.sort(key=lambda x: x[0])
        if len(pts) < 2:
            return 0.0
        for i in range(1, len(pts)):
            if pts[i][1] >= pts[i-1][1] - 1e-9:
                return 0.0
    return 1.0


# === block: score_5 (check id='trend_KG_larger') ===
def score_5(artifact, step, ctx):
    # Check K/G of composite and cocrystal > epsilon-CL-20 and beta-HMX
    systems_check = ['composite', 'cocrystal']
    ref_systems = ['epsilon-CL-20', 'beta-HMX']
    by_temp = {}
    for row in artifact:
        sys = row.get('System')
        try:
            temp = int(row.get('Temperature_K'))
        except:
            continue
        kg_str = row.get('K_G_ratio')
        if kg_str is None or kg_str == '':
            continue
        try:
            kg = float(kg_str)
        except:
            continue
        by_temp.setdefault(temp, {})[sys] = kg
    for temp, vals in by_temp.items():
        for csys in systems_check:
            if csys not in vals:
                return 0.0
            cv = vals[csys]
            for rsys in ref_systems:
                if rsys not in vals:
                    return 0.0
                if cv <= vals[rsys]:
                    return 0.0
    return 1.0


_SCORERS = {
    'numeric_accuracy': score_0,
    'trend_Lmax_ordering': score_1,
    'trend_Lmax_monotonic': score_2,
    'trend_CED_Ebind_decrease': score_3,
    'trend_elastic_moduli_decrease': score_4,
    'trend_KG_larger': score_5,
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
