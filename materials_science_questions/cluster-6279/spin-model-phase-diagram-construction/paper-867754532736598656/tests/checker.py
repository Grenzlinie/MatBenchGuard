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
    return {}


# === block: score_0 (check id='step3_boundary_t0') ===
def score_0(artifact, step, ctx):
    rows = artifact  # list of dicts
    ref = step['reference_points']
    tol = step['tolerance']
    struct_weight = step.get('structural_weight', 0.0)
    from collections import defaultdict
    by_lambda = defaultdict(list)
    for r in rows:
        lam = r.get('Lambda', '').strip()
        try:
            gh = float(r['gH'])
            mu = float(r['mu_crit'])
            by_lambda[lam].append((gh, mu))
        except:
            pass

    def interpolate(pts, x):
        gh_vals = [p[0] for p in pts]
        mu_vals = [p[1] for p in pts]
        if x <= gh_vals[0]:
            return mu_vals[0]
        if x >= gh_vals[-1]:
            return mu_vals[-1]
        for i in range(len(gh_vals)-1):
            if gh_vals[i] <= x <= gh_vals[i+1]:
                t = (x - gh_vals[i]) / (gh_vals[i+1] - gh_vals[i])
                return mu_vals[i] + t * (mu_vals[i+1] - mu_vals[i])
        return mu_vals[-1]

    interp_scores = []
    for lam_key, lam_refs in ref.items():
        if lam_key not in by_lambda:
            interp_scores.append(0.0)
            continue
        pts = sorted(by_lambda[lam_key], key=lambda x: x[0])
        if len(pts) < 2:
            interp_scores.append(0.0)
            continue
        lam_ok = True
        for rp in lam_refs:
            mu_agent = interpolate(pts, rp['gH'])
            mu_ref = rp['mu_crit']
            if abs(mu_agent - mu_ref) > tol * max(1e-6, mu_ref):
                lam_ok = False
                break
        interp_scores.append(1.0 if lam_ok else 0.0)
    ref_score = sum(interp_scores) / max(len(interp_scores), 1)

    # monotonic check
    mono_score = 1.0
    for lam_key, pts in by_lambda.items():
        pts_sorted = sorted(pts, key=lambda x: x[0])
        for i in range(len(pts_sorted)-1):
            if pts_sorted[i+1][1] < pts_sorted[i][1] - 1e-6:
                mono_score = 0.0
                break
        if not mono_score:
            break
    if 'monotonic_increase' not in step.get('structural_checks', []):
        mono_score = 1.0
    return (1 - struct_weight) * ref_score + struct_weight * mono_score


# === block: score_1 (check id='step4_boundary_t015') ===
def score_1(artifact, step, ctx):
    rows = artifact
    ref = step['reference_points']
    tol = step['tolerance']
    struct_weight = step.get('structural_weight', 0.0)
    from collections import defaultdict
    by_lambda = defaultdict(list)
    for r in rows:
        lam = r.get('Lambda', '').strip()
        try:
            gh = float(r['gH'])
            mu = float(r['mu_crit'])
            by_lambda[lam].append((gh, mu))
        except:
            pass

    def interpolate(pts, x):
        gh_vals = [p[0] for p in pts]
        mu_vals = [p[1] for p in pts]
        if x <= gh_vals[0]:
            return mu_vals[0]
        if x >= gh_vals[-1]:
            return mu_vals[-1]
        for i in range(len(gh_vals)-1):
            if gh_vals[i] <= x <= gh_vals[i+1]:
                t = (x - gh_vals[i]) / (gh_vals[i+1] - gh_vals[i])
                return mu_vals[i] + t * (mu_vals[i+1] - mu_vals[i])
        return mu_vals[-1]

    interp_scores = []
    for lam_key, lam_refs in ref.items():
        if lam_key not in by_lambda:
            interp_scores.append(0.0)
            continue
        pts = sorted(by_lambda[lam_key], key=lambda x: x[0])
        if len(pts) < 2:
            interp_scores.append(0.0)
            continue
        lam_ok = True
        for rp in lam_refs:
            mu_agent = interpolate(pts, rp['gH'])
            mu_ref = rp['mu_crit']
            if abs(mu_agent - mu_ref) > tol * max(1e-6, mu_ref):
                lam_ok = False
                break
        interp_scores.append(1.0 if lam_ok else 0.0)
    ref_score = sum(interp_scores) / max(len(interp_scores), 1)

    mono_score = 1.0
    for lam_key, pts in by_lambda.items():
        pts_sorted = sorted(pts, key=lambda x: x[0])
        for i in range(len(pts_sorted)-1):
            if pts_sorted[i+1][1] < pts_sorted[i][1] - 1e-6:
                mono_score = 0.0
                break
        if not mono_score:
            break
    if 'monotonic_increase' not in step.get('structural_checks', []):
        mono_score = 1.0
    return (1 - struct_weight) * ref_score + struct_weight * mono_score


# === block: score_2 (check id='step5_diquark_mu04') ===
def score_2(artifact, step, ctx):
    rows = artifact
    ref = step['reference_points']
    tol = step['tolerance']
    struct_weight = step.get('structural_weight', 0.0)

    if not rows:
        return 0.0

    gH_vals = []
    columns = ['Delta_T0', 'Delta_T0.1', 'Delta_T0.15']
    by_col = {c: [] for c in columns}
    for r in rows:
        try:
            gh = float(r['gH'])
            gH_vals.append(gh)
            for c in columns:
                by_col[c].append(float(r[c]))
        except:
            pass
    if len(gH_vals) < 2:
        return 0.0
    sorted_idx = sorted(range(len(gH_vals)), key=lambda i: gH_vals[i])
    gH_sorted = [gH_vals[i] for i in sorted_idx]
    for c in columns:
        by_col[c] = [by_col[c][i] for i in sorted_idx]

    def interpolate(xs, ys, x):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + t * (ys[i+1] - ys[i])
        return ys[-1]

    all_ok = True
    for rp in ref:
        gh_ref = rp['gH']
        for c in columns:
            delta_agent = interpolate(gH_sorted, by_col[c], gh_ref)
            delta_ref = rp[c]
            if delta_ref != 0.0:
                if abs(delta_agent - delta_ref) > tol * abs(delta_ref):
                    all_ok = False
                    break
            else:
                if abs(delta_agent) > 1e-4:
                    all_ok = False
                    break
        if not all_ok:
            break
    ref_score = 1.0 if all_ok else 0.0

    # vanishing at large gH for T>0
    vanishing_ok = True
    if gH_sorted:
        max_gh = gH_sorted[-1]
        for c in ['Delta_T0.1', 'Delta_T0.15']:
            # find delta at max_gh
            idx_max = len(gH_sorted)-1
            val = by_col[c][idx_max]
            if abs(val) > 0.005:
                vanishing_ok = False
                break
        if 'vanishing_at_large_gH' not in step.get('structural_checks', []):
            vanishing_ok = True
    else:
        vanishing_ok = False
    struct_score = 1.0 if vanishing_ok else 0.0
    return (1 - struct_weight) * ref_score + struct_weight * struct_score


# === block: score_3 (check id='step6_diquark_mu08') ===
def score_3(artifact, step, ctx):
    rows = artifact
    ref = step['reference_points']
    tol = step['tolerance']
    struct_weight = step.get('structural_weight', 0.0)

    if not rows:
        return 0.0

    gH_vals = []
    columns = ['Delta_T0_Lambda0.8', 'Delta_T0_Lambda1.0', 'Delta_T0.15_Lambda0.8', 'Delta_T0.15_Lambda1.0']
    by_col = {c: [] for c in columns}
    for r in rows:
        try:
            gh = float(r['gH'])
            gH_vals.append(gh)
            for c in columns:
                by_col[c].append(float(r[c]))
        except:
            pass
    if len(gH_vals) < 2:
        return 0.0
    sorted_idx = sorted(range(len(gH_vals)), key=lambda i: gH_vals[i])
    gH_sorted = [gH_vals[i] for i in sorted_idx]
    for c in columns:
        by_col[c] = [by_col[c][i] for i in sorted_idx]

    def interpolate(xs, ys, x):
        if x <= xs[0]:
            return ys[0]
        if x >= xs[-1]:
            return ys[-1]
        for i in range(len(xs)-1):
            if xs[i] <= x <= xs[i+1]:
                t = (x - xs[i]) / (xs[i+1] - xs[i])
                return ys[i] + t * (ys[i+1] - ys[i])
        return ys[-1]

    all_ok = True
    for rp in ref:
        gh_ref = rp['gH']
        for c in columns:
            delta_agent = interpolate(gH_sorted, by_col[c], gh_ref)
            delta_ref = rp[c]
            if delta_ref != 0.0:
                if abs(delta_agent - delta_ref) > tol * abs(delta_ref):
                    all_ok = False
                    break
            else:
                if abs(delta_agent) > 1e-4:
                    all_ok = False
                    break
        if not all_ok:
            break
    ref_score = 1.0 if all_ok else 0.0

    vanishing_ok = True
    if gH_sorted:
        max_gh = gH_sorted[-1]
        for c in ['Delta_T0.15_Lambda0.8', 'Delta_T0.15_Lambda1.0']:
            idx_max = len(gH_sorted)-1
            val = by_col[c][idx_max]
            if abs(val) > 0.005:
                vanishing_ok = False
                break
        if 'vanishing_at_large_gH' not in step.get('structural_checks', []):
            vanishing_ok = True
    else:
        vanishing_ok = False
    struct_score = 1.0 if vanishing_ok else 0.0
    return (1 - struct_weight) * ref_score + struct_weight * struct_score


_SCORERS = {
    'step3_boundary_t0': score_0,
    'step4_boundary_t015': score_1,
    'step5_diquark_mu04': score_2,
    'step6_diquark_mu08': score_3,
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
