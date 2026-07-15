import os
import json
import csv

# === author imports / helpers ===
import os, csv

def rel_score(val, gold, tol):
    if val is None or gold is None: return 0.0
    if gold == 0: return 1.0 if abs(val) < 1e-9 else 0.0
    err = abs(val - gold) / abs(gold)
    if err <= tol: return 1.0
    return max(0.0, 1.0 - (err - tol) / tol)

def abs_score(val, gold, tol):
    if val is None: return 0.0
    err = abs(val - gold)
    if err <= tol: return 1.0
    return max(0.0, 1.0 - (err - tol) / tol)

def monotonic_check(rows, col, increasing=True):
    vals = []
    for r in rows:
        try:
            v = float(r[col])
            vals.append(v)
        except:
            pass
    if len(vals) < 2: return 1.0
    ok = 0
    pairs = len(vals) - 1
    for i in range(pairs):
        if increasing:
            if vals[i+1] >= vals[i] - 1e-9:
                ok += 1
        else:
            if vals[i+1] <= vals[i] + 1e-9:
                ok += 1
    return ok / max(1, pairs)

def liquid_check(mech):
    total = 0
    ok = 0
    for r in mech:
        try:
            ext = float(r['extent'])
        except: continue
        if ext <= 0.3 + 1e-9:
            try:
                sh = float(r['shear_modulus_GPa'])
                yi = float(r['yield_strength_MPa'])
            except: continue
            total += 1
            if sh <= 0.001 and yi <= 0.001:
                ok += 1
    if total == 0: return 1.0
    return ok / total

def cte_trend(rows):
    total = 0
    ok = 0
    for r in rows:
        try:
            below = float(r['CTE_below_Tg_per_C'])
            above = float(r['CTE_above_Tg_per_C'])
        except: continue
        total += 1
        if above > below + 1e-12:
            ok += 1
    if total == 0: return 1.0
    return ok / total


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
    import os, csv

    ctx = {}

    phys_path = os.path.join(outputs_dir, "physical_properties.csv")
    try:
        with open(phys_path, newline='') as f:
            reader = csv.DictReader(f)
            ctx['physical'] = list(reader)
    except Exception:
        ctx['physical'] = []

    mech_path = os.path.join(outputs_dir, "mechanical_properties.csv")
    try:
        with open(mech_path, newline='') as f:
            reader = csv.DictReader(f)
            ctx['mechanical'] = list(reader)
    except Exception:
        ctx['mechanical'] = []

    therm_path = os.path.join(outputs_dir, "thermal_properties.csv")
    try:
        with open(therm_path, newline='') as f:
            reader = csv.DictReader(f)
            ctx['thermal'] = list(reader)
    except Exception:
        ctx['thermal'] = []

    return ctx


# === block: score_0 (check id='step_physical') ===
def score_0(artifact, step, ctx):
    phys = ctx.get('physical', [])
    if not phys:
        return 0.0
    checks = step.get('params', {}).get('checks', [])
    total_weight = sum(c['weight'] for c in checks)
    if total_weight == 0:
        return 0.0
    final_row = None
    for row in phys:
        try:
            if abs(float(row['extent']) - 0.915) < 1e-6:
                final_row = row
                break
        except: pass
    if final_row is None:
        if phys:
            phys_sorted = sorted(phys, key=lambda r: float(r['extent']))
            final_row = phys_sorted[-1]
        else:
            return 0.0
    def get_float(row, col):
        try:
            return float(row[col])
        except:
            return None
    density = get_float(final_row, 'density_g_per_cc')
    shrinkage = get_float(final_row, 'volumetric_shrinkage_pct')
    score = 0.0
    for c in checks:
        w = c.get('weight', 0)
        name = c.get('name', '')
        if name == 'final_density':
            s = rel_score(density, c['gold'], c['tolerance_rel']) if density is not None else 0.0
        elif name == 'final_shrinkage':
            s = rel_score(shrinkage, c['gold'], c['tolerance_rel']) if shrinkage is not None else 0.0
        elif name == 'monotonic_density':
            s = monotonic_check(phys, 'density_g_per_cc', True)
        elif name == 'monotonic_shrinkage':
            s = monotonic_check(phys, 'volumetric_shrinkage_pct', True)
        else:
            s = 0.0
        score += s * w
    return score / total_weight


# === block: score_1 (check id='step_mechanical') ===
def score_1(artifact, step, ctx):
    mech = ctx.get('mechanical', [])
    if not mech:
        return 0.0
    checks = step.get('params', {}).get('checks', [])
    total_weight = sum(c['weight'] for c in checks)
    if total_weight == 0:
        return 0.0
    final_row = None
    for row in mech:
        try:
            if abs(float(row['extent']) - 0.915) < 1e-6:
                final_row = row
                break
        except: pass
    if final_row is None:
        if mech:
            mech_sorted = sorted(mech, key=lambda r: float(r['extent']))
            final_row = mech_sorted[-1]
        else:
            return 0.0
    def get_float(row, col):
        try: return float(row[col])
        except: return None
    bulk = get_float(final_row, 'bulk_modulus_GPa') if final_row else None
    shear = get_float(final_row, 'shear_modulus_GPa') if final_row else None
    young = get_float(final_row, 'Youngs_modulus_GPa') if final_row else None
    poisson = get_float(final_row, 'Poisson_ratio') if final_row else None
    yield_val = get_float(final_row, 'yield_strength_MPa') if final_row else None
    score = 0.0
    for c in checks:
        w = c.get('weight', 0)
        name = c.get('name', '')
        if name == 'final_bulk':
            s = rel_score(bulk, c['gold'], c['tolerance_rel'])
        elif name == 'final_shear':
            s = rel_score(shear, c['gold'], c['tolerance_rel'])
        elif name == 'final_young':
            s = rel_score(young, c['gold'], c['tolerance_rel'])
        elif name == 'final_poisson':
            s = abs_score(poisson, c['gold'], c['tolerance_abs'])
        elif name == 'final_yield':
            s = rel_score(yield_val, c['gold'], c['tolerance_rel'])
        elif name == 'monotonic_moduli':
            s1 = monotonic_check(mech, 'bulk_modulus_GPa', True)
            s2 = monotonic_check(mech, 'shear_modulus_GPa', True)
            s3 = monotonic_check(mech, 'Youngs_modulus_GPa', True)
            s = (s1 + s2 + s3) / 3.0
        elif name == 'liquid_low_extent':
            s = liquid_check(mech)
        else:
            s = 0.0
        score += s * w
    return score / total_weight


# === block: score_2 (check id='step_thermal') ===
def score_2(artifact, step, ctx):
    therm = ctx.get('thermal', [])
    if not therm:
        return 0.0
    checks = step.get('params', {}).get('checks', [])
    total_weight = sum(c['weight'] for c in checks)
    if total_weight == 0:
        return 0.0
    final_row = None
    for row in therm:
        try:
            if abs(float(row['extent']) - 0.915) < 1e-6:
                final_row = row
                break
        except: pass
    if final_row is None:
        if therm:
            therm_sorted = sorted(therm, key=lambda r: float(r['extent']))
            final_row = therm_sorted[-1]
        else:
            return 0.0
    def get_float(row, col):
        try: return float(row[col])
        except: return None
    tg = get_float(final_row, 'Tg_C') if final_row else None
    cte_below = get_float(final_row, 'CTE_below_Tg_per_C') if final_row else None
    score = 0.0
    for c in checks:
        w = c.get('weight', 0)
        name = c.get('name', '')
        if name == 'final_tg':
            s = rel_score(tg, c['gold'], c['tolerance_rel'])
        elif name == 'final_cte_below':
            s = rel_score(cte_below, c['gold'], c['tolerance_rel'])
        elif name == 'monotonic_tg':
            s = monotonic_check(therm, 'Tg_C', True)
        elif name == 'cte_above_gt_below':
            s = cte_trend(therm)
        else:
            s = 0.0
        score += s * w
    return score / total_weight


_SCORERS = {
    'step_physical': score_0,
    'step_mechanical': score_1,
    'step_thermal': score_2,
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
