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
    import csv, json, os

    fx300 = fx0 = stress = None
    results = None

    def load_csv(path):
        if not os.path.exists(path):
            return []
        with open(path, 'r', newline='') as f:
            return list(csv.DictReader(f))

    path = os.path.join(outputs_dir, 'force_deformation_300K.csv')
    fx300 = load_csv(path)
    path = os.path.join(outputs_dir, 'force_deformation_0K.csv')
    fx0 = load_csv(path)
    path = os.path.join(outputs_dir, 'stress_profiles_300K.csv')
    stress = load_csv(path)
    path = os.path.join(outputs_dir, 'results.json')
    if os.path.exists(path):
        with open(path, 'r') as f:
            results = json.load(f)

    return {'fx300': fx300, 'fx0': fx0, 'stress': stress, 'results': results}


# === block: score_0 (check id='step_fx_300K') ===
def score_0(artifact, step, ctx):
    rows = ctx.get('fx300', [])
    if not rows:
        return 0.0
    try:
        deformations = [float(r['deformation_nm']) for r in rows if r['deformation_nm']]
        forces = [float(r['force_nN']) for r in rows if r['force_nN']]
        if not deformations or not forces or len(deformations) != len(forces):
            return 0.0
        max_force = max(forces)
        idx = forces.index(max_force)
        max_def = deformations[idx]
    except (KeyError, ValueError):
        return 0.0

    target = step.get('target', {})
    ref_force = target.get('critical_force_300K_nN', 0.65)
    ref_def = target.get('critical_deformation_300K_nm', 9.5)
    tol = step.get('tolerance', {})
    tol_force = tol.get('force_nN', 0.10)
    tol_def = tol.get('deformation_nm', 0.5)

    err_f = max(0.0, abs(max_force - ref_force) - tol_force)
    score_force = 1.0 - min(1.0, err_f / (2 * tol_force)) if tol_force > 0 else 1.0

    err_d = max(0.0, abs(max_def - ref_def) - tol_def)
    score_def = 1.0 - min(1.0, err_d / (2 * tol_def)) if tol_def > 0 else 1.0

    return 0.5 * score_force + 0.5 * score_def


# === block: score_1 (check id='step_fx_0K') ===
def score_1(artifact, step, ctx):
    rows = ctx.get('fx0', [])
    if not rows:
        return 0.0
    try:
        deformations = [float(r['deformation_nm']) for r in rows if r['deformation_nm']]
        forces = [float(r['force_nN']) for r in rows if r['force_nN']]
        if not deformations or not forces or len(deformations) != len(forces):
            return 0.0
        max_force = max(forces)
        idx = forces.index(max_force)
        max_def = deformations[idx]
    except (KeyError, ValueError):
        return 0.0

    target = step.get('target', {})
    ref_force = target.get('critical_force_0K_nN', 2.25)
    ref_def = target.get('critical_deformation_0K_nm', 9.5)
    tol = step.get('tolerance', {})
    tol_force = tol.get('force_nN', 0.20)
    tol_def = tol.get('deformation_nm', 0.5)

    err_f = max(0.0, abs(max_force - ref_force) - tol_force)
    score_force = 1.0 - min(1.0, err_f / (2 * tol_force)) if tol_force > 0 else 1.0

    err_d = max(0.0, abs(max_def - ref_def) - tol_def)
    score_def = 1.0 - min(1.0, err_d / (2 * tol_def)) if tol_def > 0 else 1.0

    return 0.5 * score_force + 0.5 * score_def


# === block: score_2 (check id='step_stress_300K') ===
def score_2(artifact, step, ctx):
    rows = ctx.get('stress', [])
    if not rows:
        return 0.0
    try:
        defs = []
        vm_top = []
        vm_side = []
        i1_top = []
        i1_side = []
        for r in rows:
            defs.append(float(r['deformation_nm']))
            vm_top.append(float(r['vM_top_MPa']))
            vm_side.append(float(r['vM_side_MPa']))
            i1_top.append(float(r['I1_top_MPa']))
            i1_side.append(float(r['I1_side_MPa']))
        if len(defs) < 2:
            return 0.0
        # crossing deformation
        cross_def = None
        for i in range(len(defs)-1):
            x1, x2 = defs[i], defs[i+1]
            d1 = vm_top[i] - vm_side[i]
            d2 = vm_top[i+1] - vm_side[i+1]
            if d1 * d2 <= 0 and x1 != x2:
                if d2 - d1 == 0:
                    cross_def = x1
                else:
                    cross_def = x1 + (x2 - x1) * (-d1) / (d2 - d1)
                break
        # trend check
        slope_top = (i1_top[-1] - i1_top[0]) / (defs[-1] - defs[0])
        slope_side = (i1_side[-1] - i1_side[0]) / (defs[-1] - defs[0])
        trend_ok = (slope_top < 0) and (slope_side > 0)
    except (IndexError, ZeroDivisionError, ValueError):
        return 0.0

    target_cross = step.get('target', {}).get('crossing_deformation_vM_300K_nm', 7.2)
    tol_cross = step.get('tolerance', {}).get('deformation_nm', 0.5)
    score_cross = 0.0
    if cross_def is not None:
        err = max(0.0, abs(cross_def - target_cross) - tol_cross)
        score_cross = 1.0 - min(1.0, err / (2 * tol_cross)) if tol_cross > 0 else 1.0
    else:
        score_cross = 0.0

    trend_score = 1.0 if trend_ok else 0.0

    return 0.7 * score_cross + 0.3 * trend_score


# === block: score_3 (check id='step_results_json') ===
def score_3(artifact, step, ctx):
    artifact = ctx.get('results', artifact)
    if not isinstance(artifact, dict):
        return 0.0

    # recompute from raw csvs
    rows300 = ctx.get('fx300', [])
    rows0 = ctx.get('fx0', [])
    rows_stress = ctx.get('stress', [])

    recomputed = {}
    # 300K max force
    try:
        defs300 = [float(r['deformation_nm']) for r in rows300 if r['deformation_nm']]
        forces300 = [float(r['force_nN']) for r in rows300 if r['force_nN']]
        if defs300 and forces300 and len(defs300)==len(forces300):
            max_f300 = max(forces300)
            idx300 = forces300.index(max_f300)
            max_def300 = defs300[idx300]
            recomputed['critical_force_300K_nN'] = max_f300
            recomputed['critical_deformation_300K_nm'] = max_def300
        else:
            recomputed['critical_force_300K_nN'] = None
            recomputed['critical_deformation_300K_nm'] = None
    except:
        recomputed['critical_force_300K_nN'] = None
        recomputed['critical_deformation_300K_nm'] = None

    # 0K max force
    try:
        defs0 = [float(r['deformation_nm']) for r in rows0 if r['deformation_nm']]
        forces0 = [float(r['force_nN']) for r in rows0 if r['force_nN']]
        if defs0 and forces0 and len(defs0)==len(forces0):
            max_f0 = max(forces0)
            idx0 = forces0.index(max_f0)
            max_def0 = defs0[idx0]
            recomputed['critical_force_0K_nN'] = max_f0
            recomputed['critical_deformation_0K_nm'] = max_def0
        else:
            recomputed['critical_force_0K_nN'] = None
            recomputed['critical_deformation_0K_nm'] = None
    except:
        recomputed['critical_force_0K_nN'] = None
        recomputed['critical_deformation_0K_nm'] = None

    # crossing vM
    try:
        defs_s = [float(r['deformation_nm']) for r in rows_stress]
        vm_top = [float(r['vM_top_MPa']) for r in rows_stress]
        vm_side = [float(r['vM_side_MPa']) for r in rows_stress]
        cross_def = None
        for i in range(len(defs_s)-1):
            x1, x2 = defs_s[i], defs_s[i+1]
            d1 = vm_top[i] - vm_side[i]
            d2 = vm_top[i+1] - vm_side[i+1]
            if d1 * d2 <= 0:
                if d2 - d1 != 0:
                    cross_def = x1 + (x2 - x1) * (-d1) / (d2 - d1)
                else:
                    cross_def = x1
                break
        recomputed['crossing_deformation_vM_300K_nm'] = cross_def
    except:
        recomputed['crossing_deformation_vM_300K_nm'] = None

    # compare
    fields = [
        ('critical_force_300K_nN', 0.05),
        ('critical_deformation_300K_nm', 0.2),
        ('critical_force_0K_nN', 0.1),
        ('critical_deformation_0K_nm', 0.2),
        ('crossing_deformation_vM_300K_nm', 0.2)
    ]
    total = 0
    ok = 0
    for key, tol in fields:
        if key in artifact and key in recomputed and recomputed[key] is not None:
            total += 1
            if abs(artifact[key] - recomputed[key]) <= tol:
                ok += 1
    if total == 0:
        return 0.0
    return ok / total


_SCORERS = {
    'step_fx_300K': score_0,
    'step_fx_0K': score_1,
    'step_stress_300K': score_2,
    'step_results_json': score_3,
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
