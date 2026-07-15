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


# === block: score_0 (check id='schema_check') ===
def score_0(artifact, step, ctx):
    return 1.0 if isinstance(artifact, dict) and all(k in artifact for k in ('sigma_vs_R','Gamma_vs_R','chi_int_vs_R','chi_ovl_vs_R_fixed_chi_int','organics_effect')) else 0.0


# === block: score_1 (check id='sigma_trend') ===
def score_1(artifact, step, ctx):
    arr = artifact.get('sigma_vs_R', [])
    if not arr:
        return 0.0
    groups = {}
    for item in arr:
        chi = item.get('chi_ovl')
        r = item.get('R_nm')
        s = item.get('sigma_dyne_cm')
        if chi is None or r is None or s is None:
            return 0.0
        groups.setdefault(chi, []).append((r, s))
    total = 0
    satisfied = 0
    for chi, points in groups.items():
        points.sort(key=lambda x: x[0])
        for i in range(len(points)-1):
            if points[i][0] < points[i+1][0]:
                total += 1
                if points[i][1] >= points[i+1][1] - 1e-9:
                    satisfied += 1
    return satisfied / total if total > 0 else 0.0


# === block: score_2 (check id='Gamma_trend') ===
def score_2(artifact, step, ctx):
    arr = artifact.get('Gamma_vs_R', [])
    if not arr:
        return 0.0
    groups = {}
    for item in arr:
        chi = item.get('chi_ovl')
        r = item.get('R_nm')
        g = item.get('Gamma_rel')
        if chi is None or r is None or g is None:
            return 0.0
        groups.setdefault(chi, []).append((r, g))
    total = 0
    satisfied = 0
    for chi, points in groups.items():
        points.sort(key=lambda x: x[0])
        for i in range(len(points)-1):
            if points[i][0] < points[i+1][0]:
                total += 1
                # larger R -> larger coverage, so point[i] <= point[i+1]
                if points[i][1] <= points[i+1][1] + 1e-9:
                    satisfied += 1
    return satisfied / total if total > 0 else 0.0


# === block: score_3 (check id='chi_int_trend') ===
def score_3(artifact, step, ctx):
    arr = artifact.get('chi_int_vs_R', [])
    if not arr:
        return 0.0
    groups = {}
    for item in arr:
        chi = item.get('chi_ovl')
        r = item.get('R_nm')
        c = item.get('chi_int')
        if chi is None or r is None or c is None:
            return 0.0
        groups.setdefault(chi, []).append((r, c))
    total = 0
    satisfied = 0
    for chi, points in groups.items():
        points.sort(key=lambda x: x[0])
        for i in range(len(points)-1):
            if points[i][0] < points[i+1][0]:
                total += 1
                # larger R -> larger chi_int
                if points[i][1] <= points[i+1][1] + 1e-9:
                    satisfied += 1
    return satisfied / total if total > 0 else 0.0


# === block: score_4 (check id='chi_ovl_trend') ===
def score_4(artifact, step, ctx):
    arr = artifact.get('chi_ovl_vs_R_fixed_chi_int', [])
    if not arr:
        return 0.0
    groups = {}
    for item in arr:
        chi = item.get('chi_int')
        r = item.get('R_nm')
        c = item.get('chi_ovl')
        if chi is None or r is None or c is None:
            return 0.0
        groups.setdefault(chi, []).append((r, c))
    total = 0
    satisfied = 0
    for chi, points in groups.items():
        points.sort(key=lambda x: x[0])
        for i in range(len(points)-1):
            if points[i][0] < points[i+1][0]:
                total += 1
                # larger R -> smaller chi_ovl, so point[i] >= point[i+1]
                if points[i][1] >= points[i+1][1] - 1e-9:
                    satisfied += 1
    return satisfied / total if total > 0 else 0.0


# === block: score_5 (check id='organics_trend') ===
def score_5(artifact, step, ctx):
    arr = artifact.get('organics_effect', [])
    if not arr:
        return 0.0
    # Group by Po
    po_groups = {}
    for item in arr:
        po = item.get('Po_Torr')
        r = item.get('R_nm')
        s = item.get('sigma_dyne_cm')
        if po is None or r is None or s is None:
            return 0.0
        po_groups.setdefault(po, {}).setdefault('points', []).append((r, s))
        # Also store Po-value for later cross-pressure check
    # Check monotonicity within each Po: larger R -> lower sigma
    sat = 0
    total = 0
    for po, grp in po_groups.items():
        pts = grp['points']
        pts.sort(key=lambda x: x[0])
        for i in range(len(pts)-1):
            if pts[i][0] < pts[i+1][0]:
                total += 1
                if pts[i][1] >= pts[i+1][1] - 1e-9:
                    sat += 1
    # Cross-pressure check: for each R, sigma should decrease with increasing Po
    # Build dict mapping R to list of (Po, sigma)
    r_dict = {}
    for item in arr:
        r = item['R_nm']
        r_dict.setdefault(r, []).append((item['Po_Torr'], item['sigma_dyne_cm']))
    for r, po_list in r_dict.items():
        po_list.sort(key=lambda x: x[0])  # increasing Po
        for i in range(len(po_list)-1):
            if po_list[i][0] < po_list[i+1][0]:
                total += 1
                if po_list[i][1] >= po_list[i+1][1] - 1e-9:
                    sat += 1
    return sat / total if total > 0 else 0.0


# === block: score_6 (check id='sigma_spot') ===
def score_6(artifact, step, ctx):
    arr = artifact.get('sigma_vs_R', [])
    if not arr:
        return 0.0
    config = step.get('config', {})
    points = config.get('points', [])
    if not points:
        return 0.0
    correct = 0
    for pt in points:
        chi = pt['chi_ovl']
        r_target = pt['R_nm']
        target_val = pt['target']
        tol = pt['tolerance']
        found = None
        for entry in arr:
            if math.isclose(entry.get('chi_ovl', -999), chi, abs_tol=1e-6) and math.isclose(entry.get('R_nm', -999), r_target, abs_tol=1e-6):
                found = entry.get('sigma_dyne_cm')
                break
        if found is not None and abs(found - target_val) <= tol:
            correct += 1
    return correct / len(points) if points else 0.0


_SCORERS = {
    'schema_check': score_0,
    'sigma_trend': score_1,
    'Gamma_trend': score_2,
    'chi_int_trend': score_3,
    'chi_ovl_trend': score_4,
    'organics_trend': score_5,
    'sigma_spot': score_6,
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
