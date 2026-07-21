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


# === block: score_0 (check id='spatial_distribution') ===
def score_0(artifact, step, ctx):
    def group_by_B(rows):
        groups = {}
        for r in rows:
            b = float(r['B_ratio'])
            z = int(r['distance'])
            c = int(r['count'])
            groups.setdefault(b, []).append((z, c))
        return groups

    def spatial_score(artifact, step, ctx):
        groups = group_by_B(artifact)
        params = step['params']
        flat_thresh = params['flatness_ratio_threshold']
        peak_ranges = params['peak_distance_ranges']
        trough_fac = params['trough_depth_factor']
        central_region = params['central_region']
        # B values expected
        bs = [0.0, 0.1, 0.3, 0.5]
        passes = 0
        total = 0
        for b in bs:
            if b not in groups:
                continue
            total += 1
            dist_counts = dict(groups[b])
            # B=0 flatness
            if b == 0.0:
                vals = [dist_counts.get(z, 0) for z in range(central_region[0], central_region[1]+1)]
                if vals:
                    mx = max(vals)
                    mn = min(vals) if min(vals) > 0 else 1
                    ratio = mx / mn
                    if ratio <= flat_thresh:
                        passes += 1
            else:
                # B>0 double peak check
                z_vals = sorted(dist_counts.keys())
                if len(z_vals) < 3:
                    continue
                counts = [dist_counts[z] for z in z_vals]
                # find local maxima
                peaks = []
                for i in range(1, len(z_vals)-1):
                    if counts[i] > counts[i-1] and counts[i] > counts[i+1]:
                        peaks.append((z_vals[i], counts[i]))
                if len(peaks) < 2:
                    continue
                # check at least two peaks within the target ranges
                in_ranges = [p for p in peaks if any(r[0] <= p[0] <= r[1] for r in peak_ranges)]
                if len(in_ranges) < 2:
                    continue
                # trough depth: minimum count between the two extreme peaks
                peak_z_sorted = sorted([p[0] for p in in_ranges])
                if len(peak_z_sorted) < 2:
                    continue
                z1, z2 = peak_z_sorted[0], peak_z_sorted[-1]
                mid_z = [z for z in z_vals if z1 <= z <= z2]
                if not mid_z:
                    continue
                mid_min = min([dist_counts[z] for z in mid_z])
                peak_heights = [dist_counts[p[0]] for p in in_ranges]
                min_peak = min(peak_heights)
                if mid_min < trough_fac * min_peak:
                    passes += 1
        if total == 0:
            return 0.0
        return passes / total

    return spatial_score(artifact, step, ctx)


# === block: score_1 (check id='size_distribution') ===
def score_1(artifact, step, ctx):
    def size_score(artifact, step, ctx):
        groups = {}
        for r in artifact:
            b = float(r['B_ratio'])
            sz = int(r['size'])
            cnt = int(r['count'])
            if b not in groups:
                groups[b] = []
            groups[b].append((sz, cnt))
        def compute_median(pairs):
            # pairs: list of (size, count)
            total = sum(c for _, c in pairs)
            if total == 0:
                return None
            half = total / 2
            cum = 0
            for sz, cnt in sorted(pairs):
                cum += cnt
                if cum >= half:
                    return sz
            return None
        bs = [0.0, 0.1, 0.3, 0.5]
        medians = {}
        for b in bs:
            if b in groups:
                m = compute_median(groups[b])
                if m is not None:
                    medians[b] = m
        # Check monotonic non-decreasing
        comparisons = 0
        passed = 0
        sorted_bs = sorted(medians.keys())
        for i in range(len(sorted_bs)-1):
            b1 = sorted_bs[i]
            b2 = sorted_bs[i+1]
            comparisons += 1
            if medians[b1] <= medians[b2]:
                passed += 1
        if comparisons == 0:
            return 0.0
        return passed / comparisons

    return size_score(artifact, step, ctx)


# === block: score_2 (check id='order_parameters') ===
def score_2(artifact, step, ctx):
    def order_score(artifact, step, ctx):
        thresh = step['params']['abs_order_threshold']
        passed = 0
        total = 0
        for r in artifact:
            p = float(r['order_parameter'])
            total += 1
            if abs(p) < thresh:
                passed += 1
        if total == 0:
            return 0.0
        return passed / total

    return order_score(artifact, step, ctx)


# === block: score_3 (check id='melting_curve') ===
def score_3(artifact, step, ctx):
    def melting_score(artifact, step, ctx):
        groups = {}
        for r in artifact:
            b = float(r['B_ratio'])
            vf = float(r['volume_fraction_C'])
            tm = float(r['melting_temperature'])
            groups.setdefault(b, []).append((vf, tm))
        flat_thresh = step['params']['flat_range_tolerance']
        monot_tol = step['params']['monotonic_tolerance']
        bs = [0.0, 0.1, 0.3, 0.5]
        passed = 0
        total = 0
        for b in bs:
            if b not in groups:
                continue
            total += 1
            pairs = sorted(groups[b])  # sort by volume_fraction_C ascending
            tm_vals = [p[1] for p in pairs]
            if b == 0.0:
                # approximately constant
                if len(tm_vals) >= 2:
                    rng = max(tm_vals) - min(tm_vals)
                    if rng <= flat_thresh:
                        passed += 1
            else:
                # should be monotonically decreasing as vf increases (i.e., non-increasing)
                ok = True
                for i in range(len(tm_vals)-1):
                    if tm_vals[i] + monot_tol < tm_vals[i+1]:
                        ok = False
                        break
                if ok:
                    passed += 1
        if total == 0:
            return 0.0
        return passed / total

    return melting_score(artifact, step, ctx)


_SCORERS = {
    'spatial_distribution': score_0,
    'size_distribution': score_1,
    'order_parameters': score_2,
    'melting_curve': score_3,
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
