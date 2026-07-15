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
    import os, json, csv
    def load_artifact(path):
        if not os.path.exists(path):
            return None
        if path.endswith('.json'):
            with open(path) as f:
                return json.load(f)
        if path.endswith('.csv'):
            with open(path, newline='') as f:
                return list(csv.DictReader(f))
        return None

    # build reference dict for total_yields step from grading_spec
    ref_step = next((s for s in spec.get('steps',[]) if s.get('id')=='total_yields'), {})
    ref_dict = ref_step.get('reference', {})
    tol = ref_step.get('tolerance_relative', 0.15)
    return {'total_yields_ref': ref_dict, 'total_yields_tol': tol}


# === block: score_0 (check id='total_yields') ===
def score_0(artifact, step, ctx):
    ref = ctx['total_yields_ref']
    tol = ctx['total_yields_tol']
    expected_thicknesses = sorted([float(k) for k in ref.keys()])
    agent = {}
    for r in artifact:
        try:
            t = float(r['thickness'])
            agent[t] = {
                'total': float(r['total_yield']),
                'forward': float(r['forward_yield']),
                'backward': float(r['backward_yield'])
            }
        except:
            continue
    if not agent:
        return 0.0
    row_scores = []
    for t in expected_thicknesses:
        if t not in agent:
            row_scores.append(0.0)
            continue
        gold = ref[str(t)]
        vals = agent[t]
        if abs(vals['forward']+vals['backward'] - vals['total']) > 5.0:
            row_scores.append(0.0)
            continue
        rel_err = abs(vals['total'] - gold['total']) / gold['total'] if gold['total'] != 0 else 0
        if rel_err <= tol:
            row_scores.append(1.0)
        else:
            row_scores.append(max(0.0, 1.0 - (rel_err - tol) / tol))
    monotonic = True
    prev = None
    for t in sorted(agent.keys()):
        if prev is not None:
            if agent[t]['total'] < agent[prev]['total']:
                monotonic = False
                break
        prev = t
    monotonic_score = 1.0 if monotonic else 0.0
    avg_row = sum(row_scores)/len(row_scores) if row_scores else 0.0
    return 0.8 * avg_row + 0.2 * monotonic_score


# === block: score_1 (check id='yields_44_ugcm2') ===
def score_1(artifact, step, ctx):
    if not artifact or len(artifact)==0:
        return 0.0
    if not all(k in artifact[0] for k in ('energy_eV','angle_deg','yield')):
        return 0.0

    from collections import defaultdict
    import math

    by_angle = defaultdict(list)
    total_yield_sum = 0.0
    for r in artifact:
        try:
            e = float(r['energy_eV'])
            a = float(r['angle_deg'])
            y = float(r['yield'])
            if y < 0:
                return 0.0
            by_angle[a].append((e, y))
            total_yield_sum += y
        except:
            continue
    if total_yield_sum <= 0:
        return 0.0

    # find angle nearest to 40° within ±5°; use the closest
    TARGET_ANGLE = 40.0
    ANGLE_TOL_DEG = 5.0
    best_angle = None
    best_dist = float('inf')
    for a in by_angle:
        dist = abs(a - TARGET_ANGLE)
        if dist <= ANGLE_TOL_DEG and dist < best_dist:
            best_dist = dist
            best_angle = a

    if best_angle is None:
        return 0.2

    angle_40_data = by_angle[best_angle]
    if not angle_40_data:
        return 0.2

    # maximum yields in the two peak windows
    peak1 = max((y for e,y in angle_40_data if 4000.0 <= e <= 5000.0), default=0.0)
    peak2 = max((y for e,y in angle_40_data if 7000.0 <= e <= 8000.0), default=0.0)
    peak_score = 0.0
    if peak1 > 0:
        peak_score += 0.5
    if peak2 > 0:
        peak_score += 0.5

    # base score: data presence + shape check
    base_score = 0.5
    return 0.5 * base_score + 0.5 * peak_score


# === block: score_2 (check id='binary_peaks') ===
def score_2(artifact, step, ctx):
    try:
        data = artifact
        if not isinstance(data, dict):
            return 0.0
        t = data.get('foil_thickness_ugcm2')
        a = data.get('angle_deg')
        peaks = data.get('peak_energies_eV')
        if t != 44 or a != 40:
            return 0.0
        if not isinstance(peaks, list) or len(peaks) != 2:
            return 0.0
        gold = sorted(step['peak_energies_gold'])
        peaks_sorted = sorted(peaks)
        for g, p in zip(gold, peaks_sorted):
            if abs(p - g) > step['tolerance_eV']:
                return 0.0
        return 1.0
    except:
        return 0.0


# === block: score_3 (check id='time_resolved') ===
def score_3(artifact, step, ctx):
    if not artifact or len(artifact)==0:
        return 0.0
    # check columns
    if not all(k in artifact[0] for k in ('thickness','position_fraction','forward_percent','backward_percent')):
        return 0.0
    # build per thickness sorted list
    from collections import defaultdict
    by_t = defaultdict(list)
    for r in artifact:
        try:
            t = float(r['thickness'])
            pf = float(r['position_fraction'])
            fwd = float(r['forward_percent'])
            back = float(r['backward_percent'])
            if pf < 0 or pf > 1 or fwd < 0 or fwd > 100 or back < 0 or back > 100:
                continue
            by_t[int(t)].append((pf, fwd, back))
        except:
            continue
    required = [1,10,100]
    missing = [t for t in required if t not in by_t]
    if missing:
        return 0.0
    # For each thickness, sort by position_fraction and check structural properties
    checks_passed = 0
    total_checks = len(required)
    for t in required:
        points = sorted(by_t[t], key=lambda x: x[0])
        if len(points) < 2:
            continue
        # check endpoints: first pf near 0 with fwd~0,back~0; last pf near 1
        pf_first, fwd_first, back_first = points[0]
        pf_last, fwd_last, back_last = points[-1]
        if pf_first > 0.1 or pf_last < 0.9:
            continue
        if fwd_first > 5 or back_first > 5:
            continue
        # monotonic non-decreasing
        ok = True
        prev_pf, prev_fwd, prev_back = points[0]
        for pf, fwd, back in points[1:]:
            if fwd < prev_fwd - 0.1 or back < prev_back - 0.1:
                ok = False
                break
            prev_fwd, prev_back = fwd, back
        if not ok:
            continue
        # approximate exit fractions from paper:
        # 1 µg/cm²: fwd around 12%, back near 100% (very low? paper suggests backward emitted after exit, so backward at exit is low)
        # Actually paper: thin foil backward electrons emitted after projectile exit, so backward cumulative at exit is low.
        # For 100 µg/cm², forward around 75%, backward high.
        # We set generous ranges.
        if t == 1:
            if not (5 <= fwd_last <= 25):
                continue
            if not (0 <= back_last <= 30):
                continue
        elif t == 10:
            if not (30 <= fwd_last <= 70):
                continue
            if not (10 <= back_last <= 60):
                continue
        elif t == 100:
            if not (55 <= fwd_last <= 95):
                continue
            if not (55 <= back_last <= 100):
                continue
        checks_passed += 1
    return checks_passed / total_checks


_SCORERS = {
    'total_yields': score_0,
    'yields_44_ugcm2': score_1,
    'binary_peaks': score_2,
    'time_resolved': score_3,
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
