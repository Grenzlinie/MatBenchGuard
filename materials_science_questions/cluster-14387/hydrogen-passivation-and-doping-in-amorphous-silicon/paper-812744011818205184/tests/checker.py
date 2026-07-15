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


# === block: score_0 (check id='step_2_chadi_chang') ===
def score_0(artifact, step, ctx):
    params = step.get('params', {})
    freq_p = params.get('frequency', {})
    charge_p = params.get('charge', {})
    note_p = params.get('note', {})

    # frequency sub-score
    target_f = freq_p.get('target', 432)
    tol_f = freq_p.get('tolerance', 10)
    val = artifact.get(freq_p.get('field', 'e_mode_frequency_cm1'))
    score_f = 1.0 if isinstance(val, (int, float)) and abs(val - target_f) <= tol_f else 0.0

    # charge sub-score
    target_c = charge_p.get('target', 0.63)
    tol_c = charge_p.get('tolerance', 0.1)
    val_c = artifact.get(charge_p.get('field', 'effective_charge_e'))
    score_c = 1.0 if isinstance(val_c, (int, float)) and abs(val_c - target_c) <= tol_c else 0.0

    # note sub-score
    note = artifact.get('note', '')
    score_note = 1.0 if isinstance(note, str) and 'singlet' in note.lower() and ('not distinct' in note.lower() or 'falls within' in note.lower()) else 0.0

    w_f = freq_p.get('weight', 0.5)
    w_c = charge_p.get('weight', 0.35)
    w_n = note_p.get('weight', 0.15)
    total = w_f * score_f + w_c * score_c + w_n * score_note
    return total


# === block: score_1 (check id='step_3_breathing') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    trip_p = params.get('triplets', {})
    mean_p = params.get('mean', {})
    charge_p = params.get('charge', {})
    energy_p = params.get('energy', {})

    # triplets sub-score
    agent_triplets = artifact.get(trip_p.get('field', 'triplet_frequencies_cm1'))
    trip_score = 0.0
    if isinstance(agent_triplets, list) and len(agent_triplets) == 3:
        gold_triplets = sorted(trip_p.get('gold', [352, 347, 342]))
        agent_sorted = sorted(agent_triplets)
        tol_t = trip_p.get('tolerance', 10)
        hits = sum(1 for a, g in zip(agent_sorted, gold_triplets) if abs(a - g) <= tol_t)
        trip_score = hits / 3.0
    else:
        trip_score = 0.0

    # mean sub-score: use agent's own triplet list to compute mean, then score against gold
    agent_mean = artifact.get(mean_p.get('field', 'mean_frequency_cm1'))
    mean_score = 0.0
    if isinstance(agent_triplets, list) and len(agent_triplets) == 3:
        computed_mean = sum(agent_triplets) / 3.0
        # consistency check: agent's reported mean must match computed mean
        if isinstance(agent_mean, (int, float)) and abs(agent_mean - computed_mean) < 1e-4:
            # now score against gold target
            target_m = mean_p.get('target', 347)
            tol_m = mean_p.get('tolerance', 10)
            mean_score = 1.0 if abs(agent_mean - target_m) <= tol_m else 0.0
        else:
            mean_score = 0.0

    # charge sub-score
    target_c = charge_p.get('target', 1.85)
    tol_c = charge_p.get('tolerance', 0.1)
    val_c = artifact.get(charge_p.get('field', 'effective_charge_e'))
    charge_score = 1.0 if isinstance(val_c, (int, float)) and abs(val_c - target_c) <= tol_c else 0.0

    # energy sub-score
    target_e = energy_p.get('target', 0.01)
    tol_e = energy_p.get('tolerance', 0.02)
    val_e = artifact.get(energy_p.get('field', 'energy_difference_eV'))
    energy_score = 1.0 if isinstance(val_e, (int, float)) and abs(val_e - target_e) <= tol_e else 0.0

    w_t = trip_p.get('weight', 0.35)
    w_m = mean_p.get('weight', 0.25)
    w_c = charge_p.get('weight', 0.25)
    w_e = energy_p.get('weight', 0.15)
    total = w_t * trip_score + w_m * mean_score + w_c * charge_score + w_e * energy_score
    return total


# === block: score_2 (check id='step_4_comparison') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    text = artifact if isinstance(artifact, str) else ""
    text_lower = text.lower()

    # required phrases
    required = params.get('required_phrases', ['Chadi-Chang', 'breathing', '376 cm⁻¹'])
    phrase_hits = sum(1 for p in required if p.lower() in text_lower)
    phrase_score = phrase_hits / len(required) if required else 1.0

    # correct assignment: breathing consistent, Chadi-Chang not
    correct = 0.0
    if ('breathing' in text_lower) and ('consistent' in text_lower or 'agreement' in text_lower):
        correct += 0.5
    if ('chadi' in text_lower or 'chadi-chang' in text_lower) and ('not' in text_lower or 'inconsistent' in text_lower or 'does not' in text_lower):
        correct += 0.5

    # combine: 0.4 phrase, 0.6 assignment
    return 0.4 * phrase_score + 0.6 * correct


_SCORERS = {
    'step_2_chadi_chang': score_0,
    'step_3_breathing': score_1,
    'step_4_comparison': score_2,
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
