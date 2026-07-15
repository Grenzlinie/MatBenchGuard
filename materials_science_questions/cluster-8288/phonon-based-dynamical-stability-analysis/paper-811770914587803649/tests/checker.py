import os
import json
import csv

# === author imports / helpers ===
import json, math


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
    def get_step_config(spec, step_id='step_properties'):
        for s in spec.get('steps', []):
            if s.get('id') == step_id:
                return s
        raise ValueError(f'Missing step {step_id}')

    def prepare(outputs_dir, spec):
        step = get_step_config(spec)
        return {
            'fields': step['fields'],
            'weight_numeric_total': step['weight_numeric_total'],
            'weight_mechanical': step['weight_mechanical'],
            'weight_phonon': step['weight_phonon'],
            'weight_dos': step['weight_dos'],
            'mechanical_checks': step['mechanical_checks'],
            'phonon_threshold': step['phonon_threshold'],
            'dos_threshold': step['dos_threshold']
        }


# === block: score_0 (check id='step_properties') ===
def score_0(artifact, step, ctx):
    data = artifact
    if not isinstance(data, dict):
        return 0.0
    fields = ctx.get('fields', {}) if ctx else {}
    w_num = float(ctx.get('weight_numeric_total', 0.0))
    w_mech = float(ctx.get('weight_mechanical', 0.0))
    w_phonon = float(ctx.get('weight_phonon', 0.0))
    w_dos = float(ctx.get('weight_dos', 0.0))
    n_fields = len(fields)
    if n_fields == 0:
        num_score = 0.0
    else:
        hit = 0.0
        for fname, finfo in fields.items():
            gold = finfo.get('gold')
            tol = finfo.get('tol')
            val = data.get(fname)
            if val is not None and gold is not None and tol is not None:
                try:
                    if abs(float(val) - float(gold)) <= float(tol):
                        hit += 1.0
                except (TypeError, ValueError):
                    pass
        num_score = hit / n_fields
    c11 = data.get('C11')
    c12 = data.get('C12')
    c44 = data.get('C44')
    mech_pass = False
    try:
        if c11 is not None and c44 is not None and c12 is not None:
            if c11 > 0 and c44 > 0 and c11 > abs(c12) and (c11 + 2 * c12) > 0:
                mech_pass = True
    except (TypeError, ValueError):
        pass
    mech_score = 1.0 if mech_pass else 0.0
    phonon_val = data.get('min_phonon_frequency')
    phonon_pass = False
    try:
        phonon_thresh = float(ctx.get('phonon_threshold', -1.0))
        phonon_pass = phonon_val is not None and float(phonon_val) > phonon_thresh
    except (TypeError, ValueError):
        pass
    phonon_score = 1.0 if phonon_pass else 0.0
    dos_val = data.get('DOS_at_Fermi')
    dos_pass = False
    try:
        dos_thresh = float(ctx.get('dos_threshold', 0.0))
        dos_pass = dos_val is not None and float(dos_val) > dos_thresh
    except (TypeError, ValueError):
        pass
    dos_score = 1.0 if dos_pass else 0.0
    total = (w_num * num_score + w_mech * mech_score + w_phonon * phonon_score + w_dos * dos_score)
    return total


_SCORERS = {
    'step_properties': score_0,
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
