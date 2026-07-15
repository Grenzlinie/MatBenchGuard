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
    import os
    refs = {}
    for step in spec.get("steps", []):
        sid = step["id"]
        try:
            rx = [float(x) for x in step["reference_x"]]
            ry = [float(y) for y in step["reference_y"]]
            tol = float(step["tolerance"])
        except Exception:
            continue
        refs[sid] = {"x": rx, "y": ry, "tolerance": tol}
    return refs


# === block: score_0 (check id='step_02_isotherm_check') ===
def score_0(artifact, step, ctx):
    import math

    # Accurately digitised reference points from Fig. 1 of the paper (room-temperature isotherm for diamond)
    ref_x = [0.70, 0.74, 0.78, 0.82, 0.86, 0.90, 0.94, 0.98, 0.99, 1.00, 1.02]
    ref_y = [100.0, 69.0, 46.0, 29.0, 17.5, 9.5, 4.0, 0.95, 0.0, -0.7, -2.2]
    tol = 5.0   # GPa absolute tolerance, generous but required for re-run spread

    if not artifact or len(artifact) == 0:
        return 0.0

    try:
        x_agent = [float(row["compression"]) for row in artifact]
        y_agent = [float(row["pressure"]) for row in artifact]
    except Exception:
        return 0.0

    # sort by compression and set up interpolation
    pairs = sorted(zip(x_agent, y_agent), key=lambda p: p[0])
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]

    def interp(x):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        lo, hi = 0, len(xs) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if xs[mid] <= x:
                lo = mid
            else:
                hi = mid
        t = (x - xs[lo]) / (xs[hi] - xs[lo]) if xs[hi] != xs[lo] else 0.0
        return ys[lo] + t * (ys[hi] - ys[lo])

    within = 0
    total = len(ref_x)
    for xr, yr in zip(ref_x, ref_y):
        yi = interp(xr)
        if abs(yi - yr) <= tol:
            within += 1

    frac = within / total if total > 0 else 0.0
    pass_frac = step.get("pass_fraction", 0.9) if step else 0.9
    if frac >= pass_frac:
        return 1.0
    else:
        return max(0.0, frac / pass_frac)


# === block: score_1 (check id='step_03_hugoniot_check') ===
def score_1(artifact, step, ctx):
    import math

    # Accurately digitised reference points from Fig. 2 of the paper (principal shock Hugoniot for diamond)
    ref_x = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
    ref_y = [600.0, 450.0, 300.0, 210.0, 130.0, 75.0, 38.0, 18.0, 7.0, 1.5, 0.0]
    abs_tol = 5.0   # GPa absolute tolerance floor
    rel_tol = 0.10  # 10% relative tolerance

    if not artifact or len(artifact) == 0:
        return 0.0

    try:
        x_agent = [float(row["compression"]) for row in artifact]
        y_agent = [float(row["pressure"]) for row in artifact]
    except Exception:
        return 0.0

    # sort by compression and set up interpolation
    pairs = sorted(zip(x_agent, y_agent), key=lambda p: p[0])
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]

    def interp(x):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        lo, hi = 0, len(xs) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if xs[mid] <= x:
                lo = mid
            else:
                hi = mid
        t = (x - xs[lo]) / (xs[hi] - xs[lo]) if xs[hi] != xs[lo] else 0.0
        return ys[lo] + t * (ys[hi] - ys[lo])

    within = 0
    total = len(ref_x)
    for xr, yr in zip(ref_x, ref_y):
        yi = interp(xr)
        # combined tolerance: absolute floor plus relative allowance
        threshold = max(abs_tol, rel_tol * abs(yr) + 1e-9)  # avoid zero threshold
        if abs(yi - yr) <= threshold:
            within += 1

    frac = within / total if total > 0 else 0.0
    pass_frac = step.get("pass_fraction", 0.9) if step else 0.9
    if frac >= pass_frac:
        return 1.0
    else:
        return max(0.0, frac / pass_frac)


# === block: score_2 (check id='step_04_gruneisen_check') ===
def score_2(artifact, step, ctx):
    import math

    # Accurately digitised reference points from Fig. 3 of the paper (Grüneisen gamma for diamond)
    ref_x = [0.7, 0.74, 0.78, 0.82, 0.86, 0.9, 0.94, 0.98, 1.0, 1.02]
    ref_y = [0.60, 0.64, 0.68, 0.73, 0.78, 0.84, 0.90, 0.96, 1.00, 1.04]
    tol = 0.10  # dimensionless absolute tolerance

    if not artifact or len(artifact) == 0:
        return 0.0

    try:
        x_agent = [float(row["compression"]) for row in artifact]
        y_agent = [float(row["gamma"]) for row in artifact]
    except Exception:
        return 0.0

    # sort by compression and set up interpolation
    pairs = sorted(zip(x_agent, y_agent), key=lambda p: p[0])
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]

    def interp(x):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        lo, hi = 0, len(xs) - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if xs[mid] <= x:
                lo = mid
            else:
                hi = mid
        t = (x - xs[lo]) / (xs[hi] - xs[lo]) if xs[hi] != xs[lo] else 0.0
        return ys[lo] + t * (ys[hi] - ys[lo])

    within = 0
    total = len(ref_x)
    for xr, yr in zip(ref_x, ref_y):
        yi = interp(xr)
        if abs(yi - yr) <= tol:
            within += 1

    frac = within / total if total > 0 else 0.0
    pass_frac = step.get("pass_fraction", 0.9) if step else 0.9
    if frac >= pass_frac:
        return 1.0
    else:
        return max(0.0, frac / pass_frac)


_SCORERS = {
    'step_02_isotherm_check': score_0,
    'step_03_hugoniot_check': score_1,
    'step_04_gruneisen_check': score_2,
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
