import os
import json
import csv

# === author imports / helpers ===
import math
import json

def find_local_extrema(energies, values, low, high, mode='max'):
    """
    Find energies within [low, high] where values have a local extremum.
    mode: 'max' for local maxima, 'min' for local minima.
    Returns list of (energy, value) tuples.
    """
    extrema = []
    for i in range(1, len(energies)-1):
        e = energies[i]
        if e < low or e > high:
            continue
        v0 = values[i-1]
        v1 = values[i]
        v2 = values[i+1]
        if mode == 'max':
            if v1 > v0 and v1 > v2:
                extrema.append((e, v1))
        else:
            if v1 < v0 and v1 < v2:
                extrema.append((e, v1))
    return extrema

def nearest_index(energies, target):
    """Return index of energy closest to target."""
    best = -1
    best_dist = float('inf')
    for i, e in enumerate(energies):
        d = abs(e - target)
        if d < best_dist:
            best_dist = d
            best = i
    return best


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


# === block: score_0 (check id='band_gap_type_check') ===
def score_0(artifact, step, ctx):
    art = artifact
    if isinstance(art, dict):
        val = art.get('band_gap_type', '').strip().lower()
        if val == 'indirect':
            return 1.0
    return 0.0


# === block: score_1 (check id='band_gap_value_check') ===
def score_1(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    val = art.get('band_gap_value')
    if not isinstance(val, (int, float)):
        return 0.0
    target = step.get('target', 1.37)
    tol = step.get('tolerance_abs', 0.2)
    decay = step.get('decay_zone', 0.3)
    diff = abs(val - target)
    if diff <= tol:
        return 1.0
    elif diff <= tol + decay:
        return max(0.0, 1.0 - (diff - tol) / decay)
    else:
        return 0.0


# === block: score_2 (check id='static_dielectric_recompute') ===
def score_2(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    config = step.get('config', {})
    keys = config.get('epsilon1_keys', ['epsilon1_xx', 'epsilon1_yy', 'epsilon1_zz'])
    targets = config.get('targets', {'xx':8.83, 'yy':9.79, 'zz':9.01})
    tol = config.get('tolerance_abs', 0.3)
    decay = config.get('decay_zone', 0.5)
    labels = ['xx', 'yy', 'zz']
    scores = []
    for key, lbl in zip(keys, labels):
        arr = art.get(key)
        if not arr or len(arr) < 1:
            scores.append(0.0)
            continue
        eps1_0 = arr[0][1]  # assume energy grid starts at 0
        target_val = targets.get(lbl, 0.0)
        diff = abs(eps1_0 - target_val)
        if diff <= tol:
            s = 1.0
        elif diff <= tol + decay:
            s = max(0.0, 1.0 - (diff - tol) / decay)
        else:
            s = 0.0
        scores.append(s)
    return sum(scores) / len(scores) if scores else 0.0


# === block: score_3 (check id='first_peak_energy_recompute') ===
def score_3(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    config = step.get('config', {})
    keys = config.get('epsilon2_keys', ['epsilon2_xx', 'epsilon2_yy', 'epsilon2_zz'])
    energy_range = config.get('energy_range', [2.0, 3.0])
    target = config.get('target_energy', 2.56)
    tol = config.get('tolerance_abs', 0.3)
    decay = config.get('decay_zone', 0.3)
    peaks = []
    for key in keys:
        arr = art.get(key)
        if not arr or len(arr) < 3:
            continue
        energies = [p[0] for p in arr]
        values = [p[1] for p in arr]
        ext = find_local_extrema(energies, values, energy_range[0], energy_range[1], mode='max')
        if ext:
            # take the maximum value peak
            best = max(ext, key=lambda x: x[1])
            peaks.append(best[0])
    if not peaks:
        return 0.0
    avg_peak = sum(peaks) / len(peaks)
    diff = abs(avg_peak - target)
    if diff <= tol:
        return 1.0
    elif diff <= tol + decay:
        return max(0.0, 1.0 - (diff - tol) / decay)
    else:
        return 0.0


# === block: score_4 (check id='first_peak_assignment_check') ===
def score_4(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    txt = art.get('first_peak_assignment', '')
    keywords = step.get('keywords', [])
    require_all = step.get('require_all', True)
    if not keywords:
        return 1.0
    found = all(kw in txt for kw in keywords) if require_all else any(kw in txt for kw in keywords)
    return 1.0 if found else 0.0


# === block: score_5 (check id='epsilon2_peak_shape') ===
def score_5(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    config = step.get('config', {})
    keys = config.get('epsilon2_keys', ['epsilon2_xx', 'epsilon2_yy', 'epsilon2_zz'])
    energy_range = config.get('energy_range', [2.0, 3.0])
    count = 0
    for key in keys:
        arr = art.get(key)
        if not arr or len(arr) < 3:
            continue
        energies = [p[0] for p in arr]
        values = [p[1] for p in arr]
        ext = find_local_extrema(energies, values, energy_range[0], energy_range[1], mode='max')
        if ext:
            count += 1
    return count / len(keys) if keys else 1.0


# === block: score_6 (check id='reflectivity_min_shape') ===
def score_6(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    config = step.get('config', {})
    keys = config.get('reflectivity_keys', ['reflectivity_xx', 'reflectivity_yy', 'reflectivity_zz'])
    energy_range = config.get('energy_range', [6.0, 8.0])
    count = 0
    for key in keys:
        arr = art.get(key)
        if not arr or len(arr) < 3:
            continue
        energies = [p[0] for p in arr]
        values = [p[1] for p in arr]
        ext = find_local_extrema(energies, values, energy_range[0], energy_range[1], mode='min')
        if ext:
            count += 1
    return count / len(keys) if keys else 1.0


# === block: score_7 (check id='absorption_edge_check') ===
def score_7(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    config = step.get('config', {})
    keys = config.get('absorption_keys', ['absorption_xx', 'absorption_yy', 'absorption_zz'])
    low_e = config.get('energy_low', 2.35)
    high_e = config.get('energy_high', 3.0)
    count = 0
    for key in keys:
        arr = art.get(key)
        if not arr or len(arr) < 2:
            continue
        energies = [p[0] for p in arr]
        values = [p[1] for p in arr]
        idx_low = nearest_index(energies, low_e)
        idx_high = nearest_index(energies, high_e)
        if idx_low < 0 or idx_high < 0:
            continue
        if values[idx_high] > values[idx_low]:
            count += 1
    return count / len(keys) if keys else 1.0


# === block: score_8 (check id='anisotropy_check') ===
def score_8(artifact, step, ctx):
    art = artifact
    if not isinstance(art, dict):
        return 0.0
    config = step.get('config', {})
    keys = config.get('epsilon1_keys', ['epsilon1_xx', 'epsilon1_yy', 'epsilon1_zz'])
    ratio = config.get('ratio_threshold', 1.05)
    if len(keys) < 3:
        return 0.0
    eps_xx = None
    eps_yy = None
    eps_zz = None
    for key in keys:
        arr = art.get(key)
        if not arr or len(arr) < 1:
            return 0.0
        val = arr[0][1]  # static epsilon
        if 'xx' in key:
            eps_xx = val
        elif 'yy' in key:
            eps_yy = val
        elif 'zz' in key:
            eps_zz = val
    if None in (eps_xx, eps_yy, eps_zz):
        return 0.0
    cond1 = eps_yy > eps_xx * ratio
    cond2 = eps_yy > eps_zz * ratio
    return 1.0 if (cond1 and cond2) else 0.0


_SCORERS = {
    'band_gap_type_check': score_0,
    'band_gap_value_check': score_1,
    'static_dielectric_recompute': score_2,
    'first_peak_energy_recompute': score_3,
    'first_peak_assignment_check': score_4,
    'epsilon2_peak_shape': score_5,
    'reflectivity_min_shape': score_6,
    'absorption_edge_check': score_7,
    'anisotropy_check': score_8,
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
