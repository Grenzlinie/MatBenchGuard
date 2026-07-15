import os
import json
import csv

# === author imports / helpers ===
import csv
import math


def spearman_correlation(actual_vals, gold_order, value_getter):
    """Compute Spearman rank correlation between actual sorted order and gold rank."""
    # Gold order: list of labels, first is most negative (rank 1)
    gold_ranks = {label: i + 1 for i, label in enumerate(gold_order)}
    # Assign ranks to actual species based on value (lowest value gets rank 1)
    sorted_actual = sorted(actual_vals, key=value_getter)
    actual_ranks = [gold_ranks[value_getter(row)] for row in sorted_actual if value_getter(row) in gold_ranks]
    gold_ranks_list = list(range(1, len(gold_order) + 1))
    if len(actual_ranks) != len(gold_ranks_list):
        return -1.0
    n = len(actual_ranks)
    d2 = sum((a - g) ** 2 for a, g in zip(actual_ranks, gold_ranks_list))
    rho = 1.0 - (6.0 * d2) / (n * (n * n - 1))
    return max(rho, -1.0)


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


# === block: score_0 (check id='adsorption_ranking') ===
def score_0(artifact, step, ctx):
    rows = artifact  # artifact is list of dicts from CSV
    config = step.get('config', {})
    gold_ranking = config.get('gold_ranking', {})
    pristine_ranking = gold_ranking.get('pristine', [])
    vacancy_ranking = gold_ranking.get('vacancy', [])

    # Extract rows per surface
    pristine_rows = [r for r in rows if r.get('surface_type', '').strip().lower() == 'pristine']
    vacancy_rows = [r for r in rows if r.get('surface_type', '').strip().lower() == 'vacancy']

    # Get value as float
    def get_energy(r):
        return float(r.get('adsorption_energy', 0))

    rho_pristine = spearman_correlation(pristine_rows, pristine_ranking, get_energy) if pristine_rows else -1.0
    rho_vacancy = spearman_correlation(vacancy_rows, vacancy_ranking, get_energy) if vacancy_rows else -1.0

    # Scores: if any surface missing, score 0; else average Spearman (clamp to 0 if negative)
    def clamp_rho(r):
        return max(r, 0.0)

    if rho_pristine < -0.5 or rho_vacancy < -0.5:  # severely wrong
        return 0.0
    score = (clamp_rho(rho_pristine) + clamp_rho(rho_vacancy)) / 2.0
    return round(score, 4)


# === block: score_1 (check id='fermi_shifts') ===
def score_1(artifact, step, ctx):
    rows = artifact
    config = step.get('config', {})
    abs_max = config.get('o_vac_abs_max', 0.05)
    oh_min = config.get('oh_min', 0.1)

    # Initialize passed flags
    passed_o_vac = False
    passed_oh_pristine = False
    passed_oh_vacancy = False

    for r in rows:
        species = r.get('species', '').strip()
        surface = r.get('surface_type', '').strip().lower()
        shift = float(r.get('fermi_level_shift', 0))

        if species == 'O' and surface == 'vacancy':
            if abs(shift) <= abs_max:
                passed_o_vac = True
            else:
                return 0.0  # critical: O/V must be near zero
        if species == 'OH':
            if shift < oh_min:
                continue
            if surface == 'pristine':
                passed_oh_pristine = True
            elif surface == 'vacancy':
                passed_oh_vacancy = True

    score = 0.0
    if passed_o_vac:
        score += 0.4
    if passed_oh_pristine:
        score += 0.3
    if passed_oh_vacancy:
        score += 0.3
    return score


# === block: score_2 (check id='reaction_trends') ===
def score_2(artifact, step, ctx):
    rows = artifact
    config = step.get('config', {})
    overall_range = config.get('overall_range', [0.4, 0.8])

    # Build dict from reaction string to delta_E
    reaction_dict = {}
    for r in rows:
        react = r.get('reaction', '').strip()
        val = float(r.get('delta_E', 0))
        reaction_dict[react] = val

    # Required reactions
    step1 = 'H2O/V -> OH/V + H/S'
    step2 = 'OH/V -> O/V + H/S'
    overall = 'H2O/V -> O/V + H2'

    if step1 not in reaction_dict or step2 not in reaction_dict or overall not in reaction_dict:
        return 0.0

    delta1 = reaction_dict[step1]
    delta2 = reaction_dict[step2]
    delta_total = reaction_dict[overall]

    checks = 0
    passed = 0

    # All positive
    all_pos = delta1 > 0 and delta2 > 0 and delta_total > 0
    if all_pos:
        passed += 1
    checks += 1

    # Step1 < step2
    if delta1 < delta2:
        passed += 1
    checks += 1

    # Overall in range
    if overall_range[0] <= delta_total <= overall_range[1]:
        passed += 1
    checks += 1

    return passed / checks if checks else 0.0


_SCORERS = {
    'adsorption_ranking': score_0,
    'fermi_shifts': score_1,
    'reaction_trends': score_2,
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
