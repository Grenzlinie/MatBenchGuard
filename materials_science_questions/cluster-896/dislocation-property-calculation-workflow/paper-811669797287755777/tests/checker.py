import os
import json
import csv

# === author imports / helpers ===
import math

EPSILON = 1e-6

def _local_maxima_indices(values):
    indices = []
    n = len(values)
    if n < 3:
        return indices
    for i in range(1, n-1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            indices.append(i)
    return indices


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
    import csv, os

    outputs_dir = os.path.join(os.path.dirname(__file__), '../../app/outputs')  # adjust in final but we are in checker context; actual path is known: /app/outputs
    outputs_dir = '/app/outputs'

    free_path = os.path.join(outputs_dir, 'etch_rate_dislocation_free.csv')
    disloc_path = os.path.join(outputs_dir, 'etch_rate_with_dislocation.csv')

    free_rates = []
    if os.path.exists(free_path):
        with open(free_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    dm = float(row['delta_mu'])
                    rate = float(row['etch_rate'])
                    free_rates.append((dm, rate))
                except (ValueError, KeyError):
                    pass

    disloc_rates = []
    if os.path.exists(disloc_path):
        with open(disloc_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    dm = float(row['delta_mu'])
                    rate = float(row['etch_rate'])
                    disloc_rates.append((dm, rate))
                except (ValueError, KeyError):
                    pass

    return {'free_rates': free_rates, 'disloc_rates': disloc_rates}


# === block: score_0 (check id='specific_heat_peak_and_roughness') ===
def score_0(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 3:
        return 0.0

    pts = []
    for row in artifact:
        try:
            T = float(row['temperature'])
            Cv = float(row['specific_heat'])
            pts.append((T, Cv))
        except (ValueError, KeyError):
            continue

    if len(pts) < 5:
        return 0.0

    pts.sort(key=lambda x: x[0])
    temps = [p[0] for p in pts]
    cv = [p[1] for p in pts]

    peak_t = step.get('peak_temperature', 0.35)
    peak_tol = step.get('peak_tol', 0.02)
    rough_t = step.get('roughening_temperature', 0.75)
    elev_factor = step.get('elevation_factor', 1.5)

    # Peak detection
    peak_indices = _local_maxima_indices(cv)
    peak_found = False
    for idx in peak_indices:
        if abs(temps[idx] - peak_t) <= peak_tol:
            peak_found = True
            break

    # If no clear local maximum, check absolute maximum in interval
    if not peak_found:
        max_cv_idx = max(range(len(temps)), key=lambda i: cv[i])
        if abs(temps[max_cv_idx] - peak_t) <= peak_tol:
            peak_found = True

    # Baseline: low-temperature specific heat (before the peak region)
    baseline = None
    for i, T in enumerate(temps):
        if T < peak_t - 0.05:
            if baseline is None or cv[i] < baseline:
                baseline = cv[i]
    if baseline is None:
        # fallback to the lowest Cv in the entire dataset
        baseline = min(cv) if cv else 0.0

    # Roughening elevation: specific heat near T_R
    rough_cv = None
    for i, T in enumerate(temps):
        if rough_t - 0.05 <= T <= rough_t + 0.1:
            rough_cv = cv[i]
            break
    if rough_cv is None and len(temps) > 0:
        # take maximum after 0.6
        later = [cv[i] for i in range(len(temps)) if temps[i] > 0.6]
        if later:
            rough_cv = max(later)

    elevation_ok = False
    if rough_cv is not None and baseline is not None and baseline > 0:
        if rough_cv >= elev_factor * baseline:
            elevation_ok = True

    score = 0.0
    if peak_found:
        score += 0.6
    if elevation_ok:
        score += 0.4
    return score


# === block: score_1 (check id='etch_rate_monotonic_free') ===
def score_1(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0

    pts = []
    for row in artifact:
        try:
            dm = float(row['delta_mu'])
            rate = float(row['etch_rate'])
            pts.append((dm, rate))
        except (ValueError, KeyError):
            continue

    if len(pts) < 2:
        return 0.0

    pts.sort(key=lambda x: x[0])  # delta_mu negative, larger magnitude (more negative)
    previous = pts[0][1]
    monotonic_count = 0
    total_pairs = 0
    for i in range(1, len(pts)):
        current = pts[i][1]
        total_pairs += 1
        if current >= previous - step.get('eps', EPSILON):
            monotonic_count += 1
        previous = current

    if total_pairs == 0:
        return 0.0
    return monotonic_count / total_pairs


# === block: score_2 (check id='etch_rate_monotonic_disloc') ===
def score_2(artifact, step, ctx):
    if not artifact or not isinstance(artifact, list) or len(artifact) < 2:
        return 0.0

    pts = []
    for row in artifact:
        try:
            dm = float(row['delta_mu'])
            rate = float(row['etch_rate'])
            pts.append((dm, rate))
        except (ValueError, KeyError):
            continue

    if len(pts) < 2:
        return 0.0

    pts.sort(key=lambda x: x[0])
    previous = pts[0][1]
    monotonic_count = 0
    total_pairs = 0
    for i in range(1, len(pts)):
        current = pts[i][1]
        total_pairs += 1
        if current >= previous - step.get('eps', EPSILON):
            monotonic_count += 1
        previous = current

    if total_pairs == 0:
        return 0.0
    return monotonic_count / total_pairs


# === block: score_3 (check id='etch_rate_comparison') ===
def score_3(artifact, step, ctx):
    disloc_data = ctx.get('disloc_rates', [])
    free_data = ctx.get('free_rates', [])

    if not disloc_data or not free_data:
        return 0.0

    disloc_dict = {}
    for dm, rate in disloc_data:
        disloc_dict[dm] = rate

    free_dict = {}
    for dm, rate in free_data:
        free_dict[dm] = rate

    common_deltas = sorted(set(disloc_dict.keys()) & set(free_dict.keys()))
    if not common_deltas:
        return 0.0

    # 1) dislocation rate > free rate
    comparison_ok_count = 0
    total_common = len(common_deltas)
    for dm in common_deltas:
        if disloc_dict[dm] > free_dict[dm] + EPSILON:
            comparison_ok_count += 1

    # 2) reference tolerance check
    ref = step.get('reference_rates', {})
    ref_delta_mu = ref.get('delta_mu', [])
    ref_free = ref.get('free', [])
    ref_disloc = ref.get('disloc', [])
    tol_factor = step.get('rate_tolerance_factor', 0.5)

    ref_match_count = 0
    total_ref = 0
    if ref_delta_mu:
        for i, dm in enumerate(ref_delta_mu):
            if dm in common_deltas:
                total_ref += 1
                # check free
                if i < len(ref_free):
                    ref_rate_free = ref_free[i]
                    submitted_rate_free = free_dict[dm]
                    lower = ref_rate_free * (1 - tol_factor)
                    upper = ref_rate_free * (1 + tol_factor)
                    if lower - EPSILON <= submitted_rate_free <= upper + EPSILON:
                        ref_match_count += 1
                # check disloc
                if i < len(ref_disloc):
                    ref_rate_dis = ref_disloc[i]
                    submitted_rate_dis = disloc_dict[dm]
                    lower = ref_rate_dis * (1 - tol_factor)
                    upper = ref_rate_dis * (1 + tol_factor)
                    if lower - EPSILON <= submitted_rate_dis <= upper + EPSILON:
                        ref_match_count += 1

    if total_common == 0:
        return 0.0

    score_comp = comparison_ok_count / total_common
    score_ref = (ref_match_count / (2 * total_ref)) if total_ref > 0 else 1.0

    # weight comparison 0.6, reference 0.4
    return 0.6 * score_comp + 0.4 * score_ref


_SCORERS = {
    'specific_heat_peak_and_roughness': score_0,
    'etch_rate_monotonic_free': score_1,
    'etch_rate_monotonic_disloc': score_2,
    'etch_rate_comparison': score_3,
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
