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


# === block: score_0 (check id='step03_eos_fit') ===
def score_0(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerances']
    score_parts = []
    for phase in ['beta', 'gamma']:
        phase_data = artifact.get(phase, {})
        # E0 is omitted because absolute per-atom energy is not transferable
        # across DFT implementations; it remains required in the contract but is
        # not scored.
        for field in ['V0', 'K', 'K_prime']:
            val = phase_data.get(field)
            if val is None:
                score_parts.append(0.0)
                continue
            g = gold[phase][field]
            t = tol[field]
            diff = abs(val - g)
            score_parts.append(1.0 if diff <= t else 0.0)
    return sum(score_parts) / len(score_parts)


# === block: score_1 (check id='step04_structural') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    lat_tol = 0.02   # relaxed to absorb cross-code spread
    coord_tol = 0.005
    scores = []
    for phase in ['beta', 'gamma']:
        if phase not in artifact:
            scores += [0.0]*10
            continue
        lat = artifact[phase].get('lattice_constants', {})
        gold_lat = gold[phase]['lattice_constants']
        for key in gold_lat:
            if key in lat:
                diff = abs(lat[key] - gold_lat[key])
                scores.append(1.0 if diff <= lat_tol else 0.0)
            else:
                scores.append(0.0)
        gold_coords = gold[phase]['internal_coordinates']
        agent_coords = artifact[phase].get('internal_coordinates', [])
        agent_map = {}
        for entry in agent_coords:
            key = (entry.get('atom', ''), entry.get('site_label', ''))
            agent_map.setdefault(key, []).append([entry.get('x'), entry.get('y'), entry.get('z')])
        for gentry in gold_coords:
            gkey = (gentry['atom'], gentry['site_label'])
            gcoords = gentry['coords']
            if gkey in agent_map:
                acoords = agent_map[gkey][0]
                match = True
                for i in range(3):
                    if acoords[i] is None or abs(acoords[i] - gcoords[i]) > coord_tol:
                        match = False
                        break
                scores.append(1.0 if match else 0.0)
            else:
                scores.append(0.0)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_2 (check id='step05_band_gap') ===
def score_2(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance']
    score = 0.0
    for phase in ['beta', 'gamma']:
        val = artifact.get(phase, {}).get('LDA_gap')
        if val is None:
            continue
        g = gold[phase]
        diff = abs(val - g)
        if diff <= tol:
            score += 1.0
    return score / 2.0


# === block: score_3 (check id='step06_phonon') ===
def score_3(artifact, step, ctx):
    gold_beta = step['gold_beta']
    gold_gamma = step['gold_gamma']
    tol_freq = step['tolerance_freq']
    def match_phase(agent_modes, gold_modes):
        if not agent_modes:
            return 0.0
        used = [False] * len(agent_modes)
        matched = 0
        for gmode in gold_modes:
            found = False
            for i, amode in enumerate(agent_modes):
                if used[i]:
                    continue
                if amode.get('symmetry_label') != gmode['symmetry_label']:
                    continue
                if amode.get('ir_active') != gmode['ir_active'] or amode.get('raman_active') != gmode['raman_active']:
                    continue
                freq = amode.get('frequency_cm-1')
                if freq is None:
                    continue
                if abs(freq - gmode['frequency_cm-1']) <= tol_freq:
                    matched += 1
                    used[i] = True
                    found = True
                    break
            # no partial credit for unmatched gold
        return matched / len(gold_modes) if gold_modes else 1.0
    score_beta = match_phase(artifact.get('beta', []), gold_beta)
    score_gamma = match_phase(artifact.get('gamma', []), gold_gamma)
    return (score_beta + score_gamma) / 2.0


# === block: score_4 (check id='step07_transition') ===
def score_4(artifact, step, ctx):
    gold = step['gold']
    tol = step['tolerance']
    try:
        val = float(artifact.strip())
    except:
        return 0.0
    diff = abs(val - gold)
    return 1.0 if diff <= tol else 0.0


_SCORERS = {
    'step03_eos_fit': score_0,
    'step04_structural': score_1,
    'step05_band_gap': score_2,
    'step06_phonon': score_3,
    'step07_transition': score_4,
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
