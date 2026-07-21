import os
import json
import csv

# === author imports / helpers ===
import math

class _NumpyCompat:
    @staticmethod
    def array(iterable):
        return list(iterable)
    @staticmethod
    def mean(arr):
        if not arr: return 0.0
        return sum(arr) / len(arr)
    @staticmethod
    def min(arr):
        if not arr: return 0.0
        return min(arr)
    @staticmethod
    def max(arr):
        if not arr: return 0.0
        return max(arr)

np = _NumpyCompat()


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


# === block: score_0 (check id='cv5_timeseries') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) == 0:
        return 0.0
    vals = []
    for row in artifact:
        try:
            v = float(row.get('CV5_angstrom'))
            vals.append(v)
        except (ValueError, TypeError):
            continue
    if not vals:
        return 0.0
    arr = np.array(vals)
    mean = np.mean(arr)
    min_val = np.min(arr)
    max_val = np.max(arr)
    targets = step.get('targets', {})
    target_mean = targets.get('mean', -0.363)
    tol_mean = targets.get('tolerance_mean', 0.05)
    min_amplitude = targets.get('min_amplitude', 1.6)
    w_mean = targets.get('weight_mean', 0.6)
    w_amp = targets.get('weight_amplitude', 0.4)
    # mean score: closeness within tolerance
    mean_diff = abs(mean - target_mean)
    mean_score = max(0.0, 1.0 - mean_diff / tol_mean) if tol_mean > 0 else (1.0 if mean_diff <= 1e-9 else 0.0)
    # amplitude score: range >= min_amplitude
    amplitude = max_val - min_val
    amp_score = min(1.0, amplitude / min_amplitude) if min_amplitude > 0 else 1.0
    final = w_mean * mean_score + w_amp * amp_score
    return round(min(1.0, max(0.0, final)), 6)


# === block: score_1 (check id='md2_summary') ===
def score_1(artifact, step, ctx):
    data = artifact
    targets = step.get('targets', {})
    if not data or not isinstance(data, dict):
        return 0.0
    scores = []
    weights = []
    for field, tdef in targets.items():
        if field not in data:
            scores.append(0.0)
            weights.append(1.0)
            continue
        if isinstance(tdef, dict) and tdef.get('exact'):
            # boolean exact match
            expected = tdef['value']
            scores.append(1.0 if data[field] == expected else 0.0)
            weights.append(1.0)
        elif isinstance(tdef, dict) and 'value' in tdef:
            target_val = tdef['value']
            tol = tdef.get('tolerance', 0.0)
            try:
                rep_val = float(data[field])
                diff = abs(rep_val - target_val)
                if tol > 0:
                    sc = max(0.0, 1.0 - diff / tol)
                else:
                    sc = 1.0 if diff <= 1e-9 else 0.0
                scores.append(sc)
                weights.append(1.0)
            except (ValueError, TypeError):
                scores.append(0.0)
                weights.append(1.0)
        else:
            # ignore unknown format
            weight = 0.0
            scores.append(0.0)
            weights.append(0.0)
    if not weights or sum(weights) == 0:
        return 0.0
    avg = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
    return round(min(1.0, max(0.0, avg)), 6)


# === block: score_2 (check id='md3_summary') ===
def score_2(artifact, step, ctx):
    data = artifact
    targets = step.get('targets', {})
    if not data or not isinstance(data, dict):
        return 0.0
    scores = []
    weights = []
    for field, tdef in targets.items():
        if field not in data:
            scores.append(0.0)
            weights.append(1.0)
            continue
        if isinstance(tdef, dict) and 'value' in tdef:
            target_val = tdef['value']
            tol = tdef.get('tolerance', 0.0)
            try:
                rep_val = float(data[field])
                diff = abs(rep_val - target_val)
                if tol > 0:
                    sc = max(0.0, 1.0 - diff / tol)
                else:
                    sc = 1.0 if diff <= 1e-9 else 0.0
                scores.append(sc)
                weights.append(1.0)
            except (ValueError, TypeError):
                scores.append(0.0)
                weights.append(1.0)
        else:
            scores.append(0.0)
            weights.append(0.0)
    if not weights or sum(weights) == 0:
        return 0.0
    avg = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
    return round(min(1.0, max(0.0, avg)), 6)


# === block: score_3 (check id='free_energies') ===
def score_3(artifact, step, ctx):
    data = artifact
    targets = step.get('targets', {})
    if not data or not isinstance(data, dict):
        return 0.0
    scores = []
    weights = []
    for field, tdef in targets.items():
        if field not in data:
            scores.append(0.0)
            weights.append(1.0)
            continue
        if isinstance(tdef, dict) and 'value' in tdef:
            target_val = tdef['value']
            tol = tdef.get('tolerance', 0.0)
            try:
                rep_val = float(data[field])
                diff = abs(rep_val - target_val)
                if tol > 0:
                    sc = max(0.0, 1.0 - diff / tol)
                else:
                    sc = 1.0 if diff <= 1e-9 else 0.0
                scores.append(sc)
                weights.append(1.0)
            except (ValueError, TypeError):
                scores.append(0.0)
                weights.append(1.0)
        else:
            scores.append(0.0)
            weights.append(0.0)
    if not weights or sum(weights) == 0:
        return 0.0
    avg = sum(s * w for s, w in zip(scores, weights)) / sum(weights)
    return round(min(1.0, max(0.0, avg)), 6)


_SCORERS = {
    'cv5_timeseries': score_0,
    'md2_summary': score_1,
    'md3_summary': score_2,
    'free_energies': score_3,
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
