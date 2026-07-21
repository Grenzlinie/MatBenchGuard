import os
import json
import csv

# === author imports / helpers ===
import json, csv, math, os

def detect_peaks(modes, threshold):
    """Return the number of modes with keff > threshold, and the list of (freq, keff) for peaks."""
    peaks = [(float(row['frequency_Hz']), float(row['keff'])) for row in modes if float(row['keff']) > threshold]
    return len(peaks), peaks

def compute_keff_and_freqs(modes, peaks):
    """Given list of (freq, keff) peaks, return the maximum keff and its frequency (fr).
    Also compute anti-resonance frequency fa using keff = sqrt(1 - (fr/fa)^2)."""
    if not peaks:
        return None, None, None
    max_peak = max(peaks, key=lambda x: x[1])
    fr = max_peak[0]
    keff = max_peak[1]
    if keff >= 1.0 - 1e-12:
        return fr, keff, None
    fa = fr / math.sqrt(1.0 - keff ** 2)
    return fr, keff, fa


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
    return {"outputs_dir": outputs_dir}


# === block: score_0 (check id='pt2a_keff') ===
def score_0(artifact, step, ctx):
    params = step.get("params", {})
    peaks_thr = params.get("peaks_threshold", 0.03)
    min_peaks = params.get("min_peaks_for_spurious", 2)
    target_spurious = params.get("target_spurious", True)

    if not artifact or not isinstance(artifact, list):
        return 0.0

    # Sort by frequency for robustness
    modes = sorted(artifact, key=lambda row: float(row.get('frequency_Hz', 0.0)))
    try:
        peak_count, _ = detect_peaks(modes, peaks_thr)
    except Exception:
        return 0.0

    recomputed_spurious = peak_count >= min_peaks
    return 1.0 if recomputed_spurious == target_spurious else 0.0


# === block: score_1 (check id='pt2b_keff') ===
def score_1(artifact, step, ctx):
    params = step.get("params", {})
    peaks_thr = params.get("peaks_threshold", 0.03)
    target_keff = params.get("target_keff", 0.40)

    if not artifact or not isinstance(artifact, list):
        return 0.0

    modes = sorted(artifact, key=lambda row: float(row.get('frequency_Hz', 0.0)))
    try:
        peak_count, peaks = detect_peaks(modes, peaks_thr)
        fr, keff, fa = compute_keff_and_freqs(modes, peaks)
    except Exception:
        return 0.0

    # Spurious check: PT2b should have exactly one peak (clean)
    spurious_ok = (peak_count == 1)

    # keff score (threshold_or_better: higher is better)
    if keff is None:
        keff_score = 0.0
    elif keff >= target_keff:
        keff_score = 1.0
    else:
        # Partial credit: score decays linearly from target_keff to 0
        keff_score = max(0.0, keff / target_keff)

    # Combine: 70% keff, 30% spurious
    score = 0.7 * keff_score + 0.3 * (1.0 if spurious_ok else 0.0)
    return min(1.0, max(0.0, score))


# === block: score_2 (check id='summary') ===
def score_2(artifact, step, ctx):
    params = step.get("params", {})
    freq_tol = params.get("freq_tol_rel", 0.05)

    ctx_outputs_dir = ctx.get("outputs_dir", "/app/outputs")
    pt2a_csv_path = os.path.join(ctx_outputs_dir, "pt2a_keff.csv")
    pt2b_csv_path = os.path.join(ctx_outputs_dir, "pt2b_keff.csv")

    if not artifact or not isinstance(artifact, dict):
        return 0.0

    # Load both CSVs for recomputation
    def load_csv(path):
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            return list(csv.DictReader(f))

    pt2a_data = load_csv(pt2a_csv_path)
    pt2b_data = load_csv(pt2b_csv_path)

    if pt2a_data is None or pt2b_data is None:
        return 0.0

    # Compute spurious flags and PT2b params
    peaks_thr = 0.03  # consistent with other steps
    min_peaks_spurious = 2

    # PT2a
    modes_a = sorted(pt2a_data, key=lambda row: float(row.get('frequency_Hz', 0.0)))
    peak_count_a, _ = detect_peaks(modes_a, peaks_thr)
    recomputed_spurious_a = peak_count_a >= min_peaks_spurious

    # PT2b
    modes_b = sorted(pt2b_data, key=lambda row: float(row.get('frequency_Hz', 0.0)))
    peak_count_b, peaks_b = detect_peaks(modes_b, peaks_thr)
    recomputed_spurious_b = peak_count_b >= min_peaks_spurious
    fr_b, keff_b, fa_b = compute_keff_and_freqs(modes_b, peaks_b)

    # Compare with summary.json
    summary = artifact
    checks = []

    # 1. PT2a spurious flag exact match
    pta_flag_match = (summary.get("PT2a_spurious_modes_present") == recomputed_spurious_a)
    checks.append(1.0 if pta_flag_match else 0.0)

    # 2. PT2b spurious flag exact match
    ptb_flag_match = (summary.get("PT2b_spurious_modes_present") == recomputed_spurious_b)
    checks.append(1.0 if ptb_flag_match else 0.0)

    # 3. PT2b resonance frequency within relative tolerance
    fr_reported = summary.get("PT2b_resonance_frequency_Hz")
    if fr_b is not None and fr_reported is not None:
        rel_diff = abs(fr_reported - fr_b) / max(1.0, abs(fr_b))
        checks.append(1.0 if rel_diff <= freq_tol else max(0.0, 1.0 - rel_diff))
    else:
        checks.append(0.0)

    # 4. PT2b anti-resonance frequency
    fa_reported = summary.get("PT2b_anti_resonance_frequency_Hz")
    if fa_b is not None and fa_reported is not None:
        rel_diff = abs(fa_reported - fa_b) / max(1.0, abs(fa_b))
        checks.append(1.0 if rel_diff <= freq_tol else max(0.0, 1.0 - rel_diff))
    else:
        checks.append(0.0)

    # 5. PT2b keff consistency with recomputed
    keff_reported = summary.get("PT2b_keff")
    if keff_b is not None and keff_reported is not None:
        # keff should be within tight tolerance (0.01)
        if abs(keff_reported - keff_b) <= 0.01:
            checks.append(1.0)
        else:
            checks.append(0.0)
    else:
        checks.append(0.0)

    # Average the checks
    score = sum(checks) / len(checks) if checks else 0.0
    return min(1.0, max(0.0, score))


_SCORERS = {
    'pt2a_keff': score_0,
    'pt2b_keff': score_1,
    'summary': score_2,
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
