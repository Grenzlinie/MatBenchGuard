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
    return {'gold': spec['steps'][0]['hidden_gold']}


# === block: score_0 (check id='step_compute_dipole_ps') ===
def score_0(artifact, step, ctx):
    import re

    def get_gold_index(label, phase):
        if phase == 'paraelectric':
            if re.search(r'BeF4', label, re.I):
                return 2
            if (re.search(r'\bI\b', label) or re.search(r'1', label) or re.search(r'\(I\)', label)) and not (re.search(r'\bII\b', label) or re.search(r'\(II\)', label)):
                return 0
            if re.search(r'\bII\b', label) or re.search(r'2', label) or re.search(r'\(II\)', label):
                return 1
            return -1
        else:
            if re.search(r'BeF4', label, re.I):
                if "'" in label or "′" in label or "prime" in label.lower():
                    return 5
                return 4
            is_I = bool(re.search(r'\bI\b', label) or re.search(r'\(I\)', label))
            is_II = bool(re.search(r'\bII\b', label) or re.search(r'\(II\)', label))
            prime = "'" in label or "′" in label or "prime" in label.lower()
            if is_I and not prime:
                return 0
            if is_I and prime:
                return 1
            if is_II and not prime:
                return 2
            if is_II and prime:
                return 3
            m = re.search(r'(\d+)([\'′]?)', label)
            if m:
                num = m.group(1)
                prime_flag = m.group(2)
                if num == '1':
                    return 0 if not prime_flag else 1
                elif num == '2':
                    return 2 if not prime_flag else 3
                elif num == '3':
                    return 4 if not prime_flag else 5
            return -1

    gold = ctx['gold']
    tol_dipole = 0.001
    tol_Ps = 0.01
    total_fields = 0
    matches = 0
    agent_pe = artifact.get('paraelectric', [])
    gold_pe = gold['paraelectric']
    used_pe = set()
    for i, gold_entry in enumerate(gold_pe):
        matched = None
        for j, agent_entry in enumerate(agent_pe):
            if j in used_pe:
                continue
            if get_gold_index(agent_entry.get('ion_label', ''), 'paraelectric') == i:
                matched = j
                break
        if matched is not None:
            used_pe.add(matched)
            agent_entry = agent_pe[matched]
            for key in ['total_dipole_D', 'pa_D', 'pb_D', 'pc_D']:
                total_fields += 1
                if abs(agent_entry.get(key, 0) - gold_entry[key]) <= tol_dipole:
                    matches += 1

    agent_fe = artifact.get('ferroelectric', [])
    gold_fe = gold['ferroelectric']
    used_fe = set()
    for i, gold_entry in enumerate(gold_fe):
        matched = None
        for j, agent_entry in enumerate(agent_fe):
            if j in used_fe:
                continue
            if get_gold_index(agent_entry.get('ion_label', ''), 'ferroelectric') == i:
                matched = j
                break
        if matched is not None:
            used_fe.add(matched)
            agent_entry = agent_fe[matched]
            for key in ['total_dipole_D', 'pa_D', 'pb_D', 'pc_D']:
                total_fields += 1
                if abs(agent_entry.get(key, 0) - gold_entry[key]) <= tol_dipole:
                    matches += 1

    if 'total_Ps_muC_per_cm2' in artifact and 'total_Ps_muC_per_cm2' in gold:
        total_fields += 1
        if abs(artifact['total_Ps_muC_per_cm2'] - gold['total_Ps_muC_per_cm2']) <= tol_Ps:
            matches += 1

    if total_fields == 0:
        return 0.0
    return matches / total_fields


_SCORERS = {
    'step_compute_dipole_ps': score_0,
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
