import os
import json
import csv

# === author imports / helpers ===
import os, json, math

def match_levels(gold_list, agent_list, tol_lambda, tol_psi_sq=None):
    agent_available = list(agent_list)
    matches = 0
    for g in gold_list:
        glambda = g['lambda']
        gm = g['m']
        gpsi = g.get('psi_sq', None)
        found = None
        for i, a in enumerate(agent_available):
            if a.get('m') != gm:
                continue
            if abs(a['lambda'] - glambda) > tol_lambda:
                continue
            if gpsi is not None:
                apsi = a.get('psi_sq')
                if apsi is None or (tol_psi_sq is not None and abs(apsi - gpsi) > tol_psi_sq):
                    continue
            found = i
            break
        if found is not None:
            matches += 1
            agent_available.pop(found)
    extra = len(agent_available)
    return matches, extra

def fill_and_sum(levels, total_electrons):
    sorted_levels = sorted(levels, key=lambda x: x['lambda'])
    total = 0.0
    remaining = total_electrons
    for lv in sorted_levels:
        if remaining <= 0:
            break
        capacity = 2 * lv['m']
        fill = min(remaining, capacity)
        total += fill * lv['lambda']
        remaining -= fill
    return total


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
    output_dir = outputs_dir
    spec = spec
    ctx = {}
    gold = spec.get('gold_levels', {})
    gold_energies = spec.get('gold_total_energies', {})
    gold_ordering = spec.get('gold_ordering', {})
    ctx['gold_levels'] = gold
    ctx['gold_energies'] = gold_energies
    ctx['gold_ordering'] = gold_ordering
    def safe_load(filename):
        path = os.path.join(outputs_dir, filename)
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        return None
    ctx['agent_data'] = {
        'separation_s': safe_load('separation_limit_s_levels.json'),
        'separation_p': safe_load('separation_limit_p_levels.json'),
        'hybridization': safe_load('hybridization_limit_levels.json'),
    }
    return ctx


# === block: score_0 (check id='separation_s_levels') ===
def score_0(artifact, step, ctx):
    tol_lambda = step.get('tolerance_lambda', 1e-4)
    tol_psi_sq = step.get('tolerance_psi_sq', 1e-4)
    gold = ctx['gold_levels'].get('separation_s', {})
    agent_data = ctx['agent_data'].get('separation_s', {})
    if agent_data is None:
        return 0.0
    scenarios = ['fcc', 'hcp', 'icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']
    scores = []
    for sc in scenarios:
        gold_list = gold.get(sc, [])
        agent_list = agent_data.get(sc, [])
        if not isinstance(agent_list, list):
            agent_list = []
        matches, extra = match_levels(gold_list, agent_list, tol_lambda, tol_psi_sq)
        total_gold = len(gold_list)
        if total_gold == 0:
            sc_score = 1.0 if extra == 0 else 0.0
        else:
            correct_ratio = matches / total_gold
            penalty = extra / (len(agent_list) if len(agent_list) > 0 else 1)
            sc_score = max(0.0, correct_ratio - 0.1 * penalty)
        scores.append(sc_score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='separation_p_levels') ===
def score_1(artifact, step, ctx):
    tol_lambda = step.get('tolerance_lambda', 1e-4)
    tol_psi_sq = step.get('tolerance_psi_sq', 1e-4)
    gold = ctx['gold_levels'].get('separation_p', {})
    agent_data = ctx['agent_data'].get('separation_p', {})
    if agent_data is None:
        return 0.0
    scenarios = ['fcc', 'hcp', 'icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']
    scores = []
    for sc in scenarios:
        gold_list = gold.get(sc, [])
        agent_list = agent_data.get(sc, [])
        if not isinstance(agent_list, list):
            agent_list = []
        matches, extra = match_levels(gold_list, agent_list, tol_lambda, tol_psi_sq)
        total_gold = len(gold_list)
        if total_gold == 0:
            sc_score = 1.0 if extra == 0 else 0.0
        else:
            correct_ratio = matches / total_gold
            penalty = extra / (len(agent_list) if len(agent_list) > 0 else 1)
            sc_score = max(0.0, correct_ratio - 0.1 * penalty)
        scores.append(sc_score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='hybridization_levels') ===
def score_2(artifact, step, ctx):
    tol_lambda = step.get('tolerance_lambda', 1e-4)
    tol_psi_sq = step.get('tolerance_psi_sq', 1e-4)
    gold = ctx['gold_levels'].get('hybridization', {})
    agent_data = ctx['agent_data'].get('hybridization', {})
    if agent_data is None:
        return 0.0
    scenarios = ['fcc', 'hcp', 'icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']
    scores = []
    for sc in scenarios:
        gold_list = gold.get(sc, [])
        agent_list = agent_data.get(sc, [])
        if not isinstance(agent_list, list):
            agent_list = []
        matches, extra = match_levels(gold_list, agent_list, tol_lambda, tol_psi_sq)
        total_gold = len(gold_list)
        if total_gold == 0:
            sc_score = 1.0 if extra == 0 else 0.0
        else:
            correct_ratio = matches / total_gold
            penalty = extra / (len(agent_list) if len(agent_list) > 0 else 1)
            sc_score = max(0.0, correct_ratio - 0.1 * penalty)
        scores.append(sc_score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='total_energies') ===
def score_3(artifact, step, ctx):
    tol_energy = step.get('tolerance_energy', 0.01)
    gold_energies = ctx['gold_energies']
    gold_ordering = ctx['gold_ordering']
    agent_total = artifact
    if agent_total is None:
        return 0.0

    short_name = {'fcc': 'fcc', 'hcp': 'hcp', 'icosahedron_VequalV': 'ico', 'icosahedron_Vsqrt_0_8V': 'ico'}
    energy_scores = []
    ordering_scores = []

    # separation limit
    sep_gold = gold_energies.get('separation_limit', {})
    sep_agent = agent_total.get('separation_limit', {})
    for ne_str in ['s1', 'p1', '2', '3', '4', '5']:
        for vkey in ['icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']:
            gold_val = sep_gold.get(ne_str, {}).get(vkey)
            agent_val = sep_agent.get(ne_str, {}).get(vkey)
            if gold_val is not None and agent_val is not None and abs(agent_val - gold_val) <= tol_energy:
                energy_scores.append(1.0)
            else:
                energy_scores.append(0.0)
            # ordering among clusters
            totals = {}
            for cl in ['fcc', 'hcp', 'icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']:
                totals[cl] = sep_agent.get(ne_str, {}).get(cl, float('inf'))
            min_e = min(totals.values())
            best_cluster = None
            for cl in totals:
                if abs(totals[cl] - min_e) < 1e-12:
                    best_cluster = cl
                    break
            variant_short = 'VeqV' if vkey == 'icosahedron_VequalV' else 'Vsqrt'
            expected = gold_ordering.get('separation_limit', {}).get(ne_str, {}).get(variant_short)
            ordering_scores.append(1.0 if best_cluster and short_name.get(best_cluster) == expected else 0.0)

    # hybridization limit
    hyb_gold = gold_energies.get('hybridization_limit', {})
    hyb_agent = agent_total.get('hybridization_limit', {})
    for ne_str in ['1', '2', '3', '4', '5', '6', '7']:
        for vkey in ['icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']:
            gold_val = hyb_gold.get(ne_str, {}).get(vkey)
            agent_val = hyb_agent.get(ne_str, {}).get(vkey)
            if gold_val is not None and agent_val is not None and abs(agent_val - gold_val) <= tol_energy:
                energy_scores.append(1.0)
            else:
                energy_scores.append(0.0)
            totals = {}
            for cl in ['fcc', 'hcp', 'icosahedron_VequalV', 'icosahedron_Vsqrt_0_8V']:
                totals[cl] = hyb_agent.get(ne_str, {}).get(cl, float('inf'))
            min_e = min(totals.values())
            best_cluster = None
            for cl in totals:
                if abs(totals[cl] - min_e) < 1e-12:
                    best_cluster = cl
                    break
            variant_short = 'VeqV' if vkey == 'icosahedron_VequalV' else 'Vsqrt'
            expected = gold_ordering.get('hybridization_limit', {}).get(ne_str, {}).get(variant_short)
            ordering_scores.append(1.0 if best_cluster and short_name.get(best_cluster) == expected else 0.0)

    avg_energy = sum(energy_scores) / len(energy_scores) if energy_scores else 0.0
    avg_ordering = sum(ordering_scores) / len(ordering_scores) if ordering_scores else 0.0
    return 0.8 * avg_energy + 0.2 * avg_ordering


_SCORERS = {
    'separation_s_levels': score_0,
    'separation_p_levels': score_1,
    'hybridization_levels': score_2,
    'total_energies': score_3,
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
