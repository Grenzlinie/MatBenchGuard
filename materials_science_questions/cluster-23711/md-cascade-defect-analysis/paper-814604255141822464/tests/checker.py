import os
import json
import csv

# === author imports / helpers ===
import os, json, csv, math

try:
    import numpy as np
except ImportError:
    class _FakeNumpy:
        @staticmethod
        def array(lst):
            return list(lst)

        @staticmethod
        def argmin(arr):
            return min(range(len(arr)), key=arr.__getitem__)

        @staticmethod
        def argmax(arr):
            return max(range(len(arr)), key=arr.__getitem__)

        @staticmethod
        def where(condition):
            result = [i for i, x in enumerate(condition) if x]
            if isinstance(result, list):
                return result
            return list(result)

        @staticmethod
        def abs(x):
            return [abs(v) for v in x] if isinstance(x, (list, tuple)) else abs(x)

        @staticmethod
        def min(x):
            return min(x)

        @staticmethod
        def max(x):
            return max(x)

    np = _FakeNumpy()


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
    spec = json.load(open('/tests/grading_spec.json'))
    gold = spec['steps'][0].get('gold', {})
    tol_abs = spec['steps'][0].get('tolerance_abs', 2.0)
    tol_pct = spec['steps'][0].get('tolerance_pct', 20.0)
    output_dir = '/app/outputs'
    return {
      'gold_dist_amorph': gold.get('distance_to_amorphization_nm', 6.0),
      'gold_dist_half': gold.get('distance_to_half_amorphization_nm', 22.0),
      'tol_abs': tol_abs,
      'tol_pct': tol_pct,
      'output_dir': output_dir
    }


# === block: score_0 (check id='check_profile_and_distances') ===
def score_0(artifact, step, ctx):
    def structural_audit(rows):
        if not rows: return 0.0
        cols = set(rows[0].keys())
        if 'x_nm' not in cols or 'DeltaE_eV_per_atom' not in cols:
            return 0.0
        xs = []
        ys = []
        for r in rows:
            try:
                x = float(r['x_nm'])
                y = float(r['DeltaE_eV_per_atom'])
            except:
                return 0.0
            xs.append(x)
            ys.append(y)
        if len(xs) < 100: return 0.0
        minx, maxx = min(xs), max(xs)
        if minx > 2.0 or maxx < 998.0: return 0.0
        if any(y < 0 for y in ys): return 0.0
        # The profile peaks near the boundaries and decays toward the interior.
        # The overall maximum (or the maximum in the left half) should be larger
        # than the value at the grain centre (≈ 500 nm).
        idx_mid = min(range(len(xs)), key=lambda i: abs(xs[i] - 500.0))
        if max(ys) <= ys[idx_mid]:
            return 0.0
        return 1.0

    def find_peak_index_xs_ys_left(xs, ys):
        """Return the index of the maximum y in the left half (x <= 500 nm).
        Assumes xs, ys are lists of equal length."""
        left_indices = [i for i, x in enumerate(xs) if x <= 500.0]
        if not left_indices:
            # fallback: use overall argmax
            return max(range(len(ys)), key=lambda i: ys[i])
        peak_idx = max(left_indices, key=lambda i: ys[i])
        return peak_idx

    def distance_after_peak(xs, ys, threshold):
        """Distance from the left boundary (x=0) to the first x after the
        near-boundary peak where y drops below `threshold`."""
        # sort by x
        pairs = sorted(zip(xs, ys), key=lambda t: t[0])
        xs_sorted = [x for x, _ in pairs]
        ys_sorted = [y for _, y in pairs]
        if not xs_sorted:
            return 0.0
        peak_idx = find_peak_index_xs_ys_left(xs_sorted, ys_sorted)
        # scan forward from the peak
        for i in range(peak_idx, len(xs_sorted)):
            if ys_sorted[i] < threshold:
                return xs_sorted[i]
        # if never drops below threshold, return the rightmost x
        return xs_sorted[-1]

    def distance_score(val, gold, tol_abs, tol_pct):
        tol = max(tol_abs, tol_pct / 100.0 * gold)
        return 1.0 if abs(val - gold) <= tol else 0.0

    struct = structural_audit(artifact)
    xs = [float(r['x_nm']) for r in artifact]
    ys = [float(r['DeltaE_eV_per_atom']) for r in artifact]

    d_amorph = distance_after_peak(xs, ys, 0.6)
    d_half   = distance_after_peak(xs, ys, 0.3)

    g_d_am = ctx['gold_dist_amorph']
    g_d_hf = ctx['gold_dist_half']
    ds_am = distance_score(d_amorph, g_d_am, ctx['tol_abs'], ctx['tol_pct'])
    ds_hf = distance_score(d_half,   g_d_hf, ctx['tol_abs'], ctx['tol_pct'])
    dist_score = (ds_am + ds_hf) / 2.0

    return 0.2 * struct + 0.8 * dist_score


# === block: score_1 (check id='check_distances_consistency') ===
def score_1(artifact, step, ctx):
    # artifact is a dict: distances.json

    import csv
    profile_path = os.path.join(ctx['output_dir'], 'excess_energy_profile.csv')
    if not os.path.exists(profile_path):
        return 0.0

    try:
        xs = []
        ys = []
        with open(profile_path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                xs.append(float(row['x_nm']))
                ys.append(float(row['DeltaE_eV_per_atom']))
    except Exception:
        return 0.0

    # Compute distances from the same profile
    def interpolate_distance(xs, ys, threshold):
        pairs = sorted(zip(xs, ys), key=lambda t: t[0])
        for x, y in pairs:
            if y < threshold:
                return x
        return max(xs)

    d_am = interpolate_distance(xs, ys, 0.6)
    d_hf = interpolate_distance(xs, ys, 0.3)

    # Compare to submitted JSON
    if not isinstance(artifact, dict):
        return 0.0
    rep_am = artifact.get('distance_to_amorphization_nm')
    rep_hf = artifact.get('distance_to_half_amorphization_nm')
    if rep_am is None or rep_hf is None:
        return 0.0

    try:
        rep_am = float(rep_am)
        rep_hf = float(rep_hf)
    except (ValueError, TypeError):
        return 0.0

    if abs(rep_am - d_am) > 1e-6 or abs(rep_hf - d_hf) > 1e-6:
        return 0.0
    return 1.0


_SCORERS = {
    'check_profile_and_distances': score_0,
    'check_distances_consistency': score_1,
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
