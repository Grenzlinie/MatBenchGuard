import os
import json
import csv

# === author imports / helpers ===
import math

def _find_peaks(times, rates, min_height_ratio=0.1, min_distance=5):
    peaks = []
    n = len(rates)
    if n < 3:
        return peaks
    max_rate = max(rates) if rates else 1.0
    thresh = min_height_ratio * max_rate
    for i in range(1, n-1):
        if rates[i] > rates[i-1] and rates[i] > rates[i+1] and rates[i] >= thresh:
            if not peaks or (i - peaks[-1][0] >= min_distance):
                peaks.append((i, rates[i]))
    return peaks

# Minimal numpy stub to avoid ModuleNotFoundError while keeping scorer code unchanged.
class _NumpyStub:
    def abs(self, arr):
        return [abs(x) for x in arr]
    def array(self, obj):
        return list(obj)
    def argmin(self, arr):
        if not arr:
            raise ValueError("empty array")
        min_val = arr[0]
        min_idx = 0
        for i, v in enumerate(arr):
            if v < min_val:
                min_val = v
                min_idx = i
        return min_idx

np = _NumpyStub()


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
        # No hidden gold needed; structural patterns are verified directly from the artifact.
        return {}


# === block: score_0 (check id='dist_moments') ===
def score_0(artifact, step, ctx):
        rows = artifact
        if not rows:
            return 0.0
        # Find row with time_us closest to 1.5
        best_idx = 0
        best_diff = float('inf')
        for i, r in enumerate(rows):
            try:
                t = float(r['time_us'])
            except:
                t = 0.0
            diff = abs(t - 1.5)
            if diff < best_diff:
                best_diff = diff
                best_idx = i
        row = rows[best_idx]
        try:
            f0 = float(row['f0'])
            f1 = float(row['f1'])
            f2 = float(row['f2'])
            f3 = float(row['f3'])
        except:
            return 0.0
        total = f0 + f1 + f2 + f3
        if total <= 0:
            return 0.0
        return 1.0 if f0 / total > 0.8 else 0.0


# === block: score_1 (check id='realistic_emissions') ===
def score_1(artifact, step, ctx):
        cases = {}
        for row in artifact:
            case = str(row.get('case', '')).strip()
            if not case:
                continue
            try:
                t = float(row['time_us'])
                r = float(row['emission_rate'])
            except:
                continue
            cases.setdefault(case, []).append((t, r))
        if len(cases) != 4:
            return 0.0
        # Check double peaks for each case
        for case, data in cases.items():
            data.sort(key=lambda x: x[0])
            times, rates = zip(*data)
            peaks = _find_peaks(list(times), list(rates), min_height_ratio=0.1, min_distance=5)
            if len(peaks) < 2:
                return 0.0
        # Peak ratio T2_2 vs T2_25
        def max_rate(case):
            return max(r for _, r in cases[case])
        r2 = max_rate('T2_2')
        r25 = max_rate('T2_25')
        if r25 == 0:
            return 0.0
        ratio = r2 / r25
        if ratio < 0.5 or ratio > 2.0:
            return 0.0
        return 1.0


# === block: score_2 (check id='cosh_emissions') ===
def score_2(artifact, step, ctx):
        cases = {}
        for row in artifact:
            case = str(row.get('case', '')).strip()
            if not case:
                continue
            try:
                t = float(row['time_us'])
                r = float(row['emission_rate'])
            except:
                continue
            cases.setdefault(case, []).append((t, r))
        energy_cases = {}
        amplitude_cases = {}
        for case, data in cases.items():
            if case.startswith('equal_energy'):
                param = case.split('_T2_')[-1]
                energy_cases[param] = data
            elif case.startswith('equal_amplitude'):
                param = case.split('_T2_')[-1]
                amplitude_cases[param] = data
        energy_order = ['5', '7', '10', '20']
        eng_peaks = {}
        for param in energy_order:
            data = energy_cases.get(param, [])
            if not data:
                return 0.0
            data.sort(key=lambda x: x[0])
            times, rates = zip(*data)
            peaks = _find_peaks(list(times), list(rates), min_height_ratio=0.1, min_distance=5)
            if not peaks:
                return 0.0
            eng_peaks[param] = max(p[1] for p in peaks)
        prev = None
        for param in energy_order:
            val = eng_peaks[param]
            if prev is not None and val > prev:
                return 0.0
            prev = val
        amp_peaks = {}
        for param in energy_order:
            data = amplitude_cases.get(param, [])
            if not data:
                return 0.0
            data.sort(key=lambda x: x[0])
            times, rates = zip(*data)
            peaks = _find_peaks(list(times), list(rates), min_height_ratio=0.1, min_distance=5)
            if not peaks:
                return 0.0
            amp_peaks[param] = max(p[1] for p in peaks)
        if len(amp_peaks) < 4:
            return 0.0
        max_amp = max(amp_peaks.values())
        min_amp = min(amp_peaks.values())
        if max_amp == 0:
            return 0.0
        ratio_amp = min_amp / max_amp
        if ratio_amp < 0.5:
            return 0.0
        for param in ['5', '7', '10']:
            for data_dict in [energy_cases, amplitude_cases]:
                data = data_dict.get(param, [])
                if not data:
                    return 0.0
                data.sort(key=lambda x: x[0])
                times, rates = zip(*data)
                peaks = _find_peaks(list(times), list(rates), min_height_ratio=0.1, min_distance=5)
                if len(peaks) != 1:
                    return 0.0
        return 1.0


_SCORERS = {
    'dist_moments': score_0,
    'realistic_emissions': score_1,
    'cosh_emissions': score_2,
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
