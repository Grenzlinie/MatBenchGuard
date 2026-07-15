import os
import json
import csv

# === author imports / helpers ===
import json


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
    for s in spec['steps']:
        ctx[s['id']] = s.get('params', {})
    return ctx


# === block: score_0 (check id='gga_plus_u_results') ===
def score_0(artifact, step, ctx):
    params = ctx.get(step['id'], {})
    gold = params.get('gold', {})
    tolerances = params.get('tolerances', {})
    field_weights = params.get('weights', {})

    if not isinstance(artifact, dict):
        return 0.0

    def within_tol(val, g, tol):
        if isinstance(tol, dict) and tol.get('type') == 'larger_of':
            abs_tol = tol['abs']
            rel_tol = tol['rel'] * abs(g)
            eff = max(abs_tol, rel_tol)
            return abs(val - g) <= eff
        else:
            abs_tol = tol.get('abs', 0.0)
            return abs(val - g) <= abs_tol

    # only fields that have valid paper-reported HSE reference:
    valid_fields = [
        'sheet_delta_E_meV',
        'nanotube_delta_E_meV',
        'nanotube_N1_moment',
        'nanotube_N2_moment',
        'nanotube_N3_moment',
    ]
    total_w = sum(field_weights.get(k, 0) for k in valid_fields)
    if total_w == 0.0:
        return 0.0

    score = 0.0

    # sheet ΔE
    if 'sheet_delta_E_meV' in valid_fields and 'sheet' in artifact and 'delta_E_meV' in artifact['sheet']:
        val = artifact['sheet']['delta_E_meV']
        if within_tol(val, gold.get('sheet_delta_E_meV', 0), tolerances.get('sheet_delta_E_meV', {})):
            score += field_weights.get('sheet_delta_E_meV', 0)

    # nanotube ΔE
    if 'nanotube_delta_E_meV' in valid_fields and 'nanotube' in artifact and 'delta_E_meV' in artifact['nanotube']:
        val = artifact['nanotube']['delta_E_meV']
        if within_tol(val, gold.get('nanotube_delta_E_meV', 0), tolerances.get('nanotube_delta_E_meV', {})):
            score += field_weights.get('nanotube_delta_E_meV', 0)

    # nanotube magnetic moments
    if 'nanotube' in artifact and 'magnetic_moments' in artifact['nanotube']:
        for atom in ['N1', 'N2', 'N3']:
            gkey = f'nanotube_{atom}_moment'
            if gkey in valid_fields and atom in artifact['nanotube']['magnetic_moments']:
                val = artifact['nanotube']['magnetic_moments'][atom]
                if within_tol(val, gold.get(gkey, 0), tolerances.get(gkey, {})):
                    score += field_weights.get(gkey, 0)

    return min(score / total_w, 1.0)


_SCORERS = {
    'gga_plus_u_results': score_0,
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
