import os
import json
import csv

# === author imports / helpers ===
import math

def compute_eit_score(artifact, step):
    thresholds = step.get('thresholds', {})
    wl_min = thresholds.get('wl_min', None)
    wl_max = thresholds.get('wl_max', None)
    fwhm_max = thresholds.get('fwhm_nm_max', float('inf'))
    peak_wl_min = thresholds.get('peak_wl_min', 0.0)
    peak_wl_max = thresholds.get('peak_wl_max', 9999.0)
    if wl_min is None or wl_max is None:
        return 0.0

    wls = []
    rs = []
    for row in artifact:
        try:
            wl = float(row.get('wavelength_nm', None))
            r = float(row.get('reflectance', None))
            if wl is not None and r is not None:
                wls.append(wl)
                rs.append(r)
        except:
            continue
    if len(wls) < 2:
        return 0.0

    idx = None
    max_r = -1.0
    for i, wl in enumerate(wls):
        if wl_min <= wl <= wl_max and rs[i] > max_r:
            max_r = rs[i]
            idx = i
    if idx is None or max_r <= 0:
        return 0.0
    peak_wl = wls[idx]

    target_r = max_r / 2.0
    left_wl = None
    for i in range(idx, 0, -1):
        if rs[i-1] <= target_r <= rs[i]:
            delta = rs[i] - rs[i-1]
            frac = (target_r - rs[i-1]) / delta if delta != 0 else 0.0
            left_wl = wls[i-1] + frac * (wls[i] - wls[i-1])
            break
    right_wl = None
    for i in range(idx, len(wls)-1):
        if rs[i] >= target_r >= rs[i+1]:
            delta = rs[i] - rs[i+1]
            frac = (target_r - rs[i+1]) / delta if delta != 0 else 0.0
            right_wl = wls[i] + frac * (wls[i+1] - wls[i])
            break
    if left_wl is None or right_wl is None:
        return 0.0
    fwhm = right_wl - left_wl

    # peak location score (binary window)
    if peak_wl_min <= peak_wl <= peak_wl_max:
        peak_score = 1.0
    else:
        peak_score = 0.0

    # FWHM monotonic score: full credit <= threshold, then decay
    if fwhm <= fwhm_max:
        fwhm_score = 1.0
    else:
        excess = fwhm - fwhm_max
        max_excess = 0.5 * fwhm_max     # reaches 0 at 1.5 * threshold
        if max_excess <= 0:
            fwhm_score = 0.0
        elif excess >= max_excess:
            fwhm_score = 0.0
        else:
            fwhm_score = 1.0 - excess / max_excess

    # combined weight inside the step: 0.7 for FWHM, 0.3 for peak location
    score = 0.7 * fwhm_score + 0.3 * peak_score
    return max(0.0, min(1.0, score))


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


# === block: score_0 (check id='normal_eit') ===
def score_0(artifact, step, ctx):
    return compute_eit_score(artifact, step)


# === block: score_1 (check id='oblique_eit') ===
def score_1(artifact, step, ctx):
    return compute_eit_score(artifact, step)


_SCORERS = {
    'normal_eit': score_0,
    'oblique_eit': score_1,
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
