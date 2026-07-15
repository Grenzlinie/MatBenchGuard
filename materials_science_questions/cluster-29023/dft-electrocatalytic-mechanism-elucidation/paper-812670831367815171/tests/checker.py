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


# === block: score_0 (check id='fe_abs') ===
def score_0(artifact, step, ctx):
    import json
    def score(artifact, step, ctx):
        data = artifact.get('formation_energies', {})
        gold = step['config']['gold']
        tol = step['config']['tolerance_ev']
        correct = 0
        for key, g in gold.items():
            if key in data:
                if abs(data[key] - g) <= tol:
                    correct += 1
        total = len(gold)
        return correct / total if total > 0 else 0.0


# === block: score_1 (check id='fe_trend') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact.get('formation_energies', {})
        trends = step['config']['trends']
        passed = 0
        for t in trends:
            parts = t.split()
            left = parts[0]
            op = parts[1]
            right = parts[2]
            if left in data and right in data:
                left_val = data[left]
                right_val = data[right]
                if op == '<' and left_val < right_val:
                    passed += 1
                elif op == '<=' and left_val <= right_val:
                    passed += 1
        return passed / len(trends) if trends else 1.0


# === block: score_2 (check id='ads_abs') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact.get('adsorption_energies', {})
        gold = step['config']['gold']
        tol = step['config']['tolerance_ev']
        correct = 0
        for key, g in gold.items():
            if key in data:
                if abs(data[key] - g) <= tol:
                    correct += 1
        total = len(gold)
        return correct / total if total > 0 else 0.0


# === block: score_3 (check id='ads_trend') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        data = artifact.get('adsorption_energies', {})
        series_def = step['config']['series']
        total_pairs = 0
        correct_pairs = 0
        for defect, cls in series_def.items():
            vals = []
            for cl in cls:
                key = f'PtCl_{defect}_{cl}'
                if key in data:
                    vals.append(data[key])
            for i in range(len(vals)-1):
                total_pairs += 1
                if vals[i] <= vals[i+1] + 1e-9:
                    correct_pairs += 1
        return correct_pairs / total_pairs if total_pairs > 0 else 0.0


# === block: score_4 (check id='reaction_abs') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        profiles = artifact.get('reaction_profile', {})
        prof_config = step['config']['profiles']
        all_correct = 0
        all_total = 0
        for name, cfg in prof_config.items():
            agent_prof = profiles.get(name)
            if not isinstance(agent_prof, list):
                continue
            gold_list = cfg['gold']
            tol = cfg['tolerance_ev']
            agent_map = {item['label']: item['energy'] for item in agent_prof if 'label' in item and 'energy' in item}
            for g_item in gold_list:
                label = g_item['label']
                gold_energy = g_item['energy']
                if label in agent_map:
                    all_total += 1
                    if abs(agent_map[label] - gold_energy) <= tol:
                        all_correct += 1
        return all_correct / all_total if all_total > 0 else 0.0


# === block: score_5 (check id='reaction_shape') ===
def score_5(artifact, step, ctx):
    def score(artifact, step, ctx):
        profiles = artifact.get('reaction_profile', {})
        prof_names = step['config'].get('profiles', [])
        conditions = step['config'].get('conditions', {})
        total_conditions = 0
        passed_conditions = 0
        for name in prof_names:
            prof = profiles.get(name, [])
            if not prof:
                continue
            labels = [p.get('label','') for p in prof]
            energies = [p.get('energy', None) for p in prof]
            if conditions.get('C2H2-ads_negative', False):
                total_conditions += 1
                if 'C2H2-ads' in labels:
                    idx = labels.index('C2H2-ads')
                    if energies[idx] is not None and energies[idx] < 0:
                        passed_conditions += 1
            if conditions.get('TS1_higher_than_prev', False):
                total_conditions += 1
                if 'C2H2-ads' in labels and 'TS1' in labels:
                    idx_c2 = labels.index('C2H2-ads')
                    idx_ts1 = labels.index('TS1')
                    if energies[idx_c2] is not None and energies[idx_ts1] is not None:
                        if energies[idx_ts1] > energies[idx_c2]:
                            passed_conditions += 1
            if conditions.get('VCM_gas_negative', False):
                total_conditions += 1
                if 'VCM-gas' in labels:
                    idx = labels.index('VCM-gas')
                    if energies[idx] is not None and energies[idx] < 0:
                        passed_conditions += 1
        return passed_conditions / total_conditions if total_conditions > 0 else 0.0


_SCORERS = {
    'fe_abs': score_0,
    'fe_trend': score_1,
    'ads_abs': score_2,
    'ads_trend': score_3,
    'reaction_abs': score_4,
    'reaction_shape': score_5,
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
