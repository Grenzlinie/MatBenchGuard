import os
import json
import csv

# === author imports / helpers ===
import csv
import json
from collections import Counter

def cond_key(r):
    size = int(round(float(r['size_nm'])))
    vac = int(round(float(r['vacancy_fraction']) * 100))
    return f"D{size}nm_vac{vac}"

def recompute_heating_aggregates(rows):
    conds = {}
    for r in rows:
        ck = cond_key(r)
        conds.setdefault(ck, []).append(r)
    out = {}
    for ck, rlist in conds.items():
        total = len(rlist)
        hcount = Counter(r['heating_structure'] for r in rlist)
        percents = {}
        for s in ['Dh','Ih','FCC','twinned_FCC','complex']:
            percents[s] = (hcount.get(s, 0) / total) * 100.0
        intervals = {}
        for r in rlist:
            h = r['heating_structure']
            intervals.setdefault(h, []).append((float(r['T_min_K']), float(r['T_max_K'])))
        dom = {}
        for h, tlist in intervals.items():
            mcc = Counter(tlist).most_common(1)[0][0]
            dom[h] = {'T_min_K': mcc[0], 'T_max_K': mcc[1]}
        out[ck] = {'heating_percents': percents, 'dominant_intervals': dom}
    return out

def recompute_relaxation_aggregates(rows):
    conds = {}
    for r in rows:
        ck = cond_key(r)
        conds.setdefault(ck, []).append(r)
    out = {}
    for ck, rlist in conds.items():
        total = len(rlist)
        rcount = Counter(r['relaxation_structure'] for r in rlist)
        out[ck] = {
            'FCC_percent': (rcount.get('FCC', 0) / total) * 100.0,
            'amorphous_percent': (rcount.get('amorphous', 0) / total) * 100.0
        }
    return out


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
    csv_path = os.path.join(outputs_dir, 'per_simulation_classification.csv')
    if not os.path.exists(csv_path):
        return {'csv_rows': []}
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        csv_rows = [row for row in reader]
    return {'csv_rows': csv_rows}


# === block: score_0 (check id='heating_gold') ===
def score_0(artifact, step, ctx):
    gold = step.get('gold', {})
    tol_pct = step.get('tolerance_percent', 10.0)
    tol_temp = step.get('tolerance_temp_K', 20.0)
    csv_rows = ctx['csv_rows']
    if not csv_rows:
        return 0.0
    agg = recompute_heating_aggregates(csv_rows)
    cond_scores = []
    for ckey, gv in gold.items():
        if ckey not in agg:
            cond_scores.append(0.0)
            continue
        a = agg[ckey]
        # percentage scores
        pct_sum = 0.0
        n_pct = 0
        for stype in ['Dh','Ih','FCC','twinned_FCC','complex']:
            if stype in gv.get('heating_percents', {}):
                expected = gv['heating_percents'][stype]
                observed = a['heating_percents'].get(stype, 0.0)
                diff = abs(observed - expected)
                if diff <= tol_pct:
                    pct_sum += 1.0
                elif diff <= 2 * tol_pct:
                    pct_sum += 0.5
                else:
                    pct_sum += 0.0
                n_pct += 1
        pct_score = pct_sum / max(n_pct, 1)
        # interval scores
        int_sum = 0.0
        n_int = 0
        for stype, gint in gv.get('intervals', {}).items():
            if stype in a['dominant_intervals']:
                dint = a['dominant_intervals'][stype]
                ok = (abs(dint['T_min_K'] - gint['T_min_K']) <= tol_temp and
                      abs(dint['T_max_K'] - gint['T_max_K']) <= tol_temp)
                int_sum += 1.0 if ok else 0.0
            else:
                int_sum += 0.0
            n_int += 1
        int_score = int_sum / max(n_int, 1) if n_int > 0 else 1.0
        cond_scores.append(0.5 * pct_score + 0.5 * int_score)
    return sum(cond_scores) / max(len(cond_scores), 1)


# === block: score_1 (check id='relaxation_gold') ===
def score_1(artifact, step, ctx):
    gold = step.get('gold', {})
    tol = step.get('tolerance_percent', 10.0)
    csv_rows = ctx['csv_rows']
    if not csv_rows:
        return 0.0
    agg = recompute_relaxation_aggregates(csv_rows)
    scores = []
    for ckey, gv in gold.items():
        if ckey not in agg:
            scores.append(0.0)
            continue
        a = agg[ckey]
        fcc_ok = abs(a['FCC_percent'] - gv['FCC']) <= tol
        am_ok = abs(a['amorphous_percent'] - gv['amorphous']) <= tol
        scores.append((fcc_ok + am_ok) / 2.0)
    return sum(scores) / max(len(scores), 1)


# === block: score_2 (check id='json_consistency') ===
def score_2(artifact, step, ctx):
    csv_rows = ctx['csv_rows']
    json_data = artifact
    if not isinstance(json_data, dict):
        return 0.0
    heat_agg = recompute_heating_aggregates(csv_rows) if csv_rows else {}
    relax_agg = recompute_relaxation_aggregates(csv_rows) if csv_rows else {}
    total_fields = 0
    match_fields = 0
    for ckey, jv in json_data.items():
        # relaxation stage
        if ckey in relax_agg:
            r_agg = relax_agg[ckey]
            r_json = jv.get('relaxation_stage', {})
            for key in ('FCC_percent', 'amorphous_percent'):
                total_fields += 1
                if abs(r_json.get(key, -999.0) - r_agg[key]) <= step.get('tolerance_float', 0.01):
                    match_fields += 1
        # heating stage percentages
        if ckey in heat_agg:
            h_agg_percents = heat_agg[ckey]['heating_percents']
            h_json_percents = jv.get('heating_stage', {})
            for stype in ('Dh','Ih','FCC','twinned_FCC','complex'):
                key = stype + '_percent'
                if key in h_json_percents:
                    total_fields += 1
                    if abs(h_json_percents[key] - h_agg_percents[stype]) <= step.get('tolerance_float', 0.01):
                        match_fields += 1
            # temperature intervals
            h_agg_ints = heat_agg[ckey]['dominant_intervals']
            j_ints = jv.get('temperature_intervals', {})
            for stype in h_agg_ints:
                if stype in j_ints:
                    total_fields += 2
                    jmin = j_ints[stype].get('T_min_K', -999.0)
                    jmax = j_ints[stype].get('T_max_K', -999.0)
                    if (abs(jmin - h_agg_ints[stype]['T_min_K']) <= 1.0 and
                        abs(jmax - h_agg_ints[stype]['T_max_K']) <= 1.0):
                        match_fields += 2
    if total_fields == 0:
        return 1.0
    return match_fields / total_fields


_SCORERS = {
    'heating_gold': score_0,
    'relaxation_gold': score_1,
    'json_consistency': score_2,
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
