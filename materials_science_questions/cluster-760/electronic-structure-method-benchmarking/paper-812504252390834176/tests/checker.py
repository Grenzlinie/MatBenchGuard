import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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
    ctx = {}
    ctx['experimental_cp'] = spec['steps'][0].get('experimental_cp', 381.6)
    ctx['cp_threshold'] = spec['steps'][0].get('threshold', 4.0)
    ctx['cp_temperature'] = spec['steps'][0].get('temperature', 298.15)
    step2 = spec['steps'][1]
    ctx['gold_percentages'] = step2.get('gold_percentages', {})
    ctx['tolerance_percent'] = step2.get('tolerance_percent', 2.0)
    ctx['ordering'] = step2.get('ordering', [])
    ctx['compensation'] = step2.get('compensation', {})
    return ctx


# === block: score_0 (check id='cp_validation_check') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    row = None
    for r in rows:
        if abs(float(r.get('Temperature_K', 0)) - ctx['cp_temperature']) < 0.01:
            row = r
            break
    if row is None:
        return 0.0
    try:
        cp_exp = float(row['Cp_experimental_JmolK'])
        re = float(row['RelativeError_percent'])
    except (KeyError, ValueError, TypeError):
        return 0.0
    if abs(cp_exp - ctx['experimental_cp']) > 1e-6:
        return 0.0
    if re <= ctx['cp_threshold'] + 1e-9:
        return 1.0
    return 0.0


# === block: score_1 (check id='enthalpy_analysis_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    blend_data = {}
    for r in rows:
        name = r.get('Blend', '').strip()
        try:
            blend_data[name] = {
                'dh': float(r['Delta_H_kJ_per_mol']),
                'pct': float(r['Delta_H_percent_vs_n_butanol'])
            }
        except (KeyError, ValueError):
            return 0.0

    # Check existence of component_enthalpy.csv (process evidence)
    comp_path = os.path.join('/app/outputs', 'component_enthalpy.csv')
    comp_exists = os.path.exists(comp_path)
    comp_valid = False
    if comp_exists:
        try:
            with open(comp_path, newline='') as f:
                comp_rows = list(csv.DictReader(f))
            if comp_rows and 'component' in comp_rows[0] and 'H298_kJmol' in comp_rows[0] and 'H600_kJmol' in comp_rows[0]:
                comp_valid = True
        except Exception:
            comp_valid = False

    gold = ctx['gold_percentages']
    tolerance = ctx['tolerance_percent']
    required_blends = ctx.get('required_blends', ['n-butanol', 'G100', 'G10E', 'G20E', 'G10E_plus_60pct_nbutanol', 'G100_plus_40pct_nbutanol'])
    for b in required_blends:
        if b not in blend_data:
            return 0.0

    # sub-scores (internal sum=1.0)
    score = 0.0
    # 0.1 - component_enthalpy exists and valid
    score += 0.1 if comp_valid else 0.0
    # 0.1 - n-butanol percentage is 0
    pct_nb = blend_data['n-butanol']['pct']
    if abs(pct_nb) <= 0.1:
        score += 0.1
    # 0.5 - gold percentages match within tolerance
    match_count = 0
    for blend_name in ['G100', 'G10E', 'G20E']:
        if blend_name in gold:
            diff = abs(blend_data[blend_name]['pct'] - gold[blend_name])
            if diff <= tolerance:
                match_count += 1
    score += 0.5 * (match_count / 3.0)
    # 0.1 - ordering
    ordering = ctx['ordering']
    if len(ordering) >= 2:
        dh_vals = [blend_data[b]['dh'] for b in ordering]
        if all(dh_vals[i] > dh_vals[i+1] for i in range(len(dh_vals)-1)):
            score += 0.1
    # 0.2 - compensation
    comp = ctx['compensation']
    comp_ok = 0
    for key, spec_comp in comp.items():
        if key in blend_data and spec_comp['target_blend'] in blend_data:
            diff = abs(blend_data[key]['pct'] - blend_data[spec_comp['target_blend']]['pct'])
            if diff <= spec_comp['max_diff_percent']:
                comp_ok += 1
    if comp_ok == len(comp):
        score += 0.2
    elif comp_ok > 0:
        score += 0.2 * (comp_ok / float(len(comp)))

    return min(1.0, max(0.0, score))


_SCORERS = {
    'cp_validation_check': score_0,
    'enthalpy_analysis_check': score_1,
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
