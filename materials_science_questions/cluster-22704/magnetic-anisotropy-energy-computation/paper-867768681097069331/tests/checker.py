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


# === block: score_0 (check id='relaxed_structures') ===
def score_0(artifact, step, ctx):
    def hex_volume(a, c):
        return (math.sqrt(3.0)/2.0) * a**2 * c

    tols = step['gold']['tolerances']
    gold = step['gold']
    compounds = ['Fe2Ta', 'Fe2W']
    field_weights = {'a_angstrom': 0.25, 'c_angstrom': 0.25, 'xFe2': 0.1, 'z5d': 0.1, 'volume_gold': 0.2, 'volume_self': 0.1}
    scores = []
    for comp in compounds:
        d = artifact.get(comp, {})
        if not d:
            scores.append(0.0)
            continue
        g = gold[comp]
        sub = {}
        # a, c to gold with tolerance
        for field in ['a_angstrom', 'c_angstrom']:
            val = d.get(field)
            if val is None:
                sub[field] = 0.0
                continue
            ref = g[field]
            tol = tols['a_c_ang']
            diff = abs(val - ref)
            if diff <= tol:
                sub[field] = 1.0
            else:
                sub[field] = max(0.0, 1.0 - (diff - tol)/tol)
        # internal coordinates
        for field in ['xFe2', 'z5d']:
            val = d.get(field)
            if val is None:
                sub[field] = 0.0
                continue
            ref = g[field]
            tol = tols[field]
            diff = abs(val - ref)
            if diff <= tol:
                sub[field] = 1.0
            else:
                sub[field] = max(0.0, 1.0 - (diff - tol)/tol)
        # volume compared to gold volume computed from gold a,c
        g_vol = hex_volume(g['a_angstrom'], g['c_angstrom'])
        ag_vol = d.get('volume_angstrom3')
        if ag_vol is not None:
            diffv = abs(ag_vol - g_vol)
            tol_v = tols['volume_ang3']
            if diffv <= tol_v:
                sub['volume_gold'] = 1.0
            else:
                sub['volume_gold'] = max(0.0, 1.0 - (diffv - tol_v)/tol_v)
            # self consistency: volume computed from reported a,c vs reported volume
            ag_a = d.get('a_angstrom')
            ag_c = d.get('c_angstrom')
            if ag_a is not None and ag_c is not None:
                calc_vol = hex_volume(ag_a, ag_c)
                diff_self = abs(ag_vol - calc_vol)
                tol_self = 0.1
                if diff_self <= tol_self:
                    sub['volume_self'] = 1.0
                else:
                    sub['volume_self'] = max(0.0, 1.0 - (diff_self - tol_self)/tol_self)
            else:
                sub['volume_self'] = 0.0
        else:
            sub['volume_gold'] = 0.0
            sub['volume_self'] = 0.0
        comp_score = sum(field_weights[k] * sub.get(k, 0.0) for k in field_weights)
        scores.append(comp_score)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_1 (check id='mae_moments') ===
def score_1(artifact, step, ctx):
    import math

    gold = step['gold']
    tols = gold['tolerances']
    compounds = ['Fe2Ta', 'Fe2W']
    field_weights = {'spin': 0.25, 'mae_meV': 0.25, 'mae_MJ_gold': 0.25, 'easy_axis': 0.1, 'consistency': 0.15}
    # load relaxed_structures.json for volume needed in MAE consistency
    import json, os
    relax_path = '/app/outputs/relaxed_structures.json'
    relax = None
    if os.path.exists(relax_path):
        with open(relax_path) as f:
            relax = json.load(f)

    def hex_volume(a, c):
        return (math.sqrt(3.0)/2.0) * a**2 * c

    scores = []
    for comp in compounds:
        d = artifact.get(comp, {})
        if not d:
            scores.append(0.0)
            continue
        g = gold[comp]
        sub = {}
        # spin moment
        val = d.get('total_spin_moment_muB_per_unit_cell')
        if val is not None:
            ref = g['total_spin_moment_muB_per_unit_cell']
            tol = tols['spin_moment_muB']
            diff = abs(val - ref)
            if diff <= tol:
                sub['spin'] = 1.0
            else:
                sub['spin'] = max(0.0, 1.0 - (diff - tol)/tol)
        else:
            sub['spin'] = 0.0
        # mae_meV
        val = d.get('mae_meV_per_unit_cell')
        if val is not None:
            ref = g['mae_meV_per_unit_cell']
            tol = tols['mae_meV']
            diff = abs(val - ref)
            if diff <= tol:
                sub['mae_meV'] = 1.0
            else:
                sub['mae_meV'] = max(0.0, 1.0 - (diff - tol)/tol)
        else:
            sub['mae_meV'] = 0.0
        # mae_MJ
        val = d.get('mae_MJ_per_m3')
        if val is not None:
            ref = g['mae_MJ_per_m3']
            tol = tols['mae_MJ_m3']
            diff = abs(val - ref)
            if diff <= tol:
                sub['mae_MJ_gold'] = 1.0
            else:
                sub['mae_MJ_gold'] = max(0.0, 1.0 - (diff - tol)/tol)
        else:
            sub['mae_MJ_gold'] = 0.0
        # easy axis
        ax = d.get('easy_axis')
        sub['easy_axis'] = 1.0 if ax == 'c' else 0.0
        # consistency: mae_MJ should match mae_meV converted using volume from relaxation
        mae_meV = d.get('mae_meV_per_unit_cell')
        mae_MJ_reported = d.get('mae_MJ_per_m3')
        if mae_meV is not None and mae_MJ_reported is not None and relax and comp in relax:
            rel = relax[comp]
            a = rel.get('a_angstrom')
            c = rel.get('c_angstrom')
            if a is not None and c is not None:
                vol = hex_volume(a, c)
                predicted = mae_meV * 160.2176634 / vol  # 1 meV/Å³ -> MJ/m³ factor
                tol_c = max(0.02 * abs(predicted), 0.05)
                diff = abs(mae_MJ_reported - predicted)
                if diff <= tol_c:
                    sub['consistency'] = 1.0
                else:
                    sub['consistency'] = max(0.0, 1.0 - (diff - tol_c)/tol_c)
            else:
                sub['consistency'] = 0.0
        else:
            sub['consistency'] = 0.0
        comp_score = sum(field_weights[k] * sub.get(k, 0.0) for k in field_weights)
        scores.append(comp_score)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'relaxed_structures': score_0,
    'mae_moments': score_1,
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
