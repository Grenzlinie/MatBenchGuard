import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='gxs') ===
def score_0(artifact, step, ctx):
    if not artifact or len(artifact) == 0: return 0.0
    mixture_groups = {}
    for row in artifact:
        mix = row['mixture']
        x_str = row['mole_fraction_H2']
        if x_str is None: continue
        try:
            x = float(x_str)
            v = float(row['G_xs'])
        except: continue
        mixture_groups.setdefault(mix, []).append((x, v))
    gold_curves = step['gold_curves']
    tolerances = step['tolerances']
    scores = []
    for mix in ['H2-He','H2-Ne','H2-Ar']:
        gold = gold_curves.get(mix)
        pts = mixture_groups.get(mix)
        if gold is None or pts is None or len(pts) < 11:
            scores.append(0.0)
            continue
        pts.sort()
        nx = len(pts)
        if nx != 11:
            scores.append(0.0)
            continue
        # verify composition grid 0.0 to 1.0 in 11 steps
        ok = True
        for i in range(nx):
            expected_x = round(i/10, 2)
            if abs(pts[i][0] - expected_x) > 1e-4:
                ok = False
                break
        if not ok:
            scores.append(0.0)
            continue
        squared_errors = []
        for i in range(nx):
            observed = pts[i][1]
            expected = gold[i]
            squared_errors.append((observed - expected) ** 2)
        rmsd = math.sqrt(sum(squared_errors) / nx)
        tol_hi = tolerances.get(mix, 0.5)
        if rmsd <= 1e-6:
            score = 1.0
        else:
            score = max(0.0, 1.0 - rmsd / tol_hi)
        scores.append(score)
    return sum(scores) / len(scores)


# === block: score_1 (check id='sxs') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact) == 0: return 0.0
    mixture_groups = {}
    for row in artifact:
        mix = row['mixture']
        x_str = row['mole_fraction_H2']
        if x_str is None: continue
        try:
            x = float(x_str)
            v = float(row['S_xs'])
        except: continue
        mixture_groups.setdefault(mix, []).append((x, v))
    gold_curves = step['gold_curves']
    tolerances = step['tolerances']
    scores = []
    for mix in ['H2-He','H2-Ne','H2-Ar']:
        gold = gold_curves.get(mix)
        pts = mixture_groups.get(mix)
        if gold is None or pts is None or len(pts) < 11:
            scores.append(0.0)
            continue
        pts.sort()
        nx = len(pts)
        if nx != 11:
            scores.append(0.0)
            continue
        ok = True
        for i in range(nx):
            expected_x = round(i/10, 2)
            if abs(pts[i][0] - expected_x) > 1e-4:
                ok = False
                break
        if not ok:
            scores.append(0.0)
            continue
        squared_errors = []
        for i in range(nx):
            observed = pts[i][1]
            expected = gold[i]
            squared_errors.append((observed - expected) ** 2)
        rmsd = math.sqrt(sum(squared_errors) / nx)
        tol_hi = tolerances.get(mix, 0.1)
        if rmsd <= 1e-6:
            score = 1.0
        else:
            score = max(0.0, 1.0 - rmsd / tol_hi)
        scores.append(score)
    return sum(scores) / len(scores)


# === block: score_2 (check id='scc') ===
def score_2(artifact, step, ctx):
    if not artifact or len(artifact) == 0: return 0.0
    anchor_points = step['anchor_points']
    tolerance = step.get('tolerance', 0.2)
    # build lookup: (mix, T, p) -> S_cc_star
    lookup = {}
    for row in artifact:
        mix = row['mixture']
        try:
            T = float(row['temperature_K'])
            p = float(row['pressure_GPa'])
            val = float(row['S_cc_star'])
        except:
            continue
        lookup.setdefault(mix, {})[(round(T,4), round(p,4))] = val

    scores_per_mix = {}
    for mix in ['H2-He','H2-Ne','H2-Ar']:
        gold_pts = anchor_points.get(mix)
        if gold_pts is None:
            scores_per_mix[mix] = 0.0
            continue
        devs = []
        for T, p, gold_val in gold_pts:
            key = (round(T,4), round(p,4))
            if key not in lookup.get(mix, {}):
                devs.append(1.0)  # missing point -> worst deviation
            else:
                diff = abs(lookup[mix][key] - gold_val)
                devs.append(min(1.0, diff / tolerance))
        if not devs:
            scores_per_mix[mix] = 0.0
        else:
            avg_dev = sum(devs) / len(devs)
            scores_per_mix[mix] = max(0.0, 1.0 - avg_dev)

    # structural ordering at T=150 K, p=1.0 GPa
    ordering_ok = False
    keys = {}
    for mix in ['H2-He','H2-Ne','H2-Ar']:
        k = (150.0, 1.0)
        if k in lookup.get(mix, {}):
            keys[mix] = lookup[mix][k]
    if len(keys) == 3:
        if keys['H2-Ar'] < keys['H2-Ne'] < keys['H2-He']:
            ordering_ok = True

    # average score over mixtures
    base_score = sum(scores_per_mix.values()) / 3.0
    final_score = base_score * 0.9 + (0.1 if ordering_ok else 0.0)
    return final_score


_SCORERS = {
    'gxs': score_0,
    'sxs': score_1,
    'scc': score_2,
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
