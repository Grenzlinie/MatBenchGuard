import os
import json
import csv

# === author imports / helpers ===
import json, re, math


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


# === block: score_0 (check id='shape_completeness') ===
def score_0(artifact, step, ctx):
    import re
    simulations = artifact.get("simulations")
    if not isinstance(simulations, list) or not simulations:
        return 0.0
    req_fields = ["chirality","temperature","max_shear_stress_GPa","critical_twist_angle_deg","interaction_force_at_500deg_eV_Ang"]
    by_key = {}
    pure_entry = None
    for s in simulations:
        if not isinstance(s, dict):
            return 0.0
        for f in req_fields:
            if f not in s:
                return 0.0
        chir = s.get("chirality", "")
        temp = s.get("temperature")
        if not isinstance(temp, int):
            return 0.0
        key = (chir, temp)
        by_key[key] = s
        if re.search(r"pure", chir, re.I) and temp == 300:
            pure_entry = s
    required = [("(11,11)",300),("(11,11)",500),("(11,11)",700),("(13,13)",300),("(15,15)",300)]
    for c,t in required:
        if (c,t) not in by_key:
            return 0.0
    if pure_entry is None:
        return 0.0
    if pure_entry.get("interaction_force_at_500deg_eV_Ang", 1.0) != 0.0:
        return 0.0
    return 1.0


# === block: score_1 (check id='trend1_chirality_stress_up') ===
def score_1(artifact, step, ctx):
    def get(sims, chir, temp):
        for s in sims:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                return s
        return None
    sims = artifact.get("simulations", [])
    s11 = get(sims, "(11,11)", 300)
    s13 = get(sims, "(13,13)", 300)
    s15 = get(sims, "(15,15)", 300)
    if not (s11 and s13 and s15): return 0.0
    if s11["max_shear_stress_GPa"] < s13["max_shear_stress_GPa"] < s15["max_shear_stress_GPa"]:
        return 1.0
    return 0.0


# === block: score_2 (check id='trend2_chirality_angle_down') ===
def score_2(artifact, step, ctx):
    def get(sims, chir, temp):
        for s in sims:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                return s
        return None
    sims = artifact.get("simulations", [])
    s11 = get(sims, "(11,11)", 300)
    s13 = get(sims, "(13,13)", 300)
    s15 = get(sims, "(15,15)", 300)
    if not (s11 and s13 and s15): return 0.0
    if s11["critical_twist_angle_deg"] > s13["critical_twist_angle_deg"] > s15["critical_twist_angle_deg"]:
        return 1.0
    return 0.0


# === block: score_3 (check id='trend3_temp_stress_down') ===
def score_3(artifact, step, ctx):
    def get(sims, chir, temp):
        for s in sims:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                return s
        return None
    sims = artifact.get("simulations", [])
    s300 = get(sims, "(11,11)", 300)
    s500 = get(sims, "(11,11)", 500)
    s700 = get(sims, "(11,11)", 700)
    if not (s300 and s500 and s700): return 0.0
    if s300["max_shear_stress_GPa"] > s500["max_shear_stress_GPa"] > s700["max_shear_stress_GPa"]:
        return 1.0
    return 0.0


# === block: score_4 (check id='trend4_temp_angle_down') ===
def score_4(artifact, step, ctx):
    def get(sims, chir, temp):
        for s in sims:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                return s
        return None
    sims = artifact.get("simulations", [])
    s300 = get(sims, "(11,11)", 300)
    s500 = get(sims, "(11,11)", 500)
    s700 = get(sims, "(11,11)", 700)
    if not (s300 and s500 and s700): return 0.0
    if s300["critical_twist_angle_deg"] > s500["critical_twist_angle_deg"] > s700["critical_twist_angle_deg"]:
        return 1.0
    return 0.0


# === block: score_5 (check id='trend5_temp_interaction_up') ===
def score_5(artifact, step, ctx):
    def get(sims, chir, temp):
        for s in sims:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                return s
        return None
    sims = artifact.get("simulations", [])
    s300 = get(sims, "(11,11)", 300)
    s500 = get(sims, "(11,11)", 500)
    s700 = get(sims, "(11,11)", 700)
    if not (s300 and s500 and s700): return 0.0
    if s300["interaction_force_at_500deg_eV_Ang"] < s500["interaction_force_at_500deg_eV_Ang"] < s700["interaction_force_at_500deg_eV_Ang"]:
        return 1.0
    return 0.0


# === block: score_6 (check id='pure_angle_gt_1000') ===
def score_6(artifact, step, ctx):
    sims = artifact.get("simulations", [])
    for s in sims:
        chir = s.get("chirality", "")
        if re.search(r"pure", chir, re.I) and s.get("temperature") == 300:
            angle = s.get("critical_twist_angle_deg")
            if angle is not None and angle > 1000:
                return 1.0
    return 0.0


# === block: score_7 (check id='ref_max_stress') ===
def score_7(artifact, step, ctx):
    targets = step.get("targets", {})
    tol = step.get("tolerance", 0.10)
    simulations = artifact.get("simulations", [])
    total = 0.0
    count = 0
    for key, target in targets.items():
        chir, temp_str = key.split("|")
        temp = int(temp_str)
        found = None
        for s in simulations:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                found = s
                break
        if found is None:
            score = 0.0
        else:
            v = found.get("max_shear_stress_GPa")
            if v is None:
                score = 0.0
            else:
                err = abs(v - target) / target
                score = max(0.0, 1.0 - err / tol)
        total += score
        count += 1
    if count == 0: return 0.0
    return total / count


# === block: score_8 (check id='ref_critical_angle') ===
def score_8(artifact, step, ctx):
    targets = step.get("targets", {})
    tol = step.get("tolerance", 0.05)
    simulations = artifact.get("simulations", [])
    total = 0.0
    count = 0
    for key, target in targets.items():
        chir, temp_str = key.split("|")
        temp = int(temp_str)
        found = None
        for s in simulations:
            if s.get("chirality") == chir and s.get("temperature") == temp:
                found = s
                break
        if found is None:
            score = 0.0
        else:
            v = found.get("critical_twist_angle_deg")
            if v is None:
                score = 0.0
            else:
                err = abs(v - target) / target
                score = max(0.0, 1.0 - err / tol)
        total += score
        count += 1
    if count == 0: return 0.0
    return total / count


_SCORERS = {
    'shape_completeness': score_0,
    'trend1_chirality_stress_up': score_1,
    'trend2_chirality_angle_down': score_2,
    'trend3_temp_stress_down': score_3,
    'trend4_temp_angle_down': score_4,
    'trend5_temp_interaction_up': score_5,
    'pure_angle_gt_1000': score_6,
    'ref_max_stress': score_7,
    'ref_critical_angle': score_8,
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
