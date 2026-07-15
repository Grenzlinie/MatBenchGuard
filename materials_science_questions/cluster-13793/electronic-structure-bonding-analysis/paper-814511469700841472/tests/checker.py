import os
import json
import csv

# === author imports / helpers ===
import csv
import os
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


# === block: score_0 (check id='formation_enthalpies') ===
def score_0(artifact, step, ctx):
    from collections import defaultdict

    # parse artifact (list of dicts)
    rows = artifact  # artifact is passed as list of OrderedDict
    by_pressure = defaultdict(list)
    for r in rows:
        try:
            comp = r['composition'].strip()
            pres = float(r['pressure'])
            enth = float(r['formation_enthalpy'])
            by_pressure[(comp, pres)].append(enth)
        except (ValueError, KeyError):
            continue

    # group and take minimum
    points_by_pressure = defaultdict(list)
    for (comp, pres), vals in by_pressure.items():
        if pres in [25, 50, 100]:
            points_by_pressure[pres].append((comp, min(vals)))

    # convex hull helper: lower convex hull of (x,y) -> list of (x,y) segments
    import math

    def lower_hull(points):
        # points: list of (composition_str, y)
        # convert composition to Li fraction x
        def frac(comp):
            # parse LiSi4 -> Li=1, Si=4 -> x = 1/5
            if comp.endswith('Si'):
                # format Li<num><Si><num>? Actually LiSi4, Li2Si3 etc.
                parts = comp.split('Si')
                # left part: Li or Li2, etc.
                if parts[0] == 'Li':
                    nLi = 1
                else:
                    nLi = int(parts[0][2:])
                nSi = int(parts[1]) if parts[1] else 1
                x = nLi / (nLi + nSi)
                return x
            else:
                return 0.0
        pts = []
        for comp, y in points:
            x = frac(comp)
            pts.append((x, y))
        # add endpoints Si (x=0, y=0) and Li (x=1, y=0)
        pts.append((0.0, 0.0))
        pts.append((1.0, 0.0))
        pts.sort()
        # compute lower convex hull (minimize y)
        lower = []
        for p in pts:
            while len(lower) >= 2:
                a = lower[-2]
                b = lower[-1]
                # cross product (b-a) x (p-a) should be >= 0 for lower hull? For points sorted by x ascending, we want clockwise for lower hull
                cross = (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0])
                if cross >= 0:  # keeping lower hull (non-positive?) let's test: for lower envelope we need to discard when point is above line. Use standard Andrew: lower hull removes last while cross <= 0.
                    break
                lower.pop()
            lower.append(p)
        return lower

    def hull_value_at(x, hull):
        # hull is list of points (x,y) from left to right
        for i in range(len(hull)-1):
            x1,y1 = hull[i]
            x2,y2 = hull[i+1]
            if x1 <= x <= x2:
                if x2 == x1:
                    return y1
                return y1 + (y2 - y1)*(x - x1)/(x2 - x1)
        # fallback
        return 0.0

    expected = step.get('expected_hull', {})
    tolerance = step.get('tolerance_enthalpy', 0.02)

    pressures = [25, 50, 100]
    scores = []
    for pres in pressures:
        if pres not in points_by_pressure:
            scores.append(0.0)
            continue
        pts = points_by_pressure[pres]
        hull = lower_hull(pts)
        exp_comps = expected.get(str(pres), [])
        if not exp_comps:
            scores.append(1.0)
            continue
        def frac(comp):
            if comp.endswith('Si'):
                parts = comp.split('Si')
                if parts[0] == 'Li': nLi = 1
                else: nLi = int(parts[0][2:])
                nSi = int(parts[1]) if parts[1] else 1
                return nLi/(nLi+nSi)
            return 0.0
        # build lookup for enthalpies
        enth_map = {comp: y for comp,y in pts}
        correct = 0
        for exp in exp_comps:
            if exp not in enth_map:
                continue
            y_agent = enth_map[exp]
            x = frac(exp)
            hull_y = hull_value_at(x, hull)
            if y_agent <= hull_y + tolerance:
                correct += 1
        scores.append(correct / len(exp_comps))
    return sum(scores)/len(scores)


# === block: score_1 (check id='phonon') ===
def score_1(artifact, step, ctx):
    lines = artifact.strip().splitlines()
    threshold = step.get('min_freq_threshold', -0.5)
    expected_flag = step.get('expected_flag', 'IMAGINARY_no')
    freq = None
    flag = None
    for line in lines:
        if line.startswith('# MIN_FREQ'):
            parts = line.split()
            if len(parts) >= 3:
                try:
                    freq = float(parts[1])
                except ValueError:
                    return 0.0
                flag = parts[2]
            break
    if freq is None or flag is None:
        return 0.0
    if flag != expected_flag:
        return 0.0
    if freq <= threshold:
        return 0.0
    return 1.0


# === block: score_2 (check id='transition_pressure') ===
def score_2(artifact, step, ctx):
    val = artifact.strip()
    try:
        pres = float(val)
    except ValueError:
        return 0.0
    ref = step['reference']
    tol = step['tolerance']
    if abs(pres - ref) <= tol:
        return 1.0
    return 0.0


_SCORERS = {
    'formation_enthalpies': score_0,
    'phonon': score_1,
    'transition_pressure': score_2,
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
