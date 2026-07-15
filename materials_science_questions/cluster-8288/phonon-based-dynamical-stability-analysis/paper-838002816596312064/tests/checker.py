import os
import json
import csv

# === author imports / helpers ===
import os, json, itertools

def lower_hull(points):
    """Compute lower convex hull of (x,y) points sorted by x, return hull points"""
    pts = sorted(points, key=lambda p: p[0])
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2:
            x1, y1 = lower[-2]
            x2, y2 = lower[-1]
            x3, y3 = p
            # cross product (x2-x1)(y3-y1) - (y2-y1)(x3-x1) <= 0 for lower hull (clockwise)
            if (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1) <= 0:
                break
            lower.pop()
        lower.append(p)
    return lower

def point_on_lower_hull(p, hull):
    """Return True if point is approximately on the lower hull"""
    x0, y0 = p
    # check if near any hull edge
    for i in range(len(hull)-1):
        (x1, y1), (x2, y2) = hull[i], hull[i+1]
        if x1 <= x0 <= x2 or x2 <= x0 <= x1:
            if abs(x2 - x1) < 1e-12:
                continue
            t = (x0 - x1) / (x2 - x1)
            y_line = y1 + t * (y2 - y1)
            if abs(y0 - y_line) < 1e-9:
                return True
    return False


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
    gold = spec['steps'][0].get('hidden_gold', {})
    stable_gold = gold.get('stable_ranges', {})
    tolerances = gold.get('tolerances', {'min':30, 'max':30})
    composition_frac = {
        'Mg2O3H2': 2/3,
        'MgO3H4': 1/3,
        'MgO4H6': 1/4
    }
    return {'stable_gold': stable_gold, 'tol': tolerances, 'comp_frac': composition_frac}


# === block: score_0 (check id='check_convex_hull') ===
def score_0(artifact, step, ctx):
    data = artifact
    pressures = data.get('pressures', [])
    compounds = data.get('compounds', [])
    formation = data.get('formation_enthalpy_per_fu', {})
    reference = data.get('reference_enthalpies', {})
    agent_ranges = data.get('stable_ranges', {})

    # compute best reference per pressure
    ref_mgo_per_p = []
    ref_water_per_p = []
    for idx, P in enumerate(pressures):
        # MgO best
        mgo_vals = [reference[key][idx] for key in reference if key.startswith('MgO_')]
        ref_mgo_per_p.append(min(mgo_vals) if mgo_vals else 0.0)
        # water best
        water_vals = [reference[key][idx] for key in reference if key.startswith('ice_')]
        ref_water_per_p.append(min(water_vals) if water_vals else 0.0)

    # recompute hull and stability per pressure
    on_hull = {c: [] for c in compounds}
    for idx, P in enumerate(pressures):
        points = [(0.0, 0.0), (1.0, 0.0)]
        for comp in compounds:
            x = ctx['comp_frac'][comp]
            try:
                delta = formation[comp][idx]
            except (IndexError, KeyError):
                delta = 0.0
            points.append((x, delta))
        hull = lower_hull(points)
        for comp in compounds:
            x = ctx['comp_frac'][comp]
            delta = formation.get(comp, [0]*len(pressures))[idx]
            on_hull[comp].append(point_on_lower_hull((x, delta), hull))

    # derive stable pressure sets
    stable_pressures = {}
    for comp in compounds:
        stable_pressures[comp] = {P for i, P in enumerate(pressures) if on_hull[comp][i]}

    # agent stable sets from ranges
    agent_stable = {}
    for comp in compounds:
        r = agent_ranges.get(comp)
        if not (isinstance(r, (list, tuple)) and len(r) == 2):
            agent_stable[comp] = set()
            continue
        lo, hi = r
        agent_stable[comp] = {P for P in pressures if lo <= P <= hi}

    # consistency Jaccard
    jaccards = []
    for comp in compounds:
        a = stable_pressures[comp]
        b = agent_stable[comp]
        if not a and not b:
            j = 1.0
        elif not a or not b:
            j = 0.0
        else:
            j = len(a & b) / len(a | b)
        jaccards.append(j)
    consistency_score = sum(jaccards) / len(jaccards) if jaccards else 1.0

    # accuracy against paper gold
    gold = ctx['stable_gold']
    tol = ctx['tol']
    acc_bounds = []
    for comp in compounds:
        gr = gold.get(comp)
        ar = agent_ranges.get(comp)
        if not (isinstance(ar, (list, tuple)) and len(ar) == 2):
            acc_bounds.append(0.0)
            continue
        # check bound(s)
        if gr:
            # lower bound
            if 'min' in gr and gr['min'] is not None:
                target = gr['min']
                actual = ar[0]
                tol_min = tol.get('min', 30)
                if abs(actual - target) <= tol_min:
                    lower_ok = 1.0
                else:
                    lower_ok = 0.0
            else:
                lower_ok = 1.0
            # upper bound: only if target_max is finite (<1000 say) and present
            if 'max' in gr and gr['max'] is not None and gr['max'] < 1000:
                target = gr['max']
                actual = ar[1]
                tol_max = tol.get('max', 30)
                if abs(actual - target) <= tol_max:
                    upper_ok = 1.0
                else:
                    upper_ok = 0.0
            else:
                upper_ok = 1.0
            # combine bounds equally
            comp_ok = (lower_ok + upper_ok) / 2.0 if ('min' in gr or 'max' in gr) else 1.0
        else:
            comp_ok = 0.0
        acc_bounds.append(comp_ok)
    accuracy_score = sum(acc_bounds) / len(acc_bounds) if acc_bounds else 0.0

    # combine
    w_cons = ctx.get('consistency_weight', 0.4)
    w_acc = 1.0 - w_cons
    final = w_cons * consistency_score + w_acc * accuracy_score
    return max(0.0, min(1.0, final))


# === block: score_1 (check id='check_phonon_stability') ===
def score_1(artifact, step, ctx):
    phonon = artifact.get('compounds', {})
    # load convex hull ranges for cross-check
    hull_path = os.path.join('/app/outputs', 'step_01_convex_hull.json')
    hull_data = None
    if os.path.exists(hull_path):
        with open(hull_path) as f:
            hull_data = json.load(f)
    stable_ranges = hull_data.get('stable_ranges', {}) if hull_data else {}

    compounds = ['Mg2O3H2', 'MgO3H4', 'MgO4H6']
    scores = []
    for comp in compounds:
        entry = phonon.get(comp)
        if not isinstance(entry, dict):
            scores.append(0.0)
            continue
        has_imag = entry.get('has_imaginary_modes', True)
        if has_imag:  # claimed imaginary -> zero score
            scores.append(0.0)
            continue
        # check pressure within stable range from step_01
        pressure = entry.get('pressure', None)
        in_range = False
        if pressure is not None:
            rng = stable_ranges.get(comp)
            if isinstance(rng, (list, tuple)) and len(rng) == 2:
                lo, hi = rng
                in_range = lo <= pressure <= hi
        # score: 0.7 for correct mode, 0.3 for pressure in range
        score = 0.7 + (0.3 if in_range else 0.0)
        scores.append(score)
    return sum(scores) / len(scores) if scores else 0.0


_SCORERS = {
    'check_convex_hull': score_0,
    'check_phonon_stability': score_1,
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
