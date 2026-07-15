import os
import json
import csv

# === author imports / helpers ===
import csv
import numpy as np
try:
    from scipy.signal import find_peaks
except ImportError:
    def find_peaks(x, height=None, distance=None):
        """Fallback peak detection without scipy."""
        peaks = []
        for i in range(1, len(x)-1):
            if x[i] > x[i-1] and x[i] > x[i+1]:
                if height is None or x[i] > height:
                    peaks.append(i)
        return peaks, {}


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


# === block: score_0 (check id='angular_width_recompute') ===
def score_0(artifact, step, ctx):
        if artifact is None:
            return 0.0
        # Load raw trajectory data
        raw_path = '/app/outputs/relative_energy_data.csv'
        try:
            with open(raw_path, newline='') as f:
                raw_rows = list(csv.DictReader(f))
        except Exception:
            return 0.0

        from collections import defaultdict
        data = defaultdict(list)
        for r in raw_rows:
            key = (float(r['incidence_energy_eV']), int(r['surface_temperature_K']))
            data[key].append(float(r['exit_angle_deg']))

        ref = step.get('reference_widths', {})
        tol = step.get('tolerance_abs_deg', 5.0)
        conditions = step.get('conditions', [])
        scores = []
        for cond in conditions:
            key = (cond['incidence_energy_eV'], cond['surface_temperature_K'])
            if key not in data or len(data[key]) < 10:
                scores.append(0.0)
                continue
            angles = np.array(data[key])
            w = 2.0 * np.sqrt(np.mean(angles**2) - np.mean(angles)**2)
            ref_key = f"{cond['incidence_energy_eV']}_{cond['surface_temperature_K']}"
            ref_val = ref.get(ref_key)
            if ref_val is None:
                scores.append(0.0)
            else:
                delta = abs(w - ref_val)
                if delta <= tol:
                    scores.append(1.0)
                else:
                    # Linear decay to 0 at twice tolerance
                    s = max(0.0, 1.0 - (delta - tol) / tol)
                    scores.append(s)
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_1 (check id='sticking_probability_check') ===
def score_1(artifact, step, ctx):
        if artifact is None:
            return 0.0
        ref = step.get('reference_probs', {})
        tol = step.get('tolerance_abs', 0.05)
        conditions = step.get('conditions', [])
        sensor = {}
        for row in artifact:
            e = row.get('incidence_energy_eV')
            p = row.get('sticking_probability')
            if e and p:
                sensor[float(e)] = float(p)
        scores = []
        for cond in conditions:
            e = cond['incidence_energy_eV']
            if e not in sensor:
                scores.append(0.0)
                continue
            p = sensor[e]
            ref_p = ref.get(str(e))
            if ref_p is None:
                scores.append(0.0)
            else:
                delta = abs(p - ref_p)
                if delta <= tol:
                    scores.append(1.0)
                else:
                    s = max(0.0, 1.0 - (delta - tol) / tol)
                    scores.append(s)
        if not scores:
            return 0.0
        return float(np.mean(scores))


# === block: score_2 (check id='trajectory_rainbow_audit') ===
def score_2(artifact, step, ctx):
        if artifact is None:
            return 0.0
        raw_path = '/app/outputs/relative_energy_data.csv'
        try:
            with open(raw_path, newline='') as f:
                raw_rows = list(csv.DictReader(f))
        except Exception:
            return 0.0

        static_angles = []
        hot_angles = []
        for r in raw_rows:
            if float(r['incidence_energy_eV']) == 0.1:
                if int(r['surface_temperature_K']) == 0:
                    static_angles.append(float(r['exit_angle_deg']))
                elif int(r['surface_temperature_K']) == 600:
                    hot_angles.append(float(r['exit_angle_deg']))

        def count_peaks(angles, min_frac=0.05):
            if len(angles) < 50:
                return 0
            hist, _ = np.histogram(angles, bins=30)
            max_h = max(hist)
            peaks, _ = find_peaks(hist, height=max_h*min_frac)
            return len(peaks)

        static_peaks = count_peaks(static_angles)
        hot_peaks = count_peaks(hot_angles)

        score = 0.0
        if static_peaks >= 2:
            score += 0.5
        elif static_peaks == 1:
            score += 0.25
        if hot_peaks == 1:
            score += 0.5
        elif hot_peaks == 0:
            score += 0.25

        return score


_SCORERS = {
    'angular_width_recompute': score_0,
    'sticking_probability_check': score_1,
    'trajectory_rainbow_audit': score_2,
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
