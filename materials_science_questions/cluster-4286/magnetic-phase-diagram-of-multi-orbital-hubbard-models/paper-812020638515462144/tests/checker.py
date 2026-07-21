import os
import json
import csv

# === author imports / helpers ===
import json
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
    params_ground = spec['steps'][0]['params']
    params_finite = spec['steps'][1]['params']
    ref_alpha_first = {float(k): v for k, v in params_ground['alpha_first_order_target'].items()}
    ref_alpha_second = {float(k): v for k, v in params_ground['alpha_second_order_target'].items()}
    ref_points = params_finite['reference_points']
    ctx = {
        'required_deltas': params_ground['required_deltas'],
        'abs_tol_ground': params_ground['abs_tolerance'],
        'ref_alpha_first': ref_alpha_first,
        'ref_alpha_second': ref_alpha_second,
        'required_deltas_finite': params_finite['required_deltas'],
        'abs_tol_Tc': params_finite['abs_tolerance_Tc'],
        'abs_tol_alpha': params_finite['abs_tolerance_alpha'],
        'ref_points': {str(d): v for d, v in ref_points.items()},
    }
    return ctx


# === block: score_0 (check id='ground_phase_boundaries') ===
def score_0(artifact, step, ctx):
    import json
    def score(artifact, step, ctx):
        required_deltas = ctx['required_deltas']
        tol = ctx['abs_tol_ground']
        ref_a1 = ctx['ref_alpha_first']
        ref_a2 = ctx['ref_alpha_second']
        data = {}
        if not isinstance(artifact, list):
            return 0.0
        for entry in artifact:
            if isinstance(entry, dict) and 'Delta' in entry:
                d = float(entry['Delta'])
                data[d] = entry
        correct = 0
        total = len(required_deltas) * 2
        vals_a2 = []
        vals_a1 = []
        for d in sorted(required_deltas):
            if d not in data:
                continue
            e = data[d]
            a1 = float(e.get('alpha_first_order', None))
            a2 = float(e.get('alpha_second_order', None))
            if a1 is not None and d in ref_a1 and abs(a1 - ref_a1[d]) <= tol:
                correct += 1
            if a2 is not None and d in ref_a2 and abs(a2 - ref_a2[d]) <= tol:
                correct += 1
            if a2 is not None:
                vals_a2.append((d, a2))
            if a1 is not None:
                vals_a1.append((d, a1))
        pointwise_frac = correct / total if total > 0 else 0.0
        trend_ok = True
        if len(vals_a2) >= 2:
            sorted_a2 = sorted(vals_a2, key=lambda x: x[0])
            for i in range(len(sorted_a2)-1):
                if sorted_a2[i+1][1] < sorted_a2[i][1] - 1e-9:
                    trend_ok = False
                    break
        if len(vals_a1) >= 2 and trend_ok:
            sorted_a1 = sorted(vals_a1, key=lambda x: x[0])
            for i in range(len(sorted_a1)-1):
                if sorted_a1[i+1][1] > sorted_a1[i][1] + 1e-9:
                    trend_ok = False
                    break
        return 0.7 * pointwise_frac + 0.3 * (1.0 if trend_ok else 0.0)


# === block: score_1 (check id='finite_T_critical_lines') ===
def score_1(artifact, step, ctx):
    import json
    def score(artifact, step, ctx):
        tol_Tc = ctx['abs_tol_Tc']
        tol_alpha = ctx['abs_tol_alpha']
        ref_points = ctx['ref_points']
        if not isinstance(artifact, dict):
            return 0.0
        total_ref = sum(len(v) for v in ref_points.values())
        if total_ref == 0:
            return 1.0
        matched = 0
        for delta_str, ref_list in ref_points.items():
            submitted_list = artifact.get(delta_str, artifact.get(float(delta_str), []))
            if not isinstance(submitted_list, list):
                continue
            for ref in ref_list:
                found = False
                for sub in submitted_list:
                    if isinstance(sub, dict) and 'alpha' in sub and 'Tc' in sub and 'type' in sub:
                        if abs(float(sub['alpha']) - ref['alpha']) <= tol_alpha:
                            if abs(float(sub['Tc']) - ref['Tc']) <= tol_Tc and sub['type'] == ref['type']:
                                found = True
                                break
                if found:
                    matched += 1
        return matched / total_ref


_SCORERS = {
    'ground_phase_boundaries': score_0,
    'finite_T_critical_lines': score_1,
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
