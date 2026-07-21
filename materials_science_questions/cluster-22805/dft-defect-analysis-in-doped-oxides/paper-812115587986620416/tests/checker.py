import os
import json
import csv

# === author imports / helpers ===
import math


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
    step_di = next(s for s in spec['steps'] if s['id'] == 'step_di_occupancy')
    ctx = {}
    ctx['d0'] = step_di['d0_mapping']
    ctx['li_bonds'] = step_di['li_bonds']
    ctx['nb_bonds'] = step_di['nb_bonds']
    ctx['B'] = step_di['B']
    ctx['valence_map'] = step_di['valence_map']
    ctx['tol_di'] = step_di['tolerance_di']
    import csv, os
    occ_path = os.path.join(outputs_dir, 'dopant_di_occupancy.csv')
    ctx['occupancy_data'] = {}
    if os.path.exists(occ_path):
        with open(occ_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                ion = row['ion'].strip()
                try:
                    di_li = float(row['d_i_Li'])
                    di_nb = float(row['d_i_Nb'])
                    occ = row['occupancy_predicted'].strip()
                    ctx['occupancy_data'][ion] = {'d_i_Li': di_li, 'd_i_Nb': di_nb, 'occupancy': occ}
                except:
                    pass
    return ctx


# === block: score_0 (check id='step_di_occupancy') ===
def score_0(artifact, step, ctx):
    d0 = ctx['d0']
    li_bonds = ctx['li_bonds']
    nb_bonds = ctx['nb_bonds']
    B = ctx['B']
    valence_map = ctx['valence_map']
    tol_di = ctx['tol_di']
    def compute_di(ion, site_bonds, valence):
        d0_val = d0[ion]
        s = 0.0
        for dist, mult in site_bonds:
            s += mult * math.exp((d0_val - dist) / B)
        return abs(valence - s)
    scores = []
    for row in artifact:
        ion = row['ion'].strip()
        try:
            di_li = float(row['d_i_Li'])
            di_nb = float(row['d_i_Nb'])
            occ_pred = row['occupancy_predicted'].strip().lower()
        except:
            scores.append(0.0)
            continue
        v = valence_map.get(ion)
        if v is None:
            scores.append(0.0)
            continue
        exp_li = compute_di(ion, li_bonds, v)
        exp_nb = compute_di(ion, nb_bonds, v)
        delta_li = abs(di_li - exp_li)
        delta_nb = abs(di_nb - exp_nb)
        max_delta = max(delta_li, delta_nb)
        di_score = max(0.0, 1.0 - max_delta / tol_di) if tol_di > 0 else 1.0 if max_delta == 0 else 0.0
        if exp_li < exp_nb:
            exp_occ = 'li'
        elif exp_li > exp_nb:
            exp_occ = 'nb'
        else:
            exp_occ = 'borderline'
        occ_correct = 1.0 if occ_pred == exp_occ else 0.0
        ion_score = 0.7 * di_score + 0.3 * occ_correct
        scores.append(ion_score)
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# === block: score_1 (check id='step_threshold') ===
def score_1(artifact, step, ctx):
    critical_GII = step['critical_GII']
    gold_thresholds = step['thresholds_gold']
    tol_th = step['tolerance_threshold']
    ion_list = step['ion_list']
    occ_data = ctx['occupancy_data']
    valence_map = ctx['valence_map']
    agent_th = {}
    for row in artifact:
        ion = row['ion'].strip()
        try:
            th = float(row['threshold_concentration_mol_percent'])
            agent_th[ion] = th
        except:
            agent_th[ion] = None
    scores = []
    for ion in ion_list:
        if ion not in occ_data:
            scores.append(0.0)
            continue
        di_li = occ_data[ion]['d_i_Li']
        v = valence_map[ion]
        z_m1 = v - 1
        a = (di_li + z_m1) ** 2 / 3.0
        b = di_li ** 2 + z_m1
        C = 5.0 * critical_GII ** 2
        disc = b * b + 4.0 * a * C
        if disc < 0 or a == 0:
            scores.append(0.0)
            continue
        x = (-b + math.sqrt(disc)) / (2.0 * a)
        comp_th = x * 100.0
        agent_val = agent_th.get(ion)
        if agent_val is None:
            scores.append(0.0)
            continue
        diff = abs(agent_val - comp_th)
        if diff <= tol_th:
            scores.append(1.0)
        else:
            scores.append(max(0.0, 1.0 - diff / tol_th))
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


_SCORERS = {
    'step_di_occupancy': score_0,
    'step_threshold': score_1,
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
