import os
import json
import csv

# === author imports / helpers ===
import math, bisect


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


# === block: score_0 (check id='passive_stress_relaxation') ===
def score_0(artifact, step, ctx):
    # artifact is a list of dicts with keys time, avg_pressure, solid_stress, total_stress
    times = []
    for row in artifact:
        try:
            t = float(row['time'])
            times.append(t)
        except:
            pass
    if not times or len(artifact) < 3:
        return 0.0

    # Find indices for target times
    def find_idx(target, times_list):
        if target <= times_list[0]:
            return 0
        if target >= times_list[-1]:
            return len(times_list)-1
        lo, hi = 0, len(times_list)-1
        while hi - lo > 1:
            mid = (lo+hi)//2
            if times_list[mid] <= target:
                lo = mid
            else:
                hi = mid
        # choose nearest
        if abs(times_list[lo]-target) <= abs(times_list[hi]-target):
            return lo
        else:
            return hi

    target = step['target']
    tol = step['tolerance']
    scores = []
    for i, tt in enumerate(target['time_points']):
        idx = find_idx(tt, times)
        # compute errors for each column
        e_p = abs(float(artifact[idx]['avg_pressure']) - target['avg_pressure'][i])
        e_s = abs(float(artifact[idx]['solid_stress']) - target['solid_stress'][i])
        e_tot = abs(float(artifact[idx]['total_stress']) - target['total_stress'][i])
        tol_p = tol['avg_pressure']
        tol_s = tol['solid_stress']
        tol_tot = tol['total_stress']
        # linear decay: score = max(0, 1 - error/tol) but clipped at error > 2*tol maps to 0
        def linear_score(e, tol):
            if e <= tol:
                return 1.0
            elif e >= 2*tol:
                return 0.0
            else:
                return 1.0 - (e - tol)/tol
        sp = linear_score(e_p, tol_p)
        ss = linear_score(e_s, tol_s)
        st = linear_score(e_tot, tol_tot)
        scores.append((sp+ss+st)/3.0)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_1 (check id='extract_pressure_case3') ===
def score_1(artifact, step, ctx):
    # artifact: list of dicts with time, pressure
    times = []
    for row in artifact:
        try:
            t = float(row['time'])
            times.append(t)
        except:
            pass
    if not times or len(artifact) < 2:
        return 0.0

    def find_idx(target, times_list):
        if target <= times_list[0]:
            return 0
        if target >= times_list[-1]:
            return len(times_list)-1
        lo, hi = 0, len(times_list)-1
        while hi - lo > 1:
            mid = (lo+hi)//2
            if times_list[mid] <= target:
                lo = mid
            else:
                hi = mid
        if abs(times_list[lo]-target) <= abs(times_list[hi]-target):
            return lo
        else:
            return hi

    target = step['target']
    tol = step['tolerance']['pressure']
    scores = []
    for i, tt in enumerate(target['time_points']):
        idx = find_idx(tt, times)
        e = abs(float(artifact[idx]['pressure']) - target['pressure'][i])
        if e <= tol:
            s = 1.0
        elif e >= 2*tol:
            s = 0.0
        else:
            s = 1.0 - (e - tol)/tol
        scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


# === block: score_2 (check id='extract_charge_density_case3') ===
def score_2(artifact, step, ctx):
    # artifact: list of dicts with x, charge_density
    xs = []
    for row in artifact:
        try:
            x = float(row['x'])
            xs.append(x)
        except:
            pass
    if not xs or len(artifact) < 2:
        return 0.0

    def find_idx(target, xs_list):
        if target <= xs_list[0]:
            return 0
        if target >= xs_list[-1]:
            return len(xs_list)-1
        lo, hi = 0, len(xs_list)-1
        while hi - lo > 1:
            mid = (lo+hi)//2
            if xs_list[mid] <= target:
                lo = mid
            else:
                hi = mid
        if abs(xs_list[lo]-target) <= abs(xs_list[hi]-target):
            return lo
        else:
            return hi

    target = step['target']
    tol = step['tolerance']['charge_density']
    scores = []
    for i, tx in enumerate(target['x_positions']):
        idx = find_idx(tx, xs)
        e = abs(float(artifact[idx]['charge_density']) - target['charge_density'][i])
        if e <= tol:
            s = 1.0
        elif e >= 2*tol:
            s = 0.0
        else:
            s = 1.0 - (e - tol)/tol
        scores.append(s)
    return sum(scores)/len(scores) if scores else 0.0


_SCORERS = {
    'passive_stress_relaxation': score_0,
    'extract_pressure_case3': score_1,
    'extract_charge_density_case3': score_2,
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
