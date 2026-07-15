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
    return {}


# === block: score_0 (check id='kde_pore_size') ===
def score_0(artifact, step, ctx):
    # Extract diameters and densities; find local maxima
    import math
    rows = artifact
    expected = step.get("expected_peaks", [])
    tol = step.get("tolerance_A", 0.5)
    dcol = step.get("diameter_column", "pore_diameter_A")
    vcol = step.get("density_column", "density")
    if not rows or not expected:
        return 0.0
    points = []
    for r in rows:
        try:
            x = float(r.get(dcol, math.nan))
            y = float(r.get(vcol, math.nan))
            if not math.isnan(x) and not math.isnan(y):
                points.append((x, y))
        except (ValueError, TypeError):
            pass
    points.sort(key=lambda p: p[0])
    if len(points) < 3:
        return 0.0
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    # detect local maxima by comparing immediate neighbours
    peak_diams = []
    for i in range(1, len(xs)-1):
        if ys[i] > ys[i-1] and ys[i] > ys[i+1]:
            peak_diams.append(xs[i])
    # match detected peaks to expected peaks within tolerance
    matched = 0
    for ref in expected:
        for pd in peak_diams:
            if abs(pd - ref) <= tol:
                matched += 1
                break
    score = matched / len(expected) if expected else 1.0
    return min(1.0, max(0.0, score))


# === block: score_1 (check id='pore_centers') ===
def score_1(artifact, step, ctx):
    # Check that exactly the expected labels exist in the file
    rows = artifact
    expected_labels = set(step.get("expected_labels", [1,2,3]))
    label_col = step.get("label_column", "pore_label")
    if not rows:
        return 0.0
    observed = set()
    for r in rows:
        try:
            lbl = int(r.get(label_col, -1))
            observed.add(lbl)
        except (ValueError, TypeError):
            pass
    if observed == expected_labels:
        return 1.0
    return 0.0


# === block: score_2 (check id='adsorption_isotherm') ===
def score_2(artifact, step, ctx):
    # Compute pressure at maximum derivative of loading w.r.t log10(p)
    import math
    rows = artifact
    pcol = step.get("pressure_column", "pressure_bar")
    lcol = step.get("loading_column", "loading_mmol_g")
    target_range = step.get("target_p_range", [0.02, 0.08])
    if not rows:
        return 0.0
    data = []
    for r in rows:
        try:
            p = float(r.get(pcol, math.nan))
            ld = float(r.get(lcol, math.nan))
            if not math.isnan(p) and not math.isnan(ld) and p > 0:
                data.append((p, ld))
        except (ValueError, TypeError):
            pass
    data.sort(key=lambda x: x[0])
    if len(data) < 2:
        return 0.0
    # finite difference of loading w.r.t log10(p)
    best_d = -1.0
    best_p = None
    for i in range(len(data)-1):
        p0, ld0 = data[i]
        p1, ld1 = data[i+1]
        dlog = math.log10(p1) - math.log10(p0)
        if dlog <= 0:
            continue
        dld = ld1 - ld0
        derivative = dld / dlog
        if derivative > best_d:
            best_d = derivative
            best_p = (p0 + p1) / 2.0
    if best_p is None:
        return 0.0
    if target_range[0] <= best_p <= target_range[1]:
        return 1.0
    return 0.0


# === block: score_3 (check id='pore_isotherms') ===
def score_3(artifact, step, ctx):
    # For each pore column, find step pressure and check it is within target range
    import math
    rows = artifact
    pcol = step.get("pressure_column", "pressure_bar")
    pore_cols = step.get("pore_columns", [])
    target_range = step.get("target_p_range", [0.02, 0.08])
    if not rows or not pore_cols:
        return 0.0
    def step_pressure(loading_column):
        data = []
        for r in rows:
            try:
                p = float(r.get(pcol, math.nan))
                ld = float(r.get(loading_column, math.nan))
                if not math.isnan(p) and not math.isnan(ld) and p > 0:
                    data.append((p, ld))
            except (ValueError, TypeError):
                pass
        data.sort(key=lambda x: x[0])
        if len(data) < 2:
            return None
        best_d = -1.0
        best_p = None
        for i in range(len(data)-1):
            p0, ld0 = data[i]
            p1, ld1 = data[i+1]
            dlog = math.log10(p1) - math.log10(p0)
            if dlog <= 0:
                continue
            dld = ld1 - ld0
            derivative = dld / dlog
            if derivative > best_d:
                best_d = derivative
                best_p = (p0 + p1) / 2.0
        return best_p

    passed = 0
    for col in pore_cols:
        sp = step_pressure(col)
        if sp is not None and target_range[0] <= sp <= target_range[1]:
            passed += 1
    score = passed / len(pore_cols) if pore_cols else 1.0
    return min(1.0, max(0.0, score))


# === block: score_4 (check id='radial_distribution') ===
def score_4(artifact, step, ctx):
    # Filter for requested pressure point and pore label, then find radius with max density
    import math
    rows = artifact
    target_pp = step.get("target_pressure_point", "P3")
    target_label = step.get("target_pore_label", 2)
    expected_peak = step.get("expected_peak_A", 12.0)
    tol = step.get("tolerance_A", 2.0)
    radius_col = step.get("radius_column", "radius_A")
    density_col = step.get("density_column", "density_arb")
    pressure_col = step.get("pressure_col", "pressure_point")
    label_col = step.get("label_col", "pore_label")
    if not rows:
        return 0.0
    best_radius = None
    best_density = -math.inf
    for r in rows:
        try:
            pp = str(r.get(pressure_col, "")).strip()
            lbl = int(r.get(label_col, -1))
            if pp != target_pp or lbl != target_label:
                continue
            rad = float(r.get(radius_col, math.nan))
            dens = float(r.get(density_col, math.nan))
            if not math.isnan(rad) and not math.isnan(dens):
                if dens > best_density:
                    best_density = dens
                    best_radius = rad
        except (ValueError, TypeError):
            pass
    if best_radius is None:
        return 0.0
    if abs(best_radius - expected_peak) <= tol:
        return 1.0
    return 0.0


_SCORERS = {
    'kde_pore_size': score_0,
    'pore_centers': score_1,
    'adsorption_isotherm': score_2,
    'pore_isotherms': score_3,
    'radial_distribution': score_4,
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
