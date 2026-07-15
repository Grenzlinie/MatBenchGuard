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
    return {
      "beam_gold": {"400": 160.0, "350": 155.0, "300": 130.0, "250": 100.0},
      "hplus_gold_radius_350": 140.0
    }


# === block: score_0 (check id='step_03_beam_radii') ===
def score_0(artifact, step, ctx):
    rows = artifact
    gold = ctx["beam_gold"]
    tol = step.get("tolerance_rel", 0.20)
    found = {}
    for row in rows:
        alt_str = str(row.get("altitude_km", "")).strip()
        try:
            alt_val = float(alt_str)
        except ValueError:
            continue
        alt_int = int(round(alt_val))
        if abs(alt_val - alt_int) > 1e-6:
            continue
        alt_key = str(alt_int)
        try:
            r = float(row["beam_radius_km"])
        except (KeyError, ValueError):
            continue
        if alt_key in gold:
            found[alt_key] = r
    if not found:
        return 0.0
    score = 0.0
    for alt, g in gold.items():
        actual = found.get(alt)
        if actual is None:
            continue
        err = abs(actual - g) / g if g > 0 else float('inf')
        if err <= tol:
            score += 1.0
        else:
            partial = max(0.0, 1.0 - (err - tol) / tol)
            score += partial
    return score / len(gold)


# === block: score_1 (check id='step_04_flux_profile') ===
def score_1(artifact, step, ctx):
    rows = artifact
    gold_radius = ctx["hplus_gold_radius_350"]
    tol = step.get("tolerance_rel_radius", 0.20)
    sub_w = step.get("sub_weights", {"monotonic": 0.3, "radius_80": 0.7})

    points = []
    for row in rows:
      try:
        r = float(row["radial_distance_km"])
        f = float(row["downward_Hplus_flux"])
      except (KeyError, ValueError):
        continue
      if r < 0:
        continue
      points.append((r, f))
    if len(points) < 3:
      return 0.0
    points.sort(key=lambda x: x[0])
    radii = [p[0] for p in points]
    fluxes = [p[1] for p in points]

    # Monotonic check: flux must not increase with distance (non-increasing)
    mono_ok = True
    for i in range(1, len(fluxes)):
      if fluxes[i] > fluxes[i-1] + 1e-12:
        mono_ok = False
        break
    mono_score = 1.0 if mono_ok else 0.0

    # Compute cumulative flux (approximate using trapezoidal integration over 2π r dr)
    # Ensure we start from r=0 if present, else assume flux at 0 is highest
    cr = 0.0
    cf = 0.0
    prev_r = 0.0
    prev_f = fluxes[0]
    for r, f in points:
      # integrate from prev_r to r
      if r > prev_r:
        avg_f = (prev_f + f) / 2.0
        dr = r - prev_r
        cf += 2.0 * math.pi * prev_r * avg_f * dr  # approximate using ring area 2π r dr times average flux
      prev_r = r
      prev_f = f
    total = cf
    if total <= 0:
      return 0.0

    # Find radius where cumulative fraction reaches 0.8
    cum = 0.0
    prev_r = 0.0
    prev_f = fluxes[0]
    radius80 = None
    for i in range(len(points)):
      r = points[i][0]
      f = points[i][1]
      if i == 0:
        cum = 0.0
        radius80 = 0.0
        continue
      r0 = points[i-1][0]
      f0 = points[i-1][1]
      dr = r - r0
      if dr <= 0:
        continue
      avg_f = (f0 + f) / 2.0
      inc = 2.0 * math.pi * r0 * avg_f * dr
      if cum + inc >= 0.8 * total:
        # interpolate
        needed = 0.8 * total - cum
        fraction = needed / inc if inc > 0 else 0.0
        radius80 = r0 + fraction * dr
        break
      cum += inc
      prev_r = r
      prev_f = f

    if radius80 is None:
      # use last point as fallback
      radius80 = points[-1][0]

    radius_score = 0.0
    if gold_radius > 0:
      err = abs(radius80 - gold_radius) / gold_radius
      if err <= tol:
        radius_score = 1.0
      else:
        radius_score = max(0.0, 1.0 - (err - tol) / tol)

    return sub_w["monotonic"] * mono_score + sub_w["radius_80"] * radius_score


_SCORERS = {
    'step_03_beam_radii': score_0,
    'step_04_flux_profile': score_1,
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
