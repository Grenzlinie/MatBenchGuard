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
    return {}


# === block: score_0 (check id='elastic') ===
def score_0(artifact, step, ctx):
    ref = step['reference']
    tol_ratio = step['tolerance_ratio']
    compounds = ['MAPbI3', 'MAPbBr3', 'MAPbCl3']
    # tolerance check on elastic constants
    const_scores = []
    for comp in compounds:
        if comp not in artifact:
            const_scores.append(0.0)
            continue
        art = artifact[comp]
        refc = ref[comp]
        fields = ['c11','c22','c33','c44','c55','c66','c12','c13','c23']
        passed = 0
        total = 0
        for f in fields:
            if f in art and f in refc:
                total += 1
                val = float(art[f])
                rval = float(refc[f])
                if abs(rval) < 1e-6:
                    if abs(val) < 1e-6:
                        passed += 1
                else:
                    if abs(val - rval) / abs(rval) <= tol_ratio:
                        passed += 1
        if total > 0:
            const_scores.append(passed / total)
        else:
            const_scores.append(0.0)
    const_avg = sum(const_scores) / len(compounds)
    # orthorhombic stability criteria
    stab_scores = []
    for comp in compounds:
        if comp not in artifact:
            stab_scores.append(0.0)
            continue
        a = artifact[comp]
        c11 = float(a.get('c11', -1))
        c22 = float(a.get('c22', -1))
        c33 = float(a.get('c33', -1))
        c44 = float(a.get('c44', -1))
        c55 = float(a.get('c55', -1))
        c66 = float(a.get('c66', -1))
        c12 = float(a.get('c12', -1))
        c13 = float(a.get('c13', -1))
        c23 = float(a.get('c23', -1))
        diag = [c11,c22,c33,c44,c55,c66]
        ok = all(v>0 for v in diag)
        ok = ok and (c11+c22-2*c12>0) and (c11+c33-2*c13>0) and (c22+c33-2*c23>0) and (c11+c22+c33+2*c12+2*c13+2*c23>0)
        stab_scores.append(1.0 if ok else 0.0)
    stab_avg = sum(stab_scores) / len(compounds)
    # Young's modulus trend Ey
    trend_ok = True
    Ey = {}
    for comp in compounds:
        if comp not in artifact or 'Ey' not in artifact[comp]:
            trend_ok = False
            break
        Ey[comp] = float(artifact[comp]['Ey'])
    if trend_ok and not (Ey['MAPbCl3'] > Ey['MAPbBr3'] > Ey['MAPbI3']):
        trend_ok = False
    trend_score = 1.0 if trend_ok else 0.0
    return 0.4 * const_avg + 0.3 * stab_avg + 0.3 * trend_score


# === block: score_1 (check id='bandgap') ===
def score_1(artifact, step, ctx):
    ref = step['reference']
    tol = step['tolerance']
    compounds = ['MAPbI3', 'MAPbBr3', 'MAPbCl3']
    passed = 0
    for c in compounds:
        if c in artifact and abs(float(artifact[c]) - ref[c]) <= tol:
            passed += 1
    return passed / len(compounds)


# === block: score_2 (check id='pdos') ===
def score_2(artifact, step, ctx):
    peak_target = step['peak_energy_target']
    peak_tol = step['peak_tolerance']
    max_rel = step['max_dos_relative']
    compounds = ['MAPbI3', 'MAPbBr3', 'MAPbCl3']
    compound_scores = []
    for c in compounds:
        if c not in artifact:
            compound_scores.append(0.0)
            continue
        a = artifact[c]
        peak_ok = abs(float(a['MA_p_peak_energy_eV']) - peak_target) <= peak_tol
        vbm_ok = float(a['dos_at_VBM_relative']) <= max_rel
        cbm_ok = float(a['dos_at_CBM_relative']) <= max_rel
        compound_scores.append( sum([peak_ok, vbm_ok, cbm_ok]) / 3.0 )
    return sum(compound_scores) / len(compounds)


# === block: score_3 (check id='absorption') ===
def score_3(artifact, step, ctx):
    visible = step['visible_range']
    min_peak = step['min_peak_alpha']
    max_alpha = 0.0
    for row in artifact:
        try:
            e = float(row['energy_eV'])
            alpha = float(row['alpha_MAPbI3'])
            if visible[0] <= e <= visible[1] and alpha > max_alpha:
                max_alpha = alpha
        except (KeyError, ValueError):
            continue
    return 1.0 if max_alpha >= min_peak else 0.0


# === block: score_4 (check id='dielectric') ===
def score_4(artifact, step, ctx):
    target_eps = step['static_eps1_MAPbI3_target']
    tol_eps = step['static_eps1_MAPbI3_tolerance']
    compounds = step['trend_compounds']
    # find row closest to energy 0.0
    eps1 = {c: None for c in compounds}
    best_row = None
    min_diff = float('inf')
    for row in artifact:
        try:
            e = float(row['energy_eV'])
            diff = abs(e)
            if diff < min_diff:
                min_diff = diff
                best_row = row
        except (KeyError, ValueError):
            continue
    if best_row is None:
        return 0.0
    for c in compounds:
        col = f'eps1_{c}'
        if col in best_row:
            eps1[c] = float(best_row[col])
    # MAPbI3 static epsilon check
    in_range = False
    if eps1['MAPbI3'] is not None:
        in_range = abs(eps1['MAPbI3'] - target_eps) <= tol_eps
    # trend check
    trend_ok = True
    for c in compounds:
        if eps1[c] is None:
            trend_ok = False
            break
    if trend_ok and not (eps1['MAPbI3'] > eps1['MAPbBr3'] > eps1['MAPbCl3']):
        trend_ok = False
    score = 0.0
    if in_range:
        score += 0.5
    if trend_ok:
        score += 0.5
    return score


_SCORERS = {
    'elastic': score_0,
    'bandgap': score_1,
    'pdos': score_2,
    'absorption': score_3,
    'dielectric': score_4,
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
