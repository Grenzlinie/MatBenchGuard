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


# === block: score_0 (check id='analyze_angle') ===
def score_0(artifact, step, ctx):
    grade = 0.0
    params = step.get('params', {})
    target = float(params.get('target_angle_deg', 78.0))
    cut_time = float(params.get('stabilization_time_ns', 100.0))
    tol = float(params.get('tolerance_deg', 5.0))

    perp_dev = []
    par_dev = []
    for row in artifact:
        t_str = row.get('time(ns)', '')
        if not t_str:
            continue
        try:
            t = float(t_str)
        except ValueError:
            continue
        if t < cut_time:
            continue
        for col, dev_list in [('angle_perp(deg)', perp_dev), ('angle_par(deg)', par_dev)]:
            v_str = row.get(col, '')
            try:
                v = float(v_str)
                dev_list.append(abs(v - target))
            except ValueError:
                pass

    if not perp_dev or not par_dev:
        return 0.0

    def rmse(devs):
        return math.sqrt(sum(d*d for d in devs) / len(devs))

    score_perp = max(0.0, 1.0 - rmse(perp_dev) / tol)
    score_par = max(0.0, 1.0 - rmse(par_dev) / tol)
    grade = (score_perp + score_par) / 2.0
    return grade


# === block: score_1 (check id='analyze_distance') ===
def score_1(artifact, step, ctx):
    params = step.get('params', {})
    p1_min = float(params.get('pair1_distance_min_nm', 0.05))
    p1_max = float(params.get('pair1_distance_max_nm', 0.30))
    p12_min = float(params.get('pair12_distance_min_nm', 3.0))
    p12_max = float(params.get('pair12_distance_max_nm', 4.2))
    monotonic_req = params.get('require_monotonic', True)

    perp_dists = []
    par_dists = []
    bp_map = {}
    for row in artifact:
        bp_str = row.get('base_pair', '')
        if not bp_str:
            continue
        try:
            bp = int(bp_str)
        except ValueError:
            continue
        d_perp = row.get('distance_perp(nm)', '')
        d_par  = row.get('distance_par(nm)', '')
        try:
            bp_map.setdefault(bp, []).append(bp)
            perp_dists.append((bp, float(d_perp)))
            par_dists.append((bp, float(d_par)))
        except ValueError:
            continue

    if not bp_map or 1 not in bp_map or 12 not in bp_map:
        return 0.0

    def check_monotonic(entries):
        # entries list of (bp, dist)
        entries.sort(key=lambda x: x[0])
        for i in range(1, len(entries)):
            if entries[i][1] < entries[i-1][1] - 0.001:
                return False
        return True

    def get_dist(entries, bp):
        for b, d in entries:
            if b == bp:
                return d
        return None

    p1_perp = get_dist(perp_dists, 1)
    p12_perp = get_dist(perp_dists, 12)
    p1_par = get_dist(par_dists, 1)
    p12_par = get_dist(par_dists, 12)

    if None in (p1_perp, p12_perp, p1_par, p12_par):
        return 0.0

    score = 0.0
    if p1_min <= p1_perp <= p1_max:
        score += 0.15
    if p12_min <= p12_perp <= p12_max:
        score += 0.15
    if p1_min <= p1_par <= p1_max:
        score += 0.15
    if p12_min <= p12_par <= p12_max:
        score += 0.15
    if monotonic_req:
        mono_perp = check_monotonic(perp_dists)
        mono_par = check_monotonic(par_dists)
        if mono_perp:
            score += 0.2
        if mono_par:
            score += 0.2
    else:
        score += 0.4
    return min(1.0, score)


# === block: score_2 (check id='analyze_energy') ===
def score_2(artifact, step, ctx):
    params = step.get('params', {})
    required_systems = params.get('required_systems', ['perp', 'par'])
    cutoff = params.get('cutoff', 4.0)
    vdw_min = params.get('vdw_min', -160.0)
    vdw_max = params.get('vdw_max', -80.0)
    ele_min = params.get('ele_min', -25.0)
    ele_max = params.get('ele_max', 25.0)
    total_min = params.get('total_min', -150.0)
    total_max = params.get('total_max', -90.0)

    sys_vals = {}
    for row in artifact:
        sys_name = row.get('system', '').strip().lower()
        if sys_name not in required_systems:
            continue
        try:
            d_cut = float(row.get('distance_cutoff(A)', ''))
            e_type = row.get('energy_type', '').strip().lower()
            val = float(row.get('value(kJ/mol)', ''))
        except (ValueError, TypeError):
            continue
        if abs(d_cut - cutoff) > 0.01:
            continue
        sys_vals.setdefault(sys_name, {})[e_type] = val

    score = 0.0
    for sys in required_systems:
        if sys not in sys_vals:
            continue
        vals = sys_vals[sys]
        vdw = vals.get('vdw')
        ele = vals.get('ele')
        total = vals.get('total')
        ok = 0
        if vdw is not None and vdw_min <= vdw <= vdw_max:
            ok += 1
        if ele is not None and ele_min <= ele <= ele_max:
            ok += 1
        if total is not None and total_min <= total <= total_max:
            ok += 1
        # also check that vdW magnitude dominates (optional, not always exact)
        if vdw is not None and ele is not None and abs(vdw) > abs(ele):
            ok += 0.5  # extra half point if vdW dominant
        score += ok / (4.0 * len(required_systems))  # max 1 per system
    return min(1.0, score)


# === block: score_3 (check id='final_angles') ===
def score_3(artifact, step, ctx):
    params = step.get('params', {})
    ref_angle = params.get('reference_angle_deg', 78.0)
    ref_tol = params.get('reference_tolerance_deg', 6.0)
    short_range = params.get('short_angle_range', [65.0, 75.0])
    systems_map = params.get('systems', {})
    if not systems_map:
        return 0.0

    angle_data = {}
    for row in artifact:
        sys = row.get('system', '').strip()
        if not sys:
            continue
        try:
            val = float(row.get('final_angle(deg)', ''))
        except (ValueError, TypeError):
            continue
        angle_data[sys] = val

    total_systems = len(systems_map)
    if total_systems == 0:
        return 0.0
    ok = 0
    for sys, sys_type in systems_map.items():
        if sys not in angle_data:
            continue
        val = angle_data[sys]
        if sys_type == 'reference':
            if abs(val - ref_angle) <= ref_tol:
                ok += 1
        elif sys_type == 'short':
            low, high = short_range
            if low <= val <= high:
                ok += 1
        else:
            # unknown type, skip
            pass
    return ok / total_systems if total_systems > 0 else 0.0


_SCORERS = {
    'analyze_angle': score_0,
    'analyze_distance': score_1,
    'analyze_energy': score_2,
    'final_angles': score_3,
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
