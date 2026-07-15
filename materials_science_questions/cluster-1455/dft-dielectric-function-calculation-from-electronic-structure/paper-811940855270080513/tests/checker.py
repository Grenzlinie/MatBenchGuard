import os
import json
import csv

# === author imports / helpers ===
import csv
import math
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
        eps_path = os.path.join(outputs_dir, "epsilon_spectra.csv")
        if not os.path.exists(eps_path):
            return {"peaks": {}, "data_by_T": {}}
        with open(eps_path) as f:
            reader = csv.DictReader(f)
            data_by_T = {}
            for row in reader:
                T = int(row["temperature"])
                if T not in data_by_T:
                    data_by_T[T] = {"freq": [], "eps_real": [], "eps_imag": []}
                data_by_T[T]["freq"].append(float(row["frequency"]))
                data_by_T[T]["eps_real"].append(float(row["epsilon_real"]))
                data_by_T[T]["eps_imag"].append(float(row["epsilon_imag"]))
        def find_peaks(freqs, eps_imag):
            peaks = []
            max_val = max(eps_imag) if eps_imag else 0.0
            if max_val == 0.0:
                return peaks
            for i in range(1, len(freqs)-1):
                if eps_imag[i] > eps_imag[i-1] and eps_imag[i] > eps_imag[i+1]:
                    if eps_imag[i] >= 0.05 * max_val:
                        peaks.append(freqs[i])
            return sorted(peaks)
        peaks_dict = {}
        for T in (440, 470):
            if T in data_by_T:
                peaks_dict[T] = find_peaks(data_by_T[T]["freq"], data_by_T[T]["eps_imag"])
        return {"peaks": peaks_dict, "data_by_T": data_by_T}


# === block: score_0 (check id='check_epsilon_spectra') ===
def score_0(artifact, step, ctx):
        # artifact is list of dicts with keys: temperature, frequency, epsilon_real, epsilon_imag
        targets = step.get("targets", {})
        tol_rel = targets.get("tol_rel", 0.35)
        expected = {
            440: targets.get("peak_positions_440", [12.0, 68.0]),
            470: targets.get("peak_positions_470", [16.0, 65.0]),
        }
        low_cut = targets.get("low_freq_cut", 20.0)
        high_cut = targets.get("high_freq_cut", 100.0)

        # group by temperature
        data = {}
        for row in artifact:
            T = int(row["temperature"])
            if T not in data:
                data[T] = {"freq": [], "eps_real": [], "eps_imag": []}
            data[T]["freq"].append(float(row["frequency"]))
            data[T]["eps_real"].append(float(row["epsilon_real"]))
            data[T]["eps_imag"].append(float(row["epsilon_imag"]))

        def find_peaks(freqs, eps_imag):
            peaks = []
            max_val = max(eps_imag) if eps_imag else 0.0
            if max_val == 0.0:
                return peaks
            for i in range(1, len(freqs)-1):
                if eps_imag[i] > eps_imag[i-1] and eps_imag[i] > eps_imag[i+1]:
                    if eps_imag[i] >= 0.05 * max_val:
                        peaks.append(freqs[i])
            return sorted(peaks)

        peak_score = 0.0
        for T in (440, 470):
            if T not in data:
                continue
            f = data[T]["freq"]
            e = data[T]["eps_imag"]
            peaks_all = find_peaks(f, e)
            if len(peaks_all) < 2:
                continue
            exp = expected.get(T, [])
            if not exp:
                continue
            matched = 0
            used = set()
            for e_exp in exp:
                best_i = None
                best_dist = float('inf')
                for i, p in enumerate(peaks_all):
                    if i in used:
                        continue
                    if e_exp == 0.0:
                        continue
                    dist = abs(p - e_exp) / e_exp
                    if dist < best_dist:
                        best_dist = dist
                        best_i = i
                if best_i is not None and best_dist <= tol_rel:
                    matched += 1
                    used.add(best_i)
            peak_score += (matched / len(exp)) * 0.3

        # ε' trend (decreasing with frequency) and temperature ordering
        trend_score = 0.0
        for T in (440, 470):
            if T not in data:
                continue
            f = data[T]["freq"]
            r = data[T]["eps_real"]
            low_idx = [i for i, freq in enumerate(f) if freq <= low_cut]
            high_idx = [i for i, freq in enumerate(f) if freq >= high_cut]
            if low_idx and high_idx:
                low_mean = sum(r[i] for i in low_idx) / len(low_idx)
                high_mean = sum(r[i] for i in high_idx) / len(high_idx)
                if low_mean > high_mean * 1.05:
                    trend_score += 0.05

        if 440 in data and 470 in data:
            low_440 = [r[i] for i, freq in enumerate(data[440]["freq"]) if freq <= low_cut]
            low_470 = [r[i] for i, freq in enumerate(data[470]["freq"]) if freq <= low_cut]
            if low_440 and low_470:
                m440 = sum(low_440) / len(low_440)
                m470 = sum(low_470) / len(low_470)
                if m440 > m470:
                    trend_score += 0.1

        return min(1.0, peak_score + trend_score)


# === block: score_1 (check id='check_mode_params') ===
def score_1(artifact, step, ctx):
        # artifact is list of dicts for mode_parameters.csv
        # ctx["peaks"] is a dict: {440: [peak1, peak2, ...], 470: [...]}
        tol_rel = step.get("tolerance_rel_peak_match", 0.15)
        ref_peaks = ctx.get("peaks", {})
        score = 0.0
        temps_present = 0
        for row in artifact:
            T = int(row["temperature"])
            if T not in ref_peaks:
                continue
            peaks_ref = ref_peaks[T]
            if len(peaks_ref) < 2:
                continue
            # submitted peak frequencies (only nu1_prime, nu2_prime)
            try:
                sub_p1 = float(row["nu1_prime"])
                sub_p2 = float(row["nu2_prime"])
            except (ValueError, KeyError):
                continue
            sub_peaks = sorted([sub_p1, sub_p2])
            # match submitted peaks to reference peaks, one-to-one
            matched = 0
            used = set()
            for rp in peaks_ref[:2]:  # use the two smallest reference peaks (sorted)
                best_i = None
                best_dist = float('inf')
                for i, sp in enumerate(sub_peaks):
                    if i in used:
                        continue
                    if rp == 0.0:
                        continue
                    dist = abs(sp - rp) / rp
                    if dist < best_dist:
                        best_dist = dist
                        best_i = i
                if best_i is not None and best_dist <= tol_rel:
                    matched += 1
                    used.add(best_i)
            score += matched / 2.0
            temps_present += 1
        if temps_present > 0:
            return score / temps_present
        return 0.0


_SCORERS = {
    'check_epsilon_spectra': score_0,
    'check_mode_params': score_1,
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
