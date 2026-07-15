import os
import json
import csv

# === author imports / helpers ===
import csv, json, os
from collections import defaultdict


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
    outputs_dir = "/app/outputs"
    csv_path = os.path.join(outputs_dir, "surface_dband_centers.csv")
    ctx = {}
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            records = [row for row in reader]
    except Exception:
        ctx['csv_loaded'] = False
        return ctx

    mono_groups = defaultdict(list)
    hea_groups = defaultdict(list)
    for r in records:
        el = r['element'].strip()
        try:
            eps = float(r['epsilon_d'])
        except:
            continue
        mt = r['model_type'].strip()
        if mt == 'monometallic':
            mono_groups[el].append(eps)
        elif mt == 'HEA':
            hea_groups[el].append(eps)

    mono_ranges = {}
    for el, vals in mono_groups.items():
        if vals:
            mono_ranges[el] = {'min': min(vals), 'max': max(vals), 'range': max(vals)-min(vals)}
        else:
            mono_ranges[el] = {'min': None, 'max': None, 'range': 0.0}

    hea_ranges = {}
    for el, vals in hea_groups.items():
        if vals:
            hea_ranges[el] = {'min': min(vals), 'max': max(vals), 'range': max(vals)-min(vals)}
        else:
            hea_ranges[el] = {'min': None, 'max': None, 'range': 0.0}

    all_hea = [eps for vals in hea_groups.values() for eps in vals]
    overall_min = min(all_hea) if all_hea else None
    overall_max = max(all_hea) if all_hea else None

    ctx['mono_ranges'] = mono_ranges
    ctx['hea_ranges'] = hea_ranges
    ctx['overall_min'] = overall_min
    ctx['overall_max'] = overall_max
    ctx['csv_loaded'] = True
    return ctx


# === block: score_0 (check id='csv_dband') ===
def score_0(artifact, step, ctx):
    if not ctx.get('csv_loaded'):
        return 0.0

    elements = ['Ru','Rh','Pd','Ag','Os','Ir','Pt','Au']
    mono_ranges = ctx['mono_ranges']
    hea_ranges = ctx['hea_ranges']

    broadening_scores = []
    for el in elements:
        m = mono_ranges.get(el, {})
        h = hea_ranges.get(el, {})
        mono_range = m.get('range') if m.get('range') is not None else 0.0
        hea_range = h.get('range') if h.get('range') is not None else 0.0
        if mono_range > 0 and hea_range > 1.2 * mono_range:
            broadening_scores.append(1.0)
        else:
            broadening_scores.append(0.0)
    avg_broad = sum(broadening_scores) / len(broadening_scores) if broadening_scores else 0.0

    pt_mono = mono_ranges.get('Pt', {})
    pt_hea = hea_ranges.get('Pt', {})
    pt_mono_range = pt_mono.get('range')
    pt_hea_range = pt_hea.get('range')
    if pt_mono_range is None or pt_hea_range is None:
        pt_score = 0.0
    else:
        cond1 = 1.0 if pt_mono_range < 0.5 else 0.0
        cond2 = 1.0 if pt_hea_range > 1.0 else 0.0
        pt_score = 0.5 * cond1 + 0.5 * cond2

    overall_min = ctx.get('overall_min')
    overall_max = ctx.get('overall_max')
    if overall_min is None or overall_max is None:
        span_score = 0.0
    else:
        cond3 = 1.0 if overall_min <= -3.1 else 0.0
        cond4 = 1.0 if overall_max >= -2.3 else 0.0
        span_score = 0.5 * cond3 + 0.5 * cond4

    score = 0.4 * avg_broad + 0.3 * pt_score + 0.3 * span_score
    return max(0.0, min(1.0, score))


# === block: score_1 (check id='json_ranges') ===
def score_1(artifact, step, ctx):
    if not ctx.get('csv_loaded'):
        return 0.0
    if not isinstance(artifact, dict):
        return 0.0
    required = {'monometallic', 'NMHEA', 'overall_NMHEA'}
    if not required.issubset(artifact.keys()):
        return 0.0

    mono_csv = ctx['mono_ranges']
    mono_json = artifact.get('monometallic', {})
    for el in ['Ru','Rh','Pd','Ag','Os','Ir','Pt','Au']:
        csv_range = mono_csv.get(el)
        if csv_range is None:
            continue
        json_range = mono_json.get(el)
        if json_range is None:
            return 0.0
        for key in ['min','max','range']:
            csv_val = csv_range[key]
            json_val = json_range.get(key)
            if json_val is None or abs(csv_val - json_val) > 0.01:
                return 0.0

    hea_csv = ctx['hea_ranges']
    hea_json = artifact.get('NMHEA', {})
    for el in ['Ru','Rh','Pd','Ag','Os','Ir','Pt','Au']:
        csv_range = hea_csv.get(el)
        if csv_range is None:
            continue
        json_range = hea_json.get(el)
        if json_range is None:
            return 0.0
        for key in ['min','max','range']:
            csv_val = csv_range[key]
            json_val = json_range.get(key)
            if json_val is None or abs(csv_val - json_val) > 0.01:
                return 0.0

    overall_json = artifact.get('overall_NMHEA', {})
    if not isinstance(overall_json, dict):
        return 0.0
    csv_min = ctx.get('overall_min')
    csv_max = ctx.get('overall_max')
    if csv_min is None or csv_max is None:
        return 0.0
    if abs(csv_min - overall_json.get('min', None)) > 0.01 or abs(csv_max - overall_json.get('max', None)) > 0.01:
        return 0.0

    return 1.0


_SCORERS = {
    'csv_dband': score_0,
    'json_ranges': score_1,
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
