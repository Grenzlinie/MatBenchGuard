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
    return {'gold': spec.get('gold_values', [])}


# === block: score_0 (check id='file_structure') ===
def score_0(artifact, step, ctx):
    if not isinstance(artifact, dict):
        return 0.0
    for key in ['reactants','TS','products']:
        if key not in artifact or not isinstance(artifact[key], list) or len(artifact[key])==0:
            return 0.0
    return 1.0


# === block: score_1 (check id='b3lyp_relative_energies_recompute') ===
def score_1(artifact, step, ctx):
    gold_entries = ctx['gold']
    gold_b3lyp = [g for g in gold_entries if g['method']=='B3LYP']
    if not gold_b3lyp:
        return 1.0
    agents = []
    for key in ['reactants','TS','products']:
        agents.extend([e for e in artifact.get(key, []) if e.get('method')=='B3LYP'])
    ref_energies = {}
    for e in agents:
        if e['spin_state']=='singlet' and e['species']=='reactant':
            ref_energies[(e['n'], e['metal'])] = e['absolute_energy_Hartree']
    scores = []
    for gold in gold_b3lyp:
        agent = None
        for a in agents:
            if a['n']==gold['n'] and a['metal']==gold['metal'] and a['spin_state']==gold['spin_state'] and a['species']==gold['species']:
                agent = a
                break
        if agent is None:
            scores.append(0.0)
            continue
        ref_key = (gold['n'], gold['metal'])
        if ref_key not in ref_energies:
            scores.append(0.0)
            continue
        recomputed_rel = (agent['absolute_energy_Hartree'] - ref_energies[ref_key]) * 627.509
        expected = gold['rel_energy_uncorrected']
        error = abs(recomputed_rel - expected)
        if error <= 5:
            uc_score = 1.0
        elif error <= 10:
            uc_score = 0.5
        else:
            uc_score = max(0.0, 1.0 - (error - 10)/20)
        zpe_score = 0.0
        if gold.get('rel_energy_zpe_corrected') is not None and agent.get('relative_energy_ZPE_corrected') is not None:
            zpe_error = abs(agent['relative_energy_ZPE_corrected'] - gold['rel_energy_zpe_corrected'])
            if zpe_error <= 5:
                zpe_score = 1.0
            elif zpe_error <= 10:
                zpe_score = 0.5
            else:
                zpe_score = max(0.0, 1.0 - (zpe_error - 10)/20)
            entry_score = 0.7 * uc_score + 0.3 * zpe_score
        else:
            entry_score = uc_score
        scores.append(entry_score)
    if not scores:
        return 1.0
    return sum(scores)/len(scores)


# === block: score_2 (check id='pbe_reactants_relative_energies') ===
def score_2(artifact, step, ctx):
    gold_pbe = [g for g in ctx['gold'] if g['method']=='PBE' and g['n']==0 and g['species']=='reactant']
    if not gold_pbe:
        return 1.0
    agents_pbe = []
    for key in ['reactants','TS','products']:
        agents_pbe.extend([e for e in artifact.get(key, []) if e.get('method')=='PBE' and e.get('n')==0])
    ref_energies = {}
    for e in agents_pbe:
        if e['spin_state']=='singlet' and e['species']=='reactant':
            ref_energies[(e['n'], e['metal'])] = e['absolute_energy_Hartree']
    scores = []
    for gold in gold_pbe:
        agent = None
        for a in agents_pbe:
            if a['n']==gold['n'] and a['metal']==gold['metal'] and a['spin_state']==gold['spin_state'] and a['species']==gold['species']:
                agent = a
                break
        if agent is None:
            scores.append(0.0)
            continue
        ref_key = (gold['n'], gold['metal'])
        if ref_key not in ref_energies:
            scores.append(0.0)
            continue
        recomputed_rel = (agent['absolute_energy_Hartree'] - ref_energies[ref_key]) * 627.509
        expected = gold['rel_energy_uncorrected']
        error = abs(recomputed_rel - expected)
        if error <= 5:
            s = 1.0
        elif error <= 10:
            s = 0.5
        else:
            s = max(0.0, 1.0 - (error - 10)/20)
        scores.append(s)
    if not scores:
        return 1.0
    return sum(scores)/len(scores)


# === block: score_3 (check id='st_gap_trends') ===
def score_3(artifact, step, ctx):
    reactants = [e for e in artifact.get('reactants', []) if e.get('method')=='B3LYP']
    ref_energies = {}
    for e in reactants:
        if e['spin_state']=='singlet':
            ref_energies[(e['n'], e['metal'])] = e['absolute_energy_Hartree']
    rel_T = {}
    for e in reactants:
        if e['spin_state']=='triplet' and (e['n'], e['metal']) in ref_energies:
            rel_T[(e['n'], e['metal'])] = (e['absolute_energy_Hartree'] - ref_energies[(e['n'], e['metal'])]) * 627.509
    conditions = [
        (0, 'Ti', lambda v: v < -15),
        (4, 'Ti', lambda v: v < -15),
        (0, 'Zr', lambda v: -15 <= v <= 15),
        (4, 'Zr', lambda v: -15 <= v <= 15),
        (0, 'Hf', lambda v: -15 <= v <= 15),
        (4, 'Hf', lambda v: -15 <= v <= 15),
    ]
    correct = 0
    for n,metal,cond in conditions:
        v = rel_T.get((n,metal))
        if v is not None and cond(v):
            correct += 1
    return correct / 6.0


# === block: score_4 (check id='barrier_trends') ===
def score_4(artifact, step, ctx):
    hartree_to_kcal = 627.509
    score = 0.0
    for n_val in [0, 4]:
        barriers = {}
        for metal in ['Ti', 'Zr', 'Hf']:
            reactants = [e for e in artifact.get('reactants', []) 
                         if e.get('method') == 'B3LYP' and e['n'] == n_val and e['metal'] == metal]
            ts_list = [e for e in artifact.get('TS', []) 
                       if e.get('method') == 'B3LYP' and e['n'] == n_val and e['metal'] == metal]
            if not reactants or not ts_list:
                continue
            min_reactant = min(e['absolute_energy_Hartree'] for e in reactants)
            min_ts = min(e['absolute_energy_Hartree'] for e in ts_list)
            barrier = (min_ts - min_reactant) * hartree_to_kcal
            barriers[metal] = barrier
        if all(m in barriers for m in ('Ti', 'Zr', 'Hf')):
            bTi = barriers['Ti']
            bZr = barriers['Zr']
            bHf = barriers['Hf']
            if bTi > bZr and bTi > bHf and abs(bZr - bHf) <= 5:
                score += 0.5
    return score


# === block: score_5 (check id='pbe_st_gap_ti') ===
def score_5(artifact, step, ctx):
    reactants = artifact.get('reactants', [])
    ref_sing = None
    for e in reactants:
        if e.get('method')=='PBE' and e['n']==0 and e['metal']=='Ti' and e['spin_state']=='singlet':
            ref_sing = e['absolute_energy_Hartree']
    if ref_sing is None:
        return 0.0
    trip = None
    for e in reactants:
        if e.get('method')=='PBE' and e['n']==0 and e['metal']=='Ti' and e['spin_state']=='triplet':
            trip = e['absolute_energy_Hartree']
    if trip is None:
        return 0.0
    rel_T = (trip - ref_sing) * 627.509
    gap = -rel_T
    if 0 < gap <= 10:
        return 1.0
    return 0.0


_SCORERS = {
    'file_structure': score_0,
    'b3lyp_relative_energies_recompute': score_1,
    'pbe_reactants_relative_energies': score_2,
    'st_gap_trends': score_3,
    'barrier_trends': score_4,
    'pbe_st_gap_ti': score_5,
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
