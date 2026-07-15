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


# === block: score_0 (check id='substitution_energies') ===
def score_0(artifact, step, ctx):
    required_sites = {'Mn(1)', 'Mn(2)'}
    sub_list = artifact.get('substitution_energies')
    if not isinstance(sub_list, list):
        return 0.0
    site_map = {}
    for item in sub_list:
        if not isinstance(item, dict):
            continue
        site = item.get('site')
        energy = item.get('energy_kJ_mol')
        if site in required_sites and isinstance(energy, (int, float)):
            site_map[site] = energy
    if set(site_map.keys()) != required_sites:
        return 0.0
    targets = step['target']
    tolerance = step.get('tolerance', 15.0)
    scores = []
    for site in required_sites:
        val = site_map[site]
        target = targets[site]
        if val <= target:
            scores.append(1.0)
        else:
            diff = val - target
            if diff >= tolerance:
                scores.append(0.0)
            else:
                scores.append(max(0.0, 1.0 - diff / tolerance))
    return sum(scores) / len(required_sites)


# === block: score_1 (check id='fukui_functions') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        fukui_list = artifact.get('fukui_functions')
        if not isinstance(fukui_list, list):
            return 0.0
        target_items = step.get('targets', [])
        tolerance = step.get('tolerance', 0.010)
        # Build lookup from agent data
        agent_map = {}
        for item in fukui_list:
            if not isinstance(item, dict):
                continue
            material = item.get('material')
            atom = item.get('atom')
            f_minus = item.get('f_minus')
            if material is not None and atom is not None and isinstance(f_minus, (int, float)):
                agent_map[(material, atom)] = f_minus
        if not agent_map:
            return 0.0
        scores = []
        for t in target_items:
            key = (t['material'], t['atom'])
            if key not in agent_map:
                scores.append(0.0)
            else:
                val = agent_map[key]
                target = t['f_minus']
                diff = abs(val - target)
                if diff <= tolerance:
                    scores.append(1.0)
                else:
                    # Linear decay beyond tolerance, zero when diff >= 2*tolerance
                    excess = diff - tolerance
                    scores.append(max(0.0, 1.0 - excess / tolerance))
        return sum(scores) / len(target_items) if target_items else 1.0


# === block: score_2 (check id='co_adsorption_energies') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        ads_list = artifact.get('co_adsorption')
        if not isinstance(ads_list, list):
            return 0.0
        target_items = step.get('targets', [])
        tolerance = step.get('tolerance', 15.0)
        agent_map = {}
        for item in ads_list:
            if not isinstance(item, dict):
                continue
            site = item.get('site')
            energy = item.get('adsorption_energy_kJ_mol')
            if site is not None and isinstance(energy, (int, float)):
                agent_map[site] = energy
        if not agent_map:
            return 0.0
        scores = []
        for t in target_items:
            site = t['site']
            if site not in agent_map:
                scores.append(0.0)
            else:
                val = agent_map[site]
                target = t['adsorption_energy_kJ_mol']
                if val <= target:  # more negative is better
                    scores.append(1.0)
                else:
                    diff = val - target
                    if diff >= tolerance:
                        scores.append(0.0)
                    else:
                        scores.append(max(0.0, 1.0 - diff / tolerance))
        return sum(scores) / len(target_items) if target_items else 1.0


# === block: score_3 (check id='co_bond_lengths') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        ads_list = artifact.get('co_adsorption')
        if not isinstance(ads_list, list):
            return 0.0
        target_items = step.get('targets', [])
        tolerance = step.get('tolerance', 0.05)
        agent_map = {}
        for item in ads_list:
            if not isinstance(item, dict):
                continue
            site = item.get('site')
            length = item.get('bond_length_angstrom')
            if site is not None and isinstance(length, (int, float)):
                agent_map[site] = length
        if not agent_map:
            return 0.0
        scores = []
        for t in target_items:
            site = t['site']
            if site not in agent_map:
                scores.append(0.0)
            else:
                val = agent_map[site]
                target = t['bond_length_angstrom']
                diff = abs(val - target)
                if diff <= tolerance:
                    scores.append(1.0)
                else:
                    excess = diff - tolerance
                    scores.append(max(0.0, 1.0 - excess / tolerance))
        return sum(scores) / len(target_items) if target_items else 1.0


# === block: score_4 (check id='trend_checks') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        fukui = artifact.get('fukui_functions', [])
        ads = artifact.get('co_adsorption', [])
        # Extract needed values with defaults
        f_vals = {}
        for item in fukui:
            mat = item.get('material', '')
            atom = item.get('atom', '')
            val = item.get('f_minus')
            if mat == 'Nb(2)-K-OMS-2':
                if atom == 'Nb':
                    f_vals['f_Nb'] = val
                elif atom == 'Mn(1)':
                    f_vals['f_Mn1'] = val
                elif atom == 'K':
                    f_vals['f_K'] = val
        ads_map = {}
        for item in ads:
            site = item.get('site')
            energy = item.get('adsorption_energy_kJ_mol')
            if site and isinstance(energy, (int, float)):
                ads_map[site] = energy
        passed = 0
        total = 4
        if f_vals.get('f_Nb') is not None and f_vals.get('f_Mn1') is not None:
            if f_vals['f_Nb'] > f_vals['f_Mn1']:
                passed += 1
        if f_vals.get('f_Nb') is not None and f_vals.get('f_K') is not None:
            if f_vals['f_Nb'] > f_vals['f_K']:
                passed += 1
        if ads_map.get('Nb(2)') is not None and ads_map.get('Mn(1)') is not None:
            if ads_map['Nb(2)'] < ads_map['Mn(1)']:  # more negative is smaller numerically
                passed += 1
        if ads_map.get('Nb(1)') is not None and ads_map.get('Mn(2)') is not None:
            if ads_map['Nb(1)'] < ads_map['Mn(2)']:
                passed += 1
        return passed / total


_SCORERS = {
    'substitution_energies': score_0,
    'fukui_functions': score_1,
    'co_adsorption_energies': score_2,
    'co_bond_lengths': score_3,
    'trend_checks': score_4,
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
