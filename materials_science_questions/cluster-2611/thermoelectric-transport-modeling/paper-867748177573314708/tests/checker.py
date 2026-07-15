import os
import json
import csv

# === author imports / helpers ===
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
    return {}


# === block: score_0 (check id='step2') ===
def score_0(artifact, step, ctx):
    th = step['thresholds']
    d1 = float(artifact['d_metal_semimetal_A'])
    d2 = float(artifact['d_semimetal_semiconductor_A'])
    ref1, tol1 = th['d_metal_semimetal_A']['value'], th['d_metal_semimetal_A']['abs_tol']
    ref2, tol2 = th['d_semimetal_semiconductor_A']['value'], th['d_semimetal_semiconductor_A']['abs_tol']
    def field_score(val, ref, tol):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))
    s1 = field_score(d1, ref1, tol1)
    s2 = field_score(d2, ref2, tol2)
    return 0.5 * s1 + 0.5 * s2


# === block: score_1 (check id='step4') ===
def score_1(artifact, step, ctx):
    th = step['thresholds']
    def field_score(val, ref, tol):
        diff = abs(val - ref)
        if diff <= tol:
            return 1.0
        return max(0.0, 1.0 - (diff - tol) / (2 * tol))
    scores = []
    for mat in ['As', 'Sb', 'Bi']:
        for key in ['direct_gap_no_SOI_eV', 'direct_gap_with_SOI_eV', 'SOI_gap_at_DP_eV']:
            try:
                val = float(artifact[mat][key])
            except (KeyError, TypeError, ValueError):
                return 0.0
            ref = th[mat][key]['value']
            tol = th[mat][key]['abs_tol']
            scores.append(field_score(val, ref, tol))
    return sum(scores) / len(scores)


# === block: score_2 (check id='step6') ===
def score_2(artifact, step, ctx):
    th = step['thresholds']
    for mat in ['As', 'Sb']:
        if mat not in artifact:
            return 0.0
    def seebeck_score(val, ref, better):
        v = abs(float(val))
        if better == 'greater':
            if v >= ref:
                return 1.0
            return max(0.0, v / ref)
        else:
            if v <= ref:
                return 1.0
            return max(0.0, ref / v)
    scores = []
    for mat in ['As', 'Sb']:
        art_mat = artifact[mat]
        for key in ['peak_p_type_Seebeck_uV_per_K', 'peak_n_type_Seebeck_uV_per_K']:
            try:
                val = float(art_mat[key])
            except:
                return 0.0
            ref = th[mat][key]['value']
            better = th[mat][key]['better_direction']
            scores.append(seebeck_score(val, ref, better))
    bi_art = artifact.get('Bi', {})
    try:
        val_bi = float(bi_art['peak_p_type_Seebeck_uV_per_K'])
    except:
        return 0.0
    ref_bi = th['Bi']['peak_p_type_Seebeck_uV_per_K']['value']
    better_bi = th['Bi']['peak_p_type_Seebeck_uV_per_K']['better_direction']
    scores.append(seebeck_score(val_bi, ref_bi, better_bi))
    flag_score = 1.0 if bi_art.get('bipolar_suppression_observed') is True else 0.0
    scores.append(flag_score)
    return sum(scores) / len(scores)


_SCORERS = {
    'step2': score_0,
    'step4': score_1,
    'step6': score_2,
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
