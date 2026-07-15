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
    return {}


# === block: score_0 (check id='mu_star_check') ===
def score_0(artifact, step, ctx):
    def get_nested(d, path):
        keys = path.split('.')
        for k in keys:
            if not isinstance(d, dict) or k not in d:
                return None
            d = d[k]
        return d

    def field_score(val, gold, tol_rel):
        if val is None:
            return 0.0
        if gold == 0:
            return 1.0 if abs(val) < 1e-9 else 0.0
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= tol_rel:
            return 1.0
        # linear decay to 0 at 2*tol_rel
        return max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)

    gv = step.get('gold_values', {})
    struct = step.get('structural_checks', [])
    artifact = artifact  # passed as arg

    # extract values
    h3_conv = get_nested(artifact, 'H3S.conventional.mu_star')
    h3_vc = get_nested(artifact, 'H3S.vertex_corrected.mu_star')
    ph3_conv = get_nested(artifact, 'PH3.conventional.mu_star')
    ph3_vc = get_nested(artifact, 'PH3.vertex_corrected.mu_star')

    # compute sub-scores per compound
    h3_sub = (field_score(h3_conv, gv['H3S.conventional.mu_star']['value'], gv['H3S.conventional.mu_star']['tolerance_rel']) +
              field_score(h3_vc, gv['H3S.vertex_corrected.mu_star']['value'], gv['H3S.vertex_corrected.mu_star']['tolerance_rel'])) / 2.0

    ph3_sub = (field_score(ph3_conv, gv['PH3.conventional.mu_star']['value'], gv['PH3.conventional.mu_star']['tolerance_rel']) +
               field_score(ph3_vc, gv['PH3.vertex_corrected.mu_star']['value'], gv['PH3.vertex_corrected.mu_star']['tolerance_rel'])) / 2.0

    # structural: conventional > vertex_corrected
    for sc in struct:
        if sc['type'] == 'greater_than':
            a = get_nested(artifact, sc['field_a'])
            b = get_nested(artifact, sc['field_b'])
            if a is not None and b is not None and a <= b:
                if 'H3S' in sc['field_a']:
                    h3_sub = 0.0
                else:
                    ph3_sub = 0.0

    return 0.5 * h3_sub + 0.5 * ph3_sub


# === block: score_1 (check id='gap_mass_check') ===
def score_1(artifact, step, ctx):
    def get_nested(d, path):
        keys = path.split('.')
        for k in keys:
            if not isinstance(d, dict) or k not in d:
                return None
            d = d[k]
        return d

    def field_score(val, gold, tol_rel):
        if val is None:
            return 0.0
        if gold == 0:
            return 1.0 if abs(val) < 1e-9 else 0.0
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= tol_rel:
            return 1.0
        return max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)

    gv = step.get('gold_values', {})
    struct = step.get('structural_checks', [])
    artifact = artifact

    # fields per compound
    h3_fields = ['H3S.conventional.ratio_2delta_Tc', 'H3S.vertex_corrected.ratio_2delta_Tc',
                 'H3S.conventional.delta_0', 'H3S.vertex_corrected.delta_0',
                 'H3S.conventional.m_eff_ratio', 'H3S.vertex_corrected.m_eff_ratio']
    ph3_fields = ['PH3.conventional.ratio_2delta_Tc', 'PH3.vertex_corrected.ratio_2delta_Tc',
                  'PH3.conventional.delta_0', 'PH3.vertex_corrected.delta_0',
                  'PH3.conventional.m_eff_ratio', 'PH3.vertex_corrected.m_eff_ratio']

    def compound_score(fields):
        scores = []
        for f in fields:
            val = get_nested(artifact, f)
            gold = gv[f]['value']
            tol = gv[f]['tolerance_rel']
            scores.append(field_score(val, gold, tol))
        return sum(scores)/len(scores) if scores else 0.0

    h3_sub = compound_score(h3_fields)
    ph3_sub = compound_score(ph3_fields)

    # structural penalties
    penalty_h3 = 1.0
    penalty_ph3 = 1.0
    for sc in struct:
        if sc.get('type') == 'equal_within_abs':
            a = get_nested(artifact, sc['field_a'])
            b = get_nested(artifact, sc['field_b'])
            if a is not None and b is not None:
                if abs(a - b) > sc['abs_tol']:
                    if sc['compound'] == 'H3S':
                        penalty_h3 *= sc['penalty_factor']
                    else:
                        penalty_ph3 *= sc['penalty_factor']

    return (h3_sub * penalty_h3 + ph3_sub * penalty_ph3) / 2.0


# === block: score_2 (check id='thermo_check') ===
def score_2(artifact, step, ctx):
    def get_nested(d, path):
        keys = path.split('.')
        for k in keys:
            if not isinstance(d, dict) or k not in d:
                return None
            d = d[k]
        return d

    def field_score(val, gold, tol_rel):
        if val is None:
            return 0.0
        if gold == 0:
            return 1.0 if abs(val) < 1e-9 else 0.0
        rel_err = abs(val - gold) / abs(gold)
        if rel_err <= tol_rel:
            return 1.0
        return max(0.0, 1.0 - (rel_err - tol_rel) / tol_rel)

    gv = step.get('gold_values', {})
    struct = step.get('structural_checks', [])
    artifact = artifact

    h3_fields = ['H3S.conventional.R_C', 'H3S.vertex_corrected.R_C',
                 'H3S.conventional.R_H', 'H3S.vertex_corrected.R_H']
    ph3_fields = ['PH3.conventional.R_C', 'PH3.vertex_corrected.R_C',
                  'PH3.conventional.R_H', 'PH3.vertex_corrected.R_H']

    def compound_score(fields):
        scores = []
        for f in fields:
            val = get_nested(artifact, f)
            gold = gv[f]['value']
            tol = gv[f]['tolerance_rel']
            scores.append(field_score(val, gold, tol))
        return sum(scores)/len(scores) if scores else 0.0

    h3_sub = compound_score(h3_fields)
    ph3_sub = compound_score(ph3_fields)

    penalty_h3 = 1.0
    penalty_ph3 = 1.0
    for sc in struct:
        if sc.get('type') == 'equal_within_abs':
            a = get_nested(artifact, sc['field_a'])
            b = get_nested(artifact, sc['field_b'])
            if a is not None and b is not None:
                if abs(a - b) > sc['abs_tol']:
                    # check if tolerance is relative to gold? we use absolute tol from spec
                    if sc['compound'] == 'H3S':
                        penalty_h3 *= sc['penalty_factor']
                    else:
                        penalty_ph3 *= sc['penalty_factor']

    return (h3_sub * penalty_h3 + ph3_sub * penalty_ph3) / 2.0


_SCORERS = {
    'mu_star_check': score_0,
    'gap_mass_check': score_1,
    'thermo_check': score_2,
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
