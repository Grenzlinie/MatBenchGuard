import os
import json
import csv

# === author imports / helpers ===
import math


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
    import csv
    import os

    magnetization_path = os.path.join(outputs_dir, 'magnetization_curve.csv')
    tsrt_recomputed = None
    magnetization_rows = []

    if os.path.exists(magnetization_path):
        rows = []
        with open(magnetization_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append({
                    'T': float(row['T']),
                    'm_perp': float(row['m_perp']),
                    'm_par': float(row['m_par'])
                })
        magnetization_rows = rows
    
        # Find T where m_perp - m_par crosses zero by linear interpolation
        prev = None
        for row in rows:
            diff = row['m_perp'] - row['m_par']
            if prev is not None and prev['diff'] * diff < 0:
                T0, diff0 = prev['T'], prev['diff']
                T1, diff1 = row['T'], diff
                tsrt_recomputed = T0 + (T1 - T0) * (-diff0) / (diff1 - diff0)
                break
            prev = {'T': row['T'], 'diff': diff}

    tsrt_path = os.path.join(outputs_dir, 'TSRT.txt')
    tsrt_reported = None
    if os.path.exists(tsrt_path):
        with open(tsrt_path) as f:
            content = f.read().strip()
            try:
                tsrt_reported = float(content)
            except ValueError:
                pass

    free_energy_path = os.path.join(outputs_dir, 'free_energy_landscape.csv')
    free_energy_rows = []
    if os.path.exists(free_energy_path):
        with open(free_energy_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                free_energy_rows.append({
                    'm_perp_bin': float(row['m_perp_bin']),
                    'm_par_bin': float(row['m_par_bin']),
                    'F_diff': float(row['F_diff'])
                })

    return {
        'tsrt_recomputed': tsrt_recomputed,
        'tsrt_reported': tsrt_reported,
        'magnetization_rows': magnetization_rows,
        'free_energy_rows': free_energy_rows,
    }


# === block: score_0 (check id='check_magnetization_curve') ===
def score_0(artifact, step, ctx):
    tsrt_recomputed = ctx.get('tsrt_recomputed')
    magnetization_rows = ctx.get('magnetization_rows', [])

    if tsrt_recomputed is None or not magnetization_rows:
        return 0.0

    score = 0.0

    # Read tolerance window from grading_spec step
    ref_window = step.get('reference_window', None)
    if ref_window is not None and isinstance(ref_window, (list, tuple)) and len(ref_window) == 2:
        low_bound, high_bound = ref_window
        # Full credit inside the window; linear decay outside down to [low_bound-0.1, high_bound+0.1]
        if low_bound <= tsrt_recomputed <= high_bound:
            score += 0.6
        elif low_bound - 0.1 <= tsrt_recomputed < low_bound:
            score += 0.6 * (tsrt_recomputed - (low_bound - 0.1)) / 0.10
        elif high_bound < tsrt_recomputed <= high_bound + 0.1:
            score += 0.6 * ((high_bound + 0.1) - tsrt_recomputed) / 0.10
        # else: score += 0.0 for values outside the decay region

    # Trend checks from grading_spec
    trend_checks = step.get('trend_checks', {})
    if trend_checks.get('low_T_perp_greater', False):
        lowest = min(magnetization_rows, key=lambda r: r['T'])
        if lowest['m_perp'] > lowest['m_par']:
            score += 0.2

    if trend_checks.get('mid_T_par_greater', False):
        target = 0.40
        closest = min(magnetization_rows, key=lambda r: abs(r['T'] - target))
        if closest['m_perp'] < closest['m_par']:
            score += 0.2

    return min(score, 1.0)


# === block: score_1 (check id='check_tsrt') ===
def score_1(artifact, step, ctx):
    tsrt_recomputed = ctx.get('tsrt_recomputed')
    tsrt_reported = ctx.get('tsrt_reported')

    if tsrt_recomputed is None or tsrt_reported is None:
        return 0.0

    diff = abs(tsrt_reported - tsrt_recomputed)
    if diff <= 0.05:
        return 1.0
    return max(0.0, 1.0 - (diff - 0.05) / 0.15)


# === block: score_2 (check id='check_free_energy') ===
def score_2(artifact, step, ctx):
    tsrt_recomputed = ctx.get('tsrt_recomputed')
    free_energy_rows = ctx.get('free_energy_rows', [])

    if tsrt_recomputed is None or not free_energy_rows:
        return 0.0

    # Identify all bins in the low free-energy region: F_diff <= T_SRT
    low_bins = [
        (r['m_perp_bin'], r['m_par_bin'])
        for r in free_energy_rows
        if r['F_diff'] <= tsrt_recomputed
    ]

    if not low_bins:
        return 0.0

    score = 0.0

    # Check: exists a bin in the low region with perpendicular magnetization >= 0.5
    if any(p[0] >= 0.5 for p in low_bins):
        score += 0.5

    # Check: exists a bin in the low region with in-plane magnetization >= 0.5
    if any(p[1] >= 0.5 for p in low_bins):
        score += 0.5

    return score


_SCORERS = {
    'check_magnetization_curve': score_0,
    'check_tsrt': score_1,
    'check_free_energy': score_2,
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
