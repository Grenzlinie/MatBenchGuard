import os
import json
import csv

# === author imports / helpers ===
import csv, json, math, os


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


# === block: score_0 (check id='geometric_check') ===
def score_0(artifact, step, ctx):
    # Build gold ranges (Table 2) with ±20% tolerance
    hc_min_max = {
        'Di': (7.15, 25.49),
        'Df': (3.19, 25.49),
        'vol_ASA': (1250.10, 2931.06),
        'grav_ASA': (2110.63, 5945.28)
    }
    ha_min_max = {
        'Di': (6.13, 31.31),
        'Df': (2.53, 20.76),
        'vol_ASA': (916.81, 2652.59),
        'grav_ASA': (1469.58, 6871.72)
    }
    required_hc = set(['Hc16', 'Hc2075', 'Hc1821', 'Hc145', 'Hc2558', 'Hc2368', 'Hc646'])
    required_ha = set(['Ha469', 'Ha64', 'Ha1426', 'Ha712', 'Ha779', 'Ha1589', 'Ha1239'])

    def _col(rows, col):
        return [float(row[col]) for row in rows]

    rows = artifact  # artifact is list of dicts from csv
    if not rows:
        return 0.0

    # Build id->row dict
    id2row = {}
    for row in rows:
        sid = row['structure_id']
        id2row[sid] = row

    # Check Di >= Df
    violations = 0
    for row in rows:
        di = float(row['Di_angstrom'])
        df = float(row['Df_angstrom'])
        if di < df:
            violations += 1
    total = len(rows)
    di_df_score = (total - violations) / total if total > 0 else 0.0

    # Check range
    range_violations = 0
    for row in rows:
        sid = row['structure_id']
        if sid.startswith('Hc'):
            mm = hc_min_max
        else:
            mm = ha_min_max
        di = float(row['Di_angstrom'])
        df = float(row['Df_angstrom'])
        vol = float(row['volumetric_ASA_m2_per_cm3'])
        grav = float(row['gravimetric_ASA_m2_per_g'])
        # extended bounds: min*0.8, max*1.2
        ok1 = (di >= mm['Di'][0]*0.8) and (di <= mm['Di'][1]*1.2)
        ok2 = (df >= mm['Df'][0]*0.8) and (df <= mm['Df'][1]*1.2)
        ok3 = (vol >= mm['vol_ASA'][0]*0.8) and (vol <= mm['vol_ASA'][1]*1.2)
        ok4 = (grav >= mm['grav_ASA'][0]*0.8) and (grav <= mm['grav_ASA'][1]*1.2)
        if not (ok1 and ok2 and ok3 and ok4):
            range_violations += 1
    range_score = (total - range_violations) / total if total > 0 else 0.0

    # Key structure presence
    known_hc_found = sum(1 for sid in required_hc if sid in id2row)
    known_ha_found = sum(1 for sid in required_ha if sid in id2row)
    presence_score = (known_hc_found + known_ha_found) / (len(required_hc) + len(required_ha))

    # Row count: expect ~111
    row_count_score = 1.0 if total >= 100 else 0.0  # generous

    # Weighted sum: main checks
    score = 0.3 * di_df_score + 0.3 * range_score + 0.3 * presence_score + 0.1 * row_count_score
    return min(max(score, 0.0), 1.0)


# === block: score_1 (check id='methane_check') ===
def score_1(artifact, step, ctx):
    # Paper gold for top three volumetric (V_STP/V) and gravimetric (mol/kg)
    # Paper Table 3; overall top-3 by value.
    vol_gold = {
        'Hc2075': 178.87,
        'Hc1821': 163.78,
        'Hc145': 162.05
    }
    grav_gold = {
        'Ha779': 18.83,
        'Ha1589': 17.63,
        'Hc2558': 16.14
    }

    rel_tol = 0.10  # 10% tolerance

    def _num(val):
        return float(val)

    rows = artifact  # list of dicts
    if not rows:
        return 0.0

    vol_key = 'volumetric_uptake_V_STP_per_V'
    grav_key = 'gravimetric_uptake_mol_per_kg'

    # Sort by volumetric desc
    vol_sorted = sorted(rows, key=lambda r: _num(r[vol_key]), reverse=True)
    top3_vol = [r['structure_id'] for r in vol_sorted[:3]]
    top3_vol_vals = {r['structure_id']: _num(r[vol_key]) for r in vol_sorted[:3]}

    # Sort by gravimetric desc
    grav_sorted = sorted(rows, key=lambda r: _num(r[grav_key]), reverse=True)
    top3_grav = [r['structure_id'] for r in grav_sorted[:3]]
    top3_grav_vals = {r['structure_id']: _num(r[grav_key]) for r in grav_sorted[:3]}

    # Evaluate volumetric
    vol_score = 0.0
    exp_vol_set = set(vol_gold.keys())
    if set(top3_vol) == exp_vol_set:
        # exact ID match; check values >= gold * (1 - rel_tol)
        all_ok = True
        for sid in vol_gold:
            if top3_vol_vals.get(sid, 0) < vol_gold[sid] * (1 - rel_tol):
                all_ok = False
                break
        vol_score = 1.0 if all_ok else 0.5
    else:
        # partial: count how many of the expected appear in top3
        common = exp_vol_set.intersection(set(top3_vol))
        vol_score = len(common) / len(exp_vol_set) * 0.5  # half credit if IDs only, up to 0.5
        # boost if values still meet threshold
        for sid in common:
            if top3_vol_vals.get(sid, 0) >= vol_gold[sid] * (1 - rel_tol):
                vol_score += 0.1  # small per correct value, cap at 0.5+0.3=0.8
        vol_score = min(vol_score, 1.0)

    # Evaluate gravimetric similarly
    grav_score = 0.0
    exp_grav_set = set(grav_gold.keys())
    if set(top3_grav) == exp_grav_set:
        all_ok = True
        for sid in grav_gold:
            if top3_grav_vals.get(sid, 0) < grav_gold[sid] * (1 - rel_tol):
                all_ok = False
                break
        grav_score = 1.0 if all_ok else 0.5
    else:
        common = exp_grav_set.intersection(set(top3_grav))
        grav_score = len(common) / len(exp_grav_set) * 0.5
        for sid in common:
            if top3_grav_vals.get(sid, 0) >= grav_gold[sid] * (1 - rel_tol):
                grav_score += 0.1
        grav_score = min(grav_score, 1.0)

    # Combine scores (equal weight)
    score = 0.5 * vol_score + 0.5 * grav_score
    return min(max(score, 0.0), 1.0)


_SCORERS = {
    'geometric_check': score_0,
    'methane_check': score_1,
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
