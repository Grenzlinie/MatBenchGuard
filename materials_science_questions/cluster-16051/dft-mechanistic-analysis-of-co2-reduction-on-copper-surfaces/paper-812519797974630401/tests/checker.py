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


# === block: score_0 (check id='o2_dissociation') ===
def score_0(artifact, step, ctx):
    import csv, os, math
    rows = list(csv.DictReader(open(os.path.join('/app/outputs', step['output_file']))))
    if not rows:
        return 0.0
    gold = step['params']['gold_table']
    tols = step['params']['tolerances']
    fw = step['params']['field_weights']
    key = 'Model'
    agent_data = {}
    for r in rows:
        m = r[key].strip().lower()
        agent_data[m] = r
    row_scores = []
    for gr in gold:
        gm = gr[key].strip().lower()
        if gm not in agent_data:
            continue
        ar = agent_data[gm]
        f_scores = []
        for f, w in fw.items():
            if f not in ar:
                continue
            gv = gr[f]
            av = ar[f].strip()
            # handle null gold
            if gv == '' or gv is None:
                # acceptable if agent empty too
                if av == '' or av is None:
                    f_scores.append((w, 1.0))
                else:
                    f_scores.append((w, 0.0))
                continue
            # check if multi-number string
            if ',' in str(gv):
                try:
                    gnums = [float(x.strip()) for x in str(gv).split(',')]
                    anums = [float(x.strip()) for x in av.split(',')]
                    if len(gnums) != len(anums):
                        f_scores.append((w, 0.0))
                    else:
                        hit = all(abs(a - b) <= tols.get(f + '_numlist', 0.02) for a, b in zip(anums, gnums))
                        f_scores.append((w, 1.0 if hit else 0.0))
                except (ValueError, TypeError):
                    f_scores.append((w, 0.0))
            else:
                try:
                    gn = float(gv)
                    an = float(av)
                    tol = tols.get(f, 0.1)
                    f_scores.append((w, 1.0 if math.isclose(an, gn, rel_tol=0, abs_tol=tol) else 0.0))
                except (ValueError, TypeError):
                    f_scores.append((w, 0.0))
        if f_scores:
            row_score = sum(w * s for w, s in f_scores) / sum(w for w, s in f_scores)
            row_scores.append(row_score)
    row_avg = sum(row_scores) / len(row_scores) if row_scores else 0.0
    trend_score = 1.0
    trends = step['params'].get('trends', [])
    if trends:
        t = trends[0]
        if t['description'].startswith('O2 dissociation'):
            order = [m.strip().lower() for m in t['expected_order']]
            vals = []
            for m in order:
                if m in agent_data:
                    try:
                        vals.append(float(agent_data[m][t['field']]))
                    except (ValueError, KeyError):
                        vals.append(None)
            if any(v is None for v in vals):
                trend_score = 0.0
            else:
                inc = all(vals[i] < vals[i+1] + 0.005 for i in range(len(vals)-1)) # allow slight noise
                trend_score = 1.0 if inc else 0.0
        tw = t.get('score_weight', 0.15)
        return row_avg * (1 - tw) + trend_score * tw
    else:
        return row_avg


# === block: score_1 (check id='co_adsorption') ===
def score_1(artifact, step, ctx):
    import csv, os, math
    rows = list(csv.DictReader(open(os.path.join('/app/outputs', step['output_file']))))
    if not rows:
        return 0.0
    gold = step['params']['gold_table']
    tols = step['params']['tolerances']
    fw = step['params']['field_weights']
    # key = (Model normalized, Site normalized)
    agent_data = {}
    for r in rows:
        k = (r['Model'].strip().lower(), r['Site'].strip().upper())
        agent_data[k] = r
    row_scores = []
    for gr in gold:
        gk = (gr['Model'].strip().lower(), gr['Site'].strip().upper())
        if gk not in agent_data:
            continue
        ar = agent_data[gk]
        f_scores = []
        for f, w in fw.items():
            if f not in ar or f not in gr:
                continue
            gv = gr[f]
            av = ar[f].strip()
            if av == '' and gv == '':
                f_scores.append((w, 1.0))
                continue
            try:
                gn = float(gv)
                an = float(av)
                tol = tols.get(f, 0.1)
                f_scores.append((w, 1.0 if math.isclose(an, gn, rel_tol=0, abs_tol=tol) else 0.0))
            except (ValueError, TypeError):
                f_scores.append((w, 0.0))
        if f_scores:
            row_score = sum(w * s for w, s in f_scores) / sum(w for w, s in f_scores)
            row_scores.append(row_score)
    row_avg = sum(row_scores) / len(row_scores) if row_scores else 0.0
    trends = step['params'].get('trends', [])
    trend_score = 0.0
    if trends:
        t = trends[0]
        # pairwise superior: for each model with both Pt and Cu, check Pt>Cu
        models = set()
        for k in agent_data:
            models.add(k[0])
        valid = 0
        correct = 0
        for m in models:
            pt_key = (m, 'PT')
            cu_key = (m, 'CU')
            if pt_key in agent_data and cu_key in agent_data:
                try:
                    pt_val = float(agent_data[pt_key][t['field']])
                    cu_val = float(agent_data[cu_key][t['field']])
                    if pt_val > cu_val + 0.005:
                        correct += 1
                    valid += 1
                except (ValueError, KeyError):
                    pass
        if valid > 0:
            trend_score = correct / valid
        else:
            trend_score = 0.0
        tw = t.get('score_weight', 0.15)
        return row_avg * (1 - tw) + trend_score * tw
    return row_avg


# === block: score_2 (check id='co_o2_reaction') ===
def score_2(artifact, step, ctx):
    import csv, os, math
    rows = list(csv.DictReader(open(os.path.join('/app/outputs', step['output_file']))))
    if not rows:
        return 0.0
    gold = step['params']['gold_table']
    tols = step['params']['tolerances']
    fw = step['params']['field_weights']
    key = 'Model'
    agent_data = {}
    for r in rows:
        m = r[key].strip().lower()
        agent_data[m] = r
    row_scores = []
    for gr in gold:
        gm = gr[key].strip().lower()
        if gm not in agent_data:
            continue
        ar = agent_data[gm]
        f_scores = []
        for f, w in fw.items():
            if f not in ar:
                continue
            gv = gr[f]
            av = ar[f].strip()
            if av == '' and gv == '':
                f_scores.append((w, 1.0))
                continue
            try:
                gn = float(gv)
                an = float(av)
                tol = tols.get(f, 0.1)
                f_scores.append((w, 1.0 if math.isclose(an, gn, rel_tol=0, abs_tol=tol) else 0.0))
            except (ValueError, TypeError):
                f_scores.append((w, 0.0))
        if f_scores:
            row_score = sum(w * s for w, s in f_scores) / sum(w for w, s in f_scores)
            row_scores.append(row_score)
    row_avg = sum(row_scores) / len(row_scores) if row_scores else 0.0
    trends = step['params'].get('trends', [])
    trend_score = 0.0
    if trends:
        t = trends[0]
        target_model = t['min_model'].strip().lower()
        field = t['field']
        vals = {}
        for k, r in agent_data.items():
            try:
                vals[k] = float(r[field])
            except (ValueError, KeyError):
                pass
        if vals:
            min_model = min(vals, key=vals.get)
            trend_score = 1.0 if min_model == target_model else 0.0
        tw = t.get('score_weight', 0.15)
        return row_avg * (1 - tw) + trend_score * tw
    return row_avg


_SCORERS = {
    'o2_dissociation': score_0,
    'co_adsorption': score_1,
    'co_o2_reaction': score_2,
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
