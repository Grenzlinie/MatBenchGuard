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


# === block: score_0 (check id='step03_curvature_gap_csv') ===
def score_0(artifact, step, ctx):
        gold = step.get('gold', {})
        flat_EG = gold.get('flat_EG', 0.6)
        flat_NEG = gold.get('flat_NEG', 1.2)
        c1_kappa = gold.get('c1_kappa', 0.0625)
        c1_EG = gold.get('c1_EG', 0.55)
        c1_NEG = gold.get('c1_NEG', 1.3)
        high_kappa = gold.get('high_kappa', 0.1667)
        high_EG = gold.get('high_EG', 0.2)
        tol_EG = gold.get('tolerance_EG', 0.15)
        tol_NEG = gold.get('tolerance_NEG', 0.15)

        rows = artifact  # list of dicts with keys 'curvature','EG','NEG'
        if not rows:
            return 0.0
        curv_vals = []
        eg_vals = []
        neg_vals = []
        for r in rows:
            try:
                curv = float(r['curvature'])
                eg = float(r['EG'])
                neg = float(r['NEG'])
            except:
                continue
            curv_vals.append(curv)
            eg_vals.append(eg)
            neg_vals.append(neg)
        if not curv_vals:
            return 0.0

        # helper: find closest row to target curvature
        def get_val_at(target, vals, allows_none=False):
            best = None
            best_dist = None
            for c, eg, neg in zip(curv_vals, eg_vals, neg_vals):
                dist = abs(c - target)
                if best is None or dist < best_dist:
                    best = (c, eg, neg)
                    best_dist = dist
            if best is None:
                return None
            return best[1] if vals == 'EG' else best[2]

        checks = []
        # Flat point present
        flat_c = get_val_at(0.0, 'curvature')
        has_flat = any(abs(c-0.0)<0.005 for c in curv_vals)
        checks.append(1.0 if has_flat else 0.0)  # weight 0.1
        # High curvature point present
        has_high = any(abs(c-high_kappa)<0.01 for c in curv_vals)
        checks.append(1.0 if has_high else 0.0)  # weight 0.1
        # EG at flat within tolerance
        flat_eg_val = get_val_at(0.0, 'EG')
        eg_flat_ok = flat_eg_val is not None and abs(flat_eg_val - flat_EG) <= tol_EG
        checks.append(1.0 if eg_flat_ok else 0.0)  # weight 0.1
        # NEG at flat within tolerance
        flat_neg_val = get_val_at(0.0, 'NEG')
        neg_flat_ok = flat_neg_val is not None and abs(flat_neg_val - flat_NEG) <= tol_NEG
        checks.append(1.0 if neg_flat_ok else 0.0)  # weight 0.1
        # EG at kappa_c1 within tolerance
        c1_eg_val = get_val_at(c1_kappa, 'EG')
        eg_c1_ok = c1_eg_val is not None and abs(c1_eg_val - c1_EG) <= tol_EG
        checks.append(1.0 if eg_c1_ok else 0.0)  # weight 0.1
        # NEG at kappa_c1 within tolerance
        c1_neg_val = get_val_at(c1_kappa, 'NEG')
        neg_c1_ok = c1_neg_val is not None and abs(c1_neg_val - c1_NEG) <= tol_NEG
        checks.append(1.0 if neg_c1_ok else 0.0)  # weight 0.1
        # NEG hump: NEG at kappa_c1 > NEG at flat
        hump_ok = (c1_neg_val is not None and flat_neg_val is not None) and (c1_neg_val > flat_neg_val)
        checks.append(1.0 if hump_ok else 0.0)  # weight 0.15
        # EG decrease: EG at kappa_c1 <= EG at flat - 0.02 (allow slight increase)
        eg_dec_ok = (c1_eg_val is not None and flat_eg_val is not None) and (c1_eg_val <= flat_eg_val - 0.02)
        checks.append(1.0 if eg_dec_ok else 0.0)  # weight 0.15
        # EG at high curvature significantly lower
        high_eg_val = get_val_at(high_kappa, 'EG')
        high_drop_ok = (high_eg_val is not None and flat_eg_val is not None) and (flat_eg_val - high_eg_val) > 0.3
        checks.append(1.0 if high_drop_ok else 0.0)  # weight 0.2

        weights = [0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.15, 0.15, 0.20]
        total = sum(c*w for c,w in zip(checks, weights))
        return total


# === block: score_1 (check id='step04_critical_curvatures') ===
def score_1(artifact, step, ctx):
        text = artifact  # string content
        import re
        gold = step['gold']
        k0_target = gold['kappa0']
        kc1_target = gold['kappac1']
        kc2_target = gold['kappac2']
        tol = gold['tolerance']
        def extract_value(label):
            pattern = label + r':\s*([0-9]+\.?[0-9]*)'
            m = re.search(pattern, text)
            if m:
                try:
                    return float(m.group(1))
                except:
                    pass
            return None
        v0 = extract_value('kappa0')
        v1 = extract_value('kappac1')
        v2 = extract_value('kappac2')
        score = 0.0
        if v0 is not None and abs(v0 - k0_target) <= tol:
            score += 1/3
        if v1 is not None and abs(v1 - kc1_target) <= tol:
            score += 1/3
        if v2 is not None and abs(v2 - kc2_target) <= tol:
            score += 1/3
        return score


# === block: score_2 (check id='step06_flat_width_csv') ===
def score_2(artifact, step, ctx):
        gold = step['gold']
        peak_ns = gold['peak_ns']
        eg_min_peak = gold['EG_min_peak']
        eg_max_neighbor = gold['EG_max_neighbor']
        small_split_max = gold['small_split_max']
        ratio_min = gold['split_ratio_min']
        ratio_max = gold['split_ratio_max']
        tol = gold['EG_flat_tolerance']
        rows = artifact  # list of dicts with n,EG,delta_EC,delta_EV
        if not rows:
            return 0.0
        # build dict by n
        data = {}
        for r in rows:
            try:
                n = int(r['n'])
                eg = float(r['EG'])
                dec = float(r['delta_EC'])
                dev = float(r['delta_EV'])
                data[n] = (eg, dec, dev)
            except:
                continue
        full_ns = set(gold['n_range'])
        if not full_ns.issubset(data.keys()):
            return 0.0
        checks = []
        # property 1: EG for peak_ns > neighbors
        for p in peak_ns:
            eg_p = data[p][0]
            neighbors = []
            if p-1 in data:
                neighbors.append(data[p-1][0])
            if p+1 in data:
                neighbors.append(data[p+1][0])
            ok = True
            for nb in neighbors:
                if eg_p <= nb:
                    ok = False
                    break
            checks.append(1.0 if ok else 0.0)
        n_peaks = len(peak_ns)
        # property 2: EG for peak_ns > eg_min_peak
        for p in peak_ns:
            eg_p = data[p][0]
            checks.append(1.0 if eg_p >= eg_min_peak else 0.0)
        # property 3: EG for non-peak n is <= eg_max_neighbor (or smaller than peaks)
        other_ns = [n for n in full_ns if n not in peak_ns]
        for n in other_ns:
            eg = data[n][0]
            checks.append(1.0 if eg <= eg_max_neighbor else 0.0)
        # property 4: for peak_ns, delta_EC and delta_EV small
        for p in peak_ns:
            _, dec, dev = data[p]
            if dec is not None and dec <= small_split_max:
                checks.append(1.0 if True else 0.0)  # always 1
            else:
                checks.append(0.0)
            if dev is not None and dev <= small_split_max:
                checks.append(1.0 if True else 0.0)
            else:
                checks.append(0.0)
        # property 5: for other_ns, delta_EV ~ 3 * delta_EC
        for n in other_ns:
            _, dec, dev = data[n]
            if dec is None or dev is None or dec == 0:
                checks.append(0.0)
                continue
            ratio = dev / dec if dec else 0
            ok = ratio_min <= ratio <= ratio_max
            checks.append(1.0 if ok else 0.0)
        if not checks:
            return 0.0
        return sum(checks)/len(checks)


# === block: score_3 (check id='step08_exciton_table') ===
def score_3(artifact, step, ctx):
        gold = step['gold']
        rows_gold = gold['rows']
        tol_rel = gold['tolerance_rel']
        tol_abs = gold['tolerance_abs']
        rows = artifact  # list of dicts
        if not rows:
            return 0.0
        def get_tolerance(target):
            return max(tol_rel * abs(target), tol_abs)
        score = 0.0
        total = 0
        for rg in rows_gold:
            rad = rg['radius']
            # find matching row by radius string
            row_agent = None
            for r in rows:
                if str(r.get('radius','')).strip().lower() == rad.strip().lower():
                    row_agent = r
                    break
            if row_agent is None:
                continue
            for field in ['Eg','EA','Eb','EAtriplet','DeltaST']:
                target = rg[field]
                try:
                    val = float(row_agent.get(field))
                except:
                    continue
                err = abs(val - target)
                ok = err <= get_tolerance(target)
                score += 1.0 if ok else max(0.0, 1.0 - err/get_tolerance(target))
                total += 1
        if total == 0:
            return 0.0
        return score / total


_SCORERS = {
    'step03_curvature_gap_csv': score_0,
    'step04_critical_curvatures': score_1,
    'step06_flat_width_csv': score_2,
    'step08_exciton_table': score_3,
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
