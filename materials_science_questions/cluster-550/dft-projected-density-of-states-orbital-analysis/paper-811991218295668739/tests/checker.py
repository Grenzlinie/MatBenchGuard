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
    ctx = {}
    steps = spec.get("steps", [])
    for step in steps:
        step_id = step.get("id")
        if "expected" in step:
            ctx[step_id] = step["expected"]
        else:
            ctx[step_id] = None
    return ctx


# === block: score_0 (check id='polymer_angles') ===
def score_0(artifact, step, ctx):
    expected = ctx.get("polymer_angles")
    if not artifact or not expected:
        return 0.0
    tolerances = expected.get("tolerances", {})
    gold_rows = expected.get("rows", [])
    total = len(gold_rows)
    if total == 0:
        return 0.0
    matched = 0
    for gold in gold_rows:
        found = False
        for row in artifact:
            if str(row.get("polymer_name","")).strip() == str(gold["polymer_name"]).strip() and \
               str(row.get("angle_type","")).strip() == str(gold["angle_type"]).strip():
                angle_ok = True
                try:
                    val = float(row.get("angle_value_deg", "nan"))
                    if abs(val - gold["angle_value_deg"]) > tolerances.get("angle_value_deg", 2.0):
                        angle_ok = False
                except:
                    angle_ok = False
                length_ok = True
                try:
                    val = float(row.get("repeat_length_A", "nan"))
                    if abs(val - gold["repeat_length_A"]) > tolerances.get("repeat_length_A", 0.05):
                        length_ok = False
                except:
                    length_ok = False
                if angle_ok and length_ok:
                    found = True
                    break
        if found:
            matched += 1
    return matched / total


# === block: score_1 (check id='doped_geometries') ===
def score_1(artifact, step, ctx):
    expected = ctx.get("doped_geometries")
    if not artifact or not expected:
        return 0.0
    tolerances = expected.get("tolerances", {})
    gold_rows = expected.get("rows", [])
    total = len(gold_rows)
    matched = 0
    for gold in gold_rows:
        found = False
        for row in artifact:
            if str(row.get("system","")).strip() == str(gold["system"]).strip() and \
               str(row.get("relaxation_type","")).strip() == str(gold["relaxation_type"]).strip():
                ok = True
                for field, tol in tolerances.items():
                    gold_val = gold.get(field)
                    if gold_val is None:
                        continue
                    try:
                        agent_val = float(row.get(field, "nan"))
                    except:
                        ok = False
                        break
                    if abs(agent_val - gold_val) > tol:
                        ok = False
                        break
                if ok:
                    found = True
                    break
        if found:
            matched += 1
    return matched / total


# === block: score_2 (check id='strain_energy') ===
def score_2(artifact, step, ctx):
    expected = ctx.get("strain_energy")
    if not artifact or not expected:
        return 0.0
    tolerances = expected.get("tolerances", {})
    gold_rows = expected.get("rows", [])
    total = len(gold_rows)
    matched = 0
    for gold in gold_rows:
        found = False
        for row in artifact:
            if str(row.get("system","")).strip() == str(gold["system"]).strip():
                try:
                    val = float(row.get("strain_energy_per_defect_eV", "nan"))
                except:
                    continue
                if abs(val - gold["strain_energy_per_defect_eV"]) <= tolerances.get("strain_energy_per_defect_eV", 0.15):
                    found = True
                    break
        if found:
            matched += 1
    return matched / total


# === block: score_3 (check id='adsorption_energy') ===
def score_3(artifact, step, ctx):
    expected = ctx.get("adsorption_energy")
    if not artifact or not expected:
        return 0.0
    tolerances = expected.get("tolerances", {})
    gold_rows = expected.get("rows", [])
    total = len(gold_rows)
    matched = 0
    for gold in gold_rows:
        found = False
        for row in artifact:
            if str(row.get("reaction","")).strip() == str(gold["reaction"]).strip():
                try:
                    val = float(row.get("adsorption_energy_eV", "nan"))
                except:
                    continue
                if abs(val - gold["adsorption_energy_eV"]) <= tolerances.get("adsorption_energy_eV", 0.15):
                    found = True
                    break
        if found:
            matched += 1
    return matched / total


# === block: score_4 (check id='structural_trends') ===
def score_4(artifact, step, ctx):
    import os
    import csv
    output_dir = "/app/outputs"
    def read_csv(filename):
        path = os.path.join(output_dir, filename)
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    polymer = read_csv("step_01_polymer_angles.csv")
    doped = read_csv("step_02_doped_geometries.csv")
    strain = read_csv("step_03_strain_energy.csv")
    adsorb = read_csv("step_04_adsorption_energy.csv")
    checks = 0
    passed = 0
    si_c_si_poly = None
    si_n_si_poly = None
    si_o_si_poly = []
    if polymer:
        for row in polymer:
            ang = row.get("angle_type","")
            try:
                val = float(row.get("angle_value_deg",""))
            except:
                continue
            if ang == "Si-C-Si":
                si_c_si_poly = val
            elif ang == "Si-N-Si":
                si_n_si_poly = val
            elif ang == "Si-O-Si":
                si_o_si_poly.append(val)
    checks += 1
    if si_c_si_poly is not None and si_n_si_poly is not None and len(si_o_si_poly)>=1:
        if si_c_si_poly < si_n_si_poly < max(si_o_si_poly):
            passed += 1
    si_c_si_doped = None
    si_n_si_doped = None
    if doped:
        for row in doped:
            sys = row.get("system","").strip()
            relax = row.get("relaxation_type","").strip()
            if sys == "1CH2-SOD" and relax == "f":
                try:
                    si_c_si_doped = float(row.get("SiXSi_angle_deg","nan"))
                except:
                    pass
            if sys == "1NH-SOD" and relax == "f":
                try:
                    si_n_si_doped = float(row.get("SiXSi_angle_deg","nan"))
                except:
                    pass
    checks += 1
    if si_c_si_doped is not None and si_n_si_doped is not None:
        if si_c_si_doped < si_n_si_doped:
            passed += 1
    checks += 1
    if strain:
        all_ok = True
        for row in strain:
            try:
                e = float(row.get("strain_energy_per_defect_eV","nan"))
            except:
                all_ok = False
                break
            if e > 0.2:
                all_ok = False
                break
        if all_ok:
            passed += 1
    checks += 1
    if adsorb:
        e_nh = None
        e_osi = None
        for row in adsorb:
            rxn = row.get("reaction","").strip()
            try:
                e = float(row.get("adsorption_energy_eV","nan"))
            except:
                continue
            if "Si-NH-Si" in rxn:
                e_nh = e
            elif "Si-O-Si" in rxn:
                e_osi = e
        if e_nh is not None and e_osi is not None:
            if (e_nh - e_osi) < -0.2:
                passed += 1
    if checks == 0:
        return 0.0
    return passed / checks


_SCORERS = {
    'polymer_angles': score_0,
    'doped_geometries': score_1,
    'strain_energy': score_2,
    'adsorption_energy': score_3,
    'structural_trends': score_4,
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
