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
    import os
    full_csv_path = os.path.join(outputs_dir, 'raman_spectrum_2.33eV.csv')
    frame = None
    with open(full_csv_path, newline='') as f:
        import csv
        reader = csv.DictReader(f)
        rows = list(reader)
        if rows and 'raman_shift_cm1' in rows[0] and 'intensity' in rows[0]:
            frame = [(float(r['raman_shift_cm1']), float(r['intensity'])) for r in rows]
            frame.sort(key=lambda x: x[0])
    windows = {
        'TOLA_K': (2400, 2500),
        '2TO_K': (2630, 2730),
        '2LO_Gamma': (3200, 3300),
        'LOZO_Gamma': (1680, 1780),
        'TOZO_K': (1850, 1950)
    }
    peaks_full = {}
    if frame:
        for band, (lo, hi) in windows.items():
            sub = [(s,i) for s,i in frame if lo <= s <= hi]
            if not sub:
                peaks_full[band] = None
            else:
                best = max(sub, key=lambda x: x[1])
                peaks_full[band] = {'peak_cm1': best[0], 'relative_intensity': best[1]}
    overtone_csv_path = os.path.join(outputs_dir, 'overtone_only_2D_contribution.csv')
    peaks_overtone_2D = None
    if os.path.exists(overtone_csv_path):
        with open(overtone_csv_path, newline='') as f:
            reader = csv.DictReader(f)
            rows2 = list(reader)
            if rows2:
                data2 = [(float(r['raman_shift_cm1']), float(r['intensity'])) for r in rows2]
                data2.sort(key=lambda x: x[0])
                sub2 = [(s,i) for s,i in data2 if windows['2TO_K'][0] <= s <= windows['2TO_K'][1]]
                if sub2:
                    best2 = max(sub2, key=lambda x: x[1])
                    peaks_overtone_2D = best2[0]
    return {'peaks_full': peaks_full, 'peaks_overtone_2D_position': peaks_overtone_2D}


# === block: score_0 (check id='full_spectrum_peaks') ===
def score_0(artifact, step, ctx):
    targets = step.get('targets', {})
    tol_shift = step.get('tol_shift_cm1', 5)
    tol_int_rel = step.get('tol_intensity_rel', 0.2)
    peaks = ctx.get('peaks_full', {})
    if not peaks:
        return 0.0
    band_order = ['TOLA_K', '2TO_K', '2LO_Gamma', 'LOZO_Gamma', 'TOZO_K']
    total = 0.0
    n = len(band_order)
    for band in band_order:
        info = peaks.get(band)
        if info is None:
            continue
        targ = targets.get(band)
        if not targ:
            continue
        shift_ok = abs(info['peak_cm1'] - targ['peak_cm1']) <= tol_shift
        int_diff = abs(info.get('relative_intensity', 0.0) - targ['relative_intensity'])
        int_ok = int_diff <= tol_int_rel * abs(targ['relative_intensity'])
        total += 1.0 if (shift_ok and int_ok) else 0.0
    return total / n if n > 0 else 0.0


# === block: score_1 (check id='overtone_consistency') ===
def score_1(artifact, step, ctx):
    peaks_full = ctx.get('peaks_full', {})
    overtone_pos = ctx.get('peaks_overtone_2D_position')
    full_2TO = peaks_full.get('2TO_K')
    if full_2TO is None or overtone_pos is None:
        return 0.0
    tol = step.get('tol_shift_cm1', 5)
    return 1.0 if abs(full_2TO['peak_cm1'] - overtone_pos) <= tol else 0.0


# === block: score_2 (check id='self_reported_peaks') ===
def score_2(artifact, step, ctx):
    import json
    if artifact is None:
        return 0.0
    if isinstance(artifact, str):
        artifact = json.loads(artifact)
    if not isinstance(artifact, dict):
        return 0.0
    targets = step.get('targets', {})
    tol_shift = step.get('tol_shift_cm1', 5)
    tol_int_rel = step.get('tol_intensity_rel', 0.2)
    band_order = ['2TO_K', '2LO_Gamma', 'TOLA_K', 'LOZO_Gamma', 'TOZO_K']
    total = 0.0
    n = len(band_order)
    for band in band_order:
        agent_entry = artifact.get(band)
        if not agent_entry:
            continue
        targ = targets.get(band)
        if not targ:
            continue
        shift_ok = abs(agent_entry.get('peak_cm1', 0) - targ['peak_cm1']) <= tol_shift
        int_diff = abs(agent_entry.get('relative_intensity', 0.0) - targ['relative_intensity'])
        int_ok = int_diff <= tol_int_rel * abs(targ['relative_intensity'])
        total += 1.0 if (shift_ok and int_ok) else 0.0
    return total / n if n > 0 else 0.0


_SCORERS = {
    'full_spectrum_peaks': score_0,
    'overtone_consistency': score_1,
    'self_reported_peaks': score_2,
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
