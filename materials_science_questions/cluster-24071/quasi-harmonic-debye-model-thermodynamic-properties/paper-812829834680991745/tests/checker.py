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
    return spec


# === block: score_0 (check id='step_01_properties') ===
def score_0(artifact, step, ctx):
    gold_compositions = step['gold']['compositions']
    tols = step['gold']['columns_tolerances']
    gold_map = {c['composition'].strip(): c for c in gold_compositions}
    row_scores = {col: [] for col in ['a0','B0','Theta','gamma','alpha','kappa_lat_300K']}
    for row in artifact:
        comp = row['composition'].strip()
        gold = gold_map.get(comp)
        if not gold:
            continue
        a0 = float(row['a0']); rel = abs(a0 - gold['a0']) / gold['a0']
        row_scores['a0'].append(1.0 if rel <= tols['a0']['tolerance_relative'] else 0.0)
        b0 = float(row['B0']); rel = abs(b0 - gold['B0']) / gold['B0']
        row_scores['B0'].append(1.0 if rel <= tols['B0']['tolerance_relative'] else 0.0)
        theta = float(row['Theta']); rel = abs(theta - gold['Theta']) / gold['Theta']
        row_scores['Theta'].append(1.0 if rel <= tols['Theta']['tolerance_relative'] else 0.0)
        kappa = float(row['kappa_lat_300K']); rel = abs(kappa - gold['kappa_lat_300K']) / gold['kappa_lat_300K']
        row_scores['kappa_lat_300K'].append(1.0 if rel <= tols['kappa_lat_300K']['tolerance_relative'] else 0.0)
        gamma = float(row['gamma'])
        # Use a generous relative tolerance (50%) for gamma to accommodate implementation spread
        gamma_tol_rel = 0.5
        row_scores['gamma'].append(1.0 if abs(gamma - gold['gamma_gold']) / gold['gamma_gold'] <= gamma_tol_rel else 0.0)
        alpha = float(row['alpha'])
        row_scores['alpha'].append(1.0 if tols['alpha']['min'] < alpha < tols['alpha']['max'] else 0.0)
    col_means = {k: (sum(v)/len(v) if v else 0.0) for k, v in row_scores.items()}
    weights = {'a0':0.25, 'B0':0.15, 'Theta':0.25, 'gamma':0.15, 'alpha':0.05, 'kappa_lat_300K':0.15}
    total = sum(weights[k]*col_means[k] for k in weights)
    return total


# === block: score_1 (check id='step_02_kappa_vs_T') ===
def score_1(artifact, step, ctx):
    gold = step['gold']
    ref = gold['reference']
    comp_names = list(ref.keys())
    tol_rel = gold['tolerance_relative_kappa']
    # build per-comp T->kappa dict
    data = {}
    for row in artifact:
        comp = row['composition'].strip()
        t = int(row['T'])
        kappa = float(row['kappa_lat'])
        data.setdefault(comp, {})[t] = kappa
    # kappa_300 and kappa_1000 match
    scores_300 = []
    scores_1000 = []
    for comp in comp_names:
        if comp in data:
            v300 = data[comp].get(300, None)
            v1000 = data[comp].get(1000, None)
            if v300 is not None:
                rel = abs(v300 - ref[comp]['kappa_300']) / ref[comp]['kappa_300']
                scores_300.append(1.0 if rel <= tol_rel else 0.0)
            else: scores_300.append(0.0)
            if v1000 is not None:
                rel = abs(v1000 - ref[comp]['kappa_1000']) / ref[comp]['kappa_1000']
                scores_1000.append(1.0 if rel <= tol_rel else 0.0)
            else: scores_1000.append(0.0)
        else:
            scores_300.append(0.0)
            scores_1000.append(0.0)
    score_k300 = sum(scores_300)/len(scores_300) if scores_300 else 0.0
    score_k1000 = sum(scores_1000)/len(scores_1000) if scores_1000 else 0.0
    # reduction percentages
    red_target = gold['reduction_percents']
    red_tol = gold['reduction_tolerance_pp']
    red_scores = []
    baseline = data.get('TiNiSn', {}).get(300, None)
    if baseline:
        for comp, target in red_target.items():
            if comp in data and 300 in data[comp]:
                red = (baseline - data[comp][300]) / baseline * 100
                diff = abs(red - target)
                red_scores.append(1.0 if diff <= red_tol else max(0.0, (red_tol - diff)/red_tol*0.5))
            else:
                red_scores.append(0.0)
    score_red = sum(red_scores)/len(red_scores) if red_scores else 0.0
    # ordering
    order = gold['ordering']
    ord_scores = []
    Ts = sorted({int(t) for d in data.values() for t in d})
    for t in Ts:
        vals = []
        for comp in order:
            vals.append(data.get(comp, {}).get(t, None))
        if None in vals:
            ord_scores.append(0.0)
        else:
            # check increasing
            ok = all(vals[i] < vals[i+1] for i in range(len(vals)-1))
            ord_scores.append(1.0 if ok else 0.0)
    score_ord = sum(ord_scores)/len(ord_scores) if ord_scores else 0.0
    # monotonic decreasing for each composition
    mono_scores = []
    for comp in comp_names:
        if comp in data:
            ts = sorted(data[comp].keys())
            dec = all(data[comp][ts[i]] >= data[comp][ts[i+1]] - 1e-12 for i in range(len(ts)-1))
            mono_scores.append(1.0 if dec else 0.0)
        else:
            mono_scores.append(0.0)
    score_mono = sum(mono_scores)/len(mono_scores) if mono_scores else 0.0
    # weighted sum
    w = {'k300':0.2, 'k1000':0.2, 'reduction':0.2, 'ordering':0.2, 'monotonic':0.2}
    return w['k300']*score_k300 + w['k1000']*score_k1000 + w['reduction']*score_red + w['ordering']*score_ord + w['monotonic']*score_mono


_SCORERS = {
    'step_01_properties': score_0,
    'step_02_kappa_vs_T': score_1,
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
