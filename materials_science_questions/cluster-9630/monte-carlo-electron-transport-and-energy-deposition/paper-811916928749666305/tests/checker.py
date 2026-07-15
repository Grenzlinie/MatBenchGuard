import os
import json
import csv

# === author imports / helpers ===
import math

def find_diameter(records, energy, distance, factor):
    """Return the diameter (cm) where dN_dS falls to on_axis/factor, or None."""
    sel = [(r, dn) for e,d,r,dn in records if e==energy and d==distance]
    if not sel:
        return None
    sel.sort(key=lambda x: x[0])
    on_axis = sel[0][1]
    if on_axis == 0:
        return None
    threshold = on_axis / factor
    # find first radius where dn <= threshold
    rad_interp = None
    for i in range(len(sel)-1):
        r0, dn0 = sel[i][0], sel[i][1]
        r1, dn1 = sel[i+1][0], sel[i+1][1]
        if dn1 <= threshold:
            if dn0 > threshold:
                t = (threshold - dn0) / (dn1 - dn0) if dn1 != dn0 else 0.0
                rad_interp = r0 + t * (r1 - r0)
            else:
                rad_interp = r0
            break
    if rad_interp is None:
        # beam never falls below threshold within the recorded range
        return None
    return 2.0 * rad_interp


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


# === block: score_0 (check id='coverage_check') ===
def score_0(artifact, step, ctx):
    if not artifact: return 0.0
    config = step.get('config', {})
    req_energies = set(config.get('required_energies', []))
    req_distances = set(config.get('required_distances', []))
    if not req_energies or not req_distances: return 0.0
    present = set()
    for row in artifact:
        try:
            e = int(float(row['energy_keV']))
            d = int(float(row['distance_cm']))
        except: continue
        if e in req_energies and d in req_distances:
            present.add((e,d))
    expected = len(req_energies) * len(req_distances)
    return 1.0 if len(present) == expected else 0.0


# === block: score_1 (check id='attenuation_check') ===
def score_1(artifact, step, ctx):
    if not artifact: return 0.0
    config = step.get('config', {})
    gold_atten = config.get('gold_attenuation', {})
    tolerance = config.get('tolerance', 0.3)
    initial_density = config.get('initial_on_axis_density', 1.0/math.pi)

    records = []
    for row in artifact:
        try:
            e = float(row['energy_keV'])
            d = float(row['distance_cm'])
            r = float(row['radius_cm'])
            dn = float(row['dN_dS'])
            records.append((e,d,r,dn))
        except: continue
    if not records: return 0.0

    total = 0.0
    count = 0
    for energy_str, gold_factor in gold_atten.items():
        energy = float(energy_str)
        sel = [(r,dn) for e,d,r,dn in records if e==energy and d==100.0]
        if not sel: continue
        sel.sort(key=lambda x: x[0])
        on_axis = sel[0][1]
        if on_axis <= 0: continue
        factor = initial_density / on_axis
        rel_err = abs(factor - gold_factor) / gold_factor if gold_factor != 0 else 0.0
        if rel_err <= tolerance:
            score = 1.0
        else:
            score = max(0.0, 1.0 - (rel_err - tolerance) / tolerance)
        total += score
        count += 1
    return total / count if count > 0 else 0.0


# === block: score_2 (check id='diameters_check') ===
def score_2(artifact, step, ctx):
    if not artifact: return 0.0
    config = step.get('config', {})
    combinations = config.get('combinations', [])

    records = []
    for row in artifact:
        try:
            e = float(row['energy_keV'])
            d = float(row['distance_cm'])
            r = float(row['radius_cm'])
            dn = float(row['dN_dS'])
            records.append((e,d,r,dn))
        except: continue
    if not records or not combinations: return 0.0

    total_score = 0.0
    for combo in combinations:
        energy = float(combo['energy'])
        dist = float(combo['distance'])
        gold_diam = float(combo['gold_diameter'])
        tol = float(combo['tolerance'])
        diam = find_diameter(records, energy, dist, 10.0)
        if diam is None:
            continue
        rel_err = abs(diam - gold_diam) / gold_diam if gold_diam != 0 else 0.0
        if rel_err <= tol:
            score = 1.0
        else:
            score = max(0.0, 1.0 - (rel_err - tol) / tol)
        total_score += score
    return total_score / len(combinations)


# === block: score_3 (check id='halfwidth_check') ===
def score_3(artifact, step, ctx):
    if not artifact: return 0.0
    config = step.get('config', {})
    gold_hw = config.get('gold_halfwidth_cm', {})
    tolerance = config.get('tolerance', 0.2)

    records = []
    for row in artifact:
        try:
            e = float(row['energy_keV'])
            d = float(row['distance_cm'])
            r = float(row['radius_cm'])
            dn = float(row['dN_dS'])
            records.append((e,d,r,dn))
        except: continue
    if not records: return 0.0

    total = 0.0
    count = 0
    for energy_str, gold_diam in gold_hw.items():
        energy = float(energy_str)
        diam = find_diameter(records, energy, 100.0, 2.0)  # half = on_axis/2
        if diam is None: continue
        rel_err = abs(diam - gold_diam) / gold_diam if gold_diam != 0 else 0.0
        if rel_err <= tolerance:
            score = 1.0
        else:
            score = max(0.0, 1.0 - (rel_err - tolerance) / tolerance)
        total += score
        count += 1
    return total / count if count > 0 else 0.0


# === block: score_4 (check id='monotonicity_check') ===
def score_4(artifact, step, ctx):
    if not artifact: return 0.0
    records = []
    for row in artifact:
        try:
            e = float(row['energy_keV'])
            d = float(row['distance_cm'])
            r = float(row['radius_cm'])
            dn = float(row['dN_dS'])
            records.append((e,d,r,dn))
        except: continue
    if not records: return 0.0

    # group by (energy, distance)
    from itertools import groupby
    records.sort(key=lambda x: (x[0], x[1], x[2]))
    total_profiles = 0
    monotonic_profiles = 0
    for (e,d), group in groupby(records, key=lambda x: (x[0], x[1])):
        rows = list(group)
        rows.sort(key=lambda x: x[2])
        prev_dn = None
        monotonic = True
        for _,_,r,dn in rows:
            if prev_dn is not None and dn > prev_dn + 1e-12:
                monotonic = False
                break
            prev_dn = dn
        total_profiles += 1
        if monotonic:
            monotonic_profiles += 1
    return monotonic_profiles / total_profiles if total_profiles > 0 else 0.0


_SCORERS = {
    'coverage_check': score_0,
    'attenuation_check': score_1,
    'diameters_check': score_2,
    'halfwidth_check': score_3,
    'monotonicity_check': score_4,
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
