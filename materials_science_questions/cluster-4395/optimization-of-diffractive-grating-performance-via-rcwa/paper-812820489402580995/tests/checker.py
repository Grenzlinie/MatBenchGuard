import os
import json
import csv

# === author imports / helpers ===
import csv, os, math


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


# === block: score_0 (check id='spectrum_TE') ===
def score_0(artifact, step, ctx):
    if not artifact:
        return 0.0
    for row in artifact:
        try:
            wl = float(row.get('wavelength_um', None))
            eff = float(row.get('efficiency', None))
        except (ValueError, TypeError):
            return 0.0
        if not (1.2 <= wl <= 1.7 and 0.0 <= eff <= 1.0):
            return 0.0
    return 1.0


# === block: score_1 (check id='spectrum_TM') ===
def score_1(artifact, step, ctx):
    if not artifact:
        return 0.0
    for row in artifact:
        try:
            wl = float(row.get('wavelength_um', None))
            eff = float(row.get('efficiency', None))
        except (ValueError, TypeError):
            return 0.0
        if not (1.2 <= wl <= 1.7 and 0.0 <= eff <= 1.0):
            return 0.0
    return 1.0


# === block: score_2 (check id='peaks_extracted') ===
def score_2(artifact, step, ctx):
    import os, csv, math

    # basic shape gate already passed by framework
    if not isinstance(artifact, list) or len(artifact) < 3:
        return 0.0

    te_path = '/app/outputs/coupling_spectrum_TE.csv'
    tm_path = '/app/outputs/coupling_spectrum_TM.csv'

    def load_spectrum(path):
        data = []
        if not os.path.exists(path):
            return None
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    wl = float(row['wavelength_um'])
                    eff = float(row['efficiency'])
                except (ValueError, KeyError):
                    continue
                data.append((wl, eff))
        return sorted(data, key=lambda x: x[0])

    te_data = load_spectrum(te_path)
    tm_data = load_spectrum(tm_path)
    if not te_data or not tm_data:
        return 0.0

    target_peaks = step.get('target_peaks', [])
    if not target_peaks:
        return 0.0

    def find_peak(data, target_wl, window=0.1):
        candidates = [(wl, eff) for wl, eff in data if abs(wl - target_wl) <= window]
        if not candidates:
            return None
        peak_wl, peak_eff = max(candidates, key=lambda x: x[1])
        half_max = peak_eff / 2.0
        left_wl = right_wl = None
        # find left crossing
        for i in range(len(data)):
            wl, eff = data[i][0], data[i][1]
            if wl < peak_wl and eff >= half_max and i+1 < len(data):
                wl2, eff2 = data[i+1][0], data[i+1][1]
                if eff2 <= half_max:
                    if eff2 != eff:
                        left_wl = wl + (half_max - eff) * (wl2 - wl) / (eff2 - eff)
                    else:
                        left_wl = wl
                    break
        # find right crossing
        for i in range(len(data)):
            wl, eff = data[i][0], data[i][1]
            if wl > peak_wl and eff >= half_max and i+1 < len(data):
                wl2, eff2 = data[i+1][0], data[i+1][1]
                if eff2 <= half_max:
                    if eff2 != eff:
                        right_wl = wl + (half_max - eff) * (wl2 - wl) / (eff2 - eff)
                    else:
                        right_wl = wl
                    break
        if left_wl is not None and right_wl is not None:
            bw_nm = (right_wl - left_wl) * 1000.0
        else:
            bw_nm = None
        return peak_wl, peak_eff, bw_nm

    total_score = 0.0
    num_checks = 0
    te0_eff = None
    other_effs = []

    for tp in target_peaks:
        data = te_data if tp['mode'] == 'TE0' else tm_data
        pi = find_peak(data, tp['wavelength_um'], window=0.1)
        if pi is None:
            continue
        ag_wl, ag_eff, ag_bw = pi
        # wavelength
        if abs(ag_wl - tp['wavelength_um']) <= tp.get('wavelength_tol', 0.015):
            total_score += 1.0
        num_checks += 1
        # efficiency (threshold_or_better, monotonic)
        eff_lower = tp['efficiency'] - tp.get('efficiency_tol', 0.03)
        if ag_eff >= eff_lower:
            total_score += 1.0
        else:
            partial = max(0.0, ag_eff / eff_lower) if eff_lower > 0 else 0.0
            total_score += partial
        num_checks += 1
        # bandwidth (threshold_or_better: wider is better, never penalise larger bandwidth)
        bw_threshold = tp['bandwidth_3dB_nm'] - tp.get('bandwidth_tol', 8)
        if ag_bw is not None:
            if ag_bw >= bw_threshold:
                total_score += 1.0
            else:
                partial = max(0.0, ag_bw / bw_threshold) if bw_threshold > 0 else 0.0
                total_score += partial
        num_checks += 1
        if tp['mode'] == 'TE0':
            te0_eff = ag_eff
        else:
            other_effs.append(ag_eff)

    # TE0 highest check
    if te0_eff is not None and other_effs:
        if te0_eff >= max(other_effs) - 1e-9:
            total_score += 1.0
        num_checks += 1

    if num_checks == 0:
        return 0.0
    return total_score / num_checks


_SCORERS = {
    'spectrum_TE': score_0,
    'spectrum_TM': score_1,
    'peaks_extracted': score_2,
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
