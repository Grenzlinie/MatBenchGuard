import os
import json
import csv

# === author imports / helpers ===
import os, csv, math, json


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
    return {'spec': spec}


# === block: score_0 (check id='barrier_heights') ===
def score_0(artifact, step, ctx):
    step = ctx['spec']['steps'][0]
    ref = step['reference']
    tols = step['tolerances']
    expected = set(ref.keys())
    found = set()
    row_scores = []
    for r in artifact:
        rot = r.get('rotation', '').strip()
        if not rot:
            continue
        if rot in expected:
            found.add(rot)
            h = float(r['barrier_height'])
            g = ref[rot]
            t = tols[rot]
            d = abs(h - g)
            s = 1.0 if d <= t else max(0.0, 1.0 - (d - t) / t)
            row_scores.append(s)
        else:
            row_scores.append(0.0)
    if not found and expected:
        return 0.0
    coverage = len(found) / len(expected) if expected else 1.0
    avg = sum(row_scores) / max(len(row_scores), 1)
    return coverage * avg


# === block: score_1 (check id='conformer_energies_populations') ===
def score_1(artifact, step, ctx):
    step = ctx['spec']['steps'][1]
    ref = step['reference']
    tol = step['tolerances']
    R = 0.0019872041  # kcal/mol·K
    T = 298.0
    def boltzmann_factor(e):
        return math.exp(-e / (R * T))
    data = {}
    for row in artifact:
        name = row['conformer'].strip()
        data[name] = {
            'de1': float(row['deltaE_631Gdp']),
            'de2': float(row['deltaE_6311PlusG3df2p']),
            'pop': float(row['Boltzmann_population']),
            'dh': float(row['deltaH_formation'])
        }
    conformers = list(ref.keys())
    scores = []
    for conf in conformers:
        if conf not in data:
            scores.append(0.0)
            continue
        d = data[conf]
        g = ref[conf]
        # deltaE scores
        de1_score = 1.0 if abs(d['de1'] - g['deltaE_631Gdp']) <= tol['deltaE'] else max(0, 1 - (abs(d['de1'] - g['deltaE_631Gdp']) - tol['deltaE'])/tol['deltaE'])
        de2_score = 1.0 if abs(d['de2'] - g['deltaE_6311PlusG3df2p']) <= tol['deltaE'] else max(0, 1 - (abs(d['de2'] - g['deltaE_6311PlusG3df2p']) - tol['deltaE'])/tol['deltaE'])
        # population score
        pop_gold_score = 1.0 if abs(d['pop'] - g['Boltzmann_population']) <= tol['population_gold'] else max(0, 1 - (abs(d['pop'] - g['Boltzmann_population']) - tol['population_gold'])/tol['population_gold'])
        # recompute populations from submitted deltaE values (both basis sets, take best consistency)
        de1_vals = [row['de1'] for row in data.values()]
        E_ref = min(de1_vals)
        weights = [boltzmann_factor(de1_vals[i] - E_ref) for i in range(len(de1_vals))]
        Z = sum(weights)
        pop_recomputed = [w / Z for w in weights]
        # map recomputed back to conformer order
        conf_idx = conformers.index(conf)
        pop_recomp = pop_recomputed[conf_idx]
        de1_consistency = 1.0 if abs(d['pop'] - pop_recomp) <= tol['population_recompute_tol'] else 0.0
        # try with deltaE2
        de2_vals = [row['de2'] for row in data.values()]
        E_ref2 = min(de2_vals)
        weights2 = [boltzmann_factor(de2_vals[i] - E_ref2) for i in range(len(de2_vals))]
        Z2 = sum(weights2)
        pop_recomputed2 = [w / Z2 for w in weights2]
        pop_recomp2 = pop_recomputed2[conf_idx]
        de2_consistency = 1.0 if abs(d['pop'] - pop_recomp2) <= tol['population_recompute_tol'] else 0.0
        consistency_score = max(de1_consistency, de2_consistency)
        pop_score = 0.5 * pop_gold_score + 0.5 * consistency_score
        # enthalpy score
        dh_score = 1.0 if abs(d['dh'] - g['deltaH_formation']) <= tol['deltaH_formation'] else max(0, 1 - (abs(d['dh'] - g['deltaH_formation']) - tol['deltaH_formation'])/tol['deltaH_formation'])
        scores.append((de1_score + de2_score + pop_score + dh_score) / 4.0)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_2 (check id='ensemble_enthalpy') ===
def score_2(artifact, step, ctx):
    step = ctx['spec']['steps'][2]
    gold = step['reference']
    tol = step['tolerance']
    sub_val = float(artifact.strip())
    # recompute from conformer csv
    csv_path = os.path.join('/app/outputs', ctx['spec']['steps'][1]['output_file'])
    if not os.path.exists(csv_path):
        recomputed = None
    else:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            pop = []
            dh = []
            for row in reader:
                pop.append(float(row['Boltzmann_population']))
                dh.append(float(row['deltaH_formation']))
        recomputed = sum(p * h for p, h in zip(pop, dh))
    base_score = 1.0 if abs(sub_val - gold) <= tol else max(0.0, 1.0 - (abs(sub_val - gold) - tol) / tol)
    if recomputed is not None and abs(sub_val - recomputed) <= 1e-6:
        consistency_factor = 1.0
    else:
        consistency_factor = 0.8
    return base_score * consistency_factor


_SCORERS = {
    'barrier_heights': score_0,
    'conformer_energies_populations': score_1,
    'ensemble_enthalpy': score_2,
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
