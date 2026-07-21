import os
import json
import csv

# === author imports / helpers ===
import csv, os, math

def compute_loop_area_and_coercive(rows, field_key, mag_key):
    sorted_rows = sorted(rows, key=lambda r: float(r[field_key]))
    xs = [float(r[field_key]) for r in sorted_rows]
    ys = [float(r[mag_key]) for r in sorted_rows]
    # close loop
    xs.append(xs[0])
    ys.append(ys[0])
    area = 0.5 * abs(sum(xs[i]*ys[i+1] - xs[i+1]*ys[i] for i in range(len(xs)-1)))
    coercivity = None
    for i in range(len(sorted_rows)-1):
        y1 = float(sorted_rows[i][mag_key])
        y2 = float(sorted_rows[i+1][mag_key])
        if y1 < 0 and y2 >= 0:
            x1 = float(sorted_rows[i][field_key])
            x2 = float(sorted_rows[i+1][field_key])
            if y2 - y1 != 0:
                coercivity = x1 + (0 - y1) / (y2 - y1) * (x2 - x1)
            else:
                coercivity = (x1 + x2) / 2
            break
    if coercivity is None:
        coercivity = 0.0
    return area, coercivity


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
    ctx = {}
    nonint_path = os.path.join(outputs_dir, "hysteresis_noninteracting.csv")
    if os.path.isfile(nonint_path):
        with open(nonint_path, newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        groups = {}
        for r in rows:
            sig = int(r["sigma"])
            groups.setdefault(sig, []).append(r)
        if 15 in groups:
            area15, _ = compute_loop_area_and_coercive(groups[15], "field", "magnetization")
            ctx["nonint_area15"] = area15
    return ctx


# === block: score_0 (check id='hysteresis_noninteracting_shape') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = {}
    for r in artifact:
        sig = int(r["sigma"])
        groups.setdefault(sig, []).append(r)
    required = [2,5,15]
    if not all(s in groups for s in required):
        return 0.0

    def compute_loop_area_and_coercive(rows, field_key, mag_key):
        xs = [float(r[field_key]) for r in rows]
        ys = [float(r[mag_key]) for r in rows]
        # close loop if not already closed
        if len(xs) >= 2 and (abs(xs[0]-xs[-1]) > 1e-12 or abs(ys[0]-ys[-1]) > 1e-12):
            xs.append(xs[0])
            ys.append(ys[0])
        area = 0.5 * abs(sum(xs[i]*ys[i+1] - xs[i+1]*ys[i] for i in range(len(xs)-1)))
        coercivity = None
        for i in range(len(ys)-1):
            y1 = ys[i]
            y2 = ys[i+1]
            if y1 < 0 and y2 >= 0:
                x1 = xs[i]
                x2 = xs[i+1]
                if y2 - y1 != 0:
                    coercivity = x1 + (0 - y1) / (y2 - y1) * (x2 - x1)
                else:
                    coercivity = (x1 + x2) / 2
                break
        if coercivity is None:
            coercivity = 0.0
        return area, coercivity

    areas = []
    coercivities = []
    for s in required:
        area, coerc = compute_loop_area_and_coercive(groups[s], "field", "magnetization")
        areas.append(area)
        coercivities.append(coerc)
    eps = 1e-9
    area_inc = all(areas[i+1] > areas[i] + eps for i in range(len(areas)-1))
    coerc_inc = all(coercivities[i+1] > coercivities[i] + eps for i in range(len(coercivities)-1))
    max_mags = [max(abs(float(r["magnetization"])) for r in groups[s]) for s in required]
    mag_ok = all(m > 0.7 for m in max_mags)
    score = 0.0
    if area_inc:
        score += 0.3
    if coerc_inc:
        score += 0.3
    if mag_ok:
        score += 0.4
    return score


# === block: score_1 (check id='hysteresis_interacting_trend') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    groups = {}
    for r in artifact:
        n = int(r["num_particles"])
        groups.setdefault(n, []).append(r)
    required_n = [100,500,1000]
    if not all(n in groups for n in required_n):
        return 0.0
    areas = []
    coercivities = []
    for n in required_n:
        area, coerc = compute_loop_area_and_coercive(groups[n], "field", "magnetization")
        areas.append(area)
        coercivities.append(coerc)
    # monotonic
    eps = 1e-9
    area_inc = all(areas[i+1] > areas[i] + eps for i in range(len(areas)-1))
    coerc_inc = all(coercivities[i+1] > coercivities[i] + eps for i in range(len(coercivities)-1))
    # wider than noninteracting sigma=15
    nonint_area15 = ctx.get("nonint_area15")
    wider_ok = True
    if nonint_area15 is not None:
        wider_ok = all(a > nonint_area15 * 0.95 for a in areas)
    score = 0.0
    if area_inc:
        score += 0.2
    if coerc_inc:
        score += 0.2
    if wider_ok:
        score += 0.6
    return score


_SCORERS = {
    'hysteresis_noninteracting_shape': score_0,
    'hysteresis_interacting_trend': score_1,
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
