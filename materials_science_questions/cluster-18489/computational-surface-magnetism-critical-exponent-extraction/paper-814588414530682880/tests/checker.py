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


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    try:
        by_r = {}
        for row in rows:
            delta_s = float(row['delta_s'])
            r = float(row['r'])
            t_c = float(row['t_c'])
            by_r.setdefault(r, []).append((delta_s, t_c))
    except (KeyError, ValueError):
        return 0.0
    # monotonic check
    mono_score = 0.0
    for r, points in by_r.items():
        points.sort(key=lambda x: x[0])
        ok = True
        for i in range(1, len(points)):
            if points[i][1] < points[i-1][1] - 1e-6:
                ok = False
                break
        if ok:
            mono_score += 1.0
    if by_r:
        mono_score /= len(by_r)
    # ordering check: for each delta_s present in both r=0.0 and 1.5, check t_c(r=1.5) >= t_c(r=0.0)
    r0 = by_r.get(0.0, [])
    r15 = by_r.get(1.5, [])
    if not r0 or not r15:
        order_score = 0.0
    else:
        d0 = {p[0]:p[1] for p in r0}
        d15 = {p[0]:p[1] for p in r15}
        common = set(d0.keys()) & set(d15.keys())
        if not common:
            order_score = 0.0
        else:
            ok = 0
            total = 0
            for d in common:
                if d15[d] >= d0[d] - 1e-6:
                    ok += 1
                total += 1
            order_score = ok / total if total else 0.0
    # final score
    return 0.5 * mono_score + 0.5 * order_score


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    try:
        by_ds = {}
        for row in rows:
            r = float(row['r'])
            delta_s = float(row['delta_s'])
            t_c = float(row['t_c'])
            by_ds.setdefault(delta_s, []).append((r, t_c))
    except (KeyError, ValueError):
        return 0.0
    mono_score = 0.0
    for ds, points in by_ds.items():
        points.sort(key=lambda x: x[0])
        ok = True
        for i in range(1, len(points)):
            if points[i][1] < points[i-1][1] - 1e-6:
                ok = False
                break
        if ok:
            mono_score += 1.0
    if by_ds:
        mono_score /= len(by_ds)
    # ordering: for each r, t_c(delta_s=1.5) >= t_c(delta_s=0.0)
    ds0 = by_ds.get(0.0, [])
    ds15 = by_ds.get(1.5, [])
    if not ds0 or not ds15:
        order_score = 0.0
    else:
        r0 = {p[0]:p[1] for p in ds0}
        r15 = {p[0]:p[1] for p in ds15}
        common = set(r0.keys()) & set(r15.keys())
        if not common:
            order_score = 0.0
        else:
            ok = 0
            total = 0
            for r in common:
                if r15[r] >= r0[r] - 1e-6:
                    ok += 1
                total += 1
            order_score = ok / total if total else 0.0
    return 0.5 * mono_score + 0.5 * order_score


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    try:
        by_r = {}
        for row in rows:
            r = float(row['r'])
            q = float(row['q'])
            t_c = float(row['t_c'])
            by_r.setdefault(r, []).append((q, t_c))
    except (KeyError, ValueError):
        return 0.0

    def is_monotonic_decreasing(points):
        # sorted by q
        vals = [p[1] for p in sorted(points, key=lambda x: x[0])]
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1] + 1e-6:
                return False
        return True

    def has_non_monotonic_increase(points):
        vals = [p[1] for p in sorted(points, key=lambda x: x[0])]
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1] + 1e-6:
                return True
        return False

    score = 0.0
    expected_r = [1.0, 3.0, 7.5]
    for r_val in expected_r:
        points = by_r.get(r_val, [])
        if not points:
            continue
        p_sorted = sorted(points, key=lambda x: x[0])
        q_first = p_sorted[0][1]
        q_last = p_sorted[-1][1]
        if r_val in [1.0, 3.0]:
            # requirement: monotonically decreasing, and first t_c > 0.1
            if is_monotonic_decreasing(points) and q_first > 0.1:
                score += 1.0 / 3.0
        else:  # r_val == 7.5, reentrant
            # non-monotonic (i.e., not decreasing everywhere) and t_c at q=0 > 0.1 and t_c at q=10 < 0.1
            if not is_monotonic_decreasing(points) and q_first > 0.1 and q_last < 0.1:
                score += 1.0 / 3.0
    return score


# === block: score_3 (check id='step4') ===
def score_3(artifact, step, ctx):
    if not artifact:
        return 0.0
    rows = artifact
    try:
        by_r = {}
        for row in rows:
            r = float(row['r'])
            t = float(row['t'])
            m_T = float(row['m_T'])
            by_r.setdefault(r, []).append((t, m_T))
    except (KeyError, ValueError):
        return 0.0

    def check_monotonic_decreasing(points, tol=1e-6):
        vals = [p[1] for p in sorted(points, key=lambda x: x[0])]
        for i in range(1, len(vals)):
            if vals[i] > vals[i-1] - tol:
                pass
            else:
                continue
            if vals[i] > vals[i-1] + tol:
                return False
        return True

    def has_peak(points):
        # returns True if there is a point that is a local maximum higher than both neighbours
        pts = sorted(points, key=lambda x: x[0])
        for i in range(1, len(pts)-1):
            if pts[i][1] > pts[i-1][1] + 1e-6 and pts[i][1] > pts[i+1][1] + 1e-6:
                return True
        return False

    score = 0.0
    # expected r groups
    for r_val in [1.0, 4.0, 7.0, 10.0]:
        points = by_r.get(r_val, [])
        if not points:
            continue
        pts_sorted = sorted(points, key=lambda x: x[0])
        t_first, m_first = pts_sorted[0]
        t_last, m_last = pts_sorted[-1]
        # basic: m_T in [0,1]
        valid = all(0.0 - 1e-4 <= p[1] <= 1.0 + 1e-4 for p in pts_sorted)
        if not valid:
            continue
        if r_val == 1.0:
            # normal: monotonic decrease, saturation >0.9, final zero
            if check_monotonic_decreasing(points) and m_first > 0.9 and m_last < 0.05:
                score += 0.25
        elif r_val == 4.0:
            # broad maximum: not monotonic, has peak, saturation >0.9, final zero
            if not check_monotonic_decreasing(points) and has_peak(points) and m_first > 0.9 and m_last < 0.05:
                score += 0.25
        elif r_val == 7.0:
            # similar: saturation >0.4, not monotonic, peak, final zero
            if not check_monotonic_decreasing(points) and has_peak(points) and m_first > 0.4 and m_last < 0.05:
                score += 0.25
        elif r_val == 10.0:
            # reentrant: starts near zero (<0.05), peak exists, peak >0.4, ends near zero
            if m_first < 0.05 and has_peak(points) and max(p[1] for p in pts_sorted) > 0.4 and m_last < 0.05:
                score += 0.25
    return score


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
    'step4': score_3,
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
