import os
import json
import csv

# === author imports / helpers ===
import numpy as np
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
    return {}


# === block: score_0 (check id='cluster_distributions') ===
def score_0(artifact, step, ctx):
    def compute_mean_size(distributions):
        total_count = sum(d['count'] for d in distributions)
        if total_count == 0:
            return 0.0
        total_spins = sum(d['cluster_order'] * d['count'] for d in distributions)
        return total_spins / total_count

    def get_mean(data, key, subkey, value):
        if key not in data:
            return None
        for entry in data[key]:
            if entry[subkey] == value:
                return compute_mean_size(entry['distribution'])
        return None

    scores = []
    checks = step.get('checks', [])
    for check in checks:
        w = check.get('weight', 1.0)
        name = check.get('name', '')
        try:
            if name == 'demag_ac_dc_smaller':
                means_less = []
                for t in check['types_less']:
                    m = get_mean(artifact, 'demag_types', 'demag_type', t)
                    if m is not None: means_less.append(m)
                means_greater = []
                for t in check['types_greater']:
                    m = get_mean(artifact, 'demag_types', 'demag_type', t)
                    if m is not None: means_greater.append(m)
                if len(means_less) > 0 and len(means_greater) > 0 and (sum(means_less)/len(means_less)) < (sum(means_greater)/len(means_greater)):
                    scores.append(w)
                else:
                    scores.append(0.0)
            elif name == 'interaction_monotonic':
                d_vals = check['d_values']
                means = []
                for d in d_vals:
                    m = get_mean(artifact, 'interaction_strengths', 'd', d)
                    if m is not None: means.append(m)
                    else: break
                if len(means) < 2:
                    scores.append(0.0)
                else:
                    inc = sum(1 for i in range(1,len(means)) if means[i] >= means[i-1] - 1e-9)
                    scores.append(w * inc / (len(means)-1))
            elif name == 'frequency_decreasing':
                freqs = check['frequencies']
                means = []
                for f in freqs:
                    m = get_mean(artifact, 'frequencies', 'frequency', f)
                    if m is not None: means.append(m)
                    else: break
                if len(means) < 2:
                    scores.append(0.0)
                else:
                    dec = sum(1 for i in range(1,len(means)) if means[i] <= means[i-1] + 1e-9)
                    scores.append(w * dec / (len(means)-1))
            elif name == 'virgin_curve_increasing':
                fields = check['field_values']
                means = []
                for f in fields:
                    m = get_mean(artifact, 'virgin_curve_fields', 'applied_field_h', f)
                    if m is not None: means.append(m)
                    else: break
                if len(means) < 2:
                    scores.append(0.0)
                else:
                    inc = sum(1 for i in range(1,len(means)) if means[i] >= means[i-1] - 1e-9)
                    scores.append(w * inc / (len(means)-1))
            else:
                scores.append(0.0)
        except:
            scores.append(0.0)
    return sum(scores) if scores else 0.0


# === block: score_1 (check id='magnetization_curves') ===
def score_1(artifact, step, ctx):
    from collections import defaultdict
    scores = []
    checks = step.get('checks', [])
    for check in checks:
        w = check.get('weight', 1.0)
        name = check.get('name', '')
        try:
            if name == 'initial_susceptibility_ordering':
                demag_curves = artifact.get('first_magnetization_curve_demag', [])
                if not demag_curves:
                    scores.append(0.0)
                    continue
                by_type = defaultdict(list)
                for entry in demag_curves:
                    by_type[entry['demag_type']].append((entry['field_h'], entry['magnetization']))
                low_min = check.get('field_h_range', [0.05, 0.15])[0]
                low_max = check['field_h_range'][1]
                mags = {}
                for dtype, points in by_type.items():
                    vals = [m for h, m in points if low_min <= h <= low_max]
                    if vals:
                        mags[dtype] = sum(vals) / len(vals)
                required = ['natural','thermal','AC','DC']
                if not all(k in mags for k in required):
                    scores.append(0.0)
                    continue
                satisfied = 0
                if mags['natural'] > mags['thermal']: satisfied += 1
                if mags['natural'] > mags['AC']: satisfied += 1
                if mags['natural'] > mags['DC']: satisfied += 1
                if mags['thermal'] > mags['AC']: satisfied += 1
                if mags['thermal'] > mags['DC']: satisfied += 1
                scores.append(w * satisfied / 5)
            elif name == 'curve_monotonicity':
                demag_curves = artifact.get('first_magnetization_curve_demag', [])
                interaction_curves = artifact.get('first_magnetization_curve_interaction', [])
                if not demag_curves and not interaction_curves:
                    scores.append(0.0)
                    continue
                all_series = []
                by_type = defaultdict(list)
                for entry in demag_curves:
                    by_type[entry['demag_type']].append((entry['field_h'], entry['magnetization']))
                for points in by_type.values():
                    points.sort(key=lambda x: x[0])
                    all_series.append(points)
                by_d = defaultdict(list)
                for entry in interaction_curves:
                    by_d[entry['d']].append((entry['field_h'], entry['magnetization']))
                for points in by_d.values():
                    points.sort(key=lambda x: x[0])
                    all_series.append(points)
                total_series = len(all_series)
                if total_series == 0:
                    scores.append(0.0)
                    continue
                monotonic = 0
                for series in all_series:
                    ok = True
                    for i in range(1, len(series)):
                        if series[i][1] < series[i-1][1] - 1e-9:
                            ok = False
                            break
                    if ok:
                        monotonic += 1
                scores.append(w * monotonic / total_series)
            else:
                scores.append(0.0)
        except:
            scores.append(0.0)
    return sum(scores) if scores else 0.0


_SCORERS = {
    'cluster_distributions': score_0,
    'magnetization_curves': score_1,
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
