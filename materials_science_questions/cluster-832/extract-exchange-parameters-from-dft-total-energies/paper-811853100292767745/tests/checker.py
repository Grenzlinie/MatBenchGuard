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
        j_step = None
        mr_step = None
        for step in spec.get('steps', []):
            if step.get('id') == 'step_02_j_values':
                j_step = step
            elif step.get('id') == 'step_04_transport_mr':
                mr_step = step
        return {
            'j_target': j_step.get('target'),
            'j_tolerance_factor': j_step.get('tolerance_factor', 2.0),
            'j_sub_weights': j_step.get('sub_weights'),
            'mr_threshold_ni_max': mr_step.get('threshold_ni_mr_max', 0.10),
            'mr_threshold_mn_min': mr_step.get('threshold_mn_mr_min', 1.0),
            'mr_tolerance_zero': mr_step.get('tolerance_zero_mixed', 1e-4)
        }


# === block: score_0 (check id='step_02_j_values') ===
def score_0(artifact, step, ctx):
        target = ctx['j_target']
        tol_factor = ctx['j_tolerance_factor']
        sub = ctx['j_sub_weights']

        score = 0.0
        # Ni
        ni = artifact.get('Ni', {})
        j_like = ni.get('J_like')
        j_unlike = ni.get('J_unlike')
        ni_like_sign = 1.0 if (j_like is not None and j_like * target['Ni']['J_like'] > 0) else 0.0
        ni_unlike_sign = 1.0 if (j_unlike is not None and j_unlike * target['Ni']['J_unlike'] > 0) else 0.0
        score += sub['Ni_sign'] * (ni_like_sign + ni_unlike_sign) / 2.0
        # Mn
        mn = artifact.get('Mn', {})
        j_like_mn = mn.get('J_like')
        j_unlike_mn = mn.get('J_unlike')
        mn_like_sign = 1.0 if (j_like_mn is not None and j_like_mn * target['Mn']['J_like'] > 0) else 0.0
        mn_unlike_sign = 1.0 if (j_unlike_mn is not None and j_unlike_mn * target['Mn']['J_unlike'] > 0) else 0.0
        score += sub['Mn_sign'] * (mn_like_sign + mn_unlike_sign) / 2.0

        # Magnitude within factor tolerance
        def mag_ok(val, ref):
            if val is None or ref == 0:
                return 0.0
            ratio = abs(val) / abs(ref)
            return 1.0 if (1.0 / tol_factor) <= ratio <= tol_factor else 0.0
        ni_like_mag = mag_ok(j_like, target['Ni']['J_like'])
        ni_unlike_mag = mag_ok(j_unlike, target['Ni']['J_unlike'])
        mn_like_mag = mag_ok(j_like_mn, target['Mn']['J_like'])
        mn_unlike_mag = mag_ok(j_unlike_mn, target['Mn']['J_unlike'])
        score += sub['Ni_magnitude'] * (ni_like_mag + ni_unlike_mag) / 2.0
        score += sub['Mn_magnitude'] * (mn_like_mag + mn_unlike_mag) / 2.0

        return float(min(score, 1.0))


# === block: score_1 (check id='step_04_transport_mr') ===
def score_1(artifact, step, ctx):
        rows = artifact
        ni_mr_max = 0.0
        ni_mixed_has_nonzero = False
        mn_mr_max = 0.0
        mn_mixed_all_zero = True
        for row in rows:
            imp = str(row.get('impurity', '')).strip()
            mr_str = row.get('MR')
            mixed_str = row.get('Gamma_mixed')
            if mr_str is None or mixed_str is None:
                continue
            try:
                mr = float(mr_str)
                mixed = float(mixed_str)
            except (ValueError, TypeError):
                continue
            if imp == 'Ni':
                ni_mr_max = max(ni_mr_max, mr)
                if abs(mixed) > ctx['mr_tolerance_zero']:
                    ni_mixed_has_nonzero = True
            elif imp == 'Mn':
                mn_mr_max = max(mn_mr_max, mr)
                if abs(mixed) > ctx['mr_tolerance_zero']:
                    mn_mixed_all_zero = False

        ni_score = 0.0
        if ni_mr_max <= ctx['mr_threshold_ni_max'] and ni_mixed_has_nonzero:
            ni_score = 1.0
        elif ni_mr_max <= ctx['mr_threshold_ni_max'] and not ni_mixed_has_nonzero:
            ni_score = 0.6
        else:
            ni_score = 0.0

        mn_score = 0.0
        if mn_mixed_all_zero:
            if mn_mr_max >= ctx['mr_threshold_mn_min']:
                mn_score = 1.0
            else:
                mn_score = max(0.0, min(1.0, mn_mr_max / ctx['mr_threshold_mn_min']))
        else:
            mn_score = 0.0

        return 0.5 * ni_score + 0.5 * mn_score


_SCORERS = {
    'step_02_j_values': score_0,
    'step_04_transport_mr': score_1,
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
