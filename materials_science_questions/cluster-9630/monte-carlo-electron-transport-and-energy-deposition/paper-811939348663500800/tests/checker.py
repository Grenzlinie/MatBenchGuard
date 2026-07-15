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


# === block: score_0 (check id='energy_spectrum_check') ===
def score_0(artifact, step, ctx):
    min_energy = float(step.get("params", {}).get("min_energy_MeV", 30))
    for row in artifact:
        try:
            e = float(row.get("energy_MeV", -1))
            f = float(row.get("differential_flux", 0))
        except (ValueError, TypeError):
            continue
        if e >= min_energy and f > 0:
            return 1.0
    return 0.0


# === block: score_1 (check id='spatial_distribution_check') ===
def score_1(artifact, step, ctx):
    hwhm_min = float(step.get("params", {}).get("hwhm_min_km", 5))
    hwhm_max = float(step.get("params", {}).get("hwhm_max_km", 20))
    if len(artifact) < 2:
        return 0.0
    radii = []
    fluxes = []
    for row in artifact:
        try:
            r = float(row["radius_km"])
            f = float(row["flux_per_area"])
            radii.append(r)
            fluxes.append(f)
        except (ValueError, KeyError, TypeError):
            continue
    if not radii:
        return 0.0
    # assume sorted by radius ascending
    max_flux = max(fluxes)
    half = max_flux / 2.0
    hwhm = None
    for i in range(len(fluxes)):
        if fluxes[i] < half:
            if i == 0:
                # unlikely but just take radius at first point
                hwhm = radii[0]
            else:
                r1 = radii[i-1]
                f1 = fluxes[i-1]
                r2 = radii[i]
                f2 = fluxes[i]
                if f2 != f1:
                    hwhm = r1 + (half - f1) * (r2 - r1) / (f2 - f1)
                else:
                    hwhm = (r1 + r2) / 2.0
            break
    if hwhm is None:
        # never dropped below half: HWHM > maximum radius
        hwhm = radii[-1]
    if hwhm_min <= hwhm <= hwhm_max:
        return 1.0
    return 0.0


# === block: score_2 (check id='time_profile_check') ===
def score_2(artifact, step, ctx):
    sep_min = float(step.get("params", {}).get("peak_separation_min_ms", 5))
    sep_max = float(step.get("params", {}).get("peak_separation_max_ms", 15))
    ratio_min = float(step.get("params", {}).get("amplitude_ratio_min", 0.5))
    ratio_max = float(step.get("params", {}).get("amplitude_ratio_max", 2.0))
    if len(artifact) < 3:
        return 0.0
    times = []
    counts = []
    for row in artifact:
        try:
            t = float(row["time_ms"])
            c = float(row["count_rate"])
            times.append(t)
            counts.append(c)
        except (ValueError, KeyError, TypeError):
            continue
    if len(counts) < 3:
        return 0.0
    maxc = max(counts)
    if maxc == 0:
        return 0.0
    thresh = 0.1 * maxc
    peaks = []
    for i in range(1, len(counts)-1):
        if counts[i] >= thresh and counts[i] > counts[i-1] and counts[i] > counts[i+1]:
            peaks.append((times[i], counts[i]))
    if len(peaks) < 2:
        return 0.0
    peaks.sort(key=lambda x: x[1], reverse=True)
    p1 = peaks[0]
    p2 = peaks[1]
    # order by time
    t1, a1 = p1
    t2, a2 = p2
    if t1 > t2:
        t1, t2 = t2, t1
        a1, a2 = a2, a1
    sep = t2 - t1
    if a1 == 0:
        return 0.0
    ratio = a2 / a1
    cond1 = sep >= sep_min and sep <= sep_max
    cond2 = ratio >= ratio_min and ratio <= ratio_max
    if cond1 and cond2:
        return 1.0
    return 0.0


_SCORERS = {
    'energy_spectrum_check': score_0,
    'spatial_distribution_check': score_1,
    'time_profile_check': score_2,
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
