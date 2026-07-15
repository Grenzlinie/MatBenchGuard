import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math

def load_artifact(path):
    if not os.path.exists(path): return None
    if path.endswith('.json'):
        with open(path) as f: return json.load(f)
    if path.endswith('.csv'):
        with open(path, newline='') as f:
            return list(csv.DictReader(f))
    return None

def rel_error(val, ref):
    if abs(ref) < 1e-12: ref = 1e-12
    return abs(val - ref) / abs(ref)


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
    out = outputs_dir
    ctx = {}
    ctx['dep_csv'] = load_artifact(os.path.join(out, 'ti_cl_output_deposition.csv'))
    ctx['etch_csv'] = load_artifact(os.path.join(out, 'ti_cl_output_etching.csv'))
    ctx['species_json'] = load_artifact(os.path.join(out, 'species_pressures_deposition.json'))
    # extract reference points from grading spec steps
    steps = spec.get('steps', [])
    for s in steps:
        if s['id'] == 'dep_check':
            ctx['dep_ref'] = s.get('reference_points', [])
        elif s['id'] == 'etch_check':
            ctx['etch_ref'] = s.get('reference_points', [])
        elif s['id'] == 'species_check':
            ctx['species_ref'] = s.get('reference_points', [])
    return ctx


# === block: score_0 (check id='dep_check') ===
def score_0(artifact, step, ctx):
    csv_data = ctx.get('dep_csv')
    ref_points = ctx.get('dep_ref', [])
    if not csv_data or not ref_points:
        return 0.0
    tol = float(step.get('tolerance_rel', 0.10))
    total = len(ref_points)
    if total == 0:
        return 0.0
    # Normalize column names to be robust against minor spelling/case differences
    header = csv_data[0].keys() if csv_data else []
    col_map = {}
    preferred = {
        'total_pressure_Torr': ['total_pressure_torr', 'total_pressure', 'pressure_torr'],
        'TiCl4_NH3_ratio': ['ticl4_nh3_ratio', 'ticl4_nh3', 'ticl4/nh3'],
        'temperature_K': ['temperature_k', 'temperature'],
        'Ti_Cl_output': ['ti_cl_output', 'ti/cl_output'],
    }
    for key, aliases_list in preferred.items():
        for h in header:
            norm_h = h.strip().lower()
            if norm_h == key.strip().lower() or norm_h in [a.strip().lower() for a in aliases_list]:
                col_map[key] = h
                break
    if not all(k in col_map for k in preferred):
        return 0.0
    passed = 0
    for ref in ref_points:
        try:
            p = float(ref['total_pressure_Torr'])
            r = float(ref['TiCl4_NH3_ratio'])
            t = float(ref['temperature_K'])
            gold = float(ref['Ti_Cl_output_gold'])
        except (KeyError, ValueError):
            continue
        found = False
        val = None
        for row in csv_data:
            try:
                rp = float(row[col_map['total_pressure_Torr']])
                rr = float(row[col_map['TiCl4_NH3_ratio']])
                rt = float(row[col_map['temperature_K']])
                rv = float(row[col_map['Ti_Cl_output']])
                if (abs(rp - p) < 1e-6 and abs(rr - r) < 1e-6 and abs(rt - t) < 1e-6):
                    val = rv
                    found = True
                    break
            except (KeyError, ValueError):
                continue
        if not found:
            continue
        if rel_error(val, gold) <= tol:
            passed += 1
    return passed / total


# === block: score_1 (check id='etch_check') ===
def score_1(artifact, step, ctx):
    csv_data = ctx.get('etch_csv')
    ref_points = ctx.get('etch_ref', [])
    if not csv_data or not ref_points:
        return 0.0
    tol = float(step.get('tolerance_rel', 0.10))
    total = len(ref_points)
    if total == 0:
        return 0.0
    passed = 0
    for ref in ref_points:
        try:
            p = float(ref['total_pressure_Torr'])
            t = float(ref['temperature_K'])
            gold = float(ref['Ti_Cl_output_gold'])
        except (KeyError, ValueError):
            continue
        found = False
        val = None
        for row in csv_data:
            try:
                if (abs(float(row['total_pressure_Torr']) - p) < 1e-6 and
                    abs(float(row['temperature_K']) - t) < 1e-6):
                    val = float(row['Ti_Cl_output'])
                    found = True
                    break
            except (KeyError, ValueError):
                continue
        if not found:
            continue
        if rel_error(val, gold) <= tol:
            passed += 1
    return passed / total


# === block: score_2 (check id='species_check') ===
def score_2(artifact, step, ctx):
    species = ctx.get('species_json')
    dep_csv = ctx.get('dep_csv')
    ref_points = ctx.get('species_ref', [])
    if not species or not dep_csv or not ref_points:
        return 0.0
    points = species.get('points', [])
    if not points:
        return 0.0
    tol_gold = float(step.get('tolerance_gold', 0.05))
    tol_csv = float(step.get('tolerance_csv', 0.05))
    target_temps = [800.0, 1000.0, 1200.0]
    score = 0.0
    count = 0
    for temp in target_temps:
        pt = None
        for p in points:
            try:
                if abs(float(p['temperature_K']) - temp) < 1e-6:
                    pt = p
                    break
            except (KeyError, ValueError):
                continue
        if pt is None:
            continue
        try:
            sp = pt.get('species', pt)
            p_TiCl4 = float(sp.get('TiCl4', 0))
            p_TiCl3 = float(sp.get('TiCl3', 0))
            p_TiCl2 = float(sp.get('TiCl2', 0))
            p_TiCl  = float(sp.get('TiCl', 0))
            p_HCl   = float(sp.get('HCl', 0))
            p_Cl2   = float(sp.get('Cl2', 0))
            p_Cl    = float(sp.get('Cl', 0))
            num = p_TiCl4 + p_TiCl3 + p_TiCl2 + p_TiCl
            den = 4*p_TiCl4 + 3*p_TiCl3 + 2*p_TiCl2 + p_TiCl + p_HCl + 2*p_Cl2 + p_Cl
            if den == 0:
                continue
            recomputed = num / den
        except Exception:
            continue
        # compare to hidden gold
        gold_val = None
        for ref in ref_points:
            try:
                if abs(float(ref['temperature_K']) - temp) < 1e-6:
                    gold_val = float(ref['Ti_Cl_output_gold'])
                    break
            except (KeyError, ValueError):
                continue
        if gold_val is None:
            continue
        # compare to agent's own deposition CSV for condition (0.5,0.5) at same temp
        csv_val = None
        for row in dep_csv:
            try:
                if (abs(float(row['total_pressure_Torr']) - 0.5) < 1e-6 and
                    abs(float(row['TiCl4_NH3_ratio']) - 0.5) < 1e-6 and
                    abs(float(row['temperature_K']) - temp) < 1e-6):
                    csv_val = float(row['Ti_Cl_output'])
                    break
            except (KeyError, ValueError):
                continue
        passed_gold = rel_error(recomputed, gold_val) <= tol_gold
        passed_csv = False
        if csv_val is not None:
            passed_csv = rel_error(recomputed, csv_val) <= tol_csv
        else:
            passed_csv = False
        if passed_gold and passed_csv:
            score += 1.0
        count += 1
    return score / max(count, 1)


_SCORERS = {
    'dep_check': score_0,
    'etch_check': score_1,
    'species_check': score_2,
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
