import os
import json
import csv

# === author imports / helpers ===
import json, math


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


# === block: score_0 (check id='optimized_structures') ===
def score_0(artifact, step, ctx):
    def _close(v, gold, tol):
        return 1.0 if abs(v - gold) <= tol else 0.0

    gold = step['gold']
    tol = step['tolerance']
    beta = artifact.get('beta', {})
    gamma = artifact.get('gamma', {})
    total = 0
    score = 0.0
    # beta lattice
    for key in ['a','c']:
        total += 1
        score += _close(beta.get(key,0), gold['beta'][key], tol['lattice'])
    # beta internal coordinates
    for site in ['Ge_6h','N_6h','N_2c']:
        agent_coords = beta.get(site, [0,0,0])
        gold_coords = gold['beta'][site]
        for i in range(3):
            total += 1
            score += _close(agent_coords[i], gold_coords[i], tol['coord'])
    # gamma lattice
    total += 1
    score += _close(gamma.get('a',0), gold['gamma']['a'], tol['lattice'])
    # gamma coordinates
    for site in ['GeIV_8a','GeVI_16d','N_32e']:
        agent_coords = gamma.get(site, [0,0,0])
        gold_coords = gold['gamma'][site]
        for i in range(3):
            total += 1
            score += _close(agent_coords[i], gold_coords[i], tol['coord'])
    return score / total if total > 0 else 0.0


# === block: score_1 (check id='eos_parameters') ===
def score_1(artifact, step, ctx):
    def _close(v, gold, tol):
        return 1.0 if abs(v - gold) <= tol else 0.0

    gold = step['gold']
    tol = step['tolerance']
    beta = artifact.get('beta', {})
    gamma = artifact.get('gamma', {})
    total = 0
    score = 0.0
    for phase_name in ['beta','gamma']:
        phase = beta if phase_name == 'beta' else gamma
        for param in ['V0','K','Kprime']:
            total += 1
            score += _close(phase.get(param,0), gold[phase_name][param], tol[param])
    return score / total if total > 0 else 0.0


# === block: score_2 (check id='band_gaps') ===
def score_2(artifact, step, ctx):
    def _close(v, gold, tol):
        return 1.0 if abs(v - gold) <= tol else 0.0

    gold = step['gold']
    tol = step['tolerance']['gap']
    beta = artifact.get('beta', {}).get('LDA_band_gap_eV', None)
    gamma = artifact.get('gamma', {}).get('LDA_band_gap_eV', None)
    score = 0.0
    total = 0
    if beta is not None:
        total += 1
        score += _close(beta, gold['beta'], tol)
    if gamma is not None:
        total += 1
        score += _close(gamma, gold['gamma'], tol)
    return score / total if total > 0 else 0.0


# === block: score_3 (check id='phonon_frequencies') ===
def score_3(artifact, step, ctx):
    def _match_phonons(agent_list, gold_list, tol):
        if not isinstance(agent_list, list):
            return 0
        gold_remain = list(gold_list)
        matched = 0
        for agent in agent_list:
            freq = agent.get('frequency_cm-1', None)
            sym = agent.get('symmetry', '')
            if freq is None:
                continue
            best = None
            for g in gold_remain:
                if sym != g['symmetry']:
                    continue
                if abs(freq - g['frequency_cm-1']) <= tol:
                    best = g
                    break
            if best is not None:
                gold_remain.remove(best)
                matched += 1
        return matched

    tol = step['tolerance']['frequency']
    beta_agent = artifact.get('beta', [])
    gamma_agent = artifact.get('gamma', [])
    beta_gold = step['gold']['beta']
    gamma_gold = step['gold']['gamma']
    matched = _match_phonons(beta_agent, beta_gold, tol) + _match_phonons(gamma_agent, gamma_gold, tol)
    total = len(beta_gold) + len(gamma_gold)
    return matched / total if total > 0 else 0.0


_SCORERS = {
    'optimized_structures': score_0,
    'eos_parameters': score_1,
    'band_gaps': score_2,
    'phonon_frequencies': score_3,
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
