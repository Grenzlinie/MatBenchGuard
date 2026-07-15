import os
import json
import csv

# === author imports / helpers ===
import math
from collections import defaultdict


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


# === block: score_0 (check id='step_04_isotherm') ===
def score_0(artifact, step, ctx):
    rows = artifact
    models_required = {'rigid','Nicholas_mod_flex','Demontis_mod_flex','Nicholas_avg_empty','Nicholas_avg_loaded','Demontis_avg_empty','Demontis_avg_loaded'}
    model_rows = defaultdict(list)
    models_present = set()
    for r in rows:
        m = r.get('model','').strip()
        if m:
            models_present.add(m)
            model_rows[m].append(r)

    # --- reference gold points (pressure_ratio -> loading) per model ---
    # derived from Fig. 3 and the paper's description: rigid – smooth with change of slope ~24 mol/uc;
    # Nicholas_mod_flex – sub‑step from ~30‑37 mol/uc; Demontis_mod_flex – matches experiment
    # at low loadings and saturation, no step.  Tolerance: ±15% or ±2 mol/uc, whichever larger.
    GOLD_POINTS = {
        'rigid': [(0.02, 10), (0.1, 22), (0.3, 28), (0.5, 32), (0.8, 38)],
        'Nicholas_mod_flex': [(0.02, 10), (0.1, 20), (0.3, 24), (0.5, 28), (0.7, 37), (0.9, 38)],
        'Demontis_mod_flex': [(0.02, 10), (0.1, 22), (0.3, 30), (0.5, 34), (0.8, 38)],
        # average‑structure models are not the primary target; reuse rigid-like gold with looser check
        'Nicholas_avg_empty': [(0.02, 10), (0.1, 20), (0.3, 24), (0.5, 28), (0.7, 37), (0.9, 38)],
        'Nicholas_avg_loaded': [(0.02, 10), (0.1, 20), (0.3, 24), (0.5, 28), (0.7, 37), (0.9, 38)],
        'Demontis_avg_empty': [(0.02, 10), (0.1, 22), (0.3, 30), (0.5, 34), (0.8, 38)],
        'Demontis_avg_loaded': [(0.02, 10), (0.1, 22), (0.3, 30), (0.5, 34), (0.8, 38)],
    }

    def interpolate_loading(sorted_rows, target_pressure):
        """Linear interpolation of loading at a given pressure_ratio from sorted rows."""
        if not sorted_rows:
            return None
        pressures = [float(r['pressure_ratio']) for r in sorted_rows]
        loads = [float(r['loading']) for r in sorted_rows]
        if target_pressure <= pressures[0]:
            return loads[0]
        if target_pressure >= pressures[-1]:
            return loads[-1]
        for i in range(len(pressures)-1):
            if pressures[i] <= target_pressure <= pressures[i+1]:
                if pressures[i+1] == pressures[i]:
                    return loads[i]
                frac = (target_pressure - pressures[i]) / (pressures[i+1] - pressures[i])
                return loads[i] + frac * (loads[i+1] - loads[i])
        return None

    # --- base checks (0.25 weight internally) ---
    base_score = 0.0
    if models_present == models_required:
        base_score += 0.1
    cnt10 = sum(1 for m in models_required if len(model_rows.get(m,[])) >= 10)
    base_score += 0.05 * (cnt10 / len(models_required))
    mono_count = 0
    for m in models_required:
        mrows = sorted(model_rows.get(m,[]), key=lambda x: float(x['pressure_ratio']))
        ok = True
        prev = None
        for r in mrows:
            ld = float(r['loading'])
            if ld <= 0:
                ok = False
                break
            if prev is not None and ld < prev:
                ok = False
                break
            prev = ld
        if len(mrows) > 0 and ok:
            mono_count += 1
    base_score += 0.1 * (mono_count / len(models_required))

    # --- reference point accuracy (0.40 weight) ---
    ref_score = 0.0
    models_with_ref = 0
    for m in models_required:
        golds = GOLD_POINTS.get(m, [])
        if not golds:
            continue
        mrows = model_rows.get(m, [])
        if len(mrows) < 2:
            continue
        sorted_rows = sorted(mrows, key=lambda x: float(x['pressure_ratio']))
        passed = 0
        total = len(golds)
        for p_gold, l_gold in golds:
            l_agent = interpolate_loading(sorted_rows, p_gold)
            if l_agent is None:
                continue
            tol = max(0.15 * l_gold, 2.0)  # ±15% or at least 2 molecules/uc
            if abs(l_agent - l_gold) <= tol:
                passed += 1
        ref_score += passed / total if total > 0 else 0.0
        models_with_ref += 1
    if models_with_ref > 0:
        ref_score /= models_with_ref

    # --- sub‑step detection (0.35 weight) ---
    sub_nich = 0.0
    sub_dem = 0.0
    if 'Nicholas_mod_flex' in model_rows and len(model_rows['Nicholas_mod_flex']) >= 2:
        rows_n = sorted(model_rows['Nicholas_mod_flex'], key=lambda x: float(x['pressure_ratio']))
        found = False
        for i in range(len(rows_n)):
            ld_i = float(rows_n[i]['loading'])
            if ld_i < 28: continue
            if ld_i > 40: break
            p_i = float(rows_n[i]['pressure_ratio'])
            p_limit = p_i * (10**0.5)
            max_ld = ld_i
            for j in range(i+1, len(rows_n)):
                ld_j = float(rows_n[j]['loading'])
                if ld_j > 40: break
                if float(rows_n[j]['pressure_ratio']) > p_limit:
                    break
                if ld_j > max_ld:
                    max_ld = ld_j
            if max_ld - ld_i > 5:
                found = True
                break
        sub_nich = 1.0 if found else 0.0
    if 'Demontis_mod_flex' in model_rows and len(model_rows['Demontis_mod_flex']) >= 2:
        rows_d = sorted(model_rows['Demontis_mod_flex'], key=lambda x: float(x['pressure_ratio']))
        found_dem = False
        for i in range(len(rows_d)):
            ld_i = float(rows_d[i]['loading'])
            if ld_i < 28: continue
            if ld_i > 40: break
            p_i = float(rows_d[i]['pressure_ratio'])
            p_limit = p_i * (10**0.5)
            max_ld = ld_i
            for j in range(i+1, len(rows_d)):
                ld_j = float(rows_d[j]['loading'])
                if ld_j > 40: break
                if float(rows_d[j]['pressure_ratio']) > p_limit:
                    break
                if ld_j > max_ld:
                    max_ld = ld_j
            if max_ld - ld_i > 5:
                found_dem = True
                break
        sub_dem = 0.0 if found_dem else 1.0
    sub_score = 0.6 * sub_nich + 0.4 * sub_dem

    score = 0.25 * base_score + 0.40 * ref_score + 0.35 * sub_score
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='step_05_heat') ===
def score_1(artifact, step, ctx):
    rows = artifact
    rigid_rows = [r for r in rows if r.get('model','') == 'rigid']
    dem_rows = [r for r in rows if r.get('model','') == 'Demontis_mod_flex']

    # --- hidden reference gold heat values (kJ/mol) at key loadings (molecules/u.c.) ---
    GOLD_HEAT = {
        'rigid':       {20: 12.5, 31: 11.0, 36: 9.5},
        'Demontis_mod_flex': {20: 12.5, 31: 12.5, 36: 8.5}
    }
    HEAT_TOL_FRAC = 0.20   # 20% relative or absolute floor
    HEAT_TOL_ABS  = 2.0    # kJ/mol

    def heat_at_load(sorted_rows, target):
        loads = [float(r['loading']) for r in sorted_rows]
        heats = [float(r['heat']) for r in sorted_rows]
        if not loads:
            return None
        if target <= loads[0]:
            return heats[0]
        if target >= loads[-1]:
            return heats[-1]
        for i in range(len(loads)-1):
            if loads[i] <= target <= loads[i+1]:
                if loads[i+1] == loads[i]:
                    return heats[i]
                frac = (target - loads[i]) / (loads[i+1] - loads[i])
                return heats[i] + frac * (heats[i+1] - heats[i])
        return None

    # ---------- trend score (0.4 weight) ----------
    trend_score = 0.0
    rigid_sorted = sorted(rigid_rows, key=lambda x: float(x['loading']))
    dem_sorted = sorted(dem_rows, key=lambda x: float(x['loading']))

    if len(rigid_sorted) >= 5:
        h24 = heat_at_load(rigid_sorted, 24)
        h36 = heat_at_load(rigid_sorted, 36)
        if h24 is not None and h36 is not None:
            if h36 < h24 - 0.5:
                trend_score += 0.4
            elif h36 <= h24:
                trend_score += 0.2

    if len(dem_sorted) >= 5:
        h20 = heat_at_load(dem_sorted, 20)
        h31 = heat_at_load(dem_sorted, 31)
        h36 = heat_at_load(dem_sorted, 36)
        if h20 is not None and h31 is not None and h36 is not None:
            plateau_range = max(h20, h31) - min(h20, h31)
            if plateau_range < 0.8:
                if h36 < min(h20, h31) - 0.5:
                    trend_score += 0.6
                else:
                    trend_score += 0.2
            else:
                if h36 < min(h20, h31) - 0.5:
                    trend_score += 0.3

    # ---------- value‑match score (0.6 weight) ----------
    value_score = 0.0
    n_points = 0
    for model, refs in GOLD_HEAT.items():
        model_rows = [r for r in rows if r.get('model','') == model]
        if len(model_rows) < 2:
            continue
        sorted_rows = sorted(model_rows, key=lambda x: float(x['loading']))
        for loading, gold_heat in refs.items():
            agent_heat = heat_at_load(sorted_rows, loading)
            if agent_heat is None:
                continue
            tol = max(HEAT_TOL_FRAC * abs(gold_heat), HEAT_TOL_ABS)
            err = abs(agent_heat - gold_heat)
            pt_score = max(0.0, 1.0 - err / tol)
            value_score += pt_score
            n_points += 1

    if n_points > 0:
        value_score /= n_points
    else:
        value_score = 0.0

    score = 0.4 * trend_score + 0.6 * value_score
    return min(1.0, max(0.0, score))


_SCORERS = {
    'step_04_isotherm': score_0,
    'step_05_heat': score_1,
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
