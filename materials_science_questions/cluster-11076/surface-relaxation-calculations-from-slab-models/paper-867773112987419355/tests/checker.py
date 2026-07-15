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
    step = spec['steps'][0]
    gold = step['gold_energies']
    energy_tol = step['energy_tolerance']
    sw_thresh = step['surface_weight_threshold']
    tf_thresh = step['topmost_fraction_threshold']
    weights = step['weights']
    return dict(gold_energies=gold, energy_tol=energy_tol, sw_thresh=sw_thresh, tf_thresh=tf_thresh, weights=weights)


# === block: score_0 (check id='surface_states') ===
def score_0(artifact, step, ctx):
    gold_energies = ctx['gold_energies']
    energy_tol = ctx['energy_tol']
    sw_thresh = ctx['sw_thresh']
    tf_thresh = ctx['tf_thresh']
    weights = ctx['weights']

    if not isinstance(artifact, dict):
        return 0.0

    energy_score = 0.0
    count = 0
    for term in ['B', 'Mg', 'Li']:
        term_gold = gold_energies.get(term, {})
        term_data = artifact.get(term, [])
        if not isinstance(term_data, list):
            continue
        rec_by_label = {}
        for rec in term_data:
            if isinstance(rec, dict) and 'label' in rec:
                rec_by_label[rec['label']] = rec
        for label, gold_rec in term_gold.items():
            rec = rec_by_label.get(label)
            if rec is None:
                continue
            for kpoint in ['energy_gamma', 'energy_k', 'energy_m']:
                gold_val = gold_rec.get(kpoint)
                agent_val = rec.get(kpoint)
                if agent_val is None:
                    continue
                error = abs(agent_val - gold_val)
                if error <= energy_tol:
                    point_score = 1.0
                else:
                    point_score = max(0.0, 1.0 - (error - energy_tol) / energy_tol)
                energy_score += point_score
                count += 1
    if count > 0:
        energy_score /= count
    else:
        energy_score = 0.0

    sw_score = 0.0
    if 'B' in artifact:
        for rec in artifact['B']:
            if isinstance(rec, dict) and rec.get('label') == 'sigma1':
                w_g = rec.get('surface_weight_gamma')
                w_k = rec.get('surface_weight_k')
                w_m = rec.get('surface_weight_m')
                if w_g is not None and w_k is not None and w_m is not None:
                    if w_g >= sw_thresh and w_k >= sw_thresh and w_m >= sw_thresh:
                        sw_score = 1.0
                break

    tf_score = 0.0
    if 'B' in artifact:
        needed = {'sigma2': False, 'sigma3': False}
        for rec in artifact['B']:
            if isinstance(rec, dict) and rec.get('label') in ('sigma2', 'sigma3'):
                tf_val = rec.get('topmost_layer_fraction_gamma')
                if tf_val is not None and tf_val >= tf_thresh:
                    needed[rec['label']] = True
        if needed['sigma2'] and needed['sigma3']:
            tf_score = 1.0

    total = weights['energy'] * energy_score + weights['surface_weight'] * sw_score + weights['topmost_fraction'] * tf_score
    return total


_SCORERS = {
    'surface_states': score_0,
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
