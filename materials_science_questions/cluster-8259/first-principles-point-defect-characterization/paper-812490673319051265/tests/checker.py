import os
import json
import csv

# === author imports / helpers ===
import json, os, math


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
    outputs_dir = "/app/outputs"
    def load(filename):
        path = os.path.join(outputs_dir, filename)
        if not os.path.exists(path):
            return None
        with open(path) as f:
            return json.load(f)
    ctx = {
        "step_01": load("step_01_total_energies.json"),
        "step_02": load("step_02_formation_energies.json"),
        "step_03": load("step_03_transition_levels.json"),
        "step_04": load("step_04_defect_hull.json"),
    }
    return ctx


# === block: score_0 (check id='dft_total_energies') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0
    has_bulk = False
    for item in artifact:
        if not isinstance(item, dict):
            return 0.0
        for key in ("defect", "charge", "total_energy_eV", "supercell_size"):
            if key not in item:
                return 0.0
        if item["defect"] == "bulk" and item["charge"] == 0:
            has_bulk = True
            if item["total_energy_eV"] > 0:
                return 0.0
        if not isinstance(item["supercell_size"], int) or item["supercell_size"] <= 0:
            return 0.0
    if not has_bulk:
        return 0.0
    return 1.0


# === block: score_1 (check id='defect_formation_energies') ===
def score_1(artifact, step, ctx):
    step_02 = artifact
    step_04 = ctx.get("step_04")
    if not step_02 or not isinstance(step_02, list):
        return 0.0
    total = max(len(step_02), 1)
    consistent = 0
    eF_Pb = None
    eF_Br = None
    if step_04 and isinstance(step_04, dict):
        eF_Pb = step_04.get("Pb_rich", {}).get("crossing_fermi_level_eV")
        eF_Br = step_04.get("Br_rich", {}).get("crossing_fermi_level_eV")
    for entry in step_02:
        charge = entry.get("charge")
        ef_vbm = entry.get("Ef_at_VBM_eV")
        if ef_vbm is None or charge is None:
            continue
        ok = True
        ef_pb = entry.get("Ef_at_neutral_Pbrich_eV")
        if eF_Pb is not None and ef_pb is not None:
            if abs(ef_vbm + charge * eF_Pb - ef_pb) > 0.01:
                ok = False
        ef_br = entry.get("Ef_at_neutral_Brrich_eV")
        if eF_Br is not None and ef_br is not None:
            if abs(ef_vbm + charge * eF_Br - ef_br) > 0.01:
                ok = False
        if ok:
            consistent += 1
    return consistent / total


# === block: score_2 (check id='transition_levels') ===
def score_2(artifact, step, ctx):
    gold_list = step.get("gold", [])
    if not isinstance(artifact, list):
        return 0.0
    agent_levels = artifact
    matched = 0
    for gold in gold_list:
        def_match = gold["defect"]
        trans = gold["charge_transition"]
        target = gold["energy_eV"]
        tol = gold.get("tolerance", 0.05)
        found = False
        for al in agent_levels:
            if al.get("defect") == def_match and al.get("charge_transition") == trans:
                if abs(al.get("energy_eV", 0) - target) <= tol:
                    found = True
                    break
        if found:
            matched += 1
    if len(gold_list) == 0:
        return 1.0
    return matched / len(gold_list)


# === block: score_3 (check id='defect_hull') ===
def score_3(artifact, step, ctx):
    gold = step.get("gold", {})
    if not isinstance(artifact, dict):
        return 0.0
    agent_hull = artifact
    conditions = ["Pb_rich", "Br_rich"]
    scores = []
    for cond in conditions:
        gold_cond = gold.get(cond, {})
        agent_cond = agent_hull.get(cond, {})
        if not gold_cond or not agent_cond:
            scores.append(0.0)
            continue
        gold_set = set(gold_cond.get("hull_defects", []))
        agent_set = set(agent_cond.get("hull_defects", []))
        if len(gold_set) == 0:
            hull_score = 1.0
        else:
            intersection = gold_set & agent_set
            hull_score = len(intersection) / len(gold_set)
        gold_fermi = gold_cond.get("crossing_fermi_level_eV")
        agent_fermi = agent_cond.get("crossing_fermi_level_eV")
        fermi_tol = gold_cond.get("fermi_tolerance_eV", 0.1)
        if gold_fermi is not None and agent_fermi is not None and abs(agent_fermi - gold_fermi) <= fermi_tol:
            fermi_score = 1.0
        else:
            fermi_score = 0.0
        cond_score = 0.7 * hull_score + 0.3 * fermi_score
        scores.append(cond_score)
    return sum(scores) / max(len(conditions), 1)


_SCORERS = {
    'dft_total_energies': score_0,
    'defect_formation_energies': score_1,
    'transition_levels': score_2,
    'defect_hull': score_3,
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
