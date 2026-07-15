import os
import json
import csv

# === author imports / helpers ===
import csv, math


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


# === block: score_0 (check id='e2g_peak_check') ===
def score_0(artifact, step, ctx):
    rows = [r for r in artifact]
    if not rows:
        return 0.0
    freq_map = {}
    for r in rows:
        try:
            conc = float(r['vacancy_concentration'])
            val = float(r['e2g_frequency'])
            freq_map[conc] = val
        except (ValueError, KeyError):
            pass
    expected_conc = [0, 10, 20, 30]
    if not all(c in freq_map for c in expected_conc):
        return 0.0
    freqs = [freq_map[c] for c in expected_conc]
    ref = step['reference_targets']
    tol = step['tolerance_cm']
    within = 0
    for c, v in zip(expected_conc, freqs):
        target = ref.get(str(c))
        if target is None:
            return 0.0
        if abs(v - target) <= tol:
            within += 1
    freq_within_score = within / len(expected_conc)
    monotonic = all(freqs[i] >= freqs[i+1] for i in range(len(freqs)-1))
    score = freq_within_score * 0.6 + (1.0 if monotonic else 0.0) * 0.4
    return score


# === block: score_1 (check id='pdos_shift_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    freq_min = step['frequency_range_min']
    freq_max = step['frequency_range_max']
    sum_pristine = 0.0
    sum_30 = 0.0
    for r in rows:
        try:
            f = float(r['frequency'])
            if freq_min <= f <= freq_max:
                p0 = float(r['PDOS_pristine'])
                p30 = float(r['PDOS_30'])
                sum_pristine += p0
                sum_30 += p30
        except (ValueError, KeyError):
            continue
    if sum_pristine <= 0:
        return 0.0
    return 1.0 if sum_30 < sum_pristine else 0.0


# === block: score_2 (check id='specific_heat_mono_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    points = step['temperature_points']
    if not points:
        return 0.0
    temp_idx = {}
    for i, r in enumerate(rows):
        try:
            t = float(r['temperature_K'])
            temp_idx[round(t, 1)] = i
        except (ValueError, KeyError):
            pass
    def get_cv(row, col):
        try:
            return float(row[col])
        except (ValueError, KeyError):
            return None
    passed = 0
    for T in points:
        idx = None
        # find closest row
        best_diff = None
        best_i = None
        for i, r in enumerate(rows):
            try:
                t = float(r['temperature_K'])
                diff = abs(t - T)
                if best_diff is None or diff < best_diff:
                    best_diff = diff
                    best_i = i
            except (ValueError, KeyError):
                continue
        if best_i is None:
            continue
        row = rows[best_i]
        cv_pristine = get_cv(row, 'C_V_pristine')
        cv_10 = get_cv(row, 'C_V_10')
        cv_20 = get_cv(row, 'C_V_20')
        cv_30 = get_cv(row, 'C_V_30')
        if None in (cv_pristine, cv_10, cv_20, cv_30):
            continue
        if cv_pristine >= cv_10 >= cv_20 >= cv_30:
            passed += 1
    if not points:
        return 0.0
    return passed / len(points)


_SCORERS = {
    'e2g_peak_check': score_0,
    'pdos_shift_check': score_1,
    'specific_heat_mono_check': score_2,
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
