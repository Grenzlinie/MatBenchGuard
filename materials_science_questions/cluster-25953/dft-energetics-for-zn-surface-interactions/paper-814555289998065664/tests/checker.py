import os
import json
import csv

# === author imports / helpers ===
import csv, json, os


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


# === block: score_0 (check id='check_binding_energies') ===
def score_0(artifact, step, ctx):
    expected_sites = step['hidden']['expected_sites']
    expected_order = step['hidden']['expected_order']
    gold = {s['binding_site']: s for s in expected_sites}
    site_vals = {}
    for row in artifact:
        site = row['binding_site'].strip()
        site_vals[site] = row
    dE_list = []
    dG_list = []
    within_tol = 0
    num_energies = 2 * len(expected_order)
    for site in expected_order:
        if site in site_vals:
            r = site_vals[site]
            try:
                dE = float(r['delta_E'])
                dG = float(r['delta_G_383'])
                dE_list.append((site, dE))
                dG_list.append((site, dG))
                g = gold[site]
                if abs(dE - g['delta_E_gold']) <= g['delta_E_tol']:
                    within_tol += 1
                if abs(dG - g['delta_G_gold']) <= g['delta_G_tol']:
                    within_tol += 1
            except (ValueError, KeyError):
                pass
    if not dE_list:
        abs_frac = 0.0
        ordering_score = 0.0
    else:
        abs_frac = within_tol / num_energies
        sorted_dE = sorted(dE_list, key=lambda x: x[1])
        sorted_dG = sorted(dG_list, key=lambda x: x[1])
        order_ok_dE = [s for s, _ in sorted_dE] == expected_order
        order_ok_dG = [s for s, _ in sorted_dG] == expected_order
        ordering_score = (order_ok_dE + order_ok_dG) / 2.0
    return 0.5 * abs_frac + 0.5 * ordering_score


# === block: score_1 (check id='check_single_zn') ===
def score_1(artifact, step, ctx):
    h = step['hidden']
    coord_num = h['coord_num']
    geom_key = h['geometry_keyword'].lower()
    avg_gold = h['avg_Zn_O_gold']
    avg_tol = h['avg_Zn_O_tol']
    lines = artifact.strip().splitlines()
    parsed = {}
    for line in lines:
        if '=' in line:
            key, val = line.split('=', 1)
            key = key.strip()
            val = val.strip()
            if key in ('coordination_number', 'geometry', 'avg_Zn_O_distance'):
                parsed[key] = val
    score = 0.0
    if 'coordination_number' in parsed:
        try:
            if int(parsed['coordination_number']) == coord_num:
                score += 0.3333
        except ValueError:
            pass
    if 'geometry' in parsed:
        if geom_key in parsed['geometry'].lower():
            score += 0.3333
    if 'avg_Zn_O_distance' in parsed:
        try:
            dist = float(parsed['avg_Zn_O_distance'])
            if abs(dist - avg_gold) <= avg_tol:
                score += 0.3334
        except ValueError:
            pass
    return score


# === block: score_2 (check id='check_four_zn') ===
def score_2(artifact, step, ctx):
    h = step['hidden']
    energies_gold = h['energies_gold']
    tol = h['energies_tol']
    pref_structure = h['preferred_structure']
    min_diff = h['min_diff']
    score = 0.0
    for key, gold_val in energies_gold.items():
        if key in artifact and isinstance(artifact[key], (int, float)):
            if abs(artifact[key] - gold_val) <= tol:
                score += 0.15
    if artifact.get('preferred_structure') == pref_structure:
        score += 0.2
    one = artifact.get('one_per_face_unhydrated')
    two = artifact.get('two_per_face_unhydrated')
    if isinstance(one, (int, float)) and isinstance(two, (int, float)):
        if one < two - min_diff:
            score += 0.2
    return min(score, 1.0)


_SCORERS = {
    'check_binding_energies': score_0,
    'check_single_zn': score_1,
    'check_four_zn': score_2,
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
