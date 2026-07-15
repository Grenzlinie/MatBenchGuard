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


# === block: score_0 (check id='formation_free_energies_check') ===
def score_0(artifact, step, ctx):
    artifact_rows = artifact
    step_dict = step
    gold_table = step_dict.get('gold_table', [])
    tolerance = step_dict.get('tolerance', 0.0)
    penalty_scale = step_dict.get('penalty_scale', 0.0)
    scores = []
    for gold in gold_table:
        compound = gold['compound']
        temp_key = str(gold['temperature_K'])
        found = None
        for row in artifact_rows:
            if row.get('compound') == compound and str(row.get('temperature_K')) == temp_key:
                found = row
                break
        if found is None:
            scores.append(0.0)
            continue
        try:
            agent_val = float(found['formation_free_energy_eV_per_atom'])
        except (ValueError, KeyError):
            scores.append(0.0)
            continue
        gold_val = gold['formation_free_energy_eV_per_atom']
        diff = agent_val - gold_val
        if diff <= tolerance:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - (diff - tolerance) / penalty_scale))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='elastic_moduli_values_check') ===
def score_1(artifact, step, ctx):
    artifact_rows = artifact
    step_dict = step
    gold_table = step_dict.get('gold_table', [])
    tolerance = step_dict.get('tolerance_GPa', 0.0)
    penalty_scale = step_dict.get('penalty_scale_GPa', 0.0)
    modulus_scores = []
    for gold in gold_table:
        compound = gold['compound']
        row = None
        for r in artifact_rows:
            if r.get('compound') == compound:
                row = r
                break
        if row is None:
            modulus_scores.append(0.0)
            modulus_scores.append(0.0)
            continue
        for key in ['bulk_modulus_GPa', 'shear_modulus_GPa']:
            try:
                agent_val = float(row[key])
            except (ValueError, KeyError):
                modulus_scores.append(0.0)
                continue
            gold_val = gold[key]
            diff = agent_val - gold_val
            if diff >= -tolerance:
                modulus_scores.append(1.0)
            else:
                shortfall = gold_val - tolerance - agent_val
                modulus_scores.append(max(0.0, 1.0 - shortfall / penalty_scale))
    if not modulus_scores:
        return 0.0
    return sum(modulus_scores) / len(modulus_scores)


# === block: score_2 (check id='elastic_moduli_trend_check') ===
def score_2(artifact, step, ctx):
    artifact_rows = artifact
    step_dict = step
    compounds_ordered = step_dict.get('trend_compounds', ['ZrN', 'Zr4N5', 'Zr3N2'])
    B_vals = []
    G_vals = []
    for comp in compounds_ordered:
        row = None
        for r in artifact_rows:
            if r.get('compound') == comp:
                row = r
                break
        if row is None:
            return 0.0
        try:
            B_vals.append(float(row['bulk_modulus_GPa']))
            G_vals.append(float(row['shear_modulus_GPa']))
        except (ValueError, KeyError):
            return 0.0
    def is_monotonic_decreasing(arr):
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
        return True
    b_ok = is_monotonic_decreasing(B_vals)
    g_ok = is_monotonic_decreasing(G_vals)
    score = 0.0
    if b_ok:
        score += 0.5
    if g_ok:
        score += 0.5
    return score


_SCORERS = {
    'formation_free_energies_check': score_0,
    'elastic_moduli_values_check': score_1,
    'elastic_moduli_trend_check': score_2,
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
