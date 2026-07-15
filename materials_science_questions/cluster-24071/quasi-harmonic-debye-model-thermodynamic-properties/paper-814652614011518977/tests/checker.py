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
    return {
        'spec': spec,
        'gold_freqs': spec['steps'][0]['gold_frequencies'],
        'tol_abs': spec['steps'][0]['frequency_tolerance_abs'],
        'tol_rel': spec['steps'][0]['frequency_tolerance_rel'],
        'order_check': spec['steps'][0]['ordering_check'],
        'thermo_props': spec['steps'][1]['properties']
    }


# === block: score_0 (check id='step_01_phonon_frequencies') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, list) or len(artifact) != 15:
        return 0.0
    tol_abs = ctx['tol_abs']
    tol_rel = ctx['tol_rel']
    ordering = ctx['order_check']

    # Only the six Raman frequencies reported in the paper (Table 2).
    gold_modes = [
        ('B1', 136.4),
        ('A1', 138.2),
        ('B2', 191.4),
        ('A2', 193.0),
        ('A1', 235.5),
        ('B1', 252.2),
    ]

    agent_modes = []
    for m in artifact:
        sym = m.get('symmetry', '').upper()
        freq = m.get('frequency_cm-1')
        if sym in ('A1','A2','B1','B2') and isinstance(freq, (int, float)):
            agent_modes.append({'sym': sym, 'freq': freq})
    if len(agent_modes) != 15:
        return 0.0

    used_agent = [False] * len(agent_modes)
    matched = 0
    match_ordering = {'B2': None, 'A2': None}

    for sym, gfreq in gold_modes:
        window = max(tol_abs, tol_rel * gfreq)
        best_idx = -1
        best_dist = float('inf')
        for i, am in enumerate(agent_modes):
            if used_agent[i] or am['sym'] != sym:
                continue
            dist = abs(am['freq'] - gfreq)
            if dist <= window and dist < best_dist:
                best_dist = dist
                best_idx = i
        if best_idx != -1:
            used_agent[best_idx] = True
            matched += 1
            # ordering check for the two modes that appear in ordering_check
            if ordering and sym == ordering['sym1'] and abs(agent_modes[best_idx]['freq'] - ordering['freq1']) <= window:
                match_ordering[sym] = agent_modes[best_idx]['freq']
            if ordering and sym == ordering['sym2'] and abs(agent_modes[best_idx]['freq'] - ordering['freq2']) <= window:
                match_ordering[sym] = agent_modes[best_idx]['freq']

    freq_score = matched / len(gold_modes)  # out of 6
    ordering_score = 1.0
    if match_ordering.get('B2') is not None and match_ordering.get('A2') is not None:
        ordering_score = 1.0 if match_ordering['B2'] < match_ordering['A2'] else 0.0
    else:
        ordering_score = 0.0  # if either mode not matched, fail ordering

    return 0.8 * freq_score + 0.2 * ordering_score


# === block: score_1 (check id='step_02_thermodynamic_properties') ===
def score_1(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    thermo_props = ctx['thermo_props']
    scores = []
    for prop in thermo_props:
        key = prop['key']
        gold = prop['gold']
        rel_tol = prop['rel_tol']
        if key not in artifact:
            scores.append(0.0)
            continue
        try:
            val = float(artifact[key])
        except (TypeError, ValueError):
            scores.append(0.0)
            continue
        rel_err = abs(val - gold) / gold if gold != 0 else abs(val - gold)
        if rel_err <= rel_tol:
            scores.append(1.0)
        else:
            # piecewise linear: score = max(0, 1 - (rel_err - rel_tol) / rel_tol)
            excess = (rel_err - rel_tol) / rel_tol
            scores.append(max(0.0, 1.0 - excess))
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'step_01_phonon_frequencies': score_0,
    'step_02_thermodynamic_properties': score_1,
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
