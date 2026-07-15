import os
import json
import csv

# === author imports / helpers ===
import json
import csv
import os


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


# === block: score_0 (check id='step1') ===
def score_0(artifact, step, ctx):
    ref = step.get('reference', {})
    peak_target = ref.get('peak_wavelength_nm', 660)
    fwhm_target = ref.get('fwhm_nm', 100)
    tol = ref.get('tolerance_nm', 5)
    peak_diff = abs(artifact.get('peak_wavelength_nm') - peak_target)
    fwhm_diff = abs(artifact.get('fwhm_nm') - fwhm_target)
    score = 0.0
    if peak_diff <= tol:
        score += 0.5
    if fwhm_diff <= tol:
        score += 0.5
    return score


# === block: score_1 (check id='step2') ===
def score_1(artifact, step, ctx):
    thresholds = step.get('thresholds', [])
    if not thresholds or not isinstance(artifact, list):
        return 0.0
    lookup = {}
    for row in artifact:
        cfg = row.get('configuration', '')
        pol = row.get('polarization', '')
        lookup[(cfg, pol)] = row
    row_scores = []
    for t in thresholds:
        key = (t['configuration'], t['polarization'])
        row = lookup.get(key)
        if row is None:
            row_scores.append(0.0)
            continue
        try:
            a_si = float(row['net_absorption_aSi'])
            jsc = float(row['Jsc_mA_cm2'])
        except (ValueError, KeyError):
            row_scores.append(0.0)
            continue
        ok_a = 1.0 if a_si >= t['net_absorption_aSi_min'] else 0.0
        ok_jsc = 1.0 if jsc >= t['Jsc_mA_cm2_min'] else 0.0
        row_scores.append((ok_a + ok_jsc) / 2.0)
    return sum(row_scores) / len(row_scores) if row_scores else 0.0


# === block: score_2 (check id='step3') ===
def score_2(artifact, step, ctx):
    tol = step.get('tolerance_nm', 5)
    tm_abs_thresh = step.get('tm_absorption_threshold', 0.9)

    def check_peak_invariance(data, tol):
        angles_0_60 = [a for a in data if a['angle_deg'] <= 60]
        if not angles_0_60:
            return 0.0
        ref_peak = angles_0_60[0]['peak_wavelength_nm']
        count = 0
        for a in angles_0_60:
            if abs(a['peak_wavelength_nm'] - ref_peak) <= tol:
                count += 1
        return count / len(angles_0_60)

    tm_inv = check_peak_invariance(artifact.get('ultrathin_TM', []), tol)
    te_inv = check_peak_invariance(artifact.get('ultrathin_TE', []), tol)
    invariance_score = (tm_inv + te_inv) / 2.0

    tm_80 = [a for a in artifact.get('ultrathin_TM', []) if a['angle_deg'] == 80]
    tm_80_pass = 0.0
    if tm_80:
        max_abs = tm_80[0].get('max_absorption', 0)
        tm_80_pass = 1.0 if max_abs >= tm_abs_thresh else 0.0
    else:
        tm_80_pass = 0.0

    return 0.5 * invariance_score + 0.5 * tm_80_pass


_SCORERS = {
    'step1': score_0,
    'step2': score_1,
    'step3': score_2,
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
