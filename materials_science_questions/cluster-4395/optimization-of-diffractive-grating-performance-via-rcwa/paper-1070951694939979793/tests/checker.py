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


# === block: score_0 (check id='recompute_csv_metrics') ===
def score_0(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    wavelengths, R0, Rneg, Rpos = [], [], [], []
    for row in rows:
        wavelengths.append(float(row['wavelength_nm']))
        R0.append(float(row['reflectance_0V']))
        Rneg.append(float(row['reflectance_neg30V']))
        Rpos.append(float(row['reflectance_pos30V']))

    # absolute modulation
    abs_mod = max(abs(rp - rn) for rp, rn in zip(Rpos, Rneg))
    # modulation depth on 0V spectrum
    min0 = min(R0)
    max0 = max(R0)
    depth = 1.0 - min0 / max0 if max0 > 0 else 0.0
    # FWHM and FOM
    idx_min = min(range(len(R0)), key=lambda i: R0[i])
    half = (R0[idx_min] + max0) / 2.0
    left, right = None, None
    for i, wl in enumerate(wavelengths):
        if R0[i] <= half:
            if left is None:
                left = wl
            right = wl
    FWHM = (right - left) if left is not None and right is not None else 0.0
    idx_neg = min(range(len(Rneg)), key=lambda i: Rneg[i])
    idx_pos = min(range(len(Rpos)), key=lambda i: Rpos[i])
    shift = abs(wavelengths[idx_neg] - wavelengths[idx_pos])
    FOM = shift / FWHM if FWHM > 0 else 0.0

    score_mod = abs_mod / 0.45 if abs_mod < 0.45 else 1.0
    score_depth = depth / 0.95 if depth < 0.95 else 1.0
    score_fom = FOM / 0.40 if FOM < 0.40 else 1.0
    score_mod = max(0.0, score_mod)
    score_depth = max(0.0, score_depth)
    score_fom = max(0.0, score_fom)
    return 0.5 * score_mod + 0.25 * score_depth + 0.25 * score_fom


# === block: score_1 (check id='validate_json_metrics') ===
def score_1(artifact, step, ctx):
    d = artifact
    abs_mod = float(d.get('absolute_modulation', 0))
    depth = float(d.get('modulation_depth', 0))
    phase = float(d.get('phase_shift_max', 0))
    res_shift = float(d.get('resonance_shift_nm', 0))
    fom = float(d.get('FOM', 0))

    s_abs = abs_mod / 0.45 if abs_mod < 0.45 else 1.0
    s_abs = max(0.0, s_abs)
    s_depth = depth / 0.95 if depth < 0.95 else 1.0
    s_depth = max(0.0, s_depth)
    if phase >= 200:
        s_phase = 1.0
    elif phase <= 150:
        s_phase = 0.0
    else:
        s_phase = (phase - 150) / 50.0
    s_phase = max(0.0, min(1.0, s_phase))
    s_shift = 1.0 if 1.0 <= res_shift <= 4.0 else 0.0
    s_fom = fom / 0.40 if fom < 0.40 else 1.0
    s_fom = max(0.0, s_fom)
    return (s_abs + s_depth + s_phase + s_shift + s_fom) / 5.0


_SCORERS = {
    'recompute_csv_metrics': score_0,
    'validate_json_metrics': score_1,
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
