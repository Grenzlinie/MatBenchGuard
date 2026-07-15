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


# === block: score_0 (check id='step_reflection_spectra') ===
def score_0(artifact, step, ctx):
    import statistics

    rows = artifact
    if not rows or not isinstance(rows, list):
        return 0.0
    try:
        wavelengths = [float(r['wavelength']) for r in rows]
        refl_flat = [float(r['reflectivity_flat']) for r in rows]
        refl_rho8 = [float(r['reflectivity_rho8']) for r in rows]
        refl_rho2_9 = [float(r['reflectivity_rho2_9']) for r in rows]
    except (KeyError, ValueError, TypeError):
        return 0.0

    if len(wavelengths) < 10:
        return 0.0

    thresholds = step.get('thresholds', {})
    wl_min = float(thresholds.get('peak_wavelength_min', 0.5))
    wl_max = float(thresholds.get('peak_wavelength_max', 1.5))
    pk_min_flat = float(thresholds.get('peak_reflectivity_min_flat', 0.99))
    pk_min_rho8 = float(thresholds.get('peak_reflectivity_min_rho8', 0.99))
    pk_min_rho2_9 = float(thresholds.get('peak_reflectivity_min_rho2_9', 0.90))
    margin = float(thresholds.get('baseline_margin', 0.3))

    def analyze_spectrum(wl, refl):
        filtered_vals = []
        filtered_wls = []
        for i, w in enumerate(wl):
            if wl_min <= w <= wl_max:
                filtered_vals.append(refl[i])
                filtered_wls.append(w)
        if not filtered_vals:
            return None, None, None
        max_val = max(filtered_vals)
        max_idx = filtered_vals.index(max_val)
        peak_wl = filtered_wls[max_idx]
        baseline = statistics.median(refl) if refl else 0.0
        return max_val, peak_wl, baseline

    results = {}
    for name, refl in [('flat', refl_flat), ('rho8', refl_rho8), ('rho2_9', refl_rho2_9)]:
        results[name] = analyze_spectrum(wavelengths, refl)

    sub = 0.0
    valid = 0
    for name, (pk, wlp, bl) in results.items():
        if pk is None:
            continue
        valid += 1
        if wlp is not None and wl_min <= wlp <= wl_max:
            sub += 0.05
        if name == 'flat' and pk >= pk_min_flat:
            sub += 0.15
        elif name == 'rho8' and pk >= pk_min_rho8:
            sub += 0.15
        elif name == 'rho2_9' and pk >= pk_min_rho2_9:
            sub += 0.15
        if bl is not None and (pk - bl) >= margin:
            sub += 0.1

    if valid == 0:
        return 0.0

    pk_flat = results['flat'][0] if results['flat'][0] is not None else None
    pk_rho8 = results['rho8'][0] if results['rho8'][0] is not None else None
    pk_rho2_9 = results['rho2_9'][0] if results['rho2_9'][0] is not None else None

    if pk_flat is not None and pk_rho8 is not None and pk_rho2_9 is not None:
        if pk_flat + 0.01 >= pk_rho8 and pk_rho8 + 0.01 >= pk_rho2_9:
            sub += 0.2

    return min(sub, 1.0)


# === block: score_1 (check id='step_curvature_dependence') ===
def score_1(artifact, step, ctx):
    def score(artifact, step, ctx):
        rows = artifact
        if not rows or not isinstance(rows, list) or len(rows) < 3:
            return 0.0
        try:
            curv_list = [float(r['curvature']) for r in rows]
            pk_list = [float(r['peak_reflectivity']) for r in rows]
            bw_list = [float(r['bandwidth']) for r in rows]
        except (KeyError, ValueError):
            return 0.0
        thresholds = step.get('thresholds', {})
        pk_min_flat = thresholds.get('peak_reflectivity_min_flat', 0.99)
        pk_min_rho8 = thresholds.get('peak_reflectivity_min_rho8', 0.99)
        pk_min_rho2_9 = thresholds.get('peak_reflectivity_min_rho2_9', 0.90)
        bw_flat_max = thresholds.get('bandwidth_flat_max', 0.03)
        bw_rho8_min = thresholds.get('bandwidth_rho8_min', 0.02)
        bw_rho2_9_min = thresholds.get('bandwidth_rho2_9_min', 0.03)
        def find_row(target, tol=0.02):
            for i, c in enumerate(curv_list):
                if abs(c - target) < tol:
                    return i
            return None
        idx_flat = find_row(0.0)
        idx_rho8 = find_row(0.125)
        idx_rho2_9 = find_row(0.345)
        pk_flat = pk_list[idx_flat] if idx_flat is not None else None
        pk_rho8 = pk_list[idx_rho8] if idx_rho8 is not None else None
        pk_rho2_9 = pk_list[idx_rho2_9] if idx_rho2_9 is not None else None
        bw_flat = bw_list[idx_flat] if idx_flat is not None else None
        bw_rho8 = bw_list[idx_rho8] if idx_rho8 is not None else None
        bw_rho2_9 = bw_list[idx_rho2_9] if idx_rho2_9 is not None else None
        sub = 0.0
        if pk_flat is not None and pk_flat >= pk_min_flat:
            sub += 0.15
        if pk_rho8 is not None and pk_rho8 >= pk_min_rho8:
            sub += 0.15
        if pk_rho2_9 is not None and pk_rho2_9 >= pk_min_rho2_9:
            sub += 0.15
        if bw_flat is not None and bw_flat <= bw_flat_max:
            sub += 0.1
        if bw_rho8 is not None and bw_rho8 >= bw_rho8_min:
            sub += 0.1
        if bw_rho2_9 is not None and bw_rho2_9 >= bw_rho2_9_min:
            sub += 0.1
        if pk_flat is not None and pk_rho8 is not None and pk_rho2_9 is not None:
            if pk_flat + 0.01 >= pk_rho8 and pk_rho8 + 0.01 >= pk_rho2_9:
                sub += 0.15
        if bw_flat is not None and bw_rho8 is not None and bw_rho2_9 is not None:
            if bw_flat - 0.01 <= bw_rho8 and bw_rho8 - 0.01 <= bw_rho2_9:
                sub += 0.15
        return min(sub, 1.0)


_SCORERS = {
    'step_reflection_spectra': score_0,
    'step_curvature_dependence': score_1,
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
