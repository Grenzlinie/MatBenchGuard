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
    ctx = {}
    for step in spec['steps']:
        ctx[step['id']] = step
    return ctx


# === block: score_0 (check id='transmittance_peaks') ===
def score_0(artifact, step, ctx):
    import csv, math
    rows = artifact
    if not rows or not rows[0]:
        return 0.0
    wavelengths = []
    transmittances = []
    for r in rows:
        try:
            wl = float(r['wavelength_nm'])
            t = float(r['transmittance_T'])
            wavelengths.append(wl)
            transmittances.append(t)
        except:
            return 0.0
    # Find local maxima
    peaks = []
    n = len(wavelengths)
    if n < 3:
        return 0.0
    for i in range(1, n-1):
        if transmittances[i] > transmittances[i-1] and transmittances[i] > transmittances[i+1]:
            if wavelengths[i] >= step['peak_search_range_nm'][0] and wavelengths[i] <= step['peak_search_range_nm'][1]:
                peaks.append((wavelengths[i], transmittances[i]))
    if not peaks:
        return 0.0
    expected = step['expected_peaks_nm']
    tol = step['wavelength_tolerance_nm']
    min_h = step['min_peak_height']
    def find_nearest(target, candidates):
        best = None
        best_d = float('inf')
        for p in candidates:
            if p[1] < min_h:
                continue
            d = abs(p[0] - target)
            if d < best_d:
                best_d = d
                best = p
        if best is None:
            return None, tol+1
        return best, best_d
    scores = []
    for exp_wl in expected:
        nearest, dist = find_nearest(exp_wl, peaks)
        if nearest is None:
            scores.append(0.0)
        else:
            scores.append(max(0.0, 1.0 - dist / tol))
    if not scores:
        return 0.0
    return sum(scores)/len(scores)


# === block: score_1 (check id='angular_beaming') ===
def score_1(artifact, step, ctx):
    import csv, math
    rows = artifact
    if not rows or not rows[0]:
        return 0.0
    data = {}
    for r in rows:
        try:
            wl = float(r['wavelength_nm'])
            ang = float(r['angle_deg'])
            I = float(r['intensity_I'])
        except:
            return 0.0
        if wl not in data:
            data[wl] = []
        data[wl].append((ang, I))
    wl_list = step['wavelengths_nm']
    if len(wl_list) != 2:
        return 0.0
    angle_tol = step['max_peak_angle_tolerance_deg']
    ratio_min = step['min_main_lobe_intensity_ratio']
    off_ang = step['off_angle_deg']
    total = 0.0
    count = 0
    for wl in wl_list:
        if wl not in data:
            continue
        points = data[wl]
        if not points:
            continue
        # find max intensity and corresponding angle
        max_I = -1
        max_angle = None
        for ang, I in points:
            if I > max_I:
                max_I = I
                max_angle = ang
        if max_angle is None or max_I <= 0:
            continue
        # score angle closeness (max_angle should be near 0)
        angle_err = abs(max_angle)
        angle_score = max(0.0, 1.0 - angle_err / (angle_tol * 2.5)) if angle_err <= angle_tol*2.5 else 0.0
        # score beaming ratio: I_max / I at off_angle
        I_off = 0.0
        n_off = 0
        for ang, I in points:
            if abs(ang - off_ang) < 1.0:
                I_off += I
                n_off += 1
        if n_off == 0:
            # fallback: interpolate or take closest
            best_d = float('inf')
            for ang, I in points:
                d = abs(ang - off_ang)
                if d < best_d:
                    best_d = d
                    I_off = I
            if best_d > 5:
                I_off = 1e-6
        ratio = max_I / max(I_off, 1e-12)
        ratio_score = min(1.0, ratio / ratio_min)
        wave_score = 0.5 * angle_score + 0.5 * ratio_score
        total += wave_score
        count += 1
    if count == 0:
        return 0.0
    return total / count


_SCORERS = {
    'transmittance_peaks': score_0,
    'angular_beaming': score_1,
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
