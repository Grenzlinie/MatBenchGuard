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
    ctx = {}
    steps = spec.get('steps', [])
    for step in steps:
        if step.get('output_file') == 'optical_properties.csv':
            ctx['optical_gold'] = step.get('gold', [])
        elif step.get('output_file') == 'transport_properties.csv':
            ctx['transport_gold'] = step.get('gold', [])
    return ctx


# === block: score_0 (check id='optical_check') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts from CSV
    if not isinstance(rows, list) or not rows:
        return 0.0
    gold = ctx.get('optical_gold', [])
    tolerances = step.get('tolerances', {})
    total_fields = 0
    correct = 0
    for g in gold:
        mat = g['material']
        pol = g['polarization']
        matched = None
        for r in rows:
            if r.get('material') == mat and r.get('polarization') == pol:
                matched = r
                break
        # absolute-tolerance fields
        abs_fields = [
            ('optical_band_gap_eV', 'optical_band_gap_eV'),
            ('epsilon1_static', 'epsilon1_static'),
            ('sigma_peak1_eV', 'sigma_peak1_eV'),
            ('sigma_peak2_eV', 'sigma_peak2_eV'),
        ]
        rel_fields = [
            ('sigma_peak1_s1', 'sigma_peak1_s1_rel'),
            ('sigma_peak2_s1', 'sigma_peak2_s1_rel'),
        ]
        for field, tol_key in abs_fields:
            total_fields += 1
            if matched is None:
                continue
            val = matched.get(field)
            if val is None:
                continue
            try:
                val = float(val)
            except (ValueError, TypeError):
                continue
            if abs(val - g[field]) <= tolerances.get(tol_key, 0.0):
                correct += 1
        for field, tol_key in rel_fields:
            total_fields += 1
            if matched is None:
                continue
            val = matched.get(field)
            if val is None:
                continue
            try:
                val = float(val)
            except (ValueError, TypeError):
                continue
            expected = g[field]
            if expected == 0:
                correct += 1
            else:
                if abs(val - expected) / abs(expected) <= tolerances.get(tol_key, 0.0):
                    correct += 1
    if total_fields == 0:
        return 0.0
    return correct / total_fields


# === block: score_1 (check id='transport_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not isinstance(rows, list) or not rows:
        return 0.0
    gold = ctx.get('transport_gold', [])
    tolerances = step.get('tolerances', {})
    total_fields = len(gold) * 2
    correct = 0
    vals = {}
    for g in gold:
        mat = g['material']
        matched = None
        for r in rows:
            if r.get('material') == mat:
                matched = r
                break
        if matched is None:
            continue
        for ft in ['sigma_ave_n_type', 'sigma_ave_p_type']:
            val = matched.get(ft)
            if val is None:
                continue
            try:
                val = float(val)
            except (ValueError, TypeError):
                continue
            expected = g[ft]
            tol_key = ft + '_rel'
            if expected == 0:
                correct += 1
            else:
                if abs(val - expected) / abs(expected) <= tolerances.get(tol_key, 0.0):
                    correct += 1
        vals[mat] = (float(matched.get('sigma_ave_n_type', 0)), float(matched.get('sigma_ave_p_type', 0)))
    trend_score = 0
    if 'Nb3O7(OH)' in vals and 'H-Nb2O5' in vals:
        n1, p1 = vals['Nb3O7(OH)']
        n2, p2 = vals['H-Nb2O5']
        if n1 > n2:
            trend_score += 1
        if p1 > p2:
            trend_score += 1
    total = total_fields + 2
    score = (correct + trend_score) / total
    return max(0.0, min(1.0, score))


_SCORERS = {
    'optical_check': score_0,
    'transport_check': score_1,
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
