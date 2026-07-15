import os
import json
import csv

# === author imports / helpers ===
import csv, io, math, re, statistics, itertools


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


# === block: score_0 (check id='density_check') ===
def score_0(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step.get('params', {})
        if not artifact:
            return 0.0
        # Group rows by salinity
        grouped = {}
        for row in artifact:
            try:
                sal = row['salinity'].strip()
                z = float(row['z'])
                ow = float(row['Ow_density'])
                hw = float(row['Hw_density'])
                bz = float(row['Bz_density'])
                na_ = float(row['Na_density'])
                cl_ = float(row['Cl_density'])
            except (KeyError, TypeError, ValueError):
                continue
            grouped.setdefault(sal, []).append((z, ow, hw, bz, na_, cl_))
        # Needs all three salinities
        for s in params.get('salinity_order',[]):
            if s not in grouped:
                return 0.0
        # Helper: find first peak in a list of (x,y) after min_x
        def first_peak_max(points, min_x):
            candidates = [(x,y) for x,y in points if x >= min_x]
            if not candidates:
                return None, None
            # naive: point with highest y
            idx = max(range(len(candidates)), key=lambda i: candidates[i][1])
            return candidates[idx]
        # Score components
        checks = []
        # Check 1: Ow first peak position
        for sal in params['salinity_order']:
            pts = [(z, ow) for z,ow,_,_,_,_ in grouped[sal]]
            peak_z, peak_val = first_peak_max(pts, 0.5)
            if peak_z is None:
                checks.append(0.0)
            else:
                lo, hi = params.get('ow_first_peak_range_A', [2.0,3.0])
                checks.append(1.0 if lo <= peak_z <= hi else 0.0)
        # Check 2: benzoate peak beyond hydration layer
        for sal in params['salinity_order']:
            pts_bz = [(z, bz) for z,_,_,bz,_,_ in grouped[sal]]
            bz_peak_z, bz_peak_val = first_peak_max(pts_bz, params.get('bz_peak_min_z_A',5.0))
            if bz_peak_z is None:
                checks.append(0.0)
            else:
                checks.append(1.0 if bz_peak_z >= params.get('bz_peak_min_z_A',5.0) else 0.0)
        # Check 3: benzoate peak height increases with salinity (monotonic)
        bz_peaks = []
        for sal in params['salinity_order']:
            pts_bz = [(z, bz) for z,_,_,bz,_,_ in grouped[sal]]
            _, bz_val = first_peak_max(pts_bz, params.get('bz_peak_min_z_A',5.0))
            bz_peaks.append(bz_val if bz_val else 0.0)
        mono = all(bz_peaks[i] < bz_peaks[i+1] for i in range(len(bz_peaks)-1))
        checks.append(1.0 if mono else 0.0)
        # Check 4: Na+ first peak close to Ow first peak (within proximity)
        for sal in params['salinity_order']:
            ow_pts = [(z, ow) for z,ow,_,_,_,_ in grouped[sal]]
            ow_peak_z, _ = first_peak_max(ow_pts, 0.5)
            na_pts = [(z, na_) for z,_,_,_,na_,_ in grouped[sal]]
            na_peak_z, _ = first_peak_max(na_pts, 0.5)
            if ow_peak_z is None or na_peak_z is None:
                checks.append(0.0)
            else:
                checks.append(1.0 if abs(na_peak_z - ow_peak_z) < params.get('na_peak_proximity_A',2.0) else 0.0)
        # Check 5: Cl- peak further than Na+ peak
        for sal in params['salinity_order']:
            na_pts = [(z, na_) for z,_,_,_,na_,_ in grouped[sal]]
            na_peak_z, _ = first_peak_max(na_pts, 0.5)
            cl_pts = [(z, cl_) for z,_,_,_,_,cl_ in grouped[sal]]
            cl_peak_z, _ = first_peak_max(cl_pts, 0.5)
            if na_peak_z is None or cl_peak_z is None:
                checks.append(0.0)
            else:
                checks.append(1.0 if cl_peak_z > na_peak_z else 0.0)
        if not checks:
            return 0.0
        return sum(checks) / len(checks)


# === block: score_1 (check id='rdf_nabz_check') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step.get('params', {})
        if not artifact:
            return 0.0
        grouped = {}
        for row in artifact:
            sal = row.get('salinity','').strip()
            try:
                r = float(row.get('r',0))
                g = float(row.get('g_r',0))
            except:
                continue
            grouped.setdefault(sal, []).append((r, g))
        # require all salinities
        for s in params.get('peak_height_order',[]):
            if s not in grouped:
                return 0.0
        # find first peak in g(r) after r>0.5
        def first_peak_g(points, min_r=0.5):
            cand = [(r,g) for r,g in points if r >= min_r]
            if not cand:
                return None, None
            idx = max(range(len(cand)), key=lambda i: cand[i][1])
            return cand[idx]
        checks = []
        # peak position for each salinity
        for sal in params['peak_height_order']:
            r_peak, g_peak = first_peak_g(grouped[sal])
            if r_peak is None:
                checks.append(0.0)
            else:
                lo, hi = params.get('peak_pos_range_A', [4.2, 4.8])
                checks.append(1.0 if lo <= r_peak <= hi else 0.0)
        # peak height order: LS > SW > DW
        heights = {}
        for sal in params['peak_height_order']:
            _, g_peak = first_peak_g(grouped[sal])
            heights[sal] = g_peak if g_peak is not None else 0.0
        order = params['peak_height_order']
        satisfied = (heights[order[0]] >= heights[order[1]] * (1 - params.get('tolerance_ratio',0.1))) and \
                    (heights[order[1]] >= heights[order[2]] * (1 - params.get('tolerance_ratio',0.1)))
        checks.append(1.0 if satisfied else 0.0)
        return sum(checks) / len(checks)


# === block: score_2 (check id='rdf_naow_check') ===
def score_2(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step.get('params', {})
        if not artifact:
            return 0.0
        grouped = {}
        for row in artifact:
            sal = row.get('salinity','').strip()
            try:
                r = float(row.get('r',0))
                g = float(row.get('g_r',0))
            except:
                continue
            grouped.setdefault(sal, []).append((r, g))
        # require at least DW, LS, SW? but we can check any present
        if len(grouped) == 0:
            return 0.0
        checks = []
        for sal, pts in grouped.items():
            cand = [(r,g) for r,g in pts if r >= 0.5]
            if not cand:
                checks.append(0.0)
                continue
            idx = max(range(len(cand)), key=lambda i: cand[i][1])
            r_peak, g_peak = cand[idx]
            lo, hi = params.get('peak_pos_range_A', [2.1, 2.7])
            pos_ok = lo <= r_peak <= hi
            height_ok = g_peak >= params.get('min_peak_height', 1.0)
            checks.append(1.0 if pos_ok and height_ok else 0.0)
        return sum(checks) / len(checks)


# === block: score_3 (check id='survival_check') ===
def score_3(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step.get('params', {})
        if not artifact:
            return 0.0
        grouped = {}
        for row in artifact:
            sal = row.get('salinity','').strip()
            try:
                t = float(row.get('time',0))
                p = float(row.get('p_t',0))
            except:
                continue
            grouped.setdefault(sal, []).append((t, p))
        # need all three salinities
        order = params.get('salinity_order', ['DW','LS','SW'])
        for s in order:
            if s not in grouped:
                return 0.0
        checks = []
        # area under curve (simple trapezoidal) as pseudo residence time
        def auc(pts):
            pts_sorted = sorted(pts, key=lambda x: x[0])
            area = 0.0
            for i in range(1, len(pts_sorted)):
                dt = pts_sorted[i][0] - pts_sorted[i-1][0]
                if dt < 0: dt = 0
                avg = (pts_sorted[i][1] + pts_sorted[i-1][1]) / 2.0
                area += avg * dt
            return area
        auc_dict = {}
        for sal in order:
            auc_dict[sal] = auc(grouped[sal])
        # check monotonic DW < LS < SW
        mono = (auc_dict[order[0]] < auc_dict[order[1]] < auc_dict[order[2]])
        checks.append(1.0 if mono else 0.0)
        # decay faster for DW: p_t at some time lower
        target_t = params.get('decay_time_ps', 50.0)
        p_at_t = {}
        for sal in order:
            pts = grouped[sal]
            # find closest time
            dist = min(pts, key=lambda x: abs(x[0]-target_t))
            p_at_t[sal] = dist[1]
        checks.append(1.0 if p_at_t[order[0]] < p_at_t[order[1]] < p_at_t[order[2]] else 0.0)
        return sum(checks) / len(checks)


# === block: score_4 (check id='residence_check') ===
def score_4(artifact, step, ctx):
    def score(artifact, step, ctx):
        params = step.get('params', {})
        if not artifact:
            return 0.0
        # parse as simple dict
        lookup = {}
        for row in artifact:
            sal = row.get('salinity','').strip()
            try:
                rt = float(row.get('residence_time',0))
            except:
                continue
            lookup[sal] = rt
        order = params.get('salinity_order', ['DW','LS','SW'])
        for s in order:
            if s not in lookup:
                return 0.0
        checks = []
        # monotonic
        mono = (lookup[order[0]] < lookup[order[1]] < lookup[order[2]])
        checks.append(1.0 if mono else 0.0)
        # consistency with survival integration would require cross-artifact, skip for simplicity; just weight 0.1 total
        # we can award 0.5 for each condition? But we need sum of checks to be 1 if both true. Here we have one check (mono). If true return 1.0 else 0.0.
        return 1.0 if mono else 0.0


_SCORERS = {
    'density_check': score_0,
    'rdf_nabz_check': score_1,
    'rdf_naow_check': score_2,
    'survival_check': score_3,
    'residence_check': score_4,
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
