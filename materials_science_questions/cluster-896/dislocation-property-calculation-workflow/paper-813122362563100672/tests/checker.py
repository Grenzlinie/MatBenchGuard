import os
import json
import csv

# === author imports / helpers ===
import csv, json, math


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
    return {'gold': spec.get('gold', {})}


# === block: score_0 (check id='equilibrium_n_check') ===
def score_0(artifact, step, ctx):
    # artifact: list of dicts with sigma_f_normalized, Kapp_normalized, n
    points = []
    for row in artifact:
        try:
            sf = float(row.get('sigma_f_normalized', ''))
            kapp = float(row.get('Kapp_normalized', ''))
            n = float(row.get('n', ''))
            sf = round(sf, 3)
            points.append((sf, kapp, n))
        except:
            continue
    if not points:
        return 0.0

    groups = {0.001:[], 0.002:[], 0.004:[]}
    eps_sf = 0.0005
    for sf, kapp, n in points:
        for key in [0.001,0.002,0.004]:
            if abs(sf - key) <= eps_sf:
                groups[key].append((kapp, n))
                break

    # monotonic non-decreasing per sigma_f
    monotonic_ok = 0
    for key in [0.001,0.002,0.004]:
        vals = groups[key]
        if not vals:
            continue
        vals.sort(key=lambda x: x[0])
        inc = all(vals[i][1] >= vals[i-1][1] for i in range(1, len(vals)))
        if inc:
            monotonic_ok += 1
    monotonic_score = monotonic_ok / 3.0

    def linear_interp(x, y, x0, tol_out=0.05):
        """Return interpolated y at x0 using sorted lists x, y.  Out-of-range within tol_out uses the nearest endpoint; otherwise None."""
        if not x:
            return None
        if x0 <= x[0]:
            if x[0] - x0 <= tol_out:
                return y[0]
            return None
        if x0 >= x[-1]:
            if x0 - x[-1] <= tol_out:
                return y[-1]
            return None
        for i in range(len(x)-1):
            if x[i] <= x0 <= x[i+1]:
                t = (x0 - x[i]) / (x[i+1] - x[i])
                return y[i] + t * (y[i+1] - y[i])
        return None

    # pointwise match to reference values via interpolation
    ref_points = ctx['gold']['equilibrium_n_points']
    point_scores = []
    for rp in ref_points:
        sf_target = rp['sigma_f']
        kapp_target = rp['Kapp']
        n_ref = rp['n']
        if sf_target not in groups:
            point_scores.append(0.0)
            continue
        vals = groups[sf_target]
        if not vals:
            point_scores.append(0.0)
            continue
        vals.sort(key=lambda x: x[0])
        kapp_arr = [v[0] for v in vals]
        n_arr = [v[1] for v in vals]
        n_interp = linear_interp(kapp_arr, n_arr, kapp_target, tol_out=0.05)
        if n_interp is None:
            point_scores.append(0.0)
            continue
        diff_n = abs(n_interp - n_ref)
        if diff_n <= 1:
            point_scores.append(1.0)
        elif diff_n <= 2:
            point_scores.append(0.5)
        else:
            point_scores.append(0.0)
    pointwise_score = sum(point_scores) / len(point_scores) if point_scores else 0.0

    # integer check
    int_count = sum(1 for row in artifact if isinstance(row.get('n'), int) or (isinstance(row.get('n'), float) and row.get('n').is_integer()))
    int_score = 1.0 if int_count == len(artifact) else 0.0

    total = 0.4 * monotonic_score + 0.45 * pointwise_score + 0.15 * int_score
    return min(1.0, max(0.0, total))


# === block: score_1 (check id='stress_profiles_check') ===
def score_1(artifact, step, ctx):
    rows = artifact
    if not rows:
        return 0.0
    x = []
    s1, s2, s3 = [], [], []
    for row in rows:
        try:
            x.append(float(row['x1_b']))
            s1.append(float(row['sigma_case1']))
            s2.append(float(row['sigma_case2']))
            s3.append(float(row['sigma_case3']))
        except:
            continue
    if not x:
        return 0.0

    peaks_gold = ctx['gold']['stress_peaks']
    case_scores = []
    for case, s_arr in [(1, s1), (2, s2), (3, s3)]:
        max_val = max(s_arr)
        max_idx = s_arr.index(max_val)
        max_x = x[max_idx]
        gold = next((g for g in peaks_gold if g['case'] == case), None)
        if not gold:
            case_scores.append(0.5)
            continue
        # sigma score
        rel_err = abs(max_val - gold['peak_sigma']) / max(gold['peak_sigma'], 1e-9)
        if rel_err <= 0.15:
            sigma_s = 1.0
        else:
            sigma_s = max(0.0, 1.0 - (rel_err - 0.15) / 0.3)
        # x score
        dx = abs(max_x - gold['peak_x'])
        if dx <= 20:
            x_s = 1.0
        else:
            x_s = max(0.0, 1.0 - (dx - 20) / 40)
        case_scores.append((sigma_s + x_s) / 2.0)
    return sum(case_scores) / len(case_scores) if case_scores else 0.0


# === block: score_2 (check id='resistance_curve_check') ===
def score_2(artifact, step, ctx):
    rows = artifact
    if len(rows) < 2:
        return 0.0
    adv = []
    kapp = []
    for row in rows:
        try:
            adv.append(float(row['crack_advance_b']))
            kapp.append(float(row['Kapp_normalized']))
        except:
            continue
    if len(adv) < 2:
        return 0.0

    inc = all(kapp[i] >= kapp[i-1] for i in range(1, len(kapp)))
    monotonic_score = 1.0 if inc else 0.0

    plateau_gold = ctx['gold']['resistance_plateau_Kapp']
    last_kapp = kapp[-1]
    rel_err = abs(last_kapp - plateau_gold) / max(plateau_gold, 1e-9)
    if rel_err <= 0.10:
        plateau_score = 1.0
    else:
        plateau_score = max(0.0, 1.0 - (rel_err - 0.10) / 0.2)

    if kapp[-1] <= kapp[0]:
        monotonic_score = 0.0
    final = 0.3 * monotonic_score + 0.7 * plateau_score
    return final


_SCORERS = {
    'equilibrium_n_check': score_0,
    'stress_profiles_check': score_1,
    'resistance_curve_check': score_2,
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
