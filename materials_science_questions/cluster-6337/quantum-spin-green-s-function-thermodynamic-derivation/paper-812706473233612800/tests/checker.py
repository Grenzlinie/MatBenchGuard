import os
import json
import csv

# === author imports / helpers ===
import csv, math, os


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


# === block: score_0 (check id='tc_values') ===
def score_0(artifact, step, ctx):
    import csv, math
    rows = list(csv.DictReader(open(os.path.join('/app/outputs','tc_values.csv'))))
    if len(rows) < 10:
        return 0.0

    def get_tcs(form):
        d_to_tc = {}
        for r in rows:
            if r.get('formulation','').strip().upper() == form:
                try:
                    d_to_tc[float(r['D_div_J'])] = float(r['Tc'])
                except:
                    pass
        return d_to_tc

    req_ds = [-2.0, -1.6, -1.5, 0.0, 2.0]
    tc_A = get_tcs('A')
    tc_B = get_tcs('B')

    score = 0.0
    if not tc_A or not tc_B:
        return score

    # presence of both formulations
    score += 0.1

    # correct D set
    if set(req_ds).issubset(tc_A.keys()) and set(req_ds).issubset(tc_B.keys()):
        score += 0.1

    # D=0 check
    if 0.0 in tc_A and abs(tc_A[0.0] - 2.9188) <= 0.05:
        score += 0.2
    if 0.0 in tc_B and abs(tc_B[0.0] - 2.9556) <= 0.05:
        score += 0.2

    # monotonic trend for negative D: Tc(-2.0) <= Tc(-1.6) <= Tc(-1.5) <= Tc(0.0)
    for form, data in [('A',tc_A),('B',tc_B)]:
        vals = []
        for d in [-2.0, -1.6, -1.5, 0.0]:
            if d in data:
                vals.append(data[d])
        if len(vals)==4 and vals[0]<=vals[1]<=vals[2]<=vals[3]:
            score += 0.1

    # D=2.0 < D=0
    if 2.0 in tc_A and 0.0 in tc_A and tc_A[2.0] < tc_A[0.0] - 0.01:
        score += 0.05
    if 2.0 in tc_B and 0.0 in tc_B and tc_B[2.0] < tc_B[0.0] - 0.01:
        score += 0.05

    return min(1.0, score)


# === block: score_1 (check id='specific_heat_curves') ===
def score_1(artifact, step, ctx):
    import csv, math, os
    rows = list(csv.DictReader(open(os.path.join('/app/outputs','specific_heat_curves.csv'))))
    assert rows, 'empty'
    def get_curves():
        curves = {}
        for r in rows:
            form = r['formulation'].strip().upper()
            d = float(r['D_div_J'])
            t = float(r['T_div_Tc'])
            c = float(r['specific_heat'])
            key = (form,d)
            if key not in curves:
                curves[key] = []
            curves[key].append((t,c))
        for k in curves:
            curves[k].sort()
        return curves

    curves = get_curves()
    target_ds = [-2.0, -1.6, -1.5, 2.0]
    target_forms = ['A','B']

    n_curves = len(target_ds)*len(target_forms)
    per_curve_weight = 1.0 / n_curves
    score = 0.0

    def max_in_range(data, lo, hi):
        vals = [c for t,c in data if lo<=t<=hi]
        return max(vals) if vals else -1.0
    def min_in_range(data, lo, hi):
        vals = [c for t,c in data if lo<=t<=hi]
        return min(vals) if vals else -1.0

    for form in target_forms:
        for d in target_ds:
            key = (form,d)
            if key not in curves:
                continue
            pts = curves[key]
            if not pts: continue
            sub_score = 0.0
            if d == -2.0:
                # sharp peak at Tc: max C near 1.0 > C at 0.9 and 1.1 by at least 2
                max_c = max_in_range(pts, 0.99, 1.01)
                c09 = min([c for t,c in pts if 0.89<=t<=0.91], default=-1)
                c11 = min([c for t,c in pts if 1.09<=t<=1.11], default=-1)
                if max_c>0 and c09>=0 and max_c > c09+2 and max_c > c11+2:
                    sub_score += per_curve_weight
            elif d == -1.6:
                # broad maximum in low T: max in [0.4,0.6] > 1.2*min in [0.1,0.4] and [0.6,0.9]
                max_c = max_in_range(pts, 0.4, 0.6)
                min_lo = min_in_range(pts, 0.1, 0.4)
                min_hi = min_in_range(pts, 0.6, 0.9)
                if max_c>0 and min_lo>0 and min_hi>0 and max_c > 1.2*min_lo and max_c > 1.2*min_hi:
                    sub_score += per_curve_weight
            elif d == -1.5:
                # broad max near 0.5: same criterion
                max_c = max_in_range(pts, 0.4, 0.6)
                min_lo = min_in_range(pts, 0.1, 0.4)
                min_hi = min_in_range(pts, 0.6, 0.9)
                ok = (max_c>0 and min_lo>0 and min_hi>0 and max_c > 1.2*min_lo and max_c > 1.2*min_hi)
                if ok:
                    sub_score += 0.7*per_curve_weight  # base 70%
                # extra feature for A: dip and second max
                if form=='A':
                    min_dip = min_in_range(pts, 0.65, 0.75)
                    max2 = max_in_range(pts, 0.9, 1.0)
                    if max_c>0 and min_dip>=0 and max2>0 and min_dip < max_c and max2 > min_dip+0.1:
                        sub_score += 0.3*per_curve_weight
                else:
                    sub_score += 0.3*per_curve_weight  # B gets full per_curve_weight if the main check passed
                score += sub_score
            elif d == 2.0:
                # jump at Tc: C nearly zero below Tc-0.05, and >0.5 above Tc+0.05
                below = [c for t,c in pts if t<0.95]
                above = [c for t,c in pts if t>1.05]
                if below and max(below) < 0.05 and above and max(above) > 0.5:
                    sub_score += per_curve_weight
            score += sub_score

    return min(1.0, score)


# === block: score_2 (check id='internal_energy_order_params') ===
def score_2(artifact, step, ctx):
    import csv, math, os
    rows = list(csv.DictReader(open(os.path.join('/app/outputs','internal_energy_order_params.csv'))))
    assert rows, 'empty'
    def find_closest(rows, form, d_val, t_target=0.001):
        candidates = []
        for r in rows:
            try:
                if r['formulation'].strip().upper() == form and abs(float(r['D_div_J'])-d_val)<0.001:
                    t = float(r['T_div_Tc'])
                    u = float(r['U_div_J'])
                    m = float(r['m'])
                    q = float(r['q'])
                    rval_str = r.get('r','').strip()
                    rval = float(rval_str) if rval_str else None
                    candidates.append((abs(t-t_target), t, u, m, q, rval))
            except:
                pass
        if not candidates:
            return None
        candidates.sort()
        return candidates[0]

    score = 0.0
    # D=2.0
    for form in ['A','B']:
        row = find_closest(rows, form, 2.0)
        if row:
            dist, t, u, m, q, r = row
            if form == 'A':
                ok = (abs(u+7.875)<=0.01 and r is not None and abs(r-3.375)<=0.01 and abs(m-1.5)<=0.01 and abs(q-2.25)<=0.01)
            else:
                ok = (abs(u+7.875)<=0.01 and abs(m-1.5)<=0.01 and abs(q-2.25)<=0.01)
            if ok:
                score += 0.175

    # D=-2.0
    for form in ['A','B']:
        row = find_closest(rows, form, -2.0)
        if row:
            dist, t, u, m, q, r = row
            if form == 'A':
                ok = (abs(u-0.125)<=0.01 and r is not None and abs(r-0.125)<=0.01 and abs(m-0.5)<=0.01 and abs(q-0.25)<=0.01)
            else:
                ok = (abs(u-0.125)<=0.01 and abs(m-0.5)<=0.01 and abs(q-0.25)<=0.01)
            if ok:
                score += 0.175

    # D=-1.5
    for form in ['A','B']:
        row = find_closest(rows, form, -1.5)
        if row:
            dist, t, u, m, q, r = row
            if abs(u-0.0) <= 0.01:
                score += 0.15

    return min(1.0, score)


_SCORERS = {
    'tc_values': score_0,
    'specific_heat_curves': score_1,
    'internal_energy_order_params': score_2,
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
