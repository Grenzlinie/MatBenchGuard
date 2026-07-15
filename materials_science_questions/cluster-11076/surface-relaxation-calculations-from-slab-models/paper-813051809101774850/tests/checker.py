import os
import json
import csv

# === author imports / helpers ===
import csv
import io
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
    return {}


# === block: score_0 (check id='lattice_constants') ===
def score_0(artifact, step, ctx):
    targets = step.get('targets', {})
    tols = step.get('tolerances', {})
    a_tol = tols.get('a', 0.05)
    c_tol = tols.get('c_ratio', 0.02)
    rows_by_metal = {}
    for row in artifact:
        metal = row.get('metal', '').strip()
        rows_by_metal[metal] = row
    total = len(targets)
    if total == 0:
        return 1.0
    score = 0
    for metal, target in targets.items():
        row = rows_by_metal.get(metal)
        if row is None:
            continue
        try:
            a = float(row.get('a', ''))
        except:
            continue
        ok_a = abs(a - target['a']) <= a_tol
        c_val = row.get('c_ratio', '').strip()
        has_c = c_val != '' and c_val != 'None' and c_val != 'nan'
        target_c = target.get('c_ratio')
        if target_c is None:
            ok_c = not has_c
        else:
            if has_c:
                try:
                    c = float(c_val)
                    ok_c = abs(c - target_c) <= c_tol
                except:
                    ok_c = False
            else:
                ok_c = False
        if ok_a and ok_c:
            score += 1
    return score / total


# === block: score_1 (check id='surface_properties') ===
def score_1(artifact, step, ctx):
    targets = step.get('config', {}).get('targets', [])
    tols = step.get('config', {}).get('tolerances', {})
    gtol = tols.get('gamma', 0.2)
    ttol = tols.get('tau', 0.5)
    trends_cfg = step.get('config', {}).get('trends', {})
    # Build lookup from CSV
    rows_lookup = {}
    for row in artifact:
        metal = row.get('metal', '').strip()
        surf = row.get('surface', '').strip()
        key = (metal, surf)
        rows_lookup[key] = row
    # Numeric score: fraction of targets matched within tolerance
    match_count = 0
    total_targets = len(targets)
    if total_targets == 0:
        return 1.0
    for t in targets:
        key = (t['metal'], t['surface'])
        row = rows_lookup.get(key)
        if row is None:
            continue
        try:
            gamma = float(row.get('gamma', ''))
            tau = float(row.get('tau', ''))
        except:
            continue
        if abs(gamma - t['gamma']) <= gtol and abs(tau - t['tau']) <= ttol:
            match_count += 1
    numeric_score = match_count / total_targets
    # Trend score
    trend_scores = []
    # alkali gamma decrease
    ak_metals = trends_cfg.get('alkali_gamma_decrease', {}).get('metals', [])
    if ak_metals:
        gamma_vals = []
        valid = True
        for m in ak_metals:
            # find row for metal; we need gamma for the expected surface (bcc(110))
            row = rows_lookup.get((m, 'bcc(110)'))
            if row is None:
                valid = False
                break
            try:
                gamma_vals.append(float(row['gamma']))
            except:
                valid = False
                break
        if valid and len(gamma_vals) == len(ak_metals):
            # decreasing order
            if all(gamma_vals[i] > gamma_vals[i+1] for i in range(len(gamma_vals)-1)):
                trend_scores.append(1.0)
            else:
                trend_scores.append(0.0)
        else:
            trend_scores.append(0.0)
    # alkaline earth gamma decrease
    ae_metals = trends_cfg.get('alkaline_earth_gamma_decrease', {}).get('metals', [])
    if ae_metals:
        gamma_vals = []
        valid = True
        expected_surfaces = {'Be': 'hcp(0001)', 'Mg': 'hcp(0001)', 'Ca': 'fcc(111)', 'Sr': 'fcc(111)', 'Ba': 'bcc(110)'}
        for m in ae_metals:
            key = (m, expected_surfaces.get(m, ''))
            row = rows_lookup.get(key)
            if row is None:
                valid = False
                break
            try:
                gamma_vals.append(float(row['gamma']))
            except:
                valid = False
                break
        if valid and len(gamma_vals) == len(ae_metals):
            if all(gamma_vals[i] > gamma_vals[i+1] for i in range(len(gamma_vals)-1)):
                trend_scores.append(1.0)
            else:
                trend_scores.append(0.0)
        else:
            trend_scores.append(0.0)
    # 4d local minimum Tc
    cm_cfg = trends_cfg.get('4d_local_minimum_tc', {}).get('checks', [])
    # Build lookup for 4d metals by metal name: gamma, tau from expected surfaces
    lookup_4d = {}
    for t in targets:
        if t['metal'] in ['Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd']:
            key = (t['metal'], t['surface'])
            row = rows_lookup.get(key)
            if row:
                try:
                    g = float(row['gamma'])
                    t_val = float(row['tau'])
                    lookup_4d[t['metal']] = {'gamma': g, 'tau': t_val}
                except:
                    pass
    if 'Tc' in lookup_4d:
        tc_data = lookup_4d['Tc']
        for check in cm_cfg:
            metric = check.get('metric')
            lower_than = check.get('lower_than', [])
            ok = True
            for m in lower_than:
                if m not in lookup_4d:
                    ok = False
                    break
                val_m = lookup_4d[m].get(metric)
                val_tc = tc_data.get(metric)
                if val_m is None or val_tc is None:
                    ok = False
                elif not (val_tc < val_m):
                    ok = False
                else:
                    continue
            trend_scores.append(1.0 if ok else 0.0)
    else:
        trend_scores.append(0.0)
    # Combine numeric and trend scores with weights
    num_weight = 0.8
    trend_weight = 0.2
    avg_trend = sum(trend_scores) / len(trend_scores) if trend_scores else 1.0
    return num_weight * numeric_score + trend_weight * avg_trend


_SCORERS = {
    'lattice_constants': score_0,
    'surface_properties': score_1,
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
