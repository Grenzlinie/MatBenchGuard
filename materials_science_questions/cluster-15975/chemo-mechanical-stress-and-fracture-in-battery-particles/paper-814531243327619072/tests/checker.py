import os
import json
import csv

# === author imports / helpers ===
import csv
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
    return {}


# === block: score_0 (check id='thin_film_stress_alpha') ===
def score_0(artifact, step, ctx):
    import csv, math

    rows = artifact
    if not rows:
        return 0.0

    alphas = []
    sigmas = []
    for r in rows:
        try:
            a = float(r['alpha'])
            s = float(r['sigma_film'])
            alphas.append(a)
            sigmas.append(s)
        except:
            return 0.0

    if len(alphas) < 5:
        return 0.0

    # sort by alpha
    pairs = sorted(zip(alphas, sigmas), key=lambda x: x[0])
    sorted_sigmas = [s for _, s in pairs]

    score = 0.0

    # monotonic decreasing check
    mono = True
    for i in range(1, len(sorted_sigmas)):
        if sorted_sigmas[i] > sorted_sigmas[i-1] + 1e-9:
            mono = False
            break
    if mono:
        score += 0.3

    # check the stress at alpha=0.2
    hidden = step.get('hidden', {})
    target_alpha = hidden.get('target_alpha', 0.2)
    target_sigma = hidden.get('target_sigma', 0.0125)
    tol = hidden.get('tol_abs', 0.005)

    closest = None
    min_diff = float('inf')
    for a, s in pairs:
        diff = abs(a - target_alpha)
        if diff < min_diff:
            min_diff = diff
            closest = s

    if closest is not None and abs(closest - target_sigma) <= tol:
        score += 0.7
    elif closest is not None:
        # partial credit based on distance
        score += 0.7 * max(0.0, 1.0 - (abs(closest - target_sigma) / (tol*2)))

    return min(1.0, score)


# === block: score_1 (check id='spherical_lithiation_evolution') ===
def score_1(artifact, step, ctx):
    import csv, math, numpy as np

    rows = artifact
    if not rows:
        return 0.0

    rcs = []
    rss = []
    for r in rows:
        try:
            rc = float(r['rc'])
            rs = float(r['rs'])
            rcs.append(rc)
            rss.append(rs)
        except:
            return 0.0

    if len(rcs) < 5:
        return 0.0

    score = 0.0
    hidden = step.get('hidden', {})

    # rc should be non-increasing
    if hidden.get('check_decreasing', True):
        dec = True
        for i in range(1, len(rcs)):
            if rcs[i] > rcs[i-1] + 1e-9:
                dec = False
                break
        if dec:
            score += 0.4

    # rs should be non-decreasing
    if hidden.get('check_increasing_rs', True):
        inc = True
        for i in range(1, len(rss)):
            if rss[i] < rss[i-1] - 1e-9:
                inc = False
                break
        if inc:
            score += 0.1

    # final rc should be near equilibrium
    final_rc = rcs[-1]
    target_rc = hidden.get('target_rc_equilibrium', 17.5)
    tol_rc = hidden.get('tol_rc', 2.5)
    diff = abs(final_rc - target_rc)
    if diff <= tol_rc:
        score += 0.5
    else:
        score += 0.5 * max(0.0, 1.0 - (diff - tol_rc) / (2*tol_rc))

    return min(1.0, score)


# === block: score_2 (check id='equilibrium_core_radius') ===
def score_2(artifact, step, ctx):
    import csv, math, numpy as np

    rows = artifact
    if not rows:
        return 0.0

    r_over_l0 = []
    rce_over_R = []
    for r in rows:
        try:
            r_over_l0.append(float(r['R_over_l0']))
            rce_over_R.append(float(r['rce_over_R']))
        except:
            return 0.0

    if len(r_over_l0) < 5:
        return 0.0

    score = 0.0
    hidden = step.get('hidden', {})

    # check monotonic increase
    if hidden.get('check_monotonic', True):
        mono = True
        for i in range(1, len(rce_over_R)):
            if rce_over_R[i] < rce_over_R[i-1] - 1e-9:
                mono = False
                break
        if mono:
            score += 0.4

    # compare to gold pairs
    gold_pairs = hidden.get('gold_pairs', [])
    tol = hidden.get('tol_abs', 0.08)

    matches = 0
    for R_target, rce_target in gold_pairs:
        closest_rce = None
        min_diff_R = float('inf')
        for R_val, rce_val in zip(r_over_l0, rce_over_R):
            if abs(R_val - R_target) < min_diff_R:
                min_diff_R = abs(R_val - R_target)
                closest_rce = rce_val
        if closest_rce is not None and abs(closest_rce - rce_target) <= tol:
            matches += 1
        elif closest_rce is not None:
            partial = max(0.0, 1.0 - (abs(closest_rce - rce_target) - tol) / (2*tol))
            matches += partial

    if gold_pairs:
        score += 0.6 * (matches / len(gold_pairs))

    return min(1.0, score)


# === block: score_3 (check id='energy_release_rate') ===
def score_3(artifact, step, ctx):
    import csv, math, numpy as np

    rows = artifact
    if not rows:
        return 0.0

    # organize by lithiation state
    data = {}
    for r in rows:
        try:
            a = float(r['a_over_R'])
            rc = float(r['rc_over_R'])
            G = float(r['G_normalized'])
        except:
            return 0.0
        if rc not in data:
            data[rc] = []
        data[rc].append((a, G))

    states = sorted(data.keys())  # ascending rc_over_R (i.e. 0.2, 0.5, 0.8)
    if len(states) < 2:
        return 0.0

    score = 0.0
    hidden = step.get('hidden', {})

    # 1. each curve must have a single maximum
    single_max_ok = True
    max_locations = {}
    for rc in states:
        curve = data[rc]
        Gs = [g for _, g in curve]
        maxG = max(Gs)
        peaks = [i for i, g in enumerate(Gs) if g == maxG]
        if len(peaks) != 1:
            single_max_ok = False
        else:
            max_locations[rc] = curve[peaks[0]][0]  # a/R at max

    if hidden.get('check_single_max', True):
        if single_max_ok:
            score += 0.3

    # 2. peak a/R must shift to larger values as lithiation deepens (rc_over_R decreases)
    if hidden.get('check_peak_shift', True) and len(max_locations) == len(states):
        # deeper lithiation: smaller rc_over_R -> larger a/R peak
        # so as rc decreases (state order: 0.8 -> 0.5 -> 0.2), peak a/R should increase
        a_peak_order = []
        for rc in sorted(states, reverse=True):  # descending
            a_peak_order.append(max_locations[rc])
        shift_ok = all(a_peak_order[i] <= a_peak_order[i+1] for i in range(len(a_peak_order)-1))
        if shift_ok:
            score += 0.4

    # 3. maximum G should be larger for deeper lithiation (smaller rc)
    Gmax_vals = []
    for rc in states:
        Gmax_vals.append(max([g for _, g in data[rc]]))
    # deeper lithiation (smaller rc) -> larger Gmax
    Gmax_order_ok = all(Gmax_vals[i] <= Gmax_vals[i+1] for i in range(len(Gmax_vals)-1))
    if Gmax_order_ok:
        score += 0.3

    return min(1.0, score)


# === block: score_4 (check id='gmax_vs_R') ===
def score_4(artifact, step, ctx):
    import csv, math, numpy as np

    rows = artifact
    if not rows:
        return 0.0

    R_vals = []
    G_vals = []
    for r in rows:
        try:
            R_vals.append(float(r['R_over_l0']))
            G_vals.append(float(r['G_max_normalized']))
        except:
            return 0.0

    if len(R_vals) < 5:
        return 0.0

    # sort by R
    pairs = sorted(zip(R_vals, G_vals), key=lambda x: x[0])
    R_sorted = [p[0] for p in pairs]
    G_sorted = [p[1] for p in pairs]

    score = 0.0
    hidden = step.get('hidden', {})

    # 1. monotonic increase of G_max with R
    if hidden.get('check_monotonic_increase', True):
        mono = True
        for i in range(1, len(G_sorted)):
            if G_sorted[i] < G_sorted[i-1] - 1e-9:
                mono = False
                break
        if mono:
            score += 0.3

    # 2. critical size R* where G_max crosses Gamma
    Gamma = hidden.get('Gamma', 0.1)
    R_range = hidden.get('target_Rstar_range', [24, 32])

    R_star = None
    for i in range(len(G_sorted)-1):
        if G_sorted[i] <= Gamma <= G_sorted[i+1]:
            # linear interpolation
            frac = (Gamma - G_sorted[i]) / (G_sorted[i+1] - G_sorted[i])
            R_star = R_sorted[i] + frac * (R_sorted[i+1] - R_sorted[i])
            break

    if R_star is not None:
        if R_range[0] <= R_star <= R_range[1]:
            score += 0.7
        else:
            # partial: distance from range
            dist = max(0, R_range[0] - R_star, R_star - R_range[1])
            score += 0.7 * max(0.0, 1.0 - dist/5.0)
    else:
        # no crossing found; check if all G_max < Gamma then score partial based on R_star? not applicable
        pass

    return min(1.0, score)


_SCORERS = {
    'thin_film_stress_alpha': score_0,
    'spherical_lithiation_evolution': score_1,
    'equilibrium_core_radius': score_2,
    'energy_release_rate': score_3,
    'gmax_vs_R': score_4,
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
