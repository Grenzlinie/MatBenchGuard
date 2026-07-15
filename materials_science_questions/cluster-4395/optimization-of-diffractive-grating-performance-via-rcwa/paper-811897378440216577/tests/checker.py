import os
import json
import csv

# === author imports / helpers ===
import sys
import math

class FakeArray(list):
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return FakeArray(x - other for x in self)
        return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return FakeArray(other - x for x in self)
        return NotImplemented

class _FakeNumpy:
    def array(self, obj):
        return FakeArray(obj)
    def asarray(self, obj):
        return FakeArray(obj)
    def abs(self, x):
        if isinstance(x, (list, FakeArray)):
            return FakeArray(abs(a) for a in x)
        return abs(x)
    def min(self, x):
        return min(x)
    def max(self, x):
        return max(x)
    def argsort(self, x):
        return sorted(range(len(x)), key=lambda i: x[i])
    def sum(self, x):
        return sum(x)
    def mean(self, x):
        if len(x) == 0:
            return 0.0
        return sum(x) / len(x)
    def std(self, x):
        if len(x) < 2:
            return 0.0
        m = sum(x) / len(x)
        variance = sum((v - m) ** 2 for v in x) / len(x)
        return math.sqrt(variance)

_fake = _FakeNumpy()
sys.modules['numpy'] = _fake
import numpy as np

def find_peaks(wavelengths, reflectivity, min_reflectivity=0.1):
    """Return (peak_wavelengths, peak_reflectivities) for local maxima above min_reflectivity."""
    r = np.asarray(reflectivity)
    w = np.asarray(wavelengths)
    n = len(r)
    peaks_w = []
    peaks_r = []
    for i in range(1, n-1):
        if r[i] > min_reflectivity and r[i] > r[i-1] and r[i] > r[i+1]:
            peaks_w.append(w[i])
            peaks_r.append(r[i])
    return np.array(peaks_w), np.array(peaks_r)


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
    step = None
    for s in spec.get('steps', []):
        if s.get('output_file') == 'reflection_spectra.csv':
            step = s
            break
    if step is None:
        raise ValueError('No step for reflection_spectra.csv')
    return {
        'front_design': np.array(step['front_design_peaks_nm']),
        'rear_design': np.array(step['rear_design_peaks_nm']),
        'tol': step['wavelength_tolerance_nm'],
        'std_thresh': step['std_threshold'],
        'env_thresh': step['env_dev_threshold'],
        'w_peaks': step['weight_peaks'],
        'w_std': step['weight_std'],
        'w_env': step['weight_env'],
        'min_ref': step['peak_detection_min_reflectivity'],
        'decay': step['decay_scale']
    }


# === block: score_0 (check id='step_reflectivity') ===
def score_0(artifact, step, ctx):
    import numpy as np
    import csv
    import io

    # artifact is a list of dicts (csv rows)
    if not artifact or 'wavelength_nm' not in artifact[0]:
        return 0.0

    wl = np.array([float(r['wavelength_nm']) for r in artifact])
    front = np.array([float(r['front_reflectivity']) for r in artifact])
    rear = np.array([float(r['rear_reflectivity']) for r in artifact])

    front_peaks_w, front_peaks_r = find_peaks(wl, front, ctx['min_ref'])
    rear_peaks_w, rear_peaks_r = find_peaks(wl, rear, ctx['min_ref'])

    def peak_match_score(peaks_w, design_peaks, tol):
        if len(peaks_w) == 0:
            return 0.0
        matched = 0
        for dp in design_peaks:
            dists = np.abs(peaks_w - dp)
            if np.min(dists) <= tol:
                matched += 1
        return matched / len(design_peaks)

    def uniformity_score(peaks_r, thresh, decay):
        if len(peaks_r) < 2:
            return 0.0
        std_val = np.std(peaks_r)
        if std_val <= thresh:
            return 1.0
        else:
            excess = std_val - thresh
            return max(0.0, 1.0 - excess / (decay * thresh))

    def envelope_score(peaks_w, reflectivity, wavelengths, thresh, decay):
        """Compute envelope uniformity: max deviation of between-peak mean reflectivity from envelope mean."""
        if len(peaks_w) < 2:
            return 0.0
        sorted_idx = np.argsort(peaks_w)
        p_w = peaks_w[sorted_idx]
        n_int = len(p_w) - 1
        if n_int < 1:
            return 0.0
        env_vals = []
        for i in range(n_int):
            mask = (wavelengths > p_w[i]) & (wavelengths < p_w[i+1])
            if np.sum(mask) == 0:
                continue
            env_vals.append(np.mean(reflectivity[mask]))
        if not env_vals:
            return 0.0
        env_mean = np.mean(env_vals)
        max_dev = max(abs(v - env_mean) for v in env_vals)
        if max_dev <= thresh:
            return 1.0
        else:
            excess = max_dev - thresh
            return max(0.0, 1.0 - excess / (decay * thresh))

    # Compute component scores for front and rear
    front_pmatch = peak_match_score(front_peaks_w, ctx['front_design'], ctx['tol'])
    rear_pmatch = peak_match_score(rear_peaks_w, ctx['rear_design'], ctx['tol'])

    front_std = uniformity_score(front_peaks_r, ctx['std_thresh'], ctx['decay'])
    rear_std = uniformity_score(rear_peaks_r, ctx['std_thresh'], ctx['decay'])

    front_env = envelope_score(front_peaks_w, front, wl, ctx['env_thresh'], ctx['decay'])
    rear_env = envelope_score(rear_peaks_w, rear, wl, ctx['env_thresh'], ctx['decay'])

    # Combine with weights, average front/rear for each category
    avg_peaks = (front_pmatch + rear_pmatch) / 2.0
    avg_std = (front_std + rear_std) / 2.0
    avg_env = (front_env + rear_env) / 2.0

    total = ctx['w_peaks'] * avg_peaks + ctx['w_std'] * avg_std + ctx['w_env'] * avg_env
    return min(1.0, max(0.0, total))


_SCORERS = {
    'step_reflectivity': score_0,
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
