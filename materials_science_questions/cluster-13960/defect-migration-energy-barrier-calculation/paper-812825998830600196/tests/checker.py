import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math


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
    formation_file = os.path.join(outputs_dir, 'formation_energies.csv')
    if os.path.exists(formation_file):
        with open(formation_file, newline='') as f:
            reader = csv.DictReader(f)
            formation_data = []
            for row in reader:
                formation_data.append({
                    'N_He': int(row['N_He']),
                    'E_f_groove_eV': float(row['E_f_groove_eV']),
                    'E_f_vacancy_eV': float(row['E_f_vacancy_eV'])
                })
        formation_data.sort(key=lambda x: x['N_He'])
    else:
        formation_data = None
    ctx = {'formation_data': formation_data}
    return ctx


# === block: score_0 (check id='formation_energies_check') ===
def score_0(artifact, step, ctx):
    # artifact is list of dicts with keys N_He, E_f_groove_eV, E_f_vacancy_eV (as strings)
    gold = step.get('gold_values', {})
    groove_gold = gold.get('groove', {})
    vacancy_gold = gold.get('vacancy', {})
    tol = float(step.get('tolerance_abs_eV', 0.5))
    value_w = float(step.get('value_weight', 0.8))
    mono_w = float(step.get('monotonic_weight', 0.2))
    # build dict from artifact
    agent_data = {}
    for row in artifact:
        n = int(row['N_He'])
        groove = float(row['E_f_groove_eV'])
        vacancy = float(row['E_f_vacancy_eV'])
        agent_data[n] = (groove, vacancy)

    within_tol = 0.0
    total_points = 0
    for n in range(1, 10):
        if n not in agent_data:
            continue
        g_agent, v_agent = agent_data[n]
        total_points += 1
        g_gold = groove_gold.get(str(n), None)
        if g_gold is not None and abs(g_agent - g_gold) <= tol:
            within_tol += 1
        total_points += 1
        v_gold = vacancy_gold.get(str(n), None)
        if v_gold is not None and abs(v_agent - v_gold) <= tol:
            within_tol += 1
    value_score = within_tol / max(total_points, 1) if total_points > 0 else 0.0

    # monotonicity: strictly increasing (allow tiny float roundoff 0.001)
    mono_g = True
    prev = -float('inf')
    for n in sorted(agent_data.keys()):
        g, _ = agent_data[n]
        if g <= prev - 0.001:
            mono_g = False
            break
        prev = g
    mono_v = True
    prev = -float('inf')
    for n in sorted(agent_data.keys()):
        _, v = agent_data[n]
        if v <= prev - 0.001:
            mono_v = False
            break
        prev = v
    mono_score = (1.0 if mono_g else 0.0) + (1.0 if mono_v else 0.0)
    mono_score = mono_score / 2.0
    return value_w * value_score + mono_w * mono_score


# === block: score_1 (check id='binding_energies_check') ===
def score_1(artifact, step, ctx):
    # artifact is list of dicts with keys N_He, E_b_groove_eV, E_b_vacancy_eV
    formation_data = ctx.get('formation_data')
    if formation_data is None:
        return 0.0

    # Build dict from formation data
    f_groove = {d['N_He']: d['E_f_groove_eV'] for d in formation_data}
    f_vacancy = {d['N_He']: d['E_f_vacancy_eV'] for d in formation_data}

    # Ensure we have single-atom formation energies
    if 1 not in f_groove or 1 not in f_vacancy:
        return 0.0

    e1_groove = f_groove[1]
    e1_vacancy = f_vacancy[1]

    # Recompute expected binding energies using E_b(N) = N * E_f(1) - E_f(N)
    def compute_binding(e_dict, e1):
        b = {}
        for n in sorted(e_dict.keys()):
            if n in e_dict:
                b[n] = n * e1 - e_dict[n]
        return b

    groove_binding = compute_binding(f_groove, e1_groove)
    vacancy_binding = compute_binding(f_vacancy, e1_vacancy)

    # Parse agent binding table
    agent_binding = {}
    for row in artifact:
        n = int(row['N_He'])
        g = float(row['E_b_groove_eV'])
        v = float(row['E_b_vacancy_eV'])
        agent_binding[n] = (g, v)

    max_diff = 0.0
    points = 0
    for n in range(2, 10):
        if n not in agent_binding or n not in groove_binding:
            continue
        points += 1
        exp_g = groove_binding[n]
        exp_v = vacancy_binding[n]
        agent_g, agent_v = agent_binding[n]
        max_diff = max(max_diff, abs(agent_g - exp_g), abs(agent_v - exp_v))

    if points == 0:
        return 0.0
    thresh = float(step.get('max_abs_difference_threshold_eV', 0.5))
    score = max(0.0, 1.0 - max_diff / thresh)
    return min(1.0, score)


# === block: score_2 (check id='migration_barriers_check') ===
def score_2(artifact, step, ctx):
    # artifact is list of dicts with keys N_He, barrier_eV
    gold = step.get('gold_values', {})
    tol = float(step.get('tolerance_abs_eV', 0.1))
    value_w = float(step.get('value_weight', 0.8))
    mono_w = float(step.get('monotonic_weight', 0.2))

    agent_data = {}
    for row in artifact:
        n = int(row['N_He'])
        barrier = float(row['barrier_eV'])
        agent_data[n] = barrier

    within_tol = 0
    total_points = 0
    for n, gold_val in gold.items():
        n_int = int(n)
        if n_int in agent_data:
            total_points += 1
            if abs(agent_data[n_int] - gold_val) <= tol:
                within_tol += 1
    value_score = within_tol / max(total_points, 1) if total_points > 0 else 0.0

    # monotonic
    sorted_n = sorted(agent_data.keys())
    mono = True
    prev = -float('inf')
    for n in sorted_n:
        b = agent_data[n]
        if b <= prev - 0.001:
            mono = False
            break
        prev = b
    mono_score = 1.0 if mono else 0.0
    return value_w * value_score + mono_w * mono_score


# === block: score_3 (check id='max_occupancy_check') ===
def score_3(artifact, step, ctx):
    # artifact is dict with keys max_He_in_vacancy, spillover_observed
    expected = step.get('expected', {})
    exp_max = expected.get('max_He_in_vacancy')
    exp_spill = expected.get('spillover_observed')
    actual_max = artifact.get('max_He_in_vacancy')
    actual_spill = artifact.get('spillover_observed')
    if exp_max is None or exp_spill is None:
        return 0.0
    score = 0.0
    if actual_max == exp_max:
        score += 0.5
    if actual_spill == exp_spill:
        score += 0.5
    return score


_SCORERS = {
    'formation_energies_check': score_0,
    'binding_energies_check': score_1,
    'migration_barriers_check': score_2,
    'max_occupancy_check': score_3,
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
