import os
import json
import csv

# === author imports / helpers ===
import statistics


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
    gold = {}
    for step in spec.get('steps', []):
        if step.get('id') == 'mulliken_value_match':
            gold = step['config'].get('gold', {})
            break
    return {'mulliken_gold': gold}


# === block: score_0 (check id='adsorption_energy_trends') ===
def score_0(artifact, step, ctx):
    rows = artifact
    sites = ['H\'', 'T3', 'T3\'', 'T4', 'T4\'']
    orientations = ['Cs-up', 'NF3-up']
    by_site_ori = {}
    for r in rows:
        site = r['site'].strip()
        ori = r['orientation'].strip()
        key = (site, ori)
        by_site_ori[key] = float(r['adsorption_energy_eV'])
    if len(by_site_ori) < 10:
        return 0.0
    cfg = step['config']
    akey = 'adsorption_energy_eV'
    # Condition 1: all negative
    cond1 = all(v < 0 for v in by_site_ori.values())
    # Condition 2: for each site, Cs-up < NF3-up
    cond2 = all(by_site_ori.get((s, 'Cs-up'), 0) < by_site_ori.get((s, 'NF3-up'), 0) for s in sites)
    # Condition 3: T4 Cs-up is minimum among Cs-up
    cs_up_vals = {s: by_site_ori[(s, 'Cs-up')] for s in sites}
    min_site = min(cs_up_vals, key=cs_up_vals.get)
    cond3 = (min_site == 'T4' and cs_up_vals['T4'] < min(cs_up_vals[s] for s in sites if s != 'T4'))
    # Condition 4: average Cs-up lower than average NF3-up (trend)
    avg_cs = statistics.mean([v for (s, o), v in by_site_ori.items() if o == 'Cs-up'])
    avg_nf3 = statistics.mean([v for (s, o), v in by_site_ori.items() if o == 'NF3-up'])
    cond4 = avg_cs < avg_nf3
    score = (cond1*0.25 + cond2*0.25 + cond3*0.25 + cond4*0.25)
    return score


# === block: score_1 (check id='workfunction_trends') ===
def score_1(artifact, step, ctx):
    rows = artifact
    config = step['config']
    clean_wf = float(config['clean_workfunction'])
    wf_col = 'work_function_eV'
    change_col = 'work_function_change_eV'
    orientations = ['Cs-up', 'NF3-up']
    sites = ['H\'', 'T3', 'T3\'', 'T4', 'T4\'']
    by_site_ori = {}
    for r in rows:
        s = r['site'].strip()
        o = r['orientation'].strip()
        wf = float(r[wf_col])
        ch = float(r[change_col])
        by_site_ori[(s, o)] = (wf, ch)
    if len(by_site_ori) < 10:
        return 0.0
    # Condition 1: all work function changes negative
    cond1 = all(ch < 0 for (wf, ch) in by_site_ori.values())
    # Condition 2: for each site, WF_change(Cs-up) < WF_change(NF3-up) (more negative)
    cond2 = all(by_site_ori[(s, 'Cs-up')][1] < by_site_ori[(s, 'NF3-up')][1] for s in sites)
    # Condition 3: all work functions below clean reference (4.95)
    cond3 = all(wf < clean_wf for (wf, ch) in by_site_ori.values())
    # Condition 4: work function change approx equals (wf - clean_wf) within 0.01 eV for consistency? Not required.
    score = (cond1*0.34 + cond2*0.33 + cond3*0.33)
    return score


# === block: score_2 (check id='mulliken_value_match') ===
def score_2(artifact, step, ctx):
    rows = artifact
    gold_dict = ctx.get('mulliken_gold', {})
    if not gold_dict:
        return 0.0
    cfg = step['config']
    tol_sub = float(cfg['tolerance_substrate'])
    tol_cs_nf3 = float(cfg['tolerance_cs_nf3'])
    fields = ['As_first_bilayer','Ga_first_bilayer','As_second_bilayer','Ga_second_bilayer','Cs','NF3']
    total_cells = 0
    matched = 0
    for row in rows:
        site = row['site'].strip()
        ori = row['orientation'].strip()
        key = f"{site},{ori}"
        if key not in gold_dict:
            continue
        expected = gold_dict[key]
        for f in fields:
            val = float(row.get(f, 0))
            exp = expected.get(f, 0)
            tol = tol_cs_nf3 if f in ('Cs','NF3') else tol_sub
            total_cells += 1
            if abs(val - exp) <= tol:
                matched += 1
    if total_cells == 0:
        return 0.0
    return matched / total_cells


# === block: score_3 (check id='mulliken_trends') ===
def score_3(artifact, step, ctx):
    rows = artifact
    cfg = step['config']
    neutral_max = float(cfg['nf3_neutral_max_abs'])
    neg_thresh = float(cfg['nf3_negative_thresh'])
    nf3_col = 'NF3'
    count_nf3up = 0
    count_neutral = 0
    count_csup = 0
    count_neg = 0
    for row in rows:
        ori = row['orientation'].strip()
        val = float(row.get(nf3_col, 0))
        if ori == 'NF3-up':
            count_nf3up += 1
            if abs(val) <= neutral_max:
                count_neutral += 1
        elif ori == 'Cs-up':
            count_csup += 1
            if val <= neg_thresh:
                count_neg += 1
    if count_nf3up == 0 or count_csup == 0:
        return 0.0
    score_nf3 = count_neutral / count_nf3up if count_nf3up > 0 else 0.0
    score_cs = count_neg / count_csup if count_csup > 0 else 0.0
    return 0.5 * score_nf3 + 0.5 * score_cs


# === block: score_4 (check id='dipole_trends') ===
def score_4(artifact, step, ctx):
    rows = artifact
    sites = ['H\'', 'T3', 'T3\'', 'T4', 'T4\'']
    by_site_ori = {}
    for r in rows:
        s = r['site'].strip()
        o = r['orientation'].strip()
        dz = float(r['dz_Ang'])
        q = float(r['Q_abs_e'])
        pz = float(r['Pz_eAng'])
        by_site_ori[(s, o)] = (dz, q, pz)
    if len(by_site_ori) < 10:
        return 0.0
    # check positive values
    all_pos = all(dz>0 and q>0 and pz>0 for (dz,q,pz) in by_site_ori.values())
    # per-site trends
    count_trends = 0
    total_trends = 3 * len(sites)
    for s in sites:
        if (s,'Cs-up') in by_site_ori and (s,'NF3-up') in by_site_ori:
            cs = by_site_ori[(s,'Cs-up')]
            nf = by_site_ori[(s,'NF3-up')]
            if cs[0] < nf[0]: count_trends += 1
            if cs[1] > nf[1]: count_trends += 1
            if cs[2] > nf[2]: count_trends += 1
    score_pos = 0.2 if all_pos else 0.0
    score_trend = 0.8 * (count_trends / total_trends) if total_trends > 0 else 0.0
    return score_pos + score_trend


# === block: score_5 (check id='dipole_ordering') ===
def score_5(artifact, step, ctx):
    rows = artifact
    cs_up = []
    for r in rows:
        if r['orientation'].strip() == 'Cs-up':
            site = r['site'].strip()
            pz = float(r['Pz_eAng'])
            cs_up.append((site, pz))
    if len(cs_up) < 5:
        return 0.0
    max_site = max(cs_up, key=lambda x: x[1])[0]
    min_site = min(cs_up, key=lambda x: x[1])[0]
    score = 0.0
    if max_site == "H'":
        score += 0.5
    if min_site == "T3'":
        score += 0.5
    return score


# === block: score_6 (check id='geometry_trends') ===
def score_6(artifact, step, ctx):
    rows = artifact
    sites = ['H\'', 'T3', 'T3\'', 'T4', 'T4\'']
    by_site_ori = {}
    for r in rows:
        s = r['site'].strip()
        o = r['orientation'].strip()
        d_cs_nf3 = float(r['D_Cs_NF3_Ang'])
        by_site_ori[(s, o)] = d_cs_nf3
    if len(by_site_ori) < 10:
        return 0.0
    # condition 1: all distances positive
    cond1 = all(v > 0 for v in by_site_ori.values())
    # condition 2: for each site, Cs-up distance < NF3-up distance
    cs_dists = [by_site_ori.get((s,'Cs-up'),None) for s in sites]
    nf_dists = [by_site_ori.get((s,'NF3-up'),None) for s in sites]
    cond2 = all(cs is not None and nf is not None and cs < nf for cs,nf in zip(cs_dists, nf_dists))
    score = 0.0
    if cond1:
        score += 0.5
    if cond2:
        score += 0.5
    return score


_SCORERS = {
    'adsorption_energy_trends': score_0,
    'workfunction_trends': score_1,
    'mulliken_value_match': score_2,
    'mulliken_trends': score_3,
    'dipole_trends': score_4,
    'dipole_ordering': score_5,
    'geometry_trends': score_6,
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
